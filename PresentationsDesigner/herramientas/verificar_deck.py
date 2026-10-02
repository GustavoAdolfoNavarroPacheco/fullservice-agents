#!/usr/bin/env python3
"""
verificar_deck.py — Verificación automática de una presentación Campuslands (Sistema v3, Brandbook 2023).

Uso:
    python3 herramientas/verificar_deck.py <carpeta-del-deck> [--pdf salida.pdf] [--png-dir carpeta] [--max-slides 10]

Qué mide (en Chromium headless, lámina por lámina, a tamaño real 1056×594 px):
  1. Número de láminas  ≤ máximo (10 por defecto; solo se supera si el usuario lo pidió TEXTUALMENTE: --max-slides N).
  2. Fondos: TEMA CLARO OBLIGATORIO. Toda lámina (y el visor) va sobre ARENA #E4E4DB (fondo claro de la paleta Campuslands,
     Brandbook p.12). Navy/violeta/dorado/verde/celeste solo como tarjetas, franjas y acentos, nunca como fondo de lámina.
  3. Logos: Campuslands y cliente con el MISMO PESO VISUAL (áreas de caja recortada iguales ±6 %: la altura se escala con
     herramientas/igualar_logos.py), Campuslands primero (izq→der), sin deformar, versión a color sobre arena.
     Entre ambos va una «×» (no una línea), centrada en vertical con los logos (±2 px). Prohibido el rótulo «Confidencial».
  4. Tipografía: solo Poppins (400/900), Roboto Mono (400) y Nutmeg (Brandbook p.10).  Tamaño mínimo 9 px.
  5. Geometría: nada fuera de la lámina, nada invadiendo el pie, texto recortado, huecos verticales grandes.
  6. Contraste del texto (WCAG: 4.5:1 normal · 3:1 grande/negrita) contra su fondo real.
  7. <head>: <title> y favicon existentes.
  8. (con --pdf) PDF generado: páginas = láminas y ninguna fuente de respaldo (Liberation/Georgia/Times/Arial).

Sale con código 1 si hay ERRORES. Los AVISOS (⚠) piden revisión visual pero no bloquean.
Esta herramienta NO sustituye la mirada: después de pasar, hay que ver cada lámina (--png-dir) y justificar el reparto.
"""
import argparse, json, os, re, subprocess, sys, tempfile, shutil

CHROME_CANDIDATES = ['/opt/pw-browsers/chromium-1194/chrome-linux/chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
                     '/usr/bin/google-chrome', 'chrome', 'google-chrome', 'chromium']

def find_chrome():
    for c in CHROME_CANDIDATES:
        p = shutil.which(c) or (c if os.path.exists(c) else None)
        if p: return p
    sys.exit('No encuentro Chromium/Chrome. Instálalo o ajusta CHROME_CANDIDATES.')

JS = r"""
(async () => {
  const PAL = [[94,58,226],[244,180,34],[0,170,128],[0,0,135],[44,170,255],[228,228,219]];
  const BGREP = {navy:[[0,0,135],[94,58,226]], violet:[[94,58,226],[0,0,135]], sand:[[228,228,219]]};
  const NOCONF = /confidencial/i;
  const OKFONT = ['poppins','roboto mono','nutmeg'];
  const R = {slides:[], chrome:[], notes:[]};
  await document.fonts.ready; document.fonts.forEach(f=>{ try{f.load()}catch(e){} }); await document.fonts.ready;
  const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if(!m) return null; const p=m[1].split(/[ ,\/]+/).filter(Boolean).map(Number); return {r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1}; };
  const lum = ({r,g,b}) => { const f=c=>{c/=255;return c<=0.03928?c/12.92:Math.pow((c+0.055)/1.055,2.4)}; return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b); };
  const cr = (a,b) => { const x=lum(a),y=lum(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05); };
  const near = (a,b,t=3) => Math.abs(a[0]-b[0])<=t && Math.abs(a[1]-b[1])<=t && Math.abs(a[2]-b[2])<=t;
  const decor = el => !!el.closest('[aria-hidden="true"],.ghost,.chev,.deco');
  const slides = [...document.querySelectorAll('.slide[data-slide]')];
  for (const sl of slides) {
    const n = +sl.dataset.slide, S = {n, err:[], warn:[], info:{}};
    const root = sl.firstElementChild, sr = sl.getBoundingClientRect();
    const cs = getComputedStyle(root);
    // 2 · fondo
    const bgTxt = cs.backgroundImage + ' ' + cs.backgroundColor;
    const cols = (bgTxt.match(/rgba?\([^)]*\)/g) || []).map(parse).filter(c => c && c.a > 0);
    const bad = cols.filter(c => !PAL.some(p => near(p,[c.r,c.g,c.b])));
    S.info.bg = root.dataset.bg || '(sin data-bg)';
    if (!cols.length) S.err.push('Fondo: no se pudo leer ningún color de fondo en la lámina.');
    if (bad.length) S.err.push('Fondo fuera de paleta Campuslands: ' + [...new Set(bad.map(c=>`rgb(${c.r},${c.g},${c.b})`))].join(', '));
    if (!root.dataset.bg) S.warn.push('La lámina no declara data-bg="navy|violet|sand" (necesario para verificar contraste y logo).');
    const dark = ['navy','violet'].includes(root.dataset.bg);
    if (root.dataset.bg && root.dataset.bg !== 'sand') S.err.push(`TEMA CLARO obligatorio: la lámina declara data-bg="${root.dataset.bg}"; todo fondo de lámina debe ser arena (data-bg="sand").`);
    { const bc = cols.length ? cols[cols.length-1] : null; if (bc && lum(bc) < 0.55) S.err.push('Fondo oscuro: el tema debe ser claro (arena).'); }
    if (NOCONF.test(sl.textContent)) S.err.push('Aparece el rótulo «Confidencial»: está prohibido (regla del usuario).');
    // 3 · logos
    let logos = [...sl.querySelectorAll('img[data-logo]')];
    if (!logos.length) logos = [...sl.querySelectorAll('img')].filter(i => /logo|brand|client|campuslands/i.test(i.className+' '+i.alt+' '+i.src) && !/favicon/.test(i.src));
    const lg = {};
    logos.forEach(i => { const k = (i.dataset.logo || (/campuslands/i.test(i.alt+i.src) ? 'campuslands' : 'cliente')); (lg[k] = lg[k] || []).push(i); });
    if (logos.length) {
      const c = (lg.campuslands||[])[0], k = (lg.cliente||[])[0];
      if (!c) S.err.push('Logo Campuslands ausente en la lámina.');
      if (!k) S.warn.push('Logo del cliente ausente (¿lámina sin co-branding?).');
      if (c && k) {
        const rc = c.getBoundingClientRect(), rk = k.getBoundingClientRect();
        const ac = rc.width*rc.height, ak = rk.width*rk.height, da = Math.abs(ac-ak)/Math.max(ac,ak);
        S.info.logos = {campuslands_h:+rc.height.toFixed(1), cliente_h:+rk.height.toFixed(1), area_dif_pct:+(da*100).toFixed(1),
                        campuslands_x:+rc.left.toFixed(0), cliente_x:+rk.left.toFixed(0)};
        if (da > 0.06) S.err.push(`Logos con distinto peso visual: área Campuslands ${Math.round(ac)}px² vs cliente ${Math.round(ak)}px² (${(da*100).toFixed(1)} %). Escalar el logo del cliente con igualar_logos.py (--k-cliente).`);
        if (rc.left > rk.left) S.err.push('El logo de Campuslands debe ir PRIMERO de izquierda a derecha (Brandbook p.6).');
        // separador: «×» centrada en vertical (no una línea)
        const cb = c.closest('.cobrand');
        if (cb) {
          if (cb.querySelector('.sep')) S.err.push('El separador entre logos debe ser una «×» (.x), no una línea (.sep).');
          const x = cb.querySelector('.x');
          if (!x) S.err.push('Falta la «×» entre el logo de Campuslands y el del cliente (Campuslands × Cliente).');
          else {
            const rx = x.getBoundingClientRect(), mid = ((rc.top+rc.bottom)/2 + (rk.top+rk.bottom)/2)/2, cx = (rx.top+rx.bottom)/2;
            S.info.x_off = +(cx-mid).toFixed(1);
            if (Math.abs(cx-mid) > 2) S.err.push(`La «×» no está centrada en vertical respecto a los logos (desvío ${(cx-mid).toFixed(1)}px; máx 2px).`);
            if (!(rc.right <= rx.left+0.5 && rx.right <= rk.left+0.5)) S.err.push('La «×» debe quedar entre los dos logos.');
          }
        }
      }
      logos.forEach(i => {
        const r = i.getBoundingClientRect(); if (!i.naturalWidth) { S.err.push('Logo sin cargar: '+i.src.split('/').pop()); return; }
        const ratio = i.naturalWidth/i.naturalHeight, drawn = r.width/r.height;
        if (Math.abs(ratio-drawn)/ratio > 0.03) S.err.push(`Logo deformado (${i.src.split('/').pop()}): proporción ${ratio.toFixed(2)} → ${drawn.toFixed(2)}.`);
        const f = i.src.toLowerCase(), isWhite = /blanc|white/.test(f), isColor = /color|azul/.test(f);
        if (i.dataset.logo === 'campuslands' && root.dataset.bg) {
          let e = i.parentElement, effDark = dark, plate = false;      // fondo efectivo: placa sólida más cercana, si existe
          while (e && e !== root.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c && c.a > 0.55) { effDark = lum(c) < 0.2; plate = e !== root; break; } e = e.parentElement; }
          const where = plate ? 'sobre su placa' : 'sobre el fondo';
          if (effDark && !isWhite) S.err.push(`Logo Campuslands ${where} OSCURO debe ser la versión BLANCA.`);
          if (!effDark && !isColor) S.err.push(`Logo Campuslands ${where} CLARO debe ser la versión A COLOR.`);
        }
      });
    } else if (!sl.classList.contains('sin-logos')) S.warn.push('La lámina no tiene logos.');
    // 4 · tipografía y 6 · contraste
    const bgChain = el => { let e = el, a = 1;
      while (e && e !== root.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c && c.a > 0.55) return {c, solid:true}; e = e.parentElement; }
      return {solid:false}; };
    const fontsUsed = {}, small = [], low = [], badFam = {}, badW = {};
    sl.querySelectorAll('*').forEach(el => {
      if (decor(el)) return;
      const own = [...el.childNodes].some(t => t.nodeType === 3 && /[\p{L}\p{N}]/u.test(t.textContent));
      if (!own) return;
      const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return;
      const st = getComputedStyle(el), fam = st.fontFamily.split(',')[0].replace(/["']/g,'').trim().toLowerCase();
      const w = +st.fontWeight, px = parseFloat(st.fontSize);
      fontsUsed[fam + ' ' + w] = (fontsUsed[fam + ' ' + w] || 0) + 1;
      if (!OKFONT.includes(fam)) { (badFam[fam] = badFam[fam] || {n:0, ex:`<${el.tagName.toLowerCase()} class="${(el.className.baseVal ?? el.className)}">`}).n++; }
      else if (fam === 'poppins' && ![400,900].includes(w)) { (badW['Poppins'] = badW['Poppins'] || new Set()).add(w); }
      else if (fam === 'roboto mono' && w !== 400) { (badW['Roboto Mono'] = badW['Roboto Mono'] || new Set()).add(w); }
      if (px < 9) small.push(el.tagName.toLowerCase()+'.'+el.className+' '+px.toFixed(1)+'px');
      // contraste
      const col = parse(st.color); if (!col) return;
      let op = 1, e = el; while (e && e !== sl) { op *= parseFloat(getComputedStyle(e).opacity); e = e.parentElement; }
      const b = bgChain(el);
      const bgs = b.solid ? [b.c] : (BGREP[root.dataset.bg] || []).map(([r,g,bl])=>({r,g,b:bl,a:1}));
      if (!bgs.length) return;
      const large = px >= 24 || (px >= 18.66 && w >= 700);
      const need = large ? 3 : 4.5;
      const worst = Math.min(...bgs.map(bg => { const a = col.a*op; const mix = {r:col.r*a+bg.r*(1-a), g:col.g*a+bg.g*(1-a), b:col.b*a+bg.b*(1-a)}; return cr(mix, bg); }));
      if (worst < need) low.push(`${(el.textContent||'').trim().slice(0,28)} → ${worst.toFixed(2)}:1 (mín ${need})`);
    });
    S.info.fonts = fontsUsed;
    Object.entries(badFam).forEach(([f,o]) => S.err.push(`Fuente fuera del Brandbook: «${f}» en ${o.n} elemento(s), p. ej. ${o.ex}.`));
    Object.entries(badW).forEach(([f,set]) => S.warn.push(`${f} con peso(s) ${[...set].join('/')}: el Brandbook muestra ${f==='Poppins'?'Regular 400 y Black 900':'Regular 400'}.`));
    Object.keys(fontsUsed).forEach(k => { const [fam, w] = [k.slice(0, k.lastIndexOf(' ')), k.slice(k.lastIndexOf(' ')+1)]; if (OKFONT.includes(fam) && !document.fonts.check(`${w} 12px "${fam}"`)) S.err.push(`La fuente «${fam}» peso ${w} NO se cargó (caerá a una fuente de respaldo).`); });
    if (small.length) S.warn.push('Texto < 9 px: ' + [...new Set(small)].slice(0,4).join('; '));
    if (low.length) (low.length > 3 ? S.err : S.warn).push('Contraste insuficiente: ' + [...new Set(low)].slice(0,4).join(' | '));
    // 5 · geometría
    const ft = sl.querySelector('.ft,.s-footer'), ftTop = ft ? ft.getBoundingClientRect().top : sr.bottom;
    const hdEl = sl.querySelector('.hd,.s-header'), hdBottom = hdEl ? hdEl.getBoundingClientRect().bottom : sr.top + 70;
    const out = [], over = [], clip = [], leaves = [];
    sl.querySelectorAll('*').forEach(el => {
      if (decor(el)) return;
      const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return;
      const own = [...el.childNodes].some(t => t.nodeType === 3 && t.textContent.trim()) || el.tagName === 'IMG';
      if (r.left < sr.left-1 || r.right > sr.right+1 || r.top < sr.top-1 || r.bottom > sr.bottom+1) out.push(el.tagName.toLowerCase()+'.'+el.className);
      const inFt = el.closest('.ft,.s-footer'), inHd = el.closest('.hd,.s-header');
      const bgc = parse(getComputedStyle(el).backgroundColor), boxed = el !== root && bgc && bgc.a > 0.04 && r.height > 24 && r.width > 40;
      if (boxed && !inFt && !inHd) leaves.push([r.top - sr.top, r.bottom - sr.top]);
      if (own && !inFt && !inHd) {
        leaves.push([r.top - sr.top, r.bottom - sr.top]);
        if (ft && r.bottom > ftTop + 1) over.push(el.tagName.toLowerCase()+'.'+el.className+` (+${(r.bottom-ftTop).toFixed(0)}px)`);
      }
      const o = getComputedStyle(el);
      if (el !== root && /(hidden|clip)/.test(o.overflow+o.overflowY) && (el.scrollHeight > el.clientHeight+2 || el.scrollWidth > el.clientWidth+2) && el.clientHeight>0) clip.push(el.tagName.toLowerCase()+'.'+el.className);
    });
    // imágenes (logos, fotos) que se salen de su contenedor inmediato: pisan a sus vecinos aunque sigan dentro de la lámina
    const esc = [];
    sl.querySelectorAll('img').forEach(im => { if (decor(im)) return; const r = im.getBoundingClientRect(), pr = im.parentElement.getBoundingClientRect();
      if (r.width > 1 && (r.left < pr.left-2 || r.right > pr.right+2 || r.top < pr.top-2 || r.bottom > pr.bottom+2)) esc.push((im.alt||im.src.split('/').pop())+` (${Math.max(pr.left-r.left, r.right-pr.right, pr.top-r.top, r.bottom-pr.bottom).toFixed(0)}px)`); });
    if (esc.length) S.err.push('Imagen desborda su contenedor: ' + esc.join(', '));
    if (out.length) S.err.push('Contenido fuera de la lámina: ' + [...new Set(out)].slice(0,4).join(', '));
    if (over.length) S.err.push('Contenido invade el pie de página: ' + [...new Set(over)].slice(0,3).join(', '));
    if (clip.length) S.err.push('Texto/contenido recortado por overflow: ' + [...new Set(clip)].slice(0,4).join(', '));
    // huecos verticales
    leaves.sort((a,b)=>a[0]-b[0]); const merged = [];
    leaves.forEach(([t,b]) => { const L = merged[merged.length-1]; if (L && t <= L[1]+2) L[1] = Math.max(L[1], b); else merged.push([t,b]); });
    let maxGap = 0, where = '';
    for (let i=1;i<merged.length;i++) { const g = merged[i][0]-merged[i-1][1]; if (g > maxGap) { maxGap = g; where = 'entre bloques'; } }
    const center = root.classList.contains('cover') || root.classList.contains('close') || root.dataset.layout === 'center';
    if (merged.length && !center) {
      const gTop = merged[0][0] - (hdBottom - sr.top), gBot = (ftTop - sr.top) - merged[merged.length-1][1];
      if (gTop > maxGap) { maxGap = gTop; where = 'bajo la cabecera'; }
      if (gBot > maxGap) { maxGap = gBot; where = 'sobre el pie'; }
    }
    S.info.max_gap_px = Math.round(maxGap);
    if (maxGap > (center ? 0.3 : 0.2)*sr.height) S.warn.push(`Hueco vertical de ${Math.round(maxGap)}px (${where}) = ${(maxGap/sr.height*100).toFixed(0)} % de la lámina (máx ${center ? 30 : 20} %): redistribuir (regla de balance de espacio).`);
    R.slides.push(S);
  }
  // chrome del visor (si existe): ambos logos con la misma altura
  const ch = [...document.querySelectorAll('.app-header img[data-logo]')];
  if (ch.length >= 2) { const a = ch.map(i => { const r = i.getBoundingClientRect(); return r.width*r.height; }), h = ch.map(i => i.getBoundingClientRect().height);
    const hb = document.querySelector('.app-header'), bg = hb ? parse(getComputedStyle(hb).backgroundColor) : null;
    R.chrome.push({heights:h, ok: Math.abs(a[0]-a[1])/Math.max(...a) <= 0.06, light: !bg || lum(bg) > 0.55, conf: !!document.querySelector('.badge-confidential')}); }
  { const sepx = document.querySelector('.app-header .cobrand .x'); if (!sepx && ch.length >= 2) R.chrome.push({heights:[0,0], ok:false, msg:'Visor: falta la «×» entre los logos de la barra.'}); }
  { const body = getComputedStyle(document.querySelector('.app-content') || document.body).backgroundColor; const c2 = parse(body); R.chromeBg = c2 && c2.a > 0 ? lum(c2) : null; }
  // cabecera de portada: «Fecha» debe ser Mes y Año
  { const meta = [...document.querySelectorAll('.meta div')].find(d => /fecha/i.test(d.textContent)); if (meta) { const v = (meta.querySelector('span')||meta).textContent.trim(); R.fecha = v; } }
  R.title = document.title; const ic = document.querySelector('link[rel~=icon]'); R.favicon = ic ? ic.getAttribute('href') : null;
  R.count = slides.length;
  document.getElementById('__vf').textContent = JSON.stringify(R);
})();
"""

FORCE_CSS = """
<style id="__vfcss">
 .slide{display:block!important;position:relative!important;opacity:1!important;transform:none!important;zoom:1!important;margin:0 0 20px!important;width:1056px!important;height:594px!important;box-shadow:none!important}
 html,body{height:auto!important;overflow:visible!important} .slides-container,.app-content,.slides-viewport{display:block!important;height:auto!important;padding:0!important}
 .slides-footer-controls{display:none!important}
</style>"""

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('deck'); ap.add_argument('--pdf'); ap.add_argument('--png-dir'); ap.add_argument('--max-slides', type=int, default=10)
    a = ap.parse_args()
    deck = os.path.abspath(a.deck); idx = os.path.join(deck, 'index.html')
    if not os.path.exists(idx): sys.exit(f'No existe {idx}')
    chrome = find_chrome()
    html = open(idx, encoding='utf-8').read()
    probe = html.replace('</head>', FORCE_CSS + '</head>', 1).replace('</body>', '<pre id="__vf" style="display:none"></pre><script>' + JS + '</script></body>', 1)
    tmp = os.path.join(deck, '__verificar.html'); open(tmp, 'w', encoding='utf-8').write(probe)
    try:
        out = subprocess.run([chrome, '--headless', '--no-sandbox', '--disable-gpu', '--allow-file-access-from-files', '--window-size=1200,900',
                              '--virtual-time-budget=15000', '--dump-dom', 'file://' + tmp], capture_output=True, text=True, timeout=120).stdout
    finally:
        os.remove(tmp)
    m = re.search(r'<pre id="__vf"[^>]*>(.*?)</pre>', out, re.S)
    if not m or not m.group(1).strip(): sys.exit('El verificador no devolvió datos (¿falló el script o el HTML?).')
    import html as H
    R = json.loads(H.unescape(m.group(1)))
    errs = warns = 0
    print(f'\n== {os.path.basename(deck)} — {R["count"]} lámina(s) ==')
    if R['count'] > a.max_slides: print(f'✗ ERROR  {R["count"]} láminas > máximo {a.max_slides} (solo se supera si el usuario lo pidió textualmente).'); errs += 1
    else: print(f'✓ Láminas: {R["count"]} (máx {a.max_slides})')
    if not (R.get('title') or '').strip(): print('✗ ERROR  <title> vacío.'); errs += 1
    if not R.get('favicon'): print('✗ ERROR  Falta <link rel="icon"> (isotipo de Campuslands).'); errs += 1
    elif not os.path.exists(os.path.join(deck, R['favicon'])): print('✗ ERROR  El favicon apunta a un archivo inexistente: ' + R['favicon']); errs += 1
    for c in R['chrome']:
        if c.get('msg'): print('✗ ERROR ', c['msg']); errs += 1; continue
        if c['ok']: print('✓ Visor: logos de la barra superior con igual peso visual (alturas', [round(x,1) for x in c['heights']], ')')
        else: print('✗ ERROR  Visor: logos de la barra superior con distinto peso visual (alturas', [round(x,1) for x in c['heights']], ')'); errs += 1
        if not c.get('light', True): print('✗ ERROR  Visor: la barra superior debe ser CLARA (tema claro obligatorio).'); errs += 1
        if c.get('conf'): print('✗ ERROR  Visor: el rótulo «Confidencial» está prohibido.'); errs += 1
    if R.get('chromeBg') is not None and R['chromeBg'] < 0.55: print('✗ ERROR  Visor: el fondo de la página debe ser CLARO (tema claro obligatorio).'); errs += 1
    if R.get('fecha') is not None:
        if re.fullmatch(r'\s*\d{4}\s*', R['fecha']) or not re.search(r'[A-Za-zÁÉÍÓÚáéíóúñ]{3,}.*\d{4}', R['fecha']): print(f'✗ ERROR  Portada: «Fecha» debe mostrar MES Y AÑO (p. ej. «Octubre 2026»); hay «{R["fecha"]}».'); errs += 1
        else: print(f'✓ Portada: fecha «{R["fecha"]}» (mes y año)')
    for S in R['slides']:
        mark = '✗' if S['err'] else ('⚠' if S['warn'] else '✓')
        lg = S['info'].get('logos'); lgt = f" · logos h={lg['campuslands_h']}/{lg['cliente_h']}px (Δárea {lg['area_dif_pct']}%) ×off={S['info'].get('x_off')}px" if lg else ''
        print(f"{mark} Lámina {S['n']:>2}  fondo={S['info']['bg']}{lgt} · hueco máx {S['info'].get('max_gap_px')}px")
        for e in S['err']: print('     ✗', e); errs += 1
        for w in S['warn']: print('     ⚠', w); warns += 1
    if a.pdf or a.png_dir:
        pdf = os.path.abspath(a.pdf or os.path.join(tempfile.gettempdir(), 'verificar_deck.pdf'))
        subprocess.run([chrome, '--headless', '--no-sandbox', '--disable-gpu', '--allow-file-access-from-files', '--no-pdf-header-footer',
                        '--virtual-time-budget=10000', f'--print-to-pdf={pdf}', 'file://' + idx], capture_output=True, text=True, timeout=120)
        try:
            import pymupdf
            d = pymupdf.open(pdf); names = sorted({f[3].split('+')[-1] for p in d for f in p.get_fonts() if f[3]} | {sp['font'].split('+')[-1] for p in d for b in p.get_text('dict')['blocks'] if b['type']==0 for l in b['lines'] for sp in l['spans']})
            print(f'\nPDF: {len(d)} página(s) · fuentes: {", ".join(sorted({("Type3 (fuentes variables, p. ej. Roboto Mono)" if n.startswith("Type3") else n) for n in names}))}')
            names = sorted({('Type3 (fuentes variables, p. ej. Roboto Mono)' if n.startswith('Type3') else n) for n in names})
            if len(d) != R['count']: print(f'✗ ERROR  El PDF tiene {len(d)} páginas y el deck {R["count"]} láminas.'); errs += 1
            badf = [n for n in names if re.search(r'Liberation|Georgia|Times|Arial|DejaVu|Helvetica|Segoe', n)]
            if badf: print('✗ ERROR  Fuentes de respaldo en el PDF (fuente no cargada):', ', '.join(badf)); errs += 1
            if a.png_dir:
                os.makedirs(a.png_dir, exist_ok=True)
                for i, p in enumerate(d, 1): p.get_pixmap(dpi=110).save(os.path.join(a.png_dir, f'lamina_{i:02d}.png'))
                print('PNG por lámina en', a.png_dir, '→ MIRAR cada una y justificar su reparto.')
        except ImportError:
            print('\n(pymupdf no instalado: se omite la verificación del PDF. pip install pymupdf)')
    print(f'\nResultado: {errs} error(es), {warns} aviso(s).', 'APROBADO' if not errs else 'RECHAZADO')
    sys.exit(1 if errs else 0)

if __name__ == '__main__':
    main()
