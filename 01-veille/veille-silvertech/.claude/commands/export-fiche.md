---
description: Export Markdown des éléments validés pour la fiche de veille
---

**Avant tout**, place-toi dans le dossier du pipeline (cela marche où que Claude ait été lancé dans le dépôt) :
`cd "$(git rev-parse --show-toplevel)/01-veille/veille-silvertech"`

1. `.venv/bin/python scripts/export_fiche.py > rapports/fiche-veille.md`
2. Montre le nombre d'éléments exportés par axe et le nombre de références dans la bibliographie.
3. Rappelle que seuls les éléments **validés par un humain** sont exportés : s'il y en a peu, suggérer `/revue`.
