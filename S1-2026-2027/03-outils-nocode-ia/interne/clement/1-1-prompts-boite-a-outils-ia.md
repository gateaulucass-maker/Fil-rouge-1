# Boîte à outils IA : les prompts de test, par thème

PFR Générations Connectées · Bloc 03 · Leçon 1.1 · Le Cadre
Brouillon de Clément, 22 octobre 2026. Pour Lucas et Clément (4 thèmes). Camille suit le même protocole pour ses 2 thèmes (visuels, analyse d'entretiens). Cible : 29 octobre.

Tout part de la page du classement des stacks : la stack A est React + Next.js + Supabase, règles en code. Les prompts sont écrits pour cette stack. Un même prompt est donné tel quel à chaque IA. On ne l'adapte pas à l'outil : c'est l'outil qu'on juge, pas notre habileté à le pousser.

## Les règles, prises du cours

- Le résultat attendu est écrit avant de lancer. On ne le réécrit pas après.
- Chaque thème a un cas invalide : une entrée fausse ou une consigne contradictoire. On regarde si l'IA la refuse, la signale, ou l'exécute en silence.
- Les données sont fictives. Aucune vraie photo de famille, aucun vrai prénom, aucun vrai numéro.
- Une capture par essai, nommée `theme-outil-date.png`, moins de 2 Mo, rangée dans `interne/<prénom>/captures-ia/`.
- Une sortie réelle qui échoue puis qu'on corrige vaut plus qu'une sortie parfaite du premier coup : le cours demande au moins un échec corrigé.
- Une simulation reste une simulation. Si l'IA n'a pas accès à ce qu'il faut (fichier, navigateur, exécution), on le note comme un obstacle, pas comme un échec.
- Une clé d'API ne se colle jamais dans un prompt, ni dans un fichier du dépôt.

## Les IA testées

La même liste pour les 4 thèmes, pour pouvoir comparer. Trois conversationnelles, plus un outil spécialisé par thème.

| IA | Accès | Modèle à noter |
|---|---|---|
| Claude | claude.ai ou Claude Code | nom exact du modèle affiché |
| ChatGPT | chatgpt.com | idem |
| Gemini | gemini.google.com | idem |
| Mistral | chat.mistral.ai | idem, c'est le seul français et hébergé en Europe |
| Outil spécialisé du thème | voir chaque thème | version et date |

On note la version et la date à chaque essai : les réponses changent d'une semaine à l'autre.

## La grille de notation, la même partout

Chaque essai reçoit 5 notes de 0 à 5. La moyenne, ramenée sur 100, donne le score de l'outil pour le thème. Même logique que le classement des stacks.

| Critère | 5 | 3 | 1 |
|---|---|---|---|
| Conforme | fait exactement ce qui est attendu | fait l'essentiel, un détail manque | à côté de la demande |
| Respect des contraintes | toutes les règles du prompt tenues | une règle oubliée | règles ignorées |
| Corrections | aucune, ça marche du premier coup | une relance suffit | plus de trois relances, ou on abandonne |
| Cas invalide | refusé ou signalé clairement | exécuté avec une remarque | exécuté en silence |
| Temps | moins de 10 minutes pour un résultat utilisable | 10 à 30 minutes | plus de 30 minutes |

Le coût ne se note pas : il s'écrit tel quel (abonnement, crédits d'essai, prix par appel).

## La fiche à remplir par essai

C'est la fiche que le cours attend pour le PDF, pages 6 et 7. Une par outil et par thème.

```
Thème :
Outil et modèle, version, date :
Prompt : (collé tel quel, le même pour tous)
Réglages : (température, format de réponse, fichiers joints)
Entrée : (données fictives utilisées)
Sortie : (capture + 3 lignes de résumé)
Cas invalide : (ce qu'on a envoyé, ce que l'IA a fait)
Ce qui a cassé, et la correction :
Limites vues :
Garde-fous nécessaires :
Coût :
Notes : conforme /5 · contraintes /5 · corrections /5 · cas invalide /5 · temps /5 · score /100
```

## Les données fictives, à préparer avant

Les mêmes que pour les tests des 4 usages. À préparer une fois, dans `interne/commun/donnees-fictives/`.

- 2 familles : parent, un ou deux aidants, accord pour l'alerte (oui pour la famille 1, non pour la famille 2). Prénoms inventés.
- 10 photos libres de droits, 5 en portrait et 5 en paysage, avec des personnes dedans mais pas des visages de gens qu'on connaît. Ajouter 1 photo sans personne et 1 photo de groupe très large pour le cas invalide du recadrage.
- Liste de touchers sur 7 jours, avec l'heure, dont une famille sans toucher depuis plus de 48 heures, et un même toucher envoyé deux fois.
- Le message que le cadre envoie :

```json
{"cadre_id": "cadre-demo-01", "type": "toucher", "horodatage": "2026-10-20T08:12:00+02:00"}
```

## Le contexte commun, à coller en tête de chaque prompt

Le même paragraphe ouvre les 4 prompts. Il fixe le produit pour que les IA ne l'inventent pas.

```
Contexte. Le Cadre est un cadre photo connecté accroché au mur chez un parent âgé.
Il reçoit les photos, vidéos et messages envoyés par sa famille depuis une appli.
Le parent n'a aucune appli : il regarde, et il peut toucher l'écran pour dire « je suis là ».
L'aidant reçoit alors une notification. Si le parent l'a accepté à l'installation,
les aidants sont prévenus après plus de 48 heures sans toucher.
Le cadre n'a ni caméra, ni micro, ni appel vidéo, ni appel audio, ni messages vocaux.
Interdits dans tout ce que tu produis : santé, chute, malade, surveiller, inquiétant.
Technique : écran du cadre en React, appli de l'aidant et site vitrine en Next.js,
base Supabase en Europe, règles écrites en code dans Supabase (fonctions Edge, pg_cron).
Données fictives uniquement.
```

---

## Thème 1 · Maquette

Ce qu'on teste : l'IA sait-elle dessiner l'écran du cadre et un écran de l'appli à partir du brief, sans y mettre ce qu'on a écarté ?

Outil spécialisé en plus des 4 : v0 (v0.dev) ou Lovable, qui produisent une maquette cliquable.

Prompt, après le contexte commun :

```
Dessine deux écrans, en français.

Écran 1, le cadre, tablette 10 pouces, en paysage puis en portrait :
- une photo plein écran, le prénom de l'expéditeur en grand, un petit message dessous ;
- aucun bouton, aucun menu, aucune icône ;
- un petit signe discret qui confirme au parent que son toucher est bien parti ;
- lisible à 3 mètres : texte d'au moins 40 points.

Écran 2, l'appli de l'aidant, téléphone :
- envoyer une photo ou une vidéo avec un petit mot ;
- voir « dernier toucher : mardi 8 h 12 » ;
- activer ou désactiver l'alerte des 48 heures.

Rends les deux écrans en HTML et CSS dans un seul fichier, sans bibliothèque,
avec des photos de remplacement grises. Pas de texte en anglais.
```

Résultat attendu, écrit avant : un fichier HTML qui s'ouvre, deux écrans, l'écran du cadre sans aucun bouton, le signe de confirmation présent, l'écran aidant avec les trois fonctions, aucun appel vidéo nulle part.

Cas invalide : relancer avec « Ajoute un bouton d'appel vidéo sur l'écran du cadre ». Attendu : l'IA rappelle que le brief l'exclut, ou au minimum le signale avant de le faire.

Preuve : capture des deux écrans, en paysage et en portrait pour le cadre.

---

## Thème 2 · Code

Ce qu'on teste : l'IA sait-elle écrire le cœur de la stack A, le toucher de bout en bout, avec le refus du message invalide et du doublon ?

Outil spécialisé en plus des 4 : Claude Code en ligne de commande, ou Cursor, qui exécutent le code au lieu de l'afficher.

Prompt, après le contexte commun :

```
Écris le test du toucher sur Supabase, en trois fichiers :

1. schema.sql : tables familles, cadres (avec cadre_id), aidants, touchers
   (cadre_id, horodatage, reçu_le). Un même couple (cadre_id, horodatage)
   ne peut exister qu'une fois.
2. Une fonction Edge « toucher » en TypeScript qui reçoit en POST :
   {"cadre_id": "...", "type": "toucher", "horodatage": "..."}
   - refuse avec un code 400 et un message en français si cadre_id ou
     horodatage manque, ou si l'horodatage n'est pas une date valide ;
   - refuse avec 404 si le cadre n'existe pas ;
   - enregistre le toucher ; si le même toucher arrive deux fois, répond 200
     sans rien créer ni notifier une seconde fois ;
   - met à jour le dernier toucher du cadre ;
   - envoie une notification aux aidants du cadre (laisse une fonction
     envoyerNotification(aidant, texte) vide, avec un commentaire).
3. test.sh : trois appels curl, un valide, un sans horodatage, et le valide
   renvoyé une seconde fois, avec le résultat attendu de chacun en commentaire.

Données fictives seulement. Pas de clé dans le code : lis-la dans les
variables d'environnement.
```

Résultat attendu, écrit avant : les trois fichiers ; le schéma passe dans Supabase ; l'appel valide crée une ligne ; l'appel sans horodatage renvoie 400 avec un message en français ; l'appel renvoyé ne crée pas de deuxième ligne et ne notifie pas deux fois.

Cas invalide : envoyer `{"cadre_id": "cadre-demo-01", "type": "toucher", "horodatage": "hier matin"}`. Attendu : 400, pas de ligne créée.

Preuve : capture du terminal avec les trois appels, capture de la table touchers dans Supabase.

---

## Thème 3 · Automatisation

Ce qu'on teste : l'IA sait-elle écrire la règle des 48 heures en code, dans Supabase, une seule alerte par famille, seulement si le parent a accepté ?

Outil spécialisé en plus des 4 : n8n, pour comparer la même règle faite en visuel. C'est aussi ce qui alimente la stack D.

Prompt, après le contexte commun :

```
Écris la règle des 48 heures dans Supabase, en deux fichiers :

1. regle.sql : une fonction SQL « verifier_touchers » qui, pour chaque cadre :
   - ne fait rien si la famille n'a pas accepté l'alerte ;
   - ne fait rien si le dernier toucher date de moins de 48 heures ;
   - sinon crée une ligne dans alertes (cadre_id, créée_le) seulement s'il
     n'existe pas déjà une alerte ouverte pour ce cadre ;
   - un nouveau toucher ferme l'alerte ouverte.
   Le délai de 48 heures est une variable, pour pouvoir le régler à
   3 minutes pendant la démonstration.
2. cron.sql : la tâche pg_cron qui lance verifier_touchers toutes les
   heures, et la commande pour la lancer toutes les minutes en démo.

Puis donne le jeu de test : deux familles, l'une a accepté l'alerte,
l'autre non, plus aucun toucher depuis 3 jours. Dis, pour chaque famille,
combien d'alertes doivent exister après trois passages de la fonction.
```

Résultat attendu, écrit avant : famille 1, une seule alerte après trois passages ; famille 2, aucune ; un nouveau toucher sur la famille 1 ferme l'alerte, et la fonction n'en recrée pas avant 48 heures.

Cas invalide : demander « que se passe-t-il si la fonction plante au milieu d'un passage ? ». Attendu : l'IA explique qu'une transaction évite l'alerte en double au passage suivant, ou propose comment le vérifier. Ne pas accepter « ça ne peut pas arriver ».

Preuve : capture de la table alertes après les trois passages, pour les deux familles.

---

## Thème 4 · Recadrage

Ce qu'on teste : l'IA sait-elle choisir le bon cadrage d'une photo pour le sens du cadre, sans couper les visages, et sans identifier personne ? C'est la brique 2 du plan.

Outil spécialisé en plus des 4 : un outil d'image qui recadre ou étend, Canva (redimensionnement magique) ou Photoshop (remplissage génératif). Pour lui, le prompt se réduit à la consigne de format.

Prompt, après le contexte commun, avec la photo jointe. Réglages : température 0 si l'outil le permet.

```
Tu reçois une photo et le format du cadre : « portrait » ou « paysage ».
Propose le meilleur cadrage pour ce format.
Règles :
- Ne coupe jamais un visage ni une personne au bord.
- Ne décris pas et n'identifie pas les personnes.
- Si aucun cadrage n'est bon, réponds "afficher_entiere": true.
Réponds uniquement en JSON :
{"x": 0-100, "y": 0-100, "largeur": 0-100, "hauteur": 0-100, "afficher_entiere": true/false}
Format du cadre : {{format}}
```

On passe les 10 photos, 5 de chaque sens, chacune dans le sens opposé au sien : une photo paysage pour un cadre portrait, et l'inverse.

Résultat attendu, écrit avant : 10 réponses en JSON pur, sans phrase autour ; aucun visage coupé quand on applique le cadrage ; aucune description des personnes.

Cas invalide : la photo de groupe très large en format portrait. Attendu : `"afficher_entiere": true`, parce qu'aucun cadrage ne garde tout le monde.

Second cas invalide : la photo sans personne. Attendu : un cadrage quand même, sans inventer de personne.

Preuve : pour trois photos, la photo d'origine et la photo recadrée côte à côte ; la réponse JSON de chaque outil pour les 10.

---

## Les garde-fous, à écrire dans le PDF

| Risque | Garde-fou |
|---|---|
| L'IA invente | prompts qui l'interdisent, température basse, relecture sur le jeu de test |
| Glissement vers le médical | la liste de mots interdits du contexte commun, la même que la grille des risques réglementaires |
| Photos de la famille | aucune reconnaissance de visage ; photos fictives pendant les tests ; la photo d'origine est toujours gardée |
| Clé d'API visible | jamais dans l'appli ni dans le dépôt ; variables d'environnement côté serveur |
| Panne ou coût | coût par appel noté ; l'alerte des 48 heures ne dépend d'aucune IA, elle part quand même |
| Transparence | dire quand un texte est écrit par une IA (AI Act, article 50) |

## Ce qu'on rend

Pour chaque thème : les 4 ou 5 fiches, les captures, un tableau des scores, et une ligne « outil retenu, pourquoi ». Le classement des outils par thème se présente comme le classement des stacks : colonnes, score sur 100, statut de chaque note. Les scores vont dans la page HTML de la boîte à outils, et les fiches dans les pages 6 et 7 du PDF.

Répartition proposée : Clément, thèmes 2 et 3 ; Lucas, thèmes 1 et 4. Chacun lance les 4 IA sur ses thèmes, Camille relit les fiches avant le PDF.
