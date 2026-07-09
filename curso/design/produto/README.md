# Kit visual do produto — Curso Online

> Estende a linguagem visual já estabelecida nas **capas de módulo** (`curso/design/M0…M3/`): gradiente violeta escuro, eyebrow ciano, título League Spartan, subtítulo Playfair itálico, tag **■ MÉTODO MÃOS SEGURAS** e rodapé com filete (`OM REIKI OM` · `reikibrasilia.br.com`).
> Paleta amostrada do PNG real: `#250B45` (topo-esq) → `#17082E` (centro) → `#0F0622` (base). Acentos v3: ciano `#3FD8E8`.

| Arte | Arquivo | Onde usar |
|---|---|---|
| **Capa do produto** | `capa-produto-1080.png` (1080×1080) | Imagem do produto na Eduzz / capa do curso no Nutror |
| **Banner de vitrine** | `banner-vitrine-1200x628.png` | Vitrine Eduzz, compartilhamento (OG), anúncios |
| **Banner de checkout** | `banner-checkout-1200x400.png` | Topo do checkout do curso |
| **Imagem de conclusão** | `imagem-conclusao-1280x720.png` | Tela/e-mail de fim de curso (ponte para mentoria e Nível II) |

## Decisões de conteúdo

- **Sem preço nas artes.** O upsell depende da urgência *"esta condição de R$ 197 aparece apenas agora"*. Estampar o preço numa vitrine pública contradiz isso — e a arte envelhece se o valor mudar. A Eduzz já exibe o preço.
- **Os 6 passos do Método Mãos Seguras** aparecem como chips em todas as artes: o mecanismo precisa ser visto, não só lido na página de vendas (era o ponto fraco da auditoria — mecanismo único, nota 5/10).
- **Foto do Renato + credencial** (Nível IV) ancoram a autoridade — é o diferencial do curso frente ao e-book.
- **Conformidade:** nenhuma promessa de cura, renda ou resultado garantido.

## Como regenerar

```bash
cd curso/design/produto/_src
bash render.sh     # roda build.py e renderiza os 4 PNGs nas dimensões exatas
```

## Pendência conhecida (fora deste kit)

`curso/design/M2/thumb-A8.png` está com o título **cortado** na borda direita ("COMO CONVIDAR SEM CONSTRANGIMENT…"). Vale revisar os thumbs com títulos longos.
