#!/usr/bin/env python3
"""
arreglar_pdf_sombras.py — hace legible el PDF de un deck en visores de celular.

Chrome exporta los box-shadow/text-shadow con desenfoque como máscaras de luminosidad (SMask) y varios visores
móviles las pintan como rectángulos grises alrededor de cada tarjeta. Esta herramienta:
  1. inserta en index.html (idempotente) el bloque `pdf_sombras.js`, que convierte esas sombras en capas vectoriales
     sin desenfoque SOLO al imprimir/exportar (la pantalla no cambia);
  2. regenera el PDF con Chrome headless (como los PDF originales, Skia/PDF);
  3. comprueba: mismo nº de páginas, mismas fuentes, 0 máscaras de luminosidad y poca diferencia visual con el PDF anterior;
  4. con --aplicar reemplaza el PDF (si las comprobaciones pasan).

Uso:
  python3 arreglar_pdf_sombras.py <carpeta-del-deck> [--aplicar]
  python3 arreglar_pdf_sombras.py <carpeta> --pdf nombre.pdf[?query][@pagina]  (repetible; p. ej. marval-escenario-b.pdf?escenario=b
                                                                              o miami-...-slide1.pdf@1 = solo la página 1)
Requiere pymupdf y Chrome/Chromium (el mismo que verificar_deck.py).
"""
import argparse, glob, os, re, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
MARK = 'pdfSafeShadows'
CHROME = next((c for c in ['/opt/pw-browsers/chromium-1194/chrome-linux/chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome', 'chrome', 'google-chrome', 'chromium'] if shutil.which(c) or os.path.exists(c)), None)

def luminosity_masks(doc):
    n = 0
    for p in doc:
        res = doc.xref_get_key(p.xref, 'Resources')[1] or ''
        n += sum(1 for x in re.findall(r'/G\d+ (\d+) 0 R', res) if 'Luminosity' in doc.xref_object(int(x), compressed=True))
    return n

def fonts(doc):
    return sorted({f[3].split('+')[-1] for p in doc for f in p.get_fonts() if f[3]})

def inject(deck):
    idx = os.path.join(deck, 'index.html'); html = open(idx, encoding='utf-8').read()
    js = ''.join(open(f, encoding='utf-8', errors='ignore').read() for f in glob.glob(os.path.join(deck, '*.js')))
    if MARK in html or MARK in js: return False
    blk = '<script>\n' + open(os.path.join(HERE, 'pdf_sombras.js'), encoding='utf-8').read() + '</script>\n'
    if '</body>' not in html: raise SystemExit('index.html sin </body>')
    open(idx, 'w', encoding='utf-8').write(html.replace('</body>', blk + '</body>', 1)); return True

def render(deck, query, out):
    url = 'file://' + os.path.abspath(os.path.join(deck, 'index.html')) + (('?' + query) if query else '')
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--allow-file-access-from-files', '--no-pdf-header-footer',
                    '--virtual-time-budget=10000', f'--print-to-pdf={out}', url], capture_output=True, text=True, timeout=180)
    if not os.path.exists(out): raise SystemExit('Chrome no generó el PDF')

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('deck'); ap.add_argument('--pdf', action='append'); ap.add_argument('--aplicar', action='store_true'); ap.add_argument('--forzar', action='store_true', help='reemplaza aunque cambien fuentes/aspecto (nunca si quedan máscaras o cambia el nº de páginas)')
    ap.add_argument('--umbral', type=float, default=8.0, help='diferencia media máxima por página (0-255) respecto al PDF anterior')
    a = ap.parse_args()
    import pymupdf
    specs = a.pdf or [os.path.basename(p) for p in sorted(glob.glob(os.path.join(a.deck, '*.pdf')))]
    if not specs: raise SystemExit('el deck no tiene PDF')
    if inject(a.deck): print('index.html: bloque de sombras vectoriales insertado')
    ok_all = True
    for spec in specs:
        m = re.match(r'^([^?@]+)(?:\?([^@]*))?(?:@(\d+))?$', spec); name, query, only = m.group(1), m.group(2) or '', m.group(3)
        old = os.path.join(a.deck, name); tmp = os.path.join(tempfile.gettempdir(), 'nuevo_' + name)
        render(a.deck, query, tmp)
        new = pymupdf.open(tmp)
        if only:
            keep = pymupdf.open(); keep.insert_pdf(new, from_page=int(only) - 1, to_page=int(only) - 1); keep.save(tmp + '.1'); new = pymupdf.open(tmp + '.1'); tmp = tmp + '.1'
        od = pymupdf.open(old) if os.path.exists(old) else None
        probs = []; nota = ''
        mk_new = luminosity_masks(new)
        if mk_new: probs.append(f'{mk_new} máscaras de luminosidad')
        if od:
            if len(od) != len(new): probs.append(f'páginas {len(od)}→{len(new)}')
            fo, fn = set(fonts(od)), set(fonts(new))
            fb = sorted(f for f in fn - fo if re.search(r'Liberation|DejaVu|Arial|Times|Helvetica', f))
            if fb: probs.append(f'fuentes de respaldo nuevas (fuente no cargada): {fb}')
            elif fo != fn: nota = f' · fuentes: -{sorted(fo - fn)} +{sorted(fn - fo)}'
            diffs = []
            for i in range(min(len(od), len(new))):
                A = od[i].get_pixmap(dpi=36).samples; B = new[i].get_pixmap(dpi=36).samples
                if len(A) == len(B): diffs.append(sum(abs(x - y) for x, y in zip(A, B)) / len(A))
            mx = max(diffs) if diffs else 0
            if mx > a.umbral: probs.append(f'diferencia visual alta (máx {mx:.1f}/255; el PDF anterior pudo quedar desactualizado)')
            print(f'{name}: {len(od)}→{len(new)} págs · máscaras {luminosity_masks(od)}→{mk_new} · dif. visual máx {mx:.1f}/255{nota} · ' + ('OK' if not probs else 'REVISAR: ' + '; '.join(probs)))
        else:
            print(f'{name}: nuevo · máscaras {mk_new} · ' + ('OK' if not probs else 'REVISAR: ' + '; '.join(probs)))
        grave = [q for q in probs if 'máscaras' in q or 'páginas' in q]
        if a.aplicar and (not probs or (a.forzar and not grave)): shutil.copyfile(tmp, old); print('   → PDF reemplazado' + (' (forzado)' if probs else ''))
        elif a.aplicar: ok_all = False; print('   → NO se reemplazó (revisar)')
    sys.exit(0 if ok_all else 1)

if __name__ == '__main__': main()
