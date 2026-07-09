# Protocolo de sincronização entre notebooks

> Escrito em 09/07/2026 depois de um quase-acidente (ver §4). **Leia antes de rodar `export.ps1` ou `import.ps1`.**

## 1. A regra de ouro

> **Git junta. Robocopy substitui.**

Os scripts `F:\WorkspaceSync\export.ps1` e `import.ps1` usam `robocopy /MIR` — um **espelho**. Eles não fazem merge: deixam o destino **idêntico** à origem, **apagando** o que só existe do outro lado.

Este projeto é um repositório git com remoto no GitHub. Portanto:

- **Para o repositório → use git** (`push`/`pull`). Git faz merge.
- **Para o resto** (`.claude`, memórias, plugins) → o HD é só transporte.

## 2. Protocolo

| Momento | O que fazer |
|---|---|
| **Ao TERMINAR** numa máquina | `git add . && git commit -m "..."` → **`git push origin main`** → (opcional) `export.ps1` |
| **Ao COMEÇAR** numa máquina | **`git pull origin main`** → (opcional) `import.ps1` (só para o que não é git) |

Com `push` ao sair e `pull` ao chegar, **divergência não destrói nada** — o GitHub é a fonte da verdade.

## 3. O que NUNCA fazer

❌ Rodar `export.ps1` ou `import.ps1` quando **os dois lados têm trabalho não sincronizado**.
- `export` → apaga do HD o trabalho da outra máquina.
- `import` → apaga desta máquina o trabalho local **e sobrescreve o `.git`**, podendo destruir commits não pushados.

Se estiver em dúvida sobre qual lado é o mais novo: **não rode nada**. Compare primeiro (§5).

## 4. Incidente de 09/07/2026 (o que aconteceu)

As duas máquinas divergiram:
- **HD** carregava o trabalho de casa (67 arquivos do curso: narrações, slides, capas, `metodo-maos-seguras.md`, `plano-sprints-curso.md`) — **sem commit** (HEAD parado em `8263620`).
- **Máquina do trabalho** tinha a página de upsell + fundos HeyGen — **6 commits não pushados**.

Um `export` foi rodado por engano (a intenção era `import`). Por sorte, ele não escreveu o projeto no espelho. **Se fosse `import`, teria apagado os commits de hoje.**

**Correção aplicada:** merge manual (trazer o trabalho de casa para dentro do git), commits `9c50ac1` e `f3a3d8a`, depois `export` limpo e `git push`. Nada foi perdido.

## 5. Se divergiu de novo — procedimento de recuperação

1. **Não rode export/import.**
2. Compare os dois lados (PowerShell):
   ```powershell
   $L='C:\Workspace'; $M='F:\WorkspaceSync\mirror\Workspace'
   function Snap($r){ Get-ChildItem $r -Recurse -File -Force |
     Where-Object { $_.FullName -notmatch '\\\.git\\' } |
     ForEach-Object { $_.FullName.Substring($r.Length).TrimStart('\') } }
   $l=Snap $L; $m=Snap $M
   "Só no HD (seriam apagados por export):"; $m | Where-Object { $l -notcontains $_ }
   "Só no local (seriam apagados por import):"; $l | Where-Object { $m -notcontains $_ }
   ```
3. Traga o que falta do HD para o local com `robocopy <origem> <destino> /E` (**`/E`, nunca `/MIR`** — `/E` só adiciona).
4. Revise, `git add` + `git commit` + `git push`.
5. Só então rode `export.ps1` (agora o local é superconjunto → seguro).

## 6. Verificação rápida de saúde

```bash
git fetch origin
git log --oneline origin/main..HEAD   # commits só aqui  → precisa push
git log --oneline HEAD..origin/main   # commits só lá    → precisa pull
git status --short                     # trabalho não commitado
```
Os três vazios = está tudo sincronizado.
