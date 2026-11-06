# -*- coding: utf-8 -*-
"""preview.py — genera las imágenes de vista previa del enlace (Open Graph / Twitter, 1200 × 630) de la web.

Uso:  python -X utf8 guides/_src/preview.py            (todas)
      python -X utf8 guides/_src/preview.py home       (solo la del índice)

Salida: guides/assets/img/preview/home.png y guides/assets/img/preview/<agente>-<usuario|dev>.png
Se renderizan con Chrome (Playwright) sobre las mismas fuentes, colores e iconos 3D del banner del índice, así que mantienen su identidad.
Las imágenes se versionan; vuelve a correr el script cuando cambien los textos de las guías, el nombre de un agente o el diseño.
"""
import html
import pathlib
import re
import sys

SRC = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))
import build  # noqa: E402

ROOT = build.ROOT
SALIDA = ROOT / 'assets' / 'img' / 'preview'
TMP = ROOT / '_preview_tmp.html'

CSS = """
@font-face{ font-family:'Source Serif 4'; src:url('assets/fonts/SourceSerif4.ttf') format('truetype'); font-weight:200 900; }
@font-face{ font-family:'Source Serif 4'; src:url('assets/fonts/SourceSerif4-Italic.ttf') format('truetype'); font-weight:200 900; font-style:italic; }
@font-face{ font-family:'Inter'; src:url('assets/fonts/Inter.ttf') format('truetype'); font-weight:100 900; }
*{ box-sizing:border-box; margin:0; padding:0; }
:root{ --ink:#141413; --muted:#5e5d59; --soft:#87867f; --cream:#f5f4ed; --oat:#f0eee6; --line:#e6e3d8; --clay:#d97757; --clay-d:#b9532f; }
html,body{ width:1200px; height:630px; overflow:hidden; background:var(--cream); }
body{ position:relative; font-family:'Inter',sans-serif; color:var(--ink); -webkit-font-smoothing:antialiased; }
*{ animation:none !important; }
/* aros concéntricos (los del banner) y un velo de luz a la derecha */
.aros{ position:absolute; right:-150px; top:50%; width:860px; height:860px; transform:translateY(-50%); border-radius:50%;
  background:repeating-radial-gradient(circle, transparent 0 40px, rgba(217,119,87,.24) 40px 41px);
  -webkit-mask-image:radial-gradient(circle, #000 18%, transparent 68%); mask-image:radial-gradient(circle, #000 18%, transparent 68%); }
.velo{ position:absolute; right:-80px; top:-40px; width:760px; height:760px; background:radial-gradient(circle, rgba(255,255,255,.75) 0%, transparent 62%); }
.marco{ position:absolute; inset:0; border:1px solid rgba(20,20,19,.07); }
.marca{ position:absolute; left:72px; top:56px; display:flex; align-items:center; gap:18px; }
.marca img{ height:42px; width:auto; }
.marca i{ width:1px; height:26px; background:var(--line); }
.marca span{ font-family:'Source Serif 4',serif; font-size:25px; letter-spacing:-.01em; color:var(--ink); }
.txt{ position:absolute; left:72px; width:690px; }
h1{ font-family:'Source Serif 4',serif; font-weight:400; letter-spacing:-.02em; line-height:1.04; color:var(--ink); }
.dek{ font-family:'Source Serif 4',serif; color:var(--muted); line-height:1.42; }
.kicker{ font-weight:600; font-size:21px; letter-spacing:.1em; text-transform:uppercase; color:var(--clay-d); }
.nombre{ font-size:27px; color:var(--muted); margin:14px 0 10px; }
.pie{ position:absolute; left:72px; bottom:54px; display:flex; align-items:center; gap:14px; font-size:23px; color:var(--muted); }
.pill{ display:inline-flex; align-items:center; gap:12px; padding:11px 22px 11px 13px; border-radius:99px; background:#fff; border:1px solid var(--line); font-weight:500; color:var(--ink); }
.pill img{ width:30px; height:30px; border-radius:8px; }
.pie .pt{ color:var(--soft); }
/* iconos 3D (mismas capas que el banner), quietos y con el giro del cursor ya aplicado */
.escena{ position:absolute; inset:0; --px:-.8; --py:.4; }
.ico{ position:absolute; width:var(--s); height:var(--s); perspective:900px; }
.ico-claude{ --s:250px; --glow:rgba(217,119,87,.6); --edge:#b9532f; --edge2:#8f3f24; left:800px; top:96px; }
.ico-pplx{ --s:206px; --glow:rgba(32,184,205,.5); --edge:#2a2a28; --edge2:#0d0d0c; left:938px; top:318px; }
.solo.ico-claude, .solo.ico-pplx{ --s:300px; left:840px; top:165px; }
.ico-glow{ position:absolute; inset:-38%; border-radius:50%; background:radial-gradient(circle, var(--glow) 0%, transparent 62%); filter:blur(22px); opacity:.6; }
.ico-tilt{ position:relative; width:100%; height:100%; transform-style:preserve-3d; transform:rotateX(calc(var(--py) * -14deg)) rotateY(calc(var(--px) * 16deg)); }
.ico-spin, .ico-float{ position:relative; width:100%; height:100%; transform-style:preserve-3d; }
.ico-float::before, .ico-float::after{ content:""; position:absolute; inset:0; border-radius:23%; }
.ico-float::before{ background:var(--edge); transform:translateZ(-14px); }
.ico-float::after{ background:var(--edge2); transform:translateZ(-28px); box-shadow:0 38px 56px -14px rgba(20,20,19,.38); }
.ico-face{ position:relative; display:block; width:100%; height:100%; border-radius:23%; overflow:hidden; box-shadow:inset 0 1px 0 rgba(255,255,255,.4), 0 0 0 1px rgba(255,255,255,.1); }
.ico-face img{ display:block; width:100%; height:100%; object-fit:cover; }
.ico-face::after{ content:""; position:absolute; inset:0; background:linear-gradient(115deg, transparent 38%, rgba(255,255,255,.34) 50%, transparent 62%); }
"""


def ico(clase, img, extra=''):
    return ('<div class="ico %s%s"><span class="ico-glow"></span><div class="ico-tilt"><div class="ico-spin"><div class="ico-float">'
            '<span class="ico-face"><img src="assets/img/%s" alt=""></span></div></div></div></div>' % (clase, extra, img))


def pagina(cuerpo):
    return ('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><style>%s</style></head><body><div class="aros"></div><div class="velo"></div>'
            '<div class="marco"></div>%s</body></html>' % (CSS, cuerpo))


def home():
    n = len(build.AGENTES)
    return pagina(
        '<div class="marca"><img src="assets/img/logo-campuslands-color.png" alt=""></div>'
        '<div class="txt" style="top:158px"><h1 style="font-size:96px;white-space:nowrap">fullservice-agents</h1>'
        '<p class="dek" style="font-size:30px;margin-top:24px;max-width:650px">Guías de usuario y de desarrollador de los %s agentes de Campuslands, del flujo comercial al multifuncional.</p></div>'
        '<div class="pie"><span class="pill"><img src="assets/img/plataforma-claude.png" alt="">Claude Code</span><span class="pill"><img src="assets/img/plataforma-perplexity.png" alt="">Perplexity</span>'
        '<span class="pt">· %d guías · HTML y PDF</span></div>'
        '<div class="escena">%s%s</div>' % ({7: 'siete', 8: 'ocho'}.get(n, n), n * 2, ico('ico-claude', 'plataforma-claude-lg.png'), ico('ico-pplx', 'plataforma-perplexity-lg.png')))


def guia(ag, kind, titulo):
    clave = 'ico-pplx' if ag['plataforma'] == 'Perplexity' else 'ico-claude'
    img = 'plataforma-perplexity-lg.png' if ag['plataforma'] == 'Perplexity' else 'plataforma-claude-lg.png'
    chip = 'plataforma-perplexity.png' if ag['plataforma'] == 'Perplexity' else 'plataforma-claude.png'
    slug = ag['slug']
    tam = max(56, min(100, int(690 / (len(slug) * 0.43))))                          # el nombre del agente cabe siempre en una línea
    return pagina(
        '<div class="marca"><img src="assets/img/logo-campuslands-color.png" alt=""><i></i><span>fullservice-agents</span></div>'
        '<div class="txt" style="top:158px"><p class="kicker">%s</p><p class="nombre">%s</p><h1 style="font-size:%dpx;white-space:nowrap">%s</h1>'
        '<p class="dek" style="font-size:31px;margin-top:26px;max-width:640px">%s</p></div>'
        '<div class="pie"><span class="pill"><img src="assets/img/%s" alt="">%s</span></div>'
        '<div class="escena">%s</div>'
        % (html.escape(build.TIPOS[kind]), html.escape(ag['nombre']), tam, html.escape(slug), html.escape(titulo), chip, html.escape(ag['plataforma']), ico(clave, img, ' solo')))


def titulos():
    out = {}
    for ag in build.AGENTES:
        for kind in ('usuario', 'dev'):
            f = build.SRC / 'contenido' / ag['slug'] / ('%s.md' % kind)
            if f.exists():
                meta, *_ = build.md.convert(f.read_text(encoding='utf-8'))
                out[(ag['slug'], kind)] = re.sub(r'<[^>]+>', '', build.md.inline(build.corto(meta['titulo'])))
    return out


def main():
    from playwright.sync_api import sync_playwright
    solo = [a for a in sys.argv[1:] if not a.startswith('--')]
    SALIDA.mkdir(parents=True, exist_ok=True)
    trabajos = [('home', home())]
    t = titulos()
    for ag in build.AGENTES:
        for kind in ('usuario', 'dev'):
            if (ag['slug'], kind) in t:
                trabajos.append(('%s-%s' % (ag['slug'], kind), guia(ag, kind, t[(ag['slug'], kind)])))
    if solo:
        trabajos = [j for j in trabajos if j[0] in solo or any(j[0].startswith(s) for s in solo)]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=build.CHROME)
        pg = b.new_page(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
        for nombre, doc in trabajos:
            TMP.write_text(doc, encoding='utf-8')
            pg.goto(TMP.as_uri())
            pg.evaluate('document.fonts.ready')
            pg.wait_for_function('[...document.images].every(i => i.complete)')
            pg.wait_for_timeout(150)
            destino = SALIDA / ('%s.png' % nombre)
            pg.screenshot(path=str(destino))
            print('  %-40s %4d KB' % (destino.name, destino.stat().st_size // 1024))
        b.close()
    TMP.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
