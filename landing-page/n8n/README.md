# Workflow n8n — Lista de Espera (F4)

Recebe o formulário da landing page, segmenta o lead e grava/notifica via Gmail. **Opção B (Gmail-native)** — reutiliza a credencial `Gmail OAuth2 API` já existente na instância; **nenhuma credencial nova**.

> **STATUS: no ar e validado (03/07/2026).**
> - Workflow id: `etum7cA1SJRHIk7R` · **ativo**
> - **URL de produção:** `https://reikibrasilia.app.n8n.cloud/webhook/reiki-lista-espera`
> - Teste end-to-end: `{"ok":true,"segmento":"Terapeuta em Transicao"}` · execução `success` (notificação + boas-vindas enviadas)
> - Criado/ativado/testado via API pública do n8n (não por import manual).
> - ⚠️ Pendente: aplicar o ajuste anti-duplicação na triagem (ver abaixo) — a notificação `[LISTA-ESPERA]` cai no inbox que a *Triagem de Leads Gmail* monitora.

## Fluxo

```
[Webhook POST /reiki-lista-espera]
  → [Code: valida + calcula "segmento"]
  → [Gmail: notifica Renato no inbox]  assunto "[LISTA-ESPERA] {nome} · {segmento}"
  → [Gmail: boas-vindas ao lead]
  → [Respond: 200 {ok, segmento}]
```

A credencial Gmail (`id ljxuwvtS9wNx9hDx`) já vem embutida no JSON → import plug-and-play.

## Passos para ativar

1. **n8n → Workflows → ⋯ → Import from File** → selecione `lista-espera.workflow.json`.
2. Confira o nó **Notificar Renato** — `sendTo` está como `brasiliareiki@gmail.com`; ajuste se quiser outro inbox.
3. **Save** → **Activate**.
4. Copie a **Production URL** do nó *Webhook Lista de Espera* (algo como `https://reikibrasilia.app.n8n.cloud/webhook/reiki-lista-espera`) e envie ao Claude para embutir no `index.html`.

## Organização no Gmail (opcional, recomendado)

Para os leads da lista de espera não serem reprocessados pela *Triagem de Leads Gmail*:

- **Opção rápida (filtro Gmail):** crie um filtro `assunto contém [LISTA-ESPERA]` → aplicar label `Lista de Espera` + *pular caixa de entrada*.
- **Ou (ajuste na triagem):** no workflow `Reiki — Triagem de Leads Gmail` (`xZNYB74zf4WlVRt1`), no nó *Email Recebido*, acrescente ao filtro `q`: `-subject:"LISTA-ESPERA"`.

## Payload esperado (contrato — ver spec F4 §6)

```json
{
  "origem": "landing-page-caminho-reikiano",
  "timestamp_cliente": "2026-07-03T14:22:00-03:00",
  "contato": { "nome": "Ana", "email": "ana@exemplo.com", "whatsapp": "+55 61 99999-9999" },
  "questionario": {
    "q1_momento_reiki": "nivel_1",
    "q2_tempo_iniciacao": "6_a_12_meses",
    "q3_frequencia": "semanal",
    "q4_maior_dificuldade": "medo_cobrar",
    "q5_objetivo": "profissional",
    "q6_ja_atendeu": "sim_gratis",
    "q7_investimento": "de_197_a_297"
  }
}
```

## Teste rápido (após ativar)

```bash
curl -X POST "https://reikibrasilia.app.n8n.cloud/webhook/reiki-lista-espera" \
  -H "Content-Type: application/json" \
  -d '{"origem":"teste","contato":{"nome":"Teste Lead","email":"seu-email@exemplo.com","whatsapp":"+55 61 90000-0000"},"questionario":{"q1_momento_reiki":"nivel_1","q5_objetivo":"profissional","q6_ja_atendeu":"sim_pago"}}'
# esperado: {"ok":true,"segmento":"Terapeuta em Transicao"}
```
