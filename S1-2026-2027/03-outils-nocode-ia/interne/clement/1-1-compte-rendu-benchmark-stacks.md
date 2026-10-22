# Compte rendu : le benchmark des stacks, du 16 au 22 octobre

PFR Générations Connectées · Bloc 03 · Leçon 1.1 · Le Cadre
Clément, 22 octobre 2026. Brouillon, à relire par Lucas avant le 24 octobre.

Ce document raconte ce qui a été fait sur le benchmark des stacks, les décisions prises en route, les résultats au 22 octobre, et ce qu'il reste à faire. Il est écrit pour quelqu'un qui n'a pas suivi le projet.

## En une page

- **La question** : avec quels outils construire Le Cadre, pour un produit qui marche, en respectant les 4 usages du cours (site vitrine qui vend, écran du cadre, appli de l'aidant, alertes) et le critère éliminatoire des données en Europe ?
- **La méthode** : 4 stacks comparées sur 7 critères pondérés plus un critère éliminatoire, puis chaque outil noté seul dans sa couche (construction, base, automatisation), avec une échelle écrite et un statut par note : testé, documenté ou estimé.
- **Le résultat** : la stack A, React + Next.js + Supabase avec les règles écrites en code, est devant avec 71 sur 100. FlutterFlow sur la même base est le plan B à 64. Glide et Softr sont éliminées : leurs données sortent d'Europe.
- **La réserve** : aucune note de stack n'est encore testée. Les tests sont prévus le 29 octobre.

## Ce qui a été fait, dans l'ordre

| Date | Document | Ce qu'il apporte |
|---|---|---|
| 15 octobre | Le Cadre, version retenue | le produit fixé : cadre au mur, appli pour l'enfant, aucune appli pour le parent, un toucher qui dit « je suis là », alerte après 48 h si le parent l'accepte |
| 16 octobre | Les 4 usages à tester | ce que chaque usage du cours veut dire pour Le Cadre, le test à rejouer sur chaque stack, les données fictives, les 3 statuts |
| 16 octobre | Benchmark des stacks | les 4 combinaisons, le tableau des 4 usages, les critères et leurs poids, une première lecture bon / moyen / bloquant, les sources, la stack A gardée à titre provisoire |
| 22 octobre | Classement des stacks | les notes chiffrées avec leur statut et leur source, le classement visuel façon vals.ai, la comparaison brique par brique, les décisions du jour |
| 22 octobre | Prompts de la boîte à outils IA | un prompt par thème pour tester les IA, grille et fiche communes |

Les pages, en ligne :

- Classement des stacks : https://gateaulucass-maker.github.io/Fil-rouge-1/S1-2026-2027/03-outils-nocode-ia/interne/clement/1-1-classement-stacks.html (version de travail : https://claude.ai/artifact/WHLSKt2jd1t2FJEi1MDjrp)
- Benchmark du 16 octobre : https://gateaulucass-maker.github.io/Fil-rouge-1/S1-2026-2027/03-outils-nocode-ia/interne/clement/1-1-benchmark-stacks.html
- Les 4 usages à tester : https://gateaulucass-maker.github.io/Fil-rouge-1/S1-2026-2027/03-outils-nocode-ia/interne/clement/1-1-quatre-usages-a-tester.html
- Version retenue : https://gateaulucass-maker.github.io/Fil-rouge-1/S1-2026-2027/03-outils-nocode-ia/interne/clement/1-1-le-cadre-version-retenue.html

## Les 4 stacks comparées

| Stack | Construction | Base | Automatisation | Statut |
|---|---|---|---|---|
| A | React (écran du cadre), Next.js (site vitrine, appli de l'aidant en PWA) | Supabase, région Europe | code dans Supabase : fonctions Edge et pg_cron | retenue, provisoire |
| D | FlutterFlow | Supabase | n8n | plan B |
| B | Glide | Glide Tables | Make | éliminée, Glide aux États-Unis |
| C | Softr | Airtable | Zapier | éliminée, Airtable et Zapier aux États-Unis |

A et D ont la même base. La différence se joue sur la construction, en code ou en no-code, et sur l'automatisation, en code ou avec n8n. Le cours demande au moins 3 combinaisons : on en compare 4.

## Les critères, les poids, l'échelle

Sept critères pondérés, qui font 100, et un critère éliminatoire.

| Critère | Poids | 5 | 3 | 1 |
|---|---|---|---|---|
| Capacités | 20 % | couvre les 4 usages sans contournement | 3 usages, le 4e avec un contournement | un seul usage |
| Interopérabilité | 20 % | webhooks gratuits et API libre | webhooks limités ou payants sur un maillon | pas de webhook sans payer |
| Affichage adapté au cadre | 15 % | plein écran, deux sens, lisible à 3 m | plein écran, un sens ou la vidéo à bricoler | téléphone seulement |
| Simplicité | 15 % | l'essai en une demi-journée sans aide | une journée avec la documentation | plusieurs jours ou compétence absente |
| Coûts | 10 % | gratuit pour la démo | moins de 25 € par mois | plusieurs abonnements |
| Limites | 10 % | rien de gênant pour 2 familles pendant un mois | une limite à surveiller | une limite atteinte en test |
| Stockage des vidéos | 10 % | plus de 5 Go | autour de 1 Go | moins de 200 Mo |
| Données en Europe | éliminatoire | oui, non, ou à vérifier | | |

Le score est la somme des notes multipliées par leur poids, ramenée sur 100. Chaque note porte un statut :

- **testé** : on l'a fait nous-mêmes, avec une capture ;
- **documenté** : une page officielle ou une source l'annonce, pas essayé ;
- **estimé** : notre lecture, sans test ni source ferme.

L'échelle est écrite avant les notes, pour que le jury puisse contester une note et pas la méthode.

## Les résultats au 22 octobre

### Les stacks complètes

| Stack | Capacités | Interop. | Affichage | Simplicité | Coûts | Limites | Vidéos | Score |
|---|---|---|---|---|---|---|---|---|
| A · React + Next.js + Supabase | 4 e | 4 d | 4 e | 3 e | 3 d | 3 d | 3 d | **71** |
| D · FlutterFlow + Supabase + n8n | 3 e | 4 d | 3 e | 3 e | 3 d | 3 d | 3 d | **64** |
| B · Glide + Make, éliminée | 2 e | 2 d | 2 e | 4 e | 3 d | 3 d | 2 e | 50 |
| C · Softr + Airtable + Zapier, éliminée | 3 e | 1 d | 2 e | 4 e | 2 d | 2 d | 3 d | 48 |

d = documenté, e = estimé. Sur les 32 notes, 19 sont documentées, 13 estimées, 0 testée. Les critères Capacités, Affichage et Simplicité sont estimés pour toutes les stacks : ce sont ceux que les tests du 29 octobre mesurent.

### Brique par brique

Chaque outil noté seul, sur les critères de sa couche, moyenne ramenée sur 100. Les outils en gris dans la page ne sont dans aucune des 4 stacks : ajoutés pour comparer.

**Construction** (site vitrine, écran du cadre, appli aidant, simplicité, coût, écosystème et aide)

| Outil | Score | Pour comparer |
|---|---|---|
| React + Next.js | 80 | stack A, retenu |
| Vue + Nuxt | 77 | oui |
| Flutter en code (Dart) | 73 | oui |
| Svelte + SvelteKit | 73 | oui |
| Python + Django | 70 | oui, seul langage déjà pratiqué par l'équipe |
| HTML, CSS, JavaScript seuls | 70 | oui |
| Softr | 63 | stack C |
| WordPress + WooCommerce | 63 | oui, site vitrine seulement |
| FlutterFlow | 60 | stack D |
| Glide | 53 | stack B, hors Europe |

**Base de données** (fichiers vidéo, limites, API et temps réel, coût)

| Outil | Score | |
|---|---|---|
| Supabase | 75 | stacks A et D |
| Firebase | 70 | pour comparer, hébergeur Google |
| Airtable | 60 | stack C, hors Europe |
| PostgreSQL sur Neon | 50 | la base de notre veille, à Francfort : première case « testé » |
| Glide Tables | 45 | stack B, hors Europe |

**Automatisation** (webhooks, règle dans le temps, notifications, quota, coût)

| Outil | Score | |
|---|---|---|
| Code dans Supabase | 92 | stack A, retenu |
| n8n | 88 | stack D |
| Firebase Cloud Functions | 88 | pour comparer |
| Vercel Cron + routes Next.js | 80 | pour comparer |
| Python + GitHub Actions | 72 | la veille du jeudi : deuxième case « testé » |
| Make | 68 | stack B, passe l'Europe |
| Zapier | 40 | stack C, hors Europe |

Sur les 137 notes des briques, 75 sont documentées, 60 estimées, 2 testées.

Ce que la lecture par couche apprend, et que le tableau des stacks ne montrait pas :

- la meilleure brique de chaque couche donne la stack A ;
- Make passe le critère Europe. Ce qui élimine la stack B, c'est Glide ;
- Softr fait un site vitrine aussi bien que Next.js, et plus simplement. Il perd sur le cadre et sur l'appli ;
- WordPress reste une option pour la seule brique du site vitrine, si on veut que Camille et Lucas le modifient sans code.

## Les décisions prises le 22 octobre

1. **Claude Code n'est pas un maillon de la stack.** Un outil qui écrit du code n'est pas ce qui fait tourner le produit. La stack A se nomme par ses briques : React, Next.js, Supabase. Claude Code est l'outil de travail, usage déclaré dans le rendu.
2. **Pas de n8n dans la stack A.** L'automatisation se fait en code, dans Supabase : une fonction Edge reçoit le toucher et envoie la notification, une tâche pg_cron vérifie chaque heure la règle des 48 heures. n8n reste dans la stack D.
3. **On construit en React et JavaScript.** Les autres langages sont dans le comparatif pour montrer qu'on a regardé, pas pour hésiter.
4. **La tablette récupérée, une Samsung Galaxy Tab A 2019, reste sous Android** avec une appli kiosque qui lance l'écran du cadre au démarrage, en plein écran, verrouillé. Pas de système Linux maison.
5. **Il y a trois choses à construire**, pas deux : le site vitrine qui vend le cadre et l'appli, l'écran du cadre, l'appli de l'aidant.

## Ce qui reste à aligner dans les documents de l'équipe

| Document | Ce qu'il dit encore | Ce qu'il devrait dire |
|---|---|---|
| Benchmark du 16 octobre (Clément) | stack A = Claude Code + Supabase + n8n | React + Next.js + Supabase, règles en code |
| Architecture et données (Camille) | Claude Code + React + Next + Supabase, 3 stacks comparées | même nom que le classement ; 4 stacks |
| Architecture et données (Camille) | OS Linux maison sur la tablette | Android et appli kiosque |
| Plan de la démo (Lucas) | FlutterFlow + Supabase + LiveKit + Mistral, tablette neuve | c'est la stack D, plan B ; tablette récupérée |

## Ce qu'il reste à faire

| Quand | Quoi | Qui |
|---|---|---|
| avant le 24 octobre | relire les notes, contester celles qui semblent fausses, en écrivant le désaccord dans la case | Lucas |
| dès le compte Supabase | le test commun du toucher sur la stack A : schéma, fonction Edge, page du cadre, page aidant, notification sur le téléphone, avec le cas invalide et le doublon | Clément, code préparé avec Claude Code |
| 29 octobre | les 4 usages sur A puis D ; chaque résultat passe en « testé » avec sa capture ; le classement se recalcule | Lucas et Clément |
| 29 octobre | les prompts de la boîte à outils IA sur Claude, ChatGPT, Gemini, Mistral et un outil spécialisé par thème | Lucas et Clément, Camille pour ses 2 thèmes |
| avant le 6 novembre | la version testée du classement part dans `rendus/` ; pages 2, 3 et 5 du PDF | Clément |

Si le code en React et Next.js échoue sur un usage, ou prend beaucoup trop de temps, on ne change que la brique de construction : FlutterFlow sur la même base, c'est la stack D.

## Sources

38 sources sont listées dans la page du classement, avec leur lien. Les principales :

- officielles : Supabase (conformité GDPR, prix, fonctions Edge, pg_cron), Next.js, Nuxt, SvelteKit, Flutter, Django, Vercel (prix, cron), Firebase (prix, fonctions), Neon, Make (zones de données, prix), Glide (GDPR), Airtable (résidence des données, API), GitHub Actions, MDN (Push API), enquête Stack Overflow 2025 ;
- tierces, à confirmer sur les pages officielles pendant les tests : Jet Admin (prix de Zapier et d'Airtable), CostBench (plan gratuit de Glide), VP0 (prix de FlutterFlow), Sliplane (prix de n8n), Virtua (comparatif n8n, Zapier, Make) ;
- internes : le benchmark du 16 octobre, les 4 usages à tester, le plan de la démo de Lucas, le process de veille (Neon à Francfort, GitHub Actions le jeudi).

Relevé des 15 et 16 octobre pour les prix et les limites, complété le 22 octobre pour les outils ajoutés.
