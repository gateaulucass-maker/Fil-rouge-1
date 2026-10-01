"""Fonctions partagées : configuration, connexion, normalisation, score.

Les fonctions de calcul (domaines, fraîcheur, score, préfiltre) sont pures :
elles ne touchent pas la base, ce qui permet de les tester avec pytest.
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml

RACINE = Path(__file__).resolve().parent.parent
CONFIG = RACINE / "config"
AXES = ("marche", "concurrence", "usagers", "techno", "reglementaire")
AXE_PAR_PREFIXE = {"M": "marche", "C": "concurrence", "U": "usagers", "T": "techno", "R": "reglementaire"}


# ---------------------------------------------------------------- configuration

def charger_yaml(nom: str) -> dict:
    with open(CONFIG / nom, encoding="utf-8") as f:
        return yaml.safe_load(f)


def regles() -> dict:
    return charger_yaml("regles.yaml")


def sources() -> dict:
    return charger_yaml("sources.yaml")


def catalogue() -> list[dict]:
    """Catalogue aplati : [{code, axe, libelle, statut, phase_cible}]."""
    brut = charger_yaml("catalogue.yaml")
    return [
        {"code": e["code"], "axe": axe, "libelle": e["libelle"],
         "statut": e["statut"], "phase_cible": e.get("phase_cible")}
        for axe, entrees in brut.items() for e in entrees
    ]


# ---------------------------------------------------------------- base de données

def connexion():
    import psycopg
    from dotenv import load_dotenv

    load_dotenv(RACINE / ".env")
    url = os.environ.get("DATABASE_URL")
    if not url:
        sys.exit("DATABASE_URL absent : copier .env.example en .env et le remplir.")
    return psycopg.connect(url)


def lire_json_stdin():
    donnees = sys.stdin.read().strip()
    if not donnees:
        return []
    obj = json.loads(donnees)
    return obj if isinstance(obj, list) else [obj]


# ---------------------------------------------------------------- URLs et domaines

def deredirect(url: str) -> str:
    """Retire la redirection Google (google.com/url?url=... ou ?q=...)."""
    p = urlparse(url)
    if p.netloc.endswith("google.com") and p.path == "/url":
        qs = parse_qs(p.query)
        for cle in ("url", "q"):
            if qs.get(cle):
                return qs[cle][0]
    return url


def domaine(url: str) -> str:
    hote = urlparse(deredirect(url)).netloc.lower().split(":")[0]
    return hote[4:] if hote.startswith("www.") else hote


def correspond(dom: str, liste: list[str]) -> bool:
    """True si dom est un des domaines de la liste ou un de leurs sous-domaines."""
    dom = dom.lower()
    return any(dom == d or dom.endswith("." + d) for d in liste)


def autorite(dom: str, r: dict) -> int:
    d = r["domaines"]
    if correspond(dom, d["exclus"]):
        return 0
    if correspond(dom, d["officiels"]):
        return 3
    if correspond(dom, d["medias"]):
        return 2
    return 1


# ---------------------------------------------------------------- dates et texte

def mois_ecoules(publie: date | None, aujourd_hui: date | None = None) -> int | None:
    if publie is None:
        return None
    aujourd_hui = aujourd_hui or date.today()
    return (aujourd_hui.year - publie.year) * 12 + (aujourd_hui.month - publie.month)


def vers_date(valeur) -> date | None:
    if valeur is None or valeur == "":
        return None
    if isinstance(valeur, datetime):
        return valeur.date()
    if isinstance(valeur, date):
        return valeur
    if isinstance(valeur, (tuple, list)) and len(valeur) >= 3:  # struct_time de feedparser
        return date(valeur[0], valeur[1], valeur[2])
    texte = str(valeur).strip()[:10]
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(texte, fmt).date()
        except ValueError:
            pass
    return None


def sans_accents(texte: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texte) if unicodedata.category(c) != "Mn")


def titre_normalise(titre: str) -> str:
    t = sans_accents(titre.lower())
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def nettoyer_html(texte: str | None, limite: int = 600) -> str:
    if not texte:
        return ""
    t = re.sub(r"<[^>]+>", " ", texte)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t).strip()[:limite]


def retirer_pseudos(texte: str | None) -> str:
    """Retire les pseudos et e-mails (aucune donnée personnelle stockée)."""
    if not texte:
        return ""
    t = re.sub(r"submitted by\s+/?u/[\w-]+", "", texte, flags=re.I)
    t = re.sub(r"\[link\]|\[comments\]", "", t)
    t = re.sub(r"(?<![\w/])/?u/[\w-]+", "[pseudo]", t)
    t = re.sub(r"\S+@\S+\.\w+", "[e-mail]", t)
    t = re.sub(r"(?<!\w)@\w+", "[pseudo]", t)
    return re.sub(r"\s+", " ", t).strip()


def contient_mot_cle(texte: str, mots: list[str]) -> bool:
    t = " " + sans_accents(texte.lower()) + " "
    for m in mots:
        m = sans_accents(m.lower())
        # bornes de mot pour éviter « silverware » ou « chutes d'eau » partiels trop larges
        if re.search(r"(?<![a-z])" + re.escape(m), t):
            return True
    return False


# ---------------------------------------------------------------- préfiltre (sans IA)

def motif_rejet(item: dict, r: dict, titres_recents: set[str], aujourd_hui: date | None = None) -> str | None:
    """Renvoie le motif de rejet, ou None si l'élément passe le filtre.

    item : {domaine, titre, extrait, origine, code_vise, publie_le}
    """
    dom = item["domaine"]
    if correspond(dom, r["domaines"]["exclus"]):
        return "domaine_exclu"

    if item["origine"] not in r["exemptes_mots_cles"]:
        texte = f"{item.get('titre') or ''} {item.get('extrait') or ''}"
        if not contient_mot_cle(texte, r["mots_cles_inclusion"]):
            return "hors_mots_cles"

    if titre_normalise(item["titre"]) in titres_recents:
        return "doublon_titre"

    mois = mois_ecoules(vers_date(item.get("publie_le")), aujourd_hui)
    if mois is not None and mois > r["age_max"]["mois"]:
        code = item.get("code_vise") or ""
        reglementaire = code.startswith(r["age_max"]["prefixe_code_reglementaire"]) \
            or correspond(dom, r["domaines"]["officiels"])
        if not reglementaire:
            return "trop_ancien"
    return None


# ---------------------------------------------------------------- score de fiabilité

def fraicheur(publie: date | None, axe: str, aut: int, r: dict, aujourd_hui: date | None = None) -> int:
    s = r["score"]
    if axe == "reglementaire" and aut == 3:
        return s["reglementaire_officiel_fraicheur"]
    mois = mois_ecoules(publie, aujourd_hui)
    if mois is None:
        return 0
    if mois <= s["fraicheur"]["mois_2_points"]:
        return 2
    if mois <= s["fraicheur"]["mois_1_point"]:
        return 1
    return 0


def bonus_source_primaire(url_primaire: str | None, r: dict) -> int:
    if not url_primaire:
        return 0
    if correspond(domaine(url_primaire), r["domaines"]["officiels"]):
        return r["score"]["source_primaire"]["officielle"]
    return r["score"]["source_primaire"]["autre"]


def score_fiabilite(url: str, publie: date | None, axe: str, url_primaire: str | None,
                    r: dict, aujourd_hui: date | None = None) -> dict:
    """Score d'un FAIT : autorité (0-3) + fraîcheur (0-2) + source primaire (0-2)."""
    aut = autorite(domaine(url), r)
    fr = fraicheur(publie, axe, aut, r, aujourd_hui)
    sp = bonus_source_primaire(url_primaire, r)
    return {"autorite": aut, "fraicheur": fr, "bonus_source_primaire": sp,
            "score_fiabilite": aut + fr + sp}


def niveau(score: int | None, r: dict) -> str:
    if score is None:
        return "signal"
    seuils = r["score"]["seuils"]
    if score >= seuils["prioritaire"]:
        return "prioritaire"
    if score >= seuils["a_verifier"]:
        return "a_verifier"
    return "faible"


def echapper(texte) -> str:
    return html.escape("" if texte is None else str(texte), quote=True)
