# Sources du rendu v2

Le rendu `../1-1-rendu-nocode-ia-v2.html` est généré à partir du rendu de Camille (`../../camille/1-1-rendu-nocode-ia.html`), qui n'est jamais modifié.

- `build_v2.py` : lit le rendu de Camille, ajoute la section 05 et la charte, puis écrit le v2.
- `da_section.py` : contenu et CSS de la section 05 Direction artistique.
- `soly_theme.css` : couche charte Soly appliquée à tout le document.

Pour regénérer : `python3 build_v2.py`. Une retouche faite à la main dans le HTML v2 est perdue à la génération suivante.
