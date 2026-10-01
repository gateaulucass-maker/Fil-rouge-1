---
description: Revue humaine des éléments à revoir (valider / rejeter)
argument-hint: "[axe] — optionnel : marche, concurrence, usagers, techno, reglementaire"
---

Aide l'utilisateur à faire la revue humaine de la veille.

1. Demande le **prénom** de la personne qui fait la revue (il sera enregistré dans `valide_par`).
2. `.venv/bin/python scripts/review.py liste` (ajoute `--axe $ARGUMENTS` si un axe est donné). Présente les éléments par axe, du score le plus haut au plus bas, par paquets de 5 : id, titre, score, résumé, pourquoi c'est important, badges sensible / éthique.
3. Pour chaque élément, l'utilisateur décide :
   - valider avec une pertinence finale 1-3 → `.venv/bin/python scripts/review.py valider <id> --pertinence <1-3> --par <prénom>` ;
   - rejeter → `.venv/bin/python scripts/review.py rejeter <id> --par <prénom> --commentaire "<motif>"`.
   Tu peux proposer une décision, mais c'est l'humain qui tranche. N'exécute rien sans sa réponse.
4. À la fin, lance `.venv/bin/python scripts/coverage.py` et rappelle les trous restants.

Astuce pour l'équipe : sans Claude, `.venv/bin/python scripts/review.py interactif --par <prénom>` fait la même chose au clavier.
