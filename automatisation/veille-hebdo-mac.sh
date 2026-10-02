#!/bin/zsh
# Lance la veille hebdomadaire sur le Mac de Lucas (programmée par launchd chaque jeudi à 7h45).
# Le message de la veille (avec les adresses de l'équipe) est privé : ~/.config/fil-rouge/veille-message.txt
# Journal : ~/Library/Logs/veille-hebdo.log
# Essai sans prévenir l'équipe : ESSAI=1 automatisation/veille-hebdo-mac.sh
set -u
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
DEPOT="$HOME/Fil-rouge-1"
MESSAGE="$HOME/.config/fil-rouge/veille-message.txt"
LOG="$HOME/Library/Logs/veille-hebdo.log"
cd "$DEPOT" || exit 1
PROMPT="$(cat "$MESSAGE")"
if [ "${ESSAI:-0}" = "1" ]; then
  PROMPT="$PROMPT

ESSAI : cette exécution est un test. Envoie l'email UNIQUEMENT à la première adresse de la liste de l'équipe (celle de Lucas), pas aux autres et commence son objet par « [Essai] ». Tout le reste se fait normalement."
fi
{
  echo "===== $(date '+%Y-%m-%d %H:%M') : veille hebdo ${ESSAI:+(essai)} ====="
  claude -p "$PROMPT" --model sonnet \
    --allowedTools "Bash" "Read" "Write" "Edit" "Glob" "Grep" "WebSearch" "WebFetch" "Agent" "ToolSearch" \
                   "mcp__claude_ai_Neon" "mcp__claude_ai_Gmail__send_message" \
    --permission-mode acceptEdits
  echo "===== fin $(date '+%H:%M') (code $?) ====="
} >> "$LOG" 2>&1
