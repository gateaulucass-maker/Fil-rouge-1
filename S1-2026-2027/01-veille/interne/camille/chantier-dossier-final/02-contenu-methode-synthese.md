# 02 · Contenu : méthode, synthèse, produit et prévisions, annexes, questions du jury

Matière rédigée pour le dossier final (leçon 1.1). Sert à l'intégrateur HTML. Chaque chiffre porte sa source. Convention : « réf. N » = numéro de la bibliographie de `rendus/1-1-fiche-veille-silvertech.html` (130 sources) ; « synthèse axe » = `interne/lucas/1-1-synthese-axe-produit.html` ; « fiche auto » = `interne/lucas/1-1-fiche-automatisation-veille.html`. Marqueurs : **[prouvé]** lu dans une source, **[hypothèse]** déduction de l'équipe, **[à confirmer]** à valider par l'équipe.

---

## A. Méthode et périmètre (½ page)

**Ce qu'on a observé.** Le marché des objets connectés pour seniors achetés par leurs enfants aidants, en quatre axes : marché, concurrence, technologie, réglementaire (la fiche regroupe aussi usagers et signaux). Question de la phase 1 : « Que nous apprend le marché de la silver tech sur ce qui fonctionne réellement auprès des seniors et de leurs enfants ? » (brief).

**Comment.**
- **Un pipeline lancé à la main (1er octobre 2026)** : collecte (flux RSS, avis App Store, recherche web ciblée), filtre sans IA (domaine exclu, hors mots-clés, doublon, plus de 36 mois), qualification par un agent IA, score de fiabilité sur 7 calculé par script (autorité 0-3, fraîcheur 0-2, source primaire 0-2), revue humaine. Premier run : 284 éléments collectés, 89 filtrés sans IA, 180 qualifiés, 130 validés pour la fiche (fiche, section « Méthode et limites » ; `rapports/synthese-2026-S40.md`).
- **Une veille du jeudi (depuis le 2 octobre)** : programmée à 7h45 sur le Mac de Lucas, elle cherche ce qui est nouveau, fait une **double relecture** (Claude rédige la fiche, puis un second agent qui ne l'a pas vue rouvre la source et confirme date, chiffres et résumé), publie une page et envoie un e-mail. Elle a produit 15 fiches en 3 exécutions réussies ou partielles (fiche auto, section 07).
- **Un humain décide** : rien n'entre dans la fiche sans validation de l'équipe pour le pipeline ; pour la veille du jeudi, la validation humaine n'est pas encore systématique (fiche auto, section 09).
- **Règles anti-invention** : un script retélécharge la page et retire tout chiffre ou lien absent de la source (5 chiffres retirés au premier run, `1-1-retour-pipeline-veille.html`) ; pas de date, pas de fiche.

**Période exacte.** Collecte de base : **1er octobre 2026** (premier commit du dépôt le 2026-10-01, `git log`). Veille du jeudi : essais les 2 et 6 octobre, premier jeudi réel le **8 octobre 2026** (fiche auto, section 07 ; `git log`). La fenêtre de la fiche de veille va donc du 1er au 8 octobre 2026 ; le dossier est écrit à cette date. Chaque information doit avoir moins de 12 mois, sauf deux exceptions : dernière édition d'une statistique officielle (Insee, Drees) et texte de loi en vigueur (process de veille).

**Nombre de sources.**
- **130 sources** validées et numérotées dans la bibliographie de la fiche de veille (fiche, bibliographie).
- **40 sources suivies en continu** : 24 Google Alerts, 4 médias (Silvereco, Maddyness, FrenchWeb, CNIL), 3 communautés Reddit, 4 applications (Famileo, Tous FAMiliés, Life360, Signia), 5 sites officiels prioritaires (fiche auto, section 03).
- **Écarts à lever avant impression** [à confirmer] : le chiffre « 130 validés » (fiche) et « 164 validés sur 231 qualifiés » (fiche auto, qui compte les éléments ajoutés après la revue de rattrapage) ne sont pas le même instantané ; `1-1-process-veille.html` dit « 23 Google Alerts », `dispositif-veille.md` et la fiche auto disent 24 (dont une plus lue) ; r/nocode figure dans le dispositif mais est exclu de la veille du jeudi. À harmoniser ou à citer avec leur date.

**Limites honnêtes.**
1. **Fiabilité de la concurrence faible** : les éléments viennent surtout de pages commerciales ou éditoriales, fiabilité de 1 à 3 sur 7 ; les prix sont des ordres de grandeur, pas des tarifs vérifiés (fiche, limites).
2. **Chiffres anciens** : abandon des objets connectés (2014), perception de la téléassistance (2016), équipement des seniors (2019), à actualiser (fiche, limites).
3. **Signaux d'usagers non représentatifs** : 4 applications et 3 communautés Reddit anglophones ; ils éclairent des irritants, ils ne mesurent pas leur fréquence (fiche, limites).
4. **Trous prioritaires** : aucune donnée solide sur les aidants familiaux (M3) ni sur le consentement des majeurs vulnérables (R5) (fiche, limites).
5. **Le score mesure la source, pas la vérité** ; un résumé IA peut mal interpréter une page (`dispositif-veille.md`, section 6).
6. **Dépendance technique** : la veille du jeudi tourne sur un Mac personnel ; certaines pages (Reddit, Le Figaro, La Dépêche) bloquent la lecture automatique et sont écartées (fiche auto, section 09).
7. **Aucun entretien terrain à ce stade** : le positionnement est une hypothèse documentaire, pas une validation d'usage.

---

## B. Synthèse pour le projet

### B1. Trois opportunités (un fait, une source chacune)

| # | Opportunité | Fait précis | Source |
|---|---|---|---|
| O1 | **Un besoin qui grandit** | Les seniors de 60 ans et plus en perte d'autonomie passent de plus de 2 millions en 2021 à près de 2,8 millions dans les années 2050, soit environ 700 000 de plus. | DREES / Insee, fiche réf. 7 (fiabilité 5/7) |
| O2 | **Le lien sans effort est le seul produit de lien qui réussit** | Famileo : près de 14 M€ de chiffre d'affaires en 2024, 260 000 familles, rentable depuis 2020 ; l'enfant paie et alimente, le senior reçoit sans rien faire. | Synthèse axe, règle 1 (fiche « réussites et faillites ») ; reprise dans `idee-produit-le-cadre.html` |
| O3 | **Des aidants qui demandent à souffler** | 36 % des aidants à la vie quotidienne déclarent un besoin de répit, soit 2,1 millions de personnes ; 65 % chez ceux qui aident au moins cinq heures par jour. | Drees (données 2022) via Le Media Social, fiche du jeudi 8 octobre ; fiche auto, section 07 |

### B2. Trois menaces (un fait, une source chacune)

| # | Menace | Fait précis | Source |
|---|---|---|---|
| M1 | **Le senior se désintéresse d'un objet qui demande un effort** | 41 % des seniors citent le manque d'intérêt comme premier frein aux objets connectés, devant le prix (29 %). Enquête Linexio, environ 250 seniors : petit échantillon. | Fiche réf. 48 (fiabilité 2/7 environ, à nuancer) |
| M2 | **Basculer en dispositif médical sans le vouloir** | Un logiciel est un dispositif médical s'il cumule trois critères : finalité médicale, résultat propre à un patient, analyse des données ; stocker ou transmettre ne suffit pas. S'il bascule, classe IIa ou plus avec organisme notifié. | ANSM, fiche réf. 64 (fiabilité 5/7) ; réf. 65-66 |
| M3 | **La tablette senior a déjà échoué** | Ardoiz (La Poste) : 110 000 seniors équipés, jusqu'à 200 tablettes par jour pendant le Covid, puis la demande retombe et la filiale ferme. Cause « écran à apprendre » : hypothèse de l'équipe, pas un fait prouvé. | Synthèse axe, piège 3 (fiche « réussites et faillites ») |

À garder en tête, sans en faire une menace de plus : 5 à 15 % de fausses alertes pour les capteurs de chute (ANSP 2017, fiche réf. 51, fiabilité faible), et la transparence de l'AI Act s'applique depuis le 2 août 2026, sanctions jusqu'à 15 M€ ou 3 % du chiffre d'affaires (fiche réf. 68, 70).

### B3. Le trou du marché

La carte de positionnement (analyse de marché 2.1, Q4 ; fiche, section 07) montre que la sécurité demande un effort au senior (porter, recharger, stigmate : 87 % y voient un marqueur de dépendance, Senior Strategic 2016, réf. 19) et que le lien ne demande rien mais ne détecte rien. Le coin « lien + réassurance, sans effort » est presque vide ; seuls quelques capteurs ambiants occupent le coin sécurité sans effort, surtout vendus aux Ehpad (fiche, réf. 54, 18, 53). Placement qualitatif de l'équipe, non mesuré. La Q5 de l'analyse de marché formule trois « gaps » : détecter sans rien porter, des alertes rares et fiables, rassurer sans stigmatiser.

### B4. Deux pistes de positionnement

**Piste A : la tablette relationnelle (famille « objets compagnons »).**
- *Archétype* : une tablette posée chez le parent, avec galerie photo partagée alimentée par les enfants au fil de la journée, appel vidéo en un geste, petits messages vidéo et petits mots, trace de tous les échanges. Axe relationnel, aucune donnée de santé (brief).
- *Pourquoi* : elle garde le lien sans effort de Famileo (O2) en ajoutant la réponse du senior et l'image ; elle évite la frontière dispositif médical (M2).
- *Point faible à traiter en premier* : l'écran à apprendre (M3, Ardoiz). Condition : une interface réduite à un ou deux gestes, installée par la famille.

**Piste B : l'objet à un seul geste, « signe de vie par le lien » (alternative issue de la veille).**
- *Archétype* : un objet du quotidien (cadre, lampe ou petit poste), branché au secteur et connecté en 4G, qui affiche ou imprime photos et messages de la famille ; le senior répond d'un geste (« j'ai vu », « je pense à toi ») ; l'enfant reçoit un résumé simple, et une alerte douce seulement si le geste habituel n'arrive pas (synthèse axe, section 05).
- *Pourquoi* : elle répond directement à M1 et M3 (rien à apprendre, rien à porter) et reste dans le trou de la carte.
- *Point faible* : moins de valeur perçue (pas d'appel vidéo), donc un prix à justifier ; concurrents à documenter (Komp de No Isolation, cadres photo connectés, offres « signe de vie » de La Poste : synthèse axe, section 06).
- *Écartée* : les capteurs ambiants sans port (Orme, wi-fi). Ils comblent le coin sécurité sans effort, mais relèvent de la détection de chute, proche de la frontière médicale (M2), et se vendent surtout en Ehpad (réf. 54, 30 ; Domalys cité comme échec dans la synthèse axe).

### B5. Convergence avec Le Cadre (Clément) et La Fenêtre (Lucas)

Les trois idées partagent la même colonne vertébrale, sans que personne ne l'ait imposée aux autres :

| Point commun | Tablette (brief) | Le Cadre (Clément) | La Fenêtre (Lucas) |
|---|---|---|---|
| Un objet posé chez le senior, aucun port, aucune recharge | oui | oui (cadre photo) | oui (cadre) |
| La famille l'alimente, le senior reçoit | galerie photo partagée | photos envoyées par la famille | présence et live |
| Rien à apprendre | à prouver (risque Ardoiz) | un toucher pour dire bonjour | à la voix, sans écran tactile |
| Lien, pas surveillance | trace des échanges | pas de caméra ni de micro | caméra et micro : point sensible RGPD |
| Le senior garde la main | à concevoir | accepte à l'allumage, pause à volonté | bouton « muet », lumière d'écoute |
| Le parent pose les limites | à concevoir | un seul responsable, jamais les secours | à définir |
| Payeur | l'enfant | l'enfant, environ 8 €/mois (hypothèse de Clément) | l'enfant, repères Famileo 5,99 à 17,99 € par mois |

Lecture : les trois idées sont des variantes d'une même famille (objet de lien, zéro effort, enfant payeur). Le Cadre est la version la plus légère (piste B), La Fenêtre ajoute la voix et le direct, la tablette est la version la plus riche (piste A). Les différences portent sur le degré d'effort pour le senior et sur le niveau de captation (aucune / micro et caméra). **Le dossier ne tranche pas** : le choix revient à l'équipe après entretiens (voir C4).

---

## C. Le produit envisagé et nos prévisions

*Statut : hypothèse, pas encore décidé (brief). Ce chapitre termine le dossier.*

### C1. Promesse en une phrase

« Un objet posé chez votre parent qui garde la famille présente chaque jour par les photos et les messages, et qui vous prévient avec douceur quand le lien se distend, sans rien surveiller de sa santé. »

### C2. Les trois faces

| Face | Qui | Ce qu'elle fait | Garde-fou |
|---|---|---|---|
| **Achat (enfant)** | L'enfant qui offre | Parcours d'achat : comprendre ce que l'objet fait et ne fait pas, choisir l'abonnement, inviter la fratrie (cagnotte partageable, hypothèse de la synthèse axe), configurer les proches autorisés | Ce que le produit ne fait pas est dit avant l'achat (bien-être et lien, aucun dispositif médical, aucune promesse de sécurité absolue : brief) |
| **Senior** | Le parent | Voit les photos, répond d'un geste, appelle en visio, reçoit et envoie des petits messages | Il accepte lui-même à l'allumage, voit ce qui est partagé, peut mettre en pause à tout moment (Le Cadre ; synthèse axe) |
| **Aidant** | L'enfant référent | Reçoit un résumé simple et rare, voit la trace des échanges, reçoit une alerte douce actionnable, exporte tout | Notifications rares et utiles (principe 03 de la fiche) ; un seul responsable à la fois (Le Cadre) |

### C3. Chaîne événement → alerte douce (compatible avec la règle du MVP, sans santé)

Règle du MVP (phase 4, brief) : un événement simulé côté objet doit déclencher une alerte visible et actionnable côté aidant. Le hardware est simulé par un générateur d'événements ; aucune donnée réelle de santé.

1. **Événement simulé** (générateur) : « la tablette n'a pas été ouverte depuis X jours », « aucun geste de réponse depuis X jours », ou « un message est resté sans réponse depuis X jours ». Seul un fait daté est produit, jamais un état (pas de sommeil, pas de déplacement, pas de santé).
2. **Règle côté serveur** : si le seuil X est dépassé et que le senior n'a pas mis le signe en pause, une alerte est créée. X est un paramètre à fixer avec les entretiens [à confirmer].
3. **Interrogation du senior d'abord** : l'objet affiche un message doux (« Touchez l'écran pour dire bonjour à votre famille », inspiré du Cadre).
4. **Alerte douce côté aidant, si pas de réponse** : un fait daté et neutre (« Aucune ouverture depuis 3 jours. Pouvez-vous l'appeler ? »), avec une action en un geste (appeler, envoyer un petit mot). Un seul responsable alerté à la fois.
5. **Escalade limitée** : à défaut, proposer un contact local choisi par le parent. Le produit n'appelle jamais les secours (Le Cadre) et ne parle jamais de santé.
6. **Journal** : l'événement, l'alerte et la suite donnée sont tracés (exportables).

Pourquoi c'est compatible : aucune finalité médicale, aucun résultat propre à un patient, aucune analyse de donnée de santé, donc hors des trois critères cumulatifs de l'ANSM (réf. 64). Limite à dire : un silence ne prouve rien (animal, visite, voyage) ; un faux positif fatigue l'aidant (fausses alertes documentées pour les capteurs de chute : 5 à 15 %, réf. 51, source faible) ; d'où le choix d'une alerte douce et d'un seuil à tester.

### C4. Problème identifié dans la veille, réponse, statut

Statuts : **prouvé** = fait sourcé qui valide le problème ou le principe de la réponse ; **à tester** = hypothèse de l'équipe à vérifier en entretien ou avec le simulateur ; **ouvert** = pas de réponse arrêtée.

| # | Problème identifié (source) | Notre réponse | Statut |
|---|---|---|---|
| 1 | Le senior n'adopte pas ce qui demande un effort : non-port et déclenchements accidentels (réf. 45), 41 % de manque d'intérêt (réf. 48), tablette Ardoiz fermée (synthèse axe) | Rien à porter ni à recharger, branché au secteur, interface à un ou deux gestes, installation par la famille | Problème : prouvé. Réponse : **à tester** auprès de 2 ou 3 seniors (la tablette porte le risque Ardoiz) |
| 2 | La téléassistance stigmatise : 87 % y voient un marqueur de dépendance (Senior Strategic 2016, réf. 19, ancien) | Un objet de lien familial, offert, sans vocabulaire de surveillance (principe 04) | **À tester** (source de 2016, à confirmer en entretien) |
| 3 | Le lien sans effort fonctionne mais sans objet ni réponse du senior (Famileo, synthèse axe) | Galerie alimentée par les enfants, réponse d'un geste, visio, messages | Principe : **prouvé** (Famileo). Version objet connecté : **à tester** |
| 4 | L'aidant est épuisé, 36 % ont besoin de répit ; un outil qui ajoute une tâche devient une corvée (Drees via fiche du jeudi ; réf. 77, 108) | Résumé rare plutôt que flux, une seule alerte à la fois, action en un geste | Problème : **prouvé**. Réponse : **à tester** (nombre d'alertes acceptable) |
| 5 | Les fausses alertes et les bugs font perdre la confiance (5 à 15 % de fausses alertes, réf. 51 ; Life360, réf. 90, 91) | Alerte fondée sur un fait daté, seuil X réglable, interrogation du senior avant l'aidant, pause possible | **À tester** avec le simulateur d'événements (phase 4). Seuil X : **ouvert** |
| 6 | Frontière dispositif médical (3 critères cumulatifs, réf. 64) | Aucune donnée de santé, aucune analyse de patient, produit relationnel | Règle : **prouvée** (ANSM). Conformité de notre conception : à relire à chaque évolution |
| 7 | Photos, messages et visio sont des données personnelles ; le consentement du senior est central (RGPD, CNIL : réf. 58-61). Constat utilisateur du brief : chez Abbott, seuls les derniers jours d'historique sont téléchargeables (durée exacte et CGU françaises non vérifiées) | Consentement du senior à l'allumage, pause, **export complet des échanges (photos, messages)** dès la conception (art. 15 accès, art. 20 portabilité, délai d'un mois, art. 12 : brief) | Obligation : **prouvée**. Mise en œuvre : **à tester**. Cas Abbott : non vérifié |
| 8 | Qui paie et combien : repères Famileo 5,99 à 17,99 € par mois, téléassistance 20 à 50 € par mois (synthèse axe) ; 8 €/mois est une hypothèse de Clément | Abonnement payé par l'enfant, partageable entre frères et sœurs, ouverture possible aux mutuelles et services d'aide à domicile (hypothèse) | **Ouvert** (prix et canaux à tester en entretien) |

### C5. Prochaines étapes (phases 2 à 6)

Le sujet complet est hors dépôt (`~/Fil-rouge-equipe/sujet-pfr-s1.txt`). Le dépôt ne confirme que la phase 4 (MVP avec événement simulé → alerte) et mentionne des « précautions » en phase 2 (brief). **Les intitulés des phases 2, 3, 5 et 6 ci-dessous sont à reporter depuis le sujet [à confirmer]** ; le contenu proposé s'appuie sur les prochaines étapes déjà écrites par l'équipe (synthèse axe, section « Prochaines étapes » ; Le Cadre, « ce qu'il reste à prouver »).

| Phase | Ce qu'on fait pour ce produit | Livrable attendu |
|---|---|---|
| **2** [intitulé à confirmer] | 3 à 5 entretiens d'aidants (ce qui les rassure, combien ils paieraient, ce que leur parent refuserait) ; 2 ou 3 seniors face à une maquette (un objet à un geste est-il accepté ?) ; ajouter à la veille les écrans « un bouton » et cadres photo connectés | Verbatims anonymisés, décision piste A ou B |
| **3** [à confirmer] | Choisir l'objet (tablette, cadre, lampe) ; définir les parcours des trois faces ; prix et modèle économique ; textes des alertes | Parcours et maquettes des trois faces |
| **4** (MVP, brief) | Générateur d'événements, règle de seuil, alerte douce côté aidant, export complet des échanges | MVP démontrable : événement simulé → alerte visible et actionnable |
| **5** [à confirmer] | Tester le seuil X et les textes d'alerte, mesurer la charge pour l'aidant | Retours de test, corrections |
| **6** [à confirmer] | Dossier final, démonstration, bilan, usage de l'IA déclaré | Présentation et dossier |

---

## D. Annexes

### D1. Dispositif de veille (sources, outils, fréquence)

Source : `interne/commun/veille-silvertech/docs/dispositif-veille.md` et fiche auto, section 03. Le pipeline est à la main (lundi dans le dispositif écrit) ; la veille du jeudi est automatique.

| Famille | Sources | Mode | Fréquence |
|---|---|---|---|
| Google Alerts | 24 alertes (13 du catalogue créées le 01/10/2026, 11 de la veille du jeudi créées le 02/10/2026), en français, région France | Flux RSS | Relevé chaque jeudi sur 7 jours |
| Médias spécialisés | Silvereco, Maddyness, FrenchWeb | Flux RSS | Hebdomadaire |
| Régulateur | CNIL | Flux RSS | Hebdomadaire |
| Communautés | r/AgingParents, r/CaregiverSupport (validés par l'équipe le 01/10/2026, voix des aidants, anglophones) ; r/nocode au pipeline, exclu du jeudi | Flux RSS publics, verbatims anonymisés | Hebdomadaire |
| Avis d'applications | App Store : Famileo, Tous FAMiliés, Life360, Signia | Flux public Apple | Hebdomadaire |
| Avis Google Play | Fiches Play Store | Saisie manuelle (pas d'API gratuite) | Ponctuelle |
| Recherche web ciblée | 2 ou 3 requêtes par code ; sites officiels prioritaires : Insee, Drees, CNIL, ANSM, EUR-Lex, Légifrance, service-public.fr | Agent collecteur | Hebdomadaire, sur les codes sous-couverts |
| Données d'entreprises | pappers.fr, societe.com, crunchbase.com | Consultation ciblée, jamais d'extraction massive | Ponctuelle |
| Concurrents suivis (jeudi) | Famileo, Présence Verte, Vitaris, Filien, Telegrafik, La Poste, Apple Watch, ElliQ | Recherche web | Chaque jeudi |

| Outil | Rôle |
|---|---|
| Claude Code | Orchestrateur, 3 sous-agents (collecteur, qualificateur, rapporteur) et 4 commandes (`/veille`, `/revue`, `/couverture`, `/export-fiche`) |
| Python | Collecte, filtre, score, rendu (aucune API payante) |
| Neon (PostgreSQL) | Base partagée : brut, rejets avec motif, fiches, journal des exécutions |
| launchd (Mac de Lucas) | Déclenche la veille du jeudi à 7h45 |
| GitHub Pages et e-mail | Page publiée et récapitulatif à l'équipe |

| Rythme | Quoi |
|---|---|
| Une fois, 1er octobre | Pipeline de base : catalogue de 32 types d'information (13 requis) sur 5 axes |
| Chaque jeudi, 7h45 | Veille automatique : 5 à 10 fiches, double relecture, page, e-mail |
| Dans la semaine | Revue humaine, environ 20 minutes par personne (dispositif) |
| Avant un rendu | `/couverture` (trous) puis `/export-fiche` |

Écartés volontairement : Facebook, Instagram, TikTok, Pinterest, contenus sponsorisés, comparateurs sans sources. Limites : voir A.

### D2. Fiche d'automatisation (auteur : Lucas)

Renvoi, sans réécriture : [`interne/lucas/1-1-fiche-automatisation-veille.html`](../../lucas/1-1-fiche-automatisation-veille.html) (chemin relatif depuis ce fichier ; à réécrire selon l'emplacement du HTML final dans `interne/camille/`, soit `../lucas/1-1-fiche-automatisation-veille.html`).

Résumé en 5 lignes :
1. Deux machines, une même méthode : le pipeline, lancé à la main le 1er octobre, constitue la base large et notée ; la veille du jeudi, programmée à 7h45, la tient à jour.
2. Le flux : collecter (script), filtrer sans IA (script), qualifier (IA), noter (script, jamais par l'IA), relire par un second agent indépendant (IA), décider (équipe).
3. Quatre master prompts écrits et versionnés pilotent chaque étape ; l'IA ne décide pas seule de sa méthode.
4. Résultats réels : 284 collectés puis 231 qualifiés et 164 validés au premier run ; 15 fiches en 3 exécutions du jeudi (330 candidats, moins de 5 % deviennent une fiche).
5. Limites constatées : Mac à garder allumé, pages bloquées, peu de fiches sur l'acceptation, les prix et le consentement, deux tables à réunir, revue humaine encore légère.

### D3. CLAUDE.md : notre méthode de travail avec l'IA

Source : `CLAUDE.md` (racine), `AGENTS.md`, `.claude/`. L'équipe de 3 travaille chacune avec son agent IA (Claude Code) ; `CLAUDE.md` est lu au début de chaque session et `AGENTS.md` y renvoie les autres agents (Codex, ChatGPT, Cursor, Gemini).

Points clés :
1. **Dépôt public** : jamais de secret, de coordonnées de l'équipe, de donnée personnelle de tiers, de document de cours ni de fichier de plus de 2 Mo.
2. **Contrôle automatique avant commit** (`.claude/hooks/verifier-commit.sh`) : il bloque secret probable, e-mail, téléphone, `.env`, clé, PDF hors `rendus/`, fichier lourd ; l'agent n'utilise jamais `--no-verify`.
3. **Synchronisation et anti-écrasement** : `git pull` au démarrage (hook), jamais de `--force` ni de `reset --hard` sur du travail poussé ; en cas de conflit, l'agent s'arrête et demande.
4. **Qui modifie quoi** : chacun écrit dans `interne/<prénom>/` ; on ne touche pas au dossier d'un autre ; `rendus/` seulement après accord de l'équipe ; modification de `CLAUDE.md` et `AGENTS.md` validée par Camille.
5. **Rangement systématique** : semestre, bloc, leçon (l'agent demande s'il ne trouve pas le numéro, il ne devine pas), nom `X-Y-ce-que-c-est`.
6. **L'humain pousse** : l'agent ne pousse que si le membre le demande.

Garde-fous propres à la veille : l'IA ne note jamais la fiabilité (script), ne fabrique ni URL, ni chiffre, ni date ; un script retire les chiffres absents de la source ; rien n'entre sans relecture ; verbatims anonymisés, 300 caractères au plus.

**Déclaration d'usage de l'IA** (charte IA Ynov, d'après `process-veille` et `dispositif-veille.md`) : Claude (Claude Code) a servi à construire le pipeline, collecter, qualifier, résumer et faire la double relecture, et à assister la rédaction des fiches. Les scores de fiabilité sont calculés par script, la validation est humaine et signée. Ce dossier a été rédigé avec l'aide de l'IA à partir des seules sources du dépôt ; les choix de positionnement restent ceux de l'équipe. [à confirmer par l'équipe avant remise]

### D4. Carte mentale : statut

**Absente du dépôt.** Recherche faite (`grep -ri "carte mentale\|mind"` sur tout le dépôt hors `.git`) : seule occurrence, le brief de ce chantier (`00-brief.md`). Aucun fichier de carte mentale, aucune image, aucun lien. Il faut donc, soit que l'équipe fournisse la carte (fichier à déposer dans `interne/<prénom>/`), soit laisser un **emplacement prévu** dans l'annexe, libellé « Carte mentale : à fournir par l'équipe ». Ne rien inventer. La carte de positionnement (analyse 2.1, Q4) existe mais n'est pas une carte mentale : ne pas les confondre.

### D5. Qui a fait quoi (d'après le dépôt) [à confirmer par chacun]

Sources : `git log` (auteurs de commits, 1er au 8 octobre 2026) et dossiers `interne/<prénom>/`. Un commit ne dit pas qui a eu l'idée ; chacun valide sa ligne.

| Membre | Contributions repérées | Traces |
|---|---|---|
| **Clément** | Règles de travail de l'équipe (première version de `CLAUDE.md`) et hook de synchronisation ; leçon 2.1 : analyse de marché, questions 1 à 5 et carte de positionnement ; idée produit « Le Cadre » (version courte, simulateur, mise à la charte) | Commits du 02, 06 et 08/10 ; `interne/clement/idee-produit-le-cadre.html` ; `rendus/2-1-analyse-marche-questions-1-5.html` |
| **Lucas** | Pipeline de veille (collecte, filtre, qualification, score, tests) ; Google Alerts, base Neon, veille du jeudi automatisée et son audit ; page « Process de veille » ; fiche de veille HTML (130 éléments) ; analyse Apple Watch / Famileo ; question 1 (tableau acteurs) ; fiche « réussites et faillites » (16 entreprises) et synthèse axe produit ; idée « La Fenêtre » ; fiche d'automatisation ; page de suivi | Majorité des commits du 01 au 08/10 ; `interne/lucas/` ; `interne/commun/veille-silvertech/`, `veille-du-jeudi/` |
| **Camille** | Validation des règles communes `CLAUDE.md` et `AGENTS.md` (rôle écrit dans `CLAUDE.md`, section 3) ; ce dossier final (brief, plan, contenus), dans `interne/camille/chantier-dossier-final/` | **Aucun commit au nom de Camille dans le `git log` au 8 octobre** : contributions antérieures éventuelles à renseigner par l'équipe |

Remarques : des commits sont signés « Claude » (réorganisation du dépôt, réécriture de `CLAUDE.md`, suppression du dossier `02-marche`, 04 et 05/10) et « veille-hebdo-bot » (publication de la veille, 02/10) : ils relèvent de sessions d'agent lancées par un membre, dont l'identité n'est pas lisible dans l'historique [à confirmer]. Certains commits portent l'identifiant GitHub de Lucas (`gateaulucass-maker`) : même personne [à confirmer]. Le fichier `suivi/taches.json` attribue les tâches à « Claude », « Équipe d'agents » ou « Lucas » : c'est la trace de l'agent, pas d'une personne.

---

## E. Huit questions probables du jury, avec réponse courte

**1. (Marché) Le marché est-il assez grand ?**
Cela dépend du périmètre : de 60 à 130 milliards d'euros pour la « silver économie » (réf. 3, 6), mais seulement environ 250 millions d'euros pour la téléassistance (Xerfi, réf. 5), segment qui stagne en valeur (étude DGE/PIPAME, réf. 4). Le besoin grandit (de 2 à 2,8 millions de seniors en perte d'autonomie, réf. 7) ; la croissance « ne vient pas toute seule ». Nous ne chiffrons pas notre part : ce serait inventer.

**2. (Marché) Pourquoi y arriverez-vous là où d'autres ont échoué ?**
Nous évitons les causes d'échec documentées : porter et recharger (montres senior, B2C en échec, réf. 30), faire payer le senior (Coyali), affronter les géants sur la voix (Jibo, Myxyty, synthèse axe). Nous reprenons ce qui réussit : le senior ne fait rien, l'enfant paie (Famileo, près de 14 M€ de CA en 2024, 260 000 familles : synthèse axe). Reste un risque que nous nommons : Ardoiz, pour la tablette.

**3. (Produit) Pourquoi une tablette, alors que La Poste a fermé Ardoiz ?**
Nous ne l'avons pas tranché : c'est la piste A, face à la piste B (objet à un geste). Ardoiz a équipé 110 000 seniors puis la demande est retombée ; la cause « écran à apprendre » est notre hypothèse, pas un fait (synthèse axe). Notre réponse : une interface réduite à un ou deux gestes, installée par la famille, et un test auprès de 2 ou 3 seniors avant de choisir.

**4. (Produit) En quoi êtes-vous différents de Famileo, d'Echo Show ou de Familink ?**
Famileo prouve le lien sans effort mais sans objet connecté ni réponse du senior (synthèse axe). Echo Show permet déjà aux proches de se connecter et Meta a arrêté Portal (La Fenêtre) ; Familink et Livindi existent (Le Cadre). Notre différence est un assemblage et un parti pris (lien, zéro effort, alerte douce), pas une technologie : à prouver en entretien. Concurrents à ajouter à la veille.

**5. (Produit) Que se passe-t-il si le parent ne répond pas ? Appelez-vous les secours ?**
Non. Le produit interroge d'abord le parent, puis prévient un seul responsable avec un fait daté (« aucune ouverture depuis X jours »), et ne contacte jamais les secours (Le Cadre). Nous ne promettons pas de sécurité absolue (brief). Limite assumée : un silence ne prouve rien et un faux positif fatigue l'aidant (fausses alertes 5 à 15 % pour les capteurs de chute, réf. 51, source faible).

**6. (Éthique) Votre produit n'est-il pas de la surveillance déguisée ?**
La question du projet est précisément de rassurer sans placer les parents sous surveillance. Réponses : le parent accepte à l'allumage, voit ce qui est partagé et peut mettre en pause ; pas de caméra de surveillance ni de suivi de déplacements ou de santé ; l'enfant voit un fait daté, pas la pièce (Le Cadre). La Fenêtre exige un micro et une caméra : c'est un point RGPD que sa fiche liste elle-même comme risque.

**7. (Éthique et droit) Êtes-vous un dispositif médical ? Que dit le RGPD ?**
Non, parce qu'aucun des trois critères cumulatifs de l'ANSM n'est rempli : pas de finalité médicale, pas de résultat propre à un patient, pas d'analyse de données de santé (réf. 64). Photos et messages restent des données personnelles : consentement du senior, minimisation, analyse d'impact dès le prototype (réf. 58-61), export complet des échanges (droit d'accès art. 15, portabilité art. 20, délai d'un mois art. 12 : brief). Toute IA s'annoncerait comme telle (AI Act, transparence depuis le 2 août 2026, réf. 68).

**8. (Modèle économique) Qui paie, combien, et qu'est-ce qui vous empêcherait de gagner de l'argent ?**
L'enfant paie, par abonnement, comme chez Famileo (3 quarts des abonnés sont des familles, synthèse axe) ; repères 5,99 à 17,99 € par mois pour le lien, 20 à 50 € pour la téléassistance (synthèse axe). Les 8 €/mois du Cadre sont une hypothèse (Le Cadre). Nous n'avons ni prix validé ni coût matériel chiffré : c'est ouvert. Risques : trésorerie (première cause d'échec documentée : Myxyty, Coyali, Ardoiz) et le fait de faire payer le senior.

---

*Écarts de chiffres signalés en A à arbitrer avant impression. Aucune donnée personnelle ni coordonnée dans ce fichier.*
