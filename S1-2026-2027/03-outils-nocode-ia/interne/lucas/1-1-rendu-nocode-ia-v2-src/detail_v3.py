# Panneau « résumé complet » : gabarit plus lisible (exécuté à la fin de stack_v3.py, agit sur s)
a=s.index('  function openFull(d,btn){');b=s.index('  VEIL.addEventListener("click",closePanel);',a)
JS=r'''  var LB=document.createElement("div");LB.id="lb";LB.setAttribute("role","dialog");LB.setAttribute("aria-modal","true");LB.setAttribute("aria-label","Capture agrandie");document.body.appendChild(LB);
  function closeLb(){if(!LB.classList.contains("on"))return false;LB.classList.remove("on");LB.innerHTML="";var f=LB._from;LB._from=null;if(f)try{f.focus()}catch(e){}return true}
  function openLb(btn){LB._from=btn;LB.innerHTML='<figure><img src="'+btn.dataset.src+'" alt=""><figcaption><b>'+esc(btn.dataset.p)+'</b>'+esc(btn.dataset.l)+'</figcaption></figure><button class="p-x" type="button">Fermer</button>';LB.classList.add("on");LB.querySelector(".p-x").focus()}
  LB.addEventListener("click",function(e){if(e.target===LB||e.target.closest(".p-x"))closeLb()});
  window.addEventListener("keydown",function(e){if(e.key==="Escape"&&closeLb()){e.preventDefault();e.stopImmediatePropagation()}},true);
  function bar(n){var m=/^(\d+(?:[.,]\d+)?)\s*\/\s*5$/.exec(n);if(!m)return '<span class="f-yn">'+esc(n)+'</span>';var v=parseFloat(m[1].replace(",","."));return '<span class="f-nt"><b>'+esc(m[1])+'</b><small>/5</small><i><s style="width:'+(v*20)+'%"></s></i></span>'}
  function proof(t){return String(t).split(/\n\n+/).map(function(p){var m=/^(Ce que ça change|Limite honnête|Limite)\s*:\s*/.exec(p);if(m)return '<p class="f-so'+(m[1]==="Ce que ça change"?'':' lim')+'"><b>'+esc(m[1])+'</b>'+esc(p.slice(m[0].length))+'</p>';return '<p>'+esc(p)+'</p>'}).join("")}
  function openFull(d,btn){
    var it=d.it,col=vc(it.verdict.couleur),h='',nav=[],body='';
    function sec(id,t,c){nav.push([id,t]);body+='<section class="f-sec" id="fs-'+id+'"><h3>'+t+'</h3>'+c+'</section>'}
    var ctx=String(it.plan||"").split(/\n\n+/).filter(function(p){return p&&p.indexOf(it.ouverture.slice(0,40))<0});
    sec("bref","En bref",'<p class="f-lead">'+esc(it.ouverture)+'</p>'+ctx.map(function(p){return '<p>'+esc(p)+'</p>'}).join(""));
    if(it.demarche&&it.demarche.length)sec("methode","La méthode",'<ol class="f-steps">'+it.demarche.map(function(s,i){return '<li><span>'+(i+1)+'</span><div><b>'+esc(s.titre)+'</b><p>'+esc(s.texte)+'</p></div></li>'}).join("")+'</ol>');
    if(it.criteres&&it.criteres.length)sec("notes","Les notes",'<p class="f-help">Source : <span class="tg teste">testé</span> mesuré en local, <span class="tg doc">documenté</span> lu dans la doc officielle, <span class="tg est">estimé</span> jugé par l’équipe.</p><table class="f-tab"><thead><tr><th>Critère</th><th>Note</th><th>Source</th><th>Justification</th></tr></thead><tbody>'+it.criteres.map(function(c){var m=/^(.*?)\s*\(([^)]*)\)$/.exec(c.nom);return '<tr><td><b>'+esc(m?m[1]:c.nom)+'</b>'+(m?'<small>'+esc(m[2])+'</small>':'')+'</td><td>'+bar(c.note)+'</td><td><span class="tg '+esc(c.statut)+'">'+esc(STX[c.statut]||c.statut)+'</span></td><td>'+esc(c.pourquoi)+'</td></tr>'}).join("")+'</tbody></table>');
    if(it.sections&&it.sections.length)sec("preuves","Les preuves",'<ol class="f-proofs">'+it.sections.map(function(s,i){var cs=(s.captures||[]).map(function(c){var f=typeof c==="string"?c:c.f,l=typeof c==="string"?"":(c.legende||""),p=typeof c==="string"?"":(c.prouve||"");return '<li><button type="button" class="f-th" data-src="'+esc(f)+'" data-l="'+esc(l)+'" data-p="'+esc(p)+'" aria-label="Agrandir : '+esc(l)+'"><img loading="lazy" src="'+esc(f)+'" alt=""></button><span>'+esc(p||l)+'</span></li>'}).join("");return '<li><span class="f-pn">'+String(i+1).padStart(2,"0")+'</span><div><b>'+esc(s.titre)+'</b>'+proof(s.texte)+(cs?'<ul class="f-caps">'+cs+'</ul>':'')+'</div></li>'}).join("")+'</ol>');
    var lc='';
    if(it.limites&&it.limites.length)lc+='<div><h4>Limites</h4><ul>'+it.limites.map(function(l){return '<li>'+esc(l)+'</li>'}).join("")+'</ul></div>';
    if(it.couts&&it.couts.length)lc+='<div><h4>Coûts</h4><ul>'+it.couts.map(function(l){return '<li>'+esc(l)+'</li>'}).join("")+'</ul></div>';
    if(lc)sec("limites","Limites et coûts",'<div class="f-two">'+lc+'</div>');
    if(it.jury){var L={pertinence:"Critères pertinents",rigueur:"Rigueur du benchmark",cdc:"Réponse au cahier des charges",boite_ia:"Boîte à outils IA",lucidite:"Lucidité sur les limites"};sec("jury","Grille du jury",'<dl class="f-jury">'+Object.keys(L).filter(function(k){return it.jury[k]}).map(function(k){return '<div><dt>'+L[k]+'</dt><dd>'+esc(it.jury[k])+'</dd></div>'}).join("")+'</dl>')}
    h+='<div class="p-top"><span class="p-st">'+esc(it.verdict.mot)+' · résumé complet</span><button class="p-x" type="button" aria-label="Fermer le résumé complet">Fermer</button></div>';
    h+='<div class="f-in"><header class="f-hd"><div><h2 id="f-nom" tabindex="-1">'+esc(d.n)+'</h2><p class="f-v"><b style="--tc:'+col+'">'+esc(it.verdict.mot)+'</b>'+esc(it.verdict.phrase)+'</p></div>'+(d.s&&!(it.chiffres||[]).some(function(c){return String(c.valeur).indexOf(d.s)===0})?'<div class="f-sc"><b>'+esc(d.s)+'</b><small>'+esc(d.u)+'</small></div>':'')+'</header>';
    if(it.chiffres&&it.chiffres.length)h+='<div class="f-facts">'+it.chiffres.map(function(c){var m=/^([\d\s.,]+)(.*)$/.exec(c.valeur);return '<div><b>'+esc(m?m[1].trim():c.valeur)+(m&&m[2]?'<small>'+esc(m[2].trim())+'</small>':'')+'</b><span>'+esc(c.libelle)+'</span></div>'}).join("")+'</div>';
    h+='<nav class="f-nav" aria-label="Sections du résumé">'+nav.map(function(n){return '<button type="button" data-go="fs-'+n[0]+'">'+n[1]+'</button>'}).join("")+'</nav>'+body+'</div>';
    FULL.innerHTML=h;FULL.style.setProperty("--tc",col);FULL.scrollTop=0;fromF=btn;FULL.classList.add("on");
    FULL.querySelector(".p-x").addEventListener("click",closeFull);
    FULL.querySelector(".f-nav").addEventListener("click",function(e){var b=e.target.closest("[data-go]");if(b){var t=FULL.querySelector("#"+b.dataset.go);FULL.scrollTo({top:t.offsetTop-72,behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"})}});
    FULL.querySelectorAll(".f-th").forEach(function(t){t.addEventListener("click",function(){openLb(t)})});
    setTimeout(function(){FULL.querySelector("#f-nom").focus()},30);
  }
'''
s=s[:a]+JS+s[b:]
CSSD='''<style>
/* résumé complet, gabarit lisible */
#full .p-top{position:sticky;top:0;z-index:3;background:var(--bg)}
.f-in{max-width:1040px;padding-top:40px}
.f-hd{display:flex;gap:24px 48px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;padding-bottom:28px;border-bottom:1px solid var(--fg)}
.f-hd>div:first-child{flex:1 1 420px}
.f-in .f-hd h2{margin:0;font:600 clamp(26px,3vw,36px)/1.15 var(--title);letter-spacing:-.015em}
.f-v{margin:12px 0 0;font-size:17px;line-height:26px;max-width:62ch}
.f-v b{display:inline-flex;align-items:center;gap:6px;margin-right:10px;padding:2px 10px;border-radius:999px;background:#FFF3D9;color:var(--fg);font:500 13px/20px var(--title);vertical-align:1px}.f-v b:before{content:"";width:8px;height:8px;border-radius:50%;background:var(--tc)}
.f-sc{text-align:right}
.f-sc b{display:block;font:600 56px/1 var(--title);letter-spacing:-.02em}
.f-sc small{font-size:13px;color:var(--muted)}
.f-facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:0 32px;margin-top:28px}
.f-facts>div{padding-top:14px;border-top:2px solid var(--fg)}
.f-facts b{display:block;font:600 34px/1.1 var(--title);letter-spacing:-.02em}
.f-facts b small{font:500 15px var(--title);margin-left:4px;color:var(--muted)}
.f-facts span{display:block;margin-top:6px;font-size:14px;line-height:20px;color:var(--muted)}
.f-nav{position:sticky;top:64px;z-index:2;display:flex;flex-wrap:wrap;gap:8px;margin:36px 0 0;padding:12px 0;background:var(--bg);border-bottom:1px solid var(--hair)}
.f-nav button{font:500 14px/20px var(--title);padding:6px 14px;border-radius:999px;border:1px solid var(--hair);background:#FFF3D9;color:var(--fg);cursor:pointer}
.f-nav button:hover{background:#FFD36E;border-color:#FFD36E}
#full .f-sec{margin-top:48px;padding-top:0;border-top:0;scroll-margin-top:140px}
#full .f-sec h3{font:600 22px/30px var(--title);margin:0 0 16px;padding-bottom:10px;border-bottom:1px solid var(--hair)}
#full .f-sec p{font-size:16px;line-height:25px}
#full .f-sec .f-lead{font-size:19px;line-height:29px;color:var(--fg);max-width:60ch}
.f-help{font-size:14px!important;line-height:22px!important}
.f-steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px 32px}
.f-steps li{display:flex;gap:14px;padding:0;border:0}
.f-steps li>span{flex:none;width:28px;height:28px;border-radius:50%;background:#FFF3D9;font:600 13px/28px var(--title);text-align:center}
.f-steps b{font:500 16px/22px var(--title);color:var(--fg)}
#full .f-steps p{margin:4px 0 0;font-size:14px;line-height:21px}
#full .f-tab td{font-size:14px;line-height:21px;color:var(--muted)}
#full .f-tab td:first-child{width:22%;color:var(--fg)}
.f-tab td small{display:block;font-weight:400;color:var(--muted);font-size:12px}
.f-nt{display:inline-flex;align-items:baseline;gap:2px;white-space:nowrap}
.f-nt b{font:600 18px var(--title);color:var(--fg)}
.f-nt small{font-size:12px}
.f-nt i{display:inline-block;width:44px;height:4px;margin-left:8px;border-radius:2px;background:#F0E3C8;vertical-align:middle;overflow:hidden}
.f-nt s{display:block;height:100%;background:var(--fg)}
.f-yn{font:600 15px var(--title);color:var(--fg)}
.f-proofs{list-style:none;margin:0;padding:0}
.f-proofs>li{display:flex;gap:20px;padding:20px 0;border-top:1px solid var(--hair)}
.f-proofs>li:first-child{border-top:0;padding-top:0}
.f-pn{flex:none;font:500 13px/24px var(--mono);color:var(--muted)}
.f-proofs>li>div{flex:1;min-width:0}
.f-proofs>li>div>b{display:block;font:500 17px/24px var(--title);margin-bottom:6px;color:var(--fg)}
#full .f-so{margin:10px 0 12px;padding:10px 14px;background:#FFF3D9;border-radius:8px;color:var(--fg);max-width:64ch}
#full .f-so.lim{background:transparent;border:1px dashed #E2D6BF;color:var(--muted)}
.f-so b{display:block;font:500 12px/18px var(--title);text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.f-caps{list-style:none;margin:8px 0 0!important;padding:0;display:grid!important;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;max-width:none!important}
.f-caps li{padding:0!important;border:0!important;font-size:13px;line-height:19px}
.f-th{display:block;width:100%;padding:0;border:1px solid var(--hair);border-radius:8px;overflow:hidden;background:#fff;cursor:zoom-in}
.f-th img{display:block;width:100%;height:120px;object-fit:cover;object-position:top left;transition:transform .3s}
.f-th:hover img{transform:scale(1.03)}
.f-caps li>span{display:block;margin-top:6px}
.f-two{display:grid;grid-template-columns:1fr 1fr;gap:32px}
.f-two h4{margin:0 0 6px;font:500 13px/18px var(--title);text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
#full .f-two li{font-size:14px;line-height:21px}
.f-jury{display:grid!important;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))!important;gap:12px!important}
.f-jury>div{padding:14px 16px;background:#FFF3D9;border-radius:8px}
#full .f-jury dt{border:0;padding:0;font-size:15px}
#full .f-jury dd{border:0;padding:4px 0 0;font-size:14px;line-height:21px}
#lb{position:fixed;inset:0;z-index:130;display:none;align-items:center;justify-content:center;padding:32px;background:rgba(31,26,23,.86)}
#lb.on{display:flex}
#lb figure{margin:0;max-width:min(1200px,100%);max-height:100%;display:flex;flex-direction:column;gap:12px}
#lb img{max-width:100%;max-height:calc(100vh - 160px);object-fit:contain;border-radius:8px;background:#fff}
#lb figcaption{color:#FFF3D9;font-size:14px;line-height:20px}
#lb figcaption b{display:block;color:#fff;font-weight:600}
#lb .p-x{position:absolute;top:16px;right:16px;background:#FFF3D9}
@media(max-width:720px){.f-two{grid-template-columns:1fr}.f-sc{text-align:left}.f-tab thead{display:none}.f-tab tr{display:block;padding:12px 0;border-bottom:1px solid var(--hair)}#full .f-tab td{display:block;border:0;padding:2px 0;width:auto}.f-nav{top:56px}}
@media(prefers-reduced-motion:reduce){.f-th img{transition:none}}
</style>
'''
s=s.replace('</head>',CSSD+'</head>',1)
