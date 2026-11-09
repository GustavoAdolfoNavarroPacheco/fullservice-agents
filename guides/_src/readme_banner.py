# -*- coding: utf-8 -*-
"""readme_banner.py — banner del README del repositorio, basado en la portada de la web de guías.

Uso:  python -X utf8 guides/_src/readme_banner.py
Salida: .github/assets/banner.svg (claro) y .github/assets/banner-dark.svg (oscuro).

Reproduce la portada de la web: barra superior con la marca y el botón de GitHub, héroe con el título, la bajada, los aros concéntricos y los dos iconos
(Claude y Perplexity) flotando con su canto, y la barra de pestañas con la primera activa. Es un SVG autocontenido (los iconos van incrustados): GitHub no
carga fuentes ni imágenes externas dentro de un <img>, así que el texto usa pilas de sistema (Georgia para el título, como sustituto de Source Serif 4).
La animación de los iconos es CSS dentro del propio SVG y se detiene sola con «reducir movimiento».
"""
import base64
import io
import pathlib

from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parents[2]
IMG = RAIZ / 'guides' / 'assets' / 'img'
SALIDA = RAIZ / '.github' / 'assets'

W, H = 1280, 440
BARRA, PESTANAS = 64, 64          # alto de la barra superior y de la barra de pestañas

TEMAS = {
    'claro': dict(fondo='#faf9f5', heroe='#f3f1ea', linea='#e6e3d8', tinta='#141413', suave='#5e5d59', chip='#e9e6dc', pill='#f0eee6', acento='#d97757',
                  aro='rgba(20,20,19,.10)', logo='logo-campuslands-color.png', sombra='rgba(20,20,19,.30)'),
    'oscuro': dict(fondo='#1a1918', heroe='#22211f', linea='#3a3835', tinta='#f0eee6', suave='#a8a69d', chip='#2f2d2a', pill='#2b2926', acento='#e08a6a',
                   aro='rgba(240,238,230,.09)', logo=None, sombra='rgba(0,0,0,.55)'),
}
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"


def b64(ruta, alto=None, ancho=None, recorta=False):
    im = Image.open(ruta).convert('RGBA')
    if recorta:                                   # los logos traen margen transparente: se recorta para que midan lo mismo
        im = im.crop(im.getchannel('A').getbbox())
    if alto or ancho:
        k = (alto / im.height) if alto else (ancho / im.width)
        im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode('ascii'), im.size


def icono(idx, x, y, s, archivo, borde, borde2, tono, t):
    """Icono con canto (láminas desplazadas hacia abajo y a la derecha), brillo de marca detrás y sombra; flota con un desfase propio."""
    datos, _ = b64(IMG / archivo, ancho=2 * s)
    r = s * 0.23
    prof = 9
    capas = ''.join('<rect x="{d}" y="{d}" width="{s}" height="{s}" rx="{r}" fill="{c}"/>'.format(
        d=round(prof * (1 - k / prof) , 2), s=s, r=r, c=_mezcla(borde2, borde, k / prof)) for k in range(prof))
    return f'''
  <g class="flota f{idx}">
    <circle cx="{x + s / 2}" cy="{y + s / 2}" r="{s * 0.95}" fill="url(#brillo{idx})"/>
    <ellipse cx="{x + s / 2 + 6}" cy="{y + s + 18}" rx="{s * 0.42}" ry="9" fill="{t['sombra']}" opacity=".55" filter="url(#difumina)"/>
    <g transform="translate({x} {y})">
      {capas}
      <clipPath id="cara{idx}"><rect width="{s}" height="{s}" rx="{r}"/></clipPath>
      <image href="{datos}" width="{s}" height="{s}" clip-path="url(#cara{idx})" preserveAspectRatio="xMidYMid slice"/>
      <rect width="{s}" height="{s}" rx="{r}" fill="none" stroke="#fff" stroke-opacity=".18"/>
    </g>
  </g>'''


def _mezcla(a, b, k):
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(round(ca[i] + (cb[i] - ca[i]) * k) for i in range(3))


def svg(nombre):
    t = TEMAS[nombre]
    logo_arch = t['logo'] or None
    if logo_arch:
        logo, (lw, lh) = b64(IMG / logo_arch, alto=56, recorta=True)
    else:
        logo, (lw, lh) = b64(RAIZ / 'resources' / 'campuslands-resources' / 'Logo Campuslands  Horizontal Blanco.png', alto=56, recorta=True)
    lw2, lh2 = lw / 2, lh / 2
    aros = ''.join(f'<circle cx="1010" cy="226" r="{r}" fill="none" stroke="{t["aro"]}" stroke-width="1"/>' for r in range(35, 330, 35))
    pestanas = [('Inicio', True), ('Instalación', False), ('Guía de usuario', False), ('Guía de desarrollador', False)]
    xs, x = [], 64
    anchos = {'Inicio': 54, 'Instalación': 92, 'Guía de usuario': 126, 'Guía de desarrollador': 180}
    tabs = ''
    for txt, on in pestanas:
        w = anchos[txt]
        tabs += f'<text x="{x}" y="{H - PESTANAS / 2 + 5}" font-family="{SANS}" font-size="15" font-weight="{500 if on else 400}" fill="{t["tinta"] if on else t["suave"]}">{txt}</text>'
        if on:
            tabs += f'<rect x="{x - 18}" y="{H - 4}" width="{w + 36}" height="3" fill="{t["acento"]}"/>'
        x += w + 44
    chips, cx = '', 64
    for txt, w in (('8 agentes de IA', 128), ('Claude Code · Perplexity', 196), ('Guías de usuario y de desarrollador', 270)):
        chips += (f'<rect x="{cx}" y="{BARRA + 232}" width="{w}" height="32" rx="16" fill="{t["chip"]}"/>'
                  f'<text x="{cx + w / 2}" y="{BARRA + 253}" text-anchor="middle" font-family="{SANS}" font-size="14" fill="{t["suave"]}">{txt}</text>')
        cx += w + 12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">fullservice-agents</title>
<desc id="d">Ocho agentes de IA para el flujo comercial de Campuslands, de la prospección al contrato. Guías de usuario y de desarrollador.</desc>
<defs>
  <radialGradient id="brillo1"><stop offset="0" stop-color="#d97757" stop-opacity=".42"/><stop offset="1" stop-color="#d97757" stop-opacity="0"/></radialGradient>
  <radialGradient id="brillo2"><stop offset="0" stop-color="#20b8cd" stop-opacity=".30"/><stop offset="1" stop-color="#20b8cd" stop-opacity="0"/></radialGradient>
  <radialGradient id="velo" cx="1010" cy="226" r="330" gradientUnits="userSpaceOnUse"><stop offset=".25" stop-color="#fff"/><stop offset="1" stop-color="#000"/></radialGradient>
  <mask id="mascara"><rect width="{W}" height="{H}" fill="url(#velo)"/></mask>
  <filter id="difumina" x="-50%" y="-200%" width="200%" height="500%"><feGaussianBlur stdDeviation="9"/></filter>
</defs>
<style>
  .flota{{animation:flota 7s ease-in-out infinite}}
  .f2{{animation-duration:8.6s;animation-delay:-3.4s;animation-direction:reverse}}
  @keyframes flota{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-12px)}}}}
  @media (prefers-reduced-motion:reduce){{.flota{{animation:none}}}}
</style>

<!-- barra superior -->
<rect width="{W}" height="{BARRA}" fill="{t['fondo']}"/>
<rect y="{BARRA - 1}" width="{W}" height="1" fill="{t['linea']}"/>
<image href="{logo}" x="64" y="{(BARRA - lh2) / 2}" width="{lw2}" height="{lh2}"/>
<rect x="{64 + lw2 + 16}" y="{BARRA / 2 - 10}" width="1" height="20" fill="{t['linea']}"/>
<text x="{64 + lw2 + 32}" y="{BARRA / 2 + 5}" font-family="{SERIF}" font-size="16" fill="{t['tinta']}">fullservice-agents</text>
<rect x="{W - 64 - 112}" y="{BARRA / 2 - 19}" width="112" height="38" rx="19" fill="{t['pill']}"/>
<circle cx="{W - 64 - 112 + 26}" cy="{BARRA / 2}" r="8" fill="{t['tinta']}"/>
<text x="{W - 64 - 112 + 44}" y="{BARRA / 2 + 5}" font-family="{SANS}" font-size="15" font-weight="500" fill="{t['tinta']}">GitHub</text>

<!-- héroe -->
<rect y="{BARRA}" width="{W}" height="{H - BARRA - PESTANAS}" fill="{t['heroe']}"/>
<g mask="url(#mascara)">{aros}</g>
<text x="64" y="{BARRA + 112}" font-family="{SERIF}" font-size="60" letter-spacing="-1" fill="{t['tinta']}">fullservice-agents</text>
<text font-family="{SERIF}" font-size="21" fill="{t['suave']}"><tspan x="64" y="{BARRA + 160}">Ocho agentes de IA para el flujo comercial de Campuslands,</tspan><tspan x="64" y="{BARRA + 192}">de la prospección al contrato.</tspan></text>
{chips}
{icono(1, 880, 96, 150, 'plataforma-claude-xl.png', '#b9532f', '#7a3318', 'claude', t)}
{icono(2, 1032, 208, 124, 'plataforma-perplexity-xl.png', '#2a2a28', '#0d0d0c', 'pplx', t)}

<!-- pestañas -->
<rect y="{H - PESTANAS}" width="{W}" height="{PESTANAS}" fill="{t['fondo']}"/>
<rect y="{H - PESTANAS}" width="{W}" height="1" fill="{t['linea']}"/>
{tabs}
</svg>
'''


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    for nombre, arch in (('claro', 'banner.svg'), ('oscuro', 'banner-dark.svg')):
        (SALIDA / arch).write_text(svg(nombre), encoding='utf-8')
        print('  %-18s %5d KB' % (arch, (SALIDA / arch).stat().st_size // 1024))


if __name__ == '__main__':
    main()
