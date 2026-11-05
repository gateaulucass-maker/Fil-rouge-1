#!/usr/bin/env python3
"""Assemble la présentation DA Soly.

Usage :
  python3 _src/build.py                      -> écrit index.html (toutes les slides)
  python3 _src/build.py --only 06 --out x.html -> une seule slide (pour vérifier)

Chaque slide est un fragment slides/NN.html contenant UNE balise
<section class="slide" data-s="NN" data-title="..."> ... </section>.
"""
import argparse
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHELL = ROOT / "_src" / "shell.html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="numéro de slide, ex. 06")
    ap.add_argument("--out", help="fichier de sortie")
    a = ap.parse_args()

    files = sorted((ROOT / "slides").glob("[0-9][0-9].html"))
    if a.only:
        files = [f for f in files if f.stem == a.only.zfill(2)]
        if not files:
            raise SystemExit(f"slides/{a.only}.html introuvable")

    parts = []
    for f in files:
        html = f.read_text(encoding="utf-8").strip()
        if not re.search(r'<section class="slide[^"]*" data-s="%s"' % f.stem, html):
            raise SystemExit(f"{f.name} : la balise <section class=\"slide\" data-s=\"{f.stem}\"> manque")
        parts.append(html)

    out = pathlib.Path(a.out) if a.out else ROOT / "index.html"
    shell = SHELL.read_text(encoding="utf-8")
    base = "" if not a.out else f'<base href="{ROOT.as_uri()}/">'
    page = shell.replace("<!--BASE-->", base).replace("<!--SLIDES-->", "\n\n".join(parts))
    if a.only:
        page = page.replace("<html lang=\"fr\">", "<html lang=\"fr\" data-raw>")
    out.write_text(page, encoding="utf-8")
    print(f"{out} : {len(parts)} slide(s)")


if __name__ == "__main__":
    main()
