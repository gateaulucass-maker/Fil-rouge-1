"""Rendu v4 : résumé complet au gabarit Contexte, Méthode, Notation, Preuves, Synthèse et comparaison.
Lit la version de Camille (sans la modifier) et les textes outN.json, écrit lucas/1-1-rendu-nocode-ia-v4.html."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
D = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.cwd()
TPL = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE
s = (D / 'camille/1-1-rendu-nocode-ia-nouvelle-version-camille.html').read_text(encoding='utf-8')

ENR = {}
for n in range(4):
    ENR.update(json.loads((TPL / f'out{n}.json').read_text(encoding='utf-8')))
bad = [k for k, v in ENR.items() for t in json.dumps(v, ensure_ascii=False) if t in '—–']
if bad: sys.exit(f'tiret long dans {set(bad)}')

def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: sys.exit(f'{c} occurrences pour {a[:60]}')
    s = s.replace(a, b)

# chemins : le fichier vit dans lucas/, les captures restent chez Camille
rep('"1-1-rendu-nocode-ia/captures/', '"../camille/1-1-rendu-nocode-ia/captures/', s.count('"1-1-rendu-nocode-ia/captures/'))

i = s.index('function openFull(d,btn){')
j = s.index('\n  }\n', i) + 4
old = s[i:j]
pick = re.search(r'var PICK=(\{.*?\}),pk=PICK\[it\.match\];', old).group(1)

NEW = r'''function openFull(d,btn){
    var it=d.it,col=vc(it.verdict.couleur),h='',body='',E=ENR[it.match]||{};
    function sec(id,t,c){body+='<section class="f-sec" id="fs-'+id+'"><h3>'+t+'</h3>'+c+'</section>'}
    var PICK=__PICK__,pk=PICK[it.match];
    function capsFor(s,i){var cs=s.captures||[];if(!pk)return cs.slice(0,1);return cs.filter(function(c){var f=typeof c==="string"?c:c.f;return pk[i]&&f.split("/").pop()===pk[i]})}
    function srcTag(st){return '<span class="f-src '+esc(st)+'">'+esc(STX[st]||st)+'</span>'}
    function first(x){var m=/^[^.!?]*[.!?]/.exec(String(x||""));return m?m[0]:String(x||"")}
    sec("contexte","Contexte",'<p class="f-lead">'+esc(E.contexte||it.ouverture)+'</p>');
    if(it.demarche&&it.demarche.length)sec("methode","Méthode",'<ol class="f-steps">'+it.demarche.map(function(s){return '<li><b>'+esc(s.titre)+'</b><p>'+esc(s.texte)+'</p></li>'}).join("")+'</ol>');
    if(it.criteres&&it.criteres.length)sec("notes","Notation",'<div class="f-tw"><table class="f-tab f-nt4"><thead><tr><th>Critère</th><th>Note</th><th>Justification</th></tr></thead><tbody>'+it.criteres.map(function(c,k){var m=/^(.*?)\s*\(([^)]*)\)$/.exec(c.nom),J=(E.justifs&&E.justifs[k])||c.pourquoi;return '<tr><th scope="row">'+esc(m?m[1]:c.nom)+(m?'<small>'+esc(m[2])+'</small>':'')+'</th><td class="f-nn">'+bar(c.note)+srcTag(c.statut)+'</td><td class="f-j">'+esc(J)+'</td></tr>'}).join("")+'</tbody>'+(d.s?'<tfoot><tr><th scope="row">Score</th><td colspan="2"><b>'+esc(d.s)+'</b> '+esc(d.u)+'</td></tr></tfoot>':'')+'</table></div><p class="f-note">Testé : mesuré en local. Documenté : lu dans la documentation officielle. Estimé : jugé par l’équipe.</p>');
    if(it.sections&&it.sections.length)sec("preuves","Preuves",it.sections.map(function(s,i){var cs=capsFor(s,i).map(function(c){var f=typeof c==="string"?c:c.f,l=typeof c==="string"?"":(c.legende||""),p=typeof c==="string"?"":(c.prouve||"");return '<figure><button type="button" class="f-th" title="Agrandir" data-src="'+escA(f)+'" data-l="'+escA(l)+'" data-p="'+escA(p)+'" aria-label="Agrandir : '+escA(l)+'"><img loading="lazy" src="'+escA(f)+'" alt=""></button></figure>'}).join("");var t=(E.preuves&&E.preuves[i])||first(s.texte);return '<article class="f-pr f-pr4'+(cs?'':' solo')+'"><div class="f-pt"><span class="f-pn">Preuve '+(i+1)+'</span><h4>'+esc(s.titre)+'</h4><p class="f-key">'+esc(t)+'</p></div>'+(cs?'<div class="f-caps">'+cs+'</div>':'')+'</article>'}).join(""));
    var cmp=String(comparaison(d,btn)||"").replace(/^<p>Tous les outils[^<]*<\/p>/,"");
    sec("synthese","Synthèse",'<p class="f-lead">'+esc(E.synthese||it.verdict.phrase)+'</p>'+((E.comparaison||cmp)?'<h4 class="f-sub">Comparaison</h4>'+(E.comparaison?'<p class="f-cp">'+esc(E.comparaison)+'</p>':'')+cmp:''));
    h+='<div class="p-top"><span class="p-st">Résumé complet</span><button class="p-x" type="button" aria-label="Fermer le résumé complet">Fermer</button></div>';
    h+='<div class="f-in"><header class="f-hd"><div><p class="f-ey"><i style="background:'+col+'"></i>'+esc(it.verdict.mot)+'</p><h2 id="f-nom" tabindex="-1">'+esc(d.n)+'</h2><p class="f-v">'+esc(it.verdict.phrase)+'</p></div>'+(d.s?'<div class="f-sc"><b>'+esc(d.s)+'</b><small>'+esc(d.u)+'</small></div>':'')+'</header>';
    h+=body+'</div>';
    FULL.innerHTML=h;FULL.style.setProperty("--tc",col);FULL.scrollTop=0;fromF=btn;FULL.classList.add("on");
    FULL.querySelector(".p-x").addEventListener("click",closeFull);
    FULL.querySelectorAll(".f-th").forEach(function(t){t.addEventListener("click",function(){openLb(t)})});
    setTimeout(function(){FULL.querySelector("#f-nom").focus()},30);
  }
'''.replace('__PICK__', pick)
s = s[:i] + NEW + s[j:]
rep('var RES=', 'var ENR=' + json.dumps(ENR, ensure_ascii=False).replace('</', '<\\/') + ';\nvar RES=')

CSS = '''<style id="gabarit-v4">
#full table.f-nt4,#full table.f-nt4 tbody,#full table.f-nt4 tfoot{display:block;width:100%}
#full table.f-nt4 thead{display:none!important}
#full table.f-nt4 tr{display:grid!important;grid-template-columns:210px 110px minmax(0,1fr);gap:4px 24px;padding:16px 0;border-bottom:1px solid #F0E3C8}
#full table.f-nt4 th,#full table.f-nt4 td{display:block;width:auto!important;padding:0;border:0;grid-column:auto!important;white-space:normal}
#full table.f-nt4 tbody th small{display:block;margin-top:2px;font:400 13px/18px var(--body,inherit);color:var(--muted)}
#full table.f-nt4 .f-nn{white-space:nowrap}
#full table.f-nt4 .f-nn .f-src{display:block;margin-top:6px}
#full table.f-nt4 .f-j{color:var(--fg);font-size:15px;line-height:24px}
#full table.f-nt4 tfoot tr{grid-template-columns:210px minmax(0,1fr);border-bottom:0;border-top:1px solid currentColor}
@media (max-width:720px){#full table.f-nt4 tr{grid-template-columns:1fr auto}#full table.f-nt4 .f-j{grid-column:1/-1!important}}
#full .f-pr4 .f-key{margin:0;font-size:16px;line-height:24px;font-weight:400;color:var(--muted)}
#full .f-pr4 figure{margin:0}
#full #fs-synthese .f-lead{color:var(--fg)}
#full .f-cp{margin:4px 0 12px;font-size:15px;line-height:24px}
@media (max-width:720px){#full .f-nt4 tbody th,#full .f-nt4 .f-nn{width:auto}}
</style>
</head>'''
rep('</head>', CSS)
out = D / 'lucas/1-1-rendu-nocode-ia-v4.html'
out.write_text(s, encoding='utf-8')
print('ok', len(ENR), 'fiches', len(s) // 1024, 'Ko', out)
