---
description: Pipeline de veille complet (collecte, préfiltre, qualification, rapport)
argument-hint: "[plafond d'éléments à qualifier, défaut 100]"
---

**Avant tout**, place-toi dans le dossier du pipeline (cela marche où que Claude ait été lancé dans le dépôt) :
`cd "$(git rev-parse --show-toplevel)/01-veille/veille-silvertech"`

Lance le pipeline de veille complet. Plafond de qualification : $ARGUMENTS (100 si vide). Toutes les commandes depuis la racine du projet avec `.venv/bin/python`.

1. `.venv/bin/python scripts/run_log.py debut` → note l'id du run.
2. `.venv/bin/python scripts/collect_rss.py` et `.venv/bin/python scripts/collect_app_reviews.py` → note les bilans JSON (dernière ligne) et les flux en erreur.
3. Sous-agent **collecteur** sur les codes sous-couverts (codes requis en priorité).
4. `.venv/bin/python scripts/prefilter.py` → note le nombre filtré.
5. Sous-agent **qualificateur** en boucle jusqu'à épuisement ou jusqu'au plafond (`scripts/pending.py --compter` pour suivre). Plusieurs qualificateurs peuvent tourner en parallèle sur des lots disjoints.
6. Sous-agent **rapporteur** → synthèse + rapport HTML.
7. `.venv/bin/python scripts/run_log.py fin <id> --collectes '<json par origine>' --filtres N --qualifies N --hors-sujet N --notes "<flux en erreur, remarques>"`.
8. Bilan chiffré final : collectés par origine, filtrés (par motif), qualifiés, hors sujet, restant à qualifier, chemin du rapport.
