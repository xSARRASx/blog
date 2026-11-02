# Routines du Robot BLOG (texte à recréer sur le Mac)

Les deux tâches programmées de la conversation cloud ont été **mises en pause le 02/11/2026** (pas supprimées) :

| Tâche | ID cloud | Cron (UTC) | Heure Paris |
|---|---|---|---|
| Robot blog : article du lundi | `trig_018Re37nCRvKAFkHiXmcCbA3` | `0 6 * * 1` | lundi 7h-8h |
| Robot blog : article du jeudi (conditionnel) | `trig_01879X2BCDSn7bEjgivroJf9` | `0 6 * * 4` | jeudi 7h-8h |

Sur le Mac, une tâche programmée ne se lance que si le Mac est allumé et Claude ouvert. Ne les recréer qu'APRÈS un premier article publié avec succès depuis le Mac.

Ci-dessous : le texte des deux tâches en version v6, c'est-à-dire la v5 du cloud corrigée de ce qui a changé depuis (bonne branche, commande yt-dlp actuelle, secours Gemini, chemins Mac). À coller tel quel comme message de chaque tâche.

---

## Tâche du LUNDI (vidéo du dimanche)

```
ROBOT BLOG LUNDI (v6, Mac, PUBLICATION DIRECTE EN LIGNE) : vidéo du dimanche. Dépôt ~/blog (xSARRASx/blog), branche claude/robot-blog-lundi-4cya0g. Lis d'abord REPRISE.md et CLAUDE.md (sections 1bis, 1ter, 1quater, 3 à 9). Autonomie totale, aucune question, messages courts.

0) GARDE-FOU STOP : si Martin a écrit STOP depuis la dernière exécution (sans START après), ne produis RIEN, confirme l'arrêt en 1 phrase.

1) VIDÉO CIBLE : cd ~/blog && git pull origin claude/robot-blog-lundi-4cya0g, puis
   yt-dlp --flat-playlist --playlist-items 1-3 --print "%(id)s\t%(title)s\t%(duration)s" "https://www.youtube.com/@moresebastien/videos"
   Ne JAMAIS juger une vidéo par son titre (YouTube traduit en anglais) : seule la transcription française fait foi. Vrai titre français : curl -sSL "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<ID>&format=json".

2) ANTI-DOUBLON : vidéo déjà traitée si (a) ID dans .robot-blog/traite.json ET (b) article réellement existant, vérifié par
   curl -sS -u "$WP_APP_USER:$WP_APP_PASSWORD" "https://www.locationcourteduree.fr/wp-json/wp/v2/posts?slug=<slug>&status=draft,pending,future,publish&_fields=id,slug,status"
   Utiliser ?slug= et non ?search=. Référence morte : retraiter. Rien de nouveau : une ligne, stop. Une vidéo plus ancienne absente de traite.json passe en priorité.

2bis) GARDE-FOU CONTENU : lister les articles récents (auth, tous statuts) ; si un article traite déjà le même sujet ou un slug proche, ne rien créer, le dire en une ligne, stop.

3) TRANSCRIPTION (jamais d'article sans transcription réelle) :
   a) yt-dlp --js-runtimes "node:$(which node)" --skip-download --write-auto-sub --sub-lang "fr.*" --sub-format json3 -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=<ID>"
      Privilégier <ID>.fr-orig.json3 ; concaténer segs[].utf8. En cas d'échec, relancer UNE fois avec -v et lire les WARNING.
   b) Si bloqué (Sign in to confirm, 429, pas de sous-titres) : TOUT DE SUITE python3 .robot-blog/transcrire-gemini.py <ID> <ID>.txt (basse résolution, environ 0,12 euro). Relire les chiffres clés.
   c) Si Gemini échoue aussi (402 = crédits épuisés) : prévenir Martin avec le vrai titre français, ne rien mettre dans traite.json, proposer une relance.

4) ARTICLE LCD : mot-clé court à fort volume, sans cannibaliser ceux de la section 2 de CLAUDE.md. 2500-3000 mots, wrapper lcd-wrap obligatoire (grep -c 'class="lcd-wrap"' = 1), mot-clé dans le tout 1er <p>, densité environ 1 %, sous-titres 50-65 %, transitions Yoast 40-50 %, 0 passif, moins de 25 % de phrases longues, aucun début identique consécutif, FAQ dividers en <h3>, 2-4 liens internes LCD en URL complète sans target blank, 1-3 liens croisés vers les autres sites (section 1quater, avec target="_blank" rel="noopener"), pont produit Guestlucky/Lucky Cover en fin, charte orange #FF5101 / navy #182745, 5 visuels NOUVEAUX (jamais utilisés, voir section 2), préfixes CSS uniques, !important, responsive 540px, vouvoiement, zéro emoji, zéro tiret long, zéro H1. Contrôle : python3 .robot-blog/check-seo.py <fichier> "<mot-clé>" jusqu'à tout OK. Regarder le rendu de chaque visuel (capture Chrome headless) avant de publier.

5) IMAGE : Gemini gemini-2.5-flash-image, "imageConfig":{"aspectRatio":"16:9"}, couleurs en toutes lettres (jamais de code hexadécimal), « Absolutely no text, no words, no letters, no numbers, no signs, no labels anywhere », sujet qui remplit le cadre. REGARDER l'image. Secours : miniature https://i.ytimg.com/vi/<ID>/maxresdefault.jpg ou couverture SVG.

6) PUBLICATION API (curl uniquement, jamais Python-urllib) :
   a) rm -f du fichier de réponse AVANT chaque appel. POST /wp-json/wp/v2/media en UN seul envoi, sans --retry, --max-time 170. Si http=000 : GET /media?search=<slug> avant de réessayer (sinon doublon). Vérifier le nom de fichier avant d'utiliser l'id.
   b) Métadonnées média UN champ par requête : alt_text (mot-clé avec accents), puis title, caption, description. Noter source_url.
   c) Catégories : Location courte durée=4, Conciergerie=88, Sous-location=62, Investissement locatif=53, Immobilier=52, Fiscalité=90, Développement Personnel=89.
   d) POST /wp-json/wp/v2/posts : title, slug, status=publish, content, excerpt, featured_media, categories, meta {"_yoast_wpseo_focuskw","_yoast_wpseo_title","_yoast_wpseo_metadesc"} (snippet 5). Titre SEO < 60 caractères, méta 120-145. Vérifier d['slug'] avant d['id'].
   e) Contrôles : relecture context=edit (HTML, featured_media, catégories, 3 meta Yoast), puis URL publique avec un User-Agent navigateur (HTTP 200, <title>, méta, og:image, iframe YouTube, visuels, FAQ), puis accueil en 200. Si og:image reste l'ancienne : second POST du post (cache LiteSpeed). Espacer les lectures (pare-feu).
   Si le site refuse l'API : fichier PROMPTS-EXTENSION-<date>.md avec un bloc unique pour l'extension Chrome (liens raw GitHub de la branche), et le dire franchement.

7) TRAÇABILITÉ : ajouter {"id","date_traitement","article","wp_post_id","url"} dans .robot-blog/traite.json, ligne d'historique des visuels dans la section 2 de CLAUDE.md, puis git pull --rebase, commit, git push -u origin claude/robot-blog-lundi-4cya0g.

8) LIVRAISON (Martin lit sur téléphone), dans cet ordre :
   1. « Image de couverture à contrôler » : source_url seul sur sa ligne + une ligne de description (s'il ne l'aime pas, il le dit et on la remplace).
   2. URL publique de l'article.
   3. Titre, mot-clé, chiffres du check-seo.
   4. Valeurs Yoast + résultat des contrôles.

9) REMPLACEMENT D'IMAGE À LA DEMANDE : régénérer en tenant compte de sa remarque, uploader, mettre à jour featured_media, reposer les métadonnées, second POST du post, vérifier, renvoyer le lien.

10) VOCAUX : transcrire avec faster-whisper (section 1ter, vad_filter=True), corriger les noms propres et le signaler.

Si quelque chose bloque : le dire franchement, ne pas contourner. Aucun secret dans le code ni dans le chat.
```

---

## Tâche du JEUDI (vidéo du mercredi, conditionnelle)

```
ROBOT BLOG JEUDI (v6, Mac, conditionnel) : vidéo du MERCREDI 18h. Même procédure exactement que la tâche du lundi (texte complet dans .robot-blog/ROUTINES.md du dépôt ~/blog, branche claude/robot-blog-lundi-4cya0g), avec cette différence en tête :

TEST CONDITIONNEL D'ABORD (coût minimal) : cd ~/blog && git pull, puis yt-dlp --flat-playlist --playlist-items 1-3 --print "%(id)s\t%(title)s\t%(duration)s" "https://www.youtube.com/@moresebastien/videos". Si la vidéo la plus récente est déjà dans traite.json ET en ligne (vérif ?slug=), et qu'aucune vidéo plus ancienne n'est en attente : écrire UNE ligne « Pas de nouvelle vidéo mercredi : on saute cette semaine. » et S'ARRÊTER, zéro dépense. Sinon, appliquer les étapes 0 à 10 de la tâche du lundi.

Si quelque chose bloque : le dire franchement, ne pas contourner.
```
