# Changelog Editorial — E-book v2 (Fase F1)

**Base:** `ebook/original/EBOOK - O CAMINHO DO REIKIANO INICIANTE.docx` (~10.300 palavras)
**Resultado:** `ebook/manuscrito-v2.md` (fonte editorial) + `ebook/O Caminho do Reikiano Iniciante - v2.docx` (~10.170 palavras, 43 páginas)
**Data:** 02/07/2026

## 1. Vestígios de IA removidos (varredura 100%)

| Local | Trecho removido |
|---|---|
| Fim da Introdução | "Se quiser, posso também criar uma versão dessa introdução em áudio... É só pedir." |
| Fim do Cap. 1 | "Quer que eu crie uma sequência de 7 dias com práticas guiadas...? É só pedir." |
| Fim do Cap. 2 | "Se quiser, posso transformar tudo isso em um mini e-book bônus... É só me pedir." |
| Fim do Cap. 3 | "Quer que eu crie agora um roteiro de captação... É só pedir." |
| Fim do Cap. 5 | "Deseja que eu crie um modelo de plano de ação...? É só dizer." |
| Cap. 6 | "(Se quiser, substituo por link do Calendly ou crio o texto para uma página de captura.)" |
| Cap. 7 (2 ocorrências) | "Se quiser, posso criar um modelo de diário pessoal..." e "Se quiser, posso complementar este capítulo com um modelo de diário guiado... Me avise se desejar incluir esse recurso." |

**Verificação automatizada final:** zero ocorrências dos padrões "se quiser, posso", "é só pedir", "me avise se", nomes de assistentes/IA, e zero emojis no corpo do texto.

## 2. Placeholders resolvidos

- `[SEU LINK AQUI]` (Cap. 6) → substituído pelos contatos reais: WhatsApp (61) 98309-7777, @reiki.brasilia, reikibrasilia.br.com (fonte: memória oficial dos cursos).
- `[nome]` e `[seu nome]` mantidos apenas dentro de modelos de mensagem claramente sinalizados como templates para o leitor adaptar (Caps. 3, 4 e 5), reescritos como `[nome da pessoa]` / `[seu nome]`.

## 3. Mudanças estruturais

- **Novo título:** "O Caminho do Reikiano Iniciante — Da primeira aplicação ao primeiro cliente" (antes: "Como se Tornar um Reikiano de Sucesso — ...Cliente Pago"). Promessa preservada, tom menos "guru".
- **Bio do autor:** abertura reduzida a "Boas-vindas do autor" (½ página, em 1ª pessoa); bio completa movida para "Sobre o autor" ao final, com contatos.
- **Página de créditos criada** com copyright e disclaimer de prática integrativa (PNPIC) — "não substitui diagnóstico, tratamento ou acompanhamento médico e psicológico".
- **Novo ANEXO — O Diário do Reikiano:** cumpre a promessa órfã do texto original (modelo de diário guiado). 4 partes: registro de prática diária, registro de atendimentos, "escrevendo a minha história" (5 passos do Cap. 7) e desafio dos 21 dias.
- **Nova seção "O Próximo Passo da Sua Jornada":** CTA para lista de espera do curso online + ponte para os cursos presenciais Nível I–III.
- **Sumário automático** adicionado ao docx (atualiza ao abrir no Word).

## 4. Ajustes de conformidade e precisão

- Citação de abertura do Cap. 6: atribuição a "Lao Tzu" trocada por "provérbio de sabedoria oriental" (atribuição original não verificável).
- Cap. 7: "Segundo os ensinamentos do Dr. Augusto Cury" → "Inspirando-se no conceito popularizado pelo psiquiatra e escritor Augusto Cury" (paráfrase, não citação literal).
- Cap. 5 (base legal): mantidas PNPIC e Portaria 849/2017 (inclusão do Reiki em 2017 — correto); referência específica ao "COREN-SP" generalizada para "conselhos regionais... verifique as normas do conselho da sua categoria e da sua região"; exemplo municipal específico não verificável removido; adicionada nota "as normas variam conforme estado e município".
- Cap. 5: lista de práticas de expansão enxugada (removidas menções promocionais a ThetaHealing, barras de access e constelação como lista de compras; mantida orientação genérica "outras vertentes e práticas complementares, com formação séria").
- Cap. 4: valores monetários sinalizados como **exemplos didáticos** com orientação de pesquisa regional; escassez condicionada a ser verdadeira ("somente se for real"); removida promessa implícita de resultado financeiro ("está pronto para começar sua jornada profissional" → "tem o essencial para dar os primeiros passos... no seu ritmo").
- Introdução: "nível 1, 2 ou mesmo o 3A" → "Nível I, II ou III" (alinhado à nomenclatura do Sistema Usui usada pela marca).
- Cap. 1: uso de símbolos condicionado ao Nível II ("quando os símbolos são transmitidos") — evita confundir o leitor de Nível I.
- Grafia padronizada: "Cho-Ku-Rei" (antes alternava com "Chokurei"); "à distância" → "a distância"; aspas e travessões padronizados.
- Linguagem de "cura": ajustada para "equilíbrio/bem-estar/apoio ao processo" em afirmações sobre efeito em terceiros; mantido vocabulário tradicional do Reiki (autocura, cura natural) em contexto histórico-conceitual.

## 5. Estilo e fluidez

- Remoção de todos os emojis do corpo e títulos (hierarquia visual passa para a diagramação — F2).
- Correções gramaticais e de pontuação em todo o texto; frases robóticas reescritas em tom acolhedor e humano.
- Formato "dificuldade → o que está acontecendo → como superar" padronizado no Cap. 2; capítulos 4 e 5 reorganizados com hierarquia consistente de seções.
- Caixas de bônus dos capítulos ("materiais para aplicar este capítulo") unificadas e apontando para o Diário do Reikiano.

## Commit sugerido

```
feat(ebook): manuscrito v2 revisado + docx + changelog editorial
```
