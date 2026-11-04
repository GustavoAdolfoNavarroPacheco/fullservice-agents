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
    for ruta in ('/', '/prospection-agent/guia-usuario.html', '/presentations-designer/guia-dev.html', '/functional-scope/guia-dev.html'):
        for w in (360, 390, 768, 1060, 1366, 1920):
            pg = b.new_page(viewport={'width': w, 'height': 900})
            pg.goto(BASE + ruta)
            pg.wait_for_timeout(200)
            if pg.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'):
                mal.append((ruta, w))
            pg.close()
    check('sin desborde horizontal', not mal, str(mal) if mal else '(4 páginas × 6 anchos)')
    b.close()
print('\nRESULTADO:', 'TODO CORRECTO' if ok else 'HAY FALLOS')
sys.exit(0 if ok else 1)
