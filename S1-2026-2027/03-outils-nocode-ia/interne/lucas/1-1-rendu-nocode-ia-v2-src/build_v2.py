import pathlib,sys
H=pathlib.Path(__file__).resolve().parent
D=H.parent.parent
s=(D/'camille/1-1-rendu-nocode-ia.html').read_text(encoding='utf-8')
def rep(a,b,n=1):
    global s
    c=s.count(a)
    if c!=n: sys.exit(f'{c} occurrences pour {a[:60]}')
    s=s.replace(a,b)
rep('"1-1-rendu-nocode-ia/captures/','"../camille/1-1-rendu-nocode-ia/captures/',s.count('"1-1-rendu-nocode-ia/captures/'))
rep('../clement/','../clement/',s.count('../clement/'))
rep('<li class="soon"><a href="#" tabindex="-1" aria-disabled="true"><b>05</b>Direction artistique<em>à venir</em></a></li>',
 '<li data-p="da"><a href="#da"><b>05</b>Direction artistique</a><ul><li><a href="#da-marque">Principes et logo</a></li><li><a href="#da-couleurs">Couleurs et lumière</a></li><li><a href="#da-typo">Typographie</a></li><li><a href="#da-interface">Interface</a></li><li><a href="#da-applications">Applications</a></li><li><a href="#da-maquette">La maquette</a></li><li><a href="#da-audit">L’audit</a></li></ul></li>')
rep('<span>La marque Soly et les maquettes de Lucas.</span></div><span class="tag soon">à venir</span>',
 '<span>La marque Soly, la maquette v4 et l’audit de la DA en 9 axes.</span></div><span class="tag ok">fait</span>')
rep('var P=["resume","stack","ia","blueprint","equipe","usage"]','var P=["resume","stack","ia","blueprint","da","equipe","usage"]')

# couleurs des graphiques et verdicts en charte Soly
for a,c in [('style="color:#1E7A46"','style="color:#1F1A17"'),('style="color:#6A4FB3"','style="color:#1F1A17"'),('style="color:#5C4636"','style="color:#6A5F55"'),('style="color:#B4530F"','style="color:#6A5F55"'),
            ('#1E7A46','#1F1A17'),('#6A4FB3','#9B85D6'),('#D9C79A','#FFD36E'),('#B4530F','#6A5F55')]:
    if a in s: s=s.replace(a,c)
PAL=[("Aube","#FFFAF0","Fond principal"),("Crème","#FFF3D9","Fond des cartes"),("Encre","#1F1A17","Texte et boutons"),("Café doux","#6A5F55","Texte secondaire"),("Soleil","#FFD36E","La lumière, jamais en texte"),("Pêche","#FFC9A3","Accent chaud"),("Lilas","#C9B8F0","Accent doux"),("Ligne","#F0E3C8","Filets et bordures")]
pal=''.join(f'<div><i style="background:{h}"></i><b>{n}</b><code>{h}</code><span>{r}</span></div>' for n,h,r in PAL)
AX=[("ok","appliqué v4","Taille du texte","14 px minimum sur l’appli, 44 px pour toucher, 20 px et plus sur le cadre."),
("ok","appliqué v4","Statut de livraison","Chaque envoi affiche « Au mur de Jeanne » : la famille sait que la photo est arrivée."),
("ok","dans le prototype","Cadre hors ligne","Aucun écran ne disait que le cadre était hors ligne. L’état est simulé dans le prototype."),
("mid","ouvert dans Figma","Qui appelle les secours, et quand ?","Jamais seul : un rappel après 24 h, la décision reste humaine."),
("mid","ouvert dans Figma","Photo envoyée en retard (écran 19)","Dire clairement quand elle s’affichera, sans culpabiliser."),
("mid","ouvert dans Figma","Qui voit « Maman t’a envoyé un Soly » (écran 25)","Préciser qui reçoit la notification dans la famille."),
("mid","ouvert dans Figma","Mosaïque ou une photo à la fois (écran 20)","Choisir l’affichage le plus lisible pour le parent."),
("soon","observation","L’alerte depuis les réglages (écran 16)","L’alerte ne s’ouvre pas depuis les réglages : ajouter l’accès."),
("soon","observation","Petit-enfant de moins de 15 ans (écran 23)","Il manque l’écran d’attente de validation par un parent.")]
ax=''.join(f'<li><span class="an">{i:02d}</span><div class="at"><b>{t}</b><span>{p}</span></div><span class="st st-{c}">{l}</span></li>' for i,(c,l,t,p) in enumerate(AX,1))
exec(open(H/'da_section.py',encoding='utf-8').read())
rep('<section class="page" id="p-equipe">',SEC+'<section class="page" id="p-equipe">')
THEME=open(H/'soly_theme.css',encoding='utf-8').read()
rep('</head>',CSS+'\n'+THEME+'\n<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600&display=swap" rel="stylesheet">\n</head>')
(D/'lucas/1-1-rendu-nocode-ia-v2.html').write_text(s,encoding='utf-8')
print('ok',len(s)//1024,'Ko')
