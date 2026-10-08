# 00 · Brief : dossier final de la phase 1 (fiche de veille « Marché & réglementation silver tech »)

Membre : Camille · Leçon 1.1 (bloc 01-veille) · Rédigé par l'orchestrateur.

## La demande
Un **HTML final, complet, visuel et cliquable**, qui deviendra peut-être un PDF. Il sert de support écrit et de support d'oral (15 min de présentation, puis questions jusqu'à 45 min). Il doit **finir sur le produit** que l'équipe envisage.

## Le sujet (cadrage du formateur, résumé fidèle ; texte complet hors dépôt : `~/Fil-rouge-equipe/sujet-pfr-s1.txt`)
- Question du projet : « Comment un objet connecté peut-il rassurer les enfants sans placer leurs parents sous surveillance ? »
- Question centrale de la phase 1 : « Que nous apprend le marché de la silver tech sur ce qui fonctionne réellement auprès des seniors et de leurs enfants ? »
- 4 familles d'archétypes : sécurité et urgence ; capteurs de domicile ; santé du quotidien (bien-être, jamais dispositif médical) ; objets compagnons (cadre photo connecté, enceinte simplifiée, messagerie familiale).
- Produit à trois faces : parcours d'achat (enfant), face senior, face aidant. Hardware simulé par un générateur d'événements, aucune donnée réelle de santé.
- Règle du MVP (phase 4) : un événement simulé côté objet doit déclencher une alerte visible et actionnable côté aidant. **Notre produit relationnel doit donc prévoir une chaîne événement → alerte douce** (ex. : la tablette n'a pas été ouverte depuis X jours, un message sans réponse).
- Livrable phase 1 : fiche de 4 à 6 pages, dispositif de veille en annexe. Critères : diversité et fiabilité des sources, compréhension du marché, exactitude réglementaire, esprit critique face aux promesses, utilité pour la suite.
- Grille commune : qualité 40, cohérence 20, justification des choix 15, éthique et conformité 15, posture 10. **Encadré « qui a fait quoi » obligatoire.** Usage de l'IA déclaré.
- Positionnement imposé : bien-être et lien familial, aucune revendication de dispositif médical, aucune promesse de sécurité absolue.

## Le plan imposé par le membre (5 pages)
1. **Méthode et périmètre** (½ page) : ce qu'on a observé, comment, sur quelle période.
2. **Panorama du marché** (2 pages) : tableau des acteurs selon les 4 familles (acteur, promesse, prix, cible) ; tableau des modèles économiques (achat, abonnement, hybride : avantages et limites) ; 2 réussites et 2 échecs avec hypothèse d'explication ; une ligne de clôture « Ce que ça implique pour nous ».
3. **Cadre réglementaire** (1,5 page) : RGPD et données de santé, frontière bien-être / dispositif médical, AI Act. Pour chacun : la règle, la source primaire, l'implication pour notre produit.
4. **Synthèse pour le projet** (1 page) : 3 opportunités et 3 menaces, chacune reliée à un fait de la veille ; 2 pistes de positionnement avec un premier archétype.

Plus, demandé par le membre :
- **Annexes** : dispositif de veille (sources, outils, fréquence) ; la **fiche d'automatisation** de Lucas (on la présente et on y renvoie, on ne la réécrit pas : `interne/lucas/1-1-fiche-automatisation-veille.html`) ; le **CLAUDE.md** de l'équipe présenté comme méthode de travail avec l'IA (annexe) ; la **carte mentale** si elle existe dans le dépôt (sinon un emplacement prévu, pas d'invention).
- **Fin du document : le produit et nos prévisions**, reliés aux problèmes listés.

## Le produit envisagé (hypothèse, pas encore décidé)
Famille « objets compagnons ». Une **tablette posée** (format assez grand) chez le parent : une **galerie photo partagée** entre enfants et parent, alimentée par les enfants au fil de la journée, de façon très simple et ludique ; **appels vidéo** en un geste ; **petits messages vidéo** (type Loom) et petits mots ; toujours une trace des échanges. Axe **relationnel**, pour éviter les données de santé. À rapprocher de l'idée « Le Cadre » de Clément (`interne/clement/idee-produit-le-cadre.html`) et de « La Fenêtre » de Lucas (`interne/lucas/1-1-idee-produit-la-fenetre.html`) : montrer la convergence, ne pas trancher à la place de l'équipe.

## Un constat utilisateur à intégrer (partie 3, encadré)
Un médecin peut récupérer des données d'un capteur de glycémie (Abbott FreeStyle Libre / LibreView), mais seuls les derniers jours d'historique sont téléchargeables. Lecture RGPD : art. 15 (droit d'accès, copie des données traitées), art. 20 (portabilité, format structuré, couramment utilisé, lisible par machine), délai d'un mois (art. 12). Le partage avec le médecin est décidé par le patient (invitation ou identifiant de cabinet dans LibreView). Non vérifié : la durée exacte de la limite et les CGU françaises d'Abbott → le dire. Leçon pour nous : prévoir l'export complet des échanges (photos, messages) dès la conception.

## Design (demandé par le membre)
Style **suisse** : grille stricte, grosse hiérarchie typographique, gros titres, beaucoup d'air, alignements à gauche. Couleurs : **fond crème / beige clair**, **bleu identitaire** en couleur secondaire. Cohérence avec les rendus existants de l'équipe (crème, bleu, Archivo, IBM Plex Mono, grille à rail) : partir de leur charte. Cliquable : navigation par sections, détails dépliables pour aller plus loin, liens vers les rendus sources. Imprimable proprement (feuille de style d'impression, pour un futur PDF).

## Sources (seule matière autorisée, ne rien inventer)
- `rendus/1-1-fiche-veille-silvertech.html` (le livrable actuel de la veille, 130 sources)
- `rendus/2-1-analyse-marche-questions-1-5.html`, `rendus/2-1-question-1-acteurs.html`, `rendus/1-1-apple-watch-vs-famileo.html`, `rendus/1-1-process-veille.html`
- `interne/lucas/1-1-reussites-faillites-silvertech.html`, `1-1-synthese-axe-produit.html`, `1-1-fiche-automatisation-veille.html`, `1-1-idee-produit-la-fenetre.html`, `2-1-question-1-detail-par-segment.html`, `1-1-retour-pipeline-veille.html`
- `interne/clement/idee-produit-le-cadre.html`
- `interne/commun/veille-silvertech/` (docs/dispositif-veille.md, rapports/)
- `CLAUDE.md`, `.claude/`

## Contraintes
Dépôt public : aucune donnée personnelle, aucun secret, aucune coordonnée. Chaque chiffre renvoie à une source de la veille. Fichier final < 2 Mo, autonome. Nom final : `1-1-fiche-veille-finale.html` dans `interne/camille/` (le passage en `rendus/` se fera après validation de l'équipe).
