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
    function sec(id,t,c,q){nav.push([id,t]);body+='<section class="f-sec" id="fs-'+id+'"><header class="f-sh"><span>'+nav.length+'</span><div><h3>'+t+'</h3>'+(q?'<p>'+q+'</p>':'')+'</div></header>'+c+'</section>'}
    var ctx=String(it.plan||"").split(/\n\n+/).filter(function(p){return p&&p.indexOf(it.ouverture.slice(0,40))<0});
    sec("bref","En bref",'<div class="f-card f-lead">'+esc(it.ouverture)+'</div>'+(ctx.length?'<details class="f-more"><summary>Lire le contexte</summary>'+ctx.map(function(p){return '<p>'+esc(p)+'</p>'}).join("")+'</details>':''),"L’essentiel en une phrase.");
    if(it.demarche&&it.demarche.length)sec("methode","Comment on a testé",'<ol class="f-steps">'+it.demarche.map(function(s,i){return '<li><span>'+(i+1)+'</span><div><b>'+esc(s.titre)+'</b><p>'+esc(s.texte)+'</p></div></li>'}).join("")+'</ol>',"Les étapes, dans l’ordre.");
    if(it.criteres&&it.criteres.length)sec("notes","Les notes, critère par critère",'<p class="f-help"><span class="tg teste">testé</span> mesuré en local <span class="tg doc">documenté</span> lu dans la doc <span class="tg est">estimé</span> jugé par l’équipe</p><ul class="f-crit">'+it.criteres.map(function(c){var m=/^(.*?)\s*\(([^)]*)\)$/.exec(c.nom);return '<li><div class="f-cn">'+bar(c.note)+'</div><div><div class="f-ct"><b>'+esc(m?m[1]:c.nom)+'</b>'+(m?'<small>poids '+esc(m[2])+'</small>':'')+'<span class="tg '+esc(c.statut)+'">'+esc(STX[c.statut]||c.statut)+'</span></div><p>'+esc(c.pourquoi)+'</p></div></li>'}).join("")+'</ul>',"Chaque note sur 5, sa source et pourquoi.");
    if(it.sections&&it.sections.length)sec("preuves","Les preuves",'<ol class="f-proofs">'+it.sections.map(function(s,i){var cs=(s.captures||[]).map(function(c){var f=typeof c==="string"?c:c.f,l=typeof c==="string"?"":(c.legende||""),p=typeof c==="string"?"":(c.prouve||"");return '<li><button type="button" class="f-th" title="Agrandir" data-src="'+escA(f)+'" data-l="'+escA(l)+'" data-p="'+escA(p)+'" aria-label="Agrandir : '+escA(l)+'"><img loading="lazy" src="'+escA(f)+'" alt=""></button><span>'+esc(p||l)+'</span></li>'}).join("");return '<li><span class="f-pn">'+String(i+1).padStart(2,"0")+'</span><div><b>'+esc(s.titre)+'</b>'+proof(s.texte)+(cs?'<ul class="f-caps">'+cs+'</ul>':'')+'</div></li>'}).join("")+'</ol>',"Ce qu’on a vraiment vérifié. Clique sur une capture pour l’agrandir.");
    var lc='';
    if(it.limites&&it.limites.length)lc+='<div><h4>Limites</h4><ul>'+it.limites.map(function(l){return '<li>'+esc(l)+'</li>'}).join("")+'</ul></div>';
    if(it.couts&&it.couts.length)lc+='<div><h4>Coûts</h4><ul>'+it.couts.map(function(l){return '<li>'+esc(l)+'</li>'}).join("")+'</ul></div>';
    if(lc)sec("limites","Limites et coûts",'<div class="f-two">'+lc+'</div>',"Ce qui reste fragile, et ce que ça coûte.");
    if(it.jury){var L={pertinence:"Critères pertinents",rigueur:"Rigueur du benchmark",cdc:"Réponse au cahier des charges",boite_ia:"Boîte à outils IA",lucidite:"Lucidité sur les limites"};sec("jury","Grille du jury",'<dl class="f-jury">'+Object.keys(L).filter(function(k){return it.jury[k]}).map(function(k){return '<div><dt>'+L[k]+'</dt><dd>'+esc(it.jury[k])+'</dd></div>'}).join("")+'</dl>',"Où trouver chaque point attendu par le jury.")}
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
/* résumé complet, charte Soly, lecture en une colonne */
#full .p-top{position:sticky;top:0;z-index:3;background:var(--bg);border-bottom:1px solid #F0E3C8}
.f-in{max-width:860px;margin:0 auto;padding:40px 24px 80px}
.f-hd{display:flex;gap:24px;align-items:flex-start;justify-content:space-between;padding:28px;border-radius:24px;background:#FFF3D9}
.f-in .f-hd h2{margin:0;font:600 clamp(24px,3vw,34px)/1.15 var(--title);letter-spacing:-.01em}
.f-v{margin:14px 0 0;font-size:18px;line-height:28px;color:var(--fg)}
.f-v b{display:inline-flex;align-items:center;gap:8px;margin-right:10px;padding:4px 14px;border-radius:999px;background:#FFFAF0;font:500 14px/20px var(--title);color:#1F1A17;vertical-align:1px}
.f-v b:before{content:"";width:10px;height:10px;border-radius:50%;background:var(--tc)}
.f-sc{flex:none;text-align:center;padding:14px 18px;border-radius:18px;background:#FFFAF0}
.f-sc b{display:block;font:600 40px/1 var(--title)}
.f-sc small{font-size:13px;color:var(--muted)}
#full .f-sec{margin:48px 0 0;padding:0;border:0}
.f-sh{display:flex;gap:14px;align-items:flex-start;margin-bottom:18px}
.f-sh>span{flex:none;display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:#FFD36E;font:600 16px/1 var(--title);color:#1F1A17}
#full .f-sh h3{margin:6px 0 0;padding:0;border:0;font:600 22px/28px var(--title)}
#full .f-sh p{margin:2px 0 0;font-size:15px;line-height:22px;color:var(--muted)}
#full .f-sec p{font-size:17px;line-height:27px}
.f-card{padding:22px 24px;border-radius:18px;background:#FFF3D9}
#full .f-lead{font-size:20px;line-height:31px;color:var(--fg)}
.f-more{margin-top:12px}
.f-more summary{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border:2px solid #1F1A17;border-radius:999px;font:500 15px var(--title);cursor:pointer;list-style:none}
.f-more summary::-webkit-details-marker{display:none}
.f-more summary:after{content:"+";margin-left:10px}.f-more[open] summary:after{content:"\2212"}
.f-more p{max-width:68ch}
.f-steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
.f-steps li{display:flex;gap:12px;padding:18px;border-radius:16px;background:#FFF3D9;border:0}
.f-steps li>span{flex:none;display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:50%;background:#FFFAF0;font:600 14px/1 var(--title)}
.f-steps b{display:block;font:600 16px/22px var(--title);color:var(--fg)}
#full .f-steps p{margin:4px 0 0;font-size:15px;line-height:22px;color:var(--muted)}
.f-help{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;margin:0 0 14px!important;font-size:14px!important;line-height:20px!important;color:var(--muted)}
.f-help .tg{margin-left:4px}
.f-crit{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.f-crit>li{display:grid;grid-template-columns:96px 1fr;gap:18px;padding:18px 20px;border-radius:16px;background:#FFF3D9}
.f-cn{padding-top:2px}
.f-ct{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center}
.f-ct b{font:600 17px/24px var(--title)}
.f-ct small{font-size:13px;color:var(--muted)}
.f-ct .tg{margin-left:auto;padding:3px 12px;font-size:13px}
#full .f-crit p{margin:6px 0 0;font-size:15px;line-height:23px;color:var(--muted)}
.f-nt{display:flex;flex-wrap:wrap;align-items:baseline;gap:2px}
.f-nt b{font:600 28px/1 var(--title);color:var(--fg)}
.f-nt small{font-size:14px;color:var(--muted)}
.f-nt i{display:block;width:100%;height:6px;margin-top:8px;border-radius:9px;background:#FFFAF0;overflow:hidden}
.f-nt s{display:block;height:100%;border-radius:9px;background:#1F1A17}
.f-yn{font:600 18px var(--title);color:var(--fg)}
.f-proofs{list-style:none;margin:0;padding:0;display:grid;gap:16px}
.f-proofs>li{display:block;padding:24px;border-radius:20px;background:#FFF3D9}
.f-pn{display:inline-block;padding:2px 12px;border-radius:999px;background:#FFFAF0;font:500 13px/20px var(--title);color:var(--muted)}
.f-proofs>li>div>b{display:block;margin:10px 0 4px;font:600 20px/27px var(--title);color:var(--fg)}
#full .f-proofs p{font-size:16px;line-height:26px}
#full .f-so{margin:14px 0;padding:14px 18px;border:0;border-radius:14px;background:#FFFAF0;color:var(--fg)}
#full .f-so b{display:block;margin-bottom:2px;font:600 13px/18px var(--title);color:#1F1A17;text-transform:none;letter-spacing:0}
#full .f-so b:before{content:"";display:inline-block;width:10px;height:10px;margin-right:8px;border-radius:50%;background:#FFD36E}
#full .f-so.lim b:before{background:#C9B8F0}
.f-caps{list-style:none;margin:16px 0 0!important;padding:0;display:grid!important;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;max-width:none!important}
.f-caps li{padding:0!important;border:0!important;font-size:14px;line-height:20px;color:var(--muted)}
.f-th{position:relative;display:block;width:100%;padding:0;border:1px solid #F0E3C8;border-radius:14px;overflow:hidden;background:#fff;cursor:zoom-in}
.f-th img{display:block;width:100%;height:240px;object-fit:cover;object-position:top left}
.f-th:after{content:"Agrandir";position:absolute;right:10px;bottom:10px;padding:4px 12px;border-radius:999px;background:#1F1A17;color:#FFFAF0;font:500 13px/18px var(--title);opacity:0;transition:opacity .2s}
.f-th:hover:after,.f-th:focus-visible:after{opacity:1}
.f-caps li>span{display:block;margin-top:8px}
.f-two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.f-two>div{padding:20px 22px;border-radius:16px;background:#FFF3D9}
.f-two h4{margin:0 0 8px;font:600 17px/24px var(--title);text-transform:none;letter-spacing:0;color:var(--fg)}
.f-two ul{margin:0;padding-left:18px}
#full .f-two li{font-size:15px;line-height:23px;margin:4px 0;color:var(--muted)}
.f-jury{display:grid!important;grid-template-columns:1fr 1fr!important;gap:12px!important;margin:0}
.f-jury>div{padding:18px 20px;border-radius:16px;background:#FFF3D9}
#full .f-jury dt{border:0;padding:0;font:600 16px/22px var(--title)}
#full .f-jury dd{margin:0;border:0;padding:6px 0 0;font-size:15px;line-height:23px;color:var(--muted)}
#lb{position:fixed;inset:0;z-index:130;display:none;align-items:center;justify-content:center;padding:32px;background:rgba(31,26,23,.9)}
#lb.on{display:flex}
#lb figure{margin:0;max-width:min(1300px,100%);max-height:100%;display:flex;flex-direction:column;gap:12px}
#lb img{max-width:100%;max-height:calc(100vh - 160px);object-fit:contain;background:#fff;border-radius:12px}
#lb figcaption{color:#FFF3D9;font-size:14px;line-height:20px}
#lb figcaption b{display:block;color:#fff;font-weight:600}
#lb .p-x{position:absolute;top:16px;right:16px;background:#FFF3D9}
@media(max-width:720px){.f-in{padding:24px 16px 64px}.f-hd{flex-direction:column;padding:22px}.f-caps{grid-template-columns:1fr}.f-th img{height:200px}.f-two,.f-jury{grid-template-columns:1fr!important}.f-crit>li{grid-template-columns:1fr;gap:8px}.f-nt i{max-width:160px}.f-ct .tg{margin-left:0}}
@media(prefers-reduced-motion:reduce){.f-th:after{transition:none}}
</style>
'''
s=s.replace('</head>',CSSD+'</head>',1)
