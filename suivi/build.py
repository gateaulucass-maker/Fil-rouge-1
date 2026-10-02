"""Génère la page de suivi du projet à partir de suivi/taches.json.

  python3 suivi/build.py
Produit :
  - suivi.html (racine du dépôt, liens relatifs, page complète) ;
  - suivi/en-ligne.html (fragment publié sur claude.ai, liens vers GitHub).
Statuts : a_faire, en_cours, a_valider, termine, a_refaire, bloque.
"""
import json
from datetime import datetime
from html import escape
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/gateaulucass-maker/Fil-rouge-1/blob/main/"

STATUTS = [  # ordre d'affichage : ce qui demande une action d'abord
    ("bloque", "Bloqué"),
    ("a_valider", "À valider"),
    ("a_refaire", "À refaire"),
    ("en_cours", "En cours"),
    ("a_faire", "À faire"),
    ("termine", "Terminé"),
]
LIB = dict(STATUTS)
MOIS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]


def e(t):
    return escape("" if t is None else str(t), quote=True)


def date_fr(d):
    if not d:
        return ""
    x = datetime.fromisoformat(d)
    s = f"{x.day} {MOIS[x.month - 1]}"
    return s + (f" {x.year} · {x:%H:%M}" if "T" in d else "")


def lien(chemin, en_ligne):
    if not chemin:
        return ""
    href = GITHUB + chemin if en_ligne else chemin
    nom = chemin.rsplit("/", 1)[-1]
    return f'<a class="lk" href="{e(href)}">{e(nom)}</a>'


def pastille(statut):
    return f'<span class="st st-{statut}">{e(LIB[statut])}</span>'


def rendu(data, en_ligne):
    taches = [t for p in data["phases"] for t in p["taches"]]
    total = len(taches)
    compte = {s: sum(1 for t in taches if t["statut"] == s) for s, _ in STATUTS}

    barre = "".join(
        f'<span class="seg seg-{s}" style="flex:{n}" title="{e(LIB[s])} : {n}"></span>'
        for s, _ in STATUTS if (n := compte[s]))
    compteurs = "".join(
        f'<button type="button" class="ct" data-f="{s}" aria-pressed="false" id="f-{s}">'
        f'<span class="ct-n">{compte[s]}</span><span class="ct-l"><i class="dot dot-{s}"></i>{e(lib)}</span></button>'
        for s, lib in STATUTS)

    action = [(p, t) for p in data["phases"] for t in p["taches"] if t["statut"] in ("bloque", "a_valider", "a_refaire")]
    action.sort(key=lambda pt: [s for s, _ in STATUTS].index(pt[1]["statut"]))
    action_html = "".join(
        f'<li class="ac">{pastille(t["statut"])}<div class="ac-t"><b>{e(t["titre"])}</b>'
        f'<span>{e(t.get("note", ""))}</span></div><div class="ac-q">{e(t.get("qui", ""))}'
        f'{"<br>" + lien(t.get("lien"), en_ligne) if t.get("lien") else ""}</div></li>'
        for p, t in action) or '<li class="vide">Rien n\'attend ton action.</li>'

    phases_html = []
    for p in data["phases"]:
        lignes = []
        for t in p["taches"]:
            etapes = t.get("etapes") or []
            fait = sum(1 for s in etapes if s["statut"] == "termine")
            et_html = ""
            if etapes:
                items = "".join(
                    f'<li><i class="dot dot-{s["statut"]}" title="{e(LIB[s["statut"]])}"></i>'
                    f'<span class="et-t">{e(s["titre"])}{" · " + e(s["note"]) if s.get("note") else ""}</span>'
                    f'<span class="et-m">{e(s.get("qui", ""))}{" · " if s.get("qui") and s.get("date") else ""}{e(date_fr(s.get("date")))}'
                    f'{" · " + lien(s.get("lien"), en_ligne) if s.get("lien") else ""}</span></li>'
                    for s in etapes)
                et_html = (f'<details class="et"><summary>{fait} étape{"s" if fait > 1 else ""} terminée{"s" if fait > 1 else ""} '
                           f'sur {len(etapes)}</summary><ul>{items}</ul></details>')
            lignes.append(f"""<article class="tk" data-s="{t['statut']}">
<div class="tk-s">{pastille(t['statut'])}</div>
<div class="tk-c"><h3>{e(t['titre'])}</h3>{f'<p>{e(t["note"])}</p>' if t.get('note') else ''}{et_html}</div>
<div class="tk-m"><span class="k">Qui</span>{e(t.get('qui', '—'))}</div>
<div class="tk-m"><span class="k">Date</span>{e(date_fr(t.get('date'))) or '—'}</div>
<div class="tk-m"><span class="k">Fichier</span>{lien(t.get('lien'), en_ligne) or '—'}</div>
</article>""")
        phases_html.append(f"""<section class="ph" id="{e(p['id'])}">
<div class="ph-h"><span class="ph-id">{e(p['id'])}</span><h2>{e(p['titre'])}</h2><span class="ph-n">{len(p['taches'])} tâche{'s' if len(p['taches']) > 1 else ''}</span></div>
{''.join(lignes)}</section>""")

    termine = compte["termine"]
    return f"""<title>Suivi Fil rouge</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Thème unique blanc et bleu, voulu par Lucas. Grille suisse : colonne d'étiquettes à gauche, contenu à droite ; blanc et bleu, filets fins, l'état porté par la couleur des pastilles */
:root{{
  --bg:#ffffff; --fg:#0c1630; --muted:#5a6580; --hair:#d8deeb; --soft:#f2f5fc;
  --blue:#1838c8; --blue-ink:#ffffff;
  --s-a_faire:#7d879c; --s-en_cours:#1838c8; --s-a_valider:#a96300; --s-termine:#1b7a4b; --s-a_refaire:#c2361b; --s-bloque:#8c1430;
  --display:"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif; --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}}
:root{{color-scheme:light}} *{{box-sizing:border-box}} [hidden]{{display:none!important}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 var(--display);-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1180px;margin:0 auto;padding-inline:clamp(16px,4vw,48px);padding-block:clamp(28px,5vw,64px) 64px}}
a{{color:inherit}} a:focus-visible,button:focus-visible,summary:focus-visible{{outline:2px solid var(--blue);outline-offset:2px}}
.k{{font:11px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}}
.meta{{display:flex;flex-wrap:wrap;gap:6px 28px;font:11.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);border-top:3px solid var(--blue);padding-top:12px}}
.meta b{{color:var(--fg);font-weight:500}}
.hd{{display:grid;grid-template-columns:repeat(12,1fr);gap:0 24px;margin-top:clamp(24px,4vw,44px);align-items:end}}
h1{{grid-column:1/span 8;margin:0;font-weight:800;font-size:clamp(52px,10vw,128px);line-height:.86;letter-spacing:-.045em;color:var(--blue)}}
h1 span{{display:block;color:var(--fg)}}
.maj{{grid-column:9/span 4;text-align:right;min-width:0}}
.maj .v{{display:block;font:500 clamp(20px,2.4vw,28px)/1.1 var(--mono);color:var(--fg);margin-top:6px;font-variant-numeric:tabular-nums}}
.prog{{margin-top:clamp(32px,5vw,56px);border-top:1px solid var(--fg);padding-top:16px}}
.prog-h{{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;align-items:baseline}}
.prog-h b{{font-size:20px;letter-spacing:-.01em}}
.bar{{display:flex;height:14px;margin-top:12px;gap:2px}}
.seg{{display:block;min-width:6px}}
{''.join(f'.seg-{s},.dot-{s}{{background:var(--s-{s})}}' for s, _ in STATUTS)}
.cts{{display:grid;grid-template-columns:repeat(6,1fr);margin-top:18px;border-top:1px solid var(--hair)}}
.ct{{all:unset;cursor:pointer;display:flex;flex-direction:column;gap:2px;padding:12px 14px 14px 0;border-bottom:3px solid transparent}}
.ct+.ct{{padding-left:14px;border-left:1px solid var(--hair)}}
.ct:hover .ct-l{{color:var(--fg)}}
.ct[aria-pressed="true"]{{border-bottom-color:var(--blue)}}
.ct-n{{font-weight:800;font-size:clamp(28px,3.4vw,42px);line-height:1;letter-spacing:-.03em;font-variant-numeric:tabular-nums}}
.ct-l{{display:flex;align-items:center;gap:7px;font:11.5px var(--mono);letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}}
.dot{{display:inline-block;width:9px;height:9px;flex:none}}
.dot-a_faire{{background:transparent;box-shadow:inset 0 0 0 1.5px var(--s-a_faire)}}
.filt{{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:10px;font-size:13px;color:var(--muted)}}
.filt button{{all:unset;cursor:pointer;text-decoration:underline;text-underline-offset:3px;color:var(--blue)}}
section{{margin-top:clamp(44px,6vw,72px)}}
.blk-h{{display:grid;grid-template-columns:3fr 9fr;gap:0 24px;border-top:3px solid var(--fg);padding-top:14px}}
h2{{margin:0;font-weight:800;font-size:clamp(24px,3vw,36px);letter-spacing:-.025em;line-height:1.05;text-wrap:balance}}
.acs{{list-style:none;margin:16px 0 0;padding:0;display:grid;grid-template-columns:3fr 9fr;gap:0 24px}}
.ac{{grid-column:2;display:grid;grid-template-columns:118px 1fr 170px;gap:6px 16px;padding:14px 0;border-bottom:1px solid var(--hair);align-items:start}}
.ac-t{{min-width:0}} .ac-t b{{display:block;font-size:16px;letter-spacing:-.005em}} .ac-t span{{display:block;color:var(--muted);font-size:14px;margin-top:3px;max-width:70ch}}
.ac>.st,.tk-s>.st{{justify-self:start}} .ac-q{{font:12px var(--mono);color:var(--muted);text-align:right}}
.vide{{grid-column:2;padding:14px 0;color:var(--muted)}}
.st{{display:inline-block;font:500 10.5px var(--mono);letter-spacing:.07em;text-transform:uppercase;padding:4px 8px;white-space:nowrap;border:1.5px solid currentColor}}
{''.join(f'.st-{s}{{color:var(--s-{s})}}' for s, _ in STATUTS)}
.st-bloque{{background:var(--s-bloque);border-color:var(--s-bloque);color:var(--bg)}}
.st-a_refaire{{background:var(--s-a_refaire);border-color:var(--s-a_refaire);color:var(--bg)}}
.ph-h{{display:grid;grid-template-columns:3fr 5fr 1.6fr 1.2fr 1.6fr;gap:0 24px;border-top:3px solid var(--blue);padding-top:14px;align-items:baseline}}
.ph-h h2{{grid-column:2/span 3}} .ph-id{{font:500 13px var(--mono);color:var(--blue);letter-spacing:.06em}}
.ph-n{{font:12px var(--mono);color:var(--muted);text-align:right}}
.tk{{display:grid;grid-template-columns:3fr 5fr 1.6fr 1.2fr 1.6fr;gap:6px 24px;padding:18px 0;border-bottom:1px solid var(--hair);align-items:start}}
.tk>*{{min-width:0}}
.tk h3{{margin:0;font-size:17px;letter-spacing:-.01em;line-height:1.25;text-wrap:balance}}
.tk p{{margin:6px 0 0;color:var(--muted);font-size:14px;max-width:68ch}}
.tk-m{{font-size:13.5px;overflow-wrap:anywhere}} .tk-m .k{{display:block;margin-bottom:2px}}
.lk{{color:var(--blue);text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px;font:12.5px var(--mono)}}
.et{{margin-top:10px}}
.et summary{{cursor:pointer;font:12px var(--mono);color:var(--blue);list-style:none}}
.et summary::-webkit-details-marker{{display:none}} .et summary::before{{content:"+ "}} .et[open] summary::before{{content:"– "}}
.et ul{{list-style:none;margin:10px 0 0;padding:0;border-left:1px solid var(--hair)}}
.et li{{display:grid;grid-template-columns:20px 1fr;gap:2px 0;padding:6px 0 6px 12px;font-size:13.5px}}
.et li .dot{{margin-top:5px}} .et-t{{min-width:0}} .et-m{{grid-column:2;font:11.5px var(--mono);color:var(--muted)}}
.tk[hidden]{{display:none}}
footer{{margin-top:72px;border-top:1px solid var(--hair);padding-top:14px;font-size:12.5px;color:var(--muted);display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}}
@media (max-width:860px){{
  .ph-h{{grid-template-columns:auto 1fr auto}} .ph-h h2{{grid-column:auto}}
  .tk{{grid-template-columns:1fr 1fr 1fr}} .tk-s{{grid-column:1/-1}} .tk-c{{grid-column:1/-1}}
  .cts{{grid-template-columns:repeat(3,1fr)}} .ct:nth-child(4){{padding-left:0;border-left:0}}
  .ac{{grid-template-columns:1fr}} .ac-q{{text-align:left}}
}}
@media (max-width:640px){{
  .ph-h h2{{grid-column:1}}
  .hd,.blk-h,.acs,.ph-h{{grid-template-columns:1fr}} h1,.maj{{grid-column:1}} .maj{{text-align:left;margin-top:18px}}
  .ac,.vide{{grid-column:1}} .ph-n{{text-align:left}}
  .cts{{grid-template-columns:1fr 1fr}} .ct{{padding-left:0!important;border-left:0!important}}
}}
@media (prefers-reduced-motion:no-preference){{.seg{{transition:flex .3s}}}}
</style>
<div class="wrap">
<div class="meta"><span><b>Ynov</b> B2 Product Builder No-Code</span><span>{e(data['projet'])}</span><span>{total} tâches · {termine} terminées</span></div>

<header class="hd"><h1>Suivi<span>Fil rouge</span></h1>
<div class="maj"><span class="k">Dernière mise à jour</span><span class="v">{e(date_fr(data['mise_a_jour']))}</span></div></header>

<div class="prog">
<div class="prog-h"><b>Où en est le projet</b><span class="k">{total} tâches · filtre en cliquant un statut</span></div>
<div class="bar" role="img" aria-label="{' · '.join(f'{lib} {compte[s]}' for s, lib in STATUTS)}">{barre}</div>
<div class="cts" role="group" aria-label="Filtrer par statut">{compteurs}</div>
<div class="filt"><span id="filt-txt">Toutes les tâches affichées.</span><button type="button" id="filt-all" hidden>Tout afficher</button></div>
</div>

<section id="action"><div class="blk-h"><span class="k">À traiter</span><h2>Ce qui attend une action</h2></div>
<ul class="acs">{action_html}</ul></section>

{''.join(phases_html)}

<footer><span>Statuts : bloqué (attend une action extérieure) · à valider (par Lucas) · à refaire · en cours · à faire · terminé.</span>
<span>Page tenue à jour par Claude à chaque avancée.</span></footer>
</div>
<script>
(function(){{
  var btns=[].slice.call(document.querySelectorAll('.ct')),tks=[].slice.call(document.querySelectorAll('.tk')),
      txt=document.getElementById('filt-txt'),all=document.getElementById('filt-all'),
      libs={json.dumps(LIB, ensure_ascii=False)},cur=null;
  function apply(f){{
    cur=f;var n=0;
    tks.forEach(function(t){{var ok=!f||t.dataset.s===f;t.hidden=!ok;if(ok)n++;}});
    btns.forEach(function(b){{b.setAttribute('aria-pressed',String(b.dataset.f===f));}});
    document.querySelectorAll('.ph').forEach(function(p){{p.hidden=!p.querySelector('.tk:not([hidden])');}});
    txt.textContent=f?(n+' tâche'+(n>1?'s':'')+' « '+libs[f]+' » affichée'+(n>1?'s':'')+'.'):'Toutes les tâches affichées.';
    all.hidden=!f;
    try{{f?localStorage.setItem('suivi-filtre',f):localStorage.removeItem('suivi-filtre');}}catch(e){{}}
  }}
  btns.forEach(function(b){{b.addEventListener('click',function(){{apply(cur===b.dataset.f?null:b.dataset.f);}});}});
  all.addEventListener('click',function(){{apply(null);}});
  try{{var s=localStorage.getItem('suivi-filtre');if(s&&libs[s])apply(s);}}catch(e){{}}
}})();
</script>"""


def main():
    fichier = RACINE / "suivi" / "taches.json"
    data = json.loads(fichier.read_text(encoding="utf-8"))
    data["mise_a_jour"] = datetime.now().strftime("%Y-%m-%dT%H:%M")
    fichier.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    corps_local = rendu(data, en_ligne=False)
    (RACINE / "suivi.html").write_text(
        '<!doctype html>\n<html lang="fr"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        + corps_local.replace("<style>", "<style>\n", 1).replace("<div class=\"wrap\">", "</head><body><div class=\"wrap\">", 1)
        + "\n</body></html>\n", encoding="utf-8")
    (RACINE / "suivi" / "en-ligne.html").write_text(rendu(data, en_ligne=True), encoding="utf-8")
    print("suivi.html et suivi/en-ligne.html générés")


if __name__ == "__main__":
    main()
