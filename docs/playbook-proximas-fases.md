# Playbook — Próximas Fases · O Caminho do Reikiano Iniciante

> Documento de retomada **para o Notebook 1 (casa) e Notebook 2 (escritório)** e sessões futuras. Contém tudo o que é preciso para continuar sem depender do histórico de chat. Atualizado 03/07/2026 (pós-lançamento do e-book).

## 0. Estado do projeto em uma tela

| Fase | Status |
|---|---|
| F0 Setup · F1 E-book v2 · F2 Briefing · F2b Diagramação · F3 Curso+roteiros | ✅ concluídas |
| **F4 Landing page** | ✅ **NO AR e vendendo** — `reikibrasilia.br.com/ebook` (DirectAdmin, subpasta, autossuficiente); botão → checkout Eduzz real (`chk.eduzz.com/7WXGD8240A`); webhook lista de espera ativo. Fluxo testado ponta a ponta. |
| **F5 Verificação de coerência** | ✅ **concluída** — `docs/relatorio-verificacao.md` (APROVADO) |
| **Produto Eduzz (e-book R$ 29,90)** | ✅ **publicado** — imagem `design/eduzz/capa-eduzz-quadrada.png`, entrega PDF `design/eduzz/O-Caminho-do-Reikiano-Iniciante.pdf` (65 págs, foto real do autor, páginas centralizadas, logos ok) |
| **F6 Videoaulas do curso** | ⏭️ **EM ANDAMENTO** — 20 aulas HeyGen (roteiros prontos). M0+M1 já iniciados. Ver §9. |
| F7 Montagem do curso (Nutror) + **upsell R$197** + trilhas de e-mail | ⏳ após F6 — **upsell já especificado/construído**: `landing-page/upsell.html` + `landing-page/upsell-copy.md` (Método Mãos Seguras, comparação e-book×curso, CTAs sim/não). Bloqueado por: gravar vídeo do Renato + configurar upsell one-click no Eduzz + garantir entrega do e-book se recusar. **Decisão 09/07: manter a lista de espera na LP inicial por ora** (curso ainda não gravado). |

**Onde estão as coisas agora:** e-book (funil de entrada) 100% no ar. O próximo grande bloco é o **curso** (upsell R$ 197–297): produzir as videoaulas → subir no Nutror → ativar a lista de espera.

**Spec da F4 (fonte da verdade):** `docs/superpowers/specs/2026-07-03-f4-landing-page-design.md`
**Plano mestre:** `PLANO-EXECUCAO.md`

---

## 1. Decisões travadas (não reabrir sem motivo)

- **Oferta principal única da LP = e-book a R$ 29,90 fixo.** Curso online **R$ 197,00** é upsell posterior (lista de espera secundária no rodapé), nunca compete com a compra.
- **Design system = v3:** roxo `#6A10AD` + ciano `#3FD8E8`; League Spartan / Playfair Display itálico / Inter; marcador ■. Fonte: `design/canva-import/ebook-diagramado-v3.html`.
- **Garantia:** 7 dias (CDC).
- **Depoimentos:** 4 reais transcritos (ver §3).
- **Lista de espera:** webhook n8n, workflow Gmail-native (ver §2) — **já no ar**.
- **Checkout:** Eduzz (link real é pendência do Renato — bloqueador de deploy).

---

## 2. Infra n8n (VERIFICADA e no ar)

- **Instância:** `https://reikibrasilia.app.n8n.cloud` (tinha caído por assinatura; upgrade feito 03/07).
- **API:** REST v1 em `/api/v1`, header `X-N8N-API-KEY`. (A key JWT foi usada nesta sessão; se expirar, gerar nova em Settings → n8n API.)
- **Credencial Gmail reutilizável:** `Gmail OAuth2 API`, id `ljxuwvtS9wNx9hDx`.
- **Workflow da lista de espera:** `Reiki — Lista de Espera Reikiano`, id **`etum7cA1SJRHIk7R`**, **ativo**.
  - **URL de produção:** `https://reikibrasilia.app.n8n.cloud/webhook/reiki-lista-espera`
  - Fluxo: Webhook → Code (segmento) → Gmail notifica `brasiliareiki@gmail.com` → Gmail boas-vindas ao lead → Respond `{ok, segmento}`.
  - JSON versionado: `landing-page/n8n/lista-espera.workflow.json` · doc: `landing-page/n8n/README.md`.
  - Teste validado: `{"ok":true,"segmento":"Terapeuta em Transicao"}`.
- **⚠️ PENDENTE — ajuste anti-duplicação na triagem:** a notificação `[LISTA-ESPERA]` cai no inbox que o workflow `Reiki — Triagem de Leads Gmail` (id `xZNYB74zf4WlVRt1`) monitora. No nó *Email Recebido* (gmailTrigger), acrescentar ao filtro `q`: `-subject:"LISTA-ESPERA"`. (Ou criar filtro Gmail: assunto contém `[LISTA-ESPERA]` → label `Lista de Espera` + pular caixa de entrada.) **Não aplicado ainda — aguarda OK do Renato** (é workflow de produção).

### Recriar/atualizar workflow via API (referência)
```bash
# criar (só name/nodes/connections/settings; API rejeita campos read-only)
curl -s -X POST "$B/workflows" -H "X-N8N-API-KEY: $K" -H "Content-Type: application/json" --data @lista-espera.workflow.json
# ativar (PUT desativa; sempre reativar depois de atualizar)
curl -s -X POST "$B/workflows/<id>/activate" -H "X-N8N-API-KEY: $K"
# atualizar
curl -s -X PUT "$B/workflows/<id>" -H "X-N8N-API-KEY: $K" -H "Content-Type: application/json" --data @lista-espera.workflow.json
```

---

## 3. Depoimentos (prontos)

4 transcrições reais via Groq Whisper em `landing-page/depoimentos-transcricoes.md` (com pull-quotes): **Ana Lúcia, Daiane Neves, Lorena, Rafaela Lehmann**.
**Enquadramento ético:** são depoimentos da jornada com o Reiki/iniciação (não do e-book). Apresentar como alunos do Mestre Renato; disclaimer PNPIC; sem promessa de cura (fala da Rafaela cita ansiedade).

### Transcrever novos vídeos (método simples — dispensa watch.py)
```bash
curl -s "https://api.groq.com/openai/v1/audio/transcriptions" \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -F file="@arquivo.mp4" -F model="whisper-large-v3" -F language="pt" -F response_format="json"
```

---

## 4. F4 — build (✅ CONCLUÍDO 03/07/2026)

Os 3 entregáveis estão na pasta `landing-page/`. Renderização validada em desktop e mobile (preview local via `python -m http.server`, design v3 fiel, zero erro de console).

1. ✅ **`copy.md`** — copy AIDA das 12 seções (spec §5), voz da marca, e-book R$ 29,90 como herói, lista de espera secundária no rodapé.
2. ✅ **`index.html`** — página única autocontida, mobile-first, design v3 (tokens roxo/ciano, League Spartan/Playfair/Inter, marcador ■), com:
   - Webhook **real** embutido no `data-webhook` do form: `https://reikibrasilia.app.n8n.cloud/webhook/reiki-lista-espera` (envio `fetch` POST JSON, payload conforme spec §6; sucesso "Você está na lista! 🌸", erro → fallback WhatsApp).
   - Checkout com placeholder marcado `data-checkout="COLE_EDUZZ_29_90"` + constante JS `CHECKOUT_URL` (todos os 4 CTAs primários; texto já mostra R$ 29,90). **Trocar a constante pela URL da Eduzz no deploy.**
   - 4 depoimentos reais (§3), Rafaela como âncora. Primeira dobra completa (para quem / dor / o que recebe / preço / CTA) + **sticky CTA no mobile**.
   - Imagens via raw GitHub (bg-opener-v3, bg-cover-v3, foto-autor-circulo, logo) → **quebram até o push do `a9a1019`** (§6). O layout degrada com alt text; resolve sozinho após o push.
3. ✅ **`questionario-qualificacao.md`** — 7 perguntas → 3 segmentos (Praticante Pessoal / Aspirante a Terapeuta / Terapeuta em Transição) + 3 trilhas de e-mail + contrato do payload, alinhado ao webhook.

> **Config auxiliar criada:** `.claude/launch.json` (server estático `lp-reikiano` na porta 8123) para preview local — não versionado (dentro de `.claude/`).

---

## 5. Gate de deploy da LP (spec §10) — só publicar quando os 5 estiverem OK

1. [x] Botão de compra com **checkout Eduzz real** R$ 29,90 — ✅ **FEITO** (`https://chk.eduzz.com/7WXGD8240A`); LP **no ar** em `reikibrasilia.br.com/ebook`, fluxo testado ponta a ponta (botão → checkout Eduzz)
2. [x] Primeira dobra vendendo só o e-book — ✅ implementada e validada no HTML (curso só aparece na §11 secundária)
3. [x] Depoimentos reais inseridos — ✅ os 4 integrados na §6 do `index.html` e da `copy.md`
4. [x] Webhook testado — no ar e validado; form da LP envia o payload §6
5. [x] Revisão de conformidade — ✅ **F5 concluída** (`docs/relatorio-verificacao.md`): sem cura/renda garantida, "milenar" ausente, Mikao Usui 1922 na LP, disclaimer PNPIC no rodapé. 2 recomendações opcionais (R1: acrescentar "1922" no e-book v3; R2: consentimento LGPD dos depoimentos).

---

## 6. Pendências do Renato (fora do meu alcance)

- **Criar o produto na Eduzz e devolver o link de checkout** do e-book R$ 29,90.
  **Kit pronto em `design/eduzz/`:** ficha completa do produto + copy (`eduzz-produto.md`) e 5 artefatos (capa, mockup 3D transparente, imagem quadrada 1080, banner social 1200×628, banner de checkout 1200×400 — design v3). Passo a passo na §8 do `eduzz-produto.md`. Ao receber o link, trocar a constante `CHECKOUT_URL` no `landing-page/index.html` (resolve o gate item 1). **PDF de entrega já gerado:** `design/eduzz/O-Caminho-do-Reikiano-Iniciante.pdf` (65 págs, A4). Também corrigido o overlap logo/tagline na capa do `ebook-diagramado-v3.html`.
- ~~**Push do commit `a9a1019`**~~ ✅ **FEITO 03/07/2026** (`git push origin main`, `a6885a5..acbd771`). Raw do GitHub retorna 200 nas 4 imagens → backgrounds/foto/mockup da LP renderizam. Bloqueio de imagens encerrado.
- **OK para o ajuste anti-duplicação na triagem** (§2).
- Ferramenta de captura definitiva (hoje: n8n) e política de garantia já definida (7 dias).

---

## 7. F5 — Verificação de coerência (depois da F4)

Checklist: voz única entre e-book/curso/LP · preços conferidos com a memória oficial (`REIKI-CURSOS-MEMORIA.md`; Nível I R$ 129,90) · claims de saúde com disclaimer PNPIC · zero vestígio de IA · links/CTAs consistentes · Reiki "criado por Mikao Usui em 1922" (nunca "milenar") · sem promessa de renda/cura. Entregável: `docs/relatorio-verificacao.md`.

---

## 8. Ambiente (aprendizados técnicos desta máquina)

- **git funciona** neste repo local (`C:\workspace\Projetos\caminho-reikiano-iniciante`), `origin` configurado. Push é do Renato.
- **python/python3 NÃO estão no PATH do git-bash** aqui → usar **PowerShell** para parsear JSON (`ConvertFrom-Json`).
- **node** não resolve caminhos estilo `/c/...` no `require()` → passar arquivo direto ao `curl --data @` em vez de pré-processar com node.
- Groq Whisper (`whisper-large-v3`) transcreve MP4 direto — dispensa o pipeline `claude-video`/`watch.py` (que é efêmero no sandbox).
- **Chrome headless** (`--print-to-pdf` e `--screenshot`) está disponível e é o motor de PDF/artes: renderiza HTML do design v3 com fidelidade. Para PDF: reescrever URLs raw GitHub → caminho local + `print-color-adjust:exact` (senão fundos escuros saem brancos). **Pillow** e **PyMuPDF** (`pip install pymupdf`) disponíveis para compor/rasterizar/verificar.

---

## 9. F6 — Produção das videoaulas (COMO GERAR) ⏭️ próxima fase

**Fonte da verdade:** grade em `curso/grade-curricular.md`; roteiros prontos (HeyGen-ready) em `curso/roteiros/M0.md … M5.md`.
**Escopo:** 20 aulas · 6 módulos (M0–M5) · 4–7 min cada (~550–900 palavras) · avatar **HeyGen** (clone do Renato, busto, fundo violeta/grafite) · plataforma **Nutror/Eduzz** · ticket R$ 197–297.

### Passo a passo
1. **[Renato] Avatar + voz no HeyGen** — criar/validar o **clone do Renato** (busto, fundo neutro escuro coerente com a marca) e, de preferência, **clone de voz** (autenticidade). Requer gravação de treino + consentimento biométrico — só o Renato faz.
2. **[Claude] Slides de apoio** — cada roteiro traz a nota `Slide:`/`Slide de apoio:`. Gerar os slides (título + até 3 bullets, **design v3**, 1920×1080) pelo mesmo pipeline HTML→PNG (Chrome headless) usado no e-book/Eduzz. Entregar prontos para inserir como B-roll/tela cheia entre blocos.
3. **[Renato/Claude] Montagem por aula no HeyGen** — colar **apenas o texto do bloco `ROTEIRO`** no editor de script (não colar cabeçalhos nem marcações de cena). `[PAUSA]` = recurso de pausa do editor ou "..."; **negrito** = ênfase. Rodar a **prévia de voz** e ajustar naturalidade. Inserir os slides do passo 2.
4. **Render + nomeação** — 1 vídeo por aula, 4–7 min. Padrão: `M{n}-A{k}-titulo.mp4` (ex.: `M1-A05-sentindo-a-energia.mp4`).
5. **[Claude] Materiais de apoio** citados na grade (gerar os que faltam, design v3): mapa da jornada (PDF), checklists ("Estou me bloqueando ou evoluindo?"), templates de mensagem, planilha de registro de sessões, tabela das 9 dificuldades. O **Diário do Reikiano** já existe (bônus do e-book).
6. **Revisão de conformidade** (igual F5): sem "milenar" (Mikao Usui **1922**), sem promessa de cura/renda, disclaimer PNPIC quando citar saúde.

### Divisão de trabalho
- **Só o Renato:** conta HeyGen, treinar/aprovar avatar e voz (biometria/consentimento), render final, upload no Nutror.
- **Claude pode fazer sem HeyGen:** slides de apoio (PNG/PDF), PDFs/planilhas de apoio, thumbnails das aulas, revisão/ajuste fino dos roteiros, títulos e descrições das aulas, sequência de e-mails de conclusão de módulo.

### Ordem sugerida
M0 (2 aulas) → M1 (4) → M2 (4) → M3 (4) → M4 (3) → M5 (3). Começar por **M0+M1** (prova de conceito do avatar/voz + primeiro módulo entregável).

### Conversão embutida (já nos roteiros)
- **A18** → oferta da **mentoria individual** (R$ 197/sessão); **A20** → **Nível II presencial** (condição de aluno) + convite à comunidade Om Reiki Om.

---

## 10. Infra de publicação (aprendida nesta sessão — p/ atualizar a LP no ar)

- **Hospedagem:** DirectAdmin (napoleon) · painel `https://pro127.dnspro.net.br:2222/evo/` (login do Renato) · usuário `reik2545`. Web root: `~/domains/reikibrasilia.br.com/public_html`. LP na subpasta **`/ebook`**.
- **Pacote de deploy autossuficiente:** `landing-page-deploy/` (index.html + `assets/`, imagens locais, **sem** dependência do raw GitHub) + `landing-page-deploy.zip`. Gerado reescrevendo `raw.githubusercontent…/design/canva-import/` → `assets/` no `landing-page/index.html` e copiando os 3 PNGs para `assets/`.
- **Publicar/atualizar via Terminal de comando do painel** (upload pela automação do navegador é **bloqueado** — só aceita arquivos anexados ao chat). Como o repo é **público**, o deploy é por `git clone` no servidor:
  ```bash
  cd ~/domains/reikibrasilia.br.com/public_html
  git clone --depth 1 https://github.com/dpfrenatorms/caminho-reikiano-iniciante.git /tmp/x
  cp -r /tmp/x/landing-page-deploy/* ebook/ && rm -rf /tmp/x
  ```
  ⚠️ Se `landing-page-deploy/` ainda não estiver no push, montar a partir de `landing-page/index.html` no servidor com `sed` (raw→assets) + copiar os PNGs de `design/canva-import/`.
- **Trocar o checkout na LP no ar:** editar SÓ a linha de atribuição `var CHECKOUT_URL = "…"` — **não** tocar no sentinela `"COLE_EDUZZ_29_90"` da comparação. No servidor: `sed -i 's#var CHECKOUT_URL = "URL_ANTIGA"#var CHECKOUT_URL = "URL_NOVA"#' ebook/index.html`.
- **Atualizar um asset no ar** (ex.: foto): `git clone` no terminal + `cp /tmp/x/design/canva-import/<arquivo> ebook/assets/<arquivo>`.
- **Terminal do painel:** ao reabrir, o primeiro `type` costuma não registrar (sessão reconecta) — clicar e digitar de novo. Comandos com acento/`·` funcionam; para segurança, usar `[^<]*` no *match* e reservar não-ASCII só para a *substituição*.
- **Checkout Eduzz atual:** `https://chk.eduzz.com/7WXGD8240A`. **Webhook lista de espera:** `https://reikibrasilia.app.n8n.cloud/webhook/reiki-lista-espera` (§2).
- **Foto do autor:** `design/canva-import/foto-autor-circulo.png` = recorte circular 600×600 de `artefatos/Ensaio-403.jpg` (fotos profissionais em `artefatos/Ensaio-*.jpg`, `FOTO 14 - REIKI I.jpg`).
