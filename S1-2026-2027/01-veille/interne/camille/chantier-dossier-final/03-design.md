# 03 · Design : spec de maquette du dossier final (`1-1-fiche-veille-finale.html`)

Membre : Camille · Leçon 1.1 · Rôle : UX/UI design. Spec directement codable, un seul fichier HTML autonome (< 2 Mo), CSS dans `<style>`, JS optionnel en fin de `<body>`.
Charte de départ relevée dans les rendus existants (voir § 2.0). Aucun contenu rédactionnel ici : les textes viennent des fichiers `01-…`/`02-…` du chantier.

---

## 1. Principes

1. **Style suisse** : alignement à gauche partout, aucun centrage de texte courant, pas d'ombre, pas d'arrondi, pas de dégradé ; seuls les filets (traits) structurent.
2. **Grille stricte** : 12 colonnes ; rail gauche (colonnes 1-3) pour le numéro géant de section, contenu dans les colonnes 4-12. Tout bloc démarre sur une ligne de colonne.
3. **Hiérarchie par le contraste d'échelle** : titres énormes en Archivo 800, labels en IBM Plex Mono capitales espacées, corps en Archivo 400. Trois niveaux visibles d'un coup d'œil, pas plus.
4. **Gros titres, phrases courtes** : un titre de section = une affirmation ; un chapeau = la conclusion ; le détail descend dans des `<details>`.
5. **Air** : grands blancs verticaux entre sections (≥ 96 px desktop), lignes de 60-75 caractères maximum, une couleur d'accent (bleu), le reste en encre sur crème.

---

## 2. Tokens

### 2.0 Charte relevée (valeurs exactes des rendus existants)

| Source | Tokens |
|---|---|
| `interne/clement/idee-produit-le-cadre.html` | `--cream:#f4eee1` `--paper:#faf6ec` `--ink:#111526` `--muted:#5d6172` `--blue:#1d3bc1` `--line:#d3ccba` `--orange:#e8571c` ; body `17px/1.55 Archivo` ; h1 `800 clamp(52px,10vw,120px)/.92 ls -.035em` ; h2 `800 clamp(28px,4vw,46px)/1 ls -.025em` ; eyebrow `500 13px Plex Mono ls .12em uppercase` ; `.key` filet haut 6px bleu ; section filet haut 3px encre ; main 1060px |
| `rendus/2-1-analyse-marche-questions-1-5.html` | mêmes couleurs + `--blue-soft:#dfe3f2` ; grille à rail `grid-template-columns:minmax(0,200px) minmax(0,1fr); gap:0 32px` ; `.qnum 800 clamp(56px,8vw,104px)/.85 ls -.04em bleu` ; h2 `clamp(30px,4.4vw,54px)` ; barre collante `.keybar` crème + filet bas 3px bleu ; `thead th 500 12px mono ls .1em` filet 2px encre ; `tbody` filet 1px `--line` ; `.sum` bordure gauche 6px bleu ; `details.persona summary` bouton mono bleu bordé 1.5px ; `a:focus-visible{outline:2px solid var(--blue);outline-offset:2px}` ; main 1180px |
| `rendus/1-1-fiche-veille-silvertech.html` | fond blanc (exception), `--fg:#111418` `--blue:#1f3fbf` `--orange:#e8571c` `--ok:#1d7a46` `--warn:#a86400` `--low:#8a8f96` `--hair:#d5d7d9` ; grille 12 col `gap:0 24px` (label 1/span 4, texte 5/span 8) ; chiffres clés `.kv 800 clamp(30px,3.4vw,44px) tabular-nums` ; `.axe-n` numéro géant ; `@media print` déjà esquissé |

Décision : on garde la **famille crème/encre/bleu `#1d3bc1`** (Clément + analyse marché), pas le fond blanc de la fiche 1-1. Le vert/ambre de la fiche 1-1 sont repris mais **assombris** pour passer AA sur crème (§ 2.2).

### 2.1 Couleurs (`:root`)

```css
:root{
  color-scheme: light;
  /* fonds */
  --cream:#f4eee1;      /* fond de page */
  --paper:#faf6ec;      /* fond des encadrés, cartes */
  --blue-soft:#dfe3f2;  /* fond bleu clair : chapeau, ligne survolée, onglet actif */
  /* encres */
  --ink:#111526;        /* texte, filets structurants */
  --muted:#5d6172;      /* texte secondaire, labels */
  --blue:#1d3bc1;       /* bleu identitaire : numéros, liens actifs, accents */
  --blue-deep:#14298a;  /* survol/pressé des éléments bleus */
  /* filets */
  --line:#d3ccba;       /* filet décoratif fin (séparation de lignes) */
  --rule:#8c8574;       /* bordure de composant interactif (≥ 3:1) */
  /* états (texte + fond teinté) */
  --ok:#1b6b3e;   --ok-bg:#e3eee4;    /* prouvé · fiabilité haute */
  --test:#8a5200; --test-bg:#f6e9d2;  /* à tester · fiabilité moyenne */
  --open:#5d6172; --open-bg:transparent; /* ouvert · fiabilité faible : contour pointillé */
  --risk:#a3301c; --risk-bg:#f6e1da;  /* menace, échec (usage restreint) */
  --orange:#e8571c;     /* héritage charte : JAMAIS en texte < 24px, seulement filet/puce */
}
```

### 2.2 Contrastes calculés (WCAG 2.x, formule de luminance relative)

| Paire | Ratio | Verdict |
|---|---|---|
| `--ink` / `--cream` | 15,67 | AAA |
| `--ink` / `--paper` | 16,79 | AAA |
| `--ink` / `--blue-soft` | 14,16 | AAA |
| `--muted` / `--cream` | 5,31 | AA texte normal |
| `--muted` / `--paper` | 5,69 | AA |
| `--muted` / `--blue-soft` | 4,80 | AA (limite : pas de texte < 14px sur ce fond) |
| `--blue` / `--cream` | 7,42 | AAA |
| `--blue` / `--paper` | 7,95 | AAA |
| `--blue` / `--blue-soft` | 6,70 | AA |
| `#fff` / `--blue` (bouton plein) | 8,58 | AAA |
| `--cream` / `--blue` | 7,42 | AAA |
| `--blue-deep` / `--cream` | 10,60 | AAA |
| `--ok` / `--cream` · `--ok` / `--ok-bg` | 5,64 · 5,47 | AA |
| `--test` / `--cream` · `--test` / `--test-bg` | 5,52 · 5,32 | AA |
| `--risk` / `--cream` · `--risk` / `--risk-bg` | 6,06 · 5,57 | AA |
| `--rule` / `--cream` (bordure de contrôle) | 3,17 | AA non-texte (1.4.11 ≥ 3) |
| `--line` / `--cream` | 1,38 | décoratif uniquement, jamais seul porteur d'information |
| `--orange` / `--cream` | 3,13 | non-texte ou texte ≥ 24px uniquement |
| Rejetés : `#a86400` (4,05), `#8a8f96` (2,82), `#1d7a46` sur `--blue-soft` (4,18) | | remplacés ci-dessus |

Règle RGAA 3.1 : un statut n'est **jamais** porté par la couleur seule. Chaque pastille contient un mot (« Prouvé », « À tester », « Ouvert ») et une forme (trait plein / trait plein / pointillé).

### 2.3 Typographie

Chargement (un seul `<link>`, `display=swap`) :
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">
```
```css
--sans:"Archivo","Helvetica Neue",Helvetica,Arial,system-ui,sans-serif;
--mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
```

Échelle (base 17px, ratio ≈ 1,333 ; `clamp(min, préféré, max)`) :

| Token | Valeur | Usage | Graisse | Interligne | Chasse |
|---|---|---|---|---|---|
| `--fs-mega` | `clamp(52px, 11vw, 148px)` | titre de couverture | 800 | .9 | -.04em |
| `--fs-num` | `clamp(64px, 10vw, 128px)` | numéro de section dans le rail | 800 | .85 | -.05em |
| `--fs-h2` | `clamp(32px, 4.6vw, 58px)` | titre de section | 800 | 1 | -.03em |
| `--fs-h3` | `clamp(22px, 2.4vw, 28px)` | sous-partie | 800 | 1.15 | -.015em |
| `--fs-lead` | `clamp(20px, 2.2vw, 27px)` | chapeau, phrase clé | 700 | 1.25 | -.01em |
| `--fs-kv` | `clamp(36px, 4.2vw, 56px)` | chiffre clé | 800 | 1 | -.035em, `tabular-nums` |
| `--fs-body` | `17px` (print 10.5pt) | corps | 400 | 1.55 | 0 |
| `--fs-small` | `15px` | cellules de tableau, cartes | 400 | 1.5 | 0 |
| `--fs-label` | `13px` | eyebrow, kicker, h4 de carte, en-têtes de tableau | Plex 500, `uppercase` | 1.3 | .12em |
| `--fs-note` | `12.5px` | note de source, légende, pied | Plex 400 | 1.45 | .02em |

Règles : `text-wrap:balance` sur h1/h2/h3, `text-wrap:pretty` sur chapeaux ; `max-width:68ch` sur paragraphes ; `hyphens:auto` + `lang="fr"` ; jamais de texte sous 12px à l'écran.

### 2.4 Espacements (base 4)

```css
--s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px; --s7:48px; --s8:64px; --s9:96px; --s10:144px;
--gutter:clamp(16px, 4vw, 48px);   /* marge latérale de page (16px à 360px) */
--section-gap:clamp(64px, 9vw, var(--s10));
```
Usage : intérieur de carte `--s5`, entre blocs d'une section `--s6`, entre sections `--section-gap`, filet → titre `--s4`.

### 2.5 Grille

```css
.grid{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--s5)}
.wrap{max-width:1240px;margin-inline:auto;padding-inline:var(--gutter)}
.rail{grid-column:1 / span 3}          /* numéro géant + kicker */
.body{grid-column:4 / span 9;min-width:0}
.body--narrow{grid-column:4 / span 7}  /* texte courant : 7 colonnes ≈ 68ch */
.full{grid-column:1 / -1}              /* tableaux larges, schéma */
@media (max-width:900px){ .rail{grid-column:1 / span 2} .body,.body--narrow{grid-column:3 / -1} }
@media (max-width:680px){ .grid{grid-template-columns:minmax(0,1fr)} .rail,.body,.body--narrow,.full{grid-column:1} }
```
Rail = numéros 01-05 et « A » (annexes). En mobile, le numéro passe au-dessus du titre (taille `64px`).

---

## 3. Gabarit de page

Ordre du DOM :
```
<a class="skip" href="#contenu">Aller au contenu</a>
<nav class="topnav" aria-label="Sections du dossier">…</nav>
<header class="cover" id="couverture">…</header>
<nav class="toc" aria-labelledby="toc-t" id="sommaire">…</nav>
<main id="contenu">
  <section class="sec" id="s01-methode" aria-labelledby="s01-t">…</section>
  <section class="sec" id="s02-marche">…</section>
  <section class="sec" id="s03-reglementaire">…</section>
  <section class="sec" id="s04-synthese">…</section>
  <section class="sec" id="s05-produit">…</section>   <!-- le produit et nos prévisions -->
  <section class="sec sec--annexes" id="annexes">…</section>
</main>
<footer class="foot">…</footer>
```

### 3.1 Couverture `.cover`
- `min-height:min(100svh, 980px)` ; grille 12 col ; `display:grid;align-content:space-between;padding-block:var(--s8) var(--s7)`.
- Haut : `.meta` (Plex 13px capitales, `--muted`, filet haut 2px encre) : école · PFR Générations Connectées · Phase 1 · Leçon 1.1 · date (mois année).
- Centre : `h1.cover-title` en `--fs-mega`, colonnes 1-12, `max-width:12ch`, encre ; un mot ou segment peut passer en `--blue` (`<span class="b">`), pas plus d'un.
- Sous-titre = **question centrale** : bloc `.key` (filet haut 6px `--blue`, label Plex « Question centrale » en bleu, texte `--fs-lead` 700) colonnes 4-12.
- Bas : rangée `dl.cover-facts` en 3 colonnes (Équipe · Date · Leçon), labels Plex `--muted`, valeurs Archivo 700 ; prénoms uniquement.

### 3.2 Barre de navigation fixe `.topnav`
```css
.topnav{position:sticky;top:0;z-index:20;background:var(--cream);border-bottom:3px solid var(--blue)}
.topnav ol{display:flex;gap:var(--s5);margin:0;padding:10px var(--gutter);list-style:none;overflow-x:auto;scrollbar-width:none;white-space:nowrap}
.topnav a{font:500 13px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink);text-decoration:none;padding:8px 0;display:inline-block}
.topnav a span{color:var(--blue);margin-right:6px}                /* « 01 » */
.topnav a[aria-current="true"]{color:var(--blue);box-shadow:inset 0 -3px 0 var(--blue)}
.topnav .progress{position:absolute;left:0;bottom:-3px;height:3px;width:100%;background:var(--ink);transform-origin:0 50%;transform:scaleX(var(--p,0))}
```
- Contenu : `01 Méthode · 02 Marché · 03 Règles · 04 Synthèse · 05 Produit · A Annexes` + lien « Sommaire » à gauche (`#sommaire`).
- Libellés courts (1 mot) pour tenir à 360px ; la liste défile horizontalement **dans la barre** (pas la page).
- Progression : `.progress` encre posée sur le filet bleu. CSS d'abord : `@supports (animation-timeline: scroll()){ .progress{animation:grow linear both;animation-timeline:scroll(root)} @keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}} }` ; sinon JS met à jour `--p` sur `scroll` (rAF). Sans JS ni support : barre invisible, rien ne casse. `aria-hidden="true"` sur `.progress`.
- Section active : `IntersectionObserver` (rootMargin `-40% 0px -55% 0px`) pose `aria-current="true"` sur le lien. JS facultatif.
- `html{scroll-padding-top:64px}` pour que les ancres ne passent pas sous la barre.

### 3.3 Sommaire `.toc`
- Grille : label « Sommaire » en rail (col 1-3), liste en col 4-12.
- `ol` sans puces ; chaque `li` = `a` en grille `grid-template-columns:4ch 1fr auto` : numéro Plex bleu · titre Archivo 700 `--fs-h3` · indication de longueur Plex `--muted` (ex. « ½ p. », d'après le plan).
- Filet 1px `--line` entre lignes, filet 3px encre au-dessus du bloc. Survol/focus : titre `--blue`, fond `--blue-soft`.
- Sous-entrées facultatives (niveau 2) en Plex 13px, indentées col 5.

### 3.4 Structure d'une section `.sec`
```html
<section class="sec grid" id="s02-marche" aria-labelledby="s02-t">
  <div class="rail"><span class="sec-num" aria-hidden="true">02</span><p class="kicker">Panorama du marché</p></div>
  <div class="body">
    <h2 id="s02-t"><span class="vh">02. </span>Titre-affirmation</h2>
    <p class="chapeau">Chapeau : la conclusion de la section.</p>
    … contenu (h3 + composants) …
    <p class="implique">Ce que ça implique pour nous : …</p>
  </div>
</section>
```
```css
.sec{border-top:3px solid var(--ink);padding-top:var(--s5);margin-top:var(--section-gap);scroll-margin-top:64px}
.sec-num{display:block;font:800 var(--fs-num)/.85 var(--sans);letter-spacing:-.05em;color:var(--blue);position:sticky;top:72px}
.kicker{font:500 13px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-top:var(--s3)}
.chapeau{font:700 var(--fs-lead)/1.25 var(--sans);letter-spacing:-.01em;max-width:34em;padding-left:var(--s5);border-left:6px solid var(--blue);margin-block:var(--s5) var(--s7)}
.body h3{font:800 var(--fs-h3)/1.15 var(--sans);border-top:2px solid var(--ink);padding-top:var(--s3);margin-top:var(--s8)}
.implique{background:var(--blue-soft);padding:var(--s4) var(--s5);font-weight:700;border-left:6px solid var(--blue)}
```
- Le numéro est `aria-hidden` (décoratif) ; le numéro lisible est dans le `h2` via `.vh` (visually-hidden).
- Le numéro du rail est collant (`position:sticky`) pendant la lecture de la section ; désactivé sous 680px.
- Annexes : `.sec-num` = « A », sous-parties A1…A4 en h3.

### 3.5 Pied de page `.foot`
Filet 1px `--line`, Plex 12.5px `--muted`, flex `space-between` wrap : titre court du dossier · équipe (prénoms) · « Usage de l'IA : voir annexe » (lien) · date de version · lien « Haut de page ↑ » (`#couverture`). Aucune coordonnée.

---

## 4. Composants

Conventions communes : bloc = filet haut (2px encre, ou 6px bleu pour un accent), label Plex en tête, pas d'ombre, pas de radius. Chaque composant porte `break-inside:avoid` en impression.

### 4.1 Chiffre clé `.kfs > .kf`
```html
<div class="kfs"><figure class="kf"><p class="kv">…</p><figcaption class="kt">…</figcaption><p class="src-note">Source <a href="…">[n]</a></p></figure></div>
```
- `.kfs{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(220px,100%),1fr));border-top:2px solid var(--ink)}` ; `.kf{padding:var(--s4) var(--s5) var(--s5) 0;border-bottom:1px solid var(--line)}` ; séparateur vertical 1px `--line` entre cartes (`.kf + .kf{padding-left:var(--s5);border-left:1px solid var(--line)}`, retiré en 1 colonne).
- `.kv` `--fs-kv` bleu, `font-variant-numeric:tabular-nums` ; `.kt` 15px encre ; source obligatoire (règle du brief : chaque chiffre renvoie à une source).

### 4.2 Tableau `.tbl` (acteurs, modèles économiques)
```html
<div class="tbl" role="region" aria-labelledby="cap-acteurs" tabindex="0">
  <table class="data" id="t-acteurs">
    <caption id="cap-acteurs">…</caption>
    <thead><tr><th scope="col">Acteur</th><th scope="col">Famille</th><th scope="col">Promesse</th><th scope="col">Prix</th><th scope="col">Cible</th></tr></thead>
    <tbody><tr data-famille="securite">…</tr></tbody>
  </table>
</div>
```
- `.tbl{overflow-x:auto;overscroll-behavior-x:contain;border-top:2px solid var(--ink)}` ; `table{border-collapse:collapse;width:100%;min-width:640px}` → à 360px, **seul le tableau défile**, la page jamais. `tabindex="0"` + `role="region"` pour le défilement clavier (RGAA 7.3 / WCAG 2.1.1). Ombre de bord indicatrice facultative via `background-attachment:local` (dégradés `--cream`→transparent).
- `caption` : Plex 13px capitales, `--muted`, `text-align:left`, `caption-side:top`.
- `thead th` : Plex 500 12px `.1em` uppercase `--muted`, `border-bottom:2px solid var(--ink)`, `position:sticky;top:0` dans `.tbl`.
- `tbody th[scope=row]` (nom de l'acteur) : Archivo 800 17px ; `td` 15px ; `border-bottom:1px solid var(--line)` ; `vertical-align:top` ; prix en `tabular-nums`, aligné à gauche (style suisse).
- Colonne Famille : pastille texte `.fam` (Plex 11px, bordure 1px `--rule`, pas de couleur par famille, pour ne pas concurrencer les statuts).
- **Filtre par famille** (amélioration JS) : au-dessus du tableau
  ```html
  <div class="filters" role="group" aria-label="Filtrer par famille" hidden>
    <button type="button" aria-pressed="true" data-f="all">Toutes</button>
    <button type="button" aria-pressed="false" data-f="securite">Sécurité et urgence</button>
    <button … data-f="capteurs">Capteurs de domicile</button>
    <button … data-f="sante">Santé du quotidien</button>
    <button … data-f="compagnons">Objets compagnons</button>
  </div>
  <p class="filter-status" aria-live="polite"></p>   <!-- « 6 acteurs affichés sur 18 » -->
  ```
  `hidden` retiré par le JS (sans JS : boutons absents, toutes les lignes visibles). Boutons : Plex 12px uppercase, `border:1.5px solid var(--rule)`, `min-height:44px`, `padding:0 12px` ; `[aria-pressed=true]{background:var(--blue);color:#fff;border-color:var(--blue)}`. Lignes masquées par `tr[hidden]`. Rangée de boutons `flex-wrap:wrap`.
- **Tri** : non retenu (tableau court, ordre par famille déjà signifiant). Si ajouté : `<button>` dans `th`, `aria-sort` sur le `th`.
- En impression : filtres masqués, toutes les lignes visibles (`tr[hidden]{display:table-row!important}`).

### 4.3 Carte réussite / échec `.case`
```html
<article class="case case--win"><p class="case-tag">Réussite</p><h4>Nom</h4><dl><dt>Ce qui s'est passé</dt><dd>…</dd><dt>Hypothèse d'explication</dt><dd>…</dd></dl><p class="src-note">…</p></article>
```
- Grille 2×2 (`.cases{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr));gap:var(--s5)}`).
- `.case{background:var(--paper);border-top:6px solid var(--ok);padding:var(--s5)}` ; `.case--fail{border-top-color:var(--risk)}`.
- `.case-tag` Plex 12px uppercase, couleur `--ok` / `--risk` + préfixe texte (« Réussite » / « Échec ») : jamais la couleur seule.
- `dt` Plex 12px `--muted` ; « Hypothèse » signalée par la pastille `H` (cf. 4.10).

### 4.4 Bloc réglementaire règle / source / implication `.reg`
```html
<article class="reg" id="reg-rgpd">
  <h3>RGPD et données de santé</h3>
  <div class="reg-grid">
    <div class="reg-cell"><p class="reg-l">La règle</p>…</div>
    <div class="reg-cell"><p class="reg-l">Source primaire</p><p class="src-ref">Article, texte, lien</p></div>
    <div class="reg-cell reg-cell--impl"><p class="reg-l">Pour notre produit</p>…</div>
  </div>
</article>
```
- `.reg-grid{display:grid;grid-template-columns:5fr 3fr 4fr;border-top:2px solid var(--ink)}` ; cellules `padding:var(--s4) var(--s5) var(--s5) 0`, séparateur 1px `--line` entre elles ; en < 900px : 1 colonne, filet entre cellules.
- `.reg-l` = label Plex 12px uppercase `--muted` ; `.reg-cell--impl` fond `--blue-soft`, label en `--blue`, padding gauche `--s5`.
- `.src-ref` en Plex 13px ; lien vers le texte officiel (EUR-Lex, Légifrance, CNIL…) tel que présent dans la veille.
- Trois occurrences : RGPD, frontière bien-être / dispositif médical, AI Act.

### 4.5 Encadré cas réel `.real`
- Pour le constat « capteur de glycémie / RGPD » de la partie 3.
- `<aside class="real" aria-labelledby="real-t">` ; `background:var(--paper);border:1.5px solid var(--ink);border-left-width:6px;padding:var(--s5) var(--s6)` ; label Plex « Cas réel » en `--blue`.
- Structure interne fixe : **Ce qu'on a constaté** · **Ce que dit le texte** (liste des articles) · **Non vérifié** (ligne `.unverified` : Plex 13px, préfixe « Non vérifié : », bordure gauche pointillée 2px `--open`) · **Leçon pour nous** (fond `--blue-soft`).

### 4.6 Cartes opportunité / menace `.om`
```html
<div class="om-grid">
  <article class="om om--opp" id="opp-1">
    <p class="om-tag">Opportunité 1</p><h4>…</h4><p>…</p>
    <p class="om-fact"><span>Fait de la veille</span> <a href="#fait-xx">… ↗ partie 02</a></p>
  </article>
  <article class="om om--men" id="men-1">…</article>
</div>
```
- `.om-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 var(--s6)}` : colonne gauche = 3 opportunités, droite = 3 menaces (ordre DOM : O1, O2, O3 puis M1, M2, M3 via deux `div` colonnes pour garder une lecture linéaire logique). 1 colonne sous 680px.
- `.om{border-top:2px solid var(--ink);padding-block:var(--s4) var(--s6)}` ; `.om--opp .om-tag{color:var(--ok)}` avec préfixe « + » ; `.om--men .om-tag{color:var(--risk)}` avec préfixe « − ». Texte du tag toujours présent.
- `.om-fact` : Plex 13px, fond `--paper`, `padding:var(--s2) var(--s3)` ; le lien pointe vers l'`id` du fait/tableau/chiffre cité plus haut (`id="fait-…"` posés sur les éléments sources). La cible reçoit `:target{outline:3px solid var(--blue);outline-offset:4px;background:var(--blue-soft)}`.
- Lien retour facultatif depuis la cible : `<a class="back" href="#opp-1">↩ Opportunité 1</a>` (Plex 12px).

### 4.7 Piste de positionnement `.track`
- Deux pistes côte à côte (`grid-template-columns:1fr 1fr`, 1 col en mobile).
- `.track{border-top:6px solid var(--blue);padding-top:var(--s4)}` ; numéro « Piste A / Piste B » Plex bleu ; h4 `--fs-h3` ; `dl` : Promesse · Pour qui · Premier archétype (pastille famille `.fam`) · Ce qui la rend crédible (lien vers fait) · Ce qui reste à tester (pastille statut).
- Pas de « gagnante » visuelle : les deux pistes ont le même poids (le brief demande de ne pas trancher).

### 4.8 Schéma chaîne événement → alerte `.chain` (HTML/CSS pur)
```html
<figure class="chain" aria-labelledby="chain-cap">
  <ol class="chain-steps">
    <li class="step"><p class="step-l">1 · Côté objet</p><p class="step-t">Événement simulé</p><p class="step-d">…</p></li>
    <li class="step"><p class="step-l">2 · Règle</p><p class="step-t">Seuil / délai</p><p class="step-d">…</p></li>
    <li class="step"><p class="step-l">3 · Côté parent</p><p class="step-t">Relance douce</p>…</li>
    <li class="step step--end"><p class="step-l">4 · Côté aidant</p><p class="step-t">Alerte visible et actionnable</p>…</li>
  </ol>
  <figcaption id="chain-cap">…</figcaption>
</figure>
```
- `ol` = ordre sémantique (lisible sans CSS et par lecteur d'écran).
- `.chain-steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s6);list-style:none;padding:0;counter-reset:none}`.
- `.step{border-top:2px solid var(--ink);padding-top:var(--s3);position:relative}` ; `.step--end{border-top:6px solid var(--blue)}`.
- Flèche : `.step:not(:last-child)::after{content:"→";position:absolute;right:calc(-1 * var(--s6) + 4px);top:var(--s3);font:800 24px var(--sans);color:var(--blue)}` (décorative, `content: "→" / ""` pour la masquer aux AT si supporté).
- `< 680px` : 1 colonne, flèche `↓` sous chaque étape (`::after` repositionné `position:static;display:block`).
- Étape « simulé » marquée Plex « (simulé) » : rappelle qu'aucune donnée réelle n'est produite.

### 4.9 Tableau problème → réponse → statut `.prt`
- Même composant que 4.2 (`table.data.prt`), 4 colonnes : Problème identifié (lien vers la section où il apparaît) · Réponse du produit · Statut · Prochaine étape.
- Colonne Statut : pastille `.st` :
  ```css
  .st{display:inline-flex;align-items:center;gap:6px;font:500 12px/1 var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:5px 8px;border:1.5px solid currentColor;white-space:nowrap}
  .st--proved{color:var(--ok);background:var(--ok-bg)}      /* « Prouvé » ● */
  .st--test{color:var(--test);background:var(--test-bg)}    /* « À tester » ◐ */
  .st--open{color:var(--open);border-style:dashed}          /* « Ouvert » ○ */
  ```
  Symbole en `::before` décoratif + mot obligatoire. Légende des statuts au-dessus du tableau.
- **Fiabilité** des sources : même pastille, classes `.rel--high` (vert), `.rel--mid` (ambre), `.rel--low` (pointillé gris), libellé « Fiabilité haute / moyenne / faible » + score éventuel en chiffre (repris de la veille, sur 7).

### 4.10 Pastilles F / H (fait sourcé / hypothèse) — héritées
`.b{font:500 10px var(--mono);border:1px solid;padding:0 4px;margin-left:4px}` ; `.b.f{color:var(--blue)}` `.b.h{color:var(--muted)}`, avec `title`/`abbr` « Fait sourcé » / « Hypothèse de l'équipe ». Légende une fois dans le sommaire.

### 4.11 Détails dépliables « aller plus loin »
```html
<details class="more"><summary>Aller plus loin : …</summary><div class="more-c">…</div></details>
```
- `summary` reprend la charte `details.persona` : `display:inline-flex;gap:8px;min-height:44px;align-items:center;font:500 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--blue);border:1.5px solid var(--blue);padding:0 12px;cursor:pointer;list-style:none` ; `::before{content:"+"}`, `[open]>summary::before{content:"−"}` ; hover/focus : fond bleu, texte `#fff`.
- `summary::-webkit-details-marker{display:none}`.
- `.more-c{margin-top:var(--s3);background:var(--paper);border-left:6px solid var(--blue);padding:var(--s5)}`.
- Le texte du `summary` dit ce qu'on va trouver (pas « Voir plus »).

### 4.12 Note de source `.src-note` + liens vers les rendus
- Plex 12.5px `--muted`, filet haut 1px `--line`, `margin-top:var(--s3)`.
- Appel de source dans le texte : `<sup class="refs"><a href="#ref-n">n</a></sup>` (Plex 10.5px, `--muted`, hover `--blue`) vers une bibliographie en annexe (`ol.bib`, 2 colonnes, `li:target` fond `--blue-soft`).
- Lien vers un rendu de l'équipe : `<a class="doc" href="../../rendus/…html">Titre du rendu</a>` avec suffixe Plex « ↗ rendu » ; voir § 5 pour les chemins.

### 4.13 Encadré « qui a fait quoi » `.who` (obligatoire)
- Placé en fin de section 01 (Méthode) **et** rappelé dans les annexes (même `id` unique : lien depuis la nav « A »). Recommandation : un seul encadré dans 01, lien depuis le pied.
- `<aside class="who" aria-labelledby="who-t">` ; `border:2px solid var(--ink);padding:var(--s5)` ; titre Plex « Qui a fait quoi ».
- Contenu : `table` 3 lignes (Clément, Lucas, Camille) × colonnes Rôle · Contributions · Fichiers (liens) ; + ligne « Usage de l'IA » (renvoi annexe CLAUDE.md). Prénoms seulement.

### 4.14 Emplacement réservé `.placeholder`
- Pour la carte mentale (aucun fichier trouvé dans le dépôt au 2026-10-08) : bloc `border:2px dashed var(--rule);padding:var(--s6);min-height:200px` avec label Plex « Emplacement prévu : carte mentale » et aucune image inventée.

### 4.15 Mode présentation (oral) — option simple et robuste

Retenu : **un seul interrupteur de classe**, aucun contenu masqué, aucun moteur de diapos.

- Déclencheurs : bouton `<button class="present-toggle" aria-pressed="false">Mode présentation</button>` dans `.topnav` (créé/affiché par le JS) **et** touche `P` (ignorée si `event.ctrlKey||metaKey||altKey` ou si le focus est dans `input, textarea, select, [contenteditable]`). `Échap` quitte.
- Effet (`html.present`) :
  ```css
  html.present{font-size:125%}                 /* corps ≈ 21px */
  html.present body{--fs-body:21px;--fs-small:18px}
  html.present .sec{min-height:100svh;scroll-snap-align:start;margin-top:0;padding-top:var(--s7)}
  html.present{scroll-snap-type:y proximity}   /* proximity, pas mandatory : jamais de contenu inaccessible */
  html.present details.more{display:none}      /* le détail reste dans la version lecture */
  html.present .src-note,html.present sup.refs{opacity:.6}
  ```
- Navigation pendant l'oral : `PageDown/PageUp` natifs + `→`/`←` (JS : `scrollIntoView` sur la section suivante/précédente, `behavior` selon `prefers-reduced-motion`). Le lien actif de `.topnav` sert de repère.
- État mémorisé dans `sessionStorage` (try/catch). Sans JS : le mode n'existe pas, le document reste complet.

---

## 5. Interactions

- **Ancres** : `id` stables en kebab-case préfixés par section (`s02-acteurs`, `fait-…`, `reg-rgpd`, `opp-1`, `ref-12`). `html{scroll-behavior:smooth;scroll-padding-top:64px}` uniquement sous `@media (prefers-reduced-motion: no-preference)`.
- **Lien d'évitement** `.skip` : hors écran, visible au focus (`top:8px;left:8px;background:var(--blue);color:#fff;padding:8px 12px;z-index:30`).
- **Liens vers les sources internes** (chemins relatifs depuis `interne/camille/`, emplacement du fichier final ; à recalculer s'il passe en `rendus/`) :
  | Cible | `href` |
  |---|---|
  | Fiche de veille 1-1 | `../../rendus/1-1-fiche-veille-silvertech.html` |
  | Analyse marché Q1-5 | `../../rendus/2-1-analyse-marche-questions-1-5.html` |
  | Question 1 acteurs | `../../rendus/2-1-question-1-acteurs.html` |
  | Apple Watch vs Famileo | `../../rendus/1-1-apple-watch-vs-famileo.html` |
  | Process de veille | `../../rendus/1-1-process-veille.html` |
  | Fiche automatisation (Lucas) | `../lucas/1-1-fiche-automatisation-veille.html` |
  | Réussites et faillites (Lucas) | `../lucas/1-1-reussites-faillites-silvertech.html` |
  | Synthèse axe produit (Lucas) | `../lucas/1-1-synthese-axe-produit.html` |
  | La Fenêtre (Lucas) | `../lucas/1-1-idee-produit-la-fenetre.html` |
  | Détail par segment (Lucas) | `../lucas/2-1-question-1-detail-par-segment.html` |
  | Retour pipeline (Lucas) | `../lucas/1-1-retour-pipeline-veille.html` |
  | Le Cadre (Clément) | `../clement/idee-produit-le-cadre.html` |
  | Dispositif de veille | `../commun/veille-silvertech/docs/dispositif-veille.md` |
  | CLAUDE.md équipe | `../../../../CLAUDE.md` |
  | Outillage `.claude/` | `../../../../.claude/` |

  Style : `a{color:var(--ink);text-decoration-thickness:1px;text-underline-offset:3px;text-decoration-color:var(--rule)}` ; hover : `color:var(--blue);text-decoration-color:var(--blue)`. Liens externes : suffixe « ↗ » + `<span class="vh">(site externe)</span>` ; pas de `target="_blank"` (RGAA 6, contrôle à l'utilisateur).
- **Focus visible** partout : `:focus-visible{outline:3px solid var(--blue);outline-offset:3px}` ; sur fond bleu (bouton pressé, summary survolé) : `outline-color:var(--ink)`. Jamais `outline:none` sans remplaçant.
- **Cibles tactiles** ≥ 44×44 px pour boutons, `summary`, liens de la nav.
- **JS = bonus** : tout est lisible et navigable sans JS (ancres, `<details>` natifs, tableaux complets). Le JS (≈ 3 Ko, `defer`, en fin de `body`) apporte : filtre du tableau, section active + progression, mode présentation, ouverture des `details` à l'impression. Chaque fonction protégée par une détection (`if('IntersectionObserver' in window)`).
- **Mouvement** :
  ```css
  @media (prefers-reduced-motion: reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
  ```
  Transitions autorisées sinon : `color/background-color 120ms linear` sur liens et boutons, rien d'autre.
- **Sémantique** : `lang="fr"`, un seul `h1`, hiérarchie h2 > h3 > h4 sans saut, `<title>` « Fiche de veille finale », `scope` sur tous les `th`, `caption` sur tous les tableaux, `figure/figcaption` pour chiffres et schéma.

---

## 6. Impression / PDF

```css
@page{size:A4;margin:16mm 14mm 18mm}
@page :first{margin:0}                                   /* couverture pleine page */
@media print{
  :root{--fs-body:10.5pt;--fs-small:9.5pt;--fs-num:56pt;--fs-h2:24pt;--fs-mega:54pt;--fs-lead:13pt;--fs-kv:24pt}
  html,body{background:#fff}                              /* crème non imprimé par défaut ; garder --cream si « arrière-plans » cochés */
  body{-webkit-print-color-adjust:exact;print-color-adjust:exact}  /* pastilles et fonds --blue-soft conservés */
  .topnav,.skip,.filters,.filter-status,.present-toggle,.progress,.back{display:none!important}
  .cover{min-height:auto;height:267mm;break-after:page;padding:20mm 16mm}
  .toc{break-after:page}
  .sec{break-before:page;margin-top:0}                    /* une partie = nouvelle page */
  .sec-num{position:static}
  h2,h3,h4,.chapeau{break-after:avoid}
  .kf,.case,.reg,.real,.om,.track,.step,.who,tr,figure{break-inside:avoid}
  p{orphans:3;widows:3}
  .tbl{overflow:visible;border-top-width:1pt}
  table{min-width:0;font-size:9pt}
  thead{display:table-header-group}                       /* en-tête répété sur chaque page */
  tr[hidden]{display:table-row!important}
  details.more>summary{display:none}
  details.more::details-content{content-visibility:visible;display:block}   /* Chrome 131+ */
  .more-c{border-left-width:3pt}
  a{text-decoration:none;color:inherit}
  .body a[href^="http"]::after,.body a.doc::after{content:" (" attr(href) ")";font:7.5pt var(--mono);color:var(--muted);overflow-wrap:anywhere}
  sup.refs a::after,.toc a::after,a[href^="#"]::after{content:none}   /* pas d'URL pour les ancres internes */
  .placeholder{border-color:#999}
}
```
- JS complément : `addEventListener('beforeprint',…)` ouvre tous les `details` (mémorise ceux déjà ouverts), `afterprint` restaure. Couvre Firefox/Safari où `::details-content` n'existe pas.
- Pied de page imprimé : pas de compteurs de page CSS (support inégal) ; le PDF se génère depuis Chrome « Enregistrer au format PDF », en-têtes navigateur désactivés.
- Chiffre de contrôle : la couverture tient sur 1 page, chaque partie démarre en haut de page ; cible 4 à 6 pages de corps hors annexes (contrainte du livrable).

---

## 7. Responsive (360 px sans défilement horizontal de page)

- `html,body{overflow-x:clip}` en filet de sécurité **uniquement** après vérification (il ne doit masquer aucun contenu ; le vrai remède est `min-width:0` sur tous les enfants de grille).
- Tous les enfants de grille/flex : `min-width:0` ; textes longs (URL, noms de fichiers) : `overflow-wrap:anywhere`.
- Points de rupture : **900px** (rail réduit à 2 colonnes, cartes 2→1 selon `auto-fit`, `.reg-grid` en 1 colonne) ; **680px** (grille 1 colonne, numéro au-dessus du titre, `.sec-num` non collant, `.om-grid` / `.chain-steps` / `.track` en 1 colonne, chaîne verticale).
- Marges : `--gutter` = 16px à 360px.
- Tailles min. à 360px : h1 52px (environ 7 caractères par ligne : vérifier les mots longs, `hyphens:auto`), h2 32px, numéro 64px, corps 17px.
- Tableaux : seul `.tbl` défile (cf. 4.2), indication « Faire défiler le tableau → » en Plex 12px affichée sous 680px (`.tbl-hint`).
- Nav : liste horizontale défilante dans la barre, bouton présentation masqué sous 680px.
- Test : DevTools 360×740, 390×844, 768×1024, 1280×800, 1920×1080 + zoom 200 % (WCAG 1.4.4) et 400 % / 320px (1.4.10 reflow).

---

## 8. Mode sombre

**Non.** Le document est pensé comme un imprimé crème (support écrit, PDF, oral projeté) ; une version sombre doublerait la vérification des contrastes sans bénéfice pour ce livrable, et la projection en salle est plus lisible en fond clair.
```css
:root{color-scheme:light}
```
+ `<meta name="color-scheme" content="light">` dans le `<head>`. Aucune règle `prefers-color-scheme`. `body{background:var(--cream);color:var(--ink)}` explicites, pour que les navigateurs en thème sombre ne touchent pas aux couleurs.

---

## 9. Récapitulatif des sélecteurs (aide-mémoire pour l'intégration)

`.skip` `.topnav` `.progress` `.cover` `.cover-title` `.meta` `.key` `.cover-facts` `.toc` `.sec` `.rail` `.sec-num` `.kicker` `.body` `.chapeau` `.implique` `.kfs` `.kf` `.kv` `.kt` `.tbl` `table.data` `.filters` `.filter-status` `.fam` `.cases` `.case` `.case--win` `.case--fail` `.reg` `.reg-grid` `.reg-cell--impl` `.real` `.unverified` `.om-grid` `.om--opp` `.om--men` `.om-fact` `.track` `.chain` `.chain-steps` `.step` `.step--end` `.prt` `.st--proved` `.st--test` `.st--open` `.rel--high` `.rel--mid` `.rel--low` `.b.f` `.b.h` `details.more` `.more-c` `.src-note` `sup.refs` `ol.bib` `a.doc` `.who` `.placeholder` `.present-toggle` `html.present` `.vh` `.foot`
