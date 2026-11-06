import pathlib,re,sys
D=pathlib.Path('/Users/lucas/dev/_wt/fil-rouge/maquette-v4/S1-2026-2027/03-outils-nocode-ia/interne/lucas')
s=(D/'1-1-rendu-nocode-ia-v2.html').read_text(encoding='utf-8')
a=s.index('<section class="page" id="p-stack">');b=s.index('</section>',a)+len('</section>')
old=s[a:b]
chart=re.search(r'<div class="vis"><ol class="cols".*?</ol>(?:.*?</div>)?',old,re.S).group(0)
E='data-n="E · WeWeb + Supabase (UE) + n8n" data-s="68" data-u="sur 100" tabindex="0" style="--h:90.7;--c:#FFD36E'
assert chart.count(E)==1
chart=chart.replace(E,E.replace('#FFD36E','#9B85D6'))
G='data-s="70" data-u="sur 100" tabindex="0" style="--h:93.3;--c:#FFD36E'
assert chart.count(G)==1
chart=chart.replace(G,G.replace('#FFD36E','#FFC9A3'))
L='<span><i style="background:#9B85D6"></i>plan B</span>'
assert chart.count(L)==1
chart=chart.replace(L,'<span><i style="background:#FFC9A3"></i>à tester</span>'+L)
crit=re.search(r'<table class="m">.*?</table>',old,re.S).group(0)
crit=crit.replace('Un non sort la stack du classement.','Un « non » élimine la stack.')
V=[("ok","gardée","A · React + Next.js + Supabase","La seule base testée en local de bout en bout."),
("soon","à tester","G · WeWeb + Baserow + Make","Meilleure piste tout no-code. WeWeb et Make restent à essayer."),
("mid","plan B","E ou D · Supabase + n8n","Même base que A : seuls les écrans changent (WeWeb ou FlutterFlow)."),
("off","écartées","F, H, B, C","Baserow seul ne tient pas les règles (60). Bubble : Europe seulement sur Enterprise (54). Glide et Softr : données hors Europe (50, 48).")]
rows=''.join(f'<li><span class="n">{i:02d}</span><div class="a"><b>{n}</b><span>{t}</span></div><span class="tag {c}">{l}</span></li>' for i,(c,l,n,t) in enumerate(V,1))
new=f'''<section class="page" id="p-stack"><span class="k">02 · Stack</span>
<h2 class="t">On a comparé huit stacks. La stack A l’emporte, et un plan B est prêt.</h2>
<div class="facts"><div><em>La stack A</em><b>75<small>/ 100</small></b><span>React, Next.js et Supabase : la meilleure note des huit stacks comparées.</span></div><div><em>Le scénario</em><b>26<small>/ 26 étapes</small></b><span>Le parcours « Famille Test » rejoué en local, sans une seule erreur.</span></div><div><em>La sécurité</em><b>9<small>/ 9 tests</small></b><span>Tous réussis : chaque famille ne voit que ses propres données.</span></div></div>
<div class="sec" id="stack-pourquoi"><span class="k">Étape 1</span><h3>Pourquoi comparer</h3><p>Avant de construire, il fallait choisir les outils. Le Cadre doit tenir quatre usages : la vitrine, l’écran du cadre, l’appli de l’aidante et l’alerte après 48 h sans nouvelles. Une règle passe avant tout : les données des familles restent en Europe. Plusieurs assemblages pouvaient le faire, du tout no-code au code écrit par une IA. On en a comparé huit.</p></div>
<div class="sec" id="stack-notes"><span class="k">Étape 2</span><h3>Comment on a noté</h3><p>Chaque note vient d’une source, et la page dit laquelle.</p>
<div class="vis"><ol class="steps"><li><span class="n">1</span><b>Lire la doc officielle</b><p>Prix, régions et quotas relevés sur les pages des outils. Une note tirée de là est marquée « documenté ».</p></li><li><span class="n">2</span><b>Tester en local</b><p>Le scénario « Famille Test » rejoué le 22 octobre, de la création du compte à l’alerte, avec Supabase.</p></li><li><span class="n">3</span><b>Casser exprès</b><p>On a ouvert les données à tout le monde : les tests ont échoué. Ils mesurent donc vraiment.</p></li></ol></div>
<p style="margin-top:32px">Sept critères, notés de 1 à 5 puis pondérés. Les données hors Europe éliminent, quel que soit le score.</p><div class="vis">{crit}</div></div>
<div class="sec" id="stack-classement"><span class="k">Étape 3</span><h3>Le classement</h3><p>Huit stacks notées sur 100. Les hachurées sont hors classement : leurs données quittent l’Europe.</p>
{chart}</div>
<ol class="rows" style="margin-top:24px">{rows}</ol></div>
<div class="sec" id="stack-conclusion"><span class="k">Conclusion</span><h3>Ce qu’on retient</h3><p>A gagne sur les tests, pas sur la promesse. Sa base a tenu tout le scénario et refuse les erreurs. G reste la piste tout no-code à tester.</p><div class="vis three">
<div><span class="k">Raison 1</span><b>Le code est écrit par une IA</b><p>L’équipe décrit en français, Claude Code écrit, l’équipe vérifie : le travail du no-code.</p></div>
<div><span class="k">Raison 2</span><b>A refuse ce que G laisse passer</b><p>Testé en local : Supabase rejette le doublon et le fichier vide. Baserow accepte tout et publie les photos.</p></div>
<div><span class="k">Plan B</span><b>D ou E, même base</b><p>Même Supabase, mêmes tests : on change seulement les écrans. Deux jours de retard, et on bascule.</p></div></div><p class="next"><a href="#ia">Page suivante : IA <span>→</span></a></p></div>
</section>'''
s=s[:a]+new+s[b:]
nav_old=re.search(r'<li data-p="stack"><a href="#stack"><b>02</b>Stack</a><ul>.*?</ul></li>',s).group(0)
s=s.replace(nav_old,'<li data-p="stack"><a href="#stack"><b>02</b>Stack</a><ul><li><a href="#stack-pourquoi">Pourquoi comparer</a></li><li><a href="#stack-notes">Comment on a noté</a></li><li><a href="#stack-classement">Le classement</a></li><li><a href="#stack-conclusion">Ce qu’on retient</a></li></ul></li>')

# résumé : lignes « Le rendu, page par page » cliquables
a=s.index('<h3>Le rendu, page par page</h3>');b=s.index('</ol>',a)
blk=s[a:b]
assert blk.count('<ol class="rows">')==1
blk=blk.replace('<ol class="rows">','<ol class="rows pages">')
IDS={'02':'stack','03':'ia','04':'blueprint','05':'da','06':'equipe','07':'usage'}
def lk(m):
    n,t=m.group(1),m.group(2)
    return f'<span class="n">{n}</span><div class="a"><b><a href="#{IDS[n]}">{t}</a></b>'
blk,k=re.subn(r'<span class="n">(\d\d)</span><div class="a"><b>([^<]+)</b>',lk,blk)
assert k==6,k
s=s[:a]+blk+s[b:]

def rep1(a,b):
    global s
    assert s.count(a)==1,a[:50]
    s=s.replace(a,b)
rep1('<h2 class="t">On construit avec la stack A, les textes passent par Mistral, une personne les valide.</h2>',
 '<h2 class="t">Le Cadre se construit sur la stack A. Mistral écrit les textes, et une personne les relit avant chaque envoi.</h2>')
rep1('<div class="facts"><div><b>75</b><span>sur 100 pour la stack A, première de huit</span></div><div><b>8 IA</b><span>jouées sur 11 tâches : elles se valent, le pays des données décide</span></div><div><b>14</b><span>étapes du service, de la découverte à la première photo</span></div></div>',
 '<div class="facts"><div><em>La stack</em><b>75<small>/ 100</small></b><span>La note de la stack A, la meilleure des huit stacks comparées.</span></div><div><em>Les IA</em><b>8<small>IA testées</small></b><span>Sur les mêmes 11 tâches, leurs scores sont très proches. On choisit donc selon le pays où partent les données.</span></div><div><em>Le service</em><b>14<small>étapes</small></b><span>Le parcours complet de la famille, de la découverte du Cadre à la première photo reçue.</span></div></div>')
GO="""<style>
.tag.off{background:transparent;color:#8F857B;border:1px solid #E2D6BF}
#p-stack .next{margin-top:48px;text-align:right}
#p-stack .next a{font-family:var(--title);font-weight:500;font-size:18px;color:var(--ink,#1F1A17);text-decoration:none;background:linear-gradient(#FFD36E,#FFD36E) 0 100%/0% .5em no-repeat;transition:background-size .3s}
#p-stack .next a:hover,#p-stack .next a:focus-visible{background-size:100% .5em}
#p-stack .next a span{display:inline-block;transition:transform .3s}
#p-stack .next a:hover span{transform:translateX(4px)}
ol.rows.pages li{position:relative;isolation:isolate}
ol.rows.pages li::before{content:"";position:absolute;left:0;right:0;bottom:-1px;height:2px;background:#1F1A17;transform:scaleX(0);transform-origin:left center;transition:transform .45s cubic-bezier(.2,.8,.2,1)}
ol.rows.pages .a a{color:inherit;text-decoration:none;outline:none;background:linear-gradient(#FFD36E,#FFD36E) no-repeat 0 85%/0% .5em;padding:0 2px;margin:0 -2px;transition:background-size .4s cubic-bezier(.2,.8,.2,1)}
ol.rows.pages .a a::after{content:"";position:absolute;inset:0}
ol.rows.pages .a b{display:flex;align-items:center;gap:10px}
ol.rows.pages .a b::after{content:"↗";font-weight:500;opacity:0;transform:translate(-4px,4px);transition:opacity .25s ease,transform .4s cubic-bezier(.2,.8,.2,1)}
ol.rows.pages .n{transition:background-color .3s ease,color .3s ease}
ol.rows.pages li:hover::before,ol.rows.pages li:focus-within::before{transform:scaleX(1)}
ol.rows.pages li:hover .a a,ol.rows.pages li:focus-within .a a{background-size:100% .5em}
ol.rows.pages li:hover .n,ol.rows.pages li:focus-within .n{background:#FFD36E;color:#1F1A17}
ol.rows.pages li:hover .a b::after,ol.rows.pages li:focus-within .a b::after{opacity:1;transform:translate(0,0)}
ol.rows.pages a:focus-visible::after{outline:2px solid #1F1A17;outline-offset:4px}
@media (prefers-reduced-motion:reduce){ol.rows.pages li::before,ol.rows.pages .a a,ol.rows.pages .a b::after,ol.rows.pages .n{transition:none}}
.page .facts em{display:block;font:600 13px/16px var(--title);letter-spacing:.08em;text-transform:uppercase;color:#6A5F55;font-style:normal;margin-bottom:12px}
.page .facts b small{font-size:.45em;font-weight:500;letter-spacing:0;margin-left:4px;color:#6A5F55}
.page .facts span{max-width:30ch;color:#1F1A17}
</style>
</head>"""
assert s.count('</head>')==1
# retrait du bloc Limites et suite du résumé
a=s.index('<div class="sec"><h3>Limites et suite</h3>')
b=s.index('<p class="note">Rendu en HTML, à la place du PDF',a); b=s.index('</p>\n',b)+5
s=s[:a]+s[b:]
# chiffres IA et DA au format du résumé
rep1('<div class="facts"><div><b>50 / 51</b><span>pour cinq IA sur onze tâches ; trois tâches seulement les séparent</span></div><div><b>Mistral</b><span>dans le produit : le seul fournisseur européen</span></div><div><b>1 clic</b><span>humain avant que quoi que ce soit n’arrive au cadre</span></div></div>',
 '<div class="facts"><div><em>Les scores</em><b>50<small>/ 51</small></b><span>La note de cinq IA sur les mêmes onze tâches. Trois tâches seulement les départagent.</span></div><div><em>L’IA du produit</em><b>Mistral</b><span>Retenue parce que c’est le seul fournisseur européen.</span></div><div><em>Le contrôle</em><b>1<small>clic humain</small></b><span>Une personne valide chaque texte avant qu’il arrive au cadre.</span></div></div>')
rep1('<div class="facts"><div><b>24</b><span>planches de DA, de la couverture aux réseaux sociaux</span></div><div><b>28</b><span>écrans d’appli et 3 états du cadre, dans une maquette cliquable</span></div><div><b>9 axes</b><span>d’audit : 3 traités dans la maquette v4, 4 ouverts dans Figma</span></div></div>',
 '<div class="facts"><div><em>La marque</em><b>24<small>planches</small></b><span>Toute la direction artistique, de la couverture aux réseaux sociaux.</span></div><div><em>La maquette</em><b>28<small>écrans</small></b><span>Les écrans de l’appli et 3 états du cadre, dans une maquette cliquable.</span></div><div><em>L’audit</em><b>9<small>axes</small></b><span>3 traités dans la maquette v4, 4 encore ouverts dans Figma.</span></div></div>')
s=s.replace('</head>',GO)
exec(open('/private/tmp/claude-501/-Users-lucas/3cfd266f-c819-400b-b063-e74df8fae452/scratchpad/detail_v3.py',encoding='utf-8').read())
(D/'1-1-rendu-nocode-ia-v3.html').write_text(s,encoding='utf-8')
print('avant',len(old),'après',len(new),'| chart',chart.count('<li'),'barres | critères',crit.count('<tr'))
