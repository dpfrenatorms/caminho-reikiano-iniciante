# -*- coding: utf-8 -*-
"""
Gera os 4 bônus do curso em HTML (design v3) -> PDF via Chrome headless.

Uso:
    python build.py          # escreve os .html em _src/
    (depois) bash render.sh  # renderiza os PDFs em curso/upsell/bonus/

Conteúdo ancorado em: ebook/manuscrito-v2.md e curso/upsell/metodo-maos-seguras.md
Conformidade: sem promessa de cura/renda; Mikao Usui 1922; disclaimer PNPIC.
"""
import os

IMG = "../../../../design/canva-import"  # relativo a _src/

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;600;700;800;900&family=Playfair+Display:ital,wght@1,400;1,700&family=Inter:wght@300;400;600;700&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Inter',sans-serif;background:#e8e4ee}}
section.page{{width:794px;height:1123px;position:relative;overflow:hidden;margin:0 auto 24px;background:#fff}}

/* ---------- capa ---------- */
.cover{{background:#1a1040;color:#fff;text-align:center}}
img.bg{{position:absolute;top:0;left:0;width:794px;height:1123px;z-index:0}}
.cv-in{{position:relative;z-index:2;margin-top:300px;padding:0 80px}}
.cv-eyebrow{{font-family:'League Spartan',sans-serif;font-weight:800;font-size:14px;letter-spacing:.28em;color:#3FD8E8}}
.cv-line{{width:110px;height:2px;background:#3FD8E8;margin:20px auto 30px}}
.cv-title{{font-family:'League Spartan',sans-serif;font-weight:900;font-size:42px;line-height:1.1;
 text-transform:uppercase;text-shadow:0 3px 14px rgba(22,8,45,.85)}}
.cv-sub{{font-family:'Playfair Display',serif;font-style:italic;font-size:20px;color:#CDB8F0;margin-top:24px;line-height:1.5}}
.cv-meta{{font-size:12.5px;color:#EDE6FA;margin-top:40px;letter-spacing:.06em;line-height:1.7}}
img.logo{{position:absolute;bottom:44px;left:337px;width:120px;z-index:3}}

/* ---------- miolo ---------- */
.light{{padding:76px 78px 84px;color:#2B2B2B;display:flex;flex-direction:column;justify-content:center}}
.hd{{position:absolute;top:34px;left:78px;right:78px;display:flex;justify-content:space-between;
 font-size:9.5px;color:#a89bc0;letter-spacing:.08em;font-weight:300;text-transform:uppercase}}
.ft{{position:absolute;bottom:32px;left:0;right:0;text-align:center;font-size:11px;color:#6A10AD;font-weight:600}}
.ft span{{color:#d5c8e8;margin:0 10px}}
h2{{font-family:'League Spartan',sans-serif;font-weight:800;color:#6A10AD;font-size:21px;margin:0 0 6px}}
h2.sa{{font-size:28px;margin-bottom:14px}}
h3{{font-family:'League Spartan',sans-serif;font-weight:700;color:#8E3FC7;font-size:15px;margin:22px 0 8px}}
p{{font-size:13.5px;line-height:1.65;margin:0 0 11px}}
.sq{{color:#6A10AD;font-size:14px;margin-right:6px}}
.intro{{font-size:13.5px;line-height:1.7;color:#4a4a4a;margin-bottom:18px}}
ul,ol{{margin:4px 0 14px 20px}}
li{{font-size:13.5px;line-height:1.6;margin-bottom:6px}}

/* caixa de citação / frase de apoio */
.cit{{border-left:3px solid #6A10AD;padding:9px 16px;margin:12px 0 16px;font-family:'Playfair Display',serif;
 font-style:italic;font-size:14.5px;color:#3d1466;line-height:1.55}}
/* caixa de template */
.tpl{{background:#FAF0DC;border-radius:10px;padding:15px 18px;margin:12px 0 16px;font-size:13px;line-height:1.6}}
.tpl-t{{font-family:'League Spartan',sans-serif;font-weight:800;font-size:10px;letter-spacing:.14em;color:#8a6d1f;margin-bottom:7px}}
/* caixa lavanda */
.box{{background:#F5EEFF;border-left:4px solid #6A10AD;border-radius:8px;padding:14px 18px;margin:12px 0 16px}}
.box p{{margin:0;font-size:13px}}
/* checkbox printável */
.cb{{display:inline-block;width:13px;height:13px;border:1.6px solid #6A10AD;border-radius:3px;
 margin-right:9px;vertical-align:-2px}}
.ck{{list-style:none;margin-left:0}}
.ck li{{margin-bottom:9px}}
/* linha para preencher */
.fill{{border-bottom:1px dotted #b9a9d4;height:20px;margin:0 0 9px}}
/* tabela */
table{{width:100%;border-collapse:collapse;margin:10px 0 16px;font-size:12.5px}}
th{{background:#6A10AD;color:#fff;font-weight:700;padding:8px 9px;text-align:left;font-family:'League Spartan',sans-serif}}
td{{padding:7px 9px;border-bottom:.5px solid #ddd;vertical-align:top}}
tbody tr:nth-child(even){{background:#F5EEFF}}
/* grade 21 dias */
.grid21{{display:grid;grid-template-columns:repeat(7,1fr);gap:7px;margin:10px 0 8px}}
.day{{border:1.4px solid #cdbce6;border-radius:7px;height:58px;position:relative;background:#fff}}
.day b{{position:absolute;top:5px;left:7px;font-family:'League Spartan',sans-serif;font-size:11px;color:#8E3FC7}}
.wk{{font-family:'League Spartan',sans-serif;font-weight:800;font-size:11px;letter-spacing:.12em;color:#6A10AD;margin:14px 0 4px}}
.fine{{font-size:10.5px;color:#6B6B6B;line-height:1.6}}

@media print{{
 html,body{{margin:0;padding:0;background:#fff}}
 section.page{{margin:0 auto !important;page-break-after:always;break-after:page}}
 section.page:last-child{{page-break-after:auto}}
}}
@page{{size:210mm 297mm;margin:0}}
*{{-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important}}
"""

DISCLAIMER = ('<p class="fine">O Reiki é uma técnica japonesa criada por <strong>Mikao Usui em 1922</strong>, reconhecida no Brasil '
              'como prática integrativa e complementar em saúde (PNPIC — Ministério da Saúde). Este material tem caráter '
              '<strong>educacional</strong> e <strong>não substitui diagnóstico, tratamento ou acompanhamento médico ou '
              'psicológico</strong>. Não prometa cura nem resultados a quem você atende.</p>')


def cover(num, title, sub, meta):
    return f"""<section class="page cover">
  <img class="bg" src="{IMG}/bg-opener-v3.png" alt=""/>
  <div class="cv-in">
    <div class="cv-eyebrow">Bônus {num} · Curso O Caminho do Reikiano Iniciante</div>
    <div class="cv-line"></div>
    <div class="cv-title">{title}</div>
    <div class="cv-sub">{sub}</div>
    <div class="cv-meta">{meta}</div>
  </div>
  <img class="logo" src="{IMG}/logo-omreikiom.png" alt="Om Reiki Om"/>
</section>"""


def page(hd_r, n, body):
    return f"""<section class="page light">
  <div class="hd"><span>Método Mãos Seguras</span><span>{hd_r}</span></div>
  {body}
  <div class="ft"><span>—</span>{n}<span>—</span></div>
</section>"""


def ck(items):
    return '<ul class="ck">' + ''.join(f'<li><span class="cb"></span>{i}</li>' for i in items) + '</ul>'


def fills(n):
    return ''.join('<div class="fill"></div>' for _ in range(n))


# ======================= BÔNUS 1 =======================
B1 = cover(1, "Checklist<br/>Sessão Segura",
           "Para revisar tudo antes, durante e depois de aplicar.",
           "Organizado pelos 6 passos do Método Mãos Seguras<br/>Mestre Renato Menezes · Om Reiki Om")

B1 += page("Checklist Sessão Segura", 2, f"""
  <h2 class="sa">Antes de tocar em alguém</h2>
  <p class="intro">Este checklist existe para tirar da sua cabeça a pergunta <em>"esqueci alguma coisa?"</em>. Imprima, deixe ao lado da maca e marque. Com o tempo, isso vira automático — e a segurança aparece.</p>

  <h2><span class="sq">■</span> 1. Preparar — o ambiente</h2>
  {ck(["Local silencioso e sem interrupções (celular no silencioso)",
       "Luz suave ou iluminação natural",
       "Música relaxante (opcional)",
       "Incenso, óleo essencial ou aromatizador",
       "Cristais, se fizerem parte da sua prática",
       "Cadeira, maca ou colchonete confortável",
       "Água disponível para você e para quem recebe"])}

  <h2><span class="sq">■</span> 2. Preparar — você</h2>
  {ck(["Fiz meu autotratamento hoje (nem que sejam 5 minutos)",
       "Estou emocionalmente disponível para atender",
       "Combinei início, duração e valor (ou gratuidade) com a pessoa",
       "Tenho consentimento claro para a sessão"])}

  <div class="box"><p><strong>Limite saudável:</strong> se você não está bem, remarque. Atender esgotado(a) não ajuda ninguém — e ensina você a se desrespeitar.</p></div>
""")

B1 += page("Checklist Sessão Segura", 3, f"""
  <h2><span class="sq">■</span> 3. Centralizar — chegar presente</h2>
  {ck(["3 a 5 respirações profundas e conscientes",
       "Mãos em posição de prece; 1 minuto de silêncio",
       "Intenção declarada (mentalmente ou em voz baixa)",
       "Proteção energética: Cho-Ku-Rei ao redor de si e do receptor (Nível II+)",
       "Visualização de uma esfera de luz envolvendo os dois"])}
  <div class="cit">"Que eu seja apenas canal da luz e do amor. Tudo o que não me pertence passa por mim e retorna à Fonte."</div>

  <h2><span class="sq">■</span> 4. Conduzir — a sessão</h2>
  {ck(["Expliquei que a pessoa não precisa 'fazer nada' — só receber",
       "Ambiente de silêncio e acolhimento mantido",
       "Sequência de posições definida antes de começar",
       "Respiração consciente para sustentar minha presença",
       "Não estou forçando nada nem tentando 'controlar o resultado'"])}

  <div class="box"><p><strong>Se a mente divagar:</strong> volte para a respiração e para o contato das mãos. Não é erro — é prática. Comece com sessões de 15 a 20 minutos e vá aumentando.</p></div>

  <h2><span class="sq">■</span> 5. Encerrar — fechar bem</h2>
  {ck(["Agradeci internamente à energia",
       "Cho-Ku-Rei de encerramento (Nível II+)",
       "Orientei o receptor a se levantar devagar e beber água",
       "Avisei que os efeitos podem aparecer nas próximas 24 a 48 horas",
       "Lavei as mãos, bebi água, pisei no chão e respirei fundo"])}
""")

B1 += page("Checklist Sessão Segura", 4, f"""
  <h2><span class="sq">■</span> 6. Registrar — o que ficou</h2>
  <p class="intro">O registro é o que transforma sessões soltas em <strong>experiência</strong>. É também de onde saem os seus futuros depoimentos.</p>
  {ck(["Nome (ou iniciais) do receptor",
       "Data e duração da sessão",
       "Queixas principais relatadas",
       "Sensações que percebi durante e após",
       "Retorno final da pessoa",
       "Autorização para uso do depoimento (se aplicável)"])}

  <h3>Anotações desta sessão</h3>
  {fills(7)}

  <h2><span class="sq">■</span> Cuidados e limites — sempre</h2>
  {ck(["Não prometi cura nem resultado milagroso",
       "Não atendi sem consentimento",
       "Respeitei meu limite de sessões na semana",
       "Orientei a pessoa a manter seus tratamentos de saúde convencionais"])}

  <div class="box"><p><strong>Sua energia e seu tempo</strong> são parte do trabalho. Protegê-los desde o início não é egoísmo — é o que sustenta a sua prática a longo prazo.</p></div>

  {DISCLAIMER}
""")

# ======================= BÔNUS 2 =======================
B2 = cover(2, "Roteiro de Conversa<br/>com o Cliente",
           "O que falar antes, durante e depois da sessão.",
           "Frases prontas para adaptar com as suas palavras<br/>Mestre Renato Menezes · Om Reiki Om")

B2 += page("Roteiro de Conversa", 2, f"""
  <h2 class="sa">As palavras também cuidam</h2>
  <p class="intro">Boa parte da insegurança do reikiano iniciante não está nas mãos — está na <strong>boca</strong>. Não saber o que dizer trava o convite, a sessão e o retorno. Aqui estão os roteiros. Use como base e adapte com o seu jeito.</p>

  <h2><span class="sq">■</span> 1. O convite (sem parecer amador ou carente)</h2>
  <div class="tpl">
    <div class="tpl-t">MODELO — WHATSAPP OU DIRECT</div>
    <div>"Oi, [nome]! Estou em processo de formação como terapeuta de Reiki e estou abrindo algumas sessões gratuitas para prática supervisionada. Você gostaria de participar? A sessão é relaxante, sem contato físico, e pode ajudar com ansiedade, insônia ou estresse. Se tiver interesse, me avisa que envio mais detalhes. Gratidão!"</div>
  </div>
  <ul>
    <li>Seja direto(a), gentil e claro(a);</li>
    <li>Deixe explícito que é uma prática limitada ("estou abrindo 5 vagas");</li>
    <li>Senso de exclusividade evita desvalorização.</li>
  </ul>

  <h2><span class="sq">■</span> 2. Explicar o Reiki em uma frase</h2>
  <div class="tpl">
    <div class="tpl-t">VERSÃO NEUTRA — SERVE PARA QUALQUER PESSOA</div>
    <div>"Reiki é uma técnica japonesa de canalização de energia, usada para redução do estresse, equilíbrio emocional e bem-estar. É uma prática integrativa e complementar — não substitui tratamento médico."</div>
  </div>
  <ul>
    <li>Com pessoas mais racionais, <strong>evite jargão místico</strong>;</li>
    <li>Compartilhe a sua experiência pessoal — é o que cria conexão;</li>
    <li>Treine em voz alta: quem sou eu? O que eu faço? Como eu ajudo?</li>
  </ul>
""")

B2 += page("Roteiro de Conversa", 3, f"""
  <h2><span class="sq">■</span> 3. Antes da sessão</h2>
  <p><strong>Pergunte:</strong></p>
  <ul>
    <li>"Como você está se sentindo hoje, no corpo e nas emoções?"</li>
    <li>"Tem alguma coisa específica que te trouxe aqui?"</li>
    <li>"Você já recebeu Reiki antes?"</li>
  </ul>
  <p><strong>Explique e alivie a expectativa:</strong></p>
  <div class="tpl">
    <div class="tpl-t">O QUE DIZER</div>
    <div>"Você não precisa fazer nada. É só deitar, fechar os olhos e receber. Algumas pessoas sentem calor, formigamento ou relaxamento profundo; outras não sentem nada de imediato — e está tudo bem. A energia age nos níveis sutis, no seu tempo."</div>
  </div>

  <h2><span class="sq">■</span> 4. Durante a sessão</h2>
  <ul>
    <li>Silêncio e acolhimento — fale o mínimo;</li>
    <li>Se precisar avisar uma mudança de posição, use voz baixa e curta;</li>
    <li>Sustente a sua presença pela respiração. Não force nada.</li>
  </ul>

  <h2><span class="sq">■</span> 5. Depois da sessão</h2>
  <p><strong>Pergunte:</strong> "Como você se sentiu?" — e <em>escute sem corrigir</em>.</p>
  <div class="tpl">
    <div class="tpl-t">ORIENTAÇÃO DE ENCERRAMENTO</div>
    <div>"Levante devagar e beba bastante água hoje. Observe como você se sente nas próximas 24 a 48 horas — às vezes os efeitos aparecem depois. Cada pessoa reage de um jeito; confie no seu processo. E continue com os seus tratamentos de saúde normalmente."</div>
  </div>
  <div class="cit">Não é o seu papel curar ninguém. O Reiki apoia o processo de equilíbrio — e cada um tem o seu tempo.</div>
""")

B2 += page("Roteiro de Conversa", 4, f"""
  <h2><span class="sq">■</span> 6. Pedir o retorno (e o depoimento)</h2>
  <div class="tpl">
    <div class="tpl-t">MENSAGEM 24–48H DEPOIS</div>
    <div>"Oi, [nome]! Passando para saber como você se sentiu depois da sessão. Notou alguma mudança no sono, no ânimo ou no corpo? Seu retorno me ajuda muito a evoluir na prática. E, se você se sentir à vontade, posso compartilhar a sua experiência (sem citar seu nome, se preferir)?"</div>
  </div>
  <ul>
    <li>Peça o retorno <strong>depois</strong> que a pessoa teve tempo de observar;</li>
    <li>Sempre pergunte antes de publicar qualquer relato;</li>
    <li>Guarde a autorização junto do seu registro de sessão.</li>
  </ul>

  <h2><span class="sq">■</span> 7. Comunicar o valor sem medo</h2>
  <p class="intro">Quando chegar a hora de cobrar, não anuncie um preço solto — apresente o que a pessoa recebe. Cobrar com ética não diminui a espiritualidade da sua prática: é o que sustenta a sua capacidade de continuar servindo.</p>
  <div class="tpl">
    <div class="tpl-t">MODELO — APRESENTANDO O VALOR</div>
    <div>"Minhas sessões de Reiki ajudam a aliviar o estresse, melhorar o sono e trazer equilíbrio emocional. Para um atendimento individual, o valor é R$ ____ e, se você quiser um acompanhamento completo, tenho pacotes com condição especial."</div>
  </div>

  <h3>Suas frases — adapte com as suas palavras</h3>
  {fills(6)}

  {DISCLAIMER}
""")

# ======================= BÔNUS 3 =======================
B3 = cover(3, "Plano 21 Dias<br/>de Prática",
           "Para transformar estudo em rotina.",
           "5 a 10 minutos por dia · 3 semanas · 1 hábito<br/>Mestre Renato Menezes · Om Reiki Om")

B3 += page("Plano 21 Dias de Prática", 2, f"""
  <h2 class="sa">Como funciona</h2>
  <p class="intro">A confiança não vem do "dom". Vem da <strong>repetição com intenção</strong>. São 21 dias, de 5 a 10 minutos. O objetivo não é fazer bonito — é <strong>não quebrar a corrente</strong>. Se falhar um dia, retome no seguinte, sem culpa.</p>

  <h2><span class="sq">■</span> A rotina diária (base)</h2>
  <table>
    <thead><tr><th style="width:26%">Momento</th><th>O que fazer</th></tr></thead>
    <tbody>
      <tr><td><strong>Ao acordar</strong></td><td>3 respirações profundas + mãos no coração + 1 minuto de Reiki</td></tr>
      <tr><td><strong>Antes de dormir</strong></td><td>Mãos no abdômen + 5 minutos de autotratamento</td></tr>
      <tr><td><strong>Durante o dia</strong></td><td>Cho-Ku-Rei para energizar situações ou locais (a partir do Nível II)</td></tr>
    </tbody>
  </table>

  <h2><span class="sq">■</span> Posições básicas do autotratamento</h2>
  <p>Cabeça · garganta · coração · plexo solar · abdômen · joelhos · pés. Respire fundo em cada posição e apenas observe as sensações.</p>

  <h2><span class="sq">■</span> As três semanas</h2>
  <ul>
    <li><strong>Semana 1 — Fundação:</strong> autotratamento diário + os 5 Princípios do Reiki;</li>
    <li><strong>Semana 2 — Sensibilidade:</strong> exercício das mãos + visualização da energia fluindo;</li>
    <li><strong>Semana 3 — Aplicação:</strong> aplicar em outra pessoa (ou planta/animal), registrar e compartilhar.</li>
  </ul>

  <div class="box"><p><strong>Crie um espaço fixo de prática</strong> em casa: um cantinho com almofada, incenso, plantas — o que fizer sentido para você. O corpo aprende pelo lugar.</p></div>
""")

def week(n, title, dias, tarefa):
    cells = ''.join(f'<div class="day"><b>{d}</b></div>' for d in dias)
    return f'<div class="wk">SEMANA {n} — {title}</div><p style="font-size:12.5px;margin-bottom:6px">{tarefa}</p><div class="grid21">{cells}</div>'

B3 += page("Plano 21 Dias de Prática", 3, f"""
  <h2 class="sa">Sua grade de 21 dias</h2>
  <p class="intro">Marque um ✓ no dia em que praticou. Imprima esta página e deixe visível.</p>

  {week(1, "FUNDAÇÃO", range(1,8), "Autotratamento diário (5–10 min) + repetir mentalmente os 5 Princípios do Reiki.")}
  {week(2, "SENSIBILIDADE", range(8,15), "Autotratamento + exercício das mãos (abrir e fechar as palmas, sentindo calor/magnetismo) + visualizar a energia fluindo.")}
  {week(3, "APLICAÇÃO", range(15,22), "Autotratamento + aplicar Reiki em outra pessoa, planta ou animal + registrar as sensações + compartilhar sua experiência com alguém.")}

  <h2><span class="sq">■</span> O exercício das mãos (Semana 2)</h2>
  <ol>
    <li>Sente-se com a coluna ereta e junte as palmas em posição de prece;</li>
    <li>Respire profundamente por 1 minuto;</li>
    <li>Afaste as mãos cerca de 10 cm e aproxime-as devagar, várias vezes;</li>
    <li>Observe: calor, magnetismo, formigamento ou uma leve resistência;</li>
    <li>Fique alguns minutos apenas sentindo — e agradeça ao final.</li>
  </ol>
  <div class="cit">Você não precisa sentir tudo. Você não precisa ser perfeito(a). Você só precisa estar presente, confiar e continuar praticando.</div>
""")

B3 += page("Plano 21 Dias de Prática", 4, f"""
  <h2 class="sa">Registro da jornada</h2>
  <p class="intro">Ao final de cada semana, pare cinco minutos e responda. É aqui que você percebe a evolução que o dia a dia esconde.</p>

  <h3>Semana 1 — o que mudou no meu corpo e na minha mente?</h3>
  {fills(4)}
  <h3>Semana 2 — o que eu percebi nas minhas mãos e na minha percepção?</h3>
  {fills(4)}
  <h3>Semana 3 — como foi aplicar em outra pessoa? O que eu diria a quem está começando?</h3>
  {fills(4)}

  <h2><span class="sq">■</span> Checklist — estou me bloqueando ou evoluindo?</h2>
  {ck(["Estou praticando com regularidade?",
       "Estou me comparando demais com outros reikianos?",
       "Estou tentando controlar os resultados?",
       "Estou respeitando o meu tempo de aprendizagem?"])}

  <div class="box"><p><strong>Ao terminar os 21 dias:</strong> não pare. Escolha o próximo ciclo — aplicar em mais pessoas, iniciar o registro de atendimentos, ou dar o passo para a primeira sessão cobrada.</p></div>

  {DISCLAIMER}
""")

# ======================= BÔNUS 4 =======================
B4 = cover(4, "Guia de Objeções<br/>do Reikiano Iniciante",
           "Medo, cobrança, insegurança e as dúvidas que travam a prática.",
           "9 objeções reais · o que está acontecendo · o que fazer<br/>Mestre Renato Menezes · Om Reiki Om")

def obj(n, titulo, acontecendo, fazer, frase):
    itens = ''.join(f'<li>{i}</li>' for i in fazer)
    return f"""
  <h2><span class="sq">■</span> {n}. "{titulo}"</h2>
  <p><strong>O que está acontecendo:</strong> {acontecendo}</p>
  <p><strong>O que fazer:</strong></p>
  <ul>{itens}</ul>
  <div class="cit">{frase}</div>"""

B4 += page("Guia de Objeções", 2, f"""
  <h2 class="sa">Nenhuma dessas dúvidas é sinal de fracasso</h2>
  <p class="intro">Todo reikiano iniciante passa por elas. O que separa quem pratica de quem guarda o certificado na gaveta não é a ausência de dúvida — é ter uma resposta pronta para ela. Consulte este guia sempre que travar.</p>
  {obj(1, "Não sinto nada nas mãos",
       "no início, o corpo e a percepção ainda estão em ajuste energético. Nem todo mundo sente calor logo de cara — e isso não significa nada sobre a sua capacidade.",
       ["Pratique o autotratamento diariamente;",
        "Coloque a intenção com confiança, mesmo sem 'sentir' — a energia flui pela intenção e presença;",
        "Observe as sensações no corpo do receptor, não só nas suas mãos;",
        "Solte a expectativa: a percepção costuma vir com o tempo."],
       "A energia flui onde há intenção, confiança e prática — não onde há perfeição.")}
  {obj(2, "E se a pessoa disser que não sentiu nada?",
       "o Reiki atua em níveis sutis. Muitas vezes os efeitos são progressivos e internos, e aparecem nas 24 a 48 horas seguintes.",
       ["Avise antes: 'cada pessoa reage de uma forma';",
        "Peça para observar o sono, o ânimo e o corpo nos dias seguintes;",
        "Anote o retorno recebido — é assim que você acompanha o progresso;",
        "Lembre-se: não é o seu papel curar ninguém."],
       "Não é você que cura. O Reiki apoia o processo de equilíbrio — e cada um tem o seu tempo.")}
""")

B4 += page("Guia de Objeções", 3, f"""
  {obj(3, "Tenho medo de fazer errado",
       "perfeccionismo somado à falta de confiança trava a prática. O Reiki é natural, fluido e intuitivo — precisa ser sincero, não 'certinho'.",
       ["Lembre-se: o Reiki não depende de você, mas passa por você;",
        "Foque na presença, não na perfeição;",
        "Autotratamento constante gera segurança crescente;",
        "Converse com outros reikianos e normalize as suas dúvidas."],
       "Reiki é simples. Reiki é natural. Reiki é amor em movimento.")}
  {obj(4, "Tenho medo de absorver energias densas",
       "é um receio comum, e prevenível com uma rotina simples de proteção e higiene energética.",
       ["Antes: 'Eu sou apenas canal. Tudo o que não me pertence passa por mim e retorna à Fonte';",
        "Use o Cho-Ku-Rei ao redor de si e do receptor (Nível II+);",
        "Depois: lave as mãos, beba água, pise no chão, respire fundo;",
        "Aplique Reiki em você para reequilibrar o seu campo."],
       "Cuidar da sua energia aumenta a sua confiança natural como terapeuta.")}
  {obj(5, "Acho que não tenho dom",
       "crença limitante, comparação e falta de confiança. Reiki não é dom: é prática, intenção e canal.",
       ["Repita: 'Eu sou um canal puro e perfeito da energia universal';",
        "Pare de se comparar — cada um tem o seu ritmo;",
        "Volte à base: intenção + presença + prática = evolução."],
       "Se você recebeu a sintonização, você já é reikiano(a). O que falta é coragem para caminhar.")}
""")

B4 += page("Guia de Objeções", 4, f"""
  {obj(6, "Não consigo criar uma rotina",
       "a falta de rotina cria desconexão energética. O Reiki precisa ser alimentado, como qualquer prática.",
       ["Ritual diário de 5 a 10 minutos, sempre no mesmo horário;",
        "Use um calendário ou app de hábitos;",
        "Faça o desafio dos 21 Dias (Bônus 3) — e convide alguém para fazer junto."],
       "A confiança não vem do dom. Vem da repetição com intenção.")}
  {obj(7, "Como explico o Reiki sem parecer esotérico demais?",
       "você ainda está encontrando a sua forma de comunicar. Isso se treina.",
       ["Use a frase neutra: 'técnica japonesa de canalização de energia para redução do estresse, equilíbrio emocional e bem-estar';",
        "Evite jargão místico com pessoas mais racionais;",
        "Compartilhe a sua experiência pessoal — é o que cria conexão;",
        "Treine em voz alta: quem sou eu? O que eu faço? Como eu ajudo?"],
       "Simples comunica. Complicado afasta.")}
  {obj(8, "Tenho medo (ou culpa) de cobrar",
       "a crença de que 'energia não tem preço'. Mas o seu tempo, estudo e dedicação têm — e é isso que você cobra.",
       ["Apresente benefícios antes do preço, nunca o preço solto;",
        "Comece com um valor que você consiga sustentar sem ressentimento;",
        "Ofereça pacotes de acompanhamento;",
        "Entenda: cobrar com ética sustenta a sua capacidade de continuar servindo."],
       "Praticar de graça no início não é se desvalorizar. É construir base. Mas não é para sempre.")}
""")

B4 += page("Guia de Objeções", 5, f"""
  {obj(9, "Preciso de registro ou autorização para atuar?",
       "o Reiki é reconhecido no Brasil como prática integrativa e complementar em saúde (PNPIC — Ministério da Saúde). Ele não é uma profissão regulamentada em conselho próprio, e é isso que confunde muita gente.",
       ["Apresente-se como <strong>terapeuta de Reiki</strong>, nunca como profissional de saúde;",
        "Nunca prometa cura, diagnóstico ou substituição de tratamento;",
        "Oriente sempre a pessoa a manter o acompanhamento médico e psicológico;",
        "Formalize a sua atuação (contrato simples, recibo, registro de sessões);",
        "Consulte a legislação municipal — algumas cidades têm exigências próprias."],
       "Clareza legal e consciência profissional protegem você e quem você atende.")}

  <h2><span class="sq">■</span> Quando a dúvida voltar</h2>
  <p class="intro">Ela vai voltar — e tudo bem. Volte a este guia, respire e pergunte-se: <em>estou praticando com regularidade? Estou tentando controlar o resultado? Estou respeitando o meu tempo?</em></p>
  <div class="cit">Não existe reikiano perfeito. Existe reikiano presente.</div>

  <div class="box"><p><strong>Próximo passo:</strong> escolha <strong>uma</strong> objeção desta lista — a que mais te trava hoje — e aplique a resposta ainda esta semana. Uma de cada vez.</p></div>

  {DISCLAIMER}
""")

# ======================= build =======================
BONUS = {
    "bonus-1-checklist-sessao-segura": B1,
    "bonus-2-roteiro-conversa-cliente": B2,
    "bonus-3-plano-21-dias": B3,
    "bonus-4-guia-objecoes": B4,
}

here = os.path.dirname(os.path.abspath(__file__))
for name, body in BONUS.items():
    html = f"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'><title>{name}</title><style>{CSS}</style></head><body>{body}</body></html>"
    with open(os.path.join(here, name + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("html:", name)
print("ok")
