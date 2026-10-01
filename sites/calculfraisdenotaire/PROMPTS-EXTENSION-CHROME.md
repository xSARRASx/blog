# calculfraisdenotaire.net : prompts pour l'extension Claude pour Chrome

## ÉTAPE 0 : à faire par Martin AVANT de lancer l'extension (2 minutes)

1. Ouvre chaque lien d'image ci-dessous, puis Cmd+S, et enregistre-la dans **Téléchargements** sous le nom indiqué :
   - https://raw.githubusercontent.com/xSARRASx/blog/claude/robot-blog-lundi-4cya0g/sites/calculfraisdenotaire/cover-contester-taxe-fonciere.png → `contester-taxe-fonciere.png`
   - https://raw.githubusercontent.com/xSARRASx/blog/claude/robot-blog-lundi-4cya0g/sites/calculfraisdenotaire/cover-plus-value-residence-principale.png → `plus-value-residence-principale.png`
2. Ouvre ces 3 onglets dans Chrome :
   - Onglet 1 : wp-admin de calculfraisdenotaire.net (connecté)
   - Onglet 2 : https://raw.githubusercontent.com/xSARRASx/blog/claude/robot-blog-lundi-4cya0g/sites/calculfraisdenotaire/article-contester-taxe-fonciere.html
   - Onglet 3 : https://raw.githubusercontent.com/xSARRASx/blog/claude/robot-blog-lundi-4cya0g/sites/calculfraisdenotaire/article-plus-value-residence-principale.html
3. Colle le BLOC 1 dans l'extension. Quand l'article 1 est publié, colle le BLOC 2. Un bloc à la fois.

---

## BLOC 1 : article « taxe foncière » (à publier EN PREMIER)

```
Tu vas publier un article sur le WordPress de calculfraisdenotaire.net. Travaille lentement, une étape à la fois, et vérifie chaque étape avant de passer à la suivante.

RÈGLE D'OR pour CHAQUE champ à remplir : (1) clique dans le champ, (2) Cmd+A, (3) Delete, (4) colle ou tape la valeur. Ne laisse jamais l'ancien contenu du champ.

ÉTAPE 1 : REPÉRER L'ÉDITEUR DU SITE
Dans l'onglet wp-admin, va dans Articles. Ouvre en modification l'article le plus récent (« Transmission de patrimoine 2026 »). Regarde s'il est construit avec Elementor (bouton « Modifier avec Elementor ») ou avec l'éditeur de blocs WordPress. Note la méthode et quitte SANS RIEN ENREGISTRER. Tu utiliseras la même méthode pour le nouvel article.

ÉTAPE 2 : CRÉER L'ARTICLE ET COLLER LE HTML
- Articles > Ajouter.
- Titre de l'article : Contester sa taxe foncière : la méthode complète en 2026
- Va dans l'onglet 2 (Raw GitHub, fichier article-contester-taxe-fonciere.html). Clique dans la page, Cmd+A, Cmd+C.
- Reviens dans WordPress :
  - Si le site utilise l'éditeur de blocs : ajoute un bloc « HTML personnalisé » (Custom HTML) et colle dedans avec Cmd+V.
  - Si le site utilise Elementor : « Modifier avec Elementor », cherche le widget « HTML » (icône </>, PAS « Mise en évidence du code »), glisse-le dans la zone centrale, colle dans le champ « Code HTML ».
- Vérifie que le contenu collé commence par <style> et se termine par </p> ou </div>, et qu'il n'est pas vide.
- ENREGISTRE EN BROUILLON. NE PUBLIE PAS ENCORE.

ÉTAPE 3 : SLUG
Dans les réglages de l'article (panneau de droite, « Lien » ou « Permalien »), mets le slug : contester-taxe-fonciere

ÉTAPE 4 : IMAGE MISE EN AVANT
- Panneau de droite > « Image mise en avant » > « Téléverser des fichiers ».
- Dans la fenêtre de fichiers, Cmd+Shift+D pour aller dans Téléchargements, choisis contester-taxe-fonciere.png. N'en prends PAS une autre dans la médiathèque.
- Vérifie la vignette : une loupe bleue sur un avis d'imposition, avec une petite maison.
- Texte alternatif : Taxe foncière : loupe sur un avis d'imposition à vérifier
- Titre de l'image : Contester sa taxe foncière
- Valide « Définir l'image mise en avant ».

ÉTAPE 5 : EXTRAIT
Panneau de droite > Extrait. Colle :
Valeurs cadastrales figées depuis 1970, surfaces mal pondérées, dépendances fantômes : comment vérifier votre avis et le contester.

ÉTAPE 6 : CATÉGORIE
Coche la catégorie la plus proche de l'immobilier qui existe déjà (par exemple « Immobilier »). Si rien ne correspond, laisse la catégorie par défaut. Ne crée pas de nouvelle catégorie.

ÉTAPE 7 : YOAST SEO (si le bloc Yoast est présent sous l'article ou dans le panneau)
- Expression clé principale : taxe foncière
- Titre SEO (vide d'abord les variables par défaut avec Cmd+A + Delete) : Contester sa taxe foncière : mode d'emploi 2026
- Slug : contester-taxe-fonciere
- Méta description : Votre taxe foncière repose sur des données de 1970. Voici comment repérer une erreur sur votre avis et déposer votre réclamation.
Si Yoast n'est pas installé, saute cette étape et signale-le-moi à la fin.

ÉTAPE 8 : CONTRÔLE AVANT PUBLICATION
Clique sur « Prévisualiser ». Vérifie : le titre s'affiche, le texte et les encadrés colorés (bleu et navy) s'affichent, aucun code HTML brut visible à l'écran. Si tu vois du code brut, NE PUBLIE PAS et dis-le-moi.

ÉTAPE 9 : PUBLIER
Seulement si tout est bon : clique sur « Publier ». Donne-moi l'URL publique de l'article.
```

---

## BLOC 2 : article « plus-value résidence principale » (APRÈS le bloc 1)

```
Tu vas publier un deuxième article sur le WordPress de calculfraisdenotaire.net, avec exactement la même méthode d'édition que pour l'article précédent (éditeur de blocs ou Elementor). Travaille une étape à la fois.

RÈGLE D'OR pour CHAQUE champ : (1) clique dans le champ, (2) Cmd+A, (3) Delete, (4) colle ou tape la valeur.

ÉTAPE 1 : CRÉER L'ARTICLE ET COLLER LE HTML
- Articles > Ajouter.
- Titre de l'article : Plus-value résidence principale : quand le fisc conteste l'exonération
- Va dans l'onglet 3 (Raw GitHub, fichier article-plus-value-residence-principale.html). Clique dans la page, Cmd+A, Cmd+C.
- Reviens dans WordPress et colle dans un bloc « HTML personnalisé » (ou le widget HTML d'Elementor si le site l'utilise).
- Vérifie que le contenu n'est pas vide.
- ENREGISTRE EN BROUILLON. NE PUBLIE PAS ENCORE.

ÉTAPE 2 : SLUG
plus-value-residence-principale

ÉTAPE 3 : IMAGE MISE EN AVANT
- « Image mise en avant » > « Téléverser des fichiers » > Cmd+Shift+D (Téléchargements) > plus-value-residence-principale.png. N'en prends PAS une autre.
- Vérifie la vignette : une maison bleu marine inspectée à la loupe, des clés qui passent d'une main à l'autre, des pièces et une balance.
- Texte alternatif : Plus-value résidence principale : maison inspectée à la loupe avec compteur électrique
- Titre de l'image : Plus-value résidence principale
- Valide.

ÉTAPE 4 : EXTRAIT
Studio trahi par sa consommation électrique, majoration de 40 % : comment le fisc conteste l'exonération et comment vous protéger.

ÉTAPE 5 : CATÉGORIE
La même que pour l'article précédent.

ÉTAPE 6 : YOAST SEO (si présent)
- Expression clé principale : plus-value résidence principale
- Titre SEO (vide d'abord le champ) : Plus-value résidence principale : l'exonération contestée
- Slug : plus-value-residence-principale
- Méta description : Revendre sa résidence principale reste exonéré, sauf si le fisc doute. Plus-value résidence principale : pièges et preuves à garder.

ÉTAPE 7 : CONTRÔLE
« Prévisualiser » : titre, texte et encadrés visibles, aucun code brut. Clique aussi sur le lien vers l'article « Contester sa taxe foncière » dans le texte : il doit ouvrir l'article publié juste avant (pas une page d'erreur 404). Si quelque chose cloche, NE PUBLIE PAS et dis-le-moi.

ÉTAPE 8 : PUBLIER
Clique sur « Publier » et donne-moi l'URL publique.
```
