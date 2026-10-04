#!/bin/sh
# Hook Claude Code (PreToolUse, Bash) : avant qu'un agent lance « git commit »,
# lance le contrôle et interdit le contournement par --no-verify.
entree=$(cat)
case "$entree" in
  *"git commit"*) ;;
  *) exit 0 ;;
esac
# Options de « git commit » seulement : on coupe ce qui précède,
# puis le message (-m, -F, heredoc) et les commandes suivantes (&&, ;, |)
options=$(printf '%s' "$entree" | sed -e 's/.*git commit//' -e 's/ -m .*//' -e 's/ -F .*//' -e 's/ --message.*//' -e 's/<<.*//' -e 's/&&.*//' -e 's/;.*//' -e 's/|.*//')
case "$options" in
  *"--no-verify"*|*" -n "*|*" -n")
    echo "Interdit : un agent ne contourne jamais le contrôle avant commit (CLAUDE.md, section 1). Demande au membre." >&2
    exit 2 ;;
esac
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
sh automatisation/hooks/verifier-commit.sh || exit 2
exit 0
