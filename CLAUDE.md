# Fil rouge — règles de travail de l'équipe

Dépôt du projet fil rouge **PFR Générations Connectées** (Ynov B2 Product Builder No-Code, 2026-2027), thème silver economy : rassurer les familles sur leurs proches âgés.
Équipe de 3 : **Clément**, **Lucas**, **Camille**. Chacun a une copie locale du dépôt et travaille avec son agent Claude.

Ce fichier est lu par l'agent IA à chaque session. **Il s'applique avant toute écriture, tout commit et tout push.**

## 1. Avant de toucher au dépôt : se synchroniser

1. Au début de chaque session et **avant chaque modification** : `git pull --rebase --autostash`.
2. **Avant chaque push** : `git pull --rebase`, puis `git push`.
3. En cas de conflit : **ne rien écraser**. L'agent s'arrête, montre les fichiers en conflit et demande au membre qui a raison. Il ne choisit jamais « ma version » à l'aveugle.
4. Interdit : `git push --force`, `git reset --hard` sur du travail poussé, réécrire l'historique de `main`, supprimer une branche d'un autre membre.

## 2. Qui modifie quoi (anti-écrasement)

Tout le monde pousse sur `main`.

| Zone | Qui écrit | Règle |
|---|---|---|
| `interne/<prénom>/` | ce membre seulement | Libre. On ne modifie pas le dossier d'un autre membre. |
| `interne/commun/` | tout le monde | Pull juste avant, modification courte, push juste après. Annoncer dans le message de commit ce qui a changé. |
| `rendus/` | tout le monde, après accord | Un rendu se remplace seulement si l'équipe l'a validé. Le membre qui l'a produit est prévenu avant toute modification. |
| `suivi/` | tout le monde | Modifier `suivi/taches.json`, puis relancer `python3 suivi/build.py`. Ne jamais éditer `suivi.html` à la main. |
| `CLAUDE.md`, `README.md` | tout le monde, après accord | Une règle commune ne change qu'avec l'accord des 3. |

- Avant de modifier un fichier qui n'est pas dans son propre dossier, l'agent regarde qui l'a modifié en dernier (`git log -1 --format='%an %ar' -- <fichier>`). Si c'est un autre membre et que c'est récent (moins de 24 h), il demande avant.
- Pour retravailler le rendu d'un autre, on crée une **nouvelle version** (`-v2`) dans son `interne/<prénom>/` au lieu d'écraser l'original.
- Un commit = un sujet. Le message de commit est en français et dit quoi et pourquoi (`Question 2 : TAM/SAM/SOM, méthode ascendante ajoutée`).

## 3. Organisation de l'année et création de dossiers

Le dépôt est découpé par **semestre**, puis par **phase**. Chaque phase sépare le travail interne des rendus.

```
S1-2026-2027/
  01-veille/
    interne/
      clement/   lucas/   camille/   commun/
    rendus/
  02-marche/
    interne/ …
    rendus/
  03-…/
S2-2026-2027/
  01-…/
suivi/          # tâches et statuts de toute l'année (suivi.html généré)
automatisation/ # scripts et prompts partagés (veille hebdo…)
```

Règles de création :
- Un nouveau semestre : `S<n>-2026-2027/`. Une nouvelle phase : `NN-nom-court/`, numérotée dans l'ordre du semestre (`03-persona/`). Chaque nouvelle phase est créée **avec** `interne/clement/`, `interne/lucas/`, `interne/camille/`, `interne/commun/` et `rendus/`. Mettre un `.gitkeep` dans les dossiers vides.
- Aucun nouveau dossier à la racine en dehors de `S*/`, `suivi/` et `automatisation/` sans accord de l'équipe.
- Noms de fichiers et de dossiers : minuscules, sans accent ni espace, mots séparés par des tirets (`question-2-taille-marche.html`).
- `rendus/` ne contient que des versions finales, avec un nom qui dit ce que c'est (`question-1-acteurs.html`, `fiche-veille-silvertech.html`). Les brouillons, données et essais vont dans `interne/`.
- Quand un rendu est ajouté, l'agent ajoute son lien dans le `README.md` (section du semestre et de la phase) et met à jour `suivi/taches.json`.

> **Migration en attente.** Les dossiers actuels `01-veille/` et `02-marche/` sont encore à la racine. On les déplacera dans `S1-2026-2027/` en une seule fois, avec l'accord des 3 et sans travail en cours non poussé, car les chemins du pipeline de veille et des liens du README changent. D'ici là, on garde les chemins actuels.

## 4. Le rythme de l'année

- **S1 2026-2027** (en cours) : phase 01 veille, phase 02 marché (leçon 2.1). Les phases suivantes s'ajoutent au fil des cours.
- **S2 2026-2027** : à compléter.
- Chaque phase suit la même boucle : travail dans `interne/`, validation par l'équipe, version finale dans `rendus/`, lien dans le README, tâche passée à `termine` dans `suivi/`.

## 5. Protection des données (le dépôt est PUBLIC)

Tout ce qui est poussé est visible par n'importe qui sur Internet et reste dans l'historique même après suppression.

Ne jamais pousser :
- **Secrets** : mots de passe, clés d'API, jetons, chaînes de connexion (Neon, Supabase…), fichiers `.env`. Ils restent en local, dans `.env`, ignoré par git. Un exemple sans valeur réelle va dans `.env.example`.
- **Coordonnées de l'équipe** : e-mails, téléphones, adresses. Elles restent hors du dépôt.
- **Données personnelles de tiers** : noms, pseudos, villes, âges précis de seniors, d'aidants ou d'auteurs d'avis. Les verbatims sont anonymisés (300 caractères maximum).
- **Documents de cours** (PDF du formateur) et fichiers lourds : ils restent en local.

Si un secret a été poussé par erreur : le supprimer ne suffit pas. Prévenir l'équipe tout de suite et **changer le secret** (nouveau mot de passe, nouvelle clé).

Avant chaque commit, l'agent vérifie `git diff --cached` et refuse de commiter s'il voit un secret ou une donnée personnelle.

## 6. Ce que fait l'agent, en bref

1. `git pull --rebase --autostash` avant de travailler.
2. Il écrit dans `interne/<prénom du membre>/` par défaut, et ailleurs seulement selon le tableau de la section 2.
3. Il ne crée des dossiers que selon la section 3.
4. Il vérifie le diff (section 5), commite avec un message clair, fait `git pull --rebase`, puis `git push`.
5. Il ne pousse que si le membre le lui demande, et dit ce qu'il a poussé.

Les règles du pipeline de veille (`01-veille/veille-silvertech/CLAUDE.md`) s'ajoutent à celles-ci pour ce dossier.
