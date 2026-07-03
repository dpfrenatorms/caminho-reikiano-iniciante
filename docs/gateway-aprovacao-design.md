# 🚦 Gateway de Aprovação — Design (LP + Kit Eduzz)

> Portão de sign-off do **design** das peças da F4, feito com o framework `/design-critique` + design system `design-reiki` (v3) + WCAG AA (contraste medido).
> **Data da auditoria:** 2026-07-03 · **Auditor:** Claude (Cowork) · **Aprovador:** Renato Menezes
> Este gate é sobre **qualidade de design**. O gate de **deploy** (checkout, push, conformidade) continua sendo o §10 do spec F4 e o §5 do playbook — os dois precisam estar verdes para publicar.

---

## Veredito da auditoria

| Peça | Estado |
|---|---|
| **Landing page** (`landing-page/index.html`) | 🟡 **APROVADA COM 1 BLOQUEIO** — design pronto; bloqueio técnico das imagens (raw GitHub 404 até push) |
| **Kit Eduzz** (`design/eduzz/*.png`) | 🟢 **APROVADO** — sem pendências de design (PNGs baked, sem 404) |

**Score de acessibilidade (WCAG AA, contraste):** 15/16 pares PASS → **16/16 após o fix do `.wl-note`** (aplicado nesta sessão).

---

## Portão 1 — Landing page

| # | Critério de design | Status | Nota |
|---|---|---|---|
| 1 | Hierarquia AIDA (eyebrow→dor→oferta→preço→CTA) | ✅ | 1ª dobra completa |
| 2 | CTA primário único (compra R$ 29,90); lista de espera secundária | ✅ | 4 CTAs → checkout; form discreto |
| 3 | Mobile que vende (sticky CTA, alvos ≥44px, blocos curtos) | ✅ | validado em 375px |
| 4 | Fidelidade ao design system v3 (tokens, tipografia, ■) | ✅ | idêntico à capa/e-book |
| 5 | Contraste WCAG AA em todos os textos | ✅ | após fix `.wl-note` (#6a5d7c) |
| 6 | **Imagens carregam** (hero, foto autor) | ⛔ **BLOQUEIO** | raw GitHub 404 até push do `a9a1019` |
| 7 | Estados do form (sucesso/erro + fallback WhatsApp) | ✅ | testado |

**Ação para destravar o item 6 (escolher 1):**
- **A (recomendada):** Renato dá push do `a9a1019` → raw GitHub passa a servir as imagens. Zero mudança de código.
- **B (contingência):** embutir localmente os PNGs (ex.: usar `design/eduzz/mockup-ebook-3d.png` no hero) ou base64 — a LP deixa de depender do push. Claude executa em ~10 min se autorizado.

---

## Portão 2 — Kit Eduzz

| # | Critério de design | Status | Nota |
|---|---|---|---|
| 1 | Capa fiel ao e-book v3 (título ciano, logo, créditos) | ✅ | `capa-ebook.png` |
| 2 | Mockup 3D legível e profissional | ✅ | `mockup-ebook-3d.png` (transparente) |
| 3 | Imagem quadrada com hierarquia de venda + preço | ✅ | `produto-quadrado-1080.png` |
| 4 | Banners (social 1200×628 · checkout 1200×400) | ✅ | leves, on-brand |
| 5 | Elementos de marca (@reiki.brasilia, logo, credenciais) | ✅ | presentes |
| 6 | Conformidade de copy nas peças (sem "milenar"/cura/renda) | ✅ | ver F5 |
| 7 | Sem dependência de rede (PNG baked) | ✅ | não sofre o 404 da LP |

**Refinos opcionais (não bloqueiam):**
- Banner social: empilhar "de ~~R$97~~ · pagamento único" abaixo do preço (respiro).
- Capa: metade inferior tem respiro amplo (herdado do e-book) — manter para continuidade.

---

## Decisão do aprovador

> Preencher e commitar (ou responder no chat).

- [ ] **APROVO o design** das duas peças e autorizo seguir para o gate de deploy (§10).
- [ ] Item 6 do Portão 1 será resolvido por: [ ] **A (push)**  [ ] **B (embutir local)**.
- [ ] Refinos opcionais: [ ] aplicar  [ ] dispensar.
- [ ] Reprovo / peço ajustes: _(descrever)_

**Assinatura:** ______________________  **Data:** ____/____/______

---

## Rastreabilidade

- Critérios de design: `design-critique` (framework) + `design-reiki` (design system v3)
- Contraste: WCAG 2.1 AA (4.5:1 normal · 3:1 grande) — cálculo relativo de luminância
- Gate de deploy relacionado: spec F4 §10 · playbook §5
- Verificação de conteúdo/conformidade: `docs/relatorio-verificacao.md` (F5)
