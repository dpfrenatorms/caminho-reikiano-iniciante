#!/usr/bin/env bash
# Renderiza um artboard HTML para PNG via Chrome headless (2x para nitidez).
# uso: bash render.sh <arquivo.html> <largura> <altura> <saida.png> [--transparent]
set -e
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
AB="C:/Workspace/Projetos/caminho-reikiano-iniciante/design/eduzz/_artboards"
OUT="C:/Workspace/Projetos/caminho-reikiano-iniciante/design/eduzz"
html="$1"; w="$2"; h="$3"; out="$4"; extra="${5:-}"
bg=""
if [ "$extra" = "--transparent" ]; then bg="--default-background-color=00000000"; fi
"$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --allow-file-access-from-files --force-device-scale-factor=2 \
  --virtual-time-budget=12000 $bg --window-size=$w,$h \
  --screenshot="$OUT/$out" "file:///$AB/$html" 2>&1 | grep -i "bytes written" || true
python -c "from PIL import Image; print('  OK $out ->', Image.open(r'$OUT/$out').size)"
