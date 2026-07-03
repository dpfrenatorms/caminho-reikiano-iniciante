# Questionário de Qualificação — Lista de Espera do Curso

> Seção 11 da LP (secundária). 7 perguntas → 3 segmentos → 3 trilhas de e-mail.
> A LP é "burra": envia as respostas cruas ao webhook n8n; **a segmentação é calculada no nó Code** do workflow `Reiki — Lista de Espera Reikiano` (id `etum7cA1SJRHIk7R`).
> Contrato de payload = spec F4 §6. Este doc é a fonte da verdade das opções (`value`) de cada campo.

---

## As 7 perguntas

Todas obrigatórias. `radio`/`select`. O `value` (chave) vai no payload; o rótulo é o texto exibido.

### Q1 — Em que momento do Reiki você está? `q1_momento_reiki`
| value | Rótulo |
|---|---|
| `nunca_iniciei` | Ainda não me iniciei |
| `nivel_1` | Sou iniciado(a) no Nível I |
| `nivel_2_mais` | Tenho Nível II ou III |
| `mestre` | Sou Mestre(a) |

### Q2 — Há quanto tempo você se iniciou? `q2_tempo_iniciacao`
| value | Rótulo |
|---|---|
| `menos_6_meses` | Menos de 6 meses |
| `6_a_12_meses` | De 6 a 12 meses |
| `1_a_3_anos` | De 1 a 3 anos |
| `mais_3_anos` | Mais de 3 anos |

### Q3 — Com que frequência você pratica hoje? `q3_frequencia`
| value | Rótulo |
|---|---|
| `diaria` | Diariamente |
| `semanal` | Algumas vezes por semana |
| `raramente` | Raramente |
| `parei` | Parei de praticar |

### Q4 — Qual sua maior dificuldade hoje? `q4_maior_dificuldade`
| value | Rótulo |
|---|---|
| `inseguranca` | Insegurança para aplicar |
| `sentir_energia` | Sentir a energia fluir |
| `conseguir_pessoas` | Conseguir pessoas para atender |
| `medo_cobrar` | Medo ou culpa de cobrar |
| `aspectos_legais` | Aspectos legais / registro |

### Q5 — Qual seu objetivo com o Reiki? `q5_objetivo`
| value | Rótulo |
|---|---|
| `uso_pessoal` | Uso pessoal / autocuidado |
| `familia_amigos` | Atender família e amigos |
| `profissional` | Atuar profissionalmente |
| `viver_de_reiki` | Viver de Reiki |

### Q6 — Você já atendeu outras pessoas? `q6_ja_atendeu`
| value | Rótulo |
|---|---|
| `sim_gratis` | Sim, gratuitamente |
| `sim_pago` | Sim, e já cobrei |
| `ainda_nao` | Ainda não |

### Q7 — Quanto você investiria num programa completo? `q7_investimento`
| value | Rótulo |
|---|---|
| `ate_197` | Até R$ 197 |
| `de_197_a_297` | De R$ 197 a R$ 297 |
| `de_297_a_497` | De R$ 297 a R$ 497 |
| `acima_497` | Acima de R$ 497 |

---

## Segmentação (calculada no nó Code do n8n)

Prioridade de cima para baixo — a primeira condição verdadeira define o segmento.

| Segmento | Condição | Trilha |
|---|---|---|
| **Terapeuta em Transição** | `q6 = sim_pago` **ou** `q5 = viver_de_reiki` | curso + mentoria |
| **Aspirante a Terapeuta** | `q5 ∈ {profissional, viver_de_reiki}` **ou** `q4 ∈ {conseguir_pessoas, medo_cobrar, aspectos_legais}` | curso |
| **Praticante Pessoal** | demais casos (`q5 ∈ {uso_pessoal, familia_amigos}`) | nutrição |

> Nota: `viver_de_reiki` aparece em dois níveis; a prioridade garante que quem já cobrou (`sim_pago`) caia em "Transição" mesmo que também marque `viver_de_reiki`.

---

## Trilhas de e-mail (roteiro editorial — para automação futura)

### Trilha A — Praticante Pessoal (nutrição)
Tom: acolhimento, autocuidado, sem pressão comercial.
1. **Boas-vindas** — "Que bom te ter na lista 🌸" + mini-guia de autotratamento de 5 min.
2. **Valor** — como manter uma rotina de Reiki mesmo na correria (Cap. 1 do e-book).
3. **Ponte** — "e se um dia você quiser atender alguém?" — convida ao e-book R$ 29,90.
4. **Abertura** — quando o curso abrir: convite leve, foco em aprofundamento pessoal.

### Trilha B — Aspirante a Terapeuta (curso)
Tom: método, confiança, profissionalização ética.
1. **Boas-vindas** — "Você quer atender — e isso é lindo" + as 3 travas do iniciante.
2. **Prova** — depoimento de aluno + Cap. 3 (Reiki gratuito da forma certa).
3. **Oferta de entrada** — e-book R$ 29,90 como primeiro passo prático.
4. **Abertura** — curso completo com condição especial de lista de espera.

### Trilha C — Terapeuta em Transição (curso + mentoria)
Tom: parceria, escala, sustentabilidade do trabalho.
1. **Boas-vindas** — "Você já atende — vamos estruturar isso" + Cap. 4 (transição para o pago).
2. **Autoridade** — desafios dos terapeutas (Cap. 5) + mentoria com o Mestre Renato.
3. **Oferta de entrada** — e-book R$ 29,90 para preencher lacunas de base.
4. **Abertura** — curso + mentoria com condição de fundador da lista.

> Todas as trilhas respeitam a conformidade: sem promessa de cura ou renda garantida; disclaimer PNPIC no rodapé dos e-mails.

---

## Contrato do payload (enviado ao webhook)

`POST` JSON para `https://reikibrasilia.app.n8n.cloud/webhook/reiki-lista-espera`
(`Content-Type: application/json`). Segmentação NÃO vem da LP.

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

**Resposta esperada:** `{"ok": true, "segmento": "Praticante Pessoal | Aspirante a Terapeuta | Terapeuta em Transicao"}`

**Validação client-side:** `nome`, `email`, `whatsapp` obrigatórios; `email` com formato; as 7 perguntas obrigatórias. Sucesso → "Você está na lista! 🌸". Erro → fallback WhatsApp (61) 98309-7777.
