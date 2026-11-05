#!/bin/bash
# Rendu d'une planche seule en PNG 1920x1080 : _src/check.sh 06 /chemin/sortie.png
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"
N=$(printf %02d "$((10#$1))"); OUT="$2"
TMP="$(dirname "$OUT")/raw-$N.html"
python3 "$HERE/_src/build.py" --only "$N" --out "$TMP" >/dev/null
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --user-data-dir="$(dirname "$OUT")/chrome-$N" --window-size=1920,1080 --virtual-time-budget=6000 \
  --screenshot="$OUT" "file://$TMP" >/dev/null 2>&1
echo "$OUT"
