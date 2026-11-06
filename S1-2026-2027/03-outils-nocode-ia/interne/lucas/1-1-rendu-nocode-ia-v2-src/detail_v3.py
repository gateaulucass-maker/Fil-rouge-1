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
    var it=d.it,col=vc(it.verdict.couleur),h='',body='';
    function sec(id,t,c){body+='<section class="f-sec" id="fs-'+id+'"><h3>'+t+'</h3>'+c+'</section>'}
    function keyFirst(x){var ps=String(x).split(/\n\n+/),k='',rest=[];ps.forEach(function(p){var m=/^Ce que ça change\s*:\s*/.exec(p);if(m&&!k){var q=p.slice(m[0].length);k='<p class="f-key">'+esc(q.charAt(0).toUpperCase()+q.slice(1))+'</p>'}else rest.push(p)});return k+'<div class="f-det">'+proof(rest.join("\n\n"))+'</div>'}
    var PICK={"^A ·": ["t01-supabase-console.jpg", "p03-controle-negatif.jpg", "p02-temps-reel.jpg", "p05-changement-heure.jpg", "", ""], "^G ·": ["s09-baserow-photos-doublon-accepte.jpg", "s07-n8n-recoit-webhook-baserow.jpg", "", ""], "^D ·": ["", "", "o5-flutterflow-prix.jpg"], "^E ·": ["", "s04-n8n-toucher-execution-refusee-doublon.jpg", "o2x-weweb-n8n.jpg"], "^F ·": ["", "", "o2x-baserow-donnees-allemagne.jpg"], "^Le Chat": ["r2-mistral-donnees-ue.jpg", "p10-mistral-limite.jpg", "", "w04-demo-fautive-controles-rouges.jpg"], "^Claude Haiku": ["p09-ia-banc.jpg", "", "", "w03-valide-dans-file-envoi.jpg", ""], "^Claude Sonnet": ["p08-ia-pieges.jpg", "", "g01-garde-fous.jpg", "c1-vals-index.jpg"], "^Claude Opus": ["c1-vals-index.jpg"], "^ChatGPT": ["p07-ia-anniversaire.jpg", ""], "^Grok": ["", ""], "^Gemini 3\\.5": ["", ""], "^DeepSeek": ["web-deepseek-ia-f.jpg", ""], "^Kimi": ["web-kimi-ia-f.jpg", ""], "^Gemini 4 Argon": ["", "c3-lmarena.jpg"], "^Supabase$": ["", "p06-supabase-firebase.jpg", ""], "^Firebase \\(Google\\)": ["t03-firebase-console.jpg", ""], "^Code dans Supabase": ["p05-changement-heure.jpg"], "^n8n$": ["s13-terminal-n8n-curl.jpg", "", ""]},pk=PICK[it.match];
    function capsFor(s,i){var cs=s.captures||[];if(!pk)return cs.slice(0,1);return cs.filter(function(c){var f=typeof c==="string"?c:c.f;return pk[i]&&f.split("/").pop()===pk[i]})}
    function srcTag(st){return '<span class="f-src '+esc(st)+'">'+esc(STX[st]||st)+'</span>'}
    var ctx=String(it.plan||"").split(/\n\n+/).filter(function(p){var o=it.ouverture.toLowerCase(),w=p.toLowerCase().split(/[^a-zà-ÿ0-9]+/).filter(function(x){return x.length>3}),k=w.filter(function(x){return o.indexOf(x)>=0}).length;return p&&p.indexOf(it.ouverture.slice(0,40))<0&&(!w.length||k/w.length<.6)});
    sec("bref","Synthèse",'<p class="f-lead">'+esc(it.ouverture)+'</p>'+(ctx.length?'<details class="f-more"><summary>Contexte</summary>'+ctx.map(function(p){return '<p>'+esc(p)+'</p>'}).join("")+'</details>':''));
    if(it.demarche&&it.demarche.length)sec("methode","Méthode",'<ol class="f-steps">'+it.demarche.map(function(s){return '<li><b>'+esc(s.titre)+'</b><p>'+esc(s.texte)+'</p></li>'}).join("")+'</ol>');
    if(it.criteres&&it.criteres.length)sec("notes","Notation",'<div class="f-tw"><table class="f-tab"><thead><tr><th>Critère</th><th>Poids</th><th>Note</th><th>Source</th><th>Justification</th></tr></thead><tbody>'+it.criteres.map(function(c){var m=/^(.*?)\s*\(([^)]*)\)$/.exec(c.nom);return '<tr><th scope="row">'+esc(m?m[1]:c.nom)+'</th><td class="f-w">'+(m?esc(m[2]):'')+'</td><td>'+bar(c.note)+'</td><td>'+srcTag(c.statut)+'</td><td class="f-j">'+esc(c.pourquoi)+'</td></tr>'}).join("")+'</tbody>'+(d.s?'<tfoot><tr><th scope="row">Score</th><td></td><td colspan="3"><b>'+esc(d.s)+'</b> '+esc(d.u)+'</td></tr></tfoot>':'')+'</table></div><p class="f-note">Testé : mesuré en local. Documenté : lu dans la documentation officielle. Estimé : jugé par l’équipe.</p>');
    if(it.sections&&it.sections.length)sec("preuves","Preuves",it.sections.map(function(s,i){var cs=capsFor(s,i).map(function(c){var f=typeof c==="string"?c:c.f,l=typeof c==="string"?"":(c.legende||""),p=typeof c==="string"?"":(c.prouve||"");return '<figure><button type="button" class="f-th" title="Agrandir" data-src="'+escA(f)+'" data-l="'+escA(l)+'" data-p="'+escA(p)+'" aria-label="Agrandir : '+escA(l)+'"><img loading="lazy" src="'+escA(f)+'" alt=""></button><figcaption>'+esc(p||l)+'</figcaption></figure>'}).join("");return '<article class="f-pr'+(cs?'':' solo')+'"><div class="f-pt"><span class="f-pn">Preuve '+(i+1)+'</span><h4>'+esc(s.titre)+'</h4>'+keyFirst(s.texte)+'</div>'+(cs?'<div class="f-caps">'+cs+'</div>':'')+'</article>'}).join(""));
    var lc='';
    if(it.limites&&it.limites.length)lc+='<div><h4>Limites</h4><ul>'+it.limites.map(function(l){return '<li>'+esc(l)+'</li>'}).join("")+'</ul></div>';
    if(it.couts&&it.couts.length)lc+='<div><h4>Coûts</h4><ul>'+it.couts.map(function(l){return '<li>'+esc(l)+'</li>'}).join("")+'</ul></div>';
    if(lc)sec("limites","Limites et coûts",'<div class="f-two">'+lc+'</div>');
    if(it.jury){var L={pertinence:"Critères pertinents",rigueur:"Rigueur du benchmark",cdc:"Réponse au cahier des charges",boite_ia:"Boîte à outils IA",lucidite:"Lucidité sur les limites"};sec("jury","Grille du jury",'<table class="f-tab f-jt"><tbody>'+Object.keys(L).filter(function(k){return it.jury[k]}).map(function(k){return '<tr><th scope="row">'+L[k]+'</th><td>'+esc(it.jury[k])+'</td></tr>'}).join("")+'</tbody></table>')}
    h+='<div class="p-top"><span class="p-st">Résumé complet</span><button class="p-x" type="button" aria-label="Fermer le résumé complet">Fermer</button></div>';
    h+='<div class="f-in"><header class="f-hd"><div><p class="f-ey"><i style="background:'+col+'"></i>'+esc(it.verdict.mot)+'</p><h2 id="f-nom" tabindex="-1">'+esc(d.n)+'</h2><p class="f-v">'+esc(it.verdict.phrase)+'</p></div>'+(d.s?'<div class="f-sc"><b>'+esc(d.s)+'</b><small>'+esc(d.u)+'</small></div>':'')+'</header>';
    h+=body+'</div>';
    FULL.innerHTML=h;FULL.style.setProperty("--tc",col);FULL.scrollTop=0;fromF=btn;FULL.classList.add("on");
    FULL.querySelector(".p-x").addEventListener("click",closeFull);
    FULL.querySelectorAll(".f-th").forEach(function(t){t.addEventListener("click",function(){openLb(t)})});
    setTimeout(function(){FULL.querySelector("#f-nom").focus()},30);
  }
'''
s=s[:a]+JS+s[b:]
CSSD='''<style>
/* résumé complet : format rapport */
.f-more{margin-top:12px}
.f-more summary{display:inline-flex;align-items:center;gap:8px;cursor:pointer;list-style:none;font:500 15px/22px var(--title);color:var(--fg);border-bottom:1px solid #1F1A17;padding-bottom:1px}
.f-more summary::-webkit-details-marker{display:none}
.f-more summary:after{content:"+";font-weight:400}
.f-more[open] summary:after{content:"\2212"}
.f-more summary:focus-visible{outline:2px solid #9B85D6;outline-offset:4px}
#full .f-pt .f-key{margin:0 0 12px;font-size:17px;line-height:26px;font-weight:500;color:var(--fg)}
#full .f-det p{font-size:15px;line-height:24px;color:#4A413A}
#full .f-tab .f-j{color:#4A413A;font-size:15px;line-height:23px}
#full .f-steps p{color:#4A413A}
#full .p-top{position:sticky;top:0;z-index:3;background:var(--bg);border-bottom:1px solid #F0E3C8}
.f-in{max-width:1040px;margin:0 auto;padding:40px 32px 96px}
.f-hd{display:flex;gap:32px;align-items:flex-end;justify-content:space-between;padding-bottom:28px;border-bottom:1px solid #1F1A17}
.f-ey{display:flex;align-items:center;gap:8px;margin:0 0 10px;font:500 14px/20px var(--title);color:var(--muted)}
.f-ey i{width:10px;height:10px;border-radius:50%}
.f-in .f-hd h2{margin:0;font:600 clamp(26px,3vw,36px)/1.15 var(--title);letter-spacing:-.01em}
.f-v{margin:12px 0 0;font-size:18px;line-height:28px;color:var(--fg);max-width:62ch}
.f-sc{flex:none;text-align:right}
.f-sc b{display:block;font:600 48px/1 var(--title);letter-spacing:-.02em}
.f-sc small{font-size:14px;color:var(--muted)}
#full .f-sec{margin:0;padding:40px 0 0;border:0}
#full .f-sec>h3{margin:0 0 16px;padding:0;border:0;font:600 13px/18px var(--title);text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
#full .f-sec p{font-size:16px;line-height:26px;max-width:72ch;color:var(--fg)}
#full .f-sec .f-lead{margin-top:0;font-size:19px;line-height:30px}
.f-steps{list-style:none;counter-reset:st;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:0 32px}
.f-steps li{counter-increment:st;padding:14px 0 14px 32px;position:relative;border-top:1px solid #F0E3C8}
.f-steps li:before{content:counter(st);position:absolute;left:0;top:14px;font:600 15px/22px var(--title);color:var(--muted)}
.f-steps b{display:block;font:600 16px/22px var(--title);color:var(--fg)}
#full .f-steps p{margin:4px 0 0;font-size:15px;line-height:23px;color:var(--muted)}
.f-tw{overflow-x:auto}
#full .f-tab{width:100%;border-collapse:collapse;margin:0;font-size:15px}
#full .f-tab th,#full .f-tab td{padding:12px 12px 12px 0;border:0;border-bottom:1px solid #F0E3C8;text-align:left;vertical-align:top;line-height:22px}
#full .f-tab thead th{padding-top:0;border-bottom:1px solid #1F1A17;font:500 13px/18px var(--title);color:var(--muted);text-transform:none;letter-spacing:0}
#full .f-tab tbody th{font:600 15px/22px var(--title);color:var(--fg);width:22%}
#full .f-tab .f-w{color:var(--muted);white-space:nowrap}
#full .f-tab .f-j{color:var(--muted);font-size:14px}
#full .f-tab tfoot th,#full .f-tab tfoot td{border-bottom:0;border-top:1px solid #1F1A17;font:500 15px var(--title)}
#full .f-tab tfoot b{font-size:18px}
.f-nt{display:inline-flex;align-items:center;gap:8px;white-space:nowrap}
.f-nt b{font:600 16px var(--title);color:var(--fg)}
.f-nt small{font-size:13px;color:var(--muted);margin-left:-6px}
.f-nt i{display:inline-block;width:48px;height:4px;border-radius:2px;background:#F0E3C8;overflow:hidden}
.f-nt s{display:block;height:100%;background:#1F1A17}
.f-yn{font:600 15px var(--title);color:var(--fg)}
.f-src{display:inline-flex;align-items:center;gap:6px;font-size:14px;white-space:nowrap;color:var(--fg)}
.f-src:before{content:"";width:8px;height:8px;border-radius:50%;background:#9B85D6}
.f-src.teste:before{background:#1F1A17}.f-src.est:before{background:#FFC9A3;box-shadow:inset 0 0 0 1px #6A5F55}
#full .f-sec .f-note{margin:10px 0 0;font-size:13px;line-height:20px;color:var(--muted)}
.f-pr{display:grid;grid-template-columns:5fr 7fr;gap:32px;padding:24px 0;border-top:1px solid #F0E3C8}
.f-pr:first-of-type{border-top:0;padding-top:0}
.f-pr.solo{grid-template-columns:1fr}
.f-pn{display:block;font:500 13px/18px var(--title);color:var(--muted)}
#full .f-pt h4{margin:4px 0 8px;font:600 19px/26px var(--title);color:var(--fg);text-transform:none;letter-spacing:0}
#full .f-pt p{font-size:15px;line-height:24px}
#full .f-so{margin:12px 0;padding:0 0 0 12px;border:0;border-left:2px solid #1F1A17;background:none;color:var(--fg)}
#full .f-so.lim{border-left-color:#9B85D6}
#full .f-so b{display:block;font:600 13px/18px var(--title);color:var(--muted);text-transform:none;letter-spacing:0}
.f-caps{display:grid;gap:16px}
.f-caps figure{margin:0}
.f-th{display:block;width:100%;padding:0;border:1px solid #F0E3C8;border-radius:8px;overflow:hidden;background:#fff;cursor:zoom-in}
.f-th img{display:block;width:100%;height:auto;max-height:340px;object-fit:cover;object-position:top left}
.f-th:hover,.f-th:focus-visible{border-color:#1F1A17}
.f-caps figcaption{margin-top:6px;font-size:13px;line-height:19px;color:var(--muted)}
.f-two{display:grid;grid-template-columns:1fr 1fr;gap:32px}
#full .f-two h4{margin:0 0 6px;font:600 16px/22px var(--title);text-transform:none;letter-spacing:0;color:var(--fg)}
.f-two ul{margin:0;padding-left:18px;list-style:disc}
#full .f-two li{padding:0;border:0;background:none;display:list-item}#full .f-two li:before{content:none}
#full .f-two li{font-size:15px;line-height:23px;margin:6px 0;color:var(--fg)}
#full .f-jt tbody th{width:30%}
#full .f-jt td{color:var(--fg)}
#lb{position:fixed;inset:0;z-index:130;display:none;align-items:center;justify-content:center;padding:32px;background:rgba(31,26,23,.9)}
#lb.on{display:flex}
#lb figure{margin:0;max-width:min(1300px,100%);max-height:100%;display:flex;flex-direction:column;gap:12px}
#lb img{max-width:100%;max-height:calc(100vh - 160px);object-fit:contain;background:#fff;border-radius:8px}
#lb figcaption{color:#FFF3D9;font-size:14px;line-height:20px}
#lb figcaption b{display:block;color:#fff;font-weight:600}
#lb .p-x{position:absolute;top:16px;right:16px;background:#FFF3D9}
@media(max-width:760px){.f-in{padding:24px 16px 72px}.f-hd{flex-direction:column;align-items:flex-start}.f-sc{text-align:left}.f-pr,.f-two{grid-template-columns:1fr;gap:16px}
#full .f-tab:not(.f-jt) thead{display:none}#full .f-tab:not(.f-jt) tr{display:grid;grid-template-columns:auto auto 1fr;gap:4px 12px;padding:12px 0;border-bottom:1px solid #F0E3C8}#full .f-tab:not(.f-jt) th,#full .f-tab:not(.f-jt) td{border:0;padding:0;width:auto}#full .f-tab:not(.f-jt) tbody th{grid-column:1/-1}#full .f-tab .f-j{grid-column:1/-1}#full .f-jt th,#full .f-jt td{display:block;width:auto;border:0;padding:4px 0}#full .f-jt tr{display:block;padding:8px 0;border-bottom:1px solid #F0E3C8}}
</style>
'''
s=s.replace('</head>',CSSD+'</head>',1)
