# CLAUDE.md - Mémoire de production articles SEO Sébastien

Ce fichier consigne les règles, apprentissages et historique pour accélérer la production des prochains articles. À lire EN PREMIER au démarrage de chaque session.

## 1. Contexte & identité

- **Auteur** : Sébastien More
- **Sites cibles** :
  - `locationcourteduree.fr` (LCD) — blog expert neutre, pédagogique
  - `guestlucky.com` — site SaaS produit, ton conversion assumé
- **Repo GitHub** : `xSARRASx/blog`
- **Branche active** : `claude/seo-article-production-gw6zA`

## 2. Articles déjà publiés (NE PAS répéter les patterns visuels)

| Fichier | Site | Mot-clé | Patterns visuels utilisés |
|---|---|---|---|
| article-channel-manager.html | LCD | meilleur channel manager 2026 | inconnus |
| article-guestlucky.html | LCD | meilleur channel manager 2026 | inconnus |
| article-guestlucky-site.html | guestlucky.com | logiciel conciergerie airbnb | inconnus |
| article-caution.html | LCD | caution conciergerie airbnb | inconnus |
| article-nouveautes-airbnb-2026.html | LCD | nouveautés airbnb 2026 | Icon grid 6, Quote card, Comparatif 2 col, Thermomètre seuils, Stack vertical numéroté |
| article-loi-le-meur-conciergerie.html | LCD | loi le meur conciergerie | Avant/Après split, Stat block 4 amendes, Checklist dark navy, Timeline 6 étapes, CTAs duo |
| article-booking-vs-airbnb.html | LCD | booking vs airbnb | Bar chart commissions empilées, Persona compare 2 cards brandées, Algorithme boîte noire vs tableau de bord, Tableau leviers Booking, Architecture multicanal hub |

## 3. Règles SEO Yoast à appliquer DÈS LE 1ER JET (apprentissages durs)

### 3.1 Sous-titres avec expression clé (CRITIQUE - fourchette 30-75%)
- **≥30% des H2/H3** doivent contenir l'expression clé exacte
- **MAIS PAS PLUS DE 75%** sinon Yoast détecte une sur-optimisation et passe au rouge
- Sur ~8 H2 + ~20 H3 = ~29 sous-titres → viser **14-18 sous-titres avec expression clé** (50-65% zone safe)
- Privilégier le placement naturel : « Les X clés des [expression] », « Comment fonctionne [expression] », « Exploiter [expression] sans... »
- **APPRENTISSAGE** : Ne pas mettre l'expression clé dans TOUS les H2 + TOUS les H3. Garder ~30-40% des H3 sans le mot-clé, avec des reformulations contextuelles.

### 3.2 Densité expression clé
- **Minimum 10 occurrences exactes** de l'expression clé pour ~3000 mots
- Yoast affiche "L'expression clé a été trouvée X fois" — viser 12+ pour sécurité
- Densité cible : 0,8 - 1,5%

### 3.3 Méta description (CRITIQUE)
- **Viser 120-145 caractères en comptage pur** (PAS 150-156)
- Yoast compte en pixels Google : les capitales, lettres larges (m, w) et accents prennent plus de place
- 130 caractères = zone verte garantie

### 3.4 FAQ divider
- TOUJOURS utiliser `<h3 class="faqXX-divider">` et JAMAIS `<p class="faqXX-divider">`
- Sinon Yoast voit toute la FAQ comme UNE section >300 mots → erreur "Répartition sous-titres"
- Split FAQ avec H3 toutes les ~2-3 questions

### 3.5 Mots de transition (ATTENTION : Yoast est strict)
- **>30% des phrases** doivent commencer par un mot de transition
- Yoast vise environ 1 phrase sur 3
- **PIÈGE APPRENTISSAGE** : Yoast français a une liste BEAUCOUP plus restreinte que je l'imagine. Mon scanner peut trouver 50%+ alors que Yoast en trouve 25-29%. Donc viser **40-50% par mon comptage** pour assurer 30%+ chez Yoast.
- Liste à parsemer systématiquement (Yoast-compliant) : Tout d'abord, Ensuite, De plus, Par ailleurs, Cependant, Toutefois, Concrètement, Ainsi, Donc, Enfin, En revanche, Surtout, Précisément, De ce fait, En effet, Pourtant, Heureusement, Avant tout, Au final, Quant aux, En pratique, Notamment, Par exemple, D'ailleurs, En outre, Désormais, À l'inverse, Effectivement
- **Transitions NON reconnues par Yoast (à éviter de compter)** : Alors, Mais, Voici, Imaginons, Pour commencer, En clair, Sinon, Là, Au contraire, D'une part / D'autre part, Dans ce cas, Au final, Bref
- Règle d'or : sur ~180 phrases, viser **90+ phrases avec une vraie transition Yoast-officielle** (ouvertures qui démarrent par les mots de la liste ci-dessus uniquement)

### 3.6 Lisibilité
- Phrases <20 mots majoritairement (<25% de phrases longues)
- Voix passive <10% (préférer formes actives)
- Paragraphes <150 mots (visuels concaténés inclus)
- H3 toutes les <300 mots dans chaque section
- Aucune phrase consécutive ne démarre pareil
- Vouvoiement systématique

### 3.7 Alt image WordPress
- L'alt doit contenir l'expression clé exacte
- À régler DANS WordPress (Médias → image → champ "Texte alternatif")
- Pas dans le HTML, donc à rappeler explicitement à Sébastien à chaque livraison

## 4. Structure article LCD (template type)

### Bloc intro avec fond gris
```html
<div class="lcd-intro-box">
  <p class="lcd-update"><strong>Dernière modification : [DATE]</strong> : mis à jour avec [résumé court].</p>
  <p>Paragraphe intro 1 avec <strong>expression clé</strong>...</p>
  <p>Paragraphe intro 2...</p>
  <p>Paragraphe intro 3...</p>
  <p>Paragraphe intro 4...</p>
</div>
```

CSS du bloc intro :
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

### Pas de logo en tête d'article
- Le titre WordPress est mis dans le champ WP, donc PAS de bloc `lcd-logo-top` dans le HTML
- L'article démarre directement par le bloc intro avec fond gris

### Vidéo YouTube
- Iframe responsive 16:9 juste après le bloc intro
- Toujours présente sauf demande contraire

### Structure des H2/H3
1. Intro (bloc gris) + vidéo
2. H2 #1 avec expression clé + 3 H3 (dont 1 avec expression clé) + Visuel 1
3. H2 #2 avec expression clé + 2-3 H3 + Visuel 2
4. H2 #3 avec expression clé + 3 H3 (dont 1 avec expression clé) + Visuel 3
5. H2 #4 avec expression clé + 3 H3 (dont 1 avec expression clé) + Visuel 4
6. H2 #5 (peut être sans expression clé) + 3 H3 + Visuel 5
7. H2 #6 avec expression clé + 1-2 H3 + Visuel optionnel
8. H2 "Votre prochaine étape" + H3 avec expression clé + CTAs
9. H2 "Questions fréquentes" + H3 avec expression clé + FAQ accordéon

### FAQ accordéon (template critique)
```html
<style>
  .faqXX-wrap { max-width: 760px; margin: 30px auto 50px; font-family: 'Montserrat', sans-serif !important; }
  .faqXX-item { background: #eeeff1 !important; border-radius: 14px !important; margin-bottom: 12px !important; overflow: hidden !important; }
  .faqXX-q { /* ... */ }
  .faqXX-a { max-height: 0 !important; overflow: hidden !important; transition: max-height 0.3s ease !important; }
  .faqXX-a-inner { padding: 0 22px 20px !important; color: #2a3548 !important; font-size: 15px !important; line-height: 1.65 !important; }
  .faqXX-a-inner p { margin: 0 !important; color: inherit !important; font-size: inherit !important; line-height: inherit !important; }
  .faqXX-open .faqXX-a { max-height: 400px !important; }
  .faqXX-divider { color: #182745 !important; font-weight: 700 !important; font-size: 18px !important; margin: 28px 0 14px !important; padding-top: 12px !important; border-top: 2px solid #eeeff1 !important; }
</style>
<div class="faqXX-wrap" id="faqXX-wrap">
  <div class="faqXX-item">
    <div class="faqXX-q">Question 1 ?<span class="faqXX-q-icon">+</span></div>
    <div class="faqXX-a"><div class="faqXX-a-inner"><p>Réponse wrappée dans p OBLIGATOIRE.</p></div></div>
  </div>
  <!-- ... -->
  <h3 class="faqXX-divider">Sous-titre divider (PAS un p)</h3>
  <!-- 3-4 questions suivantes -->
</div>
<script>
(function(){
  var wrap = document.getElementById('faqXX-wrap');
  if (!wrap) return;
  wrap.addEventListener('click', function(e){
    var q = e.target.closest('.faqXX-q');
    if (!q || !wrap.contains(q)) return;
    var item = q.parentElement;
    item.classList.toggle('faqXX-open');
  });
})();
</script>
```

## 5. Chartes graphiques

### LCD (locationcourteduree.fr)
- Couleurs : orange `#FF5101` + navy `#182745`
- Wrapper container : `#eeeff1`
- Padding container : `60px 48px`
- Border-radius : `24px`
- Max-width : `760px`

### guestlucky.com
- Couleurs : violet `#7C3AED` + pink `#EC4899` + navy `#182745`
- Wrapper container : `#eef0f7`
- Sidebar flottante Instagram + WhatsApp obligatoire (`position: fixed`, `left: calc(50% + 400px)`)
- Tableau de prix interactif (4 plans, toggle mensuel/annuel, compteur logements)

### Typographie commune
- Body : Montserrat 400, 17px, line-height 1.7, color `#2a3548`, bg `#ffffff`
- H2 : couleur principale du site, weight 800, 30px, margin-top 56px
- H3 : navy `#182745`, weight 700, 22px, margin-top 36px
- Liens : couleur principale, weight 600, hover underline
- Strong : navy `#182745`, weight 700

## 6. Règles absolues à ne JAMAIS oublier

- **JAMAIS de H1 dans le HTML** (titre dans le champ WP)
- **HTML envoyé en UN SEUL BLOC** dans le chat
- **PAS d'emoji**, **PAS de tirets longs** (— ou `&mdash;`), **vouvoiement** systématique
- **Préfixes CSS uniques** par visuel (cm1-, gt1-, nv1-, etc.) pour éviter conflits Elementor
- `!important` sur toutes les règles CSS des visuels
- **Self-contained** : chaque visuel a son propre `<style>` juste avant le markup
- **Responsive** avec media queries à 540px (et 1320px pour guestlucky.com sidebar)
- Police Google Fonts Montserrat 400-800
- **Mot-clé dans le TOUT 1er paragraphe (bandeau lcd-update INCLUS)** : Yoast scrute ce 1er `<p>`, donc l'expression clé doit y figurer
- **2-3 liens internes vers articles LCD existants** dès le 1er jet, sinon Yoast SEO rouge "Maillage interne"
- **Liens internes : URL LCD COMPLÈTE obligatoire** (jamais d'ancre `#article-XXX` qui n'est pas comptée par Yoast). Utiliser le pattern `https://www.locationcourteduree.fr/YYYY/MM/DD/slug/`
- **Liens internes SANS `target="_blank" rel="noopener"`** : ces attributs font passer le lien en EXTERNE pour Yoast → erreur Maillage rouge. Garder `target="_blank"` uniquement pour les vrais liens externes (Guestlucky, sites tiers)
- **Phrases en voix active uniquement** : bannir « peut être X-é », « est/sont + participe », « X envoyé par Y » même dans les visuels (cards, checklist, timeline)
- **Sous-titres avec mot-clé : viser 50-65%**, jamais >75% (sur-optimisation détectée par Yoast)
- **Mots de transition Yoast-strict** : viser 40-50% au comptage perso pour assurer 30%+ chez Yoast

## 7. Bibliothèque de patterns visuels (ROTATION OBLIGATOIRE)

À piocher en évitant ceux déjà utilisés dans les articles précédents :

- ✅ Timeline horizontale étapes
- ✅ Comparatif 2 colonnes navy/orange
- ✅ Grille 3 piliers/icônes
- ✅ Tableau récap fonctionnalités
- ✅ Stat block 3 chiffres
- ✅ Avant/Après split (rouge bad / navy good ✕✓)
- ✅ Checklist visuelle dark (fond navy + bullets orange)
- ✅ Stack vertical entonnoir (tiers alternés clair/sombre)
- ✅ Process flow horizontal
- ✅ Dashboard mockup
- ✅ Quote card
- ✅ Icon grid
- ✅ Tabs
- ✅ Tableau de prix interactif (guestlucky.com seulement)
- ✅ Thermomètre seuils dégradé orange→navy

**Cible : 4-5 visuels minimum par article, tous différents et nouveaux par rapport aux articles précédents.**

## 8. Workflow de livraison (préférences Sébastien)

1. Sébastien envoie : sujet + transcription YouTube + lien vidéo + site cible
2. Je pose 2-4 questions clarification via `AskUserQuestion` (mot-clé, angle, persona) si flou
3. Je livre TOUT en un seul message avec les 8 blocs :
   1. Titre WordPress
   2. Description courte (extrait sous l'image)
   3. Bloc SEO complet
   4. Image de couverture (prompt + alt + légende + titre + description)
   5. HTML complet en un bloc (mais surtout : LIEN RAW GITHUB préféré par Sébastien)
   6. Liens internes à brancher
   7. Lien de preview raw.githack
   8. Checklist conformité

4. **Préférence Sébastien** : envoyer le **lien Raw GitHub direct** au lieu d'un fichier attaché :
   ```
   https://raw.githubusercontent.com/xSARRASx/blog/claude/seo-article-production-gw6zA/article-XXX.html
   ```

5. Commit + push systématique sur `claude/seo-article-production-gw6zA` à chaque livraison/correction

6. Si Yoast affiche des erreurs après publication → correction immédiate du HTML + nouveau push

## 9. Erreurs Yoast récurrentes et leurs fixes

| Erreur Yoast | Cause | Fix |
|---|---|---|
| Méta description trop longue | Comptage en pixels | Viser 120-145 caractères |
| Densité expression clé insuffisante | <10 occurrences | Ajouter 4-5 occurrences naturelles |
| Expression clé dans sous-titres | <30% des H2/H3 | Modifier 5-10 sous-titres pour inclure l'expression |
| Répartition sous-titres (1 section >300 mots) | FAQ divider en `<p>` | Transformer en `<h3>` |
| Mots de transition <30% | Pas assez de connecteurs | Reformuler ~20 paragraphes |
| Expression clé dans alt images | Alt vide ou sans mot-clé | À régler dans WP côté Sébastien |

## 10. Liens récurrents

- Article loi Hoguet : https://www.locationcourteduree.fr/2026/04/30/loi-hoguet-conciergerie/
- Instagram Guestlucky : https://www.instagram.com/guestlucky.off/
- Site Guestlucky : https://www.guestlucky.com/
- WhatsApp : https://api.whatsapp.com/send/?phone=33759944305&text=Bonjour%2C%0D%0AJe+voudrai+prendre+un+RDV&type=phone_number&app_absent=0
- Logo LCD (NE PAS METTRE dans le HTML) : https://www.locationcourteduree.fr/wp-content/uploads/2026/05/Design-sans-titre-45-e1778479629240.png

Placeholders à brancher article par article :
- Communauté Skool : `href="#skool"` → à remplacer par URL réelle
- Web conférence : `href="#webconf"` → à remplacer par URL réelle
- Autres articles LCD : `href="#article-XXX"` → à remplacer par URL réelle

## 11. Préférences communication Sébastien

- Pas de description trop longue (méta description ET extrait)
- Lien Raw GitHub direct au lieu de fichier attaché
- Corrections immédiates sans poser de question si l'erreur Yoast est claire
- Garder TOUS les apprentissages session après session
