# -*- coding: utf-8 -*-
"""portal.py — landing de las guías (misma marca: blanco, Poppins, sombras sin bordes)."""
import html
import kit

CSS = """
@font-face{ font-family:'Poppins'; src:url('fonts/Poppins-Regular.ttf') format('truetype'); font-weight:400; font-display:swap; }
@font-face{ font-family:'Poppins'; src:url('fonts/Poppins-Medium.ttf') format('truetype'); font-weight:500; font-display:swap; }
@font-face{ font-family:'Poppins'; src:url('fonts/Poppins-SemiBold.ttf') format('truetype'); font-weight:600; font-display:swap; }
@font-face{ font-family:'Poppins'; src:url('fonts/Poppins-Black.ttf') format('truetype'); font-weight:900; font-display:swap; }
@font-face{ font-family:'Poppins'; src:url('fonts/Poppins-BlackItalic.ttf') format('truetype'); font-weight:900; font-style:italic; font-display:swap; }
:root{ --violet:#5E3AE2; --gold:#F4B422; --green:#00AA80; --navy:#000087; --sky:#2CAAFF; --sand:#E4E4DB; --ink:#373435;
  --gutter:clamp(20px,4vw,64px); }
*{ box-sizing:border-box; margin:0; padding:0; }
html{ scroll-behavior:smooth; }
body{ background:#fff; color:var(--ink); font-family:'Poppins','Segoe UI',sans-serif; -webkit-font-smoothing:antialiased; line-height:1.5; }
a{ color:inherit; text-decoration:none; }
.bar{ position:sticky; top:0; z-index:20; height:76px; padding:0 var(--gutter); display:flex; align-items:center; gap:20px; background:#fff; box-shadow:0 8px 26px rgba(0,0,135,.10), 0 1px 4px rgba(0,0,135,.06); }
.bar img{ height:44px; width:auto; display:block; }
.chip{ display:inline-flex; align-items:center; font-weight:900; font-size:10px; letter-spacing:.14em; text-transform:uppercase; border-radius:99px; padding:6px 14px; background:rgba(94,58,226,.12); color:var(--violet); }
.hero{ position:relative; overflow:hidden; padding:clamp(40px,7vw,88px) var(--gutter) clamp(28px,4vw,48px); }
.hero svg.deco{ position:absolute; inset:0; width:100%; height:100%; z-index:0; pointer-events:none; }
.hero svg.deco .ring{ fill:none; stroke:rgba(0,0,135,.07); stroke-width:1; } .hero svg.deco .ring.accent{ stroke:rgba(94,58,226,.28); }
.hero > *:not(svg){ position:relative; z-index:1; }
h1{ font-weight:900; font-size:clamp(30px,5vw,54px); line-height:1.06; letter-spacing:-.012em; color:var(--navy); max-width:16em; }
h1 .m{ color:var(--violet); } h1 em{ color:var(--violet); font-style:italic; }
.lede{ margin-top:20px; font-size:clamp(15px,1.6vw,18px); max-width:44em; }
.legend{ margin-top:26px; display:flex; flex-wrap:wrap; gap:14px; }
.legend div{ display:flex; align-items:center; gap:12px; padding:12px 18px; border-radius:16px; background:#fff; box-shadow:0 12px 30px rgba(0,0,135,.12), 0 2px 7px rgba(0,0,135,.06); font-size:13.5px; }
.legend b{ color:var(--navy); font-weight:600; }
.pill{ display:inline-flex; font-weight:900; font-size:9.5px; letter-spacing:.14em; text-transform:uppercase; border-radius:99px; padding:5px 12px; }
.pill.dev{ background:var(--gold); color:var(--navy); } .pill.usr{ background:var(--violet); color:#fff; }
main{ padding:8px var(--gutter) 72px; }
.grid{ display:grid; grid-template-columns:repeat(auto-fill,minmax(min(100%,360px),1fr)); gap:26px; }
.card{ position:relative; overflow:hidden; display:flex; flex-direction:column; gap:14px; padding:28px; border-radius:20px; background:#fff; box-shadow:0 12px 30px rgba(0,0,135,.13), 0 2px 7px rgba(0,0,135,.07); transition:transform .25s ease, box-shadow .25s ease; }
.card:hover{ transform:translateY(-3px); box-shadow:0 18px 38px rgba(0,0,135,.17), 0 2px 7px rgba(0,0,135,.07); }
.card::before{ content:""; position:absolute; right:0; top:0; width:100%; height:100%; background:radial-gradient(circle at 100% 0%, transparent 0 54px, rgba(0,0,135,.045) 54px 96px, transparent 96px 118px, rgba(0,0,135,.045) 118px 148px, transparent 148px); pointer-events:none; }
.card > *{ position:relative; }
.num{ position:absolute !important; right:22px; top:14px; font-weight:900; font-size:40px; line-height:1; color:rgba(0,0,135,.07); filter:blur(1px); }
.ic{ width:52px; height:52px; border-radius:16px; display:grid; place-items:center; background:var(--violet); color:#fff; }
.card:nth-child(4n+2) .ic{ background:var(--navy); color:var(--gold); } .card:nth-child(4n+3) .ic{ background:var(--sky); color:var(--navy); } .card:nth-child(4n+4) .ic{ background:var(--green); color:#fff; }
.ic svg{ width:28px; height:28px; fill:none; stroke:currentColor; stroke-width:1.9; stroke-linecap:round; stroke-linejoin:round; }
h2{ font-weight:900; font-size:21px; line-height:1.15; color:var(--navy); }
.meta{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.meta .pill{ background:rgba(0,0,135,.08); color:var(--navy); }
.card p{ font-size:14px; }
.guides{ margin-top:auto; display:flex; flex-direction:column; gap:10px; padding-top:6px; }
.row{ display:flex; align-items:center; justify-content:space-between; gap:10px; padding:10px 12px 10px 16px; border-radius:14px; background:rgba(0,0,135,.04); }
.btns{ display:flex; gap:8px; }
.btn{ display:inline-flex; align-items:center; gap:6px; font-weight:600; font-size:12.5px; padding:8px 14px; border-radius:99px; background:#fff; color:var(--navy); box-shadow:0 5px 14px rgba(0,0,135,.16), 0 1px 3px rgba(0,0,135,.10); transition:background .2s, box-shadow .2s; min-height:36px; }
.btn:hover{ background:var(--gold); box-shadow:0 8px 20px rgba(244,180,34,.45), 0 1px 3px rgba(0,0,135,.10); }
.btn:focus-visible{ outline:3px solid var(--violet); outline-offset:2px; }
.btn svg{ width:15px; height:15px; fill:none; stroke:currentColor; stroke-width:2.2; stroke-linecap:round; stroke-linejoin:round; }
.btn.pdf{ background:var(--navy); color:#fff; } .btn.pdf:hover{ background:var(--violet); box-shadow:0 8px 20px rgba(94,58,226,.4); }
footer{ padding:26px var(--gutter) 34px; font-size:12px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px; opacity:.8; }
@media (max-width:560px){ .bar{ height:64px; } .bar img{ height:30px; } .card{ padding:22px; } .row{ flex-direction:column; align-items:flex-start; } }
@media print{ .bar{ position:static; } }
"""

DECO = ('<svg class="deco" viewBox="0 0 1200 400" preserveAspectRatio="xMaxYMid slice" aria-hidden="true">'
        '<circle class="ring accent" cx="1020" cy="200" r="120"/><circle class="ring" cx="1020" cy="200" r="190"/>'
        '<circle class="ring" cx="1020" cy="200" r="270"/><circle class="ring" cx="1020" cy="200" r="360"/></svg>')

OPEN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
DL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>'


def render(root, metas):
    (root / 'assets' / 'portal.css').write_text(CSS, encoding='utf-8')
    cards = []
    for i, m in enumerate(metas):
        def row(kind, label, pill):
            base = '%s/%s/' % (m['slug'], kind)
            nice = '%s - %s.pdf' % ('Guia Dev' if kind == 'dev' else 'Guia Usuario', m['nombre'])
            return ('<div class="row"><span class="pill %s">%s</span><span class="btns">'
                    '<a class="btn" href="%sindex.html" aria-label="Abrir %s de %s">Web %s</a>'
                    '<a class="btn pdf" href="%sguia-%s.pdf" download="%s" aria-label="Descargar PDF de %s de %s">PDF %s</a></span></div>'
                    % (pill, label, base, label, html.escape(m['nombre']), OPEN, base, kind, html.escape(nice), label, html.escape(m['nombre']), DL))
        cards.append(
            '<article class="card"><span class="num">%02d</span><span class="ic">%s</span><h2>%s</h2>'
            '<div class="meta"><span class="pill">%s</span><span class="pill">%s</span></div><p>%s</p>'
            '<div class="guides">%s%s</div></article>'
            % (i + 1, kit.svg(m['icono']), html.escape(m['nombre']), html.escape(m['rol']), html.escape(m['plataforma']), html.escape(m['resumen']),
               row('dev', 'Guía Dev', 'dev'), row('usuario', 'Guía de usuario', 'usr')))
    page = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Guías de los agentes — FullService</title>
  <link rel="icon" type="image/png" href="assets/img/favicon.png">
  <link rel="stylesheet" href="assets/portal.css">
</head>
<body>
  <header class="bar"><img src="assets/img/logo-campuslands-color.png" alt="Campuslands"><span class="chip">Guías de los agentes</span></header>
  <section class="hero">%s
    <h1><span class="m">&lt;/</span>Guías de uso de los <em>7 agentes</em> FullService</h1>
    <p class="lede">Cada agente tiene dos guías: una <b>técnica</b>, para quien mantiene el agente, y una <b>de usuario</b>, sin tecnicismos, para quien lo usa en el día a día. Ábrelas en la web o descárgalas en PDF.</p>
    <div class="legend">
      <div><span class="pill dev">Guía Dev</span><span><b>Developers.</b> Carpetas, ciclos, reglas, scripts y mantenimiento.</span></div>
      <div><span class="pill usr">Guía de usuario</span><span><b>Cualquier persona.</b> Qué pedir, qué recibes y cómo revisarlo.</span></div>
    </div>
  </section>
  <main><div class="grid">%s</div></main>
  <footer><span>Campuslands S.A.S. BIC · Full Service</span><span>Exploramos · Despegamos · Conquistamos</span></footer>
</body>
</html>
""" % (DECO, ''.join(cards))
    (root / 'index.html').write_text(page, encoding='utf-8')
