# Versionamento — caminho-reikiano-iniciante

O ambiente sandbox do Cowork não consegue manter o banco `.git` diretamente na pasta sincronizada (o sistema de arquivos do mount não suporta as operações de lock/rename do git). O fluxo de versionamento fica assim:

**Eu (Claude):** entrego cada fase como arquivos organizados nesta pasta, com mensagem de commit sugerida no final de cada entrega.

**Você (Renato):** roda os comandos abaixo no seu terminal (uma única vez para configurar):

```powershell
cd C:\workspace\Projetos\caminho-reikiano-iniciante
git init -b main
git remote add origin https://github.com/dpfrenatorms/caminho-reikiano-iniciante.git
git add -A
git commit -m "chore: estrutura inicial do projeto + plano de execucao aprovado"
git push -u origin main
```

E a cada fase concluída:

```powershell
git add -A
git commit -m "<mensagem sugerida na entrega>"
git push
```

**Alternativa:** se preferir que eu mesmo faça os commits e pushes, crie um *fine-grained personal access token* no GitHub (Settings → Developer settings → Tokens) com permissão de escrita apenas neste repositório e me envie. Aí passo a versionar via clone no sandbox a cada fase.

## Estrutura do repositório

```
/ebook           manuscrito revisado + docx final
/ebook/original  arquivo base original (imutável)
/design          briefing de diagramação Canva (F2)
/curso           grade curricular + /roteiros das aulas de avatar (F3)
/landing-page    copy + index.html + questionário (F4)
/docs            plano, changelogs, relatórios de verificação, memória de sessões
```

## Mensagens de commit sugeridas por fase

| Fase | Mensagem |
|---|---|
| F0 | `chore: estrutura inicial do projeto + plano de execucao aprovado` |
| F1 | `feat(ebook): manuscrito v2 revisado + docx + changelog editorial` |
| F2 | `feat(design): briefing de diagramacao canva` |
| F3 | `feat(curso): grade curricular + roteiros de avatar` |
| F4 | `feat(lp): copy + html + questionario de qualificacao` |
| F5 | `docs: relatorio de verificacao de coerencia` |
