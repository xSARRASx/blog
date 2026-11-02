# Reprise de la conversation « Robot BLOG » (état au 2 novembre 2026)

À lire en premier dans toute nouvelle conversation, avec `CLAUDE.md` (mémoire complète des règles et apprentissages).

## Qui, quoi

- Interlocuteur : Martin (il tutoie, dit « mon lapin »). Messages courts, une action à la fois, ton simple. Il lit souvent sur téléphone.
- Les vidéos sont celles de son père, Sébastien More (chaîne YouTube @moresebastien, 2 vidéos par semaine : dimanche et mercredi).
- Le robot transforme chaque vidéo en article SEO pour locationcourteduree.fr, et parfois un article jumeau pour calculfraisdenotaire.net ou declarationlmnp.fr.
- Martin a demandé de **ne plus lui demander son accord pour continuer** : on enchaîne quand c'est bien fait.

## Branche Git

- Tout le travail récent est sur la branche `claude/robot-blog-lundi-4cya0g` du dépôt `xSARRASx/blog`. Les liens raw GitHub des blocs extension pointent vers cette branche.

## Derniers articles (tous en ligne)

| Vidéo | Article | Adresse |
|---|---|---|
| J9XrIi1qWPU (TVA Airbnb) | article-tva-airbnb.html | https://www.locationcourteduree.fr/2026/10/22/tva-airbnb/ (post 10409) |
| _bR52Hhc91Q (10 villes) | article-prix-immobilier.html | https://www.locationcourteduree.fr/2026/10/29/prix-immobilier/ |
| _bR52Hhc91Q (10 villes) | sites/calculfraisdenotaire/article-capacite-emprunt.html | https://www.calculfraisdenotaire.net/capacite-emprunt/ |
| VKxhxpfDx7w (corvées de départ) | article-regles-airbnb.html | https://www.locationcourteduree.fr/2026/10/29/regles-airbnb/ |

| rnHBcB6rw0Y (9 habitudes) | article-patrimoine.html | **PAS ENCORE PUBLIÉ** (voir plus bas) |

Les trois du 29/10 ont été publiés par Martin avec l'extension Claude pour Chrome (bloc unique dans `PROMPTS-EXTENSION-28-10-2026.md`), parce que le robot n'arrivait plus à joindre le site. `.robot-blog/traite.json` est à jour jusqu'à VKxhxpfDx7w.

## PRIORITÉ N°1 : publier l'article « patrimoine »

- Vidéo rnHBcB6rw0Y (transcrite par Gemini le 02/11), article prêt et contrôlé : `article-patrimoine.html`, couverture `cover-patrimoine.png`.
- Toutes les valeurs (titre, slug `patrimoine`, catégories Développement Personnel=89 + Investissement locatif=53, extrait, titre SEO, méta, alt) sont dans `PROMPTS-EXTENSION-02-11-2026.md`.
- Pas publié parce que le site bloquait le robot cloud. Depuis le Mac : publier par API (procédure étape 6 de `.robot-blog/ROUTINES.md`), sinon donner à Martin le bloc extension du même fichier.
- Après publication : ajouter rnHBcB6rw0Y dans `traite.json` et la ligne `article-patrimoine.html` dans l'historique (section 2 de CLAUDE.md) : « Double compteur 72 000 / 98 400 (PREMIÈRE utilisation), Règle des taux 3,5 / 20 / 23,5 % (PREMIÈRE utilisation), Pile du matelas de 6 mois (PREMIÈRE utilisation), Deux tirelires 166 000 / 82 000 (PREMIÈRE utilisation), Seaux percés 220 / 400 euros (PREMIÈRE utilisation), CTAs duo ».

## Problèmes en cours

1. **Le site bloque le robot depuis le 28/10** : HTTPS coupé (`curl: (35) Connection reset by peer`) vers locationcourteduree.fr, calculfraisdenotaire.net et guestlucky.com (même hébergeur), par intermittence. Le robot sort par les IP `160.79.106.x`. Martin doit demander à son hébergeur d'autoriser la plage `160.79.106.0/24` (message prêt envoyé le 29/10). En attendant : publication par l'extension Chrome avec un bloc unique (Martin doit être connecté aux wp-admin avant, l'extension refuse de taper les mots de passe).
2. **YouTube bloque souvent yt-dlp** : la transcription de secours par Gemini marche (`python3 .robot-blog/transcrire-gemini.py <ID> <sortie.txt>`). Crédits Gemini rechargés par Martin le 29/10 (prépaiement). Basse résolution vérifiée le 02/11 : environ 0,12 € pour 34 minutes.

## Petites choses en attente

- Lien interne possible entre https://www.calculfraisdenotaire.net/capacite-emprunt/ et /erreurs-pret-immobilier/ (suggestion de l'extension).
- Ancienne remarque non traitée : la FAQ de l'article LMNP 2027 (post 10396) dit « l'amortissement reste entier », à vérifier.

## Tâches programmées (robot automatique)

- **Robot cloud ARRÊTÉ le 02/11/2026 à la demande de Martin** : les tâches lundi `trig_018Re37nCRvKAFkHiXmcCbA3` et jeudi `trig_01879X2BCDSn7bEjgivroJf9` sont en pause (pas supprimées) dans l'ancienne conversation cloud.
- Le travail continue dans une conversation Claude Code sur le Mac de Martin. Le texte complet des deux tâches, mis à jour (v6), est dans `.robot-blog/ROUTINES.md` : à recréer sur le Mac seulement après un premier article publié avec succès depuis le Mac.

## Procédure standard d'un article (résumé)

1. Lister la chaîne (`yt-dlp --flat-playlist`), anti-doublon (traite.json + `?slug=` sur le site).
2. Transcription : `bash .robot-blog/setup-ytdlp.sh` puis la commande yt-dlp de référence de CLAUDE.md ; si bloqué, Gemini tout de suite.
3. Article LCD (gabarit lcd-wrap, 5 visuels nouveaux, FAQ), contrôle `python3 .robot-blog/check-seo.py <fichier> "<mot-clé>"` jusqu'à tout OK.
4. Image Gemini 16:9 sans texte (sinon miniature YouTube ou couverture SVG).
5. Publication API (si le site répond) ou bloc extension Chrome (si bloqué).
6. traite.json + historique des visuels dans CLAUDE.md, commit + push, message court à Martin (lien de l'image en premier).

## Si la reprise se fait sur le Mac de Martin (conversation locale, pas dans le cloud)

- **Gros avantage** : le Mac de Martin n'est pas bloqué par le pare-feu de l'hébergeur (il se connecte normalement à ses wp-admin), et YouTube bloque beaucoup moins une connexion de particulier. Le robot devrait donc pouvoir de nouveau publier directement par l'API, sans passer par l'extension Chrome.
- **Récupérer le dépôt** : `git clone https://github.com/xSARRASx/blog.git ~/blog && cd ~/blog && git checkout claude/robot-blog-lundi-4cya0g`.
- **Outils à vérifier sur le Mac** : `python3`, `curl`, `git`, `yt-dlp` (`python3 -m pip install -U yt-dlp` ou `brew install yt-dlp`), Node (`brew install node`). Les chemins Linux de CLAUDE.md ne valent pas sur Mac : remplacer `node:/opt/node22/bin/node` par `node:$(which node)`. Le script `.robot-blog/setup-ytdlp.sh` est fait pour le conteneur Linux : sur Mac, l'adapter ou s'en passer.
- **Secrets** : le Mac n'a pas les variables `WP_APP_USER`, `WP_APP_PASSWORD` et `GEMINI_API_KEY`. Martin doit les ajouter lui-même dans son fichier `~/.zshrc` (lignes `export NOM="valeur"`), puis rouvrir le Terminal. **Il ne doit JAMAIS coller ces valeurs dans le chat.** Mot de passe d'application WordPress : wp-admin > Profil > Mots de passe d'application (en créer un nouveau si besoin). Clé Gemini : https://aistudio.google.com/apikey.
- **Tâches programmées** : celles du lundi et du jeudi tournent dans la conversation cloud. Une tâche programmée sur le Mac ne se lance que si le Mac est allumé avec Claude ouvert. Ne déplacer les tâches qu'une fois la conversation Mac validée sur un premier article.
