# F5 — Relatório de Verificação de Coerência

**Projeto:** O Caminho do Reikiano Iniciante — ecossistema digital
**Fase:** F5 (verificação de coerência) do `PLANO-EXECUCAO.md`
**Data:** 2026-07-03 · **Autor:** Claude (Cowork)
**Escopo:** e-book (v3), curso (grade + roteiros M0–M5), landing page (index.html + copy.md + questionário)
**Veredito geral:** ✅ **APROVADO** — nenhum bloqueador de conformidade encontrado. 2 recomendações de baixa severidade (opcionais) + os bloqueadores de deploy já conhecidos (pendências do Renato).

---

## 1. Método

Varredura automatizada (grep) + leitura cruzada dos artefatos voltados ao cliente:
`design/canva-import/ebook-diagramado-v3.html`, `curso/grade-curricular.md`, `curso/roteiros/M0–M5.md`,
`landing-page/index.html`, `landing-page/copy.md`, `landing-page/questionario-qualificacao.md`.
Referência de preços/contatos: `REIKI-CURSOS-MEMORIA.md` e regras de marca (`PLANO-EXECUCAO.md` §conformidade).

---

## 2. Conformidade de marca e saúde

| Regra | Resultado |
|---|---|
| **"milenar" nunca no conteúdo do cliente** | ✅ Zero ocorrências em e-book/curso/LP. Só aparece em docs de regra (playbook/spec/plano), como proibição. |
| **Reiki = "criado por Mikao Usui em 1922"** | ✅ LP (rodapé) e `copy.md` afirmam **"Mikao Usui em 1922"**. ⚠️ ver Recomendação R1 (e-book omite o ano). |
| **Sem promessa de cura** | ✅ Todas as menções a "cura/curar" na LP estão em **negação/objeção**: "Reiki cura doenças? **Não**…", "promessa de cura instantânea" (na coluna do "não é para você"). E-book Cap. 2: "não é seu papel curar ninguém". |
| **Sem promessa de renda/resultado garantido** | ✅ "renda", "ficar rico", "resultado garantido" só aparecem **negados**: disclaimer "não é promessa de renda ou resultado garantido"; "ficar rico da noite para o dia" está na lista do que a oferta **não** é. |
| **Disclaimer PNPIC no rodapé** | ✅ Presente no `index.html` (§12) e `copy.md`: caráter educacional, não substitui tratamento médico/psicológico, orientar manutenção do tratamento convencional. |
| **Depoimentos éticos** | ✅ 4 reais e atribuíveis, enquadrados como "alunos do Mestre Renato sobre a jornada com o Reiki" (não sobre o e-book). Fala da Rafaela (ansiedade) acompanhada do disclaimer. ⚠️ ver Recomendação R2 (consentimento LGPD). |

---

## 3. Coerência de preços

| Item | Valor | Onde | Coerência |
|---|---|---|---|
| **E-book (oferta principal)** | **R$ 29,90** | LP (23 ocorrências, todos os CTAs) | ✅ único e consistente |
| Âncora de valor | ~~R$ 97~~ | LP §7 (riscado) | ✅ apenas ancoragem visual |
| **Curso (upsell)** | **R$ 197** | LP §4 nota + curso/roteiros | ✅ bate com `curso/` |
| Faixas de investimento (Q7) | R$ 197 / 297 / 497 | LP questionário | ✅ coerente (pesquisa de disposição) |
| Nível I presencial | R$ 129,90 | `REIKI-CURSOS-MEMORIA.md` | ✅ **não citado** na LP (correto — evita competir com a oferta) |
| Exemplos de sessão | R$ 80–450 | e-book Cap. 4 | ✅ **didáticos** (exemplos de precificação de atendimento), não conflitam com preços de produto |

**Sem conflitos de preço.**

---

## 4. Voz e consistência editorial

- ✅ **Assinatura idêntica** e-book ↔ LP: *"Boa jornada. Estarei com você em cada capítulo."* — reforça continuidade de marca.
- ✅ **Léxico da marca** ecoa entre as peças: "sintonização", "canal", "e agora?", "certificado na gaveta", "de dentro para fora".
- ✅ **Tom** acolhedor + respaldo técnico, uniforme nas três peças.
- ✅ **Títulos dos 7 capítulos** na LP §3 batem 1:1 com os openers do e-book v3.
- ℹ️ **Bio "27 anos"**: a LP espelha fielmente o e-book (27 anos de Reiki desde 1998 **e** 27 anos como Delegado Federal). É a redação da fonte; coerente, embora a coincidência dos dois "27" possa ser revista editorialmente no futuro (não-bloqueador).

---

## 5. Links, CTAs e contatos

- ✅ **Hierarquia de CTA:** os 4 CTAs primários (hero, oferta, CTA final, sticky mobile) apontam todos para a **compra do e-book R$ 29,90** via `data-checkout`. Lista de espera é botão **secundário** (contorno), não compete.
- ✅ **Contatos** batem com a memória global: `@reiki.brasilia`, `wa.me/5561983097777` = (61) 98309-7777, `reikibrasilia.br.com`, `brasiliareiki@gmail.com`.
- ✅ **Webhook real** embutido no form: `https://reikibrasilia.app.n8n.cloud/webhook/reiki-lista-espera` (validado na F4).
- ✅ **Fallback de erro** do form → link WhatsApp correto.

---

## 6. Varredura anti-IA

- ✅ Sem `lorem`, `TODO`, `FIXME`, "as an AI", "language model", `[nome]`, `[inserir…]`.
- ✅ Únicos placeholders presentes são **intencionais e documentados**: `COLE_EDUZZ_29_90` (checkout, gate item 1) e os `placeholder=""` nativos dos inputs do form.
- ✅ Sem construções genéricas de IA; texto na voz da marca.

---

## 7. Recomendações (baixa severidade — opcionais)

**R1 · Coerência do "1922" no e-book (LOW).**
O e-book v3 descreve o Reiki como *"técnica japonesa de cura natural criada por Mikao Usui"* (págs. 03 e 63) **sem o ano** — enquanto a LP e o plano de marca cravam *"Mikao Usui em 1922"*. Não há data errada (não é contradição), mas, para coerência total, sugere-se numa v3.1 do e-book acrescentar *"em 1922"*. A expressão *"cura natural"* é o nome tradicional da modalidade (Reiki = "cura natural"), aceitável com o disclaimer PNPIC já presente; se desejar cautela máxima em ads, considerar *"harmonização energética"*.

**R2 · Consentimento dos depoimentos (LGPD) (LOW/processo).**
Antes do deploy, confirmar autorização de uso de nome/depoimento das 4 alunas (Ana Lúcia, Daiane Neves, Lorena, Rafaela Lehmann). Boa prática legal; não altera o código.

---

## 8. Itens em aberto (bloqueadores de deploy — já conhecidos, fora do meu alcance)

Estes **não** são falhas de coerência; são as pendências do gate §10 da spec F4:

1. ⛔ **Checkout Eduzz real** (`CHECKOUT_URL` / `data-checkout="COLE_EDUZZ_29_90"`) — pendência do Renato.
2. ⛔ **Push do commit `a9a1019`** — sem ele, as imagens (raw GitHub) dão 404 e o hero/mockup/foto quebram. Pendência do Renato.
3. ℹ️ Ajuste anti-duplicação na triagem Gmail (`-subject:"LISTA-ESPERA"`) — aguarda OK do Renato.

---

## 9. Conclusão

O ecossistema (e-book · curso · landing page) está **coerente em voz, preços, claims e conformidade**. A landing page está **pronta para deploy assim que os bloqueadores do gate §10 forem resolvidos pelo Renato** (checkout Eduzz + push das imagens). As recomendações R1 e R2 são melhorias opcionais e não impedem a publicação.

**Handoff:** com a F5 aprovada, o projeto está com todo o build concluído (F0–F5). Restam apenas as ações do Renato para colocar a LP no ar.
