"""Tests sans base de données : score, fraîcheur, domaines, Google Alerts, préfiltre, échappement."""
from datetime import date

import pytest

from common import (retirer_pseudos, autorite, bonus_source_primaire, catalogue, correspond, deredirect, domaine, echapper,
                    fraicheur, motif_rejet, niveau, regles, score_fiabilite, titre_normalise)
from report import md_simple
from save_qualified import anonymiser, chiffre_present

R = regles()
AUJ = date(2026, 10, 1)


# --- domaines ---------------------------------------------------------------

@pytest.mark.parametrize("url,attendu", [
    ("https://www.cnil.fr/fr/x", "cnil.fr"),
    ("https://drees.solidarites-sante.gouv.fr/a", "drees.solidarites-sante.gouv.fr"),
    ("http://WWW.LeMonde.fr:443/a", "lemonde.fr"),
])
def test_domaine(url, attendu):
    assert domaine(url) == attendu


def test_correspondance_sous_domaine():
    assert correspond("drees.solidarites-sante.gouv.fr", ["gouv.fr"])
    assert correspond("gouv.fr", ["gouv.fr"])
    assert not correspond("faux-gouv.fr", ["gouv.fr"])      # pas un sous-domaine
    assert not correspond("gouv.fr.arnaque.com", ["gouv.fr"])


@pytest.mark.parametrize("dom,niv", [
    ("cnil.fr", 3), ("eur-lex.europa.eu", 3), ("pour-les-personnes-agees.gouv.fr", 3),
    ("silvereco.fr", 2), ("lesechos.fr", 2), ("blog-quelconque.com", 1), ("facebook.com", 0), ("m.facebook.com", 0),
])
def test_autorite(dom, niv):
    assert autorite(dom, R) == niv


# --- Google Alerts ------------------------------------------------------------

def test_deredirect_google_url():
    u = "https://www.google.com/url?rct=j&sa=t&url=https://www.silvereco.fr/article-1&ct=ga&cd=X"
    assert deredirect(u) == "https://www.silvereco.fr/article-1"
    assert domaine(u) == "silvereco.fr"


def test_deredirect_param_q_et_url_normale():
    assert deredirect("https://www.google.com/url?q=https://a.fr/b") == "https://a.fr/b"
    assert deredirect("https://a.fr/b?url=x") == "https://a.fr/b?url=x"


# --- fraîcheur et score -----------------------------------------------------

@pytest.mark.parametrize("publie,points", [
    (date(2026, 3, 1), 2), (date(2025, 10, 1), 2), (date(2025, 6, 1), 1), (date(2024, 1, 1), 0), (None, 0),
])
def test_fraicheur(publie, points):
    assert fraicheur(publie, "marche", 2, R, AUJ) == points


def test_fraicheur_reglementaire_officiel():
    assert fraicheur(date(2016, 4, 27), "reglementaire", 3, R, AUJ) == 2   # texte officiel
    assert fraicheur(date(2016, 4, 27), "reglementaire", 2, R, AUJ) == 0   # média sur un vieux texte


def test_source_primaire():
    assert bonus_source_primaire(None, R) == 0
    assert bonus_source_primaire("https://www.insee.fr/fr/statistiques/1", R) == 2
    assert bonus_source_primaire("https://www.etude-privee.com/x", R) == 1


def test_score_maximal_et_minimal():
    s = score_fiabilite("https://www.insee.fr/a", date(2026, 6, 1), "marche", "https://drees.solidarites-sante.gouv.fr/x", R, AUJ)
    assert s == {"autorite": 3, "fraicheur": 2, "bonus_source_primaire": 2, "score_fiabilite": 7}
    s = score_fiabilite("https://www.facebook.com/a", None, "marche", None, R, AUJ)
    assert s["score_fiabilite"] == 0


def test_niveaux():
    assert niveau(5, R) == "prioritaire"
    assert niveau(4, R) == "a_verifier"
    assert niveau(2, R) == "faible"
    assert niveau(None, R) == "signal"


# --- préfiltre --------------------------------------------------------------

def item(**kw):
    base = {"domaine": "silvereco.fr", "titre": "Téléassistance : un marché en croissance", "extrait": "",
            "origine": "rss:silvereco", "code_vise": None, "publie_le": date(2026, 9, 1)}
    base.update(kw)
    return base


def test_prefiltre_retient():
    assert motif_rejet(item(), R, set(), AUJ) is None


def test_prefiltre_domaine_exclu():
    assert motif_rejet(item(domaine="instagram.com"), R, set(), AUJ) == "domaine_exclu"


def test_prefiltre_mots_cles():
    assert motif_rejet(item(titre="La French Tech lève 2 milliards"), R, set(), AUJ) == "hors_mots_cles"
    # mot-clé dans l'extrait, sans accent
    assert motif_rejet(item(titre="Nouvelle offre", extrait="pour les personnes agees"), R, set(), AUJ) is None
    # les avis d'app sont dispensés
    assert motif_rejet(item(titre="Super appli", origine="avis_app"), R, set(), AUJ) is None


def test_prefiltre_doublon_titre():
    deja = {titre_normalise("TÉLÉASSISTANCE : un marché en croissance !")}
    assert motif_rejet(item(), R, deja, AUJ) == "doublon_titre"


def test_prefiltre_trop_ancien_sauf_reglementaire():
    vieux = date(2022, 1, 1)
    assert motif_rejet(item(publie_le=vieux), R, set(), AUJ) == "trop_ancien"
    assert motif_rejet(item(publie_le=vieux, code_vise="R1"), R, set(), AUJ) is None
    assert motif_rejet(item(publie_le=vieux, domaine="legifrance.gouv.fr", titre="RGPD"), R, set(), AUJ) is None
    assert motif_rejet(item(publie_le=None), R, set(), AUJ) is None


# --- garde-fous qualification -------------------------------------------------

def test_chiffre_present():
    page = "<p>Selon l'INSEE, 1,5 million de personnes et 2 400 000 aidants, soit 21 %.</p>"
    assert chiffre_present("1,5 million", page)
    assert chiffre_present("2 400 000", page)
    assert chiffre_present("21 %", page)
    assert not chiffre_present("3,2 millions", page)
    assert not chiffre_present("beaucoup", page)


def test_anonymiser():
    v = anonymiser("Écrit par @jean_dupont, contact jean@mail.fr, vu sur u/pseudo42 " + "x" * 400)
    assert "@jean" not in v and "jean@mail.fr" not in v and "pseudo42" not in v
    assert len(v) <= 300


# --- échappement HTML ---------------------------------------------------------

def test_echappement():
    assert echapper('<script>alert("x")</script>') == "&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;"
    assert echapper(None) == ""


def test_markdown_echappe():
    h = md_simple("## Titre <b>\n- point **fort** <img src=x onerror=1>\ntexte")
    assert "<img" not in h and "&lt;img" in h
    assert "<b>fort</b>" in h and "<h4>" in h


# --- catalogue ----------------------------------------------------------------

def test_catalogue_complet():
    c = catalogue()
    codes = [x["code"] for x in c]
    assert len(codes) == len(set(codes)) == 32
    assert sum(1 for x in c if x["statut"] == "requis") == 13


def test_retirer_pseudos_reddit():
    t = retirer_pseudos("Ma mère refuse le bracelet. submitted by /u/EdwardBliss [link] [comments]")
    assert t == "Ma mère refuse le bracelet."
    assert "Bob_12" not in retirer_pseudos("merci u/Bob_12 et @bob, écrire à bob@mail.fr")


def test_organismes_publics_ajoutes():
    assert autorite("ameli.fr", R) == 3
    assert autorite("affairesjuridiques.aphp.fr", R) == 3
    assert autorite("korii.slate.fr", R) == 2
    assert autorite("bigmedia.bpifrance.fr", R) == 2
