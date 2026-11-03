# -*- coding: utf-8 -*-
"""build.py — genera las guías (web + PDF) y el índice a partir de contenido/<agente>/{dev,usuario}.md

Uso:  python -X utf8 guias/_src/build.py [slug ...] [--sin-pdf]
Salida: guias/<agente>/guia-{dev,usuario}.html y .pdf · guias/index.html
"""
import html
import pathlib
import sys

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding='utf-8')
    except Exception:
        pass
import md  # noqa: E402

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
FECHA = '3 nov 2026'

# orden del pipeline comercial
AGENTES = [
    dict(slug='prospection-agent', nombre='Radar de Campus', rol='Prospección de empresas', plataforma='Perplexity',
         resumen='Busca en la web abierta las empresas que encajan con el perfil de cliente de Campuslands y entrega un listado con datos públicos verificables.'),
    dict(slug='intelligence-commercial', nombre='Explorador de Campus', rol='Inteligencia comercial en LinkedIn', plataforma='Perplexity',
         resumen='Toma una lista de empresas, encuentra a los contactos clave de cada una y les envía solicitudes de conexión personalizadas.'),
    dict(slug='presentations-designer', nombre='Estudio de Presentaciones', rol='Presentaciones comerciales', plataforma='Claude Code',
         resumen='Construye presentaciones comerciales por cliente bajo el Brandbook de Campuslands, las exporta a PDF y las publica con un link.'),
    dict(slug='functional-scope', nombre='Alcances Funcionales', rol='Documentos de alcance funcional', plataforma='Claude Code',
         resumen='Lee las fuentes de un proyecto, detecta contradicciones y vacíos y redacta el alcance funcional para el cliente, sin inventar compromisos.'),
    dict(slug='quote-developer-v2', nombre='Desarrollador de Cotizaciones', rol='Cotizaciones: PDF + XLSX', plataforma='Claude Code',
         resumen='A partir de los alcances genera el PDF de cotización de alcance y llena la plantilla XLSX de costos del equipo Campus.'),
    dict(slug='bidding-agent', nombre='Agente Licitatorio', rol='Licitaciones y preventa técnica', plataforma='Claude Code',
         resumen='Analiza los cuatro documentos de una licitación y construye la propuesta técnica, la estimación de horas y el análisis de IA.'),
    dict(slug='contract-perfectionist', nombre='Contract Perfectionist', rol='Redacción de contratos', plataforma='Claude Code',
         resumen='Redacta el contrato final de un proyecto a partir de los alcances, la cotización y el contrato madre, listo para firma.'),
]
TIPOS = {'dev': 'Guía Dev', 'usuario': 'Guía de usuario'}
DL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>'

JS = """<script>
(function(){var l=[].slice.call(document.querySelectorAll('.toc a'));if(!l.length||!('IntersectionObserver'in window))return;
var m={};l.forEach(function(a){m[a.getAttribute('href').slice(1)]=a});
var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){l.forEach(function(a){a.classList.remove('on')});var a=m[e.target.id];if(a)a.classList.add('on')}})},{rootMargin:'-80px 0px -70% 0px'});
document.querySelectorAll('article h2').forEach(function(h){o.observe(h)})})();
</script>"""


def head(title, rel):
    return ('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>%s</title>\n<link rel="icon" type="image/png" href="%sassets/img/favicon.png">\n<link rel="stylesheet" href="%sassets/estilo.css">\n</head>\n<body>\n'
            % (html.escape(title), rel, rel))


def topbar(rel, pdf=None):
    btn = ('<a class="btn" href="%s" download>%s Descargar PDF</a>' % (pdf, DL)) if pdf else ''
    return ('<header class="top"><div class="top-in"><a class="brand" href="%sindex.html"><img src="%sassets/img/logo-campuslands-color.png" alt="Campuslands"><span>Guías de los agentes</span></a>'
            '<nav><a href="%sindex.html">Todas las guías</a>%s</nav></div></header>\n' % (rel, rel, rel, btn))


def scripts(rel):
    """Scroll suave (Lenis) en todas las páginas; suave.js lo activa."""
    return '<script src="%sassets/lenis.min.js"></script>\n<script src="%sassets/suave.js"></script>' % (rel, rel)


def guide_page(ag, kind, meta, body, toc, words):
    other = 'usuario' if kind == 'dev' else 'dev'
    mins = max(1, round(words / 210))
    title = meta.get('titulo', ag['nombre'])
    tocs = ''.join('<li><a href="#%s">%s</a></li>' % (i, html.escape(t)) for i, t in toc)
    page = head('%s — %s' % (title, ag['nombre']), '../') + topbar('../', 'guia-%s.pdf' % kind)
    page += ('<div class="shell"><aside class="toc" data-lenis-prevent><p>En esta guía</p><ol>%s</ol></aside>\n<article>\n'
             '<p class="kicker">%s · %s</p>\n<h1>%s</h1>\n<p class="dek">%s</p>\n'
             '<div class="chips"><span>%s</span><span>%s</span><span>%s</span><span>%d min de lectura</span></div>\n%s\n'
             '<div class="more"><span>¿Buscas la otra mirada de este agente?</span><nav>'
             '<a class="btn ghost" href="guia-%s.html">%s</a><a class="btn ghost" href="../index.html">Todas las guías</a></nav></div>\n</article></div>\n%s\n%s\n</body>\n</html>\n'
             % (tocs, TIPOS[kind], html.escape(ag['nombre']), md.inline(title), md.inline(meta.get('resumen', '')),
                FECHA, TIPOS[kind], html.escape(ag['slug']), mins, body, other, TIPOS[other], scripts('../'), JS))
    return page


def index_page(items):
    by = {(ag['slug'], m['tipo']): (m, w) for ag, m, w in items}

    def rows(kind):
        out = ''
        for ag in AGENTES:
            if (ag['slug'], kind) not in by:
                continue
            m, w = by[(ag['slug'], kind)]
            base = '%s/guia-%s' % (ag['slug'], kind)
            nice = '%s - %s.pdf' % ('Guia Dev' if kind == 'dev' else 'Guia Usuario', ag['nombre'])
            out += ('<div class="ag"><div><h3>%s</h3><small>%s · %s</small></div><p><b>%s</b>%s</p>'
                    '<div class="go"><small>%d min</small><a class="btn" href="%s.html">Leer</a>'
                    '<a class="btn ghost" href="%s.pdf" download="%s" aria-label="Descargar PDF de %s">PDF</a></div></div>\n'
                    % (html.escape(ag['nombre']), html.escape(ag['rol']), html.escape(ag['plataforma']), md.inline(m['titulo']), md.inline(m['resumen']),
                       max(1, round(w / 210)), base, base, html.escape(nice), html.escape(ag['nombre'])))
        return out
    page = head('Guías de los agentes — FullService', '') + topbar('')
    page += ('<main class="home"><p class="kicker">Campuslands · Full Service</p><h1>Guías de uso de los agentes</h1>'
             '<p class="dek">Siete agentes, dos guías cada uno: una para quien los usa todos los días y otra para quien los mantiene.</p>'
             '<div class="chips"><span>%s</span><span>7 agentes</span><span>14 guías</span></div>'
             '<div class="pick">'
             '<a href="#usuario"><small>Para usar el agente</small><b>Guías de usuario</b><span>Qué entregarle, cómo pedirlo, qué recibes y cómo revisarlo. Sin tecnicismos.</span><em>Ver las 7 guías →</em></a>'
             '<a href="#dev"><small>Para mantenerlo</small><b>Guías Dev</b><span>Arquitectura, ciclos de trabajo, formatos, reglas, scripts y verificación.</span><em>Ver las 7 guías →</em></a></div>'
             '<h2 id="usuario">Guías de usuario</h2><p class="sub">En el orden del flujo comercial, de la prospección al contrato.</p><div class="agents">%s</div>'
             '<h2 id="dev">Guías Dev</h2><p class="sub">Cómo está construido cada agente y cómo se mantiene.</p><div class="agents">%s</div></main>\n'
             '<footer class="site"><span>Campuslands S.A.S. BIC · Full Service</span><span>Exploramos · Despegamos · Conquistamos</span></footer>\n%s\n</body>\n</html>\n'
             % (FECHA, rows('usuario'), rows('dev'), scripts('')))
    return page


def make_pdf(html_path, pdf_path, title):
    from playwright.sync_api import sync_playwright
    hdr = ('<div style="width:100%%;padding:0 20mm;font:8px Arial,sans-serif;color:#87867f">%s</div>' % html.escape(title))
    ftr = ('<div style="width:100%;padding:0 20mm;font:8px Arial,sans-serif;color:#87867f;text-align:right">'
           'Página <span class="pageNumber"></span> de <span class="totalPages"></span></div>')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page()
        pg.goto(html_path.as_uri())
        pg.emulate_media(media='print')
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(500)
        pg.pdf(path=str(pdf_path), format='A4', print_background=True, display_header_footer=True, header_template=hdr, footer_template=ftr,
               margin=dict(top='22mm', bottom='20mm', left='20mm', right='20mm'))
        b.close()


def check_scale():
    """La hoja de estilos solo puede usar la escala tipográfica (variables --t-*): evita tamaños sueltos."""
    import re
    css = (SRC / 'estilo.css').read_text(encoding='utf-8')
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r':root\{[^}]*\}', '', css)            # definiciones de la escala
    css = re.sub(r'@media[^{]*\{\s*:root\{[^}]*\}', '@media{', css)   # redefiniciones por ancho / impresión
    bad = [v for v in re.findall(r'font-size:\s*([^;}]+)', css) if not (v.strip().startswith('var(--t-') or v.strip() == 'inherit')]
    if bad:
        raise SystemExit('estilo.css usa tamaños fuera de la escala: %s' % sorted(set(bad)))


def build(only=None, pdf=True):
    check_scale()
    (ROOT / 'assets').mkdir(exist_ok=True)
    (ROOT / 'assets' / 'estilo.css').write_text((SRC / 'estilo.css').read_text(encoding='utf-8'), encoding='utf-8')
    (ROOT / 'assets' / 'suave.js').write_text((SRC / 'suave.js').read_text(encoding='utf-8'), encoding='utf-8')
    items = []
    for ag in AGENTES:
        for kind in ('dev', 'usuario'):
            src = SRC / 'contenido' / ag['slug'] / ('%s.md' % kind)
            if not src.exists():
                continue
            meta, body, toc, words = md.convert(src.read_text(encoding='utf-8'))
            meta['tipo'] = kind
            items.append((ag, meta, words))
            if only and ag['slug'] not in only:
                continue
            out = ROOT / ag['slug']
            out.mkdir(exist_ok=True)
            hp = out / ('guia-%s.html' % kind)
            hp.write_text(guide_page(ag, kind, meta, body, toc, words), encoding='utf-8')
            print('  %-26s %-8s %5d palabras · %d secciones' % (ag['slug'], kind, words, len(toc)))
            if pdf:
                make_pdf(hp, out / ('guia-%s.pdf' % kind), '%s · %s' % (ag['nombre'], TIPOS[kind]))
    (ROOT / 'index.html').write_text(index_page(items), encoding='utf-8')


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    build(args or None, '--sin-pdf' not in sys.argv)
