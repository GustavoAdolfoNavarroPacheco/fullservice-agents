"""Genera los recursos gráficos de los componentes de las guías (se ejecuta a mano cuando cambian las fuentes):

  python recursos_web.py

- assets/img/portadas/<slug>.webp : primera página del PDF de cada presentación (apila las portadas del «card stack»)
- assets/img/logos/<empresa>.webp : logo de cada empresa de resources/companies-logos/, a color, recortado y ligero (máx. 280 × 210 px)

Requiere PyMuPDF (fitz), Pillow y numpy.
"""
import glob
import pathlib

import fitz
import numpy as np
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parents[2]
DECKS = RAIZ / 'agents/claude-agents/presentations-designer/presentaciones/decks'
LOGOS = RAIZ / 'resources/companies-logos'
SALIDA = RAIZ / 'guides/assets/img'

# slug de la portada -> PDF del deck (se elige la versión vigente de cada cliente)
PORTADAS = {
    'fullservice-campuslands-v3': 'fullservice-campuslands-v3/fullservice-campuslands-v3.pdf',
    'ai-academy': 'ai-academy/ai-academy.pdf',
    'avicampo': 'avicampo/avicampo.pdf',
    'chico': 'chico/chico.pdf',
    'colbeef-flujo-ia': 'colbeef-flujo-ia/colbeef-flujo-ia.pdf',
    'compumax-asistente-ia': 'compumax-asistente-ia/compumax-asistente-ia.pdf',
    'comultrasan-orbit': 'comultrasan-orbit/comultrasan-orbit.pdf',
    'fcv': 'fcv/fcv.pdf',
    'gaspais-chilco': 'gaspais-chilco/gaspais-chilco.pdf',
    'giron-cc-v2': 'giron-cc-v2/giron-cc-v2.pdf',
    'globant-dojo-v3': 'globant-dojo-v3/globant-dojo-v3.pdf',
    'greenmetal-fyswap': 'greenmetal-fyswap/greenmetal-fyswap.pdf',
    'hubux-v2': 'hubux-v2/hubux-v2.pdf',
    'land-cargo-v2': 'land-cargo-v2/land-cargo-v2.pdf',
    'marval': 'marval/marval-escenario-a.pdf',
    'mchaileh-crm-ia': 'mchaileh-crm-ia/mchaileh-crm-ia.pdf',
    'miami-aqua-tours-ampliado': 'miami-aqua-tours-ampliado/miami-aqua-tours-ampliado.pdf',
    'multinal-escenario-b': 'multinal-escenario-b/multinal-escenario-b.pdf',
    'palmera-jr': 'palmera-jr/palmera-jr.pdf',
    'unidrogas': 'unidrogas/unidrogas.pdf',
    've-a-la-segura': 've-a-la-segura/ve-a-la-segura.pdf',
}


def portadas():
    (SALIDA / 'portadas').mkdir(parents=True, exist_ok=True)
    for slug, pdf in PORTADAS.items():
        pag = fitz.open(DECKS / pdf)[0]
        k = 800 / pag.rect.width
        pix = pag.get_pixmap(matrix=fitz.Matrix(k, k))
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        img.save(SALIDA / 'portadas' / ('%s.webp' % slug), 'WEBP', quality=80, method=6)
        print('portada', slug)


def logos():
    """Logo a color en WebP (con transparencia), recortado a su contenido y de máx. 280 × 210 px: pesa ~5-15 KB y se ve nítido a 2x."""
    import glob as g
    for f in g.glob(str(SALIDA / 'logos' / '*.png')):                 # restos de la versión monocroma
        pathlib.Path(f).unlink()
    (SALIDA / 'logos').mkdir(parents=True, exist_ok=True)
    for carpeta in sorted(glob.glob(str(LOGOS / '*/'))):
        slug = pathlib.Path(carpeta).name
        archivo = [f for f in glob.glob(carpeta + '/*') if f.lower().endswith(('.png', '.jpg', '.webp'))][0]
        im = Image.open(archivo).convert('RGBA')
        a = np.array(im).astype(float)
        al = a[..., 3:] / 255
        sobre_blanco = a[..., :3] * al + 255 * (1 - al)
        tinta = (255 - sobre_blanco).max(axis=2) / 255              # lo que no es fondo blanco ni transparente
        ys, xs = np.where(tinta > 0.08)
        im = im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
        im.thumbnail((280, 210), Image.LANCZOS)
        im.save(SALIDA / 'logos' / ('%s.webp' % slug), 'WEBP', quality=82, alpha_quality=70, method=6)
        print('logo', slug, im.size)


if __name__ == '__main__':
    portadas()
    logos()
