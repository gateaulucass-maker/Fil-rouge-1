"""Rapport HTML hebdomadaire, statique et autonome (rapports/rapport-AAAA-Sxx.html).

Sections : synthèse de l'agent (à vérifier), faits par axe avec score, signaux
groupés par irritant, couverture du catalogue, journal des runs. Tout est échappé.
"""
import argparse
import re
from collections import defaultdict
from datetime import date

from common import RACINE, connexion, echapper as e, niveau, regles
from coverage import couverture

AXES = {"marche": "Marché", "concurrence": "Concurrence", "usagers": "Usagers",
        "techno": "Technologie", "reglementaire": "Réglementaire"}
IRRITANTS = {"stigmatisation": "Stigmatisation", "complexite": "Complexité", "fausses_alertes": "Fausses alertes",
             "prix_abonnement": "Prix / abonnement", "intrusion_vie_privee": "Intrusion dans la vie privée",
             "fiabilite_technique": "Fiabilité technique", "service_client": "Service client", "autre": "Autre"}

CSS = """
:root{--bg:#fff;--fg:#111418;--muted:#5d636b;--hair:#d5d7d9;--soft:#f4f4f2;--orange:#e8571c;--blue:#1f3fbf;
--ok:#1d7a46;--warn:#a86400;--low:#8a8f96;--display:"Archivo","Helvetica Neue",Arial,sans-serif;
--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#0f1113;--fg:#ecedee;--muted:#9aa0a6;--hair:#2c3035;--soft:#181b1e;
--orange:#ff7a45;--blue:#7d95ff;--ok:#4cc38a;--warn:#e0a040;--low:#7b8188;color-scheme:dark}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 var(--display);
-webkit-font-smoothing:antialiased}
.wrap{max-width:1100px;margin:0 auto;padding:clamp(24px,5vw,64px) clamp(16px,4vw,48px) 48px}
.meta{display:flex;flex-wrap:wrap;gap:6px 28px;font:11.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;
color:var(--muted);border-top:2px solid var(--fg);padding-top:12px}.meta b{color:var(--fg);font-weight:500}
h1{font-weight:800;font-size:clamp(38px,7vw,84px);line-height:.95;letter-spacing:-.035em;margin:28px 0 0}
h1 .o{color:var(--orange)}h1 .bl{color:var(--blue)}
h2{font-size:clamp(22px,2.6vw,30px);letter-spacing:-.02em;margin:56px 0 0;padding-top:14px;border-top:2px solid var(--fg);
display:flex;justify-content:space-between;gap:12px;align-items:baseline}
h2 small{font:11.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:400}
h3{font-size:16px;margin:28px 0 8px;display:flex;gap:10px;align-items:baseline}
h3 i{font:normal 11px var(--mono);color:var(--muted)}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1px;background:var(--hair);
border:1px solid var(--hair);margin-top:32px}
.kpi{background:var(--bg);padding:14px 16px}.kpi .n{font-size:30px;font-weight:800;font-variant-numeric:tabular-nums;
letter-spacing:-.02em}.kpi .k{font:11px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.synth{background:var(--soft);border-left:4px solid var(--orange);padding:4px 20px 12px;margin-top:16px}
.synth h4{font-size:15px;margin:16px 0 4px}.synth ul{padding-left:20px;margin:6px 0}.synth p{margin:8px 0}
.warn{display:inline-block;font:11px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--orange);
border:1px solid var(--orange);padding:2px 8px;margin-top:14px}
.item{border-bottom:1px solid var(--hair);padding:14px 0;display:grid;grid-template-columns:64px 1fr;gap:14px}
.item>*{min-width:0}
.score{font:700 20px var(--mono);text-align:center;padding:6px 0;border:2px solid currentColor;height:fit-content}
.score small{display:block;font-size:9.5px;font-weight:500;letter-spacing:.06em;text-transform:uppercase}
.s-prioritaire{color:var(--ok)}.s-a_verifier{color:var(--warn)}.s-faible{color:var(--low)}
.item .t{font-weight:700;line-height:1.3}.item .t a{color:inherit;text-decoration-color:var(--hair);text-underline-offset:3px}
.item .t a:hover{text-decoration-color:var(--orange)}
.item .src{font:11.5px var(--mono);color:var(--muted);margin-top:2px;overflow-wrap:anywhere}
.item p{margin:6px 0 0;max-width:75ch}.item .why{color:var(--muted)}
.badges{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.b{font:11px var(--mono);letter-spacing:.04em;border:1px solid var(--hair);padding:1px 7px;white-space:nowrap}
.b.sens{border-color:var(--orange);color:var(--orange)}.b.eth{border-color:var(--blue);color:var(--blue)}
.chiffres{margin:6px 0 0;padding-left:18px;font-size:14px}
.irr{margin-top:22px}.irr h3{margin:0 0 6px}.bar{height:8px;background:var(--blue);margin:4px 0 10px}
blockquote{margin:8px 0;padding:6px 14px;border-left:3px solid var(--blue);color:var(--muted);font-style:italic}
table{width:100%;border-collapse:collapse;margin-top:16px;font-size:14px}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--hair);vertical-align:top}
th{font:11px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
td.n{font-variant-numeric:tabular-nums;text-align:right;font-weight:700}
tr.trou td{background:color-mix(in srgb,var(--orange) 10%,transparent)}tr.trou td:first-child{box-shadow:inset 3px 0 var(--orange)}
.tbl{overflow-x:auto}.empty{color:var(--muted);font-style:italic}
footer{margin-top:64px;border-top:1px solid var(--hair);padding-top:14px;font-size:12.5px;color:var(--muted)}
@media (max-width:640px){.item{grid-template-columns:52px 1fr;gap:10px}.score{font-size:16px}
.hide-m{display:none}}
"""


def md_simple(texte: str) -> str:
    """Markdown minimal (titres, listes, gras, paragraphes) -> HTML échappé."""
    sortie, liste = [], False
    for ligne in texte.splitlines():
        l = ligne.strip()
        if l.startswith(("- ", "* ")):
            if not liste:
                sortie.append("<ul>"); liste = True
            sortie.append(f"<li>{_inline(l[2:])}</li>")
            continue
        if liste:
            sortie.append("</ul>"); liste = False
        if not l:
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", l)
        if m:
            if len(m.group(1)) > 1:  # le titre de niveau 1 est déjà dans la page
                sortie.append(f"<h4>{_inline(m.group(2))}</h4>")
        else:
            sortie.append(f"<p>{_inline(l)}</p>")
    if liste:
        sortie.append("</ul>")
    return "\n".join(sortie)


def _inline(t: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(t))


def carte(it, r) -> str:
    score, flux = it["score_fiabilite"], it["flux"]
    if flux == "fait":
        niv = niveau(score, r)
        lib = {"prioritaire": "prior.", "a_verifier": "à vérif.", "faible": "faible"}[niv]
        badge = f'<div class="score s-{niv}" title="autorité {it["autorite"]} + fraîcheur {it["fraicheur"]} + source primaire {it["bonus_source_primaire"]}">{e(score)}<small>/7 {lib}</small></div>'
    else:
        badge = '<div class="score s-faible">S<small>signal</small></div>'
    badges = [f'<span class="b">#{e(it["id"])}</span>', f'<span class="b">{e(it["code_info"] or "—")}</span>']
    if it["pertinence_proposee"]:
        badges.append(f'<span class="b">pertinence {e(it["pertinence_proposee"])}/3</span>')
    if it["archetype"]:
        badges.append(f'<span class="b">{e(it["archetype"])}</span>')
    if it["sensible"]:
        badges.append('<span class="b sens">sensible</span>')
    if it["ethique"]:
        badges.append('<span class="b eth">éthique</span>')
    chiffres = "".join(f"<li><b>{e(c['valeur'])}</b> — {e(c.get('contexte', ''))} <span class=\"src\">({e(c['source_citee'])})</span></li>"
                       for c in it["chiffres"] or [])
    primaire = (f'<div class="src">Source primaire : <a href="{e(it["source_primaire_url"])}">{e(it["source_primaire_url"])}</a></div>'
                if it["source_primaire_url"] else "")
    return f"""<article class="item">{badge}<div>
<div class="t"><a href="{e(it['url'])}" rel="noopener">{e(it['titre'])}</a></div>
<div class="src">{e(it['source_nom'] or '')} · {e(it['publie_le'] or 'non daté')}</div>
{f'<p>{e(it["resume"])}</p>' if it['resume'] else ''}
{f'<p class="why">→ {e(it["pourquoi_important"])}</p>' if it['pourquoi_important'] else ''}
{f'<ul class="chiffres">{chiffres}</ul>' if chiffres else ''}{primaire}
<div class="badges">{''.join(badges)}</div></div></article>"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sortie", help="chemin du fichier HTML (défaut : rapports/rapport-AAAA-Sxx.html)")
    a = p.parse_args()
    r = regles()
    annee, semaine, _ = date.today().isocalendar()
    tag = f"{annee}-S{semaine:02d}"
    sortie = a.sortie or str(RACINE / "rapports" / f"rapport-{tag}.html")

    cles = ("id", "axe", "code_info", "flux", "score_fiabilite", "autorite", "fraicheur", "bonus_source_primaire",
            "pertinence_proposee", "titre", "url", "source_nom", "publie_le", "resume", "pourquoi_important",
            "source_primaire_url", "chiffres", "archetype", "ethique", "sensible", "irritant", "verbatim", "statut")
    with connexion() as cx:
        items = [dict(zip(cles, l)) for l in cx.execute(
            f"""SELECT {', '.join(cles)} FROM veille_items WHERE statut IN ('a_revoir', 'valide')
                ORDER BY score_fiabilite DESC NULLS LAST, pertinence_proposee DESC NULLS LAST, id""").fetchall()]
        cov = couverture(cx)
        stats = cx.execute("""SELECT
              (SELECT count(*) FROM raw_items),
              (SELECT count(*) FROM raw_items WHERE etat = 'filtre'),
              (SELECT count(*) FROM veille_items WHERE statut <> 'hors_sujet'),
              (SELECT count(*) FROM veille_items WHERE statut = 'hors_sujet'),
              (SELECT count(*) FROM veille_items WHERE statut = 'valide'),
              (SELECT count(*) FROM raw_items WHERE etat = 'a_qualifier')""").fetchone()
        runs = cx.execute("""SELECT id, demarre_le, collectes, nb_filtres, nb_qualifies, nb_hors_sujet, modele,
                                    duree_secondes, notes FROM runs ORDER BY id DESC LIMIT 8""").fetchall()

    fichier_synth = RACINE / "rapports" / f"synthese-{tag}.md"
    synthese = md_simple(fichier_synth.read_text(encoding="utf-8")) if fichier_synth.exists() \
        else '<p class="empty">Pas encore de synthèse de l\'agent rapporteur pour cette semaine.</p>'

    faits = [i for i in items if i["flux"] == "fait"]
    forts = [i for i in faits if i["score_fiabilite"] is not None and i["score_fiabilite"] >= r["score"]["seuils"]["a_verifier"]]
    faibles = [i for i in faits if i not in forts]
    par_axe = defaultdict(list)
    for i in forts:
        par_axe[i["axe"]].append(i)

    html_axes = []
    for axe, nom in AXES.items():
        liste = par_axe.get(axe, [])
        corps = "".join(carte(i, r) for i in liste) or '<p class="empty">Aucun fait fiable cette semaine.</p>'
        html_axes.append(f'<h3>{e(nom)} <i>{len(liste)}</i></h3>{corps}')

    signaux = defaultdict(list)
    for i in items:
        if i["flux"] == "signal":
            signaux[i["irritant"] or "autre"].append(i)
    max_sig = max((len(v) for v in signaux.values()), default=1)
    html_sig = []
    for irr, liste in sorted(signaux.items(), key=lambda kv: -len(kv[1])):
        verb = "".join(f'<blockquote>« {e(i["verbatim"])} » <span class="src">— #{e(i["id"])}, {e(i["source_nom"])}</span></blockquote>'
                       for i in liste[:4] if i["verbatim"])
        html_sig.append(f'<div class="irr"><h3>{e(IRRITANTS.get(irr, irr))} <i>{len(liste)} occurrence(s)</i></h3>'
                        f'<div class="bar" style="width:{max(8, 100 * len(liste) // max_sig)}%"></div>{verb}</div>')

    lignes_cov = "".join(
        f'<tr class="{"trou" if c["statut"] == "requis" and c["valides"] == 0 else ""}"><td><b>{e(c["code"])}</b></td>'
        f'<td>{e(c["libelle"])}</td><td class="hide-m">{e(c["statut"])}</td><td class="n">{e(c["valides"])}</td>'
        f'<td class="n">{e(c["a_revoir"])}</td></tr>' for c in cov)
    trous = [c["code"] for c in cov if c["statut"] == "requis" and c["valides"] == 0]

    lignes_runs = "".join(
        f'<tr><td>#{e(rn[0])}</td><td>{e(rn[1].strftime("%d/%m/%Y %H:%M"))}</td>'
        f'<td>{e(", ".join(f"{k} {v}" for k, v in (rn[2] or {}).items()))}</td><td class="n">{e(rn[3])}</td>'
        f'<td class="n">{e(rn[4])}</td><td class="n">{e(rn[5])}</td><td class="hide-m">{e(rn[6])}</td>'
        f'<td class="hide-m">{e(rn[8] or "")}</td></tr>' for rn in runs)

    total, filtres, qualifies, hors_sujet, valides, restants = stats
    page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Veille silver tech · {e(tag)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;700;800&family=IBM+Plex+Mono:wght@400;500;700&display=swap">
<style>{CSS}</style></head><body><div class="wrap">
<div class="meta"><span><b>Ynov</b> B2 Product Builder No-Code</span><span>PFR Générations Connectées</span>
<span>Phase 1 · Veille</span><span>Semaine {e(tag)}</span><span>Généré le {e(date.today().strftime("%d/%m/%Y"))}</span></div>
<h1><span class="o">Veille</span><br><span class="bl">silver tech</span></h1>

<div class="kpis">
<div class="kpi"><div class="n">{e(total)}</div><div class="k">collectés</div></div>
<div class="kpi"><div class="n">{e(filtres)}</div><div class="k">filtrés sans IA</div></div>
<div class="kpi"><div class="n">{e(qualifies)}</div><div class="k">qualifiés</div></div>
<div class="kpi"><div class="n">{e(hors_sujet)}</div><div class="k">hors sujet (IA)</div></div>
<div class="kpi"><div class="n">{e(valides)}</div><div class="k">validés humain</div></div>
<div class="kpi"><div class="n">{e(len(trous))}</div><div class="k">trous requis</div></div>
</div>

<h2>Synthèse de l'agent <small>à vérifier</small></h2>
<div class="synth"><span class="warn">Rédigé par IA · à vérifier</span>{synthese}</div>

<h2>Faits par axe <small>score ≥ {e(r['score']['seuils']['a_verifier'])}/7</small></h2>
{''.join(html_axes)}

<h2>Signaux usagers <small>par récurrence</small></h2>
{''.join(html_sig) or '<p class="empty">Aucun signal.</p>'}

<h2>Couverture du catalogue <small>{e(len(trous))} codes requis sans élément validé</small></h2>
<div class="tbl"><table><thead><tr><th>Code</th><th>Information</th><th class="hide-m">Statut</th><th>Validés</th><th>À revoir</th></tr></thead>
<tbody>{lignes_cov}</tbody></table></div>

<h2>Faits peu fiables <small>score &lt; {e(r['score']['seuils']['a_verifier'])}/7</small></h2>
{''.join(carte(i, r) for i in faibles) or '<p class="empty">Aucun.</p>'}

<h2>Journal des runs <small>preuve du dispositif · usage IA</small></h2>
<div class="tbl"><table><thead><tr><th>Run</th><th>Date</th><th>Collectés</th><th>Filtrés</th><th>Qualifiés</th><th>Hors sujet</th>
<th class="hide-m">Modèle</th><th class="hide-m">Notes</th></tr></thead><tbody>{lignes_runs}</tbody></table></div>

<footer>Score de fiabilité calculé par script (autorité 0-3 + fraîcheur 0-2 + source primaire 0-2), jamais par l'IA.
L'IA classe et résume ; l'humain valide. {e(restants)} élément(s) restent à qualifier.</footer>
</div></body></html>"""
    with open(sortie, "w", encoding="utf-8") as f:
        f.write(page)
    print(sortie)


if __name__ == "__main__":
    main()
