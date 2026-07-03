# Deploy da Landing Page — `reikibrasilia.br.com/ebook`

Pacote **autossuficiente** da landing page do e-book. Não depende de GitHub, CDN externo nem banco — só arquivos estáticos. Só sobem as Google Fonts (via internet do visitante).

## Conteúdo
```
index.html          → a landing page (página única)
assets/
  bg-cover-v3.png       → capa/mockup do hero
  bg-opener-v3.png      → fundo do hero
  foto-autor-circulo.png→ foto do Renato (seção autoridade)
```

## Como publicar (subpasta /ebook — cPanel ou similar)
1. Painel de hospedagem → **Gerenciador de Arquivos** → entre em `public_html`.
2. Crie a pasta **`ebook`**.
3. Suba **`index.html`** e a pasta **`assets/`** inteira para dentro de `public_html/ebook`.
   - *(Ou suba o `landing-page-deploy.zip` e use "Extrair" — depois renomeie/mova o conteúdo para `public_html/ebook`.)*
4. Acesse **`https://reikibrasilia.br.com/ebook`** para conferir.

> Estrutura final no servidor:
> ```
> public_html/ebook/index.html
> public_html/ebook/assets/bg-cover-v3.png
> public_html/ebook/assets/bg-opener-v3.png
> public_html/ebook/assets/foto-autor-circulo.png
> ```

## ⚠️ Antes de divulgar — 2 coisas
1. **Link de checkout Eduzz:** o botão de compra ainda está com placeholder (`CHECKOUT_URL = "COLE_EDUZZ_29_90"`). Quando o produto Eduzz estiver publicado, o Claude regenera este pacote já com o link real. **Não divulgue antes disso** (gate de deploy, item 1).
2. **Webhook da lista de espera:** já está embutido e no ar (`reiki-lista-espera`) — funciona assim que a página estiver hospedada.

## Regenerar este pacote
Fonte: `landing-page/index.html`. Ao mudar a copy ou colar o checkout, rodar de novo o script que reescreve as imagens `raw.githubusercontent → assets/` e copia os PNGs. (O Claude faz isso.)
