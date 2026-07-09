#!/usr/bin/env bash
# Regenera o kit visual do produto (curso) via Chrome headless.
# uso: bash render.sh   (a partir de curso/design/produto/_src/)
set -e
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
SRC="C:/Workspace/Projetos/caminho-reikiano-iniciante/curso/design/produto/_src"
OUT="C:/Workspace/Projetos/caminho-reikiano-iniciante/curso/design/produto"

python build.py

render() {  # $1=nome  $2=largura  $3=altura
  "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
    --allow-file-access-from-files --virtual-time-budget=15000 \
    --window-size=$2,$3 --screenshot="$OUT/$1.png" "file:///$SRC/$1.html" 2>&1 \
    | grep -i "bytes written" || true
}

render capa-produto-1080          1080 1080
render banner-vitrine-1200x628    1200  628
render banner-checkout-1200x400   1200  400
render imagem-conclusao-1280x720  1280  720

echo "PNGs em: $OUT"
