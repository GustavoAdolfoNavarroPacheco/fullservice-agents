# -*- coding: utf-8 -*-
"""verificar.py — corre verificar_deck.py (presentations-designer) sobre cada guía, exporta su PDF y deja PNG por lámina.

Uso:  python guias/_src/verificar.py [--sin-png] [slug[/dev|/usuario] ...]
Salida: PDF en guias/<slug>/<tipo>/guia-<tipo>.pdf · PNG en <scratch>/png/<slug>-<tipo>/ · resumen por guía.
"""
import pathlib
import subprocess
import sys

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding='utf-8')
    except Exception:
        pass
from build import AGENTES, MAX_SLIDES  # noqa: E402

VERIF = ROOT.parent / 'presentations-designer' / 'herramientas' / 'verificar_deck.py'
SCRATCH = pathlib.Path(r'C:\Users\FULLSE~1\AppData\Local\Temp\claude\C--Users-Full-Service-dev-fullservice-agents\be3ecd83-9adb-435c-827f-9ef0c56a57a5\scratchpad')


def sheets(slug, kind):
    """Hojas de contacto (6 láminas c/u) para la revisión a la vista."""
    from PIL import Image
    pd = SCRATCH / 'png' / ('%s-%s' % (slug, kind))
    fs = sorted(pd.glob('lamina_*.png'))
    ims = [Image.open(f).convert('RGB') for f in fs]
    if not ims:
        return []
    w, h = ims[0].size
    tw, th = int(w * .62), int(h * .62)
    out = []
    for part, a in enumerate(range(0, len(ims), 6)):
        sub = ims[a:a + 6]
        r = (len(sub) + 1) // 2
        sheet = Image.new('RGB', (tw * 2 + 30, th * r + 10 * (r + 1)), '#cccccc')
        for i, im in enumerate(sub):
            sheet.paste(im.resize((tw, th)), (10 + (i % 2) * (tw + 10), 10 + (i // 2) * (th + 10)))
        f = SCRATCH / 'png' / ('hoja_%s_%s_%d.png' % (slug, kind, part))
        sheet.save(f)
        out.append(f)
    return out


def run(slug, kind, png=True):
    deck = ROOT / slug / kind
    pdf = deck / ('guia-%s.pdf' % kind)
    cmd = [sys.executable, '-X', 'utf8', str(VERIF), str(deck), '--pdf', str(pdf), '--max-slides', str(MAX_SLIDES[kind])]
    if png:
        pd = SCRATCH / 'png' / ('%s-%s' % (slug, kind))
        pd.mkdir(parents=True, exist_ok=True)
        cmd += ['--png-dir', str(pd)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout + r.stderr


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    png = '--sin-png' not in sys.argv
    targets = []
    for slug in (AGENTES if not args else []):
        targets += [(slug, 'dev'), (slug, 'usuario')]
    for a in args:
        s, _, k = a.partition('/')
        targets += [(s, k)] if k else [(s, 'dev'), (s, 'usuario')]
    bad = 0
    for slug, kind in targets:
        code, out = run(slug, kind, png)
        print('=' * 78)
        print('%s / %s  -> %s' % (slug, kind, 'APROBADO' if code == 0 else 'CON ERRORES (código %d)' % code))
        print(out.strip())
        bad += code != 0
        if png:
            for f in sheets(slug, kind):
                print('HOJA:', f)
    print('\nGuías con errores:', bad)
    sys.exit(1 if bad else 0)
