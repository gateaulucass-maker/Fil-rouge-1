# Consignes pour tout agent IA (Codex, ChatGPT, Cursor, Gemini…)

Les règles de ce dépôt sont dans **[CLAUDE.md](CLAUDE.md)**. Lis-le en entier avant toute action : il s'applique à tous les agents, pas seulement à Claude.

Si tu ne peux pas le lire, respecte au minimum :
- Le dépôt est **public**. Ne jamais commiter de secret (mot de passe, clé, `.env`, chaîne de connexion), de coordonnées de l'équipe, de donnée personnelle de tiers, de PDF de cours.
- `git pull --rebase --autostash` avant de travailler, `git pull --rebase` avant de pousser. Jamais de `--force`, de `reset --hard` sur du travail poussé, ni de `--no-verify`.
- Écrire dans `interne/<prénom du membre>/` par défaut. Ne jamais modifier le dossier d'un autre membre.
- Ne pousser que si le membre le demande.
