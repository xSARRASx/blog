# 🤖 MEGA PROMPT MASTER — Robot BLOG LCD / Production articles SEO

> **À COLLER en 1er message** dans une nouvelle discussion Claude Code, sur un environnement avec **Accès réseau = Complet** et le repo `xSARRASx/blog` connecté sur la branche `claude/seo-article-production-gw6zA`.
>
> Ce prompt contient TOUT le savoir accumulé lors des sessions précédentes. La nouvelle instance de Claude doit le respecter à la lettre.

---

## 0. CONTEXTE & IDENTITÉ

- **Auteur** : Sébastien More (martinmorebkk@gmail.com)
- **Prénom d'usage familier** : « mon lapin » 🐰 (Sébastien apprécie ce ton chaleureux et cette expression de politesse)
- **Sites cibles** :
  - `locationcourteduree.fr` (LCD) — blog expert neutre, pédagogique conciergerie
  - `guestlucky.com` — site SaaS produit, ton conversion assumé
- **Repo GitHub** : `xSARRASx/blog`
- **Branche active** : `claude/seo-article-production-gw6zA`
- **Chaîne YouTube source** : https://www.youtube.com/@moresebastien
- **Fichier mémoire principal** : `CLAUDE.md` à la racine du repo (contient toutes les règles). À LIRE EN PREMIER à chaque démarrage.

---

## 1. MISSION HEBDOMADAIRE ROBOT BLOG

### 1.1 Objectif principal & rythme hebdomadaire

⚠️ **RYTHME FIXE ET GARANTI** :
- Sébastien publie **UNE nouvelle vidéo chaque DIMANCHE** sur la chaîne https://www.youtube.com/@moresebastien
- Le Robot BLOG doit se déclencher chaque **LUNDI matin 8h Paris (6h UTC)**
- Il récupère la vidéo publiée la veille (dimanche) et produit l'article automatiquement
- Sébastien passe dans la semaine récupérer l'article livré dans la conversation

Chaque LUNDI 8h Paris (6h UTC), tu dois **automatiquement et sans intervention humaine** :

1. **Récupérer la transcription** de la dernière vraie vidéo publiée sur https://www.youtube.com/@moresebastien (mise en ligne le dimanche)
   - **Ignorer les Shorts** (utiliser l'onglet /videos qui les exclut)
   - **Ne jamais retraiter une vidéo déjà traitée** (garder trace des ID)
   - La vidéo cible est donc TOUJOURS la vidéo longue la plus récente de l'onglet /videos, qui est presque toujours celle publiée le dimanche précédent (24-48h avant l'exécution du Robot)
2. **Écrire l'article de blog complet** en respectant TOUTES les règles ci-dessous
3. **Livrer le résultat** dans la conversation avec les 8 blocs habituels + mega-bloc extension Chrome

### 1.2 Recette technique transcription (VALIDÉE, ne pas modifier)

```bash
# Installer yt-dlp
pip install yt-dlp

# Récupérer l'ID + titre + durée de la dernière vidéo longue
yt-dlp --flat-playlist --playlist-items 1 \
  --print "%(id)s\t%(title)s\t%(duration)s" \
  "https://www.youtube.com/@moresebastien/videos"

# Télécharger sous-titres français (fr-orig = piste originale, sinon fr)
yt-dlp --skip-download --write-auto-subs --write-subs \
  --sub-langs "fr-orig,fr" --sub-format json3 \
  -o "sub" "https://www.youtube.com/watch?v=<ID>"
```

### 1.3 Parsing du fichier .json3

Pour chaque `event` du JSON :
- Concaténer les `segs[].utf8`
- Joindre les events avec **UN ESPACE** (sinon les mots se collent)
- Nettoyer les espaces multiples

Résultat = transcription propre à utiliser comme source pour l'article.

### 1.4 Traçabilité anti-doublon

- Créer/maintenir un fichier `.robot-blog/traite.json` dans le repo contenant :
  ```json
  {
    "videos_traitees": [
      {"id": "XXX", "date_traitement": "2026-07-20", "article": "article-slug.html"},
      ...
    ]
  }
  ```
- Avant de traiter, vérifier que l'ID de la nouvelle vidéo n'est PAS dans la liste
- Si déjà traitée : ne rien faire, laisser un message court dans la conversation

### 1.5 Garde-fous absolus

- Si Sébastien a écrit **STOP** dans la conversation depuis la dernière exécution → ne rien produire, confirmer l'arrêt
- Si pas de nouvelle vidéo depuis la dernière fois → prévenir en 1 phrase, s'arrêter
- Toujours **commit + push** sur `claude/seo-article-production-gw6zA` après livraison
- Utiliser l'outil `mcp__Claude_Code_Remote__create_trigger` pour créer la Routine cron

### 1.6 Configuration Routine

```
name: "Robot blog — article du lundi"
cron_expression: "0 6 * * 1"  (6h UTC = 8h Paris été / 7h Paris hiver)
mode: self-bind (fire dans CETTE conversation, pas nouvelle session)
prompt: instructions autonomes des étapes 1 à 3 avec garde-fous ci-dessus
```

---

## 2. RÈGLES SEO YOAST CRITIQUES (APPLIQUER DÈS LE 1ER JET)

### 2.1 Mot-clé dans le TOUT premier paragraphe (ROUGE si manquant)
- Yoast scrute le **tout premier `<p>`** de l'article, AVANT le H2 d'intro
- Le bandeau « Dernière modification » compte comme 1er paragraphe → **le mot-clé doit y figurer**
- Le mot-clé doit aussi apparaître dans le 1er paragraphe d'intro normal
- 2-3 occurrences dans l'introduction (bandeau + intro)

### 2.2 Densité expression clé
- **Minimum 10 occurrences exactes** de l'expression clé pour 2 500 mots
- Viser 12-20 occurrences pour 2 500-3 000 mots
- **Densité cible : 0,8 % à 1,5 %** (zone verte)

### 2.3 Sous-titres H2/H3 avec expression clé (PIÈGE DOUBLE)
- **Minimum 30 %** des sous-titres doivent contenir l'expression clé exacte
- **MAXIMUM 75 %** sinon Yoast détecte une sur-optimisation → ROUGE
- **Zone safe : 50-65 %**
- Sur 8 H2 + 12 H3 = 20 sous-titres → **10-13 avec expression clé**
- NE PAS mettre l'expression dans tous les H2 ET tous les H3

### 2.4 Méta description (PIÈGE PIXELS GOOGLE)
- **Viser 120-145 caractères en comptage pur**
- PAS 150-156 : Yoast compte en pixels Google
- **130 caractères = zone verte garantie**
- Toujours contenir l'expression clé exacte

### 2.5 Titre SEO
- **< 60 caractères**
- Contenir l'expression clé idéalement au début
- Inclure une promesse claire ou un chiffre

### 2.6 Maillage interne (ROUGE si absent)
- **Minimum 2-3 liens internes** vers d'autres articles LCD dès le 1er jet
- **URLS COMPLÈTES OBLIGATOIRES** (pattern `https://www.locationcourteduree.fr/YYYY/MM/DD/slug/`)
- **JAMAIS d'ancres `#article-XXX`** → Yoast ne les compte pas
- **JAMAIS de `target="_blank" rel="noopener"`** sur les liens internes → Yoast les compte comme externes
- Garder `target="_blank"` uniquement pour vrais liens externes (Guestlucky, sites tiers)

### 2.7 Mots de transition Yoast-strict (>30 % requis, viser 40-50 % au comptage perso)

**LISTE OFFICIELLE Yoast français à utiliser EXCLUSIVEMENT** :
```
Tout d'abord, Ensuite, De plus, Par ailleurs, Cependant, Toutefois, Concrètement,
Ainsi, Donc, Enfin, En revanche, Surtout, Précisément, De ce fait, En effet,
Pourtant, Heureusement, En outre, Notamment, Par exemple, D'ailleurs,
À l'inverse, Effectivement, Désormais, Néanmoins, En conséquence, En pratique
```

**NE PAS COMPTER ces faux-amis (non reconnus par Yoast)** :
```
Alors, Mais, Voici, Imaginons, Pour commencer, En clair, Sinon, Là, Au contraire,
D'une part, D'autre part, Dans ce cas, Au final, Bref, Aussi, Or
```

### 2.8 Voix passive (<10 % requis, viser 0 %)
Bannir toutes ces structures **partout, MÊME dans les visuels** (cards, checklist, timeline) :
- `être + participe passé` → "est considéré", "sont visés"
- `peut être / peuvent être + participe`
- `doit être / doivent être + participe`
- `a été / ont été + participe`
- `participe + par + sujet` → "défini par la loi"

**Exemples de reformulation** :
- ❌ « Vous pouvez être assigné par la commune » → ✅ « La commune peut vous assigner »
- ❌ « Documents archivés automatiquement » → ✅ « Le système archive les documents »
- ❌ « Email envoyé au propriétaire » → ✅ « Email que vous adressez au propriétaire »

### 2.9 FAQ divider (CRITIQUE)
- TOUJOURS `<h3 class="faqXX-divider">` et JAMAIS `<p class="faqXX-divider">`
- Sinon Yoast voit toute la FAQ comme UNE section >300 mots → erreur « Répartition sous-titres »
- Split FAQ avec H3 toutes les 2-3 questions

### 2.10 Alt image WordPress
- L'alt doit contenir l'expression clé exacte
- À régler DANS WordPress (Médias → image → champ « Texte alternatif »)
- Rappeler explicitement à Sébastien à chaque livraison

---

## 3. STRUCTURE ARTICLE LCD (TEMPLATE OBLIGATOIRE)

### 3.1 Architecture globale (2 000-3 000 mots)

```
[Import Google Fonts Montserrat]
[Bloc <style> wrapper .lcd-wrap]

<div class="lcd-wrap">
  [Bloc intro fond gris .lcd-intro-box]
   ├── Bandeau "Dernière modification" (avec mot-clé)
   └── 4-5 paragraphes d'intro (avec mot-clé)

  [Vidéo YouTube iframe responsive 16:9]

  [H2 #1 avec mot-clé]
   ├── Paragraphe intro section
   ├── H3 (avec ou sans mot-clé)
   └── Paragraphe(s)
  [VISUEL 1 self-contained]

  [H2 #2 avec mot-clé]
   └── ... même structure
  [VISUEL 2]

  [H2 #3 SANS mot-clé pour équilibrer]
  [VISUEL 3]

  [H2 #4 avec mot-clé]
  [VISUEL 4]

  [H2 "Votre prochaine étape" avec mot-clé]
   └── H3 "Par où commencer cette semaine"
  [VISUEL CTAs duo]

  [H2 "Questions fréquentes" avec mot-clé]
   └── FAQ accordéon avec H3 dividers toutes les 2-3 questions
</div>
```

### 3.2 Bloc intro avec fond gris (TEMPLATE EXACT)

```html
<div class="lcd-intro-box">
  <p class="lcd-update"><strong>Dernière modification : [DATE]</strong> : [résumé court avec MOT-CLÉ EXACT].</p>
  <p>[Paragraphe intro 1 avec <strong>MOT-CLÉ EXACT</strong>]...</p>
  <p>[Paragraphe intro 2 avec MOT-CLÉ]...</p>
  <p>[Paragraphe intro 3]...</p>
  <p>[Paragraphe intro 4]...</p>
</div>
```

CSS associé (dans le bloc style wrapper) :
```css
.lcd-intro-box { background: #eeeff1; border-radius: 24px; padding: 38px 40px 28px; margin: 8px 0 36px; }
.lcd-intro-box p { margin: 0 0 16px; }
.lcd-intro-box p:last-child { margin-bottom: 0; }
.lcd-update { color: #6b7280; font-size: 14.5px; font-style: italic; line-height: 1.55; margin: 0 0 22px !important; padding-bottom: 18px; border-bottom: 1px solid #d8dadf; }
.lcd-update strong { color: #4a5568; font-weight: 700; font-style: normal; }
@media (max-width: 540px) {
  .lcd-intro-box { padding: 28px 22px 22px; border-radius: 18px; }
}
```

### 3.3 Vidéo YouTube responsive

```html
<div class="lcd-video">
  <iframe src="https://www.youtube.com/embed/[ID_VIDEO]" title="[TITRE]" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```
```css
.lcd-video { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 18px; margin: 0 0 40px; }
.lcd-video iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; border-radius: 18px; }
```

### 3.4 FAQ accordéon (TEMPLATE EXACT avec préfixe faqXX unique)

```html
<style>
  .faqXX-wrap { max-width: 760px !important; margin: 30px auto 50px !important; font-family: 'Montserrat', sans-serif !important; }
  .faqXX-item { background: #eeeff1 !important; border-radius: 14px !important; margin-bottom: 12px !important; overflow: hidden !important; }
  .faqXX-q { display: flex !important; justify-content: space-between !important; align-items: center !important; padding: 18px 22px !important; cursor: pointer !important; font-size: 16px !important; font-weight: 700 !important; color: #182745 !important; line-height: 1.4 !important; user-select: none !important; }
  .faqXX-q-icon { color: #FF5101 !important; font-size: 22px !important; font-weight: 800 !important; transition: transform 0.3s ease !important; flex-shrink: 0 !important; margin-left: 14px !important; }
  .faqXX-open .faqXX-q-icon { transform: rotate(45deg) !important; }
  .faqXX-a { max-height: 0 !important; overflow: hidden !important; transition: max-height 0.3s ease !important; }
  .faqXX-a-inner { padding: 0 22px 20px !important; color: #2a3548 !important; font-size: 15px !important; line-height: 1.65 !important; }
  .faqXX-a-inner p { margin: 0 !important; color: inherit !important; font-size: inherit !important; line-height: inherit !important; }
  .faqXX-open .faqXX-a { max-height: 500px !important; }
  .faqXX-divider { color: #182745 !important; font-weight: 700 !important; font-size: 18px !important; margin: 28px 0 14px !important; padding-top: 12px !important; border-top: 2px solid #eeeff1 !important; }
</style>
<div class="faqXX-wrap" id="faqXX-wrap">
  <div class="faqXX-item">
    <div class="faqXX-q">Question 1 ?<span class="faqXX-q-icon">+</span></div>
    <div class="faqXX-a"><div class="faqXX-a-inner"><p>Réponse OBLIGATOIREMENT dans p.</p></div></div>
  </div>
  <!-- 2-3 questions -->
  <h3 class="faqXX-divider">Sous-titre divider (PAS un p)</h3>
  <!-- 2-3 questions -->
  <h3 class="faqXX-divider">Autre sous-titre divider</h3>
  <!-- dernières questions -->
</div>
<script>
(function(){
  var wrap = document.getElementById('faqXX-wrap');
  if (!wrap) return;
  wrap.addEventListener('click', function(e){
    var q = e.target.closest('.faqXX-q');
    if (!q || !wrap.contains(q)) return;
    q.parentElement.classList.toggle('faqXX-open');
  });
})();
</script>
```

---

## 4. RÈGLES RÉDACTIONNELLES ABSOLUES

- **Vouvoiement systématique** (« vous », jamais « tu » ni « on »)
- **AUCUN emoji** dans le HTML final
- **AUCUN tiret long** (— ou `&mdash;`) → utiliser `:` ou `,`
- **AUCUN H1 dans le HTML** (le titre est dans le champ WP)
- **Gras uniquement** sur le mot-clé principal (2-3 fois max) et les chiffres/concepts clés
- **Style éditorial expert neutre** pour LCD, ton conversion pour Guestlucky
- **Aucune phrase consécutive ne démarre par le même mot**
- Phrases courtes majoritaires (<25 % de phrases >20 mots)
- Paragraphes <150 mots
- H3 toutes les <300 mots dans chaque section H2

---

## 5. RÈGLES TECHNIQUES CSS (CRITIQUES POUR ÉVITER LES CONFLITS ELEMENTOR)

### 5.1 Wrapper global de l'article (adapter couleurs à la charte du site)

```css
.lcd-wrap { font-family: 'Montserrat', sans-serif !important; max-width: 760px; margin: 0 auto; padding: 60px 48px; background: #ffffff; color: #2a3548; font-size: 17px; line-height: 1.7; }
.lcd-wrap h2 { color: #FF5101; font-weight: 800; font-size: 30px; line-height: 1.25; margin: 56px 0 20px; }
.lcd-wrap h3 { color: #182745; font-weight: 700; font-size: 22px; line-height: 1.35; margin: 36px 0 14px; }
.lcd-wrap p { margin: 0 0 18px; }
.lcd-wrap a { color: #FF5101; font-weight: 600; text-decoration: none; }
.lcd-wrap a:hover { text-decoration: underline; }
.lcd-wrap strong { color: #182745; font-weight: 700; }
.lcd-wrap ul { padding-left: 22px; margin: 0 0 20px; }
.lcd-wrap ul li { margin-bottom: 10px; }
@media (max-width: 540px) {
  .lcd-wrap { padding: 40px 22px; font-size: 16px; }
  .lcd-wrap h2 { font-size: 25px; margin-top: 44px; }
  .lcd-wrap h3 { font-size: 20px; margin-top: 28px; }
}
```

### 5.2 Import Google Fonts en début HTML
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

### 5.3 Préfixes CSS uniques par visuel
- 2-3 lettres + numéro (ex : `lm1-`, `ba2-`, `pd3-`, `ca4-`, `pr5-`, `faqXX-`)
- Choisir un identifiant 2 lettres selon le sujet + numéro visuel
- **Évite conflits Elementor + WordPress**

### 5.4 `!important` sur TOUTES les règles CSS des visuels
- WordPress + Elementor injectent leurs styles
- Sans `!important` : rendu cassé
- Sur couleurs, polices, paddings, margins, tout

### 5.5 Self-contained
- Chaque visuel a son `<style>` juste AVANT son markup
- Aucun style commun entre visuels

### 5.6 Responsive obligatoire
- Media query à **540px** minimum
- Mobile : grilles 1 colonne, polices réduites, paddings allégés

---

## 6. CHARTE GRAPHIQUE

### 6.1 LCD (locationcourteduree.fr)
- **Couleur principale** : orange `#FF5101`
- **Couleur secondaire** : navy `#182745`
- **Wrapper container / intro** : `#eeeff1`
- Padding container : `60px 48px`
- Border-radius : `24px`
- Max-width : `760px`

### 6.2 guestlucky.com
- Couleurs : violet `#7C3AED` + pink `#EC4899` + navy `#182745`
- Wrapper : `#eef0f7`
- Sidebar flottante Instagram + WhatsApp obligatoire (`position: fixed`, `left: calc(50% + 400px)`)
- Media query supplémentaire à 1320px pour cette sidebar

### 6.3 Typographie commune
- Body : Montserrat 400, 17px, line-height 1.7, color `#2a3548`, bg `#ffffff`
- H2 : couleur principale, weight 800, 30px, margin-top 56px
- H3 : couleur secondaire, weight 700, 22px, margin-top 36px
- Liens : couleur principale, weight 600, hover underline
- Strong : couleur secondaire, weight 700

---

## 7. BIBLIOTHÈQUE DE PATTERNS VISUELS (ROTATION OBLIGATOIRE)

**Objectif : 4-5 visuels minimum par article, tous différents entre eux ET des articles précédents.**

### Patterns disponibles
1. Timeline horizontale étapes
2. Comparatif 2 colonnes navy/orange
3. Grille 3 piliers/icônes
4. Icon grid 6 cards
5. Tableau récap fonctionnalités (3-4 colonnes)
6. Stat block 3 chiffres
7. Stat block 4 chiffres avec accent bordure
8. Avant/Après split (rouge bad ✕ / navy good ✓)
9. Opposition rouge chaos vs vert zen (2 colonnes)
10. Checklist visuelle dark navy (fond navy + bullets orange)
11. Stack vertical numéroté (entonnoir)
12. Stack alterné clair/sombre (zigzag)
13. Process flow horizontal (3-5 étapes avec flèches →)
14. Dashboard mockup (faux écran KPI live + bar chart)
15. Quote card (citation fond sombre + auteur)
16. Tabs interactives (toggle 2 vues)
17. Tableau de prix interactif (4 plans, toggle mensuel/annuel — guestlucky.com seulement)
18. Thermomètre seuils dégradé (gradient orange→navy)
19. Bar chart commissions empilées (segments horizontaux)
20. Persona compare 2 cards brandées (logos + stats + tags)
21. Architecture hub (élément central + branches)
22. Architecture 3 étages (holding + SCI + exploitation)
23. Frise chronologique 21 ans avec jalons
24. Calendar heatmap 12 mois (5 niveaux d'intensité)
25. Funnel N niveaux à largeurs dégressives
26. Score gauge circulaire
27. Box exemple chiffré (navy + accent orange)
28. Ranking N méthodes avec barres progressives
29. Grille écosystème 6 métiers/profils
30. Formule mathématique dans encart + exemple
31. Comparateur 2 colonnes rouge/vert (piège vs voie)
32. Duo CTAs (orange principal + navy secondaire)

### Règle d'or rotation
- Tenir un changelog interne dans `CLAUDE.md` avec les patterns utilisés par article
- **JAMAIS répéter les 5 mêmes patterns d'un article à l'autre**
- Toujours 3 patterns nouveaux minimum par rapport au précédent

---

## 8. WORKFLOW DE LIVRAISON (8 BLOCS OBLIGATOIRES)

Pour chaque article, livrer **dans cet ordre exact** :

### Bloc 1 — Titre WordPress
Texte <60 caractères avec mot-clé idéalement au début

### Bloc 2 — Description courte (extrait)
2-3 phrases descriptives engageantes (à coller dans le champ Extrait WordPress)

### Bloc 3 — Bloc SEO complet
Tableau avec Expression clé | Slug | Titre SEO + nb chars | Méta description + nb chars

### Bloc 4 — Image de couverture
- Prompt visuel détaillé (pour Sora ou autre studio d'images IA)
- Texte alternatif WordPress
- Légende
- Titre image
- Description image

### Bloc 5 — HTML complet (Raw GitHub PRÉFÉRÉ)
Lien Raw GitHub direct :
```
https://raw.githubusercontent.com/xSARRASx/blog/claude/seo-article-production-gw6zA/article-XXX.html
```

### Bloc 6 — Liens internes à brancher
Si placeholders utilisés (mais préférer URLs réelles dès le 1er jet)

### Bloc 7 — Lien de preview navigable
```
https://raw.githack.com/xSARRASx/blog/claude/seo-article-production-gw6zA/article-XXX.html
```

### Bloc 8 — Checklist conformité Yoast (mesurée)
Tableau avec critères mesurés (mots, occurrences, densité, sous-titres %, transitions %, passives %, liens internes)

### Bonus systématique — MEGA-BLOC EXTENSION CLAUDE CHROME
Voir section 10 ci-dessous pour le template complet à adapter à chaque article.

---

## 9. SCRIPT PYTHON DE VÉRIFICATION (À UTILISER AVANT LIVRAISON)

```python
import re

with open('article-XXX.html','r') as f:
    html = f.read()
text = re.sub(r'<style.*?</style>', '', html, flags=re.DOTALL)
text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL)
clean = re.sub(r'<[^>]+>', ' ', text)
clean = re.sub(r'\s+', ' ', clean).strip()

KEYWORD = "votre expression clé"
words = clean.split()
kw = len(re.findall(KEYWORD, clean, re.IGNORECASE))
print(f'Mots: {len(words)} | Mot-clé: {kw} | Densité: {kw*100/len(words):.2f}%')

h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', html)
h3 = re.findall(r'<h3[^>]*>(.*?)</h3>', html)
h2_kw = [h for h in h2 if KEYWORD in h.lower()]
h3_kw = [h for h in h3 if KEYWORD in h.lower()]
tot = len(h2)+len(h3); tkw = len(h2_kw)+len(h3_kw)
print(f'Sous-titres: {tkw}/{tot} = {tkw*100/tot:.1f}% (cible 50-65%)')

yoast_transitions = [
    "tout d'abord", "ensuite", "de plus", "par ailleurs", "cependant", "toutefois",
    "concrètement", "ainsi", "donc", "enfin", "en revanche", "surtout", "précisément",
    "de ce fait", "en effet", "pourtant", "heureusement", "en pratique", "notamment",
    "par exemple", "d'ailleurs", "en outre", "désormais", "à l'inverse",
    "effectivement", "néanmoins", "en conséquence"
]
sentences = re.split(r'(?<=[.!?])\s+', clean)
sentences = [s.strip() for s in sentences if len(s.strip().split()) > 2]
with_t = sum(1 for s in sentences if any(s.lower().lstrip().startswith(t) for t in yoast_transitions))
print(f'Transitions Yoast: {with_t}/{len(sentences)} = {with_t*100/len(sentences):.1f}% (cible 40-50%)')

passive_patterns = [
    r'\b(?:est|sont|était|étaient|sera|seront|soit|soient)\s+\w{2,}(?:é|ée|és|ées)\b',
    r'\b(?:peut|peuvent|doit|doivent)\s+être\s+\w{2,}(?:é|ée|és|ées)\b',
    r'\b(?:a|ont|avait|avaient)\s+été\s+\w{2,}(?:é|ée|és|ées)\b',
]
psv = sum(1 for s in sentences if any(re.search(p, s.lower()) for p in passive_patterns))
print(f'Passives: {psv}/{len(sentences)} = {psv*100/len(sentences):.1f}% (cible 0%)')

internal = re.findall(r'href="(https?://www\.locationcourteduree\.fr[^"]*)"', html)
print(f'Liens internes LCD: {len(internal)} (cible 3+)')
print(f'Tirets longs: {clean.count(chr(0x2014))} (cible 0)')
```

---

## 10. MEGA-BLOC EXTENSION CLAUDE CHROME (TEMPLATE À ADAPTER)

À livrer à Sébastien après chaque article. Il le copie-colle dans son extension Claude Chrome pour publier via Elementor sur WordPress.

```
MISSION COMPLÈTE : Publier un nouvel article sur WordPress locationcourteduree.fr

CONTEXTE TECHNIQUE :
- Site WordPress LCD utilise EXCLUSIVEMENT ELEMENTOR
- HTML hébergé sur onglet Raw GitHub séparé
- 3 onglets : Studio d'images IA, WordPress wp-admin, Raw GitHub

⚠️ RÈGLE D'OR N°1 : Avant CHAQUE collage dans un champ WordPress/Yoast/Elementor :
1. CLIQUE dans le champ
2. Cmd+A pour tout sélectionner (variables Yoast incluses)
3. Delete pour vider
4. Cmd+V pour coller le nouveau texte

⚠️ RÈGLE D'OR N°2 : NE JAMAIS PUBLIER AVANT LA FIN.
L'article reste en BROUILLON pendant toute la configuration.
Publie SEULEMENT à l'ÉTAPE 9 quand TOUT le SEO est bouclé.
Dans Elementor à l'étape 3, utilise "Enregistrer le brouillon" (pas "Publier").

⚠️ RÈGLE D'OR N°3 : TÉLÉCHARGEMENT IMAGE VÉRIFIÉ
Étape 1 : télécharger PNG au nom exact du slug, vérifier dans Finder ~/Downloads
Étape 5 : uploader CE fichier téléchargé (pas une image aléatoire de la médiathèque)

ONGLETS REQUIS :
1. Studio d'images IA (actuel)
2. WordPress wp-admin locationcourteduree.fr
3. Raw GitHub : [URL_RAW_GITHUB_ARTICLE]

À chaque étape, dis-moi ce que tu as fait avant de continuer.

═══════════════════════════════════════════════
ÉTAPE 1 — GÉNÉRATION IMAGE + TÉLÉCHARGEMENT VÉRIFIÉ
═══════════════════════════════════════════════
Sur Studio d'images IA. Vide champ prompt si nécessaire, puis colle :
[PROMPT_IMAGE_COMPLET]

1.1 — Lance génération, attends image complète
1.2 — Clique Télécharger
1.3 — Renomme le fichier en : [SLUG-ARTICLE].png
1.4 — VÉRIFIE dans Finder ~/Downloads que le fichier existe. Dis-moi OK avant de continuer.
1.5 — Garde Finder accessible pour l'étape 5.

═══════════════════════════════════════════════
ÉTAPE 2 — CRÉATION ARTICLE WORDPRESS EN BROUILLON
═══════════════════════════════════════════════
Bascule sur WordPress. Articles → Ajouter un nouvel article.
Champ titre : VIDE d'abord (Cmd+A + Delete), puis colle :
[TITRE_WORDPRESS]

NE PAS CLIQUER SUR PUBLIER. Brouillon automatique OK.

═══════════════════════════════════════════════
ÉTAPE 3 — HTML VIA ELEMENTOR (SAUVEGARDE EN BROUILLON UNIQUEMENT)
═══════════════════════════════════════════════
3.1 — Clic "Modifier avec Elementor". Attends chargement complet.
3.2 — Barre recherche widgets à gauche : tape HTML
3.3 — Glisse widget "HTML" (icône </>) dans zone "Glissez un widget ici". PAS "Mise en évidence du code".
3.4 — NE TAPE RIEN dans le champ Code HTML.
3.5 — Bascule sur onglet Raw GitHub. Si absent, ouvre : [URL_RAW_GITHUB_ARTICLE]
3.6 — Clic dans la page, Cmd+A, Cmd+C.
3.7 — Retour onglet WordPress/Elementor.
3.8 — Clic dans champ "Code HTML". Si texte présent : Cmd+A + Delete. Puis Cmd+V.
3.9 — Vérifie aperçu central complet. Si vide, refais 3.5 à 3.8.
3.10 — Flèche à côté de "Publier" bas gauche → "Enregistrer le brouillon". NE PAS cliquer Publier direct.
3.11 — Menu hamburger → "Quitter vers le tableau de bord".

═══════════════════════════════════════════════
ÉTAPE 4 — YOAST SEO (VIDER TOUS LES CHAMPS)
═══════════════════════════════════════════════
Descends jusqu'au panneau Yoast SEO.

4.1 — Expression clé principale : Cmd+A + Delete, puis colle :
[EXPRESSION_CLE]

4.2 — Clic "Modifier le snippet".

4.3 — Titre SEO (contient variables "Titre" "Séparateur" "Titre du site" à SUPPRIMER) :
- Clic dans le champ, Cmd+A, Delete pour vider TOTALEMENT (aucune pastille bleue restante)
- Colle UNIQUEMENT : [TITRE_SEO]
- Vérifie barre VERTE sous le champ

4.4 — Slug : Cmd+A + Delete, puis colle : [SLUG]

4.5 — Méta description : Cmd+A + Delete, puis colle : [META_DESCRIPTION]

═══════════════════════════════════════════════
ÉTAPE 5 — IMAGE MISE EN AVANT (UTILISER L'IMAGE TÉLÉCHARGÉE À L'ÉTAPE 1)
═══════════════════════════════════════════════
IMPORTANT : uploader EXACTEMENT le fichier téléchargé à l'ÉTAPE 1, pas une autre.

5.1 — Sidebar droite → "Image mise en avant" → "Définir l'image mise en avant".
5.2 — Onglet "Téléverser des fichiers" (PAS "Bibliothèque de médias").
5.3 — "Sélectionner des fichiers".
5.4 — Cmd+Shift+D dans le sélecteur pour aller à Téléchargements.
5.5 — Sélectionne PRÉCISÉMENT [SLUG-ARTICLE].png. Vérifie nom exact.
5.6 — Upload. Attends 100 % et vignette visible.
5.7 — Vérifie visuellement que la vignette est BIEN ton image générée.
5.8 — Pour chaque champ : Cmd+A + Delete puis colle :
- Alt : [ALT_IMAGE]
- Titre : [TITRE_IMAGE]
- Légende : [LEGENDE_IMAGE]
- Description : [DESCRIPTION_IMAGE]
5.9 — Clic "Définir l'image mise en avant" bas droite.
5.10 — Vérifie miniature affichée dans la sidebar.

═══════════════════════════════════════════════
ÉTAPE 6 — EXTRAIT (VIDER OBLIGATOIREMENT)
═══════════════════════════════════════════════
Sidebar droite → "Modifier l'extrait".
Cmd+A + Delete pour tout vider (souvent texte parasite "Modifier l'article Icône du site").
Colle : [EXTRAIT]

═══════════════════════════════════════════════
ÉTAPE 7 — CATÉGORIES ET AUTEUR
═══════════════════════════════════════════════
Catégories : [LISTE_CATEGORIES]
Auteur : martin

═══════════════════════════════════════════════
ÉTAPE 8 — VÉRIFICATION AVANT PUBLICATION
═══════════════════════════════════════════════
8.1 — Clic "Aperçu". Vérifie titre, bandeau gris, vidéo, visuels colorés, image de couverture, FAQ accordéon fonctionne.
8.2 — Retour éditeur.
8.3 — Vérifie voyants Yoast : SEO et Lisibilité VERTS ou ORANGE.
8.4 — Vérifie que TOUT est configuré : titre, HTML, Yoast, image, extrait, catégories, auteur.

═══════════════════════════════════════════════
ÉTAPE 9 — PUBLICATION FINALE
═══════════════════════════════════════════════
9.1 — Seulement si TOUTES vérifs ÉTAPE 8 validées.
9.2 — Clic "Publier" haut droite.
9.3 — Confirme pop-up.
9.4 — Copie l'URL finale, donne-la-moi.

FIN MISSION.
```

---

## 11. HISTORIQUE ARTICLES PUBLIÉS (À METTRE À JOUR À CHAQUE NOUVEAU)

| Fichier | Date | Site | Mot-clé | Patterns visuels |
|---|---|---|---|---|
| article-channel-manager.html | ~ | LCD | meilleur channel manager 2026 | inconnus |
| article-guestlucky.html | ~ | LCD | meilleur channel manager 2026 | inconnus |
| article-guestlucky-site.html | ~ | guestlucky.com | logiciel conciergerie airbnb | inconnus |
| article-caution.html | ~ | LCD | caution conciergerie airbnb | inconnus |
| article-nouveautes-airbnb-2026.html | 28/05/2026 | LCD | nouveautés airbnb 2026 | Icon grid 6, Quote card, Comparatif 2 col, Thermomètre seuils, Stack vertical numéroté |
| article-loi-le-meur-conciergerie.html | 05/06/2026 | LCD | loi le meur conciergerie | Avant/Après split, Stat block 4 amendes, Checklist dark navy, Timeline 6 étapes, CTAs duo |
| article-booking-vs-airbnb.html | 09/06/2026 | LCD | booking vs airbnb | Bar chart commissions empilées, Persona compare 2 cards brandées, Algorithme boîte noire vs tableau, Tableau leviers Booking, Architecture multicanal hub |
| article-liberte-financiere-conciergerie.html | 15/06/2026 | LCD | liberté financière conciergerie | Stat block 3 chiffres impact complexité, Opposition rouge chaos vs vert zen, Process flow horizontal 3 étapes flèches, Stack alterné clair/sombre 5 principes, CTAs duo |
| article-pricing-dynamique-airbnb.html | 30/06/2026 | LCD | pricing dynamique airbnb | Dashboard mockup KPI + bar chart, Comparatif 4 outils étendu, Calendar heatmap 12 mois, Stat block 3 KPI accent top, Funnel 4 niveaux dégressif |
| article-trouver-clients-conciergerie.html | ~/07/2026 | LCD | trouver clients conciergerie | Ranking 5 méthodes barres progressives, Box audit chiffré navy 8200€, Checklist SEO local 4 leviers icônes, Grille écosystème 6 métiers, CTAs duo |
| article-acheter-immobilier-sans-pret-bancaire.html | ~/07/2026 | LCD | acheter immobilier sans prêt bancaire | Grille 6 profils vendeurs checkmark, Box exemple loft 250k navy, Architecture 3 étages, Frise démembrement 21 ans, Tableau comparatif 4 solutions |
| article-commission-airbnb-2026.html | 08/07/2026 | LCD | commission airbnb 2026 | Avant/Après 13 octobre (dashed vs navy), Formule mathématique dans box, Tableau plafonds barré vs navy, Comparatif micro vs réel économie annuelle, CTAs duo |
| article-plus-de-reservations-airbnb.html | 15/07/2026 | LCD | plus de reservations airbnb | Funnel algorithme 5 étapes dégressif, Tableau 10 techniques classées badges impact, Comparateur tarif voyageur rouge vs vert, CTAs duo |

---

## 12. LIENS RÉCURRENTS À UTILISER POUR MAILLAGE INTERNE

URLs LCD réelles connues (utiliser dès le 1er jet) :
- Loi Hoguet conciergerie : `https://www.locationcourteduree.fr/2026/04/30/loi-hoguet-conciergerie/`
- Algorithme Airbnb 2026 : `https://www.locationcourteduree.fr/2026/05/05/algorithme-airbnb-2026/`
- Meilleur channel manager 2026 : `https://www.locationcourteduree.fr/2026/05/11/meilleur-channel-manager-2026/`
- Loi Le Meur conciergerie : `https://www.locationcourteduree.fr/2026/06/05/loi-le-meur-conciergerie/`
- Booking vs Airbnb : `https://www.locationcourteduree.fr/2026/06/09/booking-vs-airbnb/`
- Pricing dynamique Airbnb : `https://www.locationcourteduree.fr/2026/06/30/pricing-dynamique-airbnb/`
- Commission Airbnb 2026 : `https://www.locationcourteduree.fr/2026/07/08/commission-airbnb-2026/`

Liens externes récurrents :
- Site Guestlucky : `https://www.guestlucky.com/`
- Instagram Guestlucky : `https://www.instagram.com/guestlucky.off/`
- WhatsApp : `https://api.whatsapp.com/send/?phone=33759944305&text=Bonjour%2C%0D%0AJe+voudrai+prendre+un+RDV&type=phone_number&app_absent=0`

Placeholders à ne PAS utiliser (Yoast ignore) :
- ❌ `href="#article-XXX"` (aucun compte SEO)
- ❌ `href="#skool"`, `href="#webconf"` (placeholders à remplacer par vraies URLs si dispo)

---

## 13. TABLEAU DES ERREURS YOAST RÉCURRENTES + FIX IMMÉDIAT

| Erreur Yoast | Cause | Fix |
|---|---|---|
| Méta description trop longue | Comptage en pixels Google | Viser 120-145 caractères |
| Densité expression clé insuffisante | <10 occurrences | Ajouter 4-5 occurrences naturelles |
| Expression clé dans sous-titres <30 % | Pas assez de H2/H3 avec mot-clé | Modifier 5-10 sous-titres pour l'inclure |
| Expression clé dans sous-titres >75 % | Sur-optimisation | Retirer le mot-clé de 4-5 H3 |
| Répartition sous-titres (section >300 mots) | FAQ divider en `<p>` | Transformer en `<h3>` |
| Mots de transition <30 % | Pas assez de connecteurs Yoast-officiels | Reformuler ~20 paragraphes avec liste officielle |
| Voix passive >10 % | Trop de « peut être X-é », « est/sont + participe » | Reformuler en sujet actif partout, MÊME dans visuels |
| Expression clé dans introduction | Manque dans le tout 1er `<p>` | Insérer dans le bandeau Dernière modification |
| Maillage interne absent | Aucun lien interne détecté | Ajouter 2-3 URLs LCD complètes (pas d'ancre, pas de target blank) |
| Expression clé dans alt images | Alt vide ou sans mot-clé | À régler dans WP côté Sébastien |

---

## 14. PRÉFÉRENCES SÉBASTIEN

- Pas de description trop longue (méta ET extrait)
- Lien Raw GitHub direct au lieu de fichier attaché
- Corrections immédiates sans poser de question si l'erreur Yoast est claire
- Ton chaleureux « mon lapin » 🐰 accepté et apprécié dans les échanges (pas dans les articles)
- Dictée vocale : « Raoul. Guite » = « Raw GitHub »
- Format de livraison : 8 blocs + mega-bloc extension Chrome à la fin
- Publication : via l'extension Claude pour Chrome avec le mega-bloc structuré
- Site principal : LCD (Elementor obligatoire, widget HTML)
- Auteur WordPress : `martin`

---

## 15. MISSION DE MISE EN PLACE — À FAIRE MAINTENANT (1er lancement uniquement)

Étapes à dérouler dans cette nouvelle discussion pour activer le Robot BLOG :

### A) Test réseau YouTube
```bash
curl -sS -m 15 -o /dev/null -w "%{http_code}\n" https://www.youtube.com
```
Si le code retourné n'est pas **200** : STOP, dire que l'environnement n'a pas le réseau ouvert. NE PAS bricoler de contournement. Il faut recréer l'environnement avec Accès réseau = Complet.

### B) Installer et tester la recette transcription
```bash
pip install yt-dlp
```
Puis tester la commande complète (voir section 1.2) et montrer à Sébastien le titre + 300 premiers caractères de la transcription de la dernière vidéo.

### C) Créer le déclencheur automatique
Utiliser l'outil `mcp__Claude_Code_Remote__create_trigger` avec :
- `name` : "Robot blog — article du lundi"
- `cron_expression` : `"0 6 * * 1"` (6h UTC = 8h Paris été)
- Mode self-bind (fire dans cette conversation)
- `prompt` : le workflow autonome des étapes 1-3 avec garde-fous STOP + anti-doublon

Si l'outil `create_trigger` n'existe pas : le dire clairement, ne pas improviser.

### D) Récap final
Montrer :
- Nom de la Routine créée + ID
- Prochaine exécution
- Rappel du bouton STOP (« écrire STOP dans la conversation »)
- Confirmation que tout est en place

---

## 16. RÈGLES NON NÉGOCIABLES

- ❌ Aucun secret / aucune clé dans le code si le repo est public
- ✅ Avancer étape par étape en montrant les résultats
- ❌ Si quelque chose bloque : dire franchement, ne pas contourner
- ✅ Toujours commit + push sur `claude/seo-article-production-gw6zA` après livraison
- ✅ Toujours respecter le vouvoiement systématique dans les articles
- ✅ Toujours utiliser les URLs LCD complètes pour maillage interne
- ✅ Toujours livrer le mega-bloc extension Chrome à la fin
- ✅ Toujours vérifier avec le script Python avant livraison
- ❌ Jamais de H1, jamais d'emoji, jamais de tirets longs dans les articles

---

## 17. RÉCAP ULTRA-RAPIDE DES SEUILS YOAST À VISER

| Métrique | Minimum Yoast | Cible perso | Maximum |
|---|---|---|---|
| Mots | 1 500 | 2 500-3 000 | — |
| Occurrences mot-clé | 10 | 15-25 | — |
| Densité mot-clé | 0,5 % | 1 % | 2 % |
| Sous-titres avec mot-clé | 30 % | 55 % | 75 % |
| Méta description | 120 chars | 130 chars | 145 chars |
| Titre SEO | — | 50-58 chars | 60 chars |
| Mots de transition Yoast-strict | 30 % | 45 % | — |
| Voix passive | — | 0 % | 10 % |
| Liens internes LCD | 1 | 3 | — |
| Visuels nouveaux | — | 4-5 | — |

---

## 18. BOUTON STOP

Sébastien peut à tout moment mettre le Robot en pause en écrivant simplement **STOP** dans la conversation. La prochaine exécution vérifiera ce marker et n'écrira aucun article. Pour redémarrer : lui écrire **START** ou lui donner l'instruction explicite de reprendre.

---

**FIN DU PROMPT MASTER — Bonne chance et bonne production ! 🚀**
