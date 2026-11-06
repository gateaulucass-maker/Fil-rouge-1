# Notes de session (Lucas)

## 2026-11-05 : maquette interactive v4
- Hypothèse : « reprendre la maquette » = nouvelle version v4, la v3 reste intacte.
- Hypothèse : notes rangées ici car le dépôt interdit tout nouveau fichier à la racine.
- Fait : logo DA v2 (4 quarts, point soleil), texte 14 px minimum, statut de livraison affiché sur l'accueil.
- Fait : pages de rendu régénérées sur la v4. Axes « Ouvert dans Figma » laissés en questions ouvertes.

## 2026-11-05 : section 05 du rendu no-code
- Hypothèse : « l'audit de la DA » = rendu DA Soly (principes, logo, palette, typo) + les 9 axes d'audit de la maquette v4.
- Le dossier de Camille n'est pas modifié (règle du dépôt) : copie `1-1-rendu-nocode-ia-v2.html` dans interne/lucas, chemins des captures réécrits vers ../camille/.
- Section 05 ajoutée (page `#da`) : principes, logo, 8 couleurs, 2 polices, maquette v4 intégrée, 9 axes avec statut, liens vers la DA complète.

## 2026-11-05 : rendu no-code v2, DA enrichie
- Section 05 développée : principes, logo et 6 déclinaisons, construction, couleurs et lumière, typo et échelle, interface, applications, maquette, audit. 24 planches en JPG dans img-rendu-da/.
- Maquette réduite en JS (scale) pour voir cadre et téléphone entiers sans ouvrir la maquette seule.
- Hypothèse : niveau de détail entre la v2 initiale et 1-1-soly-rendu-da.html.

## 2026-11-05 : audit de la DA restylé en charte Soly
- Hypothèse : « bonne typo, bonnes couleurs, bons CTA » = charte Soly (Lexend titres et numéros, Atkinson texte, pastilles soleil/lilas/pêche avec texte encre, CTA pilule 56 px encre + contour encre).
- Même style de CTA appliqué à « Ouvrir la maquette seule » par cohérence. Classes propres (.audit, .st) pour ne pas toucher au CSS de Camille.
- Titres de toute la section 05 passés de Bricolage Grotesque à Lexend (h2, h3, h4, chiffres clés, libellés), texte en Atkinson. Le reste du rendu de Camille garde sa police.

## 2026-11-05 : tout le rendu v2 en charte Soly
- Hypothèse : « ergonomise tout » = appliquer la charte Soly à tout le document v2, pas seulement à la section 05. Le fichier de Camille n'est pas modifié.
- Couche `soly-theme` : Lexend pour les titres, libellés et menu, Atkinson pour le texte (16 à 17 px). Plus de libellés en monospace majuscule. Pastilles de statut (soleil, lilas, pêche). Boutons en pilule de 56 px. Focus lilas.
- Graphiques : retenu = encre, plan B = lilas foncé #9B85D6 (le lilas #C9B8F0 est trop pâle pour une barre sur fond aube), autres = soleil. Les verdicts du tableau sont en encre ou café doux.
- Le blueprint intégré (iframe, travail de Clément) garde son propre style.

## 2026-11-06 : gabarit du résumé complet (feat/resume-template)
- Plan : textes réécrits pour les 40 fiches (contexte, justifications de 35 à 70 mots, une ligne par preuve, synthèse, comparaison), injectés dans une v4 dérivée de la version de Camille, sans toucher à son dossier.
- Ordre : Contexte, Méthode, Notation, Preuves (photo et une ligne), Synthèse puis Comparaison. Limites et coûts, et la Grille du jury, sont retirés.
- Hypothèse : la sortie est un nouveau fichier lucas/1-1-rendu-nocode-ia-v4.html. La version de Camille reste la référence tant que la v4 n'est pas validée.
