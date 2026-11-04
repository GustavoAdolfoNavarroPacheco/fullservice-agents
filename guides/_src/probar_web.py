# -*- coding: utf-8 -*-
"""probar_web.py — prueba el comportamiento de la web en un navegador real (Chrome + Playwright).

Uso:  python -X utf8 guides/_src/probar_web.py [http://127.0.0.1:4173]
Comprueba en el índice y en una guía: Lenis cargado y activo, scroll de ancla realmente progresivo, rueda con inercia,
sin errores de consola, sin desborde horizontal (4 anchos) y solo los tamaños de fuente de la escala.
"""
import json
import sys
import urllib.request

from playwright.sync_api import sync_playwright

BASE = (sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:4173').rstrip('/')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
ESCALA = {13, 15, 17, 20, 32, 40, 52}
FUENTES = """() => { const m = {}; document.querySelectorAll('body *').forEach(e => { if (e instanceof SVGElement) return; const t = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()); if (!t) return; const s = getComputedStyle(e); if (s.display === 'none') return; m[Math.round(parseFloat(s.fontSize))] = 1; }); return Object.keys(m).map(Number); }"""
ok = True


def check(nombre, cond, detalle=''):
    global ok
    ok &= bool(cond)
    print('%s %s %s' % ('✓' if cond else '✗', nombre, detalle))


with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    for ruta in ('/', '/bidding-agent/guia-dev.html'):
        print('\n== %s' % ruta)
        pg = b.new_page(viewport={'width': 1366, 'height': 800})
        errores = []
        pg.on('console', lambda m: errores.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errores.append(str(e)))
        pg.goto(BASE + ruta)
        pg.wait_for_timeout(600)
        check('Lenis cargado', pg.evaluate("typeof window.lenis === 'object' && window.lenis !== null"))
        check('html tiene la clase lenis', pg.evaluate("document.documentElement.classList.contains('lenis')"))
        # ancla: debe avanzar en varios pasos, no saltar de golpe
        # cabecera: marca y botón de GitHub
        check('marca «fullservice-agents» en la cabecera', pg.inner_text('.brand span').strip() == 'fullservice-agents')
        check('marca en la fuente del banner (serif)', 'Source Serif' in pg.evaluate("getComputedStyle(document.querySelector('.brand span')).fontFamily"))
        gh = pg.evaluate("(()=>{const a=document.querySelector('.top nav a.gh');return a?{h:a.href,t:a.target,r:a.rel}:null})()")
        check('botón de GitHub apunta al repo', gh and gh['h'] == 'https://github.com/GustavoAdolfoNavarroPacheco/fullservice-agents' and gh['t'] == '_blank' and 'noopener' in gh['r'], str(gh))
        check('ya no hay botones de guías en la cabecera', pg.evaluate("![...document.querySelectorAll('.top nav a')].some(a=>/Guía (de usuario|de desarrollador|Dev)/i.test(a.textContent))"))
        if ruta == '/':
            vis = "(()=>['usuario','dev'].map(i=>!document.getElementById(i).hidden))()"
            check('pestañas: al abrir se ve solo la guía de usuario', pg.evaluate(vis) == [True, False] and pg.inner_text('#tab-dev') == 'Guía de desarrollador')
            pg.click('#tab-dev'); pg.wait_for_timeout(500)
            x = pg.evaluate("(()=>{const i=document.querySelector('.tab-ind').getBoundingClientRect(),t=document.getElementById('tab-dev').getBoundingClientRect();return [Math.round(i.left-t.left),Math.round(i.width-t.width)]})()")
            check('pestañas: cambia a desarrollador y el indicador la sigue', pg.evaluate(vis) == [False, True] and x == [0, 0] and pg.evaluate('location.hash') == '#dev', str(x))
            pg.focus('#tab-dev'); pg.keyboard.press('ArrowLeft'); pg.wait_for_timeout(300)
            check('pestañas: flechas del teclado', pg.evaluate(vis) == [True, False])
            pg.goto(BASE + '/#dev'); pg.reload(); pg.wait_for_timeout(400)
            check('pestañas: #dev abre la guía de desarrollador', pg.evaluate(vis) == [False, True])
            pg.goto(BASE + '/'); pg.wait_for_timeout(300)
            check('filas sin botón «Leer»', pg.evaluate("![...document.querySelectorAll('.ag .btn')].some(a=>/Leer/.test(a.textContent))"))
            bb = pg.evaluate("(()=>{const r=document.querySelector('.ag:first-child p').getBoundingClientRect();return [r.x+r.width/2, r.y+r.height/2]})()")
            pg.mouse.click(bb[0], bb[1])                        # clic en el resumen, no en el título: toda la fila es el enlace
            pg.wait_for_url('**/prospection-agent/guia-usuario.html', timeout=4000)
            check('clic en cualquier parte de la fila abre la guía', pg.url.endswith('/prospection-agent/guia-usuario.html'), pg.url)
            pg.goto(BASE + '/'); pg.wait_for_timeout(300)
            with pg.expect_download() as d:
                pg.click('.ag:first-child .pdf')
            check('el botón PDF descarga y no abre la guía', pg.url.endswith('/') and d.value.suggested_filename == 'Guia Usuario - prospection-agent.pdf', d.value.suggested_filename)
        r0 = pg.evaluate("(()=>{const f=document.querySelector('.gh-fill').getBoundingClientRect(), g=document.querySelector('.gh').getBoundingClientRect();return f.top-g.top})()")
        pg.hover('.top nav a.gh')
        pg.wait_for_timeout(900)
        r1 = pg.evaluate("(()=>{const f=document.querySelector('.gh-fill').getBoundingClientRect(), g=document.querySelector('.gh').getBoundingClientRect();return f.top-g.top})()")
        color = pg.evaluate("getComputedStyle(document.querySelector('.gh')).color")
        check('hover: el relleno sube y el texto se invierte', r0 > 10 and abs(r1) < 2 and color == 'rgb(255, 255, 255)', '(relleno %dpx → %dpx; color %s)' % (r0, r1, color))
        pg.mouse.move(5, 400)
        pg.wait_for_timeout(300)
        # ancla: debe avanzar en varios pasos, no saltar de golpe (solo en las guías; el índice no tiene anclas)
        if ruta != '/':
            destino = '#las-cinco-habilidades'
            pg.evaluate("window.scrollTo(0,0)")
            pg.wait_for_timeout(300)
            pg.click('a[href="%s"]' % destino)
            posiciones = []
            for _ in range(16):
                pg.wait_for_timeout(70)
                posiciones.append(pg.evaluate('Math.round(window.scrollY)'))
            distintas = len(set(posiciones))
            pg.wait_for_timeout(1200)                       # que termine la animación (1,25 s) antes de medir el destino
            top = pg.evaluate("Math.round(document.querySelector('%s').getBoundingClientRect().top)" % destino)
            check('ancla con scroll progresivo', distintas >= 6 and posiciones[0] < posiciones[-1], '(%d posiciones distintas; destino a %dpx del borde)' % (distintas, top))
            check('ancla llega bajo la barra superior', 60 <= top <= 130, '(top=%d)' % top)
        # rueda: debe tener inercia (sigue moviéndose tras el evento)
        pg.evaluate("window.scrollTo(0,0)")
        pg.wait_for_timeout(300)
        pg.mouse.move(683, 400)
        pg.mouse.wheel(0, 400)
        y1 = pg.evaluate('window.scrollY')
        pg.wait_for_timeout(120)
        y2 = pg.evaluate('window.scrollY')
        pg.wait_for_timeout(900)
        y3 = pg.evaluate('window.scrollY')
        check('rueda con inercia', y1 < y2 < y3, '(%d → %d → %d)' % (y1, y2, y3))
        check('sin errores de consola', not errores, str(errores[:2]) if errores else '')
        fuentes = set(pg.evaluate(FUENTES))
        check('tamaños de fuente dentro de la escala', fuentes <= ESCALA, str(sorted(fuentes)))
        pg.close()
    print('\n== desborde horizontal')
    mal = []
    for ruta in ('/', '/prospection-agent/guia-usuario.html', '/presentations-designer/guia-dev.html', '/presentations-designer/guia-usuario.html', '/functional-scope/guia-dev.html'):
        for w in (360, 390, 768, 1060, 1366, 1920):
            pg = b.new_page(viewport={'width': w, 'height': 900})
            pg.goto(BASE + ruta)
            pg.wait_for_timeout(200)
            if pg.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'):
                mal.append((ruta, w))
            pg.close()
    check('sin desborde horizontal', not mal, str(mal) if mal else '(5 páginas × 6 anchos)')

    # ---------- efectos de texto y carruseles (efectos.js)
    print('\n== efectos de texto (índice)')
    pg = b.new_page(viewport={'width': 1366, 'height': 800})
    errores = []
    pg.on('console', lambda m: errores.append(m.text) if m.type == 'error' else None)
    pg.on('pageerror', lambda e: errores.append(str(e)))
    pg.goto(BASE + '/')
    pg.wait_for_timeout(500)
    mov = "(sel) => { const c = document.querySelector(sel + ' .ls-c'); return c ? getComputedStyle(c).transform : null; }"
    check('letter swap: el texto de la pestaña se conserva', pg.evaluate("document.getElementById('tab-dev').textContent.trim()") == 'Guía de desarrollador')
    check('letter swap: reposo sin movimiento', pg.evaluate(mov, '#tab-dev') in ('none', 'matrix(1, 0, 0, 1, 0, 0)'))
    pg.hover('#tab-dev')
    pg.wait_for_timeout(900)
    check('letter swap: la pestaña anima al pasar el cursor', pg.evaluate(mov, '#tab-dev') not in ('none', 'matrix(1, 0, 0, 1, 0, 0)'), pg.evaluate(mov, '#tab-dev'))
    pg.click('#tab-dev')
    pg.wait_for_timeout(400)
    pg.hover('.panel:not([hidden]) .ag')
    pg.wait_for_timeout(900)
    check('letter swap: la fila entera dispara el cambio de su nombre', pg.evaluate(mov, '.panel:not([hidden]) .ag') not in ('none', 'matrix(1, 0, 0, 1, 0, 0)'))
    check('letter swap: el enlace conserva su nombre accesible', pg.evaluate("document.querySelector('.ag-link').getAttribute('aria-label')") == 'prospection-agent')
    pg.mouse.move(5, 5)
    pg.wait_for_timeout(300)
    check('wave text: el título lleva una letra por span', pg.evaluate("document.querySelectorAll('h1 .wv').length") == len('fullservice-agents'))
    check('wave text: el título conserva su nombre accesible', pg.evaluate("document.querySelector('h1').getAttribute('aria-label')") == 'fullservice-agents')
    pg.wait_for_timeout(1600)
    pg.hover('h1')
    pg.wait_for_timeout(150)
    check('wave text: la ola se dispara al pasar el cursor', pg.evaluate("document.querySelector('h1').classList.contains('wv-on')"))
    pg.mouse.move(5, 5)
    pg.wait_for_timeout(2000)
    check('wave text: la ola termina y queda reposo', not pg.evaluate("document.querySelector('h1').classList.contains('wv-on')"))
    check('pie: ya no está el lema', 'Exploramos' not in pg.evaluate("document.querySelector('footer.site').textContent"))
    enl = pg.evaluate("[...document.querySelectorAll('footer.site .dock-i')].map(a => [a.href, a.target, a.rel])")
    check('dock: GitHub y LinkedIn con su enlace', [e[0] for e in enl] == ['https://github.com/GustavoAdolfoNavarroPacheco', 'https://www.linkedin.com/in/gustavo-adolfo-navarro-pacheco-876b06356/'] and all(e[1] == '_blank' and 'noopener' in e[2] for e in enl), str(enl))
    pg.evaluate("document.querySelector('footer.site').scrollIntoView()")
    pg.wait_for_timeout(500)
    check('dock: en la esquina inferior derecha del pie', pg.evaluate("(() => { const f = document.querySelector('footer.site').getBoundingClientRect(), d = document.querySelector('.dock').getBoundingClientRect(); return d.right > f.right - 80 && d.bottom <= f.bottom + 1; })()"))
    check('dock: la vista previa está oculta en reposo', pg.evaluate("getComputedStyle(document.querySelector('.dock-gh .dock-pv')).opacity") == '0')
    pg.hover('.dock-gh')
    pg.wait_for_timeout(700)
    check('dock: al pasar el cursor el icono crece y aparece la tarjeta de GitHub', pg.evaluate("getComputedStyle(document.querySelector('.dock-gh .dock-pv')).opacity") == '1' and pg.evaluate("getComputedStyle(document.querySelector('.dock-gh')).transform") != 'none')
    check('dock: la tarjeta de GitHub es HTML con 210 celdas y su total', pg.evaluate("document.querySelectorAll('.dock-gh .pv-grid i').length") == 210 and '1.344' in pg.evaluate("document.querySelector('.dock-gh .dock-pv').textContent"))
    pg.hover('.dock-li')
    pg.wait_for_timeout(700)
    check('dock: LinkedIn muestra la suya y la de GitHub se oculta', pg.evaluate("getComputedStyle(document.querySelector('.dock-li .dock-pv')).opacity") == '1' and pg.evaluate("getComputedStyle(document.querySelector('.dock-gh .dock-pv')).opacity") == '0')
    check('dock: sin imágenes de captura (solo avatar)', pg.evaluate("[...document.querySelectorAll('.dock-pv img')].every(i => i.src.indexOf('avatar.webp') > 0)"))
    pg.mouse.move(5, 5)
    check('sin errores de consola (efectos)', not errores, str(errores[:2]) if errores else '')
    pg.close()

    print('\n== carruseles (presentations-designer)')
    pg = b.new_page(viewport={'width': 1366, 'height': 800})
    errores = []
    pg.on('console', lambda m: errores.append(m.text) if m.type == 'error' else None)
    pg.on('pageerror', lambda e: errores.append(str(e)))
    pg.goto(BASE + '/presentations-designer/guia-usuario.html')
    pg.wait_for_timeout(600)
    act = "(sel) => { const cs = [...document.querySelectorAll(sel + ' .cx-card')]; return cs.findIndex(c => c.getAttribute('data-pos') === '0'); }"
    cuenta = "(sel) => document.querySelector(sel + ' .cx-n').textContent"
    check('card stack: 21 portadas y activado', pg.evaluate("document.querySelectorAll('.cs.listo .cx-card').length") == 21)
    sin = pg.evaluate("document.querySelectorAll('.cx img[data-src]').length")
    check('carga bajo demanda: al abrir, las imágenes lejanas no se han pedido', sin == 36, '(%d de 36 pendientes)' % sin)
    pg.evaluate("document.querySelector('.cs').scrollIntoView({block:'center'})")
    pg.wait_for_timeout(1500)
    pend = pg.evaluate("document.querySelectorAll('.cs img[data-src]').length")
    check('carga bajo demanda: con el carrusel a la vista carga la activa y sus vecinas, no las 21', 0 < pend < 21, '(%d pendientes de 21)' % pend)
    check('card stack: las imágenes pedidas cargan', pg.evaluate("[...document.querySelectorAll('.cs img:not([data-src])')].every(i => i.complete && i.naturalWidth > 0)"))
    check('coverflow: 15 logos y activado', pg.evaluate("document.querySelectorAll('.cf.listo .cx-card').length") == 15)
    pg.mouse.move(5, 5)
    pg.wait_for_timeout(500)
    pg.click('.cs .cx-next')
    check('card stack: la flecha avanza', pg.evaluate(act, '.cs') == 1 and pg.evaluate(cuenta, '.cs').startswith('02'), pg.evaluate(cuenta, '.cs'))
    pg.click('.cs .cx-prev')
    pg.click('.cs .cx-prev')
    check('card stack: es circular', pg.evaluate(act, '.cs') == 20 and pg.evaluate(cuenta, '.cs').startswith('21'), pg.evaluate(cuenta, '.cs'))
    pg.focus('.cs .cx-stage')
    pg.keyboard.press('ArrowRight')
    pg.keyboard.press('ArrowRight')
    check('card stack: teclado (flechas)', pg.evaluate(act, '.cs') == 1)
    caja = pg.locator('.cs .cx-stage').bounding_box()
    cx, cy = caja['x'] + caja['width'] / 2, caja['y'] + caja['height'] / 2
    pg.mouse.move(cx, cy)
    pg.mouse.down()
    pg.mouse.move(cx - 60, cy, steps=4)
    pg.mouse.move(cx - 140, cy, steps=4)
    pg.mouse.up()
    check('card stack: arrastrar hacia la izquierda avanza', pg.evaluate(act, '.cs') == 2, pg.evaluate(cuenta, '.cs'))
    pg.mouse.move(cx, cy)
    pg.mouse.down()
    pg.mouse.move(cx + 60, cy, steps=4)
    pg.mouse.move(cx + 140, cy, steps=4)
    pg.mouse.up()
    check('card stack: arrastrar hacia la derecha retrocede', pg.evaluate(act, '.cs') == 1)
    pg.mouse.move(cx, cy)
    pg.wait_for_timeout(300)
    ab = pg.evaluate("getComputedStyle(document.querySelector('.cs .cx-stage')).getPropertyValue('--spread')").strip()
    check('card stack: abanico al pasar el cursor', ab == '1.5', ab)
    i0 = pg.evaluate(act, '.cs')
    pg.wait_for_timeout(4200)
    check('card stack: con el cursor encima no avanza solo', pg.evaluate(act, '.cs') == i0)
    pg.mouse.move(5, 5)
    pg.wait_for_timeout(4600)
    check('card stack: auto-avance sin cursor', pg.evaluate(act, '.cs') != i0)
    pg.evaluate("document.querySelector('.cf').scrollIntoView({block:'center'})")
    pg.wait_for_timeout(300)
    pg.click('.cf .cx-next')
    pg.wait_for_timeout(1200)
    check('coverflow: los logos conservan sus colores (imagen WebP, sin máscara)', pg.evaluate("(() => { const im = [...document.querySelectorAll('.cf-logo img:not([data-src])')]; return im.length > 0 && im.every(i => i.complete && i.naturalWidth > 0 && getComputedStyle(i.parentElement).maskImage === 'none'); })()"))
    check('sin errores de consola (carruseles)', not errores, str(errores[:2]) if errores else '')
    pg.evaluate('window.cargarImagenes()')
    pg.wait_for_timeout(1500)
    check('impresión: se cargan todas las imágenes', pg.evaluate("document.querySelectorAll('.cx img[data-src]').length") == 0)
    pg.emulate_media(media='print')
    check('impresión: las tarjetas pasan a cuadrícula', pg.evaluate("[...document.querySelectorAll('.cx-card')].every(c => getComputedStyle(c).position === 'static')"))
    pg.close()

    print('\n== reducir movimiento')
    ctx = b.new_context(viewport={'width': 1366, 'height': 800}, reduced_motion='reduce')
    pg = ctx.new_page()
    pg.goto(BASE + '/')
    pg.wait_for_timeout(500)
    check('reducir movimiento: sin ola', pg.evaluate("!document.querySelector('h1').classList.contains('wv-in')"))
    pg.goto(BASE + '/presentations-designer/guia-usuario.html')
    pg.evaluate("document.querySelector('.cs').scrollIntoView({block:'center'})")
    pg.mouse.move(5, 5)
    pg.wait_for_timeout(500)
    i0 = pg.evaluate(act, '.cs')
    pg.wait_for_timeout(4500)
    check('reducir movimiento: sin auto-avance', pg.evaluate(act, '.cs') == i0)
    ctx.close()
    b.close()
print('\nRESULTADO:', 'TODO CORRECTO' if ok else 'HAY FALLOS')
sys.exit(0 if ok else 1)
