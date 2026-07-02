# Memória do Projeto — Sessão 02/07/2026

> **ATUALIZAÇÃO (fim da sessão):** F2, F2b e F3 também foram concluídas. Ver seção "Atualização final da sessão" ao fim deste documento.

> Documento de memória persistente do projeto **Caminho do Reikiano Iniciante**. Serve como contexto de retomada para qualquer sessão futura do Claude/Cowork e como fonte para importação no Mem0 (seção "Aprendizados para o Mem0" ao final).

## Estado do projeto

**Projeto:** transformar o e-book base de Reiki em ecossistema digital completo (e-book revisado → diagramação → curso upsell → landing page com captação).
**Plano mestre:** `PLANO-EXECUCAO.md` (aprovado formalmente por Renato em 02/07/2026).
**Repositório:** https://github.com/dpfrenatorms/caminho-reikiano-iniciante.git (vazio; push a cargo do Renato — ver `docs/versionamento.md`).

| Fase | Status | Entregáveis |
|---|---|---|
| F0 — Setup | ✅ Concluída | Estrutura de pastas, .gitignore, guia de versionamento |
| F1 — Revisão editorial | ✅ Concluída | `ebook/manuscrito-v2.md`, `ebook/O Caminho do Reikiano Iniciante - v2.docx` (43 págs.), `docs/changelog-ebook.md` |
| F2 — Briefing diagramação Canva | ⏳ Próxima | `design/briefing-diagramacao-canva.md` |
| F3 — Curso + roteiros avatar | Pendente | Grade 6 módulos / ~20 aulas |
| F4 — Landing page | Pendente | Copy + HTML + questionário de qualificação |
| F5 — Verificação de coerência | Pendente | Relatório final |

## Decisões aprovadas

1. E-book = produto de entrada (tripwire) **R$ 29,90–47**.
2. Curso upsell = **compacto**, 6 módulos (M0–M5), ~20 aulas de avatar de 5–8 min, **R$ 197–297**.
3. Título oficial: **"O Caminho do Reikiano Iniciante — Da primeira aplicação ao primeiro cliente"**.
4. Landing page = copy completa + **HTML pronto** no design system da marca.
5. Insight JTBD central: o público do e-book é o **reikiano recém-iniciado** (não a persona Ana Carolina) → cria o Funil 2 da marca: pós-Nível I → e-book → curso → Nível II presencial → Mestrado.

## Pendências abertas (não bloqueantes)

- Depoimentos reais de alunos (necessários antes da F4);
- Fotos do Renato em alta resolução (F2 e F4);
- Definição da política de garantia (7 dias CDC ou estendida);
- Ferramenta do avatar de IA (HeyGen, Synthesia etc.) — define formatação dos roteiros na F3;
- Ferramenta de captura da lista de espera (Eduzz? e-mail?);
- Push do commit inicial no GitHub (Renato) ou token de acesso para o Claude versionar.

## Aprendizados técnicos da sessão

1. **Git não funciona no mount do Cowork** (filesystem não suporta locks/renames do git; `.git/config` fica corrompido/invisível). Solução adotada: repo local do Renato + guia em `docs/versionamento.md`. Não tentar `git init` no mount novamente.
2. **Exclusão de arquivos no mount** requer permissão via `allow_cowork_file_delete` (já concedida para esta pasta).
3. **Pipeline docx validado:** manuscrito em markdown → script Node (docx-js) com identidade da marca (Georgia + Segoe UI, violeta #3A145F/#200C3C, dourado) → verificação visual via LibreOffice/pdftoppm. Script em `outputs/build-ebook-docx.js` (sandbox; recriar se necessário). O TOC aparece vazio no preview LibreOffice, mas atualiza ao abrir no Word.
4. **npm install** precisa rodar fora do mount (ex.: /tmp/build) — o script deve ser copiado para lá antes de executar.

## Aprendizados editoriais (padrões da marca aplicados)

- O texto base continha 8 vestígios de chat de IA ("Se quiser, posso...") — todos removidos; varredura automatizada com padrões documentados no `docs/changelog-ebook.md`.
- Atribuições de citação não verificáveis foram generalizadas ("Lao Tzu" → "provérbio de sabedoria oriental"; Augusto Cury → "inspirado no conceito popularizado por").
- Nunca usar "milenar" para o Reiki (regra da marca: "criada por Mikao Usui em 1922"); claims de saúde sempre com disclaimer PNPIC; valores monetários no conteúdo = exemplos didáticos.
- Contatos oficiais (fonte: memória oficial dos cursos): WhatsApp (61) 98309-7777 · @reiki.brasilia · reikibrasilia.br.com · brasiliareiki@gmail.com · Nível I R$ 129,90, turma 14/06/2026, Vista Shopping, Águas Claras.

## Aprendizados para o Mem0 (importar quando conectado)

Cada linha abaixo é uma memória atômica pronta para `add_memory`:

1. Renato aprovou o plano do ecossistema "O Caminho do Reikiano Iniciante" em 02/07/2026: e-book tripwire R$ 29,90–47, curso compacto R$ 197–297, LP com copy + HTML.
2. O público do e-book "O Caminho do Reikiano Iniciante" é o reikiano recém-iniciado (segundo funil da marca), não a persona Ana Carolina.
3. F0 e F1 do projeto estão concluídas; a próxima fase é F2 (briefing de diagramação Canva).
4. Git não funciona dentro da pasta montada do Cowork; o versionamento é feito pelo Renato localmente conforme docs/versionamento.md.
5. O e-book v2 revisado tem 43 páginas, zero vestígios de IA e um novo anexo "Diário do Reikiano"; changelog completo em docs/changelog-ebook.md.
6. Pendências do projeto: depoimentos de alunos, fotos em alta resolução, política de garantia, ferramenta de avatar de IA e ferramenta de lista de espera.

---

# Atualização final da sessão (02/07/2026)

## Fases concluídas nesta sessão (estado final)

| Fase | Status | Entregáveis |
|---|---|---|
| F0 — Setup | ✅ | Estrutura de pastas, guia `docs/versionamento.md`; **push inicial feito pelo Renato** (commit `f578acb` + fix dos fundos) |
| F1 — Revisão editorial | ✅ | `ebook/manuscrito-v2.md` + docx 43 págs. + `docs/changelog-ebook.md` |
| F2 — Briefing Canva | ✅ | `design/briefing-diagramacao-canva.md` |
| F2b — Diagramação no Canva | ✅ | `design/canva-import/ebook-diagramado.html` (65 págs.) + `bg-cover.png`/`bg-opener.png`; **design editável no Canva: "O Caminho do Reikiano Iniciante — E-book Diagramado v2"**, ID `DAHONIm4LZI`, edição: canva.com/d/4sl0pMwvXZfbPww (o design v1 `DAHONMizHxs` pode ser excluído) |
| F3 — Curso + roteiros | ✅ | `curso/grade-curricular.md` (6 módulos, 20 aulas) + `curso/roteiros/M0.md`–`M5.md` (~7.800 palavras, formato HeyGen com [PAUSA]) |
| F4 — Landing page | ⏸️ Pausada | **Aguardando Renato separar os depoimentos reais de alunos** |
| F5 — Verificação | Pendente | Após F4 |

## Decisões novas desta sessão

- **Ferramenta de avatar: HeyGen** (roteiros formatados com marcações [PAUSA] e negrito de ênfase — validar na prévia de voz).
- Diagramação via Rota A: HTML fiel gerado por código → GitHub raw → `import-design-from-url` do conector Canva. Fundos violeta precisam ser **PNG** (o importador do Canva descarta degradês CSS de fundo).
- Mem0 conectado e funcionando: 6 memórias do projeto gravadas (user_id `renato`, metadata projeto `caminho-reikiano-iniciante`).

## Aprendizados técnicos novos

1. O importador do Canva converte texto HTML em elementos editáveis com fidelidade, mas **ignora backgrounds CSS (degradês)** — usar `<img>` PNG full-bleed em páginas escuras.
2. O conector Mem0 carregou no meio da sessão (tools aparecem após conexão, sem precisar de conversa nova — pode demorar alguns minutos).
3. Push do Renato requer: `git config --global user.email/name` (feito) e execução dentro da pasta do projeto.
4. Elementos com `position:absolute` no HTML podem ser reposicionados pelo importador do Canva (ex.: linha da marca na capa subiu) — ajustar manualmente no editor.

## Retomada (próxima sessão)

1. Renato entrega os **depoimentos reais** (+ definir garantia: 7 dias CDC ou estendida; + ferramenta de captura da lista de espera).
2. Executar **F4**: `landing-page/copy.md` + `index.html` (design system) + `questionario-qualificacao.md` (7 perguntas, 3 segmentos).
3. Executar **F5**: verificação cruzada de coerência (tom, preços vs. memória oficial, claims, links).
4. Ajustes manuais no Canva pendentes: posição da linha de marca na capa, foto real do autor, excluir design v1.
5. Commits sugeridos pendentes: `feat(curso): grade curricular + roteiros heygen` e `docs: memoria da sessao atualizada`.
