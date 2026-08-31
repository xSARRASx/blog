# CLAUDE.md - Mémoire de production articles SEO Sébastien

Ce fichier consigne les règles, apprentissages et historique pour accélérer la production des prochains articles. À lire EN PREMIER au démarrage de chaque session.

## 1. Contexte & identité

- **Auteur** : Sébastien More
- **Sites cibles** :
  - `locationcourteduree.fr` (LCD) — blog expert neutre, pédagogique
  - `guestlucky.com` — site SaaS produit, ton conversion assumé
- **Repo GitHub** : `xSARRASx/blog`
- **Branche active** : `claude/seo-article-production-gw6zA`

## 1bis. ROBOT BLOG v2 : publication automatique par API (depuis le 31/07/2026)

- **Interlocuteur** : Martin (auteur WordPress `martin`). Les vidéos sont celles de son père, Sébastien More, chaîne https://www.youtube.com/@moresebastien
- **Rythme chaîne : 2 vidéos/semaine** : dimanche + mercredi 18h
- **2 Routines actives** (self-bind dans la conversation Robot BLOG) :
  - Lundi 8h Paris (`trig_018Re37nCRvKAFkHiXmcCbA3`, cron `0 6 * * 1`) : article sur la vidéo du dimanche
  - Jeudi 8h Paris (`trig_01879X2BCDSn7bEjgivroJf9`, cron `0 6 * * 4`) : CONDITIONNEL, article sur la vidéo du mercredi ; si aucune nouvelle vidéo → une ligne dans la conversation, zéro dépense
- **RÈGLE TITRES** : ne JAMAIS juger une vidéo par son titre (YouTube auto-traduit les titres en anglais, ex : « €220,000: The Court Ruling... » pour une vidéo 100 % française). Seule la transcription française fait foi.
- **ANTI-DOUBLON DURCI** : verdict « déjà traitée » basé sur le RÉSULTAT FINAL = ID dans `.robot-blog/traite.json` ET article réellement existant (fichier repo + article trouvable sur le site via `wp-json/wp/v2/posts?search=<slug>`, brouillons inclus avec auth). Si référence morte → retraiter.
- **PUBLICATION API WordPress** : l'API REST de locationcourteduree.fr est ouverte, auth par mot de passe d'application (compte `martin`). Identifiants attendus en VARIABLES D'ENVIRONNEMENT : `WP_APP_USER` + `WP_APP_PASSWORD` (JAMAIS dans le repo, JAMAIS dans le chat). Si absentes → fallback livraison classique 8 blocs + mega-bloc extension Chrome.
- **PUBLICATION DIRECTE ACTIVE depuis le 31/07/2026** (accord explicite de Martin) : les articles partent en `status=publish`, plus aucun brouillon. Après publication, VÉRIFIER systématiquement : relecture en `context=edit` (HTML intact, featured_media, categories, 3 meta Yoast non vides) + chargement de l'URL publique (HTTP 200, `<title>` = titre SEO, meta description, og:image, iframe YouTube, visuels, FAQ) + santé du site (accueil + un autre article en 200).
- **REMPLACEMENT D'IMAGE À LA DEMANDE** : si Martin dit qu'une image ne lui plaît pas, régénérer avec Gemini (nouveau prompt tenant compte de sa remarque), uploader, mettre à jour `featured_media` de l'article DÉJÀ EN LIGNE, reposer alt/title/caption/description, vérifier le rendu, renvoyer le nouveau lien direct.
- **FORMAT DE LIVRAISON (Martin lit depuis son téléphone)** : commencer TOUJOURS par le **lien direct de l'image de couverture** (`source_url` du media), seul sur sa ligne, étiqueté « Image de couverture à contrôler », + une ligne décrivant le visuel généré. Puis titre/mot-clé/checklist, puis lien du brouillon wp-admin, puis valeurs Yoast posées, puis points à vérifier.
- **YOUTUBE / yt-dlp : BLOCAGE ANTI-BOT RÉSOLU (10/08/2026)**. Si `Sign in to confirm you're not a bot` : la commande qui passe est `yt-dlp --skip-download --write-auto-sub --sub-lang "fr.*" --sub-format json3 --extractor-args "youtube:player_client=android" -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=<ID>"`. DEUX éléments sont indispensables ensemble : le client `android` ET l'option de langue en regex `--sub-lang "fr.*"` (avec `--sub-langs "fr-orig,fr"` ça échoue même en android : c'est l'option de langue qui coinçait, pas le client). Si `android` tombe un jour, essayer dans l'ordre : `ios`, `mweb`, `web_safari`, `tv`. Le `--flat-playlist` du listing de chaîne passe toujours, même quand le reste est bloqué. Ne JAMAIS écrire un article sans transcription réelle.
- **YOUTUBE / erreur 429 (Too Many Requests)** : distinct du blocage anti-bot. Symptôme : `HTTP Error 429` puis `Sign in to confirm`, sur TOUTES les vidéos (même celles qui passaient une heure avant). Cause = quota temporaire sur l'IP après trop de requêtes. Remède : NE PAS insister (ça aggrave), attendre quelques heures et relancer la même commande. Test de contrôle utile : réessayer une vidéo déjà téléchargée avec succès ; si elle échoue aussi, c'est bien le quota et non la commande.
- **YOUTUBE / blocage constaté le 21/08/2026** : `android`, `ios`, `web_safari` et `tv` renvoient tous `Sign in to confirm you're not a bot`, y compris sur une vidéo déjà téléchargée avec succès quatre jours plus tôt (test de contrôle) : c'est donc bien le quota IP et pas la commande. Détail utile : le client `mweb` va plus loin, il VOIT les sous-titres FR mais refuse de les livrer faute de PO token (`Subtitles for these languages are missing: fr`). Le `--flat-playlist` du listing de chaîne et l'API oEmbed publique continuent de passer pendant le blocage. Conduite à tenir : 2-3 tentatives maximum, aucun article sans transcription, aucune entrée dans traite.json, prévenir Martin avec le vrai titre français obtenu par oEmbed, et reprogrammer une relance à quelques heures.
- **YOUTUBE / BLOCAGE RÉSOLU POUR DE BON LE 24/08/2026 : il manquait un RUNTIME JAVASCRIPT.** Le `Sign in to confirm you're not a bot` qui résistait à tous les clients (`android`, `ios`, `mweb`, `web_safari`, `tv`, `android_vr`, `tv_embedded`, `web_creator`) pendant plusieurs jours n'était PAS un quota IP : yt-dlp ne trouvait aucun runtime JS et le disait dans un WARNING discret (`No supported JavaScript runtime could be found. Only deno is enabled by default`). Node existe dans le conteneur en `/opt/node22/bin/node` mais yt-dlp ne le détecte pas tout seul. **COMMANDE QUI PASSE, à utiliser par défaut désormais :**
  `yt-dlp --js-runtimes "node:/opt/node22/bin/node" --skip-download --write-auto-sub --sub-lang "fr.*" --sub-format json3 -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=<ID>"`
  Plus besoin de forcer `player_client` : yt-dlp choisit seul. Elle produit `<ID>.fr-orig.json3` (la VO française, à privilégier), `<ID>.fr.json3` et `<ID>.fr-fr.json3`. Le WARNING sur l'impersonation est sans conséquence. Préparation faite une fois par conteneur : `pip install -U yt-dlp` (version 2026.08.19 ou plus) et `pip install bgutil-ytdlp-pot-provider` + build du générateur (`git clone --depth 1 https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git /root/bgutil-ytdlp-pot-provider && cd /root/bgutil-ytdlp-pot-provider/server && npm install && npx tsc`, avec `PATH=/opt/node22/bin:$PATH`). CONCLUSION À RETENIR : avant de conclure au quota IP, TOUJOURS relancer avec `-v` et lire les WARNING, la vraie cause peut être locale.
- **YOUTUBE / ce qui NE marche PAS ici (testé le 27/08/2026)** : `--impersonate` avec `curl_cffi` est INUTILE dans cet environnement. Le proxy sortant re-termine le TLS (voir `/root/.ccr/README.md`), donc la signature navigateur est réécrite avant d'atteindre YouTube. Sans le CA bundle, l'appel casse en `Recv failure: Connection reset by peer` ; avec le CA bundle il passe mais YouTube répond quand même `Sign in to confirm you're not a bot`. Ne pas repasser du temps dessus. **Le seul correctif durable restant = les cookies YouTube** dans une variable d'environnement `YT_COOKIES` (jamais dans le repo), puis `--cookies`. Script de restauration de l'environnement après redémarrage du conteneur : `bash .robot-blog/setup-ytdlp.sh`.
- **WORDPRESS / pare-feu 403 sur les métadonnées média (27/08/2026)** : envoyer `alt_text`, `title`, `caption` et `description` dans UN SEUL POST déclenche parfois un 403 Apache (page `Forbidden`, pas une erreur WP). Remède : les envoyer **un champ par requête**, ça passe à chaque fois. Le pare-feu limite aussi la cadence : un 403 isolé sur une lecture ou sur l'accueil est transitoire, il suffit de refaire l'appel. **ATTENTION à l'alt** : il doit contenir l'expression clé AVEC ses accents, sinon Yoast ne la reconnaît pas.
- **IMAGES : génération par API Gemini** (clé `GEMINI_API_KEY` déjà en variable d'environnement, testée OK le 31/07) : modèle `gemini-2.5-flash-image`, endpoint `generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent`, header `x-goog-api-key`, réponse inlineData base64 → `<slug>.png`. Fallback : miniature YouTube (`yt-dlp --write-thumbnail`).
- **Champs Yoast par API : RÉSOLU le 31/07/2026, désormais 100 % automatiques.** Extension `Code Snippets` (installée + activée par API) + snippet **id 5 « Robot blog - champs Yoast API »** (scope global, actif) qui fait un `register_post_meta` sur `_yoast_wpseo_focuskw`, `_yoast_wpseo_title`, `_yoast_wpseo_metadesc` (auth_callback `current_user_can('edit_posts')`). Le Robot écrit donc les 3 champs dans `meta` au POST de l'article, puis RELIT le post en `context=edit` pour confirmer. Marche arrière : désactiver le snippet 5 (interrupteur dans wp-admin → Snippets, ou API `POST /wp-json/code-snippets/v1/snippets/5` avec `{"active":false}`).
- **API : utiliser EXCLUSIVEMENT curl** pour tous les appels WordPress. Le pare-feu du site bloque le User-Agent `Python-urllib` (403 Forbidden systématique). curl passe. Testé le 31/07/2026.
- **Intégrité contenu (testé 31/07/2026)** : `<style>` et `<script>` sont préservés dans content.raw (compte admin = unfiltered_html OK). Auth testée OK (martin, administrator). Upload media + alt_text OK. Catégories dispo : Location courte durée=4, Conciergerie=88, Sous-location=62, Investissement locatif=53, Immobilier=52, Fiscalité=90.
- **Rendu** : les anciens articles sont en widget HTML Elementor ; les articles API partent en contenu classique (HTML self-contained). Vérifier le rendu du 1er brouillon dans le thème avant de généraliser (brouillon test 10355 créé le 31/07 pour validation visuelle par Martin).

## 1ter. MESSAGES VOCAUX DE MARTIN : transcription Whisper (procédure validée, 11/08/2026)

Martin envoie souvent des messages vocaux. À transcrire systématiquement avant d'y répondre.

1. **Installation** (le conteneur repart de zéro à chaque session, donc À REFAIRE à chaque fois, ~40 s) :
   `pip install --quiet faster-whisper`
2. **Transcription** :
   ```
   python3 -c "
   from faster_whisper import WhisperModel
   m = WhisperModel('small', device='cpu', compute_type='int8')
   seg, _ = m.transcribe('LE_FICHIER.opus', language='fr', vad_filter=True)
   print(' '.join(s.text for s in seg))"
   ```
- **Formats lus directement** : .opus/.ogg (vocaux WhatsApp), m4a, mp3, wav, mp4. Le décodage passe par PyAV : **ffmpeg n'est pas installé et n'est pas nécessaire**.
- **`vad_filter=True` OBLIGATOIRE** : sans lui, Whisper hallucine du texte sur les silences (typiquement « Sous-titres réalisés par la communauté d'Amara.org »).
- **Audio difficile ou jargon métier** : relancer avec `'medium'` au lieu de `'small'` (plus lent, nettement plus fidèle).
- **Noms propres et termes techniques écorchés** (GuestLucky, Beds24, noms de fonctionnalités, Lucky Cover, Meetch, Déclaloc...) : TOUJOURS relire la transcription, corriger, et **signaler à Martin ce qui a été rétabli**.
- Script tout prêt dans le repo `CARROUSSEL-` : `pipeline/transcrire_vocal.py`, usage `python3 transcrire_vocal.py vocal.ogg medium` (non disponible depuis le repo blog, mais même recette).

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
| article-liberte-financiere-conciergerie.html | LCD | liberté financière conciergerie | Stat block 3 chiffres, Opposition rouge chaos vs vert zen, Process flow horizontal 3 étapes, Stack alterné clair/sombre 5 principes, CTAs duo |
| article-pricing-dynamique-airbnb.html | LCD | pricing dynamique airbnb | Dashboard mockup KPI + bar chart, Comparatif 4 outils, Calendar heatmap 12 mois, Stat block 3 KPI accent top, Funnel 4 niveaux dégressif |
| article-trouver-clients-conciergerie.html | LCD | trouver clients conciergerie | Ranking 5 méthodes barres progressives, Box audit chiffré navy, Checklist SEO local 4 leviers icônes, Grille écosystème 6 métiers, CTAs duo |
| article-acheter-immobilier-sans-pret-bancaire.html | LCD | acheter immobilier sans prêt bancaire | Grille 6 profils vendeurs, Box exemple chiffré navy, Architecture 3 étages, Frise démembrement 21 ans, Tableau comparatif 4 solutions |
| article-commission-airbnb-2026.html | LCD | commission airbnb 2026 | Avant/Après 13 octobre, Formule mathématique box, Tableau plafonds, Comparatif micro vs réel, CTAs duo |
| article-plus-de-reservations-airbnb.html | LCD | plus de reservations airbnb | Funnel algorithme 5 étapes, Tableau 10 techniques badges impact, Comparateur tarif rouge vs vert, CTAs duo |
| article-responsabilite-conciergerie-airbnb.html | LCD | responsabilité conciergerie airbnb | Double carte sanction miroir navy/orange, Quote card verdict tribunal, Stack 2 étages sanctions, Comparatif carte G autorisé/interdit navy vs bordure orange, Checklist 6 points numérotée claire, Grille 3 briques bordure top orange, CTAs duo |
| article-assurance-airbnb-lucky-cover.html | LCD | assurance airbnb | Stat block 3 chiffres cards pleines navy/orange, Icon grid 6 garanties numérotées, Tableau récap 4 protections (th navy + ligne accent), Process flow 4 étapes flèches, CTAs duo |
| article-caution-airbnb.html | LCD | caution airbnb (REFONTE de caution-conciergerie-airbnb, slug conservé) | Visuels d'origine conservés : stat block 3 chiffres cnst, avant/après Stripe cnab, checklist, FAQ faqcn |
| article-airbnb-en-copropriete.html | LCD | airbnb en copropriété (1er article publié en brouillon par API, post 10358) | Avant/Après unanimité vs deux tiers (dashed vs navy), Stack 3 conditions numérotées (3e en navy accent), Quote card Cour de cassation, Comparatif civil navy vs commercial bordure orange, Tabs interactives investisseur/conciergerie (PREMIÈRE utilisation), CTAs duo |
| article-parler-d-argent.html | LCD (Dev perso) | parler d'argent (1er article 100% automatique publié en direct par API, post 10361) | Matrice 2x2 des 4 réactions (dégradé clair vers navy), Split iceberg ce qu'ils voient / ne voient pas (ligne de flottaison orange), Cercles concentriques 3 niveaux de confidence, Tableau 7 silences / 7 protections, CTAs duo |
| article-location-meublee-septembre-2026.html | LCD | location meublée (post 10363) | Calendrier vertical 3 jalons (pastilles dates orange/navy/gris + statut), Jauge barres avant/après plafonnement amortissement, Arbre de décision 3 questions oui/non (PREMIÈRE utilisation), Vrai/Faux 4 idées reçues badges, CTAs duo |
| article-location-saisonniere-copropriete-jugement.html | LCD | location saisonnière (post 10365) | Scoreboard verdict tribunal navy (débouté vs gagne, VS central), Grille 4 prestations 261D + jauge de bascule civil/commercial, Stack 5 boucliers icônes bouclier navy, Encart délai 2 mois orange plein, CTAs duo |
| article-basse-saison-airbnb.html | LCD | basse saison (post 10367) | Escalier de remises 3 paliers décalés (navy/gris/orange en retrait progressif), Duel de scénarios chiffrés (dashed gris vs navy plein), Switch annonce été/hiver avec tags équipements, Fiche produit bail mobilité (header navy + bandeau orange), CTAs duo |
| article-liasse-fiscale-lmnp.html | LCD | liasse fiscale (post 10369) | Arborescence de formulaires 2031 vers annexes 2033 avec badges d'ordre de remplissage (PREMIÈRE utilisation), Meuble à 3 tiroirs de documents sur fond navy, Barre segmentée des composants amortissables + durées, Balance à deux plateaux visant le résultat zéro, Mockup de formulaire 2042-C-PRO avec case surlignée orange, CTAs duo |
| article-conciergerie-rentable.html | LCD | conciergerie rentable (post 10371) | Cascade de revenus (waterfall) avec deltas orange en négatif (PREMIÈRE utilisation), Paires de barres basique vs optimisé par palier de logements avec badge x2, Cartes d'avis voyageurs avec passages surlignés orange et tag de diagnostic, Semainier 7 colonnes à tarification inversée, Boucle de fidélisation voyageur 4 étapes avec retour, CTAs duo |
| article-taxe-fonciere.html | LCD | taxe foncière (post 10373) | Plan de logement annoté avec coefficients des annexes (PREMIÈRE utilisation), Ticket de caisse des mètres carrés fantômes (PREMIÈRE utilisation), Échelle graduée des 8 catégories avec curseur et tarifs, Éclatement du correctif d'ensemble en 4 facteurs, Double sens de révision baisse/hausse en 2 colonnes, CTAs duo |
| article-menage-airbnb.html | LCD | ménage airbnb (post 10376) | Barre de journée avec créneau d'intervention 11h-16h surligné (PREMIÈRE utilisation), Grille tarifaire 3 cartes avec jauges de fourchette + bandeaux d'options, Chaîne de calcul multiplicative logements x départs x prix (PREMIÈRE utilisation), Jauges de critères pondérés vus par la conciergerie, Fil de conversation WhatsApp d'une mission (PREMIÈRE utilisation), CTAs duo |

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

### 3.7 Choix du mot-clé (conseil Camille, 27/07/2026)
- **Privilégier les mots-clés courts à fort volume** (2 mots : « caution airbnb », « assurance airbnb ») plutôt que la longue traîne à 3 mots (« caution conciergerie airbnb ») quand le contenu le permet
- **Toujours terminer un article par le pont produit** : une phrase qui présente l'option Guestlucky/Lucky Cover + un lien vers l'article dédié (call to action de fin d'article systématique)
- Lucky Cover = l'assurance voyageurs intégrée à Guestlucky, propulsée par Meetch (meetch.io) : 50 000 €/an, franchise 30 €, nuisibles 10 000 €/an, déclaration 15 j, remboursement 48 h

### 3.8 Alt image WordPress
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

6. **WORKFLOW PUBLICATION WORDPRESS - SPÉCIFICITÉS LCD (CRITIQUES)** :
   - Tous les articles LCD sont publiés via **ELEMENTOR**, jamais en Gutenberg direct
   - Le HTML doit être collé dans un **widget HTML Elementor** (icône `</>`), pas dans le widget "Mise en évidence du code"
   - Workflow : Modifier avec Elementor → recherche widget "HTML" → glisser-déposer dans zone centrale → coller HTML dans champ "Code HTML" → Publier dans Elementor → Quitter vers le tableau de bord
   - **Champ Extrait** = à remplir manuellement via "Modifier l'extrait" en sidebar droite, sinon WordPress affiche du texte parasite (interface d'admin) sur la page blog
   - **Si Sébastien utilise l'extension Claude pour Chrome** pour automatiser, lui livrer les blocs dans le format **BLOCS COPIER-COLLER ULTRA PRÉCIS** avec :
     - Mention explicite "ELEMENTOR" et "widget HTML"
     - Procédure explicite pour basculer entre onglets (WordPress / Studio d'images IA / Raw GitHub)
     - Le Raw GitHub doit être ouvert dans un onglet séparé AVANT de lancer le mega-bloc
     - Sébastien dit en dictée vocale "Raoul. Guite" pour "Raw GitHub", c'est la même chose
   - Onglets à ouvrir AVANT de lancer l'extension Claude : Studio d'images IA + WordPress wp-admin + Raw GitHub
   - L'extension Claude pour Chrome travaille mieux quand on lui livre **un BLOC à la fois** plutôt qu'un mega-prompt unique
   - **PIÈGE EXTENSION CHROME** : l'extension ne vide PAS automatiquement les champs avant de coller, ce qui crée des doublons. Toujours préciser dans le prompt : "VIDE le champ avec Cmd+A + Delete avant de coller". Particulièrement critique pour le Titre SEO Yoast qui contient des variables par défaut (Titre, Séparateur, Titre du site).
   - **Règle d'or à intégrer dans tous les mega-prompts** : Avant chaque collage dans un champ, l'extension doit (1) cliquer dans le champ, (2) Cmd+A, (3) Delete, (4) Cmd+V
   - **RÈGLE CRITIQUE : SEO AVANT PUBLICATION** : dans tous les mega-prompts, l'extension doit sauvegarder l'article en BROUILLON (pas Publier) après l'insertion HTML dans Elementor, puis faire TOUT le SEO (Yoast, image mise en avant, extrait, catégories), et SEULEMENT à la dernière étape cliquer sur PUBLIER. Ne jamais publier un article avec Yoast et l'image incomplets.
   - **RÈGLE CRITIQUE : TÉLÉCHARGEMENT IMAGE VÉRIFIÉ** : dans l'étape 1, l'extension doit (1) lancer la génération, (2) attendre l'image complète, (3) télécharger en PNG avec le nom exact du slug de l'article, (4) VÉRIFIER dans le Finder que le fichier existe dans ~/Downloads avant de continuer. Dans l'étape 5, préciser explicitement d'uploader CE fichier téléchargé (via onglet "Téléverser des fichiers" puis navigation Cmd+Shift+D vers Téléchargements), et de vérifier visuellement la vignette avant de valider. Sinon l'extension pioche parfois une image aléatoire dans la médiathèque existante.

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
