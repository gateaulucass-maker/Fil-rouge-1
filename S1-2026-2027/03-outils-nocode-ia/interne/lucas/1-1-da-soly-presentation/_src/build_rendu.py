#!/usr/bin/env python3
"""Génère les deux pages de rendu DA Soly (onglets, animations).

  python3 _src/build_rendu.py

Écrit, dans interne/lucas/ (à côté de img-da/ et du prototype) :
  1-1-soly-rendu-da.html           DA seule
  1-1-soly-rendu-da-maquette.html  DA + maquette interactive intégrée
"""
import html
import pathlib
import re

D = pathlib.Path(__file__).resolve().parent.parent
OUT = D.parent
TPL = (D / "_src" / "rendu.html").read_text(encoding="utf-8")
PROTO = OUT / "1-1-soly-prototype-interactif-v4.html"

SLIDES = {}
for f in sorted((D / "slides").glob("[0-9][0-9].html")):
    s = f.read_text(encoding="utf-8").strip()
    t = re.search(r'data-title="([^"]*)"', s).group(1)
    SLIDES[f.stem] = (t, s)

GROUP = {}
for n in ["01", "02", "03", "04", "05"]:
    GROUP[n] = "id"
for n in ["06", "07", "08", "09"]:
    GROUP[n] = "ct"
for n in ["10", "11", "12", "13"]:
    GROUP[n] = "ui"
for n in [f"{i:02d}" for i in range(14, 25)]:
    GROUP[n] = "ap"

PALETTE = [
    ("Aube", "#FFFAF0", "Fond principal", "Encre 16,6 : 1", "#1F1A17"),
    ("Crème", "#FFF3D9", "Fond des cartes", "Encre 15,7 : 1", "#1F1A17"),
    ("Encre", "#1F1A17", "Texte et boutons", "Sur aube 16,6 : 1", "#FFFAF0"),
    ("Café doux", "#6A5F55", "Texte secondaire", "Sur aube 6,0 : 1", "#FFFAF0"),
    ("Soleil", "#FFD36E", "Lumière, le point du logo", "Jamais en texte", "#1F1A17"),
    ("Pêche", "#FFC9A3", "Accent chaud", "Encre 11,6 : 1", "#1F1A17"),
    ("Lilas", "#C9B8F0", "Accent doux", "Encre 10,2 : 1", "#1F1A17"),
    ("Ligne", "#F0E3C8", "Filets et bordures", "Décoratif", "#1F1A17"),
]

MAQ_PANEL = """<!-- ======================= MAQUETTE ======================= -->
<section class="panel" id="maquette" role="tabpanel" aria-labelledby="t-maquette">
  <div class="head">
    <div><div class="lab rv">04 · Maquette interactive</div><h2 class="rv" style="--d:1">La DA, appliquée écran par écran.</h2><p class="intro rv" style="--d:2">Le cadre au mur et l’application de la famille, reliés. Lancez un scénario, ou touchez directement le téléphone et le cadre.</p></div>
    <aside class="rv" style="--d:3"><b>Prototype v4</b>28 écrans d’application, 3 états du cadre, 5 scénarios guidés.</aside>
  </div>
  <div class="steps">
    <div class="step rv"><span class="n">1</span><b>Installer</b><span>« Parcours d’installation » : le cadre affiche un code, l’appli le scanne.</span></div>
    <div class="step rv" style="--d:1"><span class="n">2</span><b>Faire signe</b><span>« Le parent touche le cadre » : le signe arrive dans l’appli.</span></div>
    <div class="step rv" style="--d:2"><span class="n">3</span><b>Le moment du jour</b><span>Une notification douce, une photo à partager.</span></div>
    <div class="step rv" style="--d:3"><span class="n">4</span><b>Rassurer</b><span>« 48 h sans toucher » : la famille est prévenue, sans alarme.</span></div>
  </div>
  <div class="mq-frame rv"><iframe id="mq" title="Maquette interactive Soly v4"></iframe></div>
  <div class="links"><a class="btn o" href="1-1-soly-prototype-interactif-v4.html" target="_blank" rel="noopener">Ouvrir la maquette seule</a></div>
</section>
<textarea hidden id="mqsrc">%s</textarea>
"""

INJECT = """<style>
.w>.eb,.w>h1,.w>.lead{display:none!important}
body{padding-top:24px!important;padding-bottom:24px!important;background:#FFFAF0}
</style>
<script>
(function(){function send(){var h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight);parent.postMessage({soly:"mqh",h:h},"*")}
addEventListener("load",function(){send();new ResizeObserver(send).observe(document.body);[300,1000,2500].forEach(function(t){setTimeout(send,t)})});
if(document.fonts)document.fonts.ready.then(send)})();
</script>
"""


def tabs_html(tabs):
    out = []
    for i, (tid, label) in enumerate(tabs):
        num = f'<span class="n">{i:02d}</span>' if 0 < i < len(tabs) - 1 else ""
        out.append(
            f'      <button class="tab" role="tab" id="t-{tid}" data-tab="{tid}" '
            f'data-label="{label}" aria-controls="{tid}" aria-selected="false" tabindex="-1">{num}{label}</button>'
        )
    return "\n".join(out)


def map_html(tabs):
    desc = {
        "identite": "Trois principes, le logo et ses déclinaisons.",
        "couleurs": "Huit couleurs, la lumière, deux polices.",
        "interface": "Composants vivants, cas d’usage, à faire et à éviter.",
        "maquette": "Le prototype interactif, intégré à la page.",
        "applications": "Le cadre, l’appli, les réseaux, le print.",
        "planches": "Les 24 planches Figma, filtrables et agrandissables.",
    }
    out = []
    for i, (tid, label) in enumerate(tabs[1:], 1):
        n = f"{i:02d}" if i < len(tabs) - 1 else "Annexe"
        out.append(
            f'      <button class="go rv" style="--d:{i-1}" data-goto="{tid}"><span class="num">{n}</span>'
            f"<b>{label}</b><span>{desc[tid]}</span><span class=\"arr\">Ouvrir →</span></button>"
        )
    return "\n".join(out)


def palette_html():
    out = []
    for i, (name, hx, role, note, fg) in enumerate(PALETTE):
        border = "box-shadow:inset 0 -1px 0 #F0E3C8;" if hx in ("#FFFAF0",) else ""
        out.append(
            f'    <button class="chip-c rv" style="--d:{i % 4}" data-hex="{hx}" data-name="{name}" '
            f'aria-label="{name} {hx}, copier">'
            f'<span class="sw" style="background:{hx};color:{fg};{border}"><em>Copier</em></span>'
            f'<span class="tx" style="display:block"><b>{name}<code>{hx}</code></b><p>{role}</p><small>{note}</small></span></button>'
        )
    return "\n".join(out)


def pl(nums):
    return "".join(f'<button class="pl" data-n="{n}"></button>' for n in nums.split(","))


def all_html():
    out = []
    for i, (n, (t, _)) in enumerate(SLIDES.items()):
        out.append(
            f'    <div class="it rv" style="--d:{i % 3}" data-g="{GROUP[n]}"><button class="pl" data-n="{n}"></button>'
            f"<p><span>{n}</span>{html.escape(t)}</p></div>"
        )
    return "\n".join(out)


def build(with_mq):
    tabs = [("projet", "Projet"), ("identite", "Identité"), ("couleurs", "Couleurs et typo"), ("interface", "Interface")]
    if with_mq:
        tabs.append(("maquette", "Maquette"))
    tabs += [("applications", "Applications"), ("planches", "Planches")]
    page = TPL
    rep = {
        "<!--TITLE-->": "Soly, DA et maquette" if with_mq else "Soly, direction artistique",
        "<!--DESC-->": "direction artistique et maquette interactive" if with_mq else "direction artistique",
        "<!--TABS-->": tabs_html(tabs),
        "<!--META-->": "DA v2 + maquette v4" if with_mq else "DA v2",
        "<!--HERO_LAB-->": " · Maquette v4" if with_mq else "",
        "<!--MAP_TITLE-->": "Six onglets, de l’idée à l’écran." if with_mq else "Cinq onglets, de l’idée à l’objet.",
        "<!--MAP-->": map_html(tabs),
        "<!--PALETTE-->": palette_html(),
        "<!--APP_NUM-->": "05" if with_mq else "04",
        "<!--ALL-->": all_html(),
        "<!--FOOT_SRC-->": ", maquette interactive v4" if with_mq else "",
        "<!--SLIDES-->": "\n".join(s for _, s in SLIDES.values()),
    }
    if with_mq:
        proto = PROTO.read_text(encoding="utf-8").replace("</head>", INJECT + "</head>", 1)
        rep["<!--MAQUETTE_PANEL-->"] = MAQ_PANEL % html.escape(proto, quote=False)
    else:
        rep["<!--MAQUETTE_PANEL-->"] = ""
    for k, v in rep.items():
        page = page.replace(k, v)
    page = re.sub(r"<!--PL:([0-9,]+)-->", lambda m: pl(m.group(1)), page)
    left = re.findall(r"<!--[A-Z_:]+-->", page)
    if left:
        raise SystemExit(f"marqueurs non remplacés : {left}")
    name = "1-1-soly-rendu-da-maquette.html" if with_mq else "1-1-soly-rendu-da.html"
    (OUT / name).write_text(page, encoding="utf-8")
    print(f"{OUT / name} : {len(page) // 1024} Ko, {len(tabs)} onglets")


if __name__ == "__main__":
    build(False)
    build(True)
