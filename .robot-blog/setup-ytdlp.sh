#!/usr/bin/env bash
# Restaure l'environnement de transcription YouTube apres un redemarrage de conteneur.
# Usage : bash .robot-blog/setup-ytdlp.sh
set -u
export PATH=/opt/node22/bin:$PATH

echo "1/3 yt-dlp"
pip install --quiet -U yt-dlp
yt-dlp --version

echo "2/3 fournisseur de PO token"
pip install --quiet bgutil-ytdlp-pot-provider
if [ ! -f /root/bgutil-ytdlp-pot-provider/server/build/generate_once.js ]; then
  rm -rf /root/bgutil-ytdlp-pot-provider
  git clone --depth 1 -q https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git /root/bgutil-ytdlp-pot-provider
  ( cd /root/bgutil-ytdlp-pot-provider/server && npm install --silent --no-fund --no-audit && npx --yes tsc )
fi
ls -la /root/bgutil-ytdlp-pot-provider/server/build/generate_once.js

echo "3/3 commande de transcription a utiliser"
cat <<'EOT'
yt-dlp --js-runtimes "node:/opt/node22/bin/node" \
  --skip-download --write-auto-sub --sub-lang "fr.*" --sub-format json3 \
  -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=<ID>"

Si des cookies YouTube sont disponibles dans la variable YT_COOKIES :
  printf '%s' "$YT_COOKIES" > /tmp/yt-cookies.txt
  puis ajouter  --cookies /tmp/yt-cookies.txt  a la commande ci-dessus.

NE PAS utiliser --impersonate : le proxy de l'environnement re-termine le TLS,
la signature navigateur est donc reecrite avant d'atteindre YouTube (teste le 27/08/2026).
EOT
