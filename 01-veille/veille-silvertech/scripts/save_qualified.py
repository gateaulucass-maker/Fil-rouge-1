"""Enregistre les qualifications de l'agent dans veille_items et calcule le score.

Entrée (stdin) : liste JSON produite par l'agent qualificateur, un objet par élément :
  raw_id, pertinent, flux, axe, code_info, titre, resume, pourquoi_important,
  pertinence_proposee, source_primaire_url, chiffres, archetype, ethique, sensible,
  irritant, verbatim

Garde-fous appliqués ici (pas par l'IA) :
- le score de fiabilité est calculé par script ;
- une source primaire ou un chiffre absent de la page source est retiré ;
- le verbatim est tronqué à 300 caractères et nettoyé des e-mails et @pseudos.
"""
import json
import re
import urllib.request

from common import (AXES, catalogue, connexion, deredirect, lire_json_stdin, nettoyer_html, regles,
                    score_fiabilite, sans_accents)

IRRITANTS = {"stigmatisation", "complexite", "fausses_alertes", "prix_abonnement",
             "intrusion_vie_privee", "fiabilite_technique", "service_client", "autre"}
ARCHETYPES = {"securite", "capteurs", "sante_quotidien", "compagnon", "transverse"}


def telecharger(url: str) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (veille-silvertech)"})
        with urllib.request.urlopen(req, timeout=15) as rep:
            return rep.read(3_000_000).decode("utf-8", errors="replace")
    except Exception:
        return None


def _norm_nombres(texte: str) -> str:
    t = sans_accents(texte.lower()).replace(" ", "").replace("\xa0", "")
    t = re.sub(r"(?<=\d)[ .](?=\d{3}\b)", "", t)  # 1 200 000 / 1.200.000 -> 1200000
    return t.replace(",", ".")


def chiffre_present(valeur: str, page: str) -> bool:
    """Chaque nombre de la valeur doit figurer dans la page."""
    nombres = re.findall(r"\d+(?:\.\d+)?", _norm_nombres(str(valeur)))
    if not nombres:
        return False
    texte = _norm_nombres(page)
    return all(re.search(r"(?<![\d.])" + re.escape(n) + r"(?![\d])", texte) for n in nombres)


def anonymiser(verbatim: str | None) -> str | None:
    if not verbatim:
        return None
    v = re.sub(r"\S+@\S+", "[…]", verbatim)
    v = re.sub(r"@\w+", "[…]", v)
    v = re.sub(r"\bu/\w+", "[…]", v)
    return v.strip()[:300] or None


def verifier(q: dict, raw: dict) -> tuple[dict, list[str]]:
    """Retire de q ce qui n'est pas vérifiable dans la source. Renvoie (q, notes)."""
    notes = []
    page = None
    if raw["origine"] != "avis_app":
        page = telecharger(raw["url"])
    texte_ref = nettoyer_html(page, 10**7) if page else (raw["extrait"] or "")
    html_ref = page or (raw["extrait"] or "")
    if page is None and raw["origine"] != "avis_app":
        notes.append("page non téléchargeable : vérification sur l'extrait")

    sp = q.get("source_primaire_url")
    if sp:
        sp = deredirect(sp)
        if sp.rstrip("/") not in html_ref and sp.split("://", 1)[-1].rstrip("/") not in html_ref:
            notes.append(f"source primaire retirée (absente de la page) : {sp}")
            sp = None
    q["source_primaire_url"] = sp

    gardes = []
    for c in q.get("chiffres") or []:
        if isinstance(c, dict) and c.get("valeur") and c.get("source_citee") \
                and chiffre_present(c["valeur"], texte_ref):
            gardes.append({"valeur": str(c["valeur"]), "contexte": c.get("contexte", ""),
                           "source_citee": c["source_citee"]})
        else:
            notes.append(f"chiffre retiré (non retrouvé ou sans source) : {c.get('valeur') if isinstance(c, dict) else c}")
    q["chiffres"] = gardes
    return q, notes


def main():
    r = regles()
    entrees = lire_json_stdin()
    codes = {c["code"] for c in catalogue()}
    bilan = {"qualifies": 0, "hors_sujet": 0, "ignores": 0, "corrections": 0}
    with connexion() as cx:
        for q in entrees:
            ligne = cx.execute(
                "SELECT id, url, source_nom, publie_le, origine, extrait, code_vise, etat FROM raw_items WHERE id = %s",
                (q.get("raw_id"),)).fetchone()
            if not ligne or ligne[7] != "a_qualifier":
                bilan["ignores"] += 1
                continue
            raw = dict(zip(("id", "url", "source_nom", "publie_le", "origine", "extrait", "code_vise", "etat"), ligne))

            code = q.get("code_info") if q.get("code_info") in codes else raw["code_vise"]
            axe = q.get("axe") if q.get("axe") in AXES else None
            if code and not axe:
                axe = {"M": "marche", "C": "concurrence", "U": "usagers", "T": "techno", "R": "reglementaire"}.get(code[0])

            if not q.get("pertinent", True) or not axe:
                cx.execute("UPDATE raw_items SET etat = 'qualifie', motif_filtre = 'hors_sujet_ia' WHERE id = %s",
                           (raw["id"],))
                if axe:
                    cx.execute(
                        """INSERT INTO veille_items (raw_id, titre, publie_le, source_nom, url, axe, flux, statut, resume)
                           VALUES (%s, %s, %s, %s, %s, %s, 'fait', 'hors_sujet', %s) ON CONFLICT (raw_id) DO NOTHING""",
                        (raw["id"], (q.get("titre") or "hors sujet")[:300], raw["publie_le"], raw["source_nom"],
                         raw["url"], axe, q.get("resume")))
                bilan["hors_sujet"] += 1
                cx.commit()
                continue

            q, notes = verifier(q, raw)
            bilan["corrections"] += sum(1 for n in notes if "retiré" in n)
            flux = q.get("flux") if q.get("flux") in ("fait", "signal") else "fait"
            if flux == "fait":
                sc = score_fiabilite(raw["url"], raw["publie_le"], axe, q["source_primaire_url"], r)
            else:
                sc = {"autorite": None, "fraicheur": None, "bonus_source_primaire": None, "score_fiabilite": None}

            pp = q.get("pertinence_proposee")
            cx.execute(
                """INSERT INTO veille_items
                   (raw_id, titre, publie_le, source_nom, url, axe, resume, pourquoi_important, pertinence_proposee,
                    code_info, flux, score_fiabilite, autorite, fraicheur, bonus_source_primaire, source_primaire_url,
                    chiffres, archetype, ethique, sensible, irritant, verbatim, commentaire)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                   ON CONFLICT (raw_id) DO NOTHING""",
                (raw["id"], (q.get("titre") or "")[:300], raw["publie_le"], raw["source_nom"], raw["url"], axe,
                 q.get("resume"), q.get("pourquoi_important"), pp if pp in (1, 2, 3) else None,
                 code, flux, sc["score_fiabilite"], sc["autorite"], sc["fraicheur"], sc["bonus_source_primaire"],
                 q["source_primaire_url"], json.dumps(q["chiffres"], ensure_ascii=False),
                 q.get("archetype") if q.get("archetype") in ARCHETYPES else None,
                 bool(q.get("ethique")), bool(q.get("sensible")),
                 q.get("irritant") if flux == "signal" and q.get("irritant") in IRRITANTS else None,
                 anonymiser(q.get("verbatim")) if flux == "signal" else None,
                 ("[vérif. auto] " + " | ".join(notes)) if notes else None))
            cx.execute("UPDATE raw_items SET etat = 'qualifie' WHERE id = %s", (raw["id"],))
            cx.commit()
            bilan["qualifies"] += 1
    print(json.dumps(bilan, ensure_ascii=False))


if __name__ == "__main__":
    main()
