# Section 05 Direction artistique (exécuté par build_v2.py : rep, AX, ax déjà définis)
IMG = "img-rendu-da/p{}.jpg"

def logo(ink="#1F1A17", sun="#FFD36E", size=40):
    return (f'<span class="lg" style="--ink:{ink};--sun:{sun};--z:{size}px" role="img" aria-label="Logo Soly">'
            f'<span class="sym"><i></i><i></i><i></i><i></i></span><span class="word">Soly<em>.</em></span></span>')

def gal(items):
    out = []
    for n, t in items:
        out.append(f'<a class="th" href="{IMG.format(n)}" target="_blank" rel="noopener">'
                   f'<img src="{IMG.format(n)}" alt="Planche {n} : {t}" loading="lazy" width="1200" height="675">'
                   f'<span><b>{n}</b>{t}</span></a>')
    return '<div class="vis gal">' + ''.join(out) + '</div>'

PAL = [("Aube", "#FFFAF0", "Fond principal", "Encre 16,6 : 1"),
       ("Crème", "#FFF3D9", "Fond des cartes", "Encre 15,7 : 1"),
       ("Encre", "#1F1A17", "Texte et boutons", "Sur aube 16,6 : 1"),
       ("Café doux", "#6A5F55", "Texte secondaire", "Sur aube 6,0 : 1"),
       ("Soleil", "#FFD36E", "Lumière, le point du logo", "Jamais en texte"),
       ("Pêche", "#FFC9A3", "Accent chaud", "Encre 11,6 : 1"),
       ("Lilas", "#C9B8F0", "Accent doux", "Encre 10,2 : 1"),
       ("Ligne", "#F0E3C8", "Filets et bordures", "Décoratif")]
pal = ''.join(f'<div><i style="background:{h}"></i><b>{n}</b><code>{h}</code><span>{r}</span><small>{c}</small></div>'
              for n, h, r, c in PAL)

DECL = [("Aube", "background:#FFFAF0", "#1F1A17", "#FFD36E", "Le fond par défaut"),
        ("Crème", "background:#FFF3D9", "#1F1A17", "#FFD36E", "Sur une carte"),
        ("Encre", "background:#1F1A17", "#FFFAF0", "#FFD36E", "En négatif"),
        ("Soleil vers pêche", "background:linear-gradient(135deg,#FFE7A8,#FFC9A3)", "#1F1A17", "#FFFAF0", "Sur la lumière"),
        ("Lilas", "background:#C9B8F0", "#1F1A17", "#FFD36E", "Accent doux"),
        ("Pêche", "background:#FFC9A3", "#1F1A17", "#FFD36E", "Accent chaud")]
decl = ''.join(f'<div><div class="tile" style="{bg}">{logo(ink, sun, 30)}</div><b>{n}</b><span>{r}</span></div>'
               for n, bg, ink, sun, r in DECL)

SCALE = [("Display", "Lexend Medium", "76 px", "−4 %", "font:500 40px/1.05 Lexend,var(--title);letter-spacing:-.04em", "Un rayon de famille."),
         ("Titre 1", "Lexend Medium", "48 px", "−3 %", "font:500 30px/1.1 Lexend,var(--title);letter-spacing:-.03em", "Un signe pour aujourd’hui"),
         ("Titre 2", "Lexend Medium", "32 px", "−2 %", "font:500 22px/1.2 Lexend,var(--title);letter-spacing:-.02em", "Vous gardez la main"),
         ("Bouton", "Lexend Medium", "17 px", "0", "font:500 17px/1.2 Lexend,var(--title)", "Envoyer un signe"),
         ("Corps L", "Atkinson", "21 px", "interligne 145 %", "font:400 19px/1.45 var(--body)", "Une photo de la famille apparaît sur le cadre."),
         ("Corps", "Atkinson", "17 px", "interligne 145 %", "font:400 17px/1.45 var(--body)", "Le cadre s’allume à 8 h, sans réglage."),
         ("Libellé", "Lexend Medium", "13 px", "+6 %", "font:500 13px/1.2 Lexend,var(--title);letter-spacing:.06em;text-transform:uppercase", "Aujourd’hui")]
scale = ''.join(f'<tr><td><b>{n}</b><br><span class="m">{f}</span></td><td>{z}</td><td>{l}</td><td><span style="{st};color:#1F1A17">{ex}</span></td></tr>'
                for n, f, z, l, st, ex in SCALE)

APPS = [("14", "Instagram, un compte qui donne le sourire"), ("15", "TikTok, quinze secondes, un seul message"),
        ("16", "Sacs, un objet qu’on a plaisir à porter"), ("17", "Coffret, ouvrir la boîte est déjà un cadeau"),
        ("18", "Icône, reconnaissable à toutes les tailles"), ("19", "Application, quatre écrans, un seul geste"),
        ("20", "Le cadre trouve sa place au mur"), ("21", "Affiche et goodies, un univers jusque dans les détails"),
        ("22", "Le cadre, en un coup d’œil"), ("23", "Un geste : on touche"), ("24", "Les quatre états du cadre")]

CSS = '''<style>
#p-da .lg{display:inline-flex;align-items:center;gap:calc(var(--z)*.32);color:var(--ink)}
#p-da .lg .sym{display:grid;grid-template-columns:1fr 1fr;gap:calc(var(--z)*.07);width:var(--z);height:var(--z)}
#p-da .lg .sym i{background:var(--ink);border-radius:calc(var(--z)*.07)}
#p-da .lg .sym i:nth-child(1){border-top-left-radius:calc(var(--z)*.3)}#p-da .lg .sym i:nth-child(2){border-top-right-radius:calc(var(--z)*.3)}
#p-da .lg .sym i:nth-child(3){border-bottom-left-radius:calc(var(--z)*.3)}
#p-da .lg .sym i:nth-child(4){background:var(--sun);border-bottom-right-radius:calc(var(--z)*.3)}
#p-da .lg .word{font:600 calc(var(--z)*.9)/1 Lexend,var(--title);letter-spacing:-.03em}
#p-da .lg .word em{font-style:normal;color:var(--sun)}
#p-da .hero{display:grid;grid-template-columns:1.2fr 1fr;gap:32px;align-items:center;padding:48px;background:#FFFAF0;border:1px solid var(--hair);border-radius:12px}
#p-da .anat{list-style:none;margin:0;padding:0;display:grid;gap:16px}
#p-da .anat li{border-top:1px solid #F0E3C8;padding-top:10px;color:#6A5F55;font-size:15px}
#p-da .anat b{display:block;color:#1F1A17}
#p-da .decl{display:grid;grid-template-columns:repeat(3,1fr);gap:24px 16px}
#p-da .decl .tile{height:120px;border-radius:12px;display:flex;align-items:center;justify-content:center;border:1px solid var(--hair)}
#p-da .decl b,#p-da .pal b{display:block;margin-top:10px}
#p-da .decl>div>span,#p-da .pal span{display:block;color:var(--muted);font-size:14px}
#p-da .kcols{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
#p-da .kcols>div{border-top:2px solid var(--fg);padding-top:12px}
#p-da .kcols p,#p-da .kcols ul{margin:6px 0 0;color:var(--muted);font-size:15px}
#p-da .kcols ul{padding-left:18px}
#p-da .no{display:flex;gap:12px;flex-wrap:wrap;margin-top:16px}
#p-da .no span{position:relative;padding:14px 18px;border:1px solid var(--hair);border-radius:12px;background:#FFFAF0;color:#1F1A17;font:600 22px/1 Lexend,var(--title)}
#p-da .no span::after{content:"";position:absolute;left:8px;right:8px;top:50%;border-top:2px solid #C0392B;transform:rotate(-12deg)}
#p-da .pal{display:grid;grid-template-columns:repeat(4,1fr);gap:24px 16px}
#p-da .pal i{display:block;height:72px;border-radius:12px;border:1px solid var(--hair)}
#p-da .pal code{font:13px/18px var(--mono);color:var(--muted)}
#p-da .pal small{display:block;font-size:13px;color:var(--fg);margin-top:2px}
#p-da .grad{display:grid;grid-template-columns:2fr 1fr 1fr;gap:16px}
#p-da .grad>div>i{display:block;height:140px;border-radius:12px}
#p-da .grad b{display:block;margin-top:10px}#p-da .grad span{display:block;color:var(--muted);font-size:14px}
#p-da .type{display:grid;grid-template-columns:1fr 1fr;gap:16px}
#p-da .type>div{border-radius:12px;padding:28px;background:#FFFAF0;border:1px solid var(--hair);color:#1F1A17}
#p-da .type>div.dk{background:#1F1A17;color:#FFFAF0;border-color:#1F1A17}
#p-da .type .aa{font-size:96px;line-height:1}
#p-da .type p{margin:8px 0 0;opacity:.75;font-size:15px}
#p-da .type .w{margin-top:10px;font-size:14px;opacity:.75}
#p-da table.sc{width:100%;border-collapse:collapse}
#p-da table.sc td{padding:14px 12px 14px 0;border-top:1px solid var(--hair);vertical-align:middle;font-size:14px}
#p-da table.sc td:nth-child(2),#p-da table.sc td:nth-child(3){color:var(--muted);white-space:nowrap}
#p-da table.sc .m{color:var(--muted)}
#p-da .ui{display:grid;grid-template-columns:1fr 1fr;gap:16px}
#p-da .ui>div{border-radius:12px;padding:28px;background:#FFFAF0;border:1px solid var(--hair);color:#1F1A17}
#p-da .ui .lab{font:500 12px/1 Lexend,var(--title);letter-spacing:.08em;text-transform:uppercase;color:#6A5F55;margin-bottom:16px}
#p-da .btn{display:inline-flex;align-items:center;justify-content:center;min-height:56px;padding:0 28px;border-radius:999px;font:500 17px/1 Lexend,var(--title);border:1.5px solid #1F1A17;margin:0 8px 8px 0}
#p-da .btn.p{background:#1F1A17;color:#FFFAF0}#p-da .btn.s{background:transparent;color:#1F1A17}
#p-da .chip{display:inline-block;padding:8px 14px;border-radius:999px;font:500 14px/1 Lexend,var(--title);margin:0 6px 8px 0;color:#1F1A17}
#p-da .fld{height:56px;border-radius:14px;border:1.5px solid #F0E3C8;background:#fff;display:flex;align-items:center;padding:0 18px;color:#6A5F55;margin-top:8px}
#p-da .fld.f{border-color:#1F1A17;color:#1F1A17}
#p-da .card{border-radius:16px;padding:20px;margin-top:10px}
#p-da .card b{display:block;font:500 18px/1.2 Lexend,var(--title)}#p-da .card span{font-size:14px;opacity:.8}
#p-da .day{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
#p-da .day>div{border-radius:12px;padding:24px;min-height:150px;display:flex;flex-direction:column;justify-content:flex-end;color:#1F1A17}
#p-da .day .h{font:500 12px/1 Lexend,var(--title);letter-spacing:.08em;text-transform:uppercase;opacity:.7;margin-bottom:auto}
#p-da .day b{font:500 20px/1.2 Lexend,var(--title)}#p-da .day span{font-size:14px;opacity:.8;margin-top:4px}
#p-da .dd{display:grid;grid-template-columns:1fr 1fr;gap:16px}
#p-da .dd>div{border-radius:12px;padding:24px 28px}
#p-da .dd .y{background:#FFFAF0;border:1px solid var(--hair);color:#1F1A17}
#p-da .dd .x{background:#1F1A17;color:#FFFAF0}
#p-da .dd ul{margin:10px 0 0;padding-left:18px;font-size:15px;line-height:1.7}
#p-da .dd b{font:500 13px/1 Lexend,var(--title);letter-spacing:.08em;text-transform:uppercase}
#p-da .frame4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;counter-reset:f}
#p-da .frame4>div{border-top:2px solid var(--fg);padding-top:12px}
#p-da .frame4 b{display:block}#p-da .frame4 span{color:var(--muted);font-size:14px}
#p-da .gal{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
#p-da .gal.g2{grid-template-columns:repeat(2,1fr)}
#p-da .th{display:block;color:var(--fg);text-decoration:none}
#p-da .th img{display:block;width:100%;height:auto;border-radius:10px;border:1px solid var(--hair);transition:transform .2s}
#p-da .th:hover img{transform:translateY(-2px)}
#p-da .th span{display:block;margin-top:8px;font-size:14px;color:var(--muted)}
#p-da .th span b{color:var(--fg);margin-right:8px;font-family:var(--mono);font-weight:400}
#p-da .mqw{margin-top:32px;border:1px solid var(--hair);border-radius:12px;overflow:hidden;background:#FFFAF0;position:relative;margin-left:auto;margin-right:auto}
#p-da .mqw iframe.bp{position:absolute;left:0;top:0;width:1280px;height:1190px;border:0;border-radius:0;margin:0;transform-origin:0 0;background:#FFFAF0}
#p-da h4{margin:56px 0 0;font:800 17px/24px var(--title);letter-spacing:-.01em}
#p-da h4+p{margin:6px 0 0;color:var(--muted);max-width:60ch}
#p-da .lk{display:flex;flex-wrap:wrap;gap:12px;margin-top:32px}
#p-da .lk a{display:inline-flex;align-items:center;justify-content:center;min-height:56px;padding:0 28px;border-radius:999px;border:2px solid #1F1A17;background:transparent;color:#1F1A17;font:500 17px/1 Lexend,var(--body);text-decoration:none;transition:background .15s,color .15s}
#p-da .lk a.cta{background:#1F1A17;color:#FFFAF0}
#p-da .lk a:hover{background:#FFF3D9}
#p-da .lk a.cta:hover{background:#3A322C;border-color:#3A322C}
#p-da .lk a:focus-visible{outline:3px solid #C9B8F0;outline-offset:3px}
#p-da{--title:Lexend,"Helvetica Neue",Arial,sans-serif;--mono:Lexend,"Helvetica Neue",Arial,sans-serif}
#p-da b:not(.atk),#p-da strong{font-family:Lexend,var(--body);font-weight:500}
#p-da b.atk{font-family:var(--body);font-weight:700}
#p-da h2,#p-da h2.t{font-family:Lexend,var(--body);font-weight:600;letter-spacing:-.02em;color:#1F1A17}
#p-da .sec>h3{font:600 30px/38px Lexend,var(--body);letter-spacing:-.01em;color:#1F1A17}
#p-da h4{font-family:Lexend,var(--body);font-weight:500;letter-spacing:0;color:#1F1A17}
#p-da .sec>p{font:400 17px/27px var(--body);color:#6A5F55;max-width:62ch}
#p-da .audit{list-style:none;margin:24px 0 0;padding:0;border-top:2px solid #1F1A17}
#p-da .audit li{display:grid;grid-template-columns:56px 1fr auto;gap:8px 24px;align-items:center;padding:20px 0;border-bottom:1px solid #F0E3C8}
#p-da .audit .an{display:flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:50%;background:#FFF3D9;color:#1F1A17;font:600 16px/1 Lexend,var(--body)}
#p-da .audit .at b{display:block;font:500 19px/26px Lexend,var(--body);color:#1F1A17;margin-bottom:4px}
#p-da .audit .at span{font:400 17px/26px var(--body);color:#6A5F55}
#p-da .st{display:inline-block;font:500 14px/20px Lexend,var(--body);font-style:normal;color:#1F1A17;padding:6px 14px;border-radius:999px;white-space:nowrap;letter-spacing:0;text-transform:none}
#p-da .st-ok{background:#FFD36E} #p-da .st-mid{background:#C9B8F0} #p-da .st-soon{background:#FFC9A3}
#p-da .leg{display:flex;flex-wrap:wrap;gap:12px 28px;margin-top:24px;font:400 15px/22px var(--body);color:#6A5F55}
#p-da .leg span{display:flex;align-items:center;gap:10px}
@media(max-width:640px){#p-da .audit li{grid-template-columns:44px 1fr}#p-da .audit .st{grid-column:2;justify-self:start}#p-da .lk a{width:100%}}
@media(max-width:900px){#p-da .hero,#p-da .type,#p-da .ui,#p-da .dd{grid-template-columns:1fr}#p-da .frame4{grid-template-columns:1fr 1fr}#p-da .hero{padding:28px}}
@media(max-width:760px){#p-da .pal,#p-da .decl,#p-da .gal,#p-da .kcols,#p-da .day{grid-template-columns:repeat(2,1fr)}#p-da .grad{grid-template-columns:1fr}#p-da table.sc td:nth-child(3){display:none}}
@media(max-width:480px){#p-da .decl,#p-da .gal,#p-da .kcols,#p-da .day,#p-da .frame4{grid-template-columns:1fr}}
</style>'''

SEC = f'''<section class="page" id="p-da"><span class="k">05 · Direction artistique</span>
<h2 class="t">Soly : une marque chaude et lisible, mise à l’épreuve écran par écran.</h2>
<div class="facts"><div><b>24</b><span>planches de DA, de la couverture aux réseaux sociaux</span></div><div><b>28</b><span>écrans d’appli et 3 états du cadre, dans une maquette cliquable</span></div><div><b>9 axes</b><span>d’audit : 3 traités dans la maquette v4, 4 ouverts dans Figma</span></div></div>

<div class="sec" id="da-marque"><h3>Principes et logo</h3><p>« Le cadre qui ensoleille la journée. » Trois règles, puis un logo : un cadre, un nom, un point.</p>
<div class="vis three"><div><span class="k">01</span><b>La lumière, pas l’aplat</b><p>Le jaune éclaire : en point, en reflet, en halo. Il ne remplit jamais un fond.</p></div><div><span class="k">02</span><b>Gros et rond</b><p>Zones tactiles larges, coins arrondis, un seul geste par écran.</p></div><div><span class="k">03</span><b>Chaleureux, jamais médical</b><p>Des mots de famille. Pas de surveillance, pas de vocabulaire de santé.</p></div></div>
<div class="vis hero"><div>{logo(size=88)}</div><ul class="anat"><li><b>Le symbole</b>Un cadre coupé en quatre quarts : trois en encre, le dernier en soleil, comme une fenêtre allumée.</li><li><b>Le nom</b>« Soly » en Lexend SemiBold, toujours en minuscules sauf l’initiale.</li><li><b>Le point</b>Rond, couleur soleil : il ferme la phrase comme un bonjour. Pas d’effet, pas de lueur.</li></ul></div>
<h4 class="vis">Déclinaisons</h4><p>Le logo garde la même forme sur six fonds. Sur un fond déjà lumineux, le point passe en aube.</p>
<div class="vis decl">{decl}</div>
<h4 class="vis">Construction</h4>
<div class="vis kcols"><div><b>Tailles minimales</b><p>56 px sur écran, 36 px sur petit écran, 22 px pour le symbole seul.</p></div><div><b>Zone de protection</b><p>La hauteur du « S » de chaque côté. Rien ne rentre dans cette zone.</p></div><div><b>Interdits</b><ul><li>pas de majuscules (SOLY)</li><li>pas de point oublié</li><li>pas de texte jaune</li><li>pas de rotation</li></ul></div></div>
<div class="no" aria-label="Exemples interdits"><span>SOLY.</span><span>Soly</span><span style="color:#FFD36E">Soly.</span><span style="transform:rotate(-8deg)">Soly.</span></div>
{gal([("03", "Logo"), ("04", "Déclinaisons"), ("05", "Construction")])}</div>

<div class="sec" id="da-couleurs"><h3>Couleurs et lumière</h3><p>Huit tons chauds. Le texte en encre sur aube atteint 16,6 : 1. Le soleil éclaire, il ne s’écrit pas.</p>
<div class="vis pal">{pal}</div>
<h4 class="vis">La lumière se pose, elle ne brille pas</h4><p>Un dégradé pour les photos, un halo d’ambiance, deux dégradés d’accent. Le halo va derrière un écran ou un titre, jamais sous un bouton ou une carte.</p>
<div class="vis grad"><div><i style="background:linear-gradient(160deg,#FFE7A8,#FFC9A3 55%,#D6C6F5)"></i><b>Dégradé photo</b><span>160° : #FFE7A8, #FFC9A3 à 55 %, #D6C6F5</span></div><div><i style="background:linear-gradient(135deg,#FFD36E,#FFC9A3)"></i><b>Soleil vers pêche</b><span>Accent chaud</span></div><div><i style="background:linear-gradient(135deg,#FFC9A3,#C9B8F0)"></i><b>Pêche vers lilas</b><span>Accent doux</span></div></div>
{gal([("06", "Couleurs"), ("07", "Gradients")]).replace('class="vis gal"', 'class="vis gal g2"')}</div>

<div class="sec" id="da-typo"><h3>Typographie</h3><p>Deux polices : Lexend pour parler, Atkinson Hyperlegible pour expliquer.</p>
<div class="vis type"><div><div class="aa" style="font-family:Lexend,var(--title);font-weight:500;letter-spacing:-.04em">Aa</div><b style="font:500 20px Lexend,var(--title)">Lexend, pour parler</b><p>Titres, boutons, libellés. Formes rondes et ouvertes, chiffres nets.</p><div class="w">Regular · Medium · SemiBold</div></div><div class="dk"><div class="aa" style="font-family:var(--body);font-weight:700">Aa</div><b class="atk" style="font:700 20px var(--body)">Atkinson Hyperlegible, pour expliquer</b><p>Le texte courant. Dessinée pour les basses visions : chaque lettre se distingue (I, l, 1).</p><div class="w">Regular · Bold</div></div></div>
<h4 class="vis">Échelle</h4>
<table class="vis sc"><tbody>{scale}</tbody></table>
<p class="note">Règles : corps de texte à 17 px sur écran, contraste minimum 4,5 : 1, jamais de texte soleil sur fond clair. Dans la maquette v4, rien ne descend sous 14 px (audit, axe 1).</p>
{gal([("08", "Typographie des titres"), ("09", "Typographie du texte")]).replace('class="vis gal"', 'class="vis gal g2"')}</div>

<div class="sec" id="da-interface"><h3>Interface</h3><p>Sobre, net, sans ombre. Des composants larges, pensés pour un doigt qui tremble un peu.</p>
<div class="vis ui"><div><div class="lab">Boutons</div><span class="btn p">Envoyer un signe</span><span class="btn s">Plus tard</span><p style="color:#6A5F55;font-size:14px;margin:8px 0 0">Pilule de 56 px minimum. Un seul bouton principal par écran. Aucun halo au survol.</p>
<div class="lab" style="margin-top:24px">Pastilles</div><span class="chip" style="background:#C9B8F0">Prévenu si besoin</span><span class="chip" style="background:#FFD36E">Aujourd’hui</span><span class="chip" style="background:#FFC9A3">En famille</span>
<div class="lab" style="margin-top:24px">Champ</div><div class="fld">Un petit mot pour Jeanne</div><div class="fld f">Bonne journée maman</div><p style="color:#6A5F55;font-size:14px;margin:8px 0 0">56 px de haut, bordure ligne qui passe en encre au focus.</p></div>
<div><div class="lab">Cartes</div><div class="card" style="background:linear-gradient(135deg,#FFE7A8,#FFC9A3)"><b>Un signe pour aujourd’hui</b><span>Une photo, un mot, un sourire.</span></div><div class="card" style="background:#1F1A17;color:#FFFAF0"><b>Vous gardez la main</b><span>Le parent choisit ce qui s’affiche.</span></div><div class="card" style="background:#C9B8F0"><b>Prévenu si besoin</b><span>Un rappel doux, jamais une alarme.</span></div></div></div>
<h4 class="vis">Trois moments de la journée</h4>
<div class="vis day"><div style="background:linear-gradient(160deg,#FFE7A8,#FFC9A3)"><span class="h">Matin</span><b>Le cadre s’allume</b><span>À 8 h, sans réglage ni bouton.</span></div><div style="background:linear-gradient(160deg,#FFC9A3,#D6C6F5)"><span class="h">Midi</span><b>Un signe arrive</b><span>Une photo de la famille, on la touche pour dire merci.</span></div><div style="background:#1F1A17;color:#FFFAF0"><span class="h">Soir</span><b>On vous rassure</b><span>La famille sait que la journée s’est bien passée.</span></div></div>
<div class="vis dd"><div class="y"><b>À faire</b><ul><li>le jaune en lumière : point, reflet, halo</li><li>texte encre sur fond clair</li><li>zones tactiles de 56 px minimum</li><li>des mots de famille, jamais de jargon médical</li><li>coins arrondis, marges larges</li></ul></div><div class="x"><b>À éviter</b><ul><li>le jaune en aplat</li><li>texte jaune ou lilas</li><li>lueurs et ombres colorées</li><li>un autre symbole ou un cadre autour du logo</li><li>les capitales</li></ul></div></div>
{gal([("10", "Composants"), ("12", "Cas d’usage"), ("13", "À faire, à éviter")])}</div>

<div class="sec" id="da-applications"><h3>Applications</h3><p>La marque sort de l’écran : le cadre au mur, l’appli de la famille, les réseaux, le coffret.</p>
<div class="vis frame4"><div><b>1 · Un écran photo</b><span>Un cadre 10 pouces, au mur du salon.</span></div><div><b>2 · Un seul geste</b><span>On touche le cadre : la famille le voit.</span></div><div><b>3 · Aucun menu</b><span>Rien à régler pour le parent.</span></div><div><b>4 · Prêt avec un code</b><span>Six chiffres à saisir dans l’appli.</span></div></div>
{gal(APPS)}</div>

<div class="sec" id="da-maquette"><h3>La maquette interactive v4</h3><p>Le cadre au mur et l’application de la famille, reliés. Lancez un scénario, ou touchez directement le téléphone et le cadre. La liste des 28 écrans est plus bas dans le module.</p>
<div class="mqw" id="da-mqw"><iframe class="bp" data-src="1-1-soly-prototype-interactif-v4.html" title="Maquette interactive Soly v4"></iframe></div>
<div class="lk"><a class="cta" href="1-1-soly-prototype-interactif-v4.html" target="_blank" rel="noopener">Ouvrir la maquette seule</a></div></div>

<div class="sec" id="da-audit"><h3>L’audit de la DA, en 9 axes</h3><p>Chaque écran relu avec une question : un parent âgé et sa famille s’y retrouvent-ils ? Ce qui est réglé passe dans la maquette, ce qui demande un choix reste ouvert dans Figma.</p>
<ol class="audit">{ax}</ol>
<div class="leg"><span><i class="st st-ok">appliqué</i>visible dans la maquette ci-dessus</span><span><i class="st st-mid">ouvert dans Figma</i>une décision d’équipe est attendue</span><span><i class="st st-soon">observation</i>relevé, pas encore dessiné</span></div>
<div class="lk"><a class="cta" href="1-1-soly-rendu-da.html" target="_blank" rel="noopener">La DA complète</a><a href="1-1-da-soly-presentation/index.html" target="_blank" rel="noopener">Les 24 planches</a><a href="1-1-soly-rendu-da-maquette.html" target="_blank" rel="noopener">DA et maquette</a></div></div>
<script>(function(){{var w=document.getElementById("da-mqw"),f=w.querySelector("iframe"),W=1280,H=1190;
function fit(){{var p=w.parentNode.clientWidth;if(!p)return;var s=Math.min(p/W,(window.innerHeight-48)/H,1);s=Math.max(s,.28);
w.style.width=Math.round(W*s)+"px";w.style.height=Math.round(H*s)+"px";f.style.transform="scale("+s+")"}}
fit();addEventListener("resize",fit);addEventListener("load",fit);addEventListener("hashchange",function(){{setTimeout(fit,0)}});}})();</script>
</section>

'''
