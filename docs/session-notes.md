
## Logo Soly version C Tournesol (Figma, page Logo Soly, y=4800 et 6000)
- Hypothese : variante 01 (8 petales ovales encre, centre soleil), car Lucas a designe le tournesol sans choisir de variante. Alternatives : 03, 05, 04 de 1-1-soly-tournesol-variantes.html.
- Teste : 6 planches relues par capture. A verifier : lisibilite a 16 px (petales fins).

## Noms de marque (page HTML 1-1-soly-noms-de-marque.html)
- Hypothese : "fais le rendu ici" = page HTML dans interne/lucas, comme les autres rendus. 5 pistes : Kinly, Filia, Tendra, Oriel, Nidia. Disponibilite (domaine, INPI) non verifiee.

## 2026-10-30 Prototype Soly v2 (brouillon de Lucas)
Fichier : S1-2026-2027/03-outils-nocode-ia/interne/lucas/1-1-soly-prototype-interactif-v2.html (cadre + app synchronisés, 25 écrans, DA V2).
Hypothèses : cadre en Café doux (pas de brun dans la palette) ; caméra du moment du jour factice ; démo accélérée x3 ; personnages fictifs ; ligne "Alerte et mode vacances" ajoutée dans Réglages (écart vs Figma, axe 2) ; lieux et emojis retirés ; lien fictif ; placeholder texte à la place de l'illustration de l'écran 1.
Testé : rendu écran 1, aucune erreur JS au chargement, clics install/touch/sim48/moment/reset sans erreur. À vérifier : tous les écrans un à un, comparaison fine avec Figma. Rien commité.

## 2026-10-30 Prototype Soly v3 (demande : reprendre l'idée de Clément, tout cliquable)
- Hypothèse : « Et ouf sur 3 » incompréhensible, ignoré.
- Base : v2 (déjà fondée sur la version retenue de Clément : sens unique, pas d'appel, secours opt-in après 48 h). Fichier `interne/lucas/1-1-soly-prototype-interactif-v3.html`, rien modifié chez Clément.
- Ajouts v3 : sens du cadre portrait réel (réglage et installation), taille des mots à l'écran (3 niveaux), statut de livraison à l'envoi (« au mur de… » ou « quand le wifi revient »), écran 26 d'attente de validation pour les moins de 15 ans.
- Testé : clics install, portrait, taille, écrans 26 puis 24 (JS sans erreur), capture portrait OK. À vérifier : relecture visuelle des autres écrans, non commité.

### 2026-10-30 Audit et corrections v3 (Soly)
- Barre noire en haut du téléphone : cause = bannière de notification vide visible. Corrigé (cachée tant qu'inactive). Testé : captures écrans 3 et 12.
- Corrigé : retours manquants à l'installation, boutons Annuler (écrans 9, 10), bouton Terminé (écran 19), chip « Vidéo rapide » inerte retirée, alerte 48 h conditionnée à l'accord du parent, prénoms dynamiques, reset complet, habillage du cadre, tailles de texte, compteur d'écrans (25).
- Hypothèse : « Appeler Jeanne » remplacé par « Renvoyer un Soly » (règle : aucun appel).
- Testé : syntaxe JS, 105 boutons sans cible invalide, toutes les actions définies, parcours de base, reset, zéro erreur console.
- À vérifier : relecture indépendante (agent reviewer), rendu 390 px sur vrai mobile.

## Retours maquette v3 appliqués
- Retirés : sens du cadre, habillage du cadre (cadre détecté seul).
- Ajouté : écran 27 « Autoriser les photos » après le consentement (hypothèse : à cet endroit du parcours).
- Onboarding : texte court, Continuer principal, Apple/Google en petit, « J'ai déjà un compte » en lien souligné, Retour et Plus tard en liens, icônes sur lignes cliquables, lignes non cliquables en pointillé.
- Navigation : Accueil, « + » central, Profil (ancien Réglages, avec réglages du cadre). Écran 11 rattaché à l'accueil par une ligne.
- Non fait (reporté) : photo statique, rotation hebdo, albums, récaps, messagerie. Nom, logo, design system : hors périmètre.
- Testé : syntaxe JS, liens data-go, parcours 2 à 6 avec écran 27, onglets, captures 1 et 16. À vérifier : captures 2, 4, 7, 27 et largeur 390 px.
- Retours 2 : cartes d'accueil en boutons d'action (icône + Voir/Ouvrir), icônes sur les cartes Envoyer et sur les CTA, Retour en pastille avec flèche (distinct de Plus tard), « Retour aux réglages » devenu « Retour au profil ». Hypothèse : écran 22, Retour = retour au partage.

## Retours maquette v3, lot 3
- Notifications et toasts en haut du téléphone. Écran 21 : « Passer pour l'instant » en vrai bouton en bas ; écran 22 : « Retour sur l'app » mène à l'accueil (7). Carré jaune et noir retiré du titre de l'accueil.
- Nouveaux écrans 28 (Mon compte, depuis la ligne cliquable du profil) et 29 (Photos et albums : un album par semaine, tri, photos à garder toujours).
- Hypothèse : tri et albums hebdomadaires simulés dans la maquette, rien n'est envoyé ni stocké. Indicateur d'écran : numéros Figma, total de 28 écrans.

- Lot 4 : écran 9 avec « Sélectionner dans ma galerie » (vrai sélecteur de fichiers local, rien envoyé). Tous les Retour deviennent un petit lien souligné, comme « J'ai déjà un compte ».

- DA v2 avec le nouveau logo : 1-1-da-soly-logo-v2.html (interne/lucas, non poussée). Hypothèse : logo = « fenêtre à quatre » de la planche (cadre arrondi en croix, quart bas droite soleil). Six thèmes, couleurs, typo, composants. Testé : captures Chrome. À valider en équipe.
- DA v2 Figma (page DA v2) : ancien logo mot seul remplacé par le nouveau (symbole 4 quarts + mot + point) sur les 24 slides, textes slide 03 et règle « à éviter » réécrits. Non remplacés : mini autocollants, mug, avatar Instagram, noms d'app dans notifications. À valider en équipe.
- Icône d'app Figma (DA v2, slide 18) : lettre S + point remplacés par le symbole 4 quarts sur les 10 icônes (tuiles, notification, écran d'accueil), légende réécrite. Non touché : prototype HTML v3 (sur main). À valider en équipe.
- Revue finale DA v2 Figma : icône « S » de la notification (slide 23) remplacée par le symbole 4 quarts ; points soleil assombris sur sacs Pêche et Aube, mug et carte (lisibilité). Non remplacés volontairement : avatar et tuile Instagram, autocollants (mot seul). À valider en équipe.
- Fiche pitch aidants : rangée en 02-besoins/interne/lucas/2-3-fiche-pitch-aidants.html (hypothèse : leçon 2.3, guides d'entretien). Le pitch produit passe APRÈS les questions (règle du guide : le marché, pas le produit). Prix non fixé, dit tel quel. Modèle visuel : fiches 2-4 et 2-5 de Camille (fond blanc et bleu, rail et numéro géant), avec onglets, objections dépliables et boutons Copier ajoutés. Synthèse 2-5 : section Enfants remplie avec l entretien d essai (proche de l enquêteur, hors des 5) et section 04 qui croise petit-enfant, enfant et grand-parent.
- Fiche pitch aidants : restylée en style suisse bleu et blanc (Archivo, IBM Plex Mono, #1f3fbf), comme 2-3-guides-entretien.
- Fiche pitch aidants : refaite sur le modèle interactif de la fiche de veille finale de Camille (nav fixe, onglets canal/durée, cartes objections, boutons Copier). Hypothèse : c'est la fiche visée par Lucas.
