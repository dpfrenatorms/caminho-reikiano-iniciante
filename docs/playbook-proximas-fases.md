# Playbook — Próximas Fases · O Caminho do Reikiano Iniciante

> Documento de retomada **para o Notebook 2 (escritório)** e sessões futuras. Contém tudo o que é preciso para continuar sem depender do histórico de chat. Atualizado 03/07/2026.

## 0. Estado do projeto em uma tela

| Fase | Status |
|---|---|
| F0 Setup · F1 E-book v2 · F2 Briefing · F2b Diagramação · F3 Curso+roteiros | ✅ concluídas |
| **F4 Landing page** | ✅ **build concluído** (`copy.md` + `index.html` + `questionario-qualificacao.md`) — falta só o **gate de deploy** (pendências do Renato: checkout Eduzz + push do commit `a9a1019`) |
| **F5 Verificação de coerência** | ✅ **concluída** — `docs/relatorio-verificacao.md` (veredito: APROVADO; sem bloqueador de conformidade; 2 recomendações opcionais) |

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
