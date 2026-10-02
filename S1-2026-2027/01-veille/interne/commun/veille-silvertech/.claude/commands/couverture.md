---
description: Couverture du catalogue (codes × éléments validés), trous en évidence
---

**Avant tout**, place-toi dans le dossier du pipeline (cela marche où que Claude ait été lancé dans le dépôt) :
`cd "$(git rev-parse --show-toplevel)/S1-2026-2027/01-veille/interne/commun/veille-silvertech"`

Lance `.venv/bin/python scripts/coverage.py` et présente le tableau code × nombre d'éléments validés et à revoir, par axe. Mets en évidence les **codes requis sans élément validé** (les trous) et propose, pour chacun, la requête de `config/sources.yaml` à relancer ou une source à ajouter.
