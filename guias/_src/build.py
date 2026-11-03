# -*- coding: utf-8 -*-
"""build.py — genera las guías (HTML) y el portal a partir de agentes/*.py.

Uso:   python guias/_src/build.py [slug ...]     (sin argumentos: las 7 guías x 2 + portal)
Luego: python guias/_src/verificar.py [slug ...] (verificador de presentations-designer + PDF)
"""
import importlib
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

import kit  # noqa: E402

# orden del pipeline comercial
AGENTES = ['prospection-agent', 'intelligence-commercial', 'presentations-designer', 'functional-scope',
           'quote-developer-v2', 'bidding-agent', 'contract-perfectionist']
MAX_SLIDES = {'dev': 12, 'usuario': 10}


def load(slug):
    return importlib.import_module('agentes.' + slug.replace('-', '_'))


def check_glyphs(doc, name):
    """Falla si el texto usa glifos que Poppins no tiene (el PDF caería a Segoe UI)."""
    from fontTools.ttLib import TTFont
    global _CMAP
    if '_CMAP' not in globals():
        _CMAP = set()
        for w in ('Regular', 'Medium', 'SemiBold', 'Black', 'BlackItalic'):
            cm = set(TTFont(str(ROOT / 'assets' / 'fonts' / ('Poppins-%s.ttf' % w))).getBestCmap())
            _CMAP = cm if not _CMAP else (_CMAP & cm)
    import re
    text = re.sub(r'<svg.*?</svg>|<style.*?</style>', '', doc, flags=re.S)
    bad = sorted({ch for ch in text if ord(ch) > 127 and ord(ch) not in _CMAP})
    if bad:
        raise SystemExit('%s: glifos fuera de Poppins: %s' % (name, ' '.join('%s(U+%04X)' % (c, ord(c)) for c in bad)))


def build(only=None):
    css = (SRC / 'base.css').read_text(encoding='utf-8') + (SRC / 'extras.css').read_text(encoding='utf-8')
    (ROOT / 'assets' / 'styles.css').write_text(css, encoding='utf-8')
    done = []
    for slug in AGENTES:
        if only and slug not in only:
            continue
        try:
            mod = load(slug)
        except ModuleNotFoundError as e:
            print('  (pendiente)', slug, '->', e)
            continue
        for kind in ('dev', 'usuario'):
            slides = getattr(mod, kind)()
            doc, n = kit.render_deck(mod.META, kind, slides)
            check_glyphs(doc, '%s/%s' % (slug, kind))
            out = ROOT / slug / kind
            out.mkdir(parents=True, exist_ok=True)
            (out / 'index.html').write_text(doc, encoding='utf-8')
            flag = '' if n <= MAX_SLIDES[kind] else '  ⚠ excede %d' % MAX_SLIDES[kind]
            print('  %-26s %-8s %2d láminas%s' % (slug, kind, n, flag))
        done.append(slug)
    try:
        import portal
        portal.render(ROOT, [load(s).META for s in AGENTES if (ROOT / s / 'dev' / 'index.html').exists()])
        print('  portal: index.html')
    except ModuleNotFoundError:
        pass
    return done


if __name__ == '__main__':
    build(sys.argv[1:] or None)
