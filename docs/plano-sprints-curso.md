# Plano de Sprints — Curso Upsell · O Caminho do Reikiano Iniciante

> **Objetivo do documento:** organizar os próximos passos do ecossistema do produto digital em sprints por **marco** (sem data fixa — cada sprint fecha quando o entregável é aprovado por você). Ponto de partida: e-book publicado e vendendo, landing page no ar, roteiros das 20 aulas prontos e **avatar/voz HeyGen já aprovados**.
> **Atualizado:** 08/07/2026 · **Base:** `PLANO-EXECUCAO.md`, `docs/playbook-proximas-fases.md`, `curso/grade-curricular.md`, roteiros `curso/roteiros/M0–M5.md`.

---

## 1. Onde estamos e para onde vamos

O **Funil 2** (Reikiano iniciado) já tem a porta de entrada funcionando:

```
E-BOOK R$ 29,90  ✅ no ar e vendendo (Eduzz + LP reikibrasilia.br.com/ebook)   ← o MAPA
      ↓  (upsell imediato pós-compra: order bump + página de upsell — foco destes sprints)
CURSO R$ 197,00 · Método Mãos Seguras   ← a PRÁTICA GUIADA · 20 aulas, roteiros prontos, avatar aprovado
      ↓
MENTORIA 1:1 (R$ 197/sessão · aula A18)  →  NÍVEL II presencial (aula A20)  →  Comunidade Om Reiki Om
```

Tudo o que falta para o upsell existir e vender está coberto nos sprints abaixo. O gargalo histórico (avatar HeyGen) **já foi resolvido**, então o plano entra direto em produção em escala.

**Estado por fase (herdado do playbook):**

| Fase | Status |
|---|---|
| F0–F5 (e-book, briefing, diagramação, curso+roteiros, LP, verificação) | ✅ concluídas |
| Produto Eduzz e-book R$ 29,90 | ✅ publicado |
| **F6 — Videoaulas (produção)** | ⏭️ estes sprints (S1–S3) |
| **F7 — Montagem Nutror + trilhas de e-mail** | ⏭️ estes sprints (S4) |
| **Go-live do upsell + otimização** | ⏭️ estes sprints (S5–S6) |

---

## 2. Como os sprints funcionam

Cada sprint fecha em um **marco revisável** (não em uma data). Ritmo definido: *por marco, sem prazo fixo* — avançamos conforme sua disponibilidade de revisão e a velocidade de render no HeyGen.

**Divisão de trabalho (vale para todos os sprints):**

- **Só o Renato (HeyGen/plataforma):** colar roteiros no HeyGen, rodar prévia de voz, render final de cada aula, upload no Nutror, criação/edição de produtos e do fluxo de upsell na Eduzz, biometria/consentimento.
- **Claude pode fazer sem HeyGen:** slides de apoio (design v3, PNG/PDF), PDFs e planilhas de apoio, thumbnails, revisão fina dos roteiros, títulos e descrições das aulas, copy das trilhas de e-mail, checklists de QA, textos de página de vendas do curso.

**Texto de gravação (padrão travado):** o avatar HeyGen lê o script **na íntegra**, então o texto colado é **somente a fala** — pausas representadas por **pontuação** (. , … ? !), sem marcações `[PAUSA]`, sem `**negrito**`, sem cabeçalhos ou notas de cena. Fonte pronta em `curso/narracao/` (um `.txt` por aula, as 20 já geradas); versão anotada (com notas de cena/slides) fica em `curso/roteiros/`.

**Definição de Pronto (DoD) padrão por aula:** roteiro revisado → slides de apoio entregues → vídeo renderizado (`M{n}-A{k}-titulo.mp4`, 4–7 min) → **thumbnail/capa da aula (design v3)** → **PDF de apoio da aula** quando aplicável → conformidade OK (sem "milenar" → Mikao Usui **1922**; sem promessa de cura/renda; disclaimer PNPIC quando citar saúde) → subido na plataforma.

**Definição de Pronto (DoD) padrão por módulo:** **capa do módulo (banner)** + **thumbnails de todas as aulas** + **apresentação de apoio (slides do módulo em PDF)** + **material de apoio em PDF** (checklist/planilha/template conforme a grade) + descrições de aula. Nenhum módulo é considerado pronto sem: videoaulas **e** material de apoio em PDF **e** apresentação.

### Kit de personalização visual por módulo (Eduzz/Nutror)

Toda a área de membros usa o **design system v3** (roxo `#6A10AD` / ciano `#3FD8E8`, League Spartan / Playfair Display itálico / Inter, marcador ■), gerado pelo mesmo pipeline HTML/PNG do e-book. Cada módulo recebe, no mínimo:

| Artefato | Dimensão | Onde entra |
|---|---|---|
| Capa/banner do módulo | 1280×720 (16:9) | cabeçalho do módulo na Eduzz/Nutror |
| Thumbnail de cada aula | 1280×720 | miniatura do player de cada videoaula |
| Slides de apoio (B-roll na aula) | 1920×1080 | inseridos dentro do vídeo, entre blocos |
| Apresentação do módulo (PDF) | A4 paisagem | download do aluno (resumo visual) |
| Material de apoio (PDF) | A4 | download do aluno (checklist/planilha/template) |
| Capa do curso + banner de vendas | 1080×1080 / 1200×628 | vitrine Eduzz e página de vendas |

Além disso, na entrega final: **capa do curso** (produto Eduzz), **banner de vitrine/checkout** e **imagem de conclusão/certificado** (se o curso emitir). Todos versionados em `curso/design/` seguindo o padrão de `design/eduzz/`.

---

## 3. Os sprints

### Sprint 1 — Prova de conceito: M0 + M1 no ar (6 aulas)

**Marco:** primeiro módulo real assistível numa área de membros de teste — o avatar aprovado "conversando" com slides, do jeito que o aluno vai ver.

| Item | Responsável | Entregável |
|---|---|---|
| Slides de apoio A1–A6 (design v3, 1920×1080) | Claude | `curso/slides/M0/`, `curso/slides/M1/` |
| Render das 6 aulas (M0: A1–A2 · M1: A3–A6) | Renato (HeyGen) | 6 `.mp4` nomeados no padrão |
| **Capas dos módulos M0 e M1 + thumbnails das 6 aulas (design v3)** | Claude | `curso/design/M0/`, `curso/design/M1/` |
| **Apresentação de apoio de M0 e M1 (slides do módulo em PDF)** | Claude | `curso/apresentacoes/` |
| Materiais de apoio de M0–M1 (PDF) | Claude | Mapa da jornada (PDF), checklist "Estou me bloqueando ou evoluindo?", roteiro de autotratamento 5–10 min, tabela das 9 dificuldades. (Diário do Reikiano já existe.) |
| QA de conformidade das 6 aulas | Claude | mini-relatório no padrão da F5 |
| Shell do curso no Nutror (estrutura de módulos vazia) | Renato | curso criado, M0–M1 populados |

**Por que começar aqui:** valida ritmo de fala, naturalidade da voz, encaixe slide↔fala e o padrão de nomeação/entrega **antes** de escalar para 14 aulas. Ajustes de estilo descobertos aqui são aplicados nos roteiros seguintes.
**Dependências:** nenhuma (avatar aprovado). **Risco:** naturalidade das pausas `[PAUSA]` no HeyGen → mitiga-se na prévia de voz de A1.

---

### Sprint 2 — Núcleo de conversão: M2 + M3 (8 aulas)

**Marco:** os dois módulos que mais sustentam a promessa ("da prática gratuita ao primeiro cliente pago") prontos e no Nutror.

| Item | Responsável | Entregável |
|---|---|---|
| Slides A7–A14 (design v3, 1920×1080) | Claude | ✅ `curso/slides/M2/`, `curso/slides/M3/` |
| **Capas dos módulos M2 e M3 + thumbnails das 8 aulas** | Claude | ✅ `curso/design/M2/`, `curso/design/M3/` |
| Render das 8 aulas (M2: A7–A10 · M3: A11–A14) | Renato | 8 `.mp4` |
| Materiais de apoio | Claude | Templates de convite (WhatsApp), guia de voluntariado, planilha de registro de sessões, frases de transição, calculadora simples de preços/pacotes, templates de pedido de depoimento, modelo de oferta de lançamento |
| QA de conformidade (foco: precificação sem promessa de renda) | Claude | relatório |

**Por que M2–M3 antes de M4–M5:** é o coração da transformação vendida na página do curso; ter esses módulos prontos permite escrever a página de vendas com prova concreta. **Risco de conformidade elevado** (transição para pago) → revisão dupla.

---

### Sprint 3 — Fechamento do conteúdo: M4 + M5 (6 aulas) + kit de apoio completo

**Marco:** as 20 aulas renderizadas e todos os materiais de apoio finalizados. Curso 100% gravado.

| Item | Responsável | Entregável |
|---|---|---|
| Slides A15–A20 | Claude | `curso/slides/M4/`, `curso/slides/M5/` |
| Render das 6 aulas (M4: A15–A17 · M5: A18–A20) | Renato | 6 `.mp4` |
| Materiais de apoio finais | Claude | Guia de legislação/PNPIC (PDF), checklist "Profissionalizando meu Reiki", roteiro de apresentação profissional, convite de mentoria 1:1, Diário do Reikiano — Parte 3 |
| Thumbnails das 20 aulas (design v3) | Claude | `curso/thumbnails/` |
| QA final de conteúdo (todas as 20) | Claude | relatório consolidado |

**Conversão embutida:** A18 apresenta a **mentoria 1:1**; A20 faz a ponte para o **Nível II presencial** + comunidade. Confirmar que os CTAs falados batem com as ofertas reais (preços da memória oficial).

---

### Sprint 4 — Montagem do produto e trilhas de e-mail (F7)

**Marco:** curso montado no Nutror, produto criado na Eduzz e trilhas de e-mail prontas — pronto para vender, ainda sem tráfego.

| Item | Responsável | Entregável |
|---|---|---|
| Estrutura completa no Nutror (20 aulas + materiais + capas de módulo) | Renato | área de membros pronta |
| Produto "curso" na Eduzz (**R$ 197,00**) + **order bump** no checkout do e-book | Renato | ver §4 (order bump no checkout do e-book R$ 29,90) |
| **Página de upsell separada** (copy pronta) + HTML design v3 | Claude | ✅ **feita** — `landing-page/upsell.html` (+ `assets/`); copy canônica em `curso/upsell/pagina-upsell.md`. ⛔ **Não publicar antes do Sprint 5** |
| **Vídeo curto do Renato** — script pronto | Renato (grava) | ✅ **gravado e embutido** (2:01, fundo liso do avatar). Master em `artefatos/` (fora do git); web em `landing-page/assets/upsell-renato.mp4`; roteiro em `curso/narracao/UPSELL-video-renato.txt` |
| **Método Mãos Seguras** (mecanismo) + tabela e-book × curso | Claude | `curso/upsell/metodo-maos-seguras.md` ✅ |
| **4 bônus** (Checklist Sessão Segura, Roteiro de Conversa, Plano 21 Dias, Guia de Objeções) em PDF | Claude | `curso/upsell/bonus/` |
| **Kit visual do curso:** capa do produto (1080×1080), banner de vitrine/checkout (1200×628 e 1200×400), imagem de conclusão | Claude | `curso/design/` (padrão `design/eduzz/`) |
| 3 trilhas de e-mail por segmento (Praticante Pessoal / Aspirante a Terapeuta / Terapeuta em Transição) | Claude | `curso/email/` — sequências alinhadas ao `questionario-qualificacao.md` |
| **Rastreamento** de compra do e-book, upsell aceito e upsell recusado | Renato | pixels/eventos na Eduzz |
| Política de preço/garantia do curso (7 dias CDC) | Renato (decisão) | ✅ definida |

**Decisão travada (08/07/2026):** ticket do curso **R$ 197,00**, oferecido como **order bump** no checkout do e-book (R$ 29,90) e, no go-live, também como **página de upsell pós-compra**. Detalhe em §4.

---

### Sprint 5 — Go-live do upsell e primeiros compradores

**Marco:** upsell ativo e testado ponta a ponta; primeiros alunos do curso entrando pelo funil real.

| Item | Responsável | Entregável |
|---|---|---|
| Fluxo e-book → order bump / página de upsell testado (compra real ponta a ponta) | Renato + Claude | checklist de gate (nos moldes do gate da LP) |
| **Retirar o curso da lista de espera da LP** (§11 do `index.html`) e apontar o e-book (página "Próximo passo") para a oferta real | Claude | edição da LP no ar + PDF do e-book |
| Sequência de lançamento para a base | Claude | e-mails + roteiro de stories/posts (skills `copy-reiki` + `codigo-de-conteudo`) |
| Painel de acompanhamento (vendas e-book, take-rate do upsell, upsell recusado, conclusão de módulos) | Claude | artefato/planilha de KPIs |

**KPIs a observar:** take-rate do upsell (meta inicial de referência a definir), taxa de conclusão M0→M1 (indicador de engajamento), conversão da lista de espera, e progressão curso → mentoria → Nível II.

---

### Sprint 6 — Otimização e expansão do ecossistema (contínuo)

**Marco:** ciclo de melhoria rodando com base em dados reais.

Ajuste de página de vendas e trilhas conforme dados; testes A/B de headline/preço; **downsell na recusa** (mini-aula prática R$ 47–67, recorte do Método Mãos Seguras); **one-click upsell pós-compra** (além do order bump); captação de depoimentos de alunos do curso (método Groq Whisper já documentado); ativação estruturada da **mentoria 1:1** (A18) e da ponte **Nível II** (A20); avaliação de novos degraus (comunidade recorrente / assinatura). Também: aplicar o ajuste anti-duplicação pendente na triagem n8n (playbook §2) quando você autorizar.

---

## 4. Mecânica do upsell (recomendação)

O e-book é o *tripwire*; o curso é o degrau de maior margem. Duas formas na Eduzz, não excludentes:

1. **Order bump no checkout do e-book** — oferta do curso com desconto marcada como caixa no próprio checkout (conversão de impulso, ticket combinado). Simples e imediata.
2. **Upsell pós-compra (one-click)** — após pagar o e-book, o comprador vê uma oferta do curso em 1 clique. Historicamente converte bem porque o cartão já foi usado.

**Decisão (08/07/2026):** o curso sai a **R$ 197,00**, ofertado como **order bump** no checkout do e-book (R$ 29,90) — menos setup e conversão de impulso, com ticket combinado de R$ 226,90. No **Sprint 6**, testar adicionalmente o **one-click upsell pós-compra**. Regra travada do playbook mantida: **na LP, a oferta herói continua sendo só o e-book** — o curso não compete na primeira dobra; aparece como próximo passo (LP §11, página "Próximo passo" do e-book e trilha de e-mail).

**Implicação para os artefatos:** todas as peças de preço do curso (página de vendas, banners, copy das trilhas, order bump na Eduzz) usam **R$ 197,00** — valor oficial, não estimativa.

### 4.1 Auditoria do upsell — mudanças obrigatórias (08/07/2026)

Uma auditoria do funil aprovou o upsell **com alterações obrigatórias**. Todas incorporadas aqui e nos artefatos de `curso/upsell/`:

1. **Separar os papéis** — e-book = **mapa** (destravar/consultar); curso = **prática guiada** (praticar/ganhar segurança); bônus = **ferramentas de aplicação**. Nunca vender o curso como "versão maior do e-book". Tabela comparativa obrigatória em toda peça (`metodo-maos-seguras.md`).
2. **Nomear o mecanismo único** — **Método Mãos Seguras** (6 passos: Preparar · Centralizar · Conduzir · Encerrar · Registrar · Evoluir). Resolve a nota 5/10 de "mecanismo" da auditoria. Recomendado inserir o nome do método nos roteiros ainda não gravados (A1, A4–A5, fim do M2).
3. **Vender como prática guiada, não conteúdo extra** — demonstração, segurança, sequência, acompanhamento, clareza. A nova objeção a vencer é **"vou conseguir aplicar sozinho?"** (não mais "isso é para mim?").
4. **Upsell imediato pós-compra** — o curso aparece **logo após a compra** do e-book (order bump + página de upsell), quando o comprador está mais quente. **Retirar o curso da "lista de espera" da LP inicial** (`landing-page/index.html` §11): não faz sentido colocar em espera algo que já será vendido a R$ 197 no ato.
5. **Página de upsell separada + vídeo curto** — não misturar com a LP do e-book; incluir vídeo de 3–6 min do Renato explicando a diferença entre ler e praticar guiado.
6. **Tom de próximo passo opcional** — "Seu e-book está garantido. Agora existe um próximo passo opcional." Nunca "sua compra ainda não acabou". Entregar o e-book **mesmo se recusar** o upsell.
7. **Downsell na recusa** — mini-aula prática por **R$ 47–67**, mas só depois de validar o funil principal (Sprint 6).
8. **Ancoragem honesta** — "menos que um atendimento individual ou curso presencial"; **evitar** "vale R$ 1.997" (soa artificial para este público). Urgência real, sem falsa escassez.
9. **Rastreamento e claims** — medir compra / upsell aceito / upsell recusado; revisar claims (sem cura, renda ou resultado garantido; Mikao Usui 1922; disclaimer PNPIC).

**Status do gate (auditoria):** aprovado para copy e implementação. Bloqueadores antes de publicar listados em `curso/upsell/pagina-upsell.md` (notas de implementação).

---

## 5. Dependências e pendências suas (fora do meu alcance)

- **HeyGen:** render das aulas (avatar já aprovado ✅).
- **Nutror:** criar curso e subir aulas/materiais.
- **Eduzz:** criar o produto do curso e configurar a mecânica de upsell.
- **Decisões:** ✅ ticket R$ 197,00 e order bump (definidos 08/07/2026). Ainda: confirmar preços da mentoria/Nível II citados em A18/A20 contra a memória oficial.
- **Autorização:** ajuste anti-duplicação no workflow de triagem n8n (produção).

---

## 6. Próximo passo imediato

Já estou executando o **Sprint 1**: produzindo os **slides de apoio de M0 + M1** (design v3). Com eles entregues, você já pode colar os roteiros no HeyGen e renderizar as 6 primeiras aulas — a prova de conceito do curso.
