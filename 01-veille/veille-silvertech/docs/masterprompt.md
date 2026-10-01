# MASTERPROMPT — Pipeline de veille « Silver tech » (PFR Générations Connectées, Phase 1)

Tu es l'architecte et le développeur principal de ce projet. Tu construis un pipeline de veille automatisé, orchestré par toi (Claude Code) via des sous-agents et des commandes slash, avec une base Neon (PostgreSQL).

**Avant d'écrire la moindre ligne de code** : lis tout ce document, puis présente-moi un plan d'implémentation en 10 lignes maximum et attends ma validation.

---

## 1. Contexte

- Projet étudiant (Bachelor 2 Product Builder No-Code, Ynov). Phase 1 du projet fil rouge : fiche de veille « Marché & réglementation silver tech » (objets connectés pour seniors, achetés par leurs enfants aidants).
- Le dispositif de veille lui-même est évalué (compétence RNCP C.1.1.1 « Mettre en place un système de veille ») et sera présenté en annexe de la fiche.
- Principe directeur : **beaucoup d'entrées, peu de sorties**. On collecte large, on filtre sans IA, on qualifie avec IA, l'humain décide.
- Équipe de 2 à 3 étudiants : chacun doit pouvoir lancer la revue et comprendre le système.

## 2. Stack imposée

- Python 3.11+, `psycopg[binary]` v3, `feedparser`, `pyyaml`, `python-dotenv`, `pytest`.
- Base : Neon (PostgreSQL), connexion via `DATABASE_URL` dans `.env`.
- Orchestration : Claude Code (commandes dans `.claude/commands/`, sous-agents dans `.claude/agents/`).
- Aucune API payante, aucun service tiers en plus. Pas de framework web : le rendu visuel est un HTML statique généré.

## 3. Architecture

```
veille-silvertech/
├── CLAUDE.md                     # règles permanentes du projet (tu le rédiges)
├── README.md                     # installation + usage pour l'équipe
├── .env.example
├── requirements.txt
├── config/
│   ├── catalogue.yaml            # les 35 types d'information (section 5)
│   ├── sources.yaml              # flux RSS, apps, requêtes par code
│   └── regles.yaml               # autorité des domaines, mots-clés, seuils
├── sql/schema.sql
├── scripts/
│   ├── common.py                 # config, connexion, normalisation
│   ├── init_db.py                # crée le schéma + seed du catalogue
│   ├── collect_rss.py            # Google Alerts, médias, Reddit (RSS)
│   ├── collect_app_reviews.py    # avis App Store (flux public Apple)
│   ├── add_items.py              # stdin JSON → raw_items (utilisé par l'agent collecteur)
│   ├── prefilter.py              # filtrage SANS IA
│   ├── pending.py                # éléments à qualifier → JSON
│   ├── save_qualified.py         # stdin JSON → veille_items + score calculé
│   ├── review.py                 # décision humaine en CLI
│   ├── coverage.py               # couverture du catalogue
│   ├── report.py                 # rapport HTML hebdomadaire
│   └── export_fiche.py           # export Markdown des éléments validés
├── tests/                        # pytest, sans base de données
├── docs/dispositif-veille.md     # annexe de la fiche (sources, outils, fréquence, méthode)
├── rapports/                     # HTML générés (gitignore)
└── .claude/
    ├── commands/  veille.md, revue.md, couverture.md, export-fiche.md
    └── agents/    collecteur.md, qualificateur.md, rapporteur.md
```

### Flux de bout en bout

```
COLLECTE (scripts + agent collecteur)
  → raw_items (brut, immuable, dédoublonné par URL)
FILTRAGE SANS IA (prefilter.py)
  → rejet : domaine exclu, hors mots-clés, doublon de titre, > 36 mois
QUALIFICATION (agent qualificateur → save_qualified.py)
  → veille_items : champs remplis par l'IA + score de fiabilité calculé par script
REVUE HUMAINE (rapport HTML + review.py)
  → statut validé / rejeté, pertinence finale, validé par
EXPORT (export_fiche.py) → alimente la fiche de veille
```

## 4. Schéma de données (Neon)

### `catalogue`
`code` (PK, ex. M1), `axe`, `libelle`, `statut` (requis | bonus), `phase_cible` (texte libre, ex. « phase 2 »).

### `raw_items`
`id`, `url` (unique), `domaine`, `source_nom`, `titre`, `extrait`, `origine` (rss:<nom> | web_search | avis_app | reddit), `code_vise` (code du catalogue ciblé par la requête, nullable), `publie_le` (date), `collecte_le`, `etat` (nouveau | filtre | a_qualifier | qualifie), `motif_filtre`.

### `veille_items` — champs de la base de veille du cours, puis champs du pipeline
**Champs du cours :**
- `titre` — titre court de l'information
- `publie_le` — date de publication
- `source_nom`, `url` — source et lien
- `axe` — marche | concurrence | usagers | techno | reglementaire
- `resume` — 3 lignes maximum, reformulé (jamais copié)
- `pourquoi_important` — 1 à 2 phrases sur l'apport pour notre projet
- `pertinence_proposee` (1-3, par l'IA) et `pertinence` (1-3, décision humaine)
- `ajoute_par` — « agent » par défaut

**Champs du pipeline :**
- `raw_id` (FK unique), `code_info` (FK catalogue), `flux` (fait | signal)
- `score_fiabilite` (0-7, calculé par script, jamais par l'IA) avec `autorite`, `fraicheur`, `bonus_source_primaire`
- `source_primaire_url`, `chiffres` (jsonb : `[{valeur, contexte, source_citee}]`)
- `archetype` (securite | capteurs | sante_quotidien | compagnon | transverse)
- `ethique` (bool : touche la tension autonomie / surveillance), `sensible` (bool)
- `irritant` et `verbatim` (signaux uniquement)
- `statut` (a_revoir | valide | rejete | hors_sujet), `valide_par`, `commentaire`, `revu_le`

### `runs`
Journal de chaque exécution : date, nb collectés par origine, nb filtrés, nb qualifiés, nb hors sujet, modèle utilisé, durée. Sert de preuve du dispositif et de déclaration d'usage IA.

Contraintes CHECK sur toutes les énumérations, index sur `(statut, axe)` et `etat`.

## 5. Catalogue des informations (à seeder dans `catalogue.yaml` et la table)

**Marché**
- M1 Taille et croissance du marché silver tech — requis
- M2 Démographie : seniors à domicile, projections — requis
- M3 Aidants familiaux : nombre, profil, distance, charge — bonus (phase 2)
- M4 Moments déclencheurs d'achat — bonus (phase 2)
- M5 Aides publiques et prises en charge — bonus (modèle économique)
- M6 Canaux de distribution — bonus (parcours d'achat, phase 3)
- M7 Politiques publiques de maintien à domicile — bonus

**Concurrence**
- C1 Acteurs par famille (téléassistance, wearables, capteurs, compagnons) — requis
- C2 Offres et prix réels (engagement, frais cachés) — requis
- C3 Réussites et échecs + hypothèse d'explication — requis
- C4 Levées de fonds, rachats, faillites — requis
- C5 Promesses marketing vs réalité — requis
- C6 Discours de marque (stigmatisant ou non) — bonus
- C7 Nouveaux lancements — bonus

**Usagers**
- U1 Irritants côté seniors — bonus (phase 2)
- U2 Irritants côté aidants — bonus (phase 2)
- U3 Raisons d'abandon (« le tiroir ») — requis
- U4 Fracture numérique : équipement et usages — bonus (phase 3)
- U5 Ce que les utilisateurs apprécient — bonus

**Techno**
- T1 Technologies de détection et leurs limites — requis
- T2 IA appliquée (résumé d'activité, anomalie de routine, compagnon) — bonus (phase 5)
- T3 Outils no-code et IA adaptés — bonus (phase 5)
- T4 Connectivité, autonomie, installation — bonus (phase 6)
- T5 Standards et interopérabilité — bonus

**Réglementaire**
- R1 RGPD : données de santé et de vie quotidienne, consentement — requis
- R2 Frontière dispositif médical / bien-être — requis
- R3 AI Act : transparence, niveaux de risque — requis
- R4 Propriété intellectuelle — requis
- R5 Consentement des majeurs vulnérables — bonus (éthique)
- R6 Accessibilité numérique (RGAA, European Accessibility Act) — bonus
- R7 Droit des abonnements et résiliation — bonus
- R8 Hébergement de données de santé — bonus (applicabilité à vérifier)

## 6. Sources (`sources.yaml`)

- **Google Alerts** : une alerte par code requis minimum, en flux RSS. URLs fournies par l'utilisateur → laisse des placeholders `REMPLACER` et demande-les-moi.
- **Médias (RSS)** : maddyness.com, frenchweb.fr, silvereco.fr, cnil.fr. Ne devine aucune URL de flux : teste-la, et si elle ne répond pas, signale-le au lieu d'inventer.
- **Reddit (RSS public `/r/<sub>/.rss`)** : r/nocode, plus 1 ou 2 subreddits aidants ou seniors que tu proposes et que je valide.
- **App Store** : flux public d'avis Apple, liste d'`app_id` en placeholder.
- **Google Play** : pas d'API publique gratuite. Pas de scraping. Collecte manuelle documentée.
- **Recherche web (agent collecteur)** : 2 à 3 requêtes par code du catalogue, stockées dans `sources.yaml`. Cibler aussi aidants.fr, pour-les-personnes-agees.gouv.fr, ansm.sante.fr, eur-lex.europa.eu, insee.fr, drees.
- **Données entreprises** (pappers.fr, societe.com, crunchbase.com) : consultation ciblée par l'agent pour C1 et C4 uniquement, jamais d'extraction massive.

## 7. Filtrage sans IA (`prefilter.py`, dans `regles.yaml`)

1. Domaine dans `exclus` (facebook.com, instagram.com, tiktok.com, pinterest.com) → rejet.
2. Aucun mot-clé d'inclusion dans titre + extrait (senior, âgé, personne âgée, aidant, téléassistance, chute, maintien à domicile, silver, EHPAD, autonomie, objet connecté, CNIL, RGPD, dispositif médical, AI Act, accessibilité…) → rejet, sauf pour `origine = avis_app`.
3. Titre normalisé déjà présent sur les 30 derniers jours → rejet (doublon de reprise).
4. Publication > 36 mois → rejet, sauf axe réglementaire (textes de loi).
Chaque rejet stocke son `motif_filtre`.

## 8. Score de fiabilité (calculé par script, jamais par l'IA)

**FAIT (0 à 7)** = autorité (0-3) + fraîcheur (0-2) + source primaire (0-2)
- Autorité : niveau 3 = officiel (gouv.fr et sous-domaines, europa.eu, cnil.fr, insee.fr, has-sante.fr, ansm.sante.fr, cnsa.fr, santepubliquefrance.fr, service-public.fr, inpi.fr) ; niveau 2 = médias reconnus (silvereco.fr, maddyness.com, frenchweb.fr, lesechos.fr, lemonde.fr, lefigaro.fr, liberation.fr, francetvinfo.fr, usine-digitale.fr, numerama.com, aidants.fr) ; autre = 1 ; exclu = 0.
- Fraîcheur : ≤ 12 mois = 2, ≤ 24 mois = 1, sinon ou non daté = 0. Pour l'axe réglementaire, un texte en vigueur vaut 2.
- Source primaire citée et vérifiée : domaine niveau 3 = 2, autre = 1, absente = 0.

**SIGNAL** : pas de score de fiabilité ; jugé sur sa récurrence (nombre d'occurrences du même `irritant`).

Seuils : ≥ 5 prioritaire, 3-4 à vérifier, < 3 affiché en fin de rapport.

## 9. Sous-agents

### `collecteur` (outils : WebSearch, Bash, Read)
Pour chaque code du catalogue sous-couvert (moins de 3 éléments validés), lance les requêtes de `sources.yaml`, garde les 5 meilleurs résultats par requête, envoie le JSON à `add_items.py` avec `code_vise`. Ne résume rien, ne juge rien.

### `qualificateur` (outils : WebFetch, Bash, Read)
Traite les éléments `a_qualifier` par lots de 10. Pour chacun : lit la page (WebFetch ; si échec, travaille sur l'extrait et le signale), puis produit un JSON strict par élément :
`raw_id, pertinent, flux, axe, code_info, titre, resume, pourquoi_important, pertinence_proposee, source_primaire_url, chiffres, archetype, ethique, sensible, irritant, verbatim`.
Règles :
- **Ne jamais inventer** une URL, un chiffre, une date ou une source. Un chiffre n'est retenu que si l'article l'affirme ET cite son origine ; sinon `chiffres` reste vide.
- `source_primaire_url` uniquement si un lien explicite figure dans l'article.
- `resume` reformulé, 3 lignes max, aucune phrase copiée.
- `verbatim` : 300 caractères max, anonymisé (aucun nom, prénom, ville, âge précis, pseudo).
- `irritant` parmi : stigmatisation, complexite, fausses_alertes, prix_abonnement, intrusion_vie_privee, fiabilite_technique, service_client, autre.
- `sensible = true` si l'élément touche des données de santé ou une allégation médicale.
- `ethique = true` si l'élément touche la tension autonomie / surveillance ou le consentement.
- Hors sujet → `pertinent: false`.

### `rapporteur` (outils : Bash, Read, Write)
Rédige `rapports/synthese-AAAA-Sxx.md` : les 10 éléments prioritaires de la semaine, les irritants les plus récurrents, et les **trous de couverture** (codes requis sans élément validé). Chaque affirmation cite l'id de l'élément. Puis lance `report.py`.

## 10. Commandes slash

- **`/veille`** : pipeline complet → collect_rss, collect_app_reviews, collecteur, prefilter, qualificateur (boucle jusqu'à épuisement, plafond 100 éléments par run), rapporteur, écriture dans `runs`, bilan chiffré final.
- **`/revue`** : liste les éléments `a_revoir` par axe et score, puis aide l'utilisateur à valider ou rejeter (via `review.py`, avec pertinence finale et prénom).
- **`/couverture`** : tableau code × nb validés, trous en évidence.
- **`/export-fiche`** : export Markdown des éléments validés, regroupés par axe puis par code, avec bibliographie numérotée.

## 11. Rendu visuel (`report.py`)

HTML statique, autonome, responsive, lisible sur mobile. Sections : synthèse de l'agent (marquée « à vérifier »), faits par axe avec badge de score coloré, badges « sensible » et « éthique », signaux groupés par irritant et triés par récurrence, tableau de couverture du catalogue. Tout le contenu est échappé.

## 12. Règles permanentes (à écrire dans `CLAUDE.md`)

- Aucune donnée personnelle stockée : pas d'auteur d'avis, pas de pseudo, verbatims anonymisés.
- Pas de scraping de réseaux sociaux ni de sites qui l'interdisent.
- Pas de reproduction d'articles : résumés reformulés uniquement.
- Le score est calculé par script ; l'IA classe et résume, elle ne note pas la fiabilité.
- Toute exécution est journalisée dans `runs`.
- Toute modification de règles passe par les fichiers de `config/`, jamais en dur dans le code.

## 13. Ordre de construction

1. Plan → validation par moi.
2. Arborescence, `requirements.txt`, `.env.example`, `.gitignore`.
3. `schema.sql`, `catalogue.yaml`, `init_db.py` (idempotent).
4. Scripts de collecte, filtrage, qualification, score.
5. Tests pytest (sans base) : score, fraîcheur, correspondance de domaines, dé-redirection des liens Google Alerts (`google.com/url?url=`), préfiltre, échappement HTML.
6. Sous-agents et commandes slash.
7. `report.py`, `coverage.py`, `export_fiche.py`.
8. Test réel : demande-moi `DATABASE_URL` et au moins une URL Google Alerts, lance `/veille` avec un plafond de 10 éléments, montre-moi le rapport.
9. `README.md` (installation en moins de 10 étapes, usage hebdomadaire, qui fait quoi) et `docs/dispositif-veille.md` (annexe de la fiche : sources, outils, fréquence, méthode de filtrage et de scoring, limites, usage de l'IA).

## 14. Critères d'acceptation

- `pytest` passe intégralement.
- `init_db.py` peut être relancé sans erreur ni doublon.
- Un run complet produit un rapport HTML lisible sur téléphone et une ligne dans `runs`.
- Aucun élément qualifié ne contient d'URL ou de chiffre absent de la page source.
- Un coéquipier sans expérience en code peut lancer `/revue` en suivant le README.

## 15. Quand t'arrêter et me demander

- Avant de créer quoi que ce soit dans Neon.
- Si une source ne répond pas ou si son URL est incertaine.
- Si une règle de ce document est ambiguë ou contradictoire.
- Si une étape nécessite un service payant.
