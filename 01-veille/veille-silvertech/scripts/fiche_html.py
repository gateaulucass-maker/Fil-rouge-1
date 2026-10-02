"""Génère la fiche de veille HTML (01-veille/fiche-veille-silvertech.html) à partir des éléments validés.

Les données (faits, signaux, bibliographie, chiffres) viennent de la base ; le texte d'analyse
ci-dessous (THESE, AXE_TEXTE, IMPLICATIONS, LIMITES) a été rédigé pour la fiche d'octobre 2026
et cite les éléments par leur id entre accolades, ex. {149}. Après une nouvelle revue, relire
ce texte puis relancer : .venv/bin/python scripts/fiche_html.py
"""
import re
import sys
from collections import Counter, defaultdict
from html import escape

import os
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "scripts"))
from common import catalogue, connexion  # noqa: E402

SORTIE = os.path.join(os.path.dirname(RACINE), "fiche-veille-silvertech.html")

AXES = [("marche", "Marché"), ("concurrence", "Concurrence"), ("usagers", "Usagers"),
        ("techno", "Technologie"), ("reglementaire", "Réglementaire")]
LIB = {c["code"]: c["libelle"] for c in catalogue()}
ORDRE_CODES = [c["code"] for c in catalogue()]

with connexion() as cx:
    cols = ("id", "axe", "code_info", "flux", "score_fiabilite", "pertinence", "titre", "resume",
            "pourquoi_important", "chiffres", "source_nom", "publie_le", "url", "irritant", "verbatim", "valide_par")
    items = [dict(zip(cols, r)) for r in cx.execute(
        f"SELECT {', '.join(cols)} FROM veille_items WHERE statut = 'valide'").fetchall()]
    stats = cx.execute("""SELECT (SELECT count(*) FROM raw_items),
                                 (SELECT count(*) FROM raw_items WHERE etat = 'filtre'),
                                 (SELECT count(*) FROM veille_items WHERE statut <> 'hors_sujet'),
                                 (SELECT count(*) FROM veille_items WHERE statut = 'hors_sujet'),
                                 (SELECT count(*) FROM veille_items WHERE statut = 'valide'),
                                 (SELECT count(*) FROM veille_items WHERE statut = 'rejete')""").fetchone()

par_id = {i["id"]: i for i in items}
faits = [i for i in items if i["flux"] == "fait"]
signaux = [i for i in items if i["flux"] == "signal"]


def cle_fait(i):
    return (ORDRE_CODES.index(i["code_info"]), -(i["pertinence"] or 0), -(i["score_fiabilite"] or 0), i["id"])


# Numérotation de la bibliographie : faits par axe puis code, puis signaux par source
ordre_faits = []
for axe, _ in AXES:
    ordre_faits += sorted([i for i in faits if i["axe"] == axe], key=cle_fait)
ordre_signaux = sorted(signaux, key=lambda i: (i["source_nom"], i["irritant"] or "~", i["id"]))
NUM = {i["id"]: n for n, i in enumerate(ordre_faits + ordre_signaux, 1)}


def ref(*ids):
    liens = [f'<a class="ref" href="#ref-{NUM[i]}">{NUM[i]}</a>' for i in ids]
    return '<sup class="refs">' + ", ".join(liens) + "</sup>"


def r(texte):
    """Remplace {149} ou {149,131} par des renvois numérotés."""
    return re.sub(r"\{([\d,\s]+)\}", lambda m: ref(*[int(x) for x in m.group(1).split(",")]), texte)


def e(t):
    return escape("" if t is None else str(t))


# ------------------------------------------------------------------ contenu éditorial

THESE = ("Le besoin de sécurité à domicile est massif et ne fera que grandir. Pourtant, les produits qui "
         "détectent un danger demandent un effort au senior, et c'est cet effort qui les fait abandonner. "
         "Ceux qui ne lui demandent rien sont appréciés, mais ne protègent de rien.")

CHIFFRES = [
    ("2 → 2,8 M", "seniors de 60 ans et plus en perte d'autonomie, de 2021 aux années 2050", "Insee, Drees", 149),
    ("1 sur 3", "des plus de 65 ans chute chaque année ; 80 % des chutes ont lieu au domicile", "Ministère de la Santé, 2022", 170),
    ("900 000", "abonnés à la téléassistance en France", "Silver Valley, baromètre 2024", 127),
    ("2 %", "des 7 millions d'appels annuels de téléassistance sont transmis aux secours", "AFRATA", 148),
    ("87 %", "voient la téléassistance comme un marqueur de dépendance", "Senior Strategic, 2016", 164),
    ("90 %", "des utilisateurs portent leur dispositif surtout quand ils sont seuls chez eux", "Drees, enquête VQS", 131),
    ("5–15 %", "de fausses alertes pour les capteurs de chute, pour 80 à 95 % de chutes détectées", "ANSP 2017 ; DITP 2023", 103),
    ("41 %", "des seniors citent le manque d'intérêt comme premier frein aux objets connectés", "Linexio, ≈ 250 seniors", 176),
]

AXE_TEXTE = {
    "marche": {
        "titre": "Un besoin qui grossit, un marché qui stagne",
        "points": [
            "La démographie porte tout : environ 700 000 seniors de plus en perte d'autonomie d'ici les années 2050 {149}, "
            "5 millions de 60 ans et plus supplémentaires et 150 000 à 200 000 emplois à créer pour les accompagner {129}. "
            "La demande de services à domicile suit la même pente {159}.",
            "La taille du « marché silver » dépend entièrement du périmètre : de 60 à 130 milliards d'euros {140, 147}. "
            "Le segment qui nous concerne, la téléassistance, ne pèse qu'environ 250 millions d'euros {126}.",
            "Ce segment stagne en valeur malgré un parc en hausse {157}, et le secteur vise à doubler l'équipement des 75 ans et plus "
            "d'ici 2030, d'environ 10 % à 20 % {148}. Il y a donc de la place, mais la croissance ne vient pas toute seule.",
        ],
    },
    "concurrence": {
        "titre": "Beaucoup d'acteurs, peu de succès grand public",
        "points": [
            "Quatre familles se partagent le terrain : la téléassistance historique (Vitaris, Filien, Présence Verte…) {164, 150}, "
            "les bracelets et montres de détection {168}, les capteurs sans port {132, 161} et les robots compagnons {151, 178, 189}.",
            "Les prix s'étalent de 6 € par mois en option {153} à 20-50 € pour la téléassistance {152} et 90 € pour un robot compagnon {178}. "
            "L'engagement de 12 mois et les frais de résiliation restent courants {165}.",
            "Les échecs ont des causes récurrentes : stigmatisation et déni du risque pour les montres senior, qui pivotent vers le B2B {154}, "
            "financement trop court {175}, cycles de vente longs {173}. Le secteur se consolide par rachats {169}, et des faillites tombent encore {194}.",
            "L'écart entre promesse et réalité est documenté : les chutes « molles » ne sont pas détectées, de l'aveu même d'un opérateur {184}, "
            "et le « sans abonnement » cache souvent un forfait SIM et une mise en service lourde pour les proches {183}.",
        ],
    },
    "usagers": {
        "titre": "Le senior ne veut pas porter, l'aidant n'en peut plus",
        "points": [
            "Le dispositif n'est pas porté quand il le faudrait : gêne, déclenchements accidentels, activités {131}. "
            "Les objets connectés finissent au tiroir par complexité ou utilité insuffisante {133, 89}.",
            "Les seniors sont peu équipés en objets de santé connectés (9 % des 60-69 ans, 5 % des 70 ans et plus en 2019) {195}, "
            "et le manque d'intérêt freine plus que le prix {176}.",
            "Côté aidants, les témoignages convergent vers l'épuisement : charge mentale, relances répétées, finances qui s'effondrent "
            "{30, 32, 48, 49}. Un outil qui ajoute une tâche à l'aidant devient une corvée et finit abandonné {9, 105}.",
            "Ce qui est apprécié ne demande rien au senior : la gazette papier ravit les grands-parents {73, 82, 64}, "
            "et la localisation rassure la famille {85, 94}… tant qu'elle est fiable {58, 69, 78}.",
        ],
    },
    "techno": {
        "titre": "Détecter sans être porté",
        "points": [
            "Les détecteurs portés reposent sur accéléromètre et gyroscope. Ils ratent les chutes molles et dépendent d'un centre d'écoute {100}, "
            "avec 5 à 15 % de fausses alertes {103}.",
            "Une génération de capteurs ambiants détecte sans rien porter : capteur de profondeur sans image {107}, analyse des ondes wi-fi {161}, "
            "capteur fixe sans caméra ni bracelet {109}. C'est la piste qui répond directement au problème du non-port.",
            "Pour construire en no-code, deux alertes : la sécurité des backends (des apps Supabase mal configurées exposent leurs données) {37}, "
            "et le plafond des outils quand le produit grandit {36}. Un prototype livré en huit semaines avec un agent IA reste possible {19}.",
        ],
    },
    "reglementaire": {
        "titre": "Rester « bien-être », protéger les données, annoncer l'IA",
        "points": [
            "Un logiciel devient dispositif médical s'il a une finalité médicale, produit un résultat propre à un patient et analyse des données ; "
            "stocker ou transmettre ne suffit pas {120}. S'il bascule, il passe le plus souvent en classe IIa ou plus, avec organisme notifié {143, 114}. "
            "Le statut dépend de ce que l'éditeur annonce {110}.",
            "Des données de vie quotidienne et de santé imposent consentement explicite, minimisation et analyse d'impact (PIA) {108, 142, 119}, "
            "plus une sécurité dès la conception {135, 111}. Les amendes RGPD ont désormais une méthode de calcul européenne {17}.",
            "Tout compagnon ou assistant IA doit dire qu'il est une IA : l'obligation de transparence de l'AI Act s'applique depuis le 2 août 2026, "
            "avec des sanctions jusqu'à 15 M€ ou 3 % du chiffre d'affaires {137, 122, 112}.",
            "Côté propriété intellectuelle, le code appartient à son auteur sauf cession écrite : une facture payée ne suffit pas {116, 118}. "
            "Le nom du produit se protège par un dépôt de marque à l'INPI {125, 146}.",
        ],
    },
}

IMPLICATIONS = [
    ("Zéro effort pour le senior",
     "Le produit ne doit rien demander au senior : ni port, ni recharge, ni écran. C'est la condition d'adoption la plus documentée {131, 164, 176}. "
     "Piste : capteurs ambiants à la maison {107, 161, 109}."),
    ("Une fiabilité avant les fonctions",
     "La confiance de l'aidant se perd au premier bug ou à la première fausse alerte {58, 69, 103, 183}. "
     "Mieux vaut peu de signaux, mais justes."),
    ("Alléger l'aidant, pas le solliciter",
     "Des aidants déjà épuisés {32, 48, 49} : notifications rares et utiles, résumé plutôt que flux continu. "
     "Ce qui devient une corvée est abandonné {9, 105}."),
    ("Un récit de lien, pas de dépendance",
     "Éviter le vocabulaire de la surveillance et de la dépendance {164, 154, 16}. "
     "Famileo montre qu'un produit de lien est attendu chaque mois {73, 82}."),
    ("Bien-être par conception",
     "Pas de finalité médicale ni d'analyse diagnostique, pour rester hors dispositif médical {120, 143}. "
     "RGPD et PIA dès le prototype {119, 108}, et toute IA s'annonce comme telle {137}."),
]

LIMITES = [
    "Plusieurs chiffres clés sont anciens : abandon des objets connectés (2014) {89}, perception de la téléassistance (2016) {164}, "
    "équipement des seniors (2019) {195}. Ils sont à actualiser.",
    "Les éléments de concurrence viennent surtout de pages commerciales ou éditoriales, avec une fiabilité de 1 à 3 sur 7 : "
    "les prix sont des ordres de grandeur, pas des tarifs vérifiés.",
    "Les signaux d'usagers viennent de 4 applications et de 3 communautés Reddit anglophones : ils éclairent des irritants, "
    "ils ne mesurent pas leur fréquence dans la population.",
    "Aucune donnée solide sur les aidants familiaux (M3) ni sur le consentement des personnes vulnérables (R5) : ce sont les trous prioritaires.",
]

IRR_LIB = {"fiabilite_technique": "Fiabilité technique", "autre": "Épuisement et charge de l'aidant",
           "complexite": "Complexité", "prix_abonnement": "Prix, abonnement", None: "Retours positifs"}

# ------------------------------------------------------------------ rendu

def bloc_axe(n, axe, nom):
    t = AXE_TEXTE[axe]
    lst = [i for i in ordre_faits if i["axe"] == axe]
    nb_sig = sum(1 for i in signaux if i["axe"] == axe)
    codes = sorted({i["code_info"] for i in items if i["axe"] == axe}, key=ORDRE_CODES.index)
    lignes = []
    for i in lst:
        score = i["score_fiabilite"]
        niv = "hi" if score >= 5 else "mid" if score >= 3 else "lo"
        chif = "".join(f'<li><b>{e(c["valeur"])}</b> {e(c.get("contexte", ""))} <span class="src">({e(c["source_citee"])})</span></li>'
                       for c in (i["chiffres"] or []))
        lignes.append(f"""<tr>
<td class="num"><a id="f-{NUM[i['id']]}" href="#ref-{NUM[i['id']]}">{NUM[i['id']]}</a></td>
<td class="code">{e(i['code_info'])}</td>
<td><div class="t">{e(i['titre'])}</div><div class="res">{e(i['resume'])}</div>{f'<ul class="ch">{chif}</ul>' if chif else ''}</td>
<td class="srcc">{e(i['source_nom'])}{'<br>' + e(i['publie_le'].strftime('%m/%Y')) if i['publie_le'] else ''}</td>
<td class="sc"><span class="pill {niv}">{score}</span></td>
<td class="sc"><span class="pert">{'●' * (i['pertinence'] or 0)}{'○' * (3 - (i['pertinence'] or 0))}</span></td>
</tr>""")
    points = "".join(f"<li><div>{r(e(p))}</div></li>" for p in t["points"])
    return f"""<section class="axe" id="axe-{axe}">
<div class="axe-h">
  <div class="axe-n">{n:02d}</div>
  <div><div class="k">Axe · {e(nom)}</div><h2>{e(t['titre'])}</h2>
  <div class="axe-meta">{len(lst)} faits · {nb_sig} signaux · codes {', '.join(codes)}</div></div>
</div>
<ol class="points">{points}</ol>
<div class="tbl"><table class="faits">
<thead><tr><th>Réf.</th><th>Code</th><th>Information</th><th>Source</th><th title="Score de fiabilité sur 7, calculé par script">Fiab.</th><th title="Pertinence décidée en revue humaine">Pert.</th></tr></thead>
<tbody>{''.join(lignes)}</tbody></table></div>
</section>"""


def bloc_signaux():
    cpt = Counter(i["irritant"] for i in signaux if i["axe"] == "usagers")
    total = sum(cpt.values())
    barres = "".join(
        f'<div class="hb"><span class="hl">{e(IRR_LIB[k])}</span><span class="hbar {"pos" if k is None else ""}" '
        f'style="--w:{v / max(cpt.values()) * 100:.0f}%"></span><span class="hv">{v}</span></div>'
        for k, v in cpt.most_common())
    groupes = [
        ("Famileo", "Gazette familiale papier", "App Store · Famileo"),
        ("Tous FAMiliés", "Journal familial mensuel", "App Store · Tous FAMiliés"),
        ("Life360", "Localisation de la famille", "App Store · Life360"),
        ("Signia", "Application d'aides auditives", "App Store · Signia"),
        ("Aidants", "r/AgingParents, r/CaregiverSupport", None),
    ]
    cartes = []
    for nom, sous, src in groupes:
        if src:
            g = [i for i in signaux if i["source_nom"] == src]
        else:
            g = [i for i in signaux if i["source_nom"] in ("r-agingparents", "r-caregiversupport")]
        pos = sum(1 for i in g if i["irritant"] is None)
        neg = len(g) - pos
        choix = sorted([i for i in g if i["verbatim"]], key=lambda i: (i["irritant"] is None, -len(i["verbatim"] or "")))
        if nom in ("Famileo", "Tous FAMiliés"):
            choix = [i for i in g if i["irritant"] is None][:2] + [i for i in g if i["irritant"]][:1]
        elif nom == "Life360":
            choix = [i for i in g if i["irritant"] is None][:1] + [i for i in g if i["irritant"]][:2]
        else:
            choix = choix[:3]
        q = "".join(f'<blockquote class="{"p" if i["irritant"] is None else "n"}">« {e(i["verbatim"])} »'
                    f'{ref(i["id"])}</blockquote>' for i in choix)
        cartes.append(f"""<article class="sg"><div class="sg-h"><h3>{e(nom)}</h3><span>{e(sous)}</span></div>
<div class="sg-c"><span class="cp">+ {pos}</span><span class="cn">− {neg}</span></div>{q}</article>""")
    return f"""<section id="signaux"><div class="sec-h"><div class="k">Signaux usagers</div>
<h2>Ce que disent seniors et aidants</h2></div>
<div class="sig-grid">
<div class="hbars"><div class="k">{total} signaux validés, par irritant</div>{barres}
<p class="note">Avis App Store et témoignages Reddit, anonymisés. Les verbatims anglais sont traduits (trad.).</p></div>
<div class="sgs">{''.join(cartes)}</div></div></section>"""


def positionnement():
    # Lecture qualitative de l'équipe : x = lien (0) → sécurité (1) ; y = effort senior nul (0) → élevé (1)
    pts = [
        ("Apple Watch", 0.86, 0.88, "o", "veille précédente"),
        ("Bracelet téléassistance", 0.80, 0.66, "o", "Filien, Vitaris, Allovie"),
        ("Life360", 0.62, 0.50, "o", "localisation"),
        ("Robots compagnons", 0.24, 0.48, "b", "Cutii, Buddy, Compan'IA"),
        ("Famileo", 0.10, 0.20, "b", "gazette papier"),
        ("Tous FAMiliés", 0.10, 0.06, "b", "journal mensuel"),
        ("Capteurs ambiants", 0.88, 0.06, "o", "Orme, wi-fi, Domalys"),
    ]
    W, H, P = 640, 420, 46
    def X(x): return P + x * (W - 2 * P)
    def Y(y): return P + (1 - y) * (H - 2 * P)
    marks = []
    for nom, x, y, c, s in pts:
        anc = "end" if x > 0.7 else "start"
        dx = -12 if anc == "end" else 12
        marks.append(f'<circle cx="{X(x):.0f}" cy="{Y(y):.0f}" r="7" class="pt {c}"/>'
                     f'<text x="{X(x) + dx:.0f}" y="{Y(y) - 2:.0f}" text-anchor="{anc}" class="pl">{e(nom)}</text>'
                     f'<text x="{X(x) + dx:.0f}" y="{Y(y) + 12:.0f}" text-anchor="{anc}" class="ps">{e(s)}</text>')
    return f"""<section id="position"><div class="sec-h"><div class="k">Positionnement</div>
<h2>Où notre produit se joue</h2></div>
<div class="pos-grid"><figure class="pos">
<svg viewBox="0 0 {W} {H}" role="img" aria-label="Carte de positionnement : axe horizontal du lien vers la sécurité, axe vertical de l'effort demandé au senior. La zone sécurité avec effort nul est peu occupée.">
<rect x="{P}" y="{P}" width="{W - 2 * P}" height="{H - 2 * P}" class="frame"/>
<line x1="{W / 2}" y1="{P}" x2="{W / 2}" y2="{H - P}" class="mid"/><line x1="{P}" y1="{H / 2}" x2="{W - P}" y2="{H / 2}" class="mid"/>
<ellipse cx="{X(0.58):.0f}" cy="{Y(0.24):.0f}" rx="100" ry="26" class="zone"/>
<text x="{X(0.58):.0f}" y="{Y(0.24) + 4:.0f}" text-anchor="middle" class="zl">Notre produit se joue ici</text>
{''.join(marks)}
<text x="{W / 2}" y="{H - 14}" text-anchor="middle" class="ax">← Lien · Sécurité →</text>
<text x="{P}" y="{P - 12}" class="ax">↑ Effort senior élevé</text><text x="{P}" y="{H - P + 18}" class="ax">Effort nul</text>
</svg></figure>
<div class="pos-txt"><p>Les produits de <b class="o">sécurité</b> demandent un effort au senior : porter, recharger, accepter l'image de la dépendance {ref(131, 164)}.
Les produits de <b class="b">lien</b> ne lui demandent rien et sont plébiscités, mais ne détectent aucun danger {ref(73, 82)}.</p>
<p>Le coin <b>sécurité sans effort</b> est presque vide : seuls quelques capteurs ambiants s'y trouvent {ref(107, 161, 109)}, surtout vendus aux Ehpad.
C'est là que se joue notre produit, qui doit aussi porter une dimension de lien pour ne pas être vécu comme une surveillance.</p>
<p class="note">Carte qualitative : placement établi par l'équipe à partir des éléments validés, pas une mesure.</p></div></div></section>"""


def biblio():
    lis = []
    for i in ordre_faits + ordre_signaux:
        date = f", {i['publie_le'].strftime('%d/%m/%Y')}" if i["publie_le"] else ""
        lis.append(f'<li id="ref-{NUM[i["id"]]}"><span class="bn">{NUM[i["id"]]}</span><span>{e(i["titre"])}. '
                   f'<i>{e(i["source_nom"])}</i>{e(date)}. <a href="{e(i["url"])}" rel="noopener">{e(i["url"])}</a></span></li>')
    return "".join(lis)


total, filtres, qualifies, hors_sujet, valides, rejetes = stats
chiffres_html = "".join(
    f'<div class="kf"><div class="kv">{e(v)}</div><div class="kt">{e(t)}</div><div class="ks">{e(s)} {ref(i)}</div></div>'
    for v, t, s, i in CHIFFRES)
axes_html = "".join(bloc_axe(n, a, nom) for n, (a, nom) in enumerate(AXES, 1))
impl_html = "".join(f'<li><span class="in">{n:02d}</span><div><h3>{e(t)}</h3><p>{r(e(d))}</p></div></li>'
                    for n, (t, d) in enumerate(IMPLICATIONS, 1))
lim_html = "".join(f"<li>{r(e(l))}</li>" for l in LIMITES)
sommaire = "".join(f'<a href="#axe-{a}"><span>{n:02d}</span>{e(nom)}</a>' for n, (a, nom) in enumerate(AXES, 1))

CSS = """
:root{--bg:#fff;--fg:#111418;--muted:#5d636b;--hair:#d5d7d9;--soft:#f5f5f3;--orange:#e8571c;--blue:#1f3fbf;
--ok:#1d7a46;--warn:#a86400;--low:#8a8f96;--on:#fff;
--display:"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 var(--display);-webkit-font-smoothing:antialiased}
a{color:inherit}
.wrap{max-width:1180px;margin:0 auto;padding:clamp(28px,6vw,72px) clamp(16px,4vw,48px) 64px}
.k{font:11.5px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.meta{display:flex;flex-wrap:wrap;gap:6px 32px;font:11.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;
color:var(--muted);border-top:2px solid var(--fg);padding-top:12px}.meta b{color:var(--fg);font-weight:500}
h1{font-weight:800;font-size:clamp(46px,9.4vw,124px);line-height:.9;letter-spacing:-.04em;margin:clamp(28px,5vw,56px) 0 0;text-wrap:balance}
h1 .o{color:var(--orange)}h1 .b{color:var(--blue)}h1 .sl{font-weight:400;color:var(--muted)}
.lede{display:grid;grid-template-columns:repeat(12,1fr);gap:0 24px;margin-top:clamp(28px,4vw,44px)}
.lede .k{grid-column:1/span 4;padding-top:6px}
.lede p{grid-column:5/span 8;margin:0;font-size:clamp(19px,2vw,26px);line-height:1.32;font-weight:700;letter-spacing:-.012em;max-width:34ch;text-wrap:pretty}
.toc{display:grid;grid-template-columns:repeat(12,1fr);gap:0 24px;margin-top:40px;border-top:1px solid var(--hair);padding-top:14px}
.toc .k{grid-column:1/span 4}.toc nav{grid-column:5/span 8;display:flex;flex-wrap:wrap;gap:8px 22px}
.toc a{text-decoration:none;font-weight:700;display:inline-flex;gap:8px;align-items:baseline}
.toc a span{font:11px var(--mono);color:var(--orange)}.toc a:hover{color:var(--orange)}
section{margin-top:clamp(56px,8vw,96px)}
.sec-h{border-top:2px solid var(--fg);padding-top:14px}
h2{font-weight:800;font-size:clamp(26px,3.4vw,44px);line-height:1.02;letter-spacing:-.03em;margin:6px 0 0;text-wrap:balance}
h3{margin:0;font-size:17px;letter-spacing:-.01em}
.kfs{display:grid;grid-template-columns:repeat(4,1fr);margin-top:22px;border-top:1px solid var(--fg)}
.kf{padding:18px 20px 20px 0;border-bottom:1px solid var(--hair);min-width:0}
.kf:not(:nth-child(4n)){border-right:1px solid var(--hair);margin-right:0}.kf:not(:nth-child(4n+1)){padding-left:20px}
.kv{font-weight:800;font-size:clamp(30px,3.4vw,44px);letter-spacing:-.035em;line-height:1;font-variant-numeric:tabular-nums}
.kf:nth-child(-n+4) .kv{color:var(--blue)}.kf:nth-child(n+5) .kv{color:var(--orange)}
.kt{margin-top:10px;font-size:14px;line-height:1.4}.ks{margin-top:8px;font:11px var(--mono);color:var(--muted)}
.kcap{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:10px;font:11px var(--mono);color:var(--muted);letter-spacing:.04em}
.kcap b{font-weight:500}.kcap .b{color:var(--blue)}.kcap .o{color:var(--orange)}
.axe-h{display:grid;grid-template-columns:3fr 9fr;gap:0 24px;border-top:2px solid var(--fg);padding-top:14px}
.axe-n{font-weight:800;font-size:clamp(56px,8vw,104px);line-height:.85;letter-spacing:-.05em;color:var(--orange)}
#axe-marche .axe-n,#axe-techno .axe-n{color:var(--blue)}#axe-usagers .axe-n{color:var(--fg)}
.axe-meta{margin-top:10px;font:11.5px var(--mono);color:var(--muted)}
.points{list-style:none;counter-reset:p;margin:26px 0 0;padding:0;display:grid;grid-template-columns:3fr 9fr;gap:0 24px}
.points li{grid-column:2;counter-increment:p;display:grid;grid-template-columns:34px 1fr;gap:10px;padding:12px 0;border-top:1px solid var(--hair);
font-size:16.5px;line-height:1.5;max-width:76ch}
.points li::before{content:counter(p,upper-alpha);font:500 12px var(--mono);color:var(--muted);padding-top:4px}
.refs{font:500 10.5px var(--mono);margin-left:2px;white-space:nowrap}
.refs a.ref{text-decoration:none;color:var(--orange)}.refs a.ref:hover{text-decoration:underline}
.tbl{overflow-x:auto;margin-top:24px}
table{width:100%;border-collapse:collapse}
.faits th{text-align:left;font:10.5px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:400;
padding:8px 10px;border-bottom:1px solid var(--fg)}
.faits td{padding:12px 10px;border-bottom:1px solid var(--hair);vertical-align:top;font-size:14px}
.faits td.num a{font:500 12px var(--mono);color:var(--muted);text-decoration:none}
.faits td.code{font:500 12px var(--mono)}
.faits .t{font-weight:700;line-height:1.3}.faits .res{color:var(--muted);margin-top:4px;line-height:1.45;max-width:70ch}
.faits ul.ch{margin:8px 0 0;padding-left:16px;font-size:13px}.faits ul.ch .src{color:var(--muted)}
.faits td.srcc{font:12px var(--mono);color:var(--muted);white-space:nowrap}
.faits td.sc{text-align:center;white-space:nowrap}
.pill{display:inline-block;min-width:26px;padding:2px 6px;font:700 12px var(--mono);border:1.5px solid currentColor}
.pill.hi{color:var(--ok)}.pill.mid{color:var(--warn)}.pill.lo{color:var(--low)}
.pert{font-size:11px;letter-spacing:2px;color:var(--orange)}
.sig-grid{display:grid;grid-template-columns:4fr 8fr;gap:24px 40px;margin-top:24px}
.hbars .k{margin-bottom:12px}
.hb{display:grid;grid-template-columns:1fr 34px;gap:4px 10px;align-items:center;margin-bottom:12px}
.hl{grid-column:1/-1;font-size:13.5px;font-weight:500}
.hbar{height:10px;background:linear-gradient(90deg,var(--orange) var(--w),var(--soft) var(--w))}
.hbar.pos{background:linear-gradient(90deg,var(--blue) var(--w),var(--soft) var(--w))}
.hv{font:700 13px var(--mono);text-align:right}
.note{font-size:12.5px;color:var(--muted);margin-top:14px}
.sgs{display:grid;grid-template-columns:1fr 1fr;gap:0 28px}
.sg{border-top:1px solid var(--fg);padding:12px 0 18px;min-width:0}
.sg-h{display:flex;justify-content:space-between;gap:10px;align-items:baseline;flex-wrap:wrap}
.sg-h span{font:11px var(--mono);color:var(--muted)}
.sg-c{display:flex;gap:10px;margin:6px 0 8px;font:700 12px var(--mono)}.cp{color:var(--blue)}.cn{color:var(--orange)}
blockquote{margin:8px 0 0;padding:2px 0 2px 12px;font-size:14px;line-height:1.45}
blockquote.p{border-left:3px solid var(--blue)}blockquote.n{border-left:3px solid var(--orange)}
.pos-grid{display:grid;grid-template-columns:7fr 5fr;gap:24px 40px;margin-top:24px;align-items:start}
.pos{margin:0}.pos svg{width:100%;height:auto;display:block}
.pos .frame{fill:none;stroke:var(--fg);stroke-width:1.5}.pos .mid{stroke:var(--hair);stroke-width:1}
.pos .zone{fill:none;stroke:var(--fg);stroke-width:1.5;stroke-dasharray:5 4}
.pos .zl{font:700 12px var(--display);fill:var(--fg)}
.pos .pt.o{fill:var(--orange)}.pos .pt.b{fill:var(--blue)}
.pos .pl{font:700 12.5px var(--display);fill:var(--fg)}.pos .ps{font:10.5px var(--mono);fill:var(--muted)}
.pos .ax{font:11px var(--mono);fill:var(--muted);letter-spacing:.04em}
.pos-txt p{margin:0 0 14px;font-size:16px;line-height:1.5}.pos-txt b.o{color:var(--orange)}.pos-txt b.b{color:var(--blue)}
.impl{list-style:none;padding:0;margin:24px 0 0;display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid var(--fg)}
.impl li{padding:16px 18px 20px 0;min-width:0}.impl li+li{padding-left:18px;border-left:1px solid var(--hair)}
.impl .in{display:block;font:800 34px var(--display);letter-spacing:-.04em;color:var(--orange);line-height:1;margin-bottom:12px}
.impl h3{font-size:16px;line-height:1.2}.impl p{margin:8px 0 0;font-size:14px;line-height:1.5;color:var(--fg)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px 48px;margin-top:24px}
.two ul{margin:0;padding-left:18px}.two li{margin-bottom:10px;font-size:14.5px}
.pipe{display:grid;grid-template-columns:repeat(5,1fr);border:1px solid var(--fg);margin-top:4px}
.pipe div{padding:12px;border-right:1px solid var(--hair)}.pipe div:last-child{border-right:0}
.pipe b{display:block;font:800 26px var(--display);letter-spacing:-.03em}.pipe span{font:10.5px var(--mono);color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.pipe div:last-child b{color:var(--orange)}
.bib{list-style:none;padding:0;margin:24px 0 0;columns:2;column-gap:40px;font-size:12.5px;line-height:1.45}
.bib li{display:grid;grid-template-columns:30px 1fr;gap:6px;break-inside:avoid;margin-bottom:8px}
.bib li:target{background:color-mix(in srgb,var(--orange) 12%,transparent)}
.bib .bn{font:500 11px var(--mono);color:var(--orange)}.bib a{color:var(--muted);overflow-wrap:anywhere;text-decoration-color:var(--hair)}
footer{margin-top:72px;border-top:1px solid var(--hair);padding-top:14px;font-size:12.5px;color:var(--muted);display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
a:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
@media (max-width:900px){
  .kfs{grid-template-columns:1fr 1fr}.kf{padding:16px 14px 16px 0!important;border-right:0!important}
  .kf:nth-child(odd){border-right:1px solid var(--hair)!important}.kf:nth-child(even){padding-left:14px!important}
  .impl{grid-template-columns:1fr 1fr}.impl li{border-left:0!important;padding-left:0!important;border-bottom:1px solid var(--hair)}
  .sig-grid,.pos-grid{grid-template-columns:1fr}.sgs{grid-template-columns:1fr}
}
@media (max-width:680px){
  .lede,.toc,.axe-h,.points,.two{grid-template-columns:1fr}.lede .k,.lede p,.toc .k,.toc nav,.points li{grid-column:1}
  .lede .k,.toc .k{margin-bottom:8px}.axe-n{font-size:56px;margin-bottom:8px}
  .impl{grid-template-columns:1fr}.bib{columns:1}
  .pipe{grid-template-columns:1fr 1fr}.pipe div{border-bottom:1px solid var(--hair)}
  .faits th:nth-child(2),.faits td.code,.faits th:nth-child(4),.faits td.srcc{display:none}
  .faits td{padding:10px 6px}
}
@media print{
  body{font-size:11pt}.wrap{max-width:none;padding:0}.toc{display:none}
  section{break-inside:auto}.faits tr,.kf,.sg,.impl li{break-inside:avoid}
  a{text-decoration:none}.bib{columns:2}
}
"""

page = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fiche de veille silver tech</title>
<meta name="description" content="Fiche de veille Marché et réglementation silver tech, PFR Générations Connectées, Ynov B2.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;700;800&family=IBM+Plex+Mono:wght@400;500;700&display=swap">
<style>{CSS}</style></head><body><div class="wrap">

<div class="meta"><span><b>Ynov</b> B2 Product Builder No-Code</span><span>PFR Générations Connectées</span>
<span>Phase 1 · Veille</span><span>Octobre 2026</span><span>{valides} éléments validés</span></div>

<h1><span class="o">Silver tech</span> <span class="sl">/</span><br><span class="b">marché &amp; règles</span></h1>

<div class="lede"><div class="k">Fiche de veille<br>Thèse</div><p>{e(THESE)}</p></div>

<div class="toc"><div class="k">Sommaire</div><nav>{sommaire}<a href="#signaux"><span>06</span>Signaux</a>
<a href="#position"><span>07</span>Positionnement</a><a href="#implications"><span>08</span>Implications</a><a href="#methode"><span>09</span>Méthode</a></nav></div>

<section id="chiffres"><div class="sec-h"><div class="k">Chiffres clés</div><h2>Le besoin, et le frein</h2></div>
<div class="kfs">{chiffres_html}</div>
<div class="kcap"><span><b class="b">Bleu</b> · le besoin et le marché</span><span><b class="o">Orange</b> · l'adoption et ses freins</span></div></section>

{axes_html}

{bloc_signaux()}

{positionnement()}

<section id="implications"><div class="sec-h"><div class="k">Implications pour le projet</div>
<h2>Cinq principes pour la suite</h2></div><ol class="impl">{impl_html}</ol></section>

<section id="methode"><div class="sec-h"><div class="k">Méthode et limites</div><h2>Comment cette veille a été faite</h2></div>
<div class="two"><div>
<div class="pipe"><div><b>{total}</b><span>collectés</span></div><div><b>{filtres}</b><span>filtrés sans IA</span></div>
<div><b>{qualifies}</b><span>qualifiés par IA</span></div><div><b>{rejetes + hors_sujet}</b><span>rejetés ou hors sujet</span></div>
<div><b>{valides}</b><span>validés humain</span></div></div>
<p>Collecte du 1<sup>er</sup> octobre 2026 : flux RSS (Silvereco, Maddyness, FrenchWeb, CNIL), 3 communautés Reddit, avis App Store de 4 applications
et recherche web ciblée sur les 13 informations requises du catalogue. Un filtre sans IA écarte les hors-sujet ; un agent IA résume et classe ;
chaque élément a été relu et validé ou rejeté par l'équipe.</p>
<p>Le <b>score de fiabilité</b> (sur 7) est calculé par script, jamais par l'IA : autorité du site (0-3), fraîcheur (0-2), source primaire citée (0-2).
La <b>pertinence</b> (●●● sur 3) est la décision de l'équipe. Les chiffres cités ont été revérifiés automatiquement dans leur page source.</p>
<p class="note">Dispositif complet : <code>01-veille/veille-silvertech/docs/dispositif-veille.md</code>.</p>
</div><div><div class="k" style="margin-bottom:10px">Limites</div><ul>{lim_html}</ul></div></div></section>

<section id="biblio"><div class="sec-h"><div class="k">Bibliographie</div><h2>{len(NUM)} sources</h2></div>
<ol class="bib">{biblio()}</ol></section>

<footer><span>Fiche de veille · PFR Générations Connectées · Phase 1</span><span>Données : base de veille, revue du 1<sup>er</sup> octobre 2026</span></footer>
</div></body></html>"""

with open(SORTIE, "w", encoding="utf-8") as f:
    f.write(page)
print(SORTIE, len(page), "octets,", len(NUM), "références")
# contrôle : tous les ids cités existent et sont validés
cites = set(int(x) for m in re.findall(r"\{([\d,\s]+)\}", str(AXE_TEXTE) + str(IMPLICATIONS) + str(LIMITES)) for x in m.split(","))
cites |= {c[3] for c in CHIFFRES} | {131, 164, 73, 82, 107, 161, 109}
print("ids cités absents :", sorted(cites - set(NUM)))
