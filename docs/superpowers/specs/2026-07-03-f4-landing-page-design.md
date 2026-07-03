# F4 — Landing Page · Design Spec

**Projeto:** O Caminho do Reikiano Iniciante — ecossistema digital
**Fase:** F4 (landing page) do `PLANO-EXECUCAO.md`
**Data:** 2026-07-03 · **Autor:** Claude (Cowork) · **Aprovação:** Renato Menezes
**Status:** aprovado para implementação (aguarda spec review + `GROQ_API_KEY` para depoimentos)

---

## 1. Objetivo

**Oferta principal única da LP: o e-book a R$ 29,90** (produto de entrada). A LP existe para **vender o e-book** — nada mais deve competir com essa venda. O curso online (**R$ 197,00**) é upsell **posterior**, capturado como lista de espera **secundária no final da página**, sem disputar atenção com a compra. A LP é a peça de entrada do Funil 2 da marca.

> **Gateway de aprovação (03/07/2026):** aprovada para **implementação**, **não** para deploy público. Liberação de deploy condicionada ao gate da §10.

**Job Statement (JTBD):** *"Quando termino minha iniciação e me sinto inseguro para aplicar Reiki em outras pessoas, quero um caminho passo a passo validado por um mestre experiente, para praticar com confiança e transformar o Reiki em atendimentos reais."*

Ansiedades a neutralizar na copy: "cobrar por Reiki é errado?", "preciso de registro/CRT?", "e se não sentirem nada?". Concorrência real (JTBD): grupos gratuitos, o "vou esperar o Nível II" e a inércia de não praticar.

---

## 2. Decisões desta fase (travadas)

| Decisão | Definição |
|---|---|
| **Design system** | **v3** (roxo `#6A10AD` + ciano `#3FD8E8`, capa fotográfica, League Spartan) — continuidade visual com o e-book v3 |
| **Oferta principal** | **E-book — R$ 29,90 fixo** (único produto vendido na LP) |
| **Upsell** | Curso online **R$ 197,00** — só como **lista de espera secundária no rodapé**, nunca como oferta concorrente |
| **Garantia** | **7 dias (CDC)** |
| **Lista de espera** | **Form nativo → webhook n8n** (payload na §6); workflow dedicado **Gmail-native (Opção B)**; segmentação no nó Code; **secundária, nunca compete com a compra** |
| **Depoimentos** | **4 vídeos transcritos** (Ana, Daiane, Lorena, Rafaela) + card texto do reel da Rafaela — reais, nunca genéricos |
| **Checkout** | Eduzz — botão de compra R$ 29,90. **Link real é bloqueador de deploy** (§10); na implementação usa placeholder marcado, texto do botão já mostra R$ 29,90 |

---

## 3. Design system v3 (fonte da verdade: `design/canva-import/ebook-diagramado-v3.html`)

**Tipografia**
- Títulos: `League Spartan` (800/900), `text-transform:uppercase` nos grandes
- Citações/frases: `Playfair Display` *itálico*
- Corpo: `Inter` (300/400/600/700)
- Import: `https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;600;700;800;900&family=Playfair+Display:ital,wght@1,400;1,700&family=Inter:wght@300;400;600;700&display=swap`

**Paleta (tokens)**
| Token | Hex | Uso |
|---|---|---|
| `--roxo` | `#6A10AD` | primária, títulos claros, marcador ■ |
| `--roxo-2` | `#8E3FC7` | subtítulos |
| `--roxo-txt` | `#3d1466` | texto de citação |
| `--escuro` | `#1a1040` | fundos de seção escura (hero, autoridade, CTA) |
| `--strip` | `rgba(58,20,95,.92)` | faixas de oferta |
| `--ciano` | `#3FD8E8` | acento, linhas, eyebrow, destaques de preço |
| `--ciano-2` | `#7FE9F4` | preço grande |
| `--lavanda` | `#CDB8F0` | frases Playfair sobre fundo escuro |
| `--lav-bg` | `#F5EEFF` | cards/caixas claras |
| `--bg` | `#e8e4ee` | fundo geral claro |
| `--txt` | `#2B2B2B` | corpo claro |

**Marcador de lista:** `■` em `--roxo` (classe `.sq`). **Linhas de acento:** 2px `--ciano`.

---

## 4. Entregáveis

1. `landing-page/index.html` — página única, autocontida, responsiva (mobile-first), CSS inline, sem dependências além das Google Fonts. Pronta para deploy em host/Eduzz.
2. `landing-page/copy.md` — copy AIDA completa por seção (texto puro para revisão editorial).
3. `landing-page/questionario-qualificacao.md` — 7 perguntas → 3 segmentos + trilhas de e-mail + contrato do payload n8n.

**Abordagem descartada:** HTML componentizado multi-arquivo — desnecessário para LP única, complica deploy.

---

## 5. Estrutura do `index.html` — 12 seções (AIDA)

| # | Seção | Conteúdo | Estilo v3 |
|---|---|---|---|
| 1 | **Hero (primeira dobra)** | Deve responder em 1 tela: **para quem** (eyebrow "PARA O REIKIANO RECÉM-INICIADO") · **qual dor** (headline job emocional: "Você foi iniciado no Reiki… mas ainda não aplicou em ninguém?") · **o que recebe** (subhead: o e-book/guia prático) · **quanto custa** (R$ 29,90 visível) · **próximo passo** (CTA "Quero o e-book — R$ 29,90"). Mockup do e-book v3 visível. **CTA visível sem scroll no desktop; CTA rápido no mobile.** | Fundo `--escuro`, eyebrow ciano, título League Spartan ~44px, linha ciano |
| 2 | **Identificação** | "Você fez sua iniciação e travou?" — 3–4 dores (certificado na gaveta; medo de "não sentirem nada"; não sabe cobrar; sem clientes) | Cards `--lav-bg`, marcador ■ |
| 3 | **O que você destrava** | 7 capítulos → 7 benefícios concretos | Lista ■ ciano |
| 4 | **Para quem é / não é** | 2 colunas de qualificação (é: recém-iniciado, travado, quer atender; não é: quem busca atalho mágico) | Contraste roxo/ciano |
| 5 | **Autoridade** | Mestre Renato — 27 anos · Nível IV · Delegado Federal · Master Coach + foto (Ensaio-403, `foto-autor-circulo.png`) | Faixa `--escuro`, foto circular borda roxa |
| 6 | **Prova social** | Depoimentos das 4 transcrições + card Rafaela (texto do reel: *"Me reencontrei comigo mesma… Foi como se uma luz acendesse dentro de mim"*) | Citações Playfair itálico, borda ciano |
| 7 | **Oferta (e-book R$ 29,90)** | Ancoragem (valor do conteúdo vs. **R$ 29,90**) + bônus (Diário do Reikiano) + **CTA de compra → checkout Eduzz do e-book**. Preço R$ 29,90 em destaque. Provas (autoridade §5 + depoimentos §6) vêm **antes** desta seção. | Strip ciano, preço `--ciano-2` grande |
| 8 | **Garantia** | Selo "7 dias — garantia incondicional (CDC)" + compra segura Eduzz | Selo, quebra de objeção |
| 9 | **FAQ** | 6–8 objeções: "não fiz Nível I ainda?", "funciona se fui iniciado por outro mestre?", "é curso ou e-book?", "preciso de registro para cobrar?", "e se eu não sentir a energia?" | Acordeão (`<details>`) |
| 10 | **CTA final + P.S.** | Reforço da promessa (caminho/método, **nunca renda garantida**) + **CTA de compra R$ 29,90** + assinatura do Mestre | Fundo `--escuro` |
| 11 | **Lista de espera do curso (secundária)** | **Só depois** de esgotada a venda do e-book: "O programa completo está chegando" + **form nativo** (nome, e-mail, WhatsApp + 7 perguntas) → webhook n8n. **Não interrompe a venda; não compete com o CTA de compra.** | Strip discreto; `data-webhook` = placeholder |
| 12 | **Rodapé** | Disclaimer PNPIC + contatos (@reiki.brasilia · WhatsApp (61) 98309-7777 · reikibrasilia.br.com · brasiliareiki@gmail.com) + políticas | Fine print |

---

## 6. Contrato do webhook n8n (lista de espera)

O `<form>` da seção 11 envia `POST` (JSON) para um endpoint n8n. Na LP o `action`/URL fica como **placeholder** (`data-webhook="COLE_AQUI_O_WEBHOOK_N8N"`) para Renato colar a URL de produção no deploy. Envio via `fetch()` com `Content-Type: application/json`; a **segmentação é calculada no n8n**, não na LP (mantém a LP burra).

### Payload (JSON enviado ao webhook)

```json
{
  "origem": "landing-page-caminho-reikiano",
  "timestamp_cliente": "2026-07-03T14:22:00-03:00",
  "contato": {
    "nome": "string",
    "email": "string (email)",
    "whatsapp": "string (com DDD, ex: +55 61 9XXXX-XXXX)"
  },
  "questionario": {
    "q1_momento_reiki":     "nunca_iniciei | nivel_1 | nivel_2_mais | mestre",
    "q2_tempo_iniciacao":   "menos_6_meses | 6_a_12_meses | 1_a_3_anos | mais_3_anos",
    "q3_frequencia":        "diaria | semanal | raramente | parei",
    "q4_maior_dificuldade": "inseguranca | sentir_energia | conseguir_pessoas | medo_cobrar | aspectos_legais",
    "q5_objetivo":          "uso_pessoal | familia_amigos | profissional | viver_de_reiki",
    "q6_ja_atendeu":        "sim_gratis | sim_pago | ainda_nao",
    "q7_investimento":      "ate_197 | de_197_a_297 | de_297_a_497 | acima_497"
  }
}
```

### Regras de segmentação (aplicar no nó Code → campo `segmento`)

| Segmento | Condição (prioridade de cima para baixo) | Trilha |
|---|---|---|
| **Terapeuta em Transição** | `q6 = sim_pago` **ou** `q5 = viver_de_reiki` | curso + mentoria |
| **Aspirante a Terapeuta** | `q5 ∈ {profissional, viver_de_reiki}` **ou** `q4 ∈ {conseguir_pessoas, medo_cobrar, aspectos_legais}` | curso |
| **Praticante Pessoal** | demais casos (`q5 ∈ {uso_pessoal, familia_amigos}`) | nutrição |

### Arquitetura n8n — VERIFICADA (03/07/2026)

Instância `reikibrasilia.app.n8n.cloud` **ativa**; 7 workflows; credencial **Gmail OAuth2 API** já configurada (usada por 5 workflows). **Não há credencial de Google Sheets** → escolhida a **Opção B (Gmail-native)** para zero setup novo.

**Workflow dedicado a criar:** `Reiki — Lista de Espera Reikiano`
```
[Webhook POST /reiki-lista-espera]
  → [Code: valida payload + calcula "segmento"]
  → [Gmail: send → inbox]   assunto "[LISTA-ESPERA] {nome} · {segmento}", corpo estruturado com as 7 respostas
  → [Gmail: addLabels → "Lista de Espera"]   (reusa credencial Gmail OAuth2 existente)
  → [Gmail: send → boas-vindas ao lead por segmento]  (opcional)
  → [Respond to Webhook: 200 {ok:true, segmento}]
```

**Integração com a triagem existente:** o workflow `Reiki — Triagem de Leads Gmail` (`xZNYB74zf4WlVRt1`) processa todo e-mail não lido e rascunha respostas via Claude. Para **não** reprocessar os leads da lista de espera (já qualificados), ajustar o filtro do gmailTrigger da triagem para incluir `-label:lista-espera`. O label `Lista de Espera` é criado/selecionado ao importar o workflow novo.

**Não reutilizar** o webhook `instagram-dm-ai` (`LJbVP9FCw7LWTrm6`) — workflow dedicado mantém a automação de DM isolada.

### Validação client-side (na LP)
- `nome`, `email`, `whatsapp` obrigatórios; `email` com validação de formato; WhatsApp aceita máscara.
- 7 perguntas como `select`/`radio` obrigatórios.
- Mensagem de sucesso ("Você está na lista! 🌸") + tratamento de erro (fallback: link do WhatsApp).

---

## 7. Conformidade e voz (contrato de qualidade)

- **Voz única:** acolhedora, inspiradora, humanizada, com respaldo técnico — idêntica ao e-book e ao curso.
- **Reiki:** prática integrativa e complementar (PNPIC/SUS), nunca substituto de tratamento médico → **disclaimer no rodapé**. Regra da marca: "técnica japonesa criada por Mikao Usui em 1922", **jamais "milenar"**.
- **Promessa:** caminho e método — **nunca renda garantida** (risco de plataforma/ads).
- **Preços de cursos presenciais** (se citados): apenas da memória oficial (`REIKI-CURSOS-MEMORIA.md` — Nível I R$ 129,90, turma 14/06/2026, Vista Shopping/Águas Claras). Preço do e-book: R$ 29,90–47 (faixa a confirmar no deploy).
- **Zero vestígio de IA** — varredura na F5.

---

## 8. Dependências e pendências

| Item | Bloqueia | Resolução |
|---|---|---|
| `GROQ_API_KEY` (gratuita) | Depoimentos reais (seção 6) | Renato fornece → transcrição Whisper local dos 4 MP4 em `artefatos/videos/` |
| **Push do commit `a9a1019`** (v3, local-only; `origin` está em `a6885a5`) | Backgrounds da LP e mockup (raw 404) + import Canva | Push para `origin/main` (confirmar com Renato) |
| Importar o workflow `Reiki — Lista de Espera Reikiano` no n8n | URL de produção do webhook | Claude gera o JSON import-ready; Renato importa, cria label `Lista de Espera`, ativa e envia a URL |
| Ajuste do filtro da triagem (`-label:lista-espera`) | Evitar reprocessamento dos leads | 1 linha no gmailTrigger de `xZNYB74zf4WlVRt1` |
| Link de checkout Eduzz + preço final | CTA da oferta | Placeholder; confirmar no deploy |

**n8n verificado (03/07/2026):** instância ativa, API key funcional, credencial Gmail OAuth2 disponível → e-mail e armazenamento resolvidos sem setup novo (Opção B).

---

## 9. Critério de conclusão da implementação (build)

- [ ] `copy.md` revisado e aprovado por Renato
- [ ] `index.html` renderiza corretamente, design v3 fiel
- [ ] **Mobile vende bem** (não só responsivo): CTA visível rápido · texto curto por bloco · botões grandes (alvo ≥ 44px) · mockup sem quebrar · form fácil de preencher · página leve (sem libs pesadas, imagens otimizadas)
- [ ] **Hierarquia de CTA:** todos os CTAs primários levam à **compra do e-book R$ 29,90**; lista de espera é secundária e não compete
- [ ] Form da lista de espera envia payload conforme §6 (testado contra webhook)
- [ ] `questionario-qualificacao.md` com 7 perguntas + 3 segmentos + trilhas
- [ ] Depoimentos reais integrados (pós-transcrição) — nenhum genérico
- [ ] Handoff para **F5** (verificação de coerência: tom, preços, claims, links, anti-IA)

## 10. Gateway de deploy (bloqueadores — LP não vai ao ar até todos resolvidos)

A LP está **aprovada para implementação, não para deploy público**. Liberar o deploy **somente** quando os 5 itens abaixo estiverem concluídos:

1. [ ] **Botão de compra com checkout Eduzz real** do e-book **R$ 29,90** (zero placeholder em botão de compra)
2. [ ] **Primeira dobra** ajustada para vender **apenas a oferta inicial** (e-book), curso não aparece como oferta principal
3. [ ] **Depoimentos reais** (ou provas substitutas éticas) inseridos
4. [ ] **Webhook/formulário testado** (curl do README → `{"ok":true,...}`) — ou o form removido da versão inicial
5. [ ] **Revisão final de conformidade:** sem promessa de cura, sem renda garantida, sem claim exagerado; Reiki como prática criada por Mikao Usui em 1922 (nunca "milenar"); disclaimer PNPIC no rodapé

**Nunca publicar enquanto houver:** link de checkout placeholder · webhook placeholder em produção · depoimento ausente/falso · preço indefinido no botão · CTA dividido entre compra e lista de espera · claim exagerado de cura/renda/resultado.
