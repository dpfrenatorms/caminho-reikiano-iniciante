#!/usr/bin/env bash
# Regenera os 4 bônus em PDF a partir do build.py (design v3, A4).
# uso: bash render.sh   (a partir de curso/upsell/bonus/_src/)
set -e
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
SRC="C:/Workspace/Projetos/caminho-reikiano-iniciante/curso/upsell/bonus/_src"
OUT="C:/Workspace/Projetos/caminho-reikiano-iniciante/curso/upsell/bonus"

python build.py

for f in bonus-1-checklist-sessao-segura \
         bonus-2-roteiro-conversa-cliente \
         bonus-3-plano-21-dias \
         bonus-4-guia-objecoes ; do
  "$CHROME" --headless=new --disable-gpu --no-sandbox \
    --no-pdf-header-footer --print-to-pdf-no-header \
    --virtual-time-budget=20000 --allow-file-access-from-files \
    --print-to-pdf="$OUT/$f.pdf" "file:///$SRC/$f.html" 2>&1 | grep -i "bytes written" || true
done
echo "PDFs em: $OUT"
