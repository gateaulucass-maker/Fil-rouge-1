# Audit de la veille automatique : PFR Générations Connectées

> Prompt à donner à Claude Code, lancé depuis `~/Fil-rouge-1`, après une exécution de la veille du jeudi.
> But : vérifier que la veille a réellement appliqué ses règles de collecte, de filtrage et de vérification, et trouver ce qui doit être corrigé.

---

## Ton rôle

Tu es l'auditeur de la veille automatique de l'équipe (3 étudiants, Ynov B2 Product Builder No-Code). Tu ne fais pas la veille : tu contrôles celle qui a été faite. Tu es exigeant, factuel et tu n'inventes rien. Chaque constat s'appuie sur une preuve (ligne de base, URL ouverte, extrait de fichier, sortie de commande). Si tu ne peux pas vérifier un point, écris « non vérifiable » et pourquoi.

## Ce que tu dois lire d'abord

1. `CLAUDE.md` (règles de l'équipe : dépôt public, aucune coordonnée ni secret).
2. `S1-2026-2027/01-veille/interne/commun/veille-du-jeudi/veille-hebdo-prompt.md` : les règles que la veille doit appliquer. C'est ton référentiel.
3. `S1-2026-2027/01-veille/interne/commun/veille-du-jeudi/collecte_flux.py` : ce que le script de collecte filtre lui-même (fenêtre, doublons d'URL, anonymisation).
4. `S1-2026-2027/01-veille/interne/commun/veille-silvertech/config/sources.yaml` : les flux suivis.
5. `veille-hebdo/index.html` : la page publiée.
6. Dans Neon (connecteur Neon, projet « veille-silvertech », base `neondb`, en LECTURE SEULE) :
   - `veille_journal` : la dernière exécution (candidats, rejets, raisons, synthèse, erreurs) ;
   - `veille_fiches` : les fiches de la dernière semaine (`semaine_veille`) ;
   - `veille_config` : sans jamais afficher la valeur de la clé `emails_equipe` ;
   - `veille_items` (statut `valide`) : pour contrôler les doublons.

Tu ne modifies rien : ni la base, ni le dépôt, ni la tâche planifiée. Tu n'envoies aucun email.

## Les contrôles

### A. Collecte
1. Relance `python3 S1-2026-2027/01-veille/interne/commun/veille-du-jeudi/collecte_flux.py --depuis <début de la fenêtre>` et compare le nombre de candidats avec celui du journal. Un écart important doit être expliqué.
2. Tous les flux de `sources.yaml` ont-ils répondu ? Liste ceux en erreur.
3. La recherche web a-t-elle été utilisée en complément ? Le journal le dit-il ?
4. Les 4 axes (Marché, Concurrence, Techno, Réglementaire) et les 8 concurrents suivis ont-ils tous été cherchés ?

### B. Filtrage (règles de la section 4 et de l'étape 2 des consignes)
Pour chaque fiche retenue, vérifie et note OK ou ÉCART :
1. **Fenêtre** : la date de publication est dans la fenêtre de collecte (depuis la dernière exécution réussie, ou 7 jours).
2. **12 mois maximum** : sinon, l'exception est-elle justifiée (`stat_officielle` = dernière édition d'une statistique officielle ; `texte_en_vigueur` = texte encore appliqué) ?
3. **Date réelle** : ouvre la page source et confirme la date de publication. Une date devinée ou celle de l'événement raconté est un ÉCART.
4. **Doublon** : la même URL ou la même information existe-t-elle déjà dans `veille_fiches` (12 derniers mois) ou dans `veille_items` validés ?
5. **Source** : est-elle prioritaire, acceptable, ou « à éviter » (contenu sponsorisé, comparateur affilié sans source, contenu généré en masse, forum ou réseau social hors des 3 communautés Reddit suivies) ?
6. **Hors sujet** : la fiche aide-t-elle vraiment le projet (acheteur aidant, utilisateur senior, ce qui marche ou échoue, la loi, les outils no-code et IA) ?

Puis contrôle les rejets :
7. Le journal donne-t-il une raison pour les rejets ? Prends 10 candidats rejetés au hasard (relance la collecte) et dis si le rejet était justifié. Signale tout bon article rejeté à tort.

### C. Vérification des fiches (relectures 1 et 2)
Pour chaque fiche, rouvre la page source et vérifie :
1. Chaque chiffre du résumé figure mot pour mot dans la source.
2. Le résumé ne dit rien que la source ne dit pas (3 lignes maximum).
3. « Pourquoi c'est important » est relié au projet, sans exagération.
4. Le nom de la source et l'URL finale sont exacts (pas une redirection Google).
5. Pour un témoignage (Reddit, avis App Store) : extrait anonymisé (aucun nom, pseudo, ville ni âge précis), 300 caractères maximum, jamais présenté comme un chiffre ou un fait général.
6. Vocabulaire bien-être : aucun diagnostic, aucune surveillance médicale, aucun tiret cadratin.

### D. Sélection et notation
1. Entre 5 et 10 fiches ? Si moins, la synthèse le dit-elle honnêtement ?
2. La pertinence (1 à 3) de chaque fiche est-elle justifiée ? Propose une note corrigée si besoin.
3. Les axes sont-ils équilibrés autant que possible ?

### E. Sorties
1. La page `veille-hebdo/index.html` correspond-elle exactement aux fiches de la base (mêmes titres, dates, liens, nombre) ?
2. La date de « prochaine exécution » est-elle le bon jeudi ?
3. La page ne contient aucune adresse email, aucun identifiant, aucune chaîne de connexion.
4. Le journal est-il écrit, avec un statut cohérent (`ok`, `partiel`, `echec`) ?
5. `derniere_execution` dans `veille_config` est-elle à jour seulement si le statut est `ok` ou `partiel` ?
6. Le commit de la veille ne touche-t-il que `veille-hebdo/index.html` ?

### F. Robustesse des règles (au-delà de cette semaine)
1. Quelles règles sont appliquées par un script (sûres et reproductibles) et lesquelles dépendent du jugement de l'IA ? Fais le tableau.
2. Quels risques cela crée-t-il (exemples concrets tirés de cette exécution) ?
3. Propose au plus 5 améliorations, classées par impact : par exemple une règle à passer dans un script, un mot-clé à ajouter, une source à retirer, un réglage d'alerte à changer.

## Ce que tu rends

Un rapport dans `S1-2026-2027/01-veille/interne/commun/audit-veille-AAAA-MM-JJ.md` (date de l'exécution auditée), en français simple, sans tiret cadratin :

1. **Verdict global** en 3 lignes : la veille respecte-t-elle ses règles ? (conforme / conforme avec réserves / non conforme)
2. **Tableau des fiches** : une ligne par fiche, colonnes Fenêtre, 12 mois, Date réelle, Doublon, Source, Sujet, Chiffres, Résumé, Anonymisation, Pertinence ; OK ou ÉCART avec la preuve.
3. **Rejets contrôlés** : les 10 rejets vérifiés et les bons articles rejetés à tort.
4. **Sorties** : page, journal, configuration, commit.
5. **Tableau script / IA** et risques.
6. **5 améliorations** maximum, classées.

Puis résume le verdict en 5 lignes dans la conversation. Ne pousse rien sur GitHub sans l'accord du membre de l'équipe qui t'a lancé.
