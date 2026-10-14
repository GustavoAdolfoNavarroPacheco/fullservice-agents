#!/usr/bin/env python3
"""
igualar_logos.py — Iguala el PESO VISUAL de los logos Campuslands × Cliente (regla del usuario, 2026-10-02).

Dos logos a la misma ALTURA no se ven del mismo tamaño si sus proporciones difieren (Campuslands horizontal a color vigente es 4,31 : 1;
Globant es 5,09 : 1 → a igual altura Globant se ve ~18 % más ancho que el logo vigente de Campuslands). La regla es: ÁREAS DE CAJA RECORTADA IGUALES.
    área = ancho × alto = ratio × alto²   →   alto_cliente = alto_campuslands × √(ratio_campuslands / ratio_cliente)

Uso:
    python3 herramientas/igualar_logos.py <logo-cliente.png> [--campuslands recursos/logos-campuslands/campuslands-horizontal-color-recortado.png]

Imprime el factor k para la variable CSS --k-cliente (el logo del cliente se dibuja con alto = alto_Campuslands × k) y las medidas
resultantes en cabecera (30 px), portada/cierre (64 px) y visor (26 px). El logo del cliente debe estar RECORTADO al contenido (alfa).
"""
import argparse, math, os, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CAMPUS = os.path.join(HERE, '..', 'recursos', 'logos-campuslands', 'campuslands-horizontal-color-recortado.png')

def ratio(path):
    im = Image.open(path).convert('RGBA'); bb = im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
    w, h = (bb[2]-bb[0], bb[3]-bb[1]) if bb else im.size
    return im.size[0] / im.size[1], w / h

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cliente'); ap.add_argument('--campuslands', default=DEFAULT_CAMPUS)
    a = ap.parse_args()
    if not os.path.exists(a.campuslands):
        sys.exit('No encuentro el logo de Campuslands: ' + a.campuslands)
    rc_file, rc_ink = ratio(a.campuslands); rk_file, rk_ink = ratio(a.cliente)
    if abs(rk_file - rk_ink) / rk_ink > 0.03:
        print(f'⚠ El logo del cliente NO está recortado a su contenido (archivo {rk_file:.2f}:1, tinta {rk_ink:.2f}:1): recórtalo antes de medir.')
    k = math.sqrt(rc_file / rk_file)
    print(f'Campuslands {rc_file:.3f}:1 · cliente {rk_file:.3f}:1  →  k = √({rc_file:.3f}/{rk_file:.3f}) = {k:.4f}')
    print(f'CSS:  :root{{ --k-cliente:{k:.4f}; }}')
    for nombre, h in (('cabecera', 30), ('portada/cierre', 64), ('visor', 26)):
        hk = h * k
        print(f'  {nombre:15} Campuslands {h}px × {h*rc_file:.0f}px = {h*h*rc_file:.0f}px² · cliente {hk:.1f}px × {hk*rk_file:.0f}px = {hk*hk*rk_file:.0f}px²')

if __name__ == '__main__':
    main()
