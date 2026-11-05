# DA Soly : présentation HTML

Les 24 planches de la direction artistique Soly (Figma « Fil rouge B2 », page DA v2), refaites en HTML. Ouvrir `index.html` dans Chrome.

## Utilisation
- Flèches, espace, clic ou glisser : planche suivante ou précédente.
- `G` : vue d'ensemble. `L` : lecture continue. `P` : présentation. `F` : plein écran.
- Bouton PDF : export une planche par page (1920 x 1080).
- Lien direct vers une planche : `index.html#06`.

## Modifier
- Une planche = un fichier `slides/NN.html` (CSS limité à `.slide[data-s="NN"]`).
- Le gabarit commun (barre, modes, impression) est dans `_src/shell.html`.
- Après chaque modification : `python3 _src/build.py` régénère `index.html`.
- Vérifier une planche seule à 1920 x 1080 : `_src/check.sh NN /chemin/rendu.png`.

## Choix
- Compteur de page : Figma affiche « / 21 » alors que la DA compte 24 planches. Le compteur est passé à « NN / 24 ». Les étiquettes de section (« 09 · USAGE »…) restent celles de Figma.
- Polices : Lexend (titres) et Atkinson Hyperlegible (texte), chargées depuis Google Fonts.
- Aucune image : logos, mockups et dégradés sont en SVG et CSS, donc nets à toute taille.
- Approximations : dégradé gris de la boîte (planche 17) et de la mini-carte (planche 18).
- Écart mesuré avec les exports Figma : moins de 2 % de pixels différents par planche.
