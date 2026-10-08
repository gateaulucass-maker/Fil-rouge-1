# 02 · Contenu de la partie 3 « Cadre réglementaire »

Matière pour la fiche de veille finale (leçon 1.1). Rédigé par l'agent « juriste-DPO » de l'équipe, le 8 octobre 2026.
**Fiche d'étudiants, pas un avis juridique.** Toute affirmation non vérifiée sur une source primaire porte la mention [à vérifier].

Produit visé (hypothèse) : une **tablette relationnelle** posée chez le parent (galerie photo partagée alimentée par les enfants, visio en un geste, petits messages vidéo et petits mots, trace des échanges), avec une **alerte douce** côté aidant (ex. : tablette non ouverte depuis X jours). Axe relationnel, aucune donnée de santé visée.

Ce que la veille disait déjà (codes R1 à R3 de `rendus/1-1-fiche-veille-silvertech.html`) : critères ANSM du logiciel DM, règle 11, consentement explicite et AIPD pour les données de santé, transparence AI Act au 2 août 2026, report du haut risque par le « Digital Omnibus » « à vérifier sur la source officielle ». Ce document vérifie et précise ces points.

Corrections à reporter dans la fiche :
- Le report du haut risque n'est plus une hypothèse : il est **adopté** (règlement (UE) 2026/1744, voir sujet 3).
- La source [125] dit que « les pouvoirs de sanction s'activent le 2 août 2026 » : le chapitre sur les sanctions (art. 99) s'applique depuis le **2 août 2025** (art. 113, b) ; seul l'art. 101 (amendes des fournisseurs de modèles d'IA à usage général) attend le 2 août 2026. À corriger ou à nuancer.

---

## Sujet 1 · RGPD : données de santé et données de vie quotidienne

**La règle.** Toute information sur une personne identifiable est une donnée personnelle : photos, voix, messages, horaires d'utilisation de la tablette. Les **données concernant la santé** (art. 4, 15) sont des données « sensibles » dont le traitement est **interdit par principe** (art. 9, 1), sauf exception, la principale pour nous étant le **consentement explicite** (art. 9, 2, a). La protection doit être pensée **dès la conception et par défaut** (art. 25), et une **analyse d'impact (AIPD)** est obligatoire quand le traitement est susceptible d'engendrer un risque élevé (art. 35), ce qui est le cas pour des personnes vulnérables suivies à domicile (critères CNIL : personnes vulnérables, données sensibles ou à caractère hautement personnel, suivi systématique) [liste CNIL : à vérifier, mais la logique est celle de l'art. 35]. En France, héberger des données de santé pour le compte d'un tiers impose un **hébergeur certifié HDS** (art. L1111-8 du Code de la santé publique).

**La source primaire.**
- Règlement (UE) 2016/679 (RGPD), art. 4 (15), 9, 12, 15, 20, 25, 35 : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679
- Code de la santé publique, art. L1111-8 (hébergement des données de santé) : https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006170991 [lien de section à vérifier] ; présentation officielle de la certification HDS par l'Agence du numérique en santé : https://esante.gouv.fr/labels-certifications/hebergement-des-donnees-de-sante
- CNIL, fiche « Applications mobiles en santé : les questions à se poser » (déjà dans la veille [113]) : https://www.cnil.fr/fr/applications-mobiles-en-sante-et-protection-des-donnees-personnelles-les-questions-se-poser

**L'implication pour notre produit.**
- Ce qu'on fait : on traite des **données de vie quotidienne et de relation** (photos, messages, appels, date de dernière ouverture), pas de santé. On liste chaque donnée et sa finalité (registre), on collecte le minimum, on fixe des durées de conservation, on chiffre, on prévoit l'**export complet** et la suppression (voir l'encadré Abbott). On réalise une **AIPD** malgré l'absence de données de santé, parce que le public est vulnérable et que l'alerte douce est une forme de suivi. Le **senior est la personne concernée principale** : c'est lui qui accepte l'installation, voit ce que l'aidant voit et peut couper l'alerte.
- Ce qu'on s'interdit : aucune question sur la santé, aucun champ libre « traitement / humeur / douleur », aucune analyse des photos ou des vidéos (posture, visage, voix) qui révélerait un état de santé, aucune alerte formulée en termes médicaux (« votre mère va mal »). L'alerte dit un fait (« la tablette n'a pas été ouverte depuis 3 jours »), pas un diagnostic.
- Attention, une donnée banale peut devenir une donnée de santé par déduction : la Cour de justice de l'UE lit largement la notion de donnée sensible, y compris quand elle est révélée **indirectement** (CJUE, 1er août 2022, aff. C-184/20, OT) [référence connue, texte non relu ici : à vérifier]. Une photo du parent en fauteuil roulant ou un message « je sors de l'hôpital » sont des contenus que les utilisateurs peuvent déposer : on ne les exploite pas, on ne les indexe pas, on ne les classe pas.

**Photos des petits-enfants, droit à l'image, consentement du senior (un mot).**
- Les photos de petits-enfants sont des données de **mineurs**. Le partage entre membres d'une famille relève de l'usage personnel (exemption « domestique », art. 2, 2, c RGPD), mais **pas notre service** : nous restons responsables de l'hébergement et de la sécurité (considérant 18 du RGPD) [à vérifier sur le considérant]. Concrètement : galerie fermée au cercle familial invité, aucun partage public, aucune réutilisation (ni marketing, ni entraînement d'IA), et c'est le **parent du mineur** (titulaire de l'autorité parentale) qui dépose la photo de son enfant.
- Droit à l'image : chacun a droit au respect de sa vie privée (art. 9 du Code civil) ; le droit à l'image en découle (jurisprudence) [à vérifier sur Legifrance]. Une personne photographiée doit pouvoir demander le retrait de sa photo : prévoir un bouton « retirer » simple.
- Consentement du senior : le consentement doit être **libre, spécifique, éclairé et univoque** (art. 4, 11 et art. 7). L'enfant qui achète **ne consent pas à la place** du parent. Si le parent fait l'objet d'une mesure de protection juridique (tutelle, curatelle), les règles de la mesure s'appliquent [modalités à vérifier]. Le consentement se donne sur la tablette, en clair, et se retire aussi simplement qu'il se donne (art. 7, 3).

**Le piège à éviter.** Croire qu'« on n'a pas de données de santé, donc pas de souci » : le RGPD s'applique pleinement aux photos et aux messages, et une seule fonction maladroite (humeur, rappel de médicament, analyse d'image) fait basculer en données sensibles, avec consentement explicite et hébergement HDS.

---

## Sujet 2 · Frontière bien-être / dispositif médical

**La règle.** Un logiciel est un **dispositif médical** (DM) s'il est destiné **par le fabricant** à une finalité médicale : diagnostic, prévention, surveillance, prédiction, pronostic, traitement ou atténuation d'une maladie, d'une blessure ou d'un handicap (règlement (UE) 2017/745, art. 2, 1). C'est donc la **destination déclarée** (notice, étiquetage, publicité, site web) qui compte, pas seulement la technique (art. 2, 12 : définition de la « destination »). Si un logiciel est un DM, la **règle 11** (annexe VIII) le classe le plus souvent en **classe IIa ou plus** (IIb, III selon la gravité), donc avec évaluation par un organisme notifié et marquage CE. Le considérant 19 précise qu'un logiciel destiné au **bien-être ou au mode de vie** n'est pas un DM.

**La source primaire.**
- Règlement (UE) 2017/745 (MDR), art. 2 (1) et (12), considérant 19, annexe VIII règle 11 : https://eur-lex.europa.eu/eli/reg/2017/745/oj?locale=fr (déjà dans la veille [121])
- Guide MDCG 2019-11 rév. 1 (juin 2025), qualification et classification des logiciels (non contraignant, mais référence des autorités) : https://health.ec.europa.eu/latest-updates/update-mdcg-2019-11-rev1-qualification-and-classification-software-regulation-eu-2017745-and-2025-06-17_en
- ANSM, « Le logiciel ou l'application santé relève-t-il du statut de dispositif médical ? » (critères : finalité médicale, résultat propre à un patient, action sur les données ; stocker ou transmettre ne suffit pas) (veille [119]) : https://ansm.sante.fr/documents/reference/le-logiciel-ou-lapplication-sante-que-je-vais-mettre-sur-le-marche-releve-t-il-du-statut-de-dispositif-medical-dm-ou-de-dispositif-medical-de-diagnostic-in-vitro-dm-div

**L'implication pour notre produit.**
- Ce qu'on fait : on déclare une destination **relationnelle** (« garder le lien entre un parent et ses enfants »), partout pareil : notice, site, pitch, parcours d'achat. La tablette **stocke et transmet** des photos et des messages, ce qui, selon l'ANSM, ne suffit pas à faire un DM. L'alerte douce porte sur l'**usage de la tablette**, pas sur l'état de la personne.
- Ce qu'on s'interdit : les mots « surveiller la santé », « détecter », « prévenir les chutes », « repérer le déclin cognitif », « isolement pathologique » ; tout score ou interprétation individuelle (« votre père semble moins actif, risque de dépression »). Pas de rappel de médicament dans la V1 [un simple rappel de prise relève souvent du bien-être selon les exemples MDCG, mais la frontière est fine : à vérifier dans les exemples du guide avant de l'ajouter].

**Le piège à éviter.** Le marketing : une seule phrase du type « détecte quand votre mère ne va pas bien » sur le site suffit à revendiquer une finalité médicale et à requalifier le produit en DM non conforme, sans qu'une ligne de code ait changé.

---

## Sujet 3 · AI Act (règlement (UE) 2024/1689)

**La règle.** L'AI Act classe les systèmes d'IA par niveau de risque. Sont **interdites**, entre autres, les IA qui **exploitent les vulnérabilités liées à l'âge**, au handicap ou à la situation sociale pour altérer substantiellement le comportement d'une personne d'une manière qui lui cause, ou peut lui causer, un préjudice important (art. 5, 1, b). Sont **à haut risque** les IA qui sont un composant de sécurité d'un produit déjà réglementé, dont les **dispositifs médicaux** (art. 6, 1 et annexe I), et celles listées à l'**annexe III** (art. 6, 2 : biométrie dont la reconnaissance des émotions, accès aux prestations sociales et de santé, emploi, etc.). Toute IA qui **dialogue** avec une personne doit lui dire qu'elle est une IA, sauf évidence (art. 50, 1) ; les contenus générés (images, voix, vidéo) doivent être marqués (art. 50, 2 et 4).

**La source primaire.**
- Règlement (UE) 2024/1689 (AI Act), art. 5, 6, 50, 99, 113, annexes I et III : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689 (veille [124])
- Règlement (UE) 2026/1744 du 8 juillet 2026 (« Digital Omnibus » sur l'IA), qui modifie le calendrier : https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601744 (page EUR-Lex non lisible par notre outil ; contenu lu sur le texte consolidé publié par https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/ et recoupé par plusieurs cabinets, par ex. https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act)

**Calendrier à la date du 8 octobre 2026.**

| Date | Ce qui s'applique | Statut |
|---|---|---|
| 1er août 2024 | Entrée en vigueur de l'AI Act | Confirmé (texte) |
| 2 février 2025 | Pratiques interdites (art. 5), maîtrise de l'IA (art. 4) | Confirmé (art. 113, a). L'Omnibus aurait allégé l'art. 4 [à vérifier] |
| 2 août 2025 | IA à usage général, gouvernance, sanctions (art. 99) | Confirmé (art. 113, b) |
| 2 août 2026 | Application générale, dont la **transparence de l'art. 50** | Confirmé ; l'Omnibus ne déplace pas l'art. 50, 1 (chatbot) selon les sources secondaires [à vérifier sur EUR-Lex] |
| 2 décembre 2026 | Nouvelles interdictions ajoutées par l'Omnibus (images intimes non consenties, contenus pédocriminels générés par IA) ; délai de grâce du marquage (art. 50, 2) pour les systèmes mis sur le marché avant le 2 août 2026 | Adopté (règlement 2026/1744), lu sur texte consolidé non officiel |
| 2 décembre 2027 | Haut risque **annexe III** (au lieu du 2 août 2026) | Adopté (règlement 2026/1744) |
| 2 août 2028 | Haut risque **annexe I** (IA intégrée à un produit réglementé, dont DM) (au lieu du 2 août 2027) | Adopté (règlement 2026/1744) |

Ce qui est confirmé : le règlement 2026/1744 existe, est daté du 8 juillet 2026 et est en vigueur depuis le 27 juillet 2026 (publication au Journal officiel le 24 juillet 2026 selon les cabinets [date de JO à vérifier sur EUR-Lex]). Ce qui reste incertain : le détail des autres modifications (art. 4, allègements PME), que nous n'avons pas lu dans le texte officiel.

**L'implication pour notre produit.**
- La V1 n'a **pas besoin d'IA** : une galerie, de la visio et des messages fonctionnent sans. Pas d'IA, pas d'obligation AI Act (le RGPD reste).
- Si on ajoute de l'IA (tri automatique des photos, sous-titres, résumé des messages, assistant vocal) : on affiche clairement « ceci est une IA » (art. 50, 1, en vigueur), on marque les contenus générés (art. 50, 2), on n'en fait jamais un levier de pression sur le senior (pas de relances culpabilisantes, pas de compagnon qui « réclame » de l'attention : risque art. 5, 1, b).
- Ce qu'on s'interdit : la **reconnaissance des émotions** sur les appels vidéo ou les photos (haut risque annexe III, 1, c, et données biométriques au sens du RGPD), toute IA à finalité médicale (elle serait à la fois DM et IA à haut risque via l'annexe I).

**Le piège à éviter.** Ajouter « un peu d'IA » pour faire moderne (compagnon conversationnel, détection d'humeur) : c'est ce qui ferait passer un produit simple et conforme à un produit soumis à la transparence, voire au haut risque et au droit des DM.

---

## Encadré · Cas réel : l'historique qu'on ne peut pas récupérer

**Le constat (rapporté par un membre de l'équipe).** Un médecin récupère les données d'un capteur de glycémie Abbott FreeStyle Libre via la plateforme LibreView, mais seuls les **derniers jours** d'historique sont téléchargeables.

**Ce que dit le RGPD.**
- **Art. 15, droit d'accès** : le patient peut obtenir la confirmation que ses données sont traitées et **une copie** de ces données (art. 15, 3), sans limite de période fixée par le texte.
- **Art. 20, droit à la portabilité** : pour les données qu'il a fournies, traitées sur la base du consentement ou d'un contrat et de façon automatisée, il peut les recevoir dans un **format structuré, couramment utilisé et lisible par machine**, et les faire transmettre à un autre responsable.
- **Art. 12, délai** : réponse dans **un mois**, prolongeable de deux mois si la demande est complexe, gratuitement en principe.
- **Qui décide du partage** : le **patient**. C'est lui qui connecte son compte au cabinet ou accepte l'invitation du professionnel dans LibreView [mécanisme décrit dans le brief, non relu sur la documentation Abbott : à vérifier]. Le médecin qui reçoit les données devient lui-même détenteur pour ce qu'il reçoit.

**Ce qui est vérifié et ce qui ne l'est pas.**
- Vérifié (avis Abbott France sur le règlement européen sur les données, réf. 10/25, https://www.freestyle.abbott/fr-fr/legal/data-act-notice.html) : les applications mobiles conservent les données **au moins 90 jours** ; un titulaire de compte LibreView peut **télécharger** ses données depuis libreview.com ; sur demande au service client, les données sont fournies en **CSV** (lisible dans un tableur) ; avec un compte LibreView, les données sont conservées « selon les lois locales applicables », **sans durée chiffrée**.
- Non vérifié : la **limite exacte de jours** téléchargeables par le médecin (elle tient peut-être à l'interface des rapports côté cabinet plutôt qu'à l'export patient) [à vérifier] ; les **CGU et la politique de confidentialité LibreView pour la France** : introuvables lors de notre recherche (la page https://www.libreview.com/privacy ne renvoie pas de texte lisible sans connexion), donc **durée de conservation LibreView non trouvée**.
- À noter : depuis le 12 septembre 2025, le **règlement européen sur les données** (Data Act, règlement (UE) 2023/2854) donne aussi à l'utilisateur d'un objet connecté un droit d'accès aux données que l'objet génère, et les objets mis sur le marché après le 12 septembre 2026 doivent rendre ces données accessibles dès la conception (art. 3) [dates connues, non relues sur EUR-Lex : à vérifier]. Abbott publie justement un avis à ce titre. Notre tablette, objet connecté, est concernée.

**La leçon pour nous.** L'historique appartient à la famille, pas à la plateforme. Dès la conception (art. 25) : un bouton **« tout télécharger »** pour le senior et pour chaque membre, qui exporte **toutes** les photos (fichiers d'origine, JPEG) et **tous** les messages (vidéos MP4, textes et dates en JSON ou CSV), sans limite de période, en quelques clics ; une réponse aux demandes d'accès en moins d'un mois ; une durée de conservation écrite noir sur blanc ; et, à la résiliation, un export proposé avant suppression.

---

## 5 questions probables du jury

1. **« Une tablette qui alerte l'aidant si le parent ne l'ouvre pas, ce n'est pas de la surveillance de santé ? »**
   Non, tant que l'alerte décrit un usage (« pas ouverte depuis 3 jours ») et pas un état (« il va mal »), sans interprétation ni score. Le senior est informé, voit l'alerte et peut la couper. On le documente dans l'AIPD.

2. **« Pourquoi pas d'hébergeur HDS ? »**
   Parce que nous ne traitons pas de données de santé : nous nous interdisons de les collecter et de les déduire. Si une fonction santé était ajoutée, l'hébergement HDS (art. L1111-8 CSP) et le consentement explicite (art. 9 RGPD) deviendraient obligatoires.

3. **« Qui consent : l'enfant qui paie ou le parent qui l'utilise ? »**
   Le parent, pour ses propres données : l'enfant ne peut pas consentir à sa place. Pour les photos de petits-enfants, c'est le titulaire de l'autorité parentale qui les dépose, dans un cercle familial fermé.

4. **« Et l'IA, vous en faites quoi ? »**
   Aucune dans la V1. Si on en ajoute, on l'annonce (art. 50 AI Act, en vigueur depuis le 2 août 2026) et on exclut la reconnaissance des émotions et toute finalité médicale. Le haut risque annexe III est reporté au 2 décembre 2027 par le règlement 2026/1744, mais il ne nous concerne pas si on reste sur ce périmètre.

5. **« Qu'est-ce que le cas Abbott change pour vous ? »**
   Il montre qu'un service peut respecter la forme (un export existe) tout en rendant l'historique difficile à récupérer en pratique. Nous prévoyons un export complet, sans limite de durée, dans des formats ouverts (JPEG, MP4, JSON/CSV), dès la première version.
