# Veille silver tech — règles permanentes

Pipeline de veille de la phase 1 du projet fil rouge (Ynov B2, PFR Générations Connectées).
Principe : **beaucoup d'entrées, peu de sorties**. On collecte large, on filtre sans IA, on qualifie avec IA, l'humain décide.

## Règles non négociables

- **Aucune donnée personnelle stockée** : pas d'auteur d'avis, pas de pseudo, verbatims anonymisés (ni nom, prénom, ville, âge précis, pseudo).
- **Pas de scraping** de réseaux sociaux ni de sites qui l'interdisent. Reddit uniquement via ses flux RSS publics ; Google Play en saisie manuelle.
- **Pas de reproduction d'articles** : résumés reformulés uniquement, 3 lignes maximum.
- **Le score de fiabilité est calculé par script** (`scripts/save_qualified.py` → `common.score_fiabilite`). L'IA classe et résume, elle ne note jamais la fiabilité.
- **Ne jamais inventer** une URL, un chiffre, une date ou une source. `save_qualified.py` retire ce qu'il ne retrouve pas dans la page.
- **Toute exécution est journalisée** dans la table `runs` (`scripts/run_log.py`).
- **Toute modification de règle** passe par `config/` (catalogue, sources, règles), jamais en dur dans le code.

## Commandes

- `/veille` : pipeline complet (collecte → préfiltre → qualification → rapport).
- `/revue` : décision humaine sur les éléments `a_revoir`.
- `/couverture` : couverture du catalogue, trous en évidence.
- `/export-fiche` : export Markdown des éléments validés pour la fiche de veille.

## Technique

- Python : `.venv/bin/python` (3.11+). Les scripts se lancent depuis la racine : `.venv/bin/python scripts/<script>.py`.
- Base : `DATABASE_URL` dans `.env` (Neon en production). Demander avant toute création dans Neon.
- Tests : `.venv/bin/python -m pytest -q` (aucune base nécessaire).
