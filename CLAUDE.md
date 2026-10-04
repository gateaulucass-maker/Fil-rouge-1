# Fil rouge — règles de travail de l'équipe

Dépôt du projet fil rouge **PFR Générations Connectées** (Ynov B2 Product Builder No-Code, 2026-2027), thème silver economy : rassurer les familles sur leurs proches âgés.
Équipe de 3 : **Clément**, **Lucas**, **Camille**. Chacun a une copie locale du dépôt et travaille avec son agent IA (Claude Code en général).

Ce fichier est lu par l'agent au début de chaque session. **Il s'applique avant toute écriture, tout commit et tout push.** Les autres agents (Codex, ChatGPT…) y sont renvoyés par `AGENTS.md`.

## 1. Le dépôt est PUBLIC : ce qui ne part jamais

Tout ce qui est poussé est visible par n'importe qui et reste dans l'historique même après suppression. Les fichiers locaux, eux, restent sur l'ordinateur de chacun : on garde en local tout ce qu'on veut, on ne publie que ce qui est sans risque.

Ne jamais commiter :
- **Secrets** : mots de passe, clés d'API, jetons, chaînes de connexion (Neon, Supabase…), fichiers `.env`. Ils restent dans `.env` (ignoré par git). Un exemple sans valeur réelle va dans `.env.example`.
- **Coordonnées de l'équipe** : e-mails, téléphones, adresses.
- **Données personnelles de tiers** : noms, pseudos, villes, âges précis de seniors, d'aidants ou d'auteurs d'avis. Verbatims anonymisés, 300 caractères maximum.
- **Documents de cours** (PDF du formateur) et **fichiers lourds** (plus de 2 Mo).

**Garde-fous automatiques** (dans `automatisation/hooks/`) :
- Avant chaque commit, `verifier-commit.sh` lit ce qui va être commité et **bloque** : secret probable, e-mail, téléphone, `.env`, clé, PDF hors `rendus/`, fichier de plus de 2 Mo. Il ne modifie et ne supprime aucun fichier.
- Il est activé automatiquement au démarrage de Claude Code. Pour un commit fait hors Claude Code, chaque membre l'active une fois sur son ordinateur : `git config core.hooksPath automatisation/hooks`.
- `.gitignore` bloque `.env`, les clés et les PDF (sauf dans `rendus/`).

Règles pour l'agent :
- Avant chaque commit, il relit `git diff --cached` en plus du contrôle automatique.
- Si le contrôle bloque, il retire l'élément ou le fichier du commit (`git restore --staged <fichier>`) et explique pourquoi. **Il n'utilise jamais `--no-verify`.** Seul le membre, s'il juge que c'est un faux positif, peut commiter lui-même en contournant.

**Si un secret a été poussé** : le supprimer ne suffit pas.
1. Prévenir l'équipe tout de suite.
2. Changer le secret (nouveau mot de passe, nouvelle clé) chez le fournisseur.
3. Ensuite seulement, retirer le secret du fichier et commiter.

## 2. Se synchroniser

1. Au démarrage de Claude Code, un hook fait `git pull` et affiche l'état du dépôt. S'il affiche **ATTENTION**, l'agent fait `git pull --rebase --autostash` avant toute autre action.
2. Avant chaque modification : `git pull --rebase --autostash`.
3. Avant chaque push : `git pull --rebase`, puis `git push`.
4. En cas de conflit : **ne rien écraser**. L'agent s'arrête, montre les fichiers en conflit et demande au membre qui a raison. Il ne choisit jamais « sa version » à l'aveugle.
5. Interdit : `git push --force`, `git reset --hard` sur du travail poussé, réécrire l'historique de `main`, supprimer une branche d'un autre membre.

## 3. Qui modifie quoi

Tout le monde pousse sur `main`.

| Zone | Qui écrit | Règle |
|---|---|---|
| `interne/<prénom>/` | ce membre seulement | Libre. On ne modifie pas le dossier d'un autre membre. |
| `interne/commun/` | tout le monde | Pull juste avant, modification courte, push juste après. Le message de commit dit ce qui a changé. |
| `rendus/` | tout le monde, après accord | Un rendu se remplace seulement si l'équipe l'a validé. Le membre qui l'a produit est prévenu avant. |
| `suivi/` | tout le monde | Modifier `suivi/taches.json`, puis relancer `python3 suivi/build.py`. Ne jamais éditer `suivi.html` à la main. |
| `automatisation/`, `.claude/` | tout le monde | Même régime que `interne/commun/`. Ne pas casser la veille du jeudi : tester avant de pousser. |
| `veille-hebdo/` | la veille automatique seulement | Personne ne l'édite à la main. |
| `CLAUDE.md`, `AGENTS.md`, `README.md` | voir ci-dessous | |

**Règles communes (`CLAUDE.md`, `AGENTS.md`)** : Camille valide les changements. Clément et Lucas sont prévenus avant le push, et le message de commit résume ce qui change. `README.md` : tout le monde peut y ajouter un lien de rendu (section 4).

- Avant de modifier un fichier hors de son propre dossier, l'agent regarde qui l'a modifié en dernier (`git log -1 --format='%an %ar' -- <fichier>`). Si c'est un autre membre il y a moins de 24 h, il demande avant.
- Pour retravailler le rendu d'un autre, on crée une **nouvelle version** (`-v2`) dans son propre `interne/<prénom>/`, sans écraser l'original.
- Chaque membre commite sous son prénom (`git config user.name "Camille"`), pour que la règle des 24 h fonctionne.
- Un commit = un sujet. Message en français qui dit quoi et pourquoi (`Question 2 : TAM/SAM/SOM, méthode ascendante ajoutée`).

## 4. Organisation et création de dossiers

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
S2-2026-2027/
suivi/          # tâches et statuts de l'année (suivi.html généré)
automatisation/ # scripts, prompts et hooks partagés (veille hebdo, contrôle avant commit)
veille-hebdo/   # page publiée chaque jeudi par la veille automatique
```

- Seuls ces dossiers existent à la racine : `S*/`, `suivi/`, `automatisation/`, `veille-hebdo/` (plus `.claude/` et `.github/`). Tout autre dossier racine demande l'accord de l'équipe.
- Nouveau semestre : `S<n>-2026-2027/`. Nouvelle phase : `NN-nom-court/`, numérotée dans l'ordre du semestre (`03-persona/`), créée **avec** `interne/clement/`, `interne/lucas/`, `interne/camille/`, `interne/commun/` et `rendus/`. Un `.gitkeep` dans chaque dossier vide.
- Noms de fichiers et de dossiers : minuscules, sans accent ni espace, mots séparés par des tirets (`question-2-taille-marche.html`).
- `rendus/` ne contient que des versions finales, avec un nom qui dit ce que c'est (`question-1-acteurs.html`). Brouillons, données et essais vont dans `interne/`.
- Quand un rendu est ajouté : lien dans `README.md` (section du semestre et de la phase) et tâche mise à jour dans `suivi/taches.json`.
- `veille-hebdo/` est publiée à l'adresse fixe https://gateaulucass-maker.github.io/Fil-rouge-1/veille-hebdo/ ; c'est pour ça qu'elle reste à la racine.

## 5. Le rythme de l'année

- **S1 2026-2027** (en cours) : phase 01 veille, phase 02 marché (leçon 2.1). Les phases suivantes s'ajoutent au fil des cours.
- **S2 2026-2027** : à compléter.
- Chaque phase suit la même boucle : travail dans `interne/`, validation par l'équipe, version finale dans `rendus/`, lien dans le README, tâche passée à `termine` dans `suivi/`.

## 6. Ce que fait l'agent, dans l'ordre

1. Il se synchronise (section 2).
2. Il écrit dans `interne/<prénom du membre>/` par défaut, ailleurs seulement selon la section 3, et ne crée des dossiers que selon la section 4.
3. Il commite (section 1 : diff relu, contrôle automatique jamais contourné).
4. Il ne pousse que si le membre le demande, après `git pull --rebase`, et dit ce qu'il a poussé.

Les règles du pipeline de veille (`S1-2026-2027/01-veille/interne/commun/veille-silvertech/CLAUDE.md`) s'ajoutent à celles-ci pour ce dossier.
