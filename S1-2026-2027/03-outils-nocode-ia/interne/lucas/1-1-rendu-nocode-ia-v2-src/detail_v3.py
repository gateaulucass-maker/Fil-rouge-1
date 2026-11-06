# Panneau « résumé complet » : gabarit plus lisible (exécuté à la fin de stack_v3.py, agit sur s)
a=s.index('  function openFull(d,btn){');b=s.index('  VEIL.addEventListener("click",closePanel);',a)
JS=r'''  var LB=document.createElement("div");LB.id="lb";LB.setAttribute("role","dialog");LB.setAttribute("aria-modal","true");LB.setAttribute("aria-label","Capture agrandie");document.body.appendChild(LB);
  function escA(x){return esc(x).replace(/"/g,"&quot;")}
  function closeLb(){if(!LB.classList.contains("on"))return false;LB.classList.remove("on");LB.innerHTML="";var f=LB._from;LB._from=null;if(f)try{f.focus()}catch(e){}return true}
  function openLb(btn){LB._from=btn;LB.innerHTML='<figure><img src="'+escA(btn.dataset.src)+'" alt=""><figcaption><b>'+esc(btn.dataset.p)+'</b>'+esc(btn.dataset.l)+'</figcaption></figure><button class="p-x" type="button">Fermer</button>';LB.classList.add("on");LB.querySelector(".p-x").focus()}
  LB.addEventListener("click",function(e){if(e.target===LB||e.target.closest(".p-x"))closeLb()});
  window.addEventListener("keydown",function(e){if(e.key==="Escape"&&closeLb()){e.preventDefault();e.stopImmediatePropagation()}},true);
  function bar(n){var m=/^(\d+(?:[.,]\d+)?)\s*\/\s*5$/.exec(n);if(!m)return '<span class="f-yn">'+esc(n)+'</span>';var v=parseFloat(m[1].replace(",","."));return '<span class="f-nt"><b>'+esc(m[1])+'</b><small>/5</small><i><s style="width:'+(v*20)+'%"></s></i></span>'}
  function proof(t){return String(t).split(/\n\n+/).map(function(p){var m=/^(Ce que ça change|Limite honnête|Limite)\s*:\s*/.exec(p);if(m)return '<p class="f-so'+(m[1]==="Ce que ça change"?'':' lim')+'"><b>'+esc(m[1])+'</b>'+esc(p.slice(m[0].length))+'</p>';return '<p>'+esc(p)+'</p>'}).join("")}
  function openFull(d,btn){
    var it=d.it,col=vc(it.verdict.couleur),h='',nav=[],body='';
    function sec(id,t,c){nav.push([id,t]);body+='<section class="f-sec" id="fs-'+id+'"><h3><span>'+String(nav.length).padStart(2,"0")+'</span>'+t+'</h3><div class="f-bd">'+c+'</div></section>'}
    var ctx=String(it.plan||"").split(/\n\n+/).filter(function(p){return p&&p.indexOf(it.ouverture.slice(0,40))<0});
    sec("bref","En bref",'<p class="f-lead">'+esc(it.ouverture)+'</p>'+ctx.map(function(p){return '<p>'+esc(p)+'</p>'}).join(""));
    if(it.demarche&&it.demarche.length)sec("methode","La méthode",'<ol class="f-steps">'+it.demarche.map(function(s,i){return '<li><span>'+(i+1)+'</span><div><b>'+esc(s.titre)+'</b><p>'+esc(s.texte)+'</p></div></li>'}).join("")+'</ol>');
    if(it.criteres&&it.criteres.length)sec("notes","Les notes",'<p class="f-help">Source : <span class="tg teste">testé</span> mesuré en local, <span class="tg doc">documenté</span> lu dans la doc officielle, <span class="tg est">estimé</span> jugé par l’équipe.</p><table class="f-tab"><thead><tr><th>Critère</th><th>Note</th><th>Source</th><th>Justification</th></tr></thead><tbody>'+it.criteres.map(function(c){var m=/^(.*?)\s*\(([^)]*)\)$/.exec(c.nom);return '<tr><td><b>'+esc(m?m[1]:c.nom)+'</b>'+(m?'<small>'+esc(m[2])+'</small>':'')+'</td><td>'+bar(c.note)+'</td><td><span class="tg '+esc(c.statut)+'">'+esc(STX[c.statut]||c.statut)+'</span></td><td>'+esc(c.pourquoi)+'</td></tr>'}).join("")+'</tbody></table>');
    if(it.sections&&it.sections.length)sec("preuves","Les preuves",'<ol class="f-proofs">'+it.sections.map(function(s,i){var cs=(s.captures||[]).map(function(c){var f=typeof c==="string"?c:c.f,l=typeof c==="string"?"":(c.legende||""),p=typeof c==="string"?"":(c.prouve||"");return '<li><button type="button" class="f-th" data-src="'+escA(f)+'" data-l="'+escA(l)+'" data-p="'+escA(p)+'" aria-label="Agrandir : '+escA(l)+'"><img loading="lazy" src="'+escA(f)+'" alt=""></button><span>'+esc(p||l)+'</span></li>'}).join("");return '<li><span class="f-pn">'+String(i+1).padStart(2,"0")+'</span><div><b>'+esc(s.titre)+'</b>'+proof(s.texte)+(cs?'<ul class="f-caps">'+cs+'</ul>':'')+'</div></li>'}).join("")+'</ol>');
    var lc='';
    if(it.limites&&it.limites.length)lc+='<div><h4>Limites</h4><ul>'+it.limites.map(function(l){return '<li>'+esc(l)+'</li>'}).join("")+'</ul></div>';
    if(it.couts&&it.couts.length)lc+='<div><h4>Coûts</h4><ul>'+it.couts.map(function(l){return '<li>'+esc(l)+'</li>'}).join("")+'</ul></div>';
    if(lc)sec("limites","Limites et coûts",'<div class="f-two">'+lc+'</div>');
    if(it.jury){var L={pertinence:"Critères pertinents",rigueur:"Rigueur du benchmark",cdc:"Réponse au cahier des charges",boite_ia:"Boîte à outils IA",lucidite:"Lucidité sur les limites"};sec("jury","Grille du jury",'<dl class="f-jury">'+Object.keys(L).filter(function(k){return it.jury[k]}).map(function(k){return '<div><dt>'+L[k]+'</dt><dd>'+esc(it.jury[k])+'</dd></div>'}).join("")+'</dl>')}
    h+='<div class="p-top"><span class="p-st">'+esc(it.verdict.mot)+' · résumé complet</span><button class="p-x" type="button" aria-label="Fermer le résumé complet">Fermer</button></div>';
    h+='<div class="f-in"><header class="f-hd"><div><h2 id="f-nom" tabindex="-1">'+esc(d.n)+'</h2><p class="f-v"><b style="--tc:'+col+'">'+esc(it.verdict.mot)+'</b>'+esc(it.verdict.phrase)+'</p></div>'+(d.s?'<div class="f-sc"><b>'+esc(d.s)+'</b><small>'+esc(d.u)+'</small></div>':'')+'</header>';
    h+=body+'</div>';
    FULL.innerHTML=h;FULL.style.setProperty("--tc",col);FULL.scrollTop=0;fromF=btn;FULL.classList.add("on");
    FULL.querySelector(".p-x").addEventListener("click",closeFull);
    FULL.querySelectorAll(".f-th").forEach(function(t){t.addEventListener("click",function(){openLb(t)})});
    setTimeout(function(){FULL.querySelector("#f-nom").focus()},30);
  }
'''
s=s[:a]+JS+s[b:]
CSSD='''<style>
/* résumé complet, style suisse */
#full .p-top{position:sticky;top:0;z-index:3;background:var(--bg)}
.f-in{max-width:1120px;padding-top:48px}
.f-hd{display:grid;grid-template-columns:1fr auto;gap:24px 48px;align-items:end;padding-bottom:24px;border-bottom:2px solid var(--fg)}
.f-in .f-hd h2{margin:0;font:600 clamp(26px,3vw,38px)/1.1 var(--title);letter-spacing:-.02em}
.f-v{margin:14px 0 0;font-size:17px;line-height:26px;max-width:60ch}
.f-v b{margin-right:10px;font:600 13px/20px var(--title);text-transform:uppercase;letter-spacing:.08em;color:var(--fg)}
.f-v b:before{content:"";display:inline-block;width:10px;height:10px;margin-right:8px;background:var(--tc);vertical-align:0}
.f-sc{text-align:right}
.f-sc b{display:block;font:600 44px/1 var(--title);letter-spacing:-.02em}
.f-sc small{font-size:13px;color:var(--muted)}
#full .f-sec{display:grid;grid-template-columns:220px 1fr;gap:16px 40px;margin:0;padding:32px 0;border-top:1px solid var(--fg)}
#full .f-hd+.f-sec{border-top:0}
#full .f-sec h3{margin:0;padding:0;border:0;font:600 17px/24px var(--title)}
#full .f-sec h3 span{display:block;margin-bottom:4px;font:500 13px/18px var(--mono);color:var(--muted)}
.f-bd{min-width:0}
#full .f-sec p{font-size:16px;line-height:25px;max-width:64ch}
#full .f-sec .f-lead{margin-top:0;font-size:19px;line-height:29px;color:var(--fg)}
.f-help{margin-top:0!important;font-size:14px!important;line-height:22px!important}
.f-steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px 32px}
.f-steps li{display:block;padding:12px 0 0;border:0;border-top:1px solid var(--hair)}
.f-steps li>span{display:block;font:500 13px/18px var(--mono);color:var(--muted)}
.f-steps b{display:block;margin-top:4px;font:500 16px/22px var(--title);color:var(--fg)}
#full .f-steps p{margin:4px 0 0;font-size:14px;line-height:21px}
#full .f-tab{margin-top:8px}
#full .f-tab td{font-size:14px;line-height:21px;color:var(--muted)}
#full .f-tab td:first-child{width:24%;color:var(--fg)}
.f-tab td small{display:block;font-weight:400;color:var(--muted);font-size:12px}
.f-nt{display:inline-flex;align-items:baseline;gap:2px;white-space:nowrap}
.f-nt b{font:600 18px var(--title);color:var(--fg)}
.f-nt small{font-size:12px}
.f-nt i{display:inline-block;width:44px;height:4px;margin-left:8px;background:#F0E3C8;vertical-align:middle;overflow:hidden}
.f-nt s{display:block;height:100%;background:var(--fg)}
.f-yn{font:600 15px var(--title);color:var(--fg)}
.f-proofs{list-style:none;margin:0;padding:0}
.f-proofs>li{display:block;padding:24px 0;border-top:1px solid var(--hair)}
.f-proofs>li:first-child{border-top:0;padding-top:0}
.f-pn{display:block;font:500 13px/18px var(--mono);color:var(--muted)}
.f-proofs>li>div>b{display:block;margin:2px 0 6px;font:500 18px/26px var(--title);color:var(--fg)}
#full .f-so{margin:12px 0;padding:0 0 0 14px;border-left:3px solid #FFD36E;color:var(--fg)}
#full .f-so.lim{border-left-color:#C9B8F0;color:var(--muted)}
.f-so b{display:block;font:600 12px/18px var(--title);text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.f-caps{list-style:none;margin:16px 0 0!important;padding:0;display:grid!important;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:24px;max-width:none!important}
.f-caps li{padding:0!important;border:0!important;font-size:13px;line-height:19px;color:var(--muted)}
.f-th{display:block;width:100%;padding:0;border:1px solid var(--hair);overflow:hidden;background:#fff;cursor:zoom-in}
.f-th img{display:block;width:100%;height:260px;object-fit:cover;object-position:top left;transition:opacity .2s}
.f-th:hover img{opacity:.85}
.f-caps li>span{display:block;margin-top:8px}
.f-two{display:grid;grid-template-columns:1fr 1fr;gap:32px}
.f-two h4{margin:0 0 6px;font:600 12px/18px var(--title);text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
#full .f-two li{font-size:14px;line-height:21px}
.f-jury{display:grid!important;grid-template-columns:1fr 1fr!important;gap:0 32px!important;margin:0}
.f-jury>div{padding:12px 0;border-top:1px solid var(--hair)}
#full .f-jury dt{border:0;padding:0;font-size:15px}
#full .f-jury dd{margin:0;border:0;padding:4px 0 0;font-size:14px;line-height:21px}
#lb{position:fixed;inset:0;z-index:130;display:none;align-items:center;justify-content:center;padding:32px;background:rgba(31,26,23,.9)}
#lb.on{display:flex}
#lb figure{margin:0;max-width:min(1300px,100%);max-height:100%;display:flex;flex-direction:column;gap:12px}
#lb img{max-width:100%;max-height:calc(100vh - 160px);object-fit:contain;background:#fff}
#lb figcaption{color:#FFF3D9;font-size:14px;line-height:20px}
#lb figcaption b{display:block;color:#fff;font-weight:600}
#lb .p-x{position:absolute;top:16px;right:16px;background:#FFF3D9}
#full .tg{display:inline-flex;align-items:center;gap:6px;padding:0;border:0;border-radius:0;background:none!important;font:500 13px/18px var(--title);color:var(--fg)}
#full .tg:before{content:"";width:9px;height:9px;background:#C9B8F0}
#full .tg.teste:before{background:#FFD36E}#full .tg.est:before{background:#FFC9A3}
@media(max-width:820px){#full .f-sec{grid-template-columns:1fr}.f-caps{grid-template-columns:1fr}.f-th img{height:200px}.f-two,.f-jury{grid-template-columns:1fr!important}.f-hd{grid-template-columns:1fr}.f-sc{text-align:left}.f-tab thead{display:none}.f-tab tr{display:block;padding:12px 0;border-bottom:1px solid var(--hair)}#full .f-tab td{display:block;border:0;padding:2px 0;width:auto}}
@media(prefers-reduced-motion:reduce){.f-th img{transition:none}}
</style>
'''
s=s.replace('</head>',CSSD+'</head>',1)
