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

**Garde-fous automatiques** (dans `.claude/hooks/`) :
- Avant chaque commit, `verifier-commit.sh` lit ce qui va être commité et **bloque** : secret probable, e-mail, téléphone, `.env`, clé, PDF hors `rendus/`, fichier de plus de 2 Mo. Il ne modifie et ne supprime aucun fichier.
- Il est activé automatiquement au démarrage de Claude Code. Pour un commit fait hors Claude Code, chaque membre l'active une fois sur son ordinateur : `git config core.hooksPath .claude/hooks`.
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
| `.claude/` (agents, commandes, hooks, réglages) | tout le monde | Même régime que `interne/commun/`. Tester avant de pousser : un hook cassé bloque tout le monde. |
| `interne/commun/veille-du-jeudi/` | tout le monde | Ne pas casser la veille du jeudi : la tester (`ESSAI=1`) avant de pousser. |
| `veille-hebdo/` | la veille automatique seulement | Personne ne l'édite à la main. |
| `CLAUDE.md`, `AGENTS.md`, `README.md` | voir ci-dessous | |

**Règles communes (`CLAUDE.md`, `AGENTS.md`)** : Camille valide les changements. Clément et Lucas sont prévenus avant le push, et le message de commit résume ce qui change. `README.md` : tout le monde peut y ajouter un lien de rendu (section 4, étape 7).

- Avant de modifier un fichier hors de son propre dossier, l'agent regarde qui l'a modifié en dernier (`git log -1 --format='%an %ar' -- <fichier>`). Si c'est un autre membre il y a moins de 24 h, il demande avant.
- Pour retravailler le rendu d'un autre, on crée une **nouvelle version** (`-v2`) dans son propre `interne/<prénom>/`, sans écraser l'original.
- Chaque membre commite sous son prénom (`git config user.name "Camille"`), pour que la règle des 24 h fonctionne.
- Un commit = un sujet. Message en français qui dit quoi et pourquoi (`Question 2 : TAM/SAM/SOM, méthode ascendante ajoutée`).

## 4. Où ranger un fichier

### La racine : seulement les règles et l'outillage

```
CLAUDE.md  AGENTS.md  README.md
.claude/        # agents/, commands/, hooks/, settings.json : l'outillage des agents IA
.github/        # workflow de publication de la veille
suivi/          # tâches et statuts de l'année (suivi.html généré à la racine)
veille-hebdo/   # page publiée chaque jeudi (adresse fixe, voir plus bas)
S1-2026-2027/   # TOUT le travail du semestre 1
S2-2026-2027/   # TOUT le travail du semestre 2
```

Rien d'autre à la racine. Un nouvel agent, une commande ou un hook va dans `.claude/`. Tout le reste (rendus, brouillons, données, scripts, prompts de travail) va dans un semestre.
`veille-hebdo/` reste à la racine parce que son adresse est publique et fixe : https://gateaulucass-maker.github.io/Fil-rouge-1/veille-hebdo/

### Dans un semestre : bloc du cours, puis rendu ou interne

Un dossier `NN-nom/` = **un bloc du cours** (un module ouvert par le formateur). Un bloc contient **plusieurs leçons**, qui ne suivent pas forcément son numéro : le bloc 01 Veille contient la leçon 1.1 (veille) **et** la leçon 2.1 (marché). Les leçons ne créent pas de sous-dossier : c'est le **préfixe du nom de fichier** qui dit de quelle leçon il vient.

```
S1-2026-2027/
  01-veille/                    # bloc 01 : leçon 1.1 (veille), leçon 2.1 (marché)…
    rendus/                     # versions finales validées, toutes leçons du bloc
      1-1-fiche-veille-silvertech.html
      2-1-question-1-acteurs.html
    interne/
      clement/  lucas/  camille/    # travail de chacun (fichiers préfixés aussi)
      commun/                       # outils et données partagés (pipeline, veille du jeudi…)
  02-<bloc suivant>/            # créé quand le formateur ouvre un nouveau bloc
```

### La procédure, à appliquer à chaque fichier créé ou rendu

Avant d'écrire un fichier (et de nouveau avant le commit), l'agent détermine sa place dans cet ordre :

1. **Outillage IA ou règle commune ?** Agent, commande, hook, réglage → `.claude/`. Règle d'équipe → `CLAUDE.md`. Sinon, étape 2.
2. **Semestre** : le semestre en cours (section 5), sauf si le membre en indique un autre.
3. **Leçon** : l'agent cherche le numéro de leçon `X.Y` dans la demande du membre, puis dans le titre ou le contenu du fichier (« Leçon 2.1 », « 2.1 », sujet du cours). **S'il ne le trouve pas, il demande. Il ne devine jamais.**
4. **Bloc** : la leçon va dans le bloc du cours auquel elle appartient, **pas** dans un dossier déduit de son numéro (la leçon 2.1 est dans `01-veille/`). Par défaut, c'est le dernier bloc ouvert du semestre. L'agent ne crée un nouveau bloc `NN-nom-court/` (numéro suivant) que si le membre dit que le formateur a ouvert un nouveau bloc ; il demande alors le nom court et crée `rendus/`, `interne/clement/`, `interne/lucas/`, `interne/camille/`, `interne/commun/` avec un `.gitkeep` dans chaque dossier vide. **Jamais de sous-dossier par leçon.**
5. **Rendu ou interne** :
   - version finale validée par l'équipe → `rendus/` ;
   - brouillon, essai, version de travail, annexe d'un membre → `interne/<prénom du membre>/` ;
   - outil, script, prompt ou données utilisés par toute l'équipe → `interne/commun/<nom-de-l-outil>/`.
6. **Nom** : `X-Y-<ce-que-c-est>.<ext>`, en minuscules, sans accent ni espace, mots séparés par des tirets (`2-1-question-2-taille-marche.html`). Une nouvelle version d'un rendu d'un autre : même nom suivi de `-v2`, dans son propre `interne/<prénom>/`. Les dossiers d'outils dans `interne/commun/` (`veille-silvertech/`, `veille-du-jeudi/`) ne prennent pas de préfixe : ils servent plusieurs leçons.
7. **Après un rendu** : lien ajouté dans `README.md` (section du bloc, sous la leçon), tâche mise à jour dans `suivi/taches.json`, puis `python3 suivi/build.py`.

Si un fichier existant est mal rangé, l'agent le signale et propose de le déplacer avec `git mv` (l'historique est conservé), en corrigeant les liens qui pointent vers lui. Il ne déplace pas le fichier d'un autre membre sans le prévenir.

## 5. Le rythme de l'année

- **S1 2026-2027** (en cours) : bloc 01 veille (leçon 1.1 veille, leçon 2.1 marché). Les blocs suivants s'ajoutent quand le formateur les ouvre.
- **S2 2026-2027** : à compléter.
- Chaque leçon suit la même boucle : travail dans `interne/`, validation par l'équipe, version finale dans `rendus/`, lien dans le README, tâche passée à `termine` dans `suivi/`.

## 6. Ce que fait l'agent, dans l'ordre

1. Il se synchronise (section 2).
2. Il range chaque fichier avec la procédure de la section 4 (`interne/<prénom du membre>/` par défaut), respecte la section 3, et ne crée des dossiers que selon la section 4.
3. Il commite (section 1 : diff relu, contrôle automatique jamais contourné).
4. Il ne pousse que si le membre le demande, après `git pull --rebase`, et dit ce qu'il a poussé.

Les règles du pipeline de veille (`S1-2026-2027/01-veille/interne/commun/veille-silvertech/CLAUDE.md`) s'ajoutent à celles-ci pour ce dossier.
