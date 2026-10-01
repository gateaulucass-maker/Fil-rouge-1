# Veille silver tech — pipeline automatisé

Pipeline de veille de la **phase 1** du projet fil rouge (Ynov B2 Product Builder No-Code, PFR Générations Connectées) :
« Marché & réglementation silver tech », c'est-à-dire les objets connectés pour seniors achetés par leurs enfants aidants.

**Principe : beaucoup d'entrées, peu de sorties.** On collecte large, on filtre sans IA, on qualifie avec IA, l'humain décide.

```
COLLECTE   flux RSS (médias, Google Alerts, Reddit) + avis App Store + recherche web (agent collecteur)
   ↓        raw_items : brut, dédoublonné par URL
FILTRE     sans IA : domaine exclu, hors mots-clés, doublon de titre, > 36 mois
   ↓
QUALIF.    agent qualificateur : axe, code, résumé, chiffres sourcés… + score de fiabilité calculé par SCRIPT
   ↓        veille_items (statut « a_revoir »)
REVUE      humaine : valider (pertinence 1-3) ou rejeter
   ↓
EXPORT     Markdown pour la fiche de veille
```

Le **dernier rapport** est dans [`rapports/`](rapports/) : télécharger le fichier `.html` et l'ouvrir dans un navigateur.

## Installation (une seule fois, 8 étapes)

1. Installer [Python 3.11+](https://www.python.org/downloads/) et [Claude Code](https://claude.com/claude-code).
2. Cloner le dépôt : `git clone https://github.com/gateaulucass-maker/Fil-rouge-1.git`
3. Aller dans le dossier : `cd Fil-rouge-1/01-veille/veille-silvertech`
4. Créer l'environnement : `python3 -m venv .venv`
5. Installer les dépendances : `.venv/bin/pip install -r requirements.txt`
6. Copier la configuration : `cp .env.example .env`
7. Dans `.env`, coller la chaîne de connexion **Neon** (demander à Lucas, ne jamais la commiter).
8. Vérifier : `.venv/bin/python -m pytest -q` doit afficher « passed ».

> Si la base est neuve (une seule personne le fait) : `.venv/bin/python scripts/init_db.py`. Relançable sans risque.

## Usage hebdomadaire

Ouvrir un terminal dans `Fil-rouge-1/01-veille/veille-silvertech`, lancer `claude`, puis taper :

| Commande | Quand | Ce que ça fait |
|---|---|---|
| `/veille` | lundi | Collecte, filtre, qualifie et produit le rapport HTML de la semaine |
| `/revue` | dans la semaine | Passe en revue les éléments à revoir : tu valides ou rejettes, avec ton prénom |
| `/couverture` | après la revue | Montre les infos du catalogue encore sans élément validé (les « trous ») |
| `/export-fiche` | avant un rendu | Génère `rapports/fiche-veille.md` avec les éléments validés et la bibliographie |

**Revue sans Claude :** `.venv/bin/python scripts/review.py interactif --par TonPrénom`, puis taper `v`, `1`/`2`/`3`, `r` ou `s`.

## Qui fait quoi

| Rôle | Qui | Tâche |
|---|---|---|
| Lancer `/veille` | une personne, à tour de rôle | lundi, environ 15 minutes |
| Revue | toute l'équipe | chacun valide l'axe qu'il suit (marché / concurrence / usagers / techno / réglementaire) |
| Sources | toute l'équipe | ajouter un flux ou une requête dans `config/sources.yaml` (jamais dans le code) |
| Fiche de veille | rédacteur du rendu | `/export-fiche`, puis rédaction de la fiche |

## Fichiers utiles

- `config/catalogue.yaml` : les 32 types d'information recherchés (M1…R8), requis ou bonus.
- `config/sources.yaml` : flux RSS, apps suivies, requêtes de recherche par code.
- `config/regles.yaml` : domaines exclus et officiels, mots-clés, seuils de score.
- `docs/dispositif-veille.md` : **annexe de la fiche** (sources, outils, fréquence, méthode, limites, usage de l'IA).
- `docs/masterprompt.md` : le cahier des charges d'origine.
- `CLAUDE.md` : les règles permanentes que Claude respecte dans ce dossier.

## Score de fiabilité (faits)

`autorité (0-3) + fraîcheur (0-2) + source primaire (0-2)` = **0 à 7**, calculé par script.
≥ 5 : prioritaire · 3-4 : à vérifier · < 3 : en fin de rapport.
Les **signaux** (avis, témoignages) n'ont pas de score : ils comptent par récurrence de l'irritant.
