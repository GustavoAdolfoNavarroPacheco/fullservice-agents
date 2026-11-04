#!/usr/bin/env python3
"""
elegir_logo.py — Elige la versión del logo de Campuslands según el contraste con el fondo (Brandbook 2023).

Uso:
    python3 herramientas/elegir_logo.py navy            # nombre de la paleta: violeta|dorado|verde|navy|celeste|arena
    python3 herramientas/elegir_logo.py "#5E3AE2"        # o un HEX cualquiera
    python3 herramientas/elegir_logo.py --tabla          # contraste de las dos versiones contra los 6 colores de la marca

Reglas que aplica (las medidas salen de recursos/logos-campuslands/*):
  · Versión A COLOR : texto del wordmark #373435 + casco con degradado #142F5D → #408AF3.
  · Versión BLANCA  : #FFFFFF.
  · El texto del logo debe superar 4.5:1 y AMBOS extremos del degradado del casco 2.5:1 contra el fondo. Si ninguna versión
    cumple, el fondo NO sirve para la zona del logo (el logo no se recolorea: Brandbook p.16 "usos incorrectos").
Los logos jamás se recolorean, rotan, recortan ni redistribuyen.
"""
import sys

PALETA = {'violeta': '#5E3AE2', 'dorado': '#F4B422', 'verde': '#00AA80', 'navy': '#000087', 'celeste': '#2CAAFF', 'arena': '#E4E4DB'}
COLOR_TEXTO, COLOR_CASCO_CLARO, COLOR_CASCO_OSCURO = '#373435', '#408AF3', '#142F5D'

def lum(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def cr(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True); return (x + 0.05) / (y + 0.05)

def evaluar(bg):
    color_txt = cr(COLOR_TEXTO, bg)
    # el casco a color es un degradado: AMBOS extremos deben verse (si el extremo claro desaparece, el logo queda "con elementos eliminados")
    color_casco = min(cr(COLOR_CASCO_CLARO, bg), cr(COLOR_CASCO_OSCURO, bg))
    blanco = cr('#FFFFFF', bg)
    ok_color = color_txt >= 4.5 and color_casco >= 2.5
    ok_blanco = blanco >= 4.5
    if ok_blanco and (not ok_color or blanco >= color_txt): rec = 'BLANCO'
    elif ok_color: rec = 'COLOR'
    else: rec = None
    return dict(color_texto=color_txt, color_casco=color_casco, blanco=blanco, ok_color=ok_color, ok_blanco=ok_blanco, recomendado=rec)

def main():
    a = sys.argv[1:]
    if not a or a[0] in ('-h', '--help'): print(__doc__); return
    if a[0] == '--tabla':
        print(f"{'fondo':9}{'hex':9}{'COLOR texto':>12}{'COLOR casco':>13}{'BLANCO':>9}   recomendado")
        for n, h in PALETA.items():
            e = evaluar(h); print(f"{n:9}{h:9}{e['color_texto']:>12.2f}{e['color_casco']:>13.2f}{e['blanco']:>9.2f}   {e['recomendado'] or '— ninguno: no usar este fondo en la zona del logo'}")
        return
    bg = PALETA.get(a[0].lower(), a[0])
    if not bg.startswith('#'): sys.exit('Fondo desconocido. Usa: ' + ', '.join(PALETA) + ' o un HEX.')
    e = evaluar(bg)
    print(f"Fondo {a[0]} ({bg})")
    print(f"  logo A COLOR : texto {e['color_texto']:.2f}:1 · casco {e['color_casco']:.2f}:1  → {'cumple' if e['ok_color'] else 'NO cumple'}")
    print(f"  logo BLANCO  : {e['blanco']:.2f}:1                     → {'cumple' if e['ok_blanco'] else 'NO cumple'}")
    print('  RECOMENDADO  :', e['recomendado'] or 'NINGUNO — cambia el fondo de la zona del logo (navy, violeta o arena)')
    sys.exit(0 if e['recomendado'] else 1)

if __name__ == '__main__':
    main()
