# Bônus do curso — 4 PDFs

> **Papel na oferta:** os bônus são as **ferramentas de aplicação** (e-book = mapa · curso = prática guiada · bônus = ferramentas). Servem para quebrar objeção e aumentar o valor percebido do upsell de R$ 197.
> Estão organizados pelos **6 passos do Método Mãos Seguras** (`../metodo-maos-seguras.md`), para reforçar o mecanismo em vez de serem PDFs soltos.

| # | Bônus | Arquivo | Págs | O que resolve |
|---|---|---|---|---|
| 1 | **Checklist Sessão Segura** | `bonus-1-checklist-sessao-segura.pdf` | 4 | "Esqueci alguma coisa?" — Preparar › Centralizar › Conduzir › Encerrar › Registrar, com caixas para marcar |
| 2 | **Roteiro de Conversa com o Cliente** | `bonus-2-roteiro-conversa-cliente.pdf` | 4 | "Não sei o que dizer" — convite, explicar Reiki, antes/durante/depois, pedir depoimento, comunicar valor |
| 3 | **Plano 21 Dias de Prática** | `bonus-3-plano-21-dias.pdf` | 4 | "Não consigo criar rotina" — grade de 21 dias para imprimir + registro semanal |
| 4 | **Guia de Objeções do Reikiano Iniciante** | `bonus-4-guia-objecoes.pdf` | 5 | As 9 travas reais (não sinto nada, medo de errar, medo de cobrar, registro legal…) |

## Fonte do conteúdo

Nada é inventado: tudo é derivado de `ebook/manuscrito-v2.md` (checklists, template de convite, comunicação com o receptor, desafio de 21 dias, as 9 dificuldades, precificação) e reorganizado sob o Método Mãos Seguras.

## Conformidade (verificada)

- Zero ocorrências de "milenar"; Reiki como técnica japonesa criada por **Mikao Usui em 1922**
- Todas as menções a "cura" aparecem como **proibição/negação** ("não é o seu papel curar ninguém", "nunca prometa cura")
- Sem promessa de renda ou resultado garantido
- Disclaimer PNPIC no rodapé de cada bônus

## Como regenerar

```bash
cd curso/upsell/bonus/_src
bash render.sh        # roda build.py e renderiza os 4 PDFs via Chrome headless
```

Design v3 (roxo `#6A10AD` + ciano `#3FD8E8`, League Spartan / Playfair / Inter), A4, páginas com conteúdo **centralizado verticalmente** e checkboxes/linhas para preencher e imprimir.
