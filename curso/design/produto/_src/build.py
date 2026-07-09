# -*- coding: utf-8 -*-
"""
Kit visual do PRODUTO (curso) — estende a linguagem das capas de módulo.
Gera 4 HTMLs; render.sh converte em PNG via Chrome headless.

Paleta amostrada de curso/design/M0/capa-modulo-M0.png:
  topo-esq #250B45 · centro #17082E · base #0F0622
Acentos v3: ciano #3FD8E8 / #7FE9F4 · lavanda #CDB8F0
"""
import os

IMG = "../../../../design/canva-import"  # relativo a _src/

BASE = f"""
@import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;600;700;800;900&family=Playfair+Display:ital,wght@1,400;1,700&family=Inter:wght@300;400;600;700&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Inter',sans-serif}}
.art{{position:relative;overflow:hidden;color:#fff;
  display:flex;flex-direction:column;justify-content:center;
  background:radial-gradient(ellipse 90% 80% at 6% 4%, #2C0E52 0%, #1B0833 46%, #0E0521 100%)}}
.fotocap{{position:absolute;text-align:center;font-size:12.5px;color:#8F7FB5;letter-spacing:.03em;line-height:1.5}}
.eyebrow{{font-family:'League Spartan',sans-serif;font-weight:800;color:#3FD8E8;text-transform:uppercase}}
.rule{{background:#3FD8E8;height:3px}}
h1{{font-family:'League Spartan',sans-serif;font-weight:900;text-transform:uppercase;line-height:1.03;color:#fff}}
.sub{{font-family:'Playfair Display',serif;font-style:italic;color:#CDB8F0}}
.metodo{{font-family:'League Spartan',sans-serif;font-weight:800;color:#EDE6FA;letter-spacing:.14em;text-transform:uppercase}}
.metodo i{{color:#3FD8E8;font-style:normal;margin-right:9px}}
.meta{{color:#CDB8F0}}
.foto{{border-radius:50%;border:3px solid #8E3FC7;object-fit:cover}}
/* rodape padrao das capas de modulo */
.foot{{position:absolute;left:0;right:0;display:flex;justify-content:space-between;align-items:center}}
.foot::before{{content:"";position:absolute;top:-16px;left:0;right:0;height:1px;background:rgba(205,184,240,.28)}}
.foot .b{{font-family:'League Spartan',sans-serif;font-weight:800;color:#3FD8E8;letter-spacing:.2em;font-size:13px}}
.foot .u{{color:#8F7FB5;font-size:12px;letter-spacing:.04em}}
/* chips dos 6 passos */
.steps{{display:flex;flex-wrap:wrap}}
.chip{{border:1.5px solid rgba(63,216,232,.5);border-radius:30px;color:#EDE6FA;
  font-family:'League Spartan',sans-serif;font-weight:700;letter-spacing:.04em}}
.chip b{{color:#3FD8E8;margin-right:7px}}
.trust{{display:flex}}
.trust span{{font-family:'League Spartan',sans-serif;font-weight:700;color:#fff;white-space:nowrap}}
.trust b{{color:#3FD8E8;margin-right:7px}}
"""

TITULO = "O Caminho do<br/>Reikiano Iniciante"
SUB = "Da primeira aplicação ao primeiro cliente"
PASSOS = ["Preparar", "Centralizar", "Conduzir", "Encerrar", "Registrar", "Evoluir"]


def chips(size=15, pad="9px 18px", gap="9px"):
    c = "".join(f'<div class="chip"><b>{i+1}</b>{p}</div>' for i, p in enumerate(PASSOS))
    return f'<div class="steps" style="gap:{gap}">{c}</div>', f".chip{{font-size:{size}px;padding:{pad}}}"


# ---------------- 1) capa do produto 1080x1080 ----------------
ch, chcss = chips(15, "9px 17px", "9px")
CAPA = f"""<style>{BASE}
html,body{{width:1080px;height:1080px}} .art{{width:1080px;height:1080px;padding:92px 88px}}
.eyebrow{{font-size:23px;letter-spacing:.24em}} .rule{{width:120px;margin:24px 0 34px}}
h1{{font-size:66px;max-width:700px}} .sub{{font-size:28px;margin-top:26px;max-width:660px;line-height:1.4}}
.metodo{{font-size:19px;margin-top:44px}}
.meta{{font-size:20px;margin-top:22px;letter-spacing:.02em}}
.foto{{width:186px;height:186px;position:absolute;right:88px;top:calc(50% - 130px)}}
.fotocap{{right:88px;top:calc(50% + 70px);width:186px}}
{chcss} .steps{{margin-top:30px;max-width:440px}}
.foot{{bottom:64px;left:88px;right:88px}}
</style>
<div class="art">
  <div class="eyebrow">Curso online</div>
  <div class="rule"></div>
  <h1>{TITULO}</h1>
  <div class="sub">{SUB}</div>
  <div class="metodo"><i>■</i>Método Mãos Seguras</div>
  {ch}
  <div class="meta">6 módulos · 20 aulas · estude no seu ritmo</div>
  <img class="foto" src="{IMG}/foto-autor-circulo.png" alt="Renato Menezes"/>
  <div class="fotocap">Mestre Renato Menezes<br/>Reiki Nível IV</div>
  <div class="foot"><span class="b">OM REIKI OM</span><span class="u">reikibrasilia.br.com</span></div>
</div>"""

# ---------------- 2) banner vitrine 1200x628 ----------------
ch2, chcss2 = chips(13, "7px 14px", "7px")
VITRINE = f"""<style>{BASE}
html,body{{width:1200px;height:628px}} .art{{width:1200px;height:628px;padding:62px 64px}}
.eyebrow{{font-size:18px;letter-spacing:.22em}} .rule{{width:96px;margin:18px 0 24px}}
h1{{font-size:48px;max-width:640px}} .sub{{font-size:22px;margin-top:18px;max-width:600px;line-height:1.4}}
.metodo{{font-size:15px;margin-top:26px}}
{chcss2} .steps{{margin-top:20px;max-width:640px}}
.foto{{width:200px;height:200px;position:absolute;right:80px;top:calc(50% - 130px)}}
.fotocap{{right:80px;top:calc(50% + 82px);width:200px}}
.trust{{gap:26px;margin-top:26px}} .trust span{{font-size:16px}}
.foot{{bottom:44px;left:64px;right:64px}}
</style>
<div class="art">
  <div class="eyebrow">Curso online · Reiki para iniciantes</div>
  <div class="rule"></div>
  <h1>{TITULO}</h1>
  <div class="sub">{SUB}</div>
  <div class="metodo"><i>■</i>Método Mãos Seguras · 6 passos</div>
  {ch2}
  <div class="trust"><span><b>✓</b>6 módulos · 20 aulas</span><span><b>✓</b>Garantia de 7 dias</span></div>
  <img class="foto" src="{IMG}/foto-autor-circulo.png" alt="Renato Menezes"/>
  <div class="fotocap">Mestre Renato Menezes<br/>Reiki Nível IV</div>
  <div class="foot"><span class="b">OM REIKI OM</span><span class="u">reikibrasilia.br.com</span></div>
</div>"""

# ---------------- 3) banner checkout 1200x400 ----------------
CHECKOUT = f"""<style>{BASE}
html,body{{width:1200px;height:400px}} .art{{width:1200px;height:400px}}
.wrap{{position:absolute;left:330px;top:50%;transform:translateY(-50%);width:600px}}
.eyebrow{{font-size:16px;letter-spacing:.2em}}
h1{{font-size:37px;margin:12px 0 8px}} .sub{{font-size:19px}}
.trust{{gap:22px;margin-top:22px}} .trust span{{font-size:16px}}
.foto{{width:190px;height:190px;position:absolute;left:82px;top:50%;transform:translateY(-50%)}}
img.logo{{position:absolute;right:64px;top:50%;transform:translateY(-50%);width:126px;opacity:.92}}
.glow{{position:absolute;right:-120px;top:-140px;width:520px;height:520px;
  background:radial-gradient(circle, rgba(63,216,232,.20), rgba(63,216,232,0) 68%)}}
</style>
<div class="art">
  <div class="glow"></div>
  <img class="foto" src="{IMG}/foto-autor-circulo.png" alt="Renato Menezes"/>
  <div class="wrap">
    <div class="eyebrow">Curso online · Método Mãos Seguras</div>
    <h1>{TITULO}</h1>
    <div class="sub">{SUB}</div>
    <div class="trust">
      <span><b>✓</b>Acesso imediato</span>
      <span><b>✓</b>Garantia de 7 dias</span>
      <span><b>✓</b>Estude no seu ritmo</span>
    </div>
  </div>
  <img class="logo" src="{IMG}/logo-omreikiom.png" alt="Om Reiki Om"/>
</div>"""

# ---------------- 4) imagem de conclusão 1280x720 ----------------
ch4, chcss4 = chips(14, "8px 16px", "8px")
CONCLUSAO = f"""<style>{BASE}
html,body{{width:1280px;height:720px}} .art{{width:1280px;height:720px;padding:74px 78px;text-align:center}}
.eyebrow{{font-size:17px;letter-spacing:.24em}} .rule{{width:110px;margin:20px auto 26px}}
h1{{font-size:64px}} .sub{{font-size:25px;margin-top:22px;line-height:1.45}}
{chcss4} .steps{{margin-top:34px;justify-content:center}}
.next{{margin-top:38px;font-size:18px;color:#EDE6FA;line-height:1.6}}
.next b{{color:#3FD8E8;font-family:'League Spartan',sans-serif;letter-spacing:.04em}}
.foot{{bottom:44px;left:78px;right:78px}}
</style>
<div class="art">
  <div class="eyebrow">Você concluiu o caminho</div>
  <div class="rule"></div>
  <h1>Parabéns!</h1>
  <div class="sub">Você percorreu os 6 passos do <strong style="color:#fff;font-style:normal;font-family:'League Spartan',sans-serif">Método Mãos Seguras</strong>.<br/>Agora é praticar — um coração por vez.</div>
  {ch4}
  <div class="next">Seu próximo passo: <b>mentoria individual</b> com o Mestre Renato<br/>ou o <b>Reiki Nível II presencial</b>, na comunidade Om Reiki Om.</div>
  <div class="foot"><span class="b">OM REIKI OM</span><span class="u">reikibrasilia.br.com</span></div>
</div>"""

ARTES = {
    "capa-produto-1080": CAPA,
    "banner-vitrine-1200x628": VITRINE,
    "banner-checkout-1200x400": CHECKOUT,
    "imagem-conclusao-1280x720": CONCLUSAO,
}

here = os.path.dirname(os.path.abspath(__file__))
for name, body in ARTES.items():
    html = f"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'></head><body>{body}</body></html>"
    open(os.path.join(here, name + ".html"), "w", encoding="utf-8").write(html)
    print("html:", name)
print("ok")
