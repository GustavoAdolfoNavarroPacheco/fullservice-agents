#!/usr/bin/env python3
"""Colores de marca de un cliente, tomados de SU logo, para las franjas de la tarjeta del portal.

Uso:
    python3 herramientas/colores_marca.py presentaciones/decks/assets/logos/<Cliente>.png [--max 3]

Imprime 1–3 colores hex (de mayor a menor presencia) listos para pegar en el campo `colors` de
`presentaciones/web/src/data/decks.ts`:   "colors": ["#01ADEE", "#ABCF40"],

Criterio: se ignoran transparentes, blancos y grises; se agrupan los píxeles por tono y se toma el promedio real de cada grupo;
solo cuentan colores con ≥ 3 % del logo y tonos claramente distintos entre sí. Revisa el resultado a la vista: si el logo
tiene un degradado o el color de marca es negro/gris, ajústalo a mano (regla del portal en CLAUDE.md).
"""
import colorsys
import sys

from PIL import Image


def colores(path: str, k: int = 3) -> list[str]:
    im = Image.open(path).convert("RGBA")
    im.thumbnail((220, 220))
    px = [p for p in im.get_flattened_data() if p[3] > 200] if hasattr(im, "get_flattened_data") else [p for p in im.getdata() if p[3] > 200]
    bins: dict[tuple[int, int, int], list[float]] = {}
    for r, g, b, _ in px:
        e = bins.setdefault((r // 24, g // 24, b // 24), [0, 0, 0, 0])
        e[0] += 1
        e[1] += r
        e[2] += g
        e[3] += b
    total = len(px) or 1
    cands = []
    for n, sr, sg, sb in sorted(bins.values(), key=lambda e: -e[0]):
        r, g, b = sr / n, sg / n, sb / n
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        if s > 0.28 and v > 0.18 and n / total >= 0.03:
            cands.append(((round(r), round(g), round(b)), h))
    picks: list[tuple[tuple[int, int, int], float]] = []
    for rgb, h in cands:
        if all(min(abs(h - ph), 1 - abs(h - ph)) > 0.06 for _, ph in picks):
            picks.append((rgb, h))
        if len(picks) == k:
            break
    return ["#%02X%02X%02X" % rgb for rgb, _ in picks]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    maximo = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 3
    print(", ".join(f'"{c}"' for c in colores(sys.argv[1], maximo)) or "(sin colores cromáticos: elige a mano)")
