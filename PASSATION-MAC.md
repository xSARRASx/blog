# Prompt de passation : à coller dans la conversation Claude Code du Mac

```
Salut ! Tu reprends le « Robot BLOG » de Martin. Il travaillait jusqu'ici dans une conversation cloud qui vient d'être arrêtée. Tu continues sur son Mac, exactement là où elle s'est arrêtée.

QUI : Martin, il tutoie et dit « mon lapin ». Il lit sur son téléphone : messages COURTS, UNE action à la fois, mots simples. Ne lui demande pas son accord pour continuer quand c'est bien fait : tu enchaînes.

RÈGLES NON NÉGOCIABLES : aucun secret dans le code ni dans le chat, avance étape par étape, si quelque chose bloque dis-le franchement au lieu de contourner, commit + push après chaque livraison. Jamais d'article sans vraie transcription de la vidéo.

ÉTAPE 1 : LE DÉPÔT
- Si ~/blog n'existe pas : git clone https://github.com/xSARRASx/blog.git ~/blog
- Puis : cd ~/blog && git fetch origin && git checkout claude/robot-blog-lundi-4cya0g && git pull
- Lis EN ENTIER, dans cet ordre : REPRISE.md, CLAUDE.md, .robot-blog/ROUTINES.md. Tout y est (règles SEO, gabarit des articles, pièges WordPress, historique).
- ATTENTION : CLAUDE.md a été écrit dans un conteneur Linux. Sur Mac : node se trouve avec $(which node) (pas /opt/node22/...), et .robot-blog/setup-ytdlp.sh ne sert pas. La bonne branche est claude/robot-blog-lundi-4cya0g (pas l'ancienne claude/seo-article-production-gw6zA citée par endroits).

ÉTAPE 2 : LES OUTILS
- Vérifie python3, curl, git, node, yt-dlp. S'il manque quelque chose, installe-le (brew install yt-dlp node, ou python3 -m pip install -U yt-dlp) en disant à Martin en une phrase ce que tu installes.

ÉTAPE 3 : LES SECRETS (Martin les pose lui-même)
- Vérifie SANS JAMAIS AFFICHER LEUR VALEUR que ces 3 variables existent : WP_APP_USER, WP_APP_PASSWORD, GEMINI_API_KEY. Par exemple : for v in WP_APP_USER WP_APP_PASSWORD GEMINI_API_KEY; do [ -n "${!v}" ] && echo "$v OK" || echo "$v MANQUANTE"; done (en zsh : utilise printenv).
- S'il en manque : explique à Martin, en messages très courts, d'ouvrir son fichier ~/.zshrc et d'y ajouter lui-même des lignes export NOM="valeur", puis de rouvrir le Terminal et Claude. Où trouver les valeurs : WordPress > wp-admin de locationcourteduree.fr > Profil > Mots de passe d'application (compte martin) ; Gemini : https://aistudio.google.com/apikey. Dis-lui bien de NE JAMAIS coller ces valeurs dans le chat.
- Test : curl -sS -u "$WP_APP_USER:$WP_APP_PASSWORD" "https://www.locationcourteduree.fr/wp-json/wp/v2/users/me?_fields=id,name" doit renvoyer martin. Et curl -sS -o /dev/null -w "%{http_code}\n" -H "x-goog-api-key: $GEMINI_API_KEY" https://generativelanguage.googleapis.com/v1beta/models doit renvoyer 200.

ÉTAPE 4 : PRIORITÉ N°1, PUBLIER L'ARTICLE « PATRIMOINE »
- Il est prêt et contrôlé : article-patrimoine.html + cover-patrimoine.png. Toutes les valeurs (titre, slug, catégories, extrait, titre SEO, méta, alt) sont dans PROMPTS-EXTENSION-02-11-2026.md.
- Vérifie d'abord qu'il n'existe pas déjà (?slug=patrimoine, tous statuts, avec auth).
- Publie-le PAR L'API en suivant l'étape 6 de .robot-blog/ROUTINES.md (un seul envoi d'image sans --retry, métadonnées un champ par requête, status=publish, 3 meta Yoast, puis tous les contrôles).
- Puis : rnHBcB6rw0Y dans .robot-blog/traite.json, ligne d'historique des visuels dans la section 2 de CLAUDE.md (texte prêt dans REPRISE.md), commit + push.
- Livre à Martin dans l'ordre : lien de l'image de couverture, URL de l'article, valeurs Yoast, résultat des contrôles.
- Si le site refuse aussi depuis le Mac : dis-le franchement et donne-lui le bloc de PROMPTS-EXTENSION-02-11-2026.md pour l'extension Chrome.

ÉTAPE 5 : LES TÂCHES PROGRAMMÉES (seulement après le succès de l'étape 4)
- Recrée 2 tâches programmées dans cette conversation avec le texte exact de .robot-blog/ROUTINES.md : lundi 8h heure de Paris (vidéo du dimanche) et jeudi 8h heure de Paris (vidéo du mercredi, conditionnelle).
- Préviens Martin en une phrase : elles ne tournent que si le Mac est allumé et Claude ouvert à ce moment-là.
- Ensuite, dès qu'une nouvelle vidéo sort, applique la procédure complète de ROUTINES.md.

PETITES CHOSES EN ATTENTE (après le reste, sans urgence) : voir la section « Petites choses en attente » de REPRISE.md.

Commence par l'étape 1 et dis-moi en une ligne où tu en es.
```
