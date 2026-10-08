# Fil rouge — PFR Générations Connectées

Projet fil rouge du semestre · **Ynov B2 Product Builder No-Code** · 2026-2027

Thème : silver economy — rassurer les familles sur leurs proches âgés.

## Structure

| Où | Contenu |
|---|---|
| [`S1-2026-2027/`](S1-2026-2027/) | **Tout le travail du semestre 1**, par bloc du cours : [`01-veille/`](S1-2026-2027/01-veille/) (leçons 1.1 veille et 2.1 marché). Dans chaque bloc : `rendus/` (versions finales) et `interne/` (travail de chacun, outils communs). |
| `S2-2026-2027/` | Semestre 2 (à venir). |
| [`suivi/`](suivi/) | Tâches et statuts de l'année ([suivi.html](suivi.html), généré). |
| [`veille-hebdo/`](veille-hebdo/) | Page publiée chaque jeudi par la veille automatique (adresse fixe). |
| `CLAUDE.md`, `AGENTS.md`, [`.claude/`](.claude/) | Règles de l'équipe et outillage des agents IA : agents, commandes, hooks (contrôle avant commit). |

Les fichiers d'une leçon portent son numéro en préfixe : `2-1-question-1-acteurs.html` = leçon 2.1.

## Livrables

### Bloc 01 · Veille

#### Leçon 1.1 · Veille

- **[Fiche de veille finale « Marché & réglementation silver tech »](S1-2026-2027/01-veille/rendus/1-1-fiche-veille-finale.html)** (HTML, fichier unique) — **le rendu final de la leçon 1.1**, au plan du sujet d'examen : partie A (méthode, panorama des 4 familles, cadre réglementaire, synthèse, notre piste), partie B (dispositif de veille et master prompts complets, tableau de bord interactif), partie C (preuves d'exécution datées), qui a fait quoi, déclaration d'usage de l'IA, sources. Tout s'ouvre au clic dans le même fichier.
- **[Support de soutenance orale](S1-2026-2027/01-veille/rendus/1-1-support-oral.html)** (HTML, 10 slides, notes d'orateur avec la touche N) — au déroulé du sujet d'examen : marché, réglementaire, synthèse, dispositif et démo live, esprit critique, notre piste. Texte d'oral de chacun, format téléphone : [interne/camille/1-1-fiches-oral.html](S1-2026-2027/01-veille/interne/camille/1-1-fiches-oral.html).
- [Fiche de veille « Silver tech / marché & règles »](S1-2026-2027/01-veille/rendus/1-1-fiche-veille-silvertech.html) (HTML) — première version, générée depuis la base : thèse, chiffres clés, 5 axes, signaux usagers, positionnement, 5 principes pour le produit, méthode et 130 sources.
- [Apple Watch / Famileo](S1-2026-2027/01-veille/rendus/1-1-apple-watch-vs-famileo.html) — grille comparative en six critères (promesse, acheteur/utilisateur, modèle éco, adoption, rejet, hypothèse business).
  Enseignement : l'Apple Watch rassure l'enfant mais demande un effort au senior ; Famileo ne demande rien au senior mais ne détecte aucun danger. Notre produit se joue entre les deux.
- **[Process de veille](S1-2026-2027/01-veille/rendus/1-1-process-veille.html)** (HTML) — comment marche la veille automatique du jeudi : axes, étapes, double relecture, règles de fraîcheur, sources, format des fiches, sorties. En ligne : https://gateaulucass-maker.github.io/Fil-rouge-1/S1-2026-2027/01-veille/rendus/1-1-process-veille.html
- [Veille de la semaine](https://gateaulucass-maker.github.io/Fil-rouge-1/veille-hebdo/) — page mise à jour chaque jeudi à 7h45.
- [Pipeline de veille silver tech](S1-2026-2027/01-veille/interne/commun/veille-silvertech/) — collecte RSS / avis App Store / recherche web, filtre sans IA, qualification par agents Claude, score de fiabilité par script, revue humaine. **Mode d'emploi pour l'équipe : [README du pipeline](S1-2026-2027/01-veille/interne/commun/veille-silvertech/README.md).**
  - [Rapport de la semaine 2026-S40](S1-2026-2027/01-veille/interne/commun/veille-silvertech/rapports/rapport-2026-S40.html) (HTML) · [synthèse](S1-2026-2027/01-veille/interne/commun/veille-silvertech/rapports/synthese-2026-S40.md)
  - [Annexe « dispositif de veille »](S1-2026-2027/01-veille/interne/commun/veille-silvertech/docs/dispositif-veille.md) pour la fiche (RNCP C.1.1.1)
  - [Veille automatique du jeudi](S1-2026-2027/01-veille/interne/commun/veille-du-jeudi/) : consignes, script de collecte, lanceur Mac, prompt d'audit.
  - [Retour de construction du pipeline](S1-2026-2027/01-veille/interne/lucas/1-1-retour-pipeline-veille.html) (HTML) : ce qui a été fait, résultats du run 1, écarts, prochaines étapes

> Pour voir un livrable HTML : l'ouvrir via GitHub Pages (https://gateaulucass-maker.github.io/Fil-rouge-1/ + chemin du fichier), ou le télécharger et l'ouvrir dans un navigateur. Organisation et règles de l'équipe : voir CLAUDE.md.

#### Leçon 2.1 · Marché

- **[Question 1 : qui utilise, qui paie, qui influence ?](S1-2026-2027/01-veille/rendus/2-1-question-1-acteurs.html)** (HTML) — tableau simple des 5 rôles pour notre marché, comme l'exemple du prof, avec 7 sources officielles.
  - [Version détaillée par segment](S1-2026-2027/01-veille/interne/lucas/2-1-question-1-detail-par-segment.html) (annexe : 4 colonnes, scores de fiabilité, 70 sources).
- **[Analyse du marché : questions 1 à 5 et carte de positionnement](S1-2026-2027/01-veille/rendus/2-1-analyse-marche-questions-1-5.html)** (HTML) — les tableaux du cours remplis, guidés par une question clé : *comment le marché aide-t-il un enfant et son parent âgé à domicile à rester en lien et à veiller sur sa santé, et où ce double besoin reste-t-il mal couvert ?*
  Résumé : l'enfant aidant paie et décide, le parent vit avec l'offre (Q1, avec un persona payeur et un persona utilisateur) ; 7,5 M de 75 ans et plus, dont 0,2 à 0,6 M de foyers autonomes, aidés et non équipés (Q2) ; le marché sépare lien et sécurité, et seul le substitut famille + téléphone couvre les deux (Q3) ; le lien se vend 5,99 €/mois, la sécurité 20-30 €/mois, l'aide publique ne finance que la sécurité (Q4) ; la case « lien + sécurité discrète » est peu occupée (carte) ; trois gaps : veiller sans effort du senior, alerter sans épuiser l'aidant, garder le lien sans surveiller (Q5). 60 sources, toutes issues de la veille validée.
- **[Fiche marché rédigée : questions 1 à 5 et positionnement](S1-2026-2027/01-veille/rendus/2-1-fiche-marche-redigee.html)** (HTML) : les mêmes réponses écrites en texte suivi, avec un « En bref » par partie, les personas à déplier, la carte et la place visée par Le Cadre. 49 sources.

