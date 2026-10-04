#!/bin/sh
# Contrôle avant commit (CLAUDE.md, section 1) : le dépôt est public.
# Lit uniquement ce qui est prêt à être commité (git add). Ne touche à aucun fichier.
# Bloque : secrets, e-mails, téléphones, .env, clés, PDF hors rendus/, fichiers de plus de 2 Mo.

TAILLE_MAX=2097152
problemes=""

signaler() { problemes="${problemes}
  - $1"; }

# Masque une valeur trouvée pour ne pas la réafficher en clair
masquer() { printf '%s' "$1" | cut -c1-6 | sed 's/$/***/'; }

fichiers=$(git diff --cached --name-only --diff-filter=ACMR)
[ -z "$fichiers" ] && exit 0

OLDIFS=$IFS
IFS='
'
for f in $fichiers; do
  # 1. Fichiers interdits par leur nom ou leur taille
  case "$f" in
    *.env.example) ;;
    .env|*/.env|.env.*|*/.env.*) signaler "$f : fichier .env (secrets), il reste en local" ;;
  esac
  case "$f" in
    *.pem|*.key) signaler "$f : fichier de clé, il reste en local" ;;
  esac
  case "$f" in
    */rendus/*.pdf|*/rendus/*.PDF) ;;
    *.pdf|*.PDF) signaler "$f : PDF hors rendus/ (cours, documents), il reste en local" ;;
  esac
  taille=$(git cat-file -s ":$f" 2>/dev/null || echo 0)
  [ "$taille" -gt "$TAILLE_MAX" ] && signaler "$f : fichier lourd ($((taille / 1048576)) Mo, maximum 2 Mo), il reste en local"

  # 2. Contenu ajouté (exemples et tests de l'anonymisation exclus)
  case "$f" in
    *.env.example|*/tests/*|automatisation/hooks/*) continue ;;
  esac
  ajouts=$(git diff --cached -U0 --no-color -- "$f" | grep '^+' | grep -v '^+++')
  [ -z "$ajouts" ] && continue

  for m in $(printf '%s\n' "$ajouts" | grep -oE 'postgres(ql)?://[^:/ ]+:[^@ ]+@[^ ]+|sk-ant-[A-Za-z0-9_-]{10,}|sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|xox[abp]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY'); do
    signaler "$f : secret probable ($(masquer "$m"))"
  done
  for m in $(printf '%s\n' "$ajouts" | grep -ioE '(api[_-]?key|secret|token|password|passwd|mot[_ ]de[_ ]passe)["'\'' ]*[:=][ ]*["'\''][^"'\'' ]{8,}'); do
    signaler "$f : mot de passe ou clé en clair ($(masquer "$m"))"
  done
  for m in $(printf '%s\n' "$ajouts" | grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' | grep -viE 'noreply|no-reply|@example\.|@exemple\.'); do
    signaler "$f : adresse e-mail ($(masquer "$m"))"
  done
  for m in $(printf '%s\n' "$ajouts" | grep -oE '(^|[^0-9])(\+33[ .]?|0)[1-9]([ .-]?[0-9]{2}){4}([^0-9]|$)' | tr -d ' .-'); do
    signaler "$f : numéro de téléphone ($(masquer "$m"))"
  done
done
IFS=$OLDIFS

[ -z "$problemes" ] && exit 0

cat >&2 <<MSG
COMMIT BLOQUÉ : le dépôt est public (CLAUDE.md, section 1).
$problemes

Que faire :
  - Retirer l'élément du fichier, ou retirer le fichier du commit : git restore --staged <fichier>
  - Les fichiers restent sur ton ordinateur, rien n'est supprimé.
  - Faux positif (ex. numéro d'entreprise public) : le membre vérifie lui-même,
    puis commite à la main avec --no-verify. Un agent IA ne le fait jamais.
MSG
exit 1
