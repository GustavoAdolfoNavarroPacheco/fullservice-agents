#!/usr/bin/env python3
"""
verificar_deck.py — Verificación automática de una presentación Campuslands (Sistema v3, Brandbook 2023).

Uso:
    python3 herramientas/verificar_deck.py <carpeta-del-deck> [--pdf salida.pdf] [--png-dir carpeta] [--max-slides 10]

Qué mide (en Chromium headless, lámina por lámina, a tamaño real 1056×594 px):
  1. Número de láminas  ≤ máximo (10 por defecto; solo se supera si el usuario lo pidió TEXTUALMENTE: --max-slides N).
  2. Fondos: TEMA CLARO OBLIGATORIO. Toda lámina (y la página del visor) va sobre BLANCO #FFFFFF (ajuste del usuario).
     Navy/violeta/dorado/verde/celeste/arena solo como tarjetas, franjas y acentos, nunca como fondo de lámina.
  3. Logos: Campuslands y cliente con el MISMO PESO VISUAL (áreas de caja recortada iguales ±6 %: la altura se escala con
     herramientas/igualar_logos.py), Campuslands primero (izq→der), sin deformar, versión a color sobre arena.
     Entre ambos va una «×» (no una línea), centrada en vertical con los logos (±2 px). Prohibido el rótulo «Confidencial».
     Los logos van SOLO en portada y cierre (+ barra del visor): una lámina de contenido con logos arriba a la izquierda es error.
     Láminas: SIN bordes ni líneas divisorias (hairlines); tarjetas y bloques se distinguen por SOMBRAS (acentos de color ≥ 3 px y marco neón permitidos).
     Visor: barra superior e inferior con la MISMA altura (--bar-h); las barras, el recuadro de la lámina y los botones se separan con SOMBRAS, sin líneas ni bordes.
     Sin indicador de página/módulo (puntos, «NN / TT») en ninguna parte de la lámina (solo el numeral grande .ghost); sin resplandor celeste en el fondo; sin borde dorado en banners/franjas.
  4. Tipografía: POPPINS en toda la presentación (400/500/600/900) y Nutmeg; Roboto Mono ya no se usa (regla del usuario).  Tamaño mínimo 9 px.
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
  const PAL = [[94,58,226],[244,180,34],[0,170,128],[0,0,135],[44,170,255],[228,228,219],[255,255,255]];
  const BGREP = {navy:[[0,0,135],[94,58,226]], violet:[[94,58,226],[0,0,135]], sand:[[228,228,219]], white:[[255,255,255]]};
  const NOCONF = /confidencial/i;
  const OKFONT = ['poppins','nutmeg'];   // POPPINS en toda la presentación (regla del usuario); Roboto Mono ya no se usa
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
    // pie de la lámina de cierre: sin la palabra «cierre» (regla del usuario, 2026-10-03)
    if (sl === slides[slides.length-1]) { const cr = sl.querySelector('.crumbs'); if (cr && /cierre/i.test(cr.textContent)) S.err.push('El pie de la lámina de cierre no debe decir «cierre» (usar solo | campuslands | propuesta | cliente |).'); }
    const cs = getComputedStyle(root);
    // 2 · fondo
    const bgTxt = cs.backgroundImage + ' ' + cs.backgroundColor;
    const cols = (bgTxt.match(/rgba?\([^)]*\)/g) || []).map(parse).filter(c => c && c.a > 0);
    const bad = cols.filter(c => !PAL.some(p => near(p,[c.r,c.g,c.b])));
    S.info.bg = root.dataset.bg || '(sin data-bg)';
    if (!cols.length) S.err.push('Fondo: no se pudo leer ningún color de fondo en la lámina.');
    if (bad.length) S.err.push('Fondo fuera de paleta Campuslands: ' + [...new Set(bad.map(c=>`rgb(${c.r},${c.g},${c.b})`))].join(', '));
    if (!root.dataset.bg) S.warn.push('La lámina no declara data-bg="white" (necesario para verificar contraste).');
    const dark = ['navy','violet'].includes(root.dataset.bg);
    if (root.dataset.bg && root.dataset.bg !== 'white') S.err.push(`FONDO BLANCO obligatorio (#FFFFFF): la lámina declara data-bg="${root.dataset.bg}"; todo fondo de lámina debe ser blanco (data-bg="white").`);
    { const bcol = parse(cs.backgroundColor); if (bcol && bcol.a > 0 && !(bcol.r===255 && bcol.g===255 && bcol.b===255)) S.err.push(`El fondo de la lámina es rgb(${bcol.r},${bcol.g},${bcol.b}); debe ser #FFFFFF.`); }
    { const bc = cols.length ? cols[cols.length-1] : null; if (bc && lum(bc) < 0.55) S.err.push('Fondo oscuro: el tema debe ser claro (arena).'); }
    const isEdge = root.classList.contains('cover') || root.classList.contains('close');
    if (/rgba?\(\s*44\s*,\s*170\s*,\s*255/.test(bgTxt)) S.err.push('Fondo con resplandor/difuminación CELESTE: prohibido (ajuste del usuario); usar solo el resplandor violeta suave.');
    { const pi = [...sl.querySelectorAll('.ft *, .s-footer *')].find(e => /^\s*\d{1,2}\s*\/\s*\d{1,2}\s*$/.test(e.textContent) && !e.children.length);
      if (pi) S.err.push('Indicador de página «NN / TT» en el pie: prohibido (ajuste del usuario); el visor ya muestra «N / total».'); }
    { const dots = [...sl.querySelectorAll('[class*="dots"],[class*="pager"],[class*="pagination"],[class*="stepper"]')].filter(e => !decor(e) && [...e.classList].some(c => /dots|pager|pagination|stepper/.test(c) && !/^fx/.test(c)));   // .fx--dots es decoración de marco, no un indicador
      const txt = [...sl.querySelectorAll('*')].find(e => !e.children.length && !decor(e) && !e.closest('.ft,.s-footer') && /^\s*\d{1,2}(\s*[·,]\s*\d{1,2})*\s*\/\s*\d{1,2}\s*$/.test(e.textContent));
      if (dots.length || txt) S.err.push('Indicador de página/módulo (puntos y/o «NN / TT») en la lámina: prohibido (ajuste del usuario); solo se conserva el numeral grande de sección (.ghost).'); }
    sl.querySelectorAll('[class*="reading"],[class*="banner"],[class*="note"],[class*="franja"]').forEach(e => { const b = getComputedStyle(e);
      const col = parse(b.borderTopColor); if (parseFloat(b.borderTopWidth) >= 1.5 && col && col.a > 0.3 && near([244,180,34],[col.r,col.g,col.b],6)) S.err.push('Banner/franja con borde dorado (neón): prohibido; el marco neón es solo para un dato/tarjeta clave (' + e.className + ').'); });
    // SIN BORDES NI LÍNEAS dentro de la lámina: las tarjetas y bloques se distinguen por SOMBRAS (acentos de color ≥ 3 px y marco neón quedan permitidos)
    { const hair = [];
      sl.querySelectorAll('*').forEach(e => { if (decor(e) || e.closest('.neon') || e === root) return;
        const cs2 = getComputedStyle(e);
        for (const k of ['Top','Right','Bottom','Left']) { const w = parseFloat(cs2['border'+k+'Width']), st2 = cs2['border'+k+'Style'], c2 = parse(cs2['border'+k+'Color']);
          if (w > 0 && w < 2.6 && st2 === 'solid' && c2 && c2.a > 0.02) { hair.push((e.className.baseVal ?? e.className).toString().split(' ')[0] || e.tagName.toLowerCase()); break; } }
        const r = e.getBoundingClientRect(); const bg = parse(cs2.backgroundColor);
        if (r.height <= 2.5 && r.width >= 40 && bg && bg.a > 0.02) hair.push('línea ' + ((e.className.baseVal ?? e.className).toString().split(' ')[0] || e.tagName.toLowerCase())); });
      if (hair.length) S.err.push('Bordes/líneas divisorias en la lámina (usar SOMBRAS, no líneas): ' + [...new Set(hair)].slice(0,5).join(', ')); }
    if (NOCONF.test(sl.textContent)) S.err.push('Aparece el rótulo «Confidencial»: está prohibido (regla del usuario).');
    // 3 · logos
    let logos = [...sl.querySelectorAll('img[data-logo]')];
    if (!logos.length) logos = [...sl.querySelectorAll('.cobrand img,.hd img,.s-header img')].filter(i => /logo|brand|client|campuslands/i.test(i.className+' '+i.alt+' '+i.src) && !/favicon/.test(i.src));
    const lg = {};
    logos.forEach(i => { const k = (i.dataset.logo || (/campuslands/i.test(i.alt+i.src) ? 'campuslands' : 'cliente')); (lg[k] = lg[k] || []).push(i); });
    if (logos.length && !isEdge && !sl.classList.contains('sin-logos')) S.err.push('Lámina de contenido con logos (Campuslands × Cliente arriba): los logos van solo en portada y cierre (ajuste del usuario).');
    if (logos.length && isEdge) {
      const c = (lg.campuslands||[])[0], k = (lg.cliente||[])[0];
      if (!c) S.err.push('Logo Campuslands ausente en la lámina.');
      if (!k) S.warn.push('Logo del cliente ausente (¿lámina sin co-branding?).');
      if (c && k) {
        const rc = c.getBoundingClientRect(), rk = k.getBoundingClientRect();
        const ac = rc.width*rc.height, ak = rk.width*rk.height, da = Math.abs(ac-ak)/Math.max(ac,ak);
        S.info.logos = {campuslands_h:+rc.height.toFixed(1), cliente_h:+rk.height.toFixed(1), area_dif_pct:+(da*100).toFixed(1),
                        campuslands_x:+rc.left.toFixed(0), cliente_x:+rk.left.toFixed(0)};
        const capped = rk.height >= rc.height*1.95 && ak < ac;   // logo VERTICAL: su alto se limita a 2× el de Campuslands (el área igual daría un logo desmesurado)
        if (capped && da > 0.06) S.warn.push(`Logo del cliente vertical limitado a 2× la altura de Campuslands: su área es ${(da*100).toFixed(0)} % menor (regla de tope; confirmar a la vista que ninguno domina).`);
        else if (da > 0.06) S.err.push(`Logos con distinto peso visual: área Campuslands ${Math.round(ac)}px² vs cliente ${Math.round(ak)}px² (${(da*100).toFixed(1)} %). Escalar el logo del cliente con igualar_logos.py (--k-cliente).`);
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
    } else if (isEdge) S.err.push('Portada/cierre sin logos: debe llevar «Campuslands × Cliente».');
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
      else if (fam === 'poppins' && ![400,500,600,900].includes(w)) { (badW['Poppins'] = badW['Poppins'] || new Set()).add(w); }
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
    Object.entries(badFam).forEach(([f,o]) => S.err.push(`Fuente no permitida: «${f}» en ${o.n} elemento(s), p. ej. ${o.ex}. Usar Poppins en toda la presentación.`));
    Object.entries(badW).forEach(([f,set]) => S.warn.push(`${f} con peso(s) ${[...set].join('/')}: el Brandbook muestra Regular 400, Medium 500, SemiBold 600 y Black 900.`));
    Object.keys(fontsUsed).forEach(k => { const [fam, w] = [k.slice(0, k.lastIndexOf(' ')), k.slice(k.lastIndexOf(' ')+1)]; if (OKFONT.includes(fam) && !document.fonts.check(`${w} 12px "${fam}"`)) S.err.push(`La fuente «${fam}» peso ${w} NO se cargó (caerá a una fuente de respaldo).`); });
    if (small.length) S.warn.push('Texto < 9 px: ' + [...new Set(small)].slice(0,4).join('; '));
    if (low.length) (low.length > 3 ? S.err : S.warn).push('Contraste insuficiente: ' + [...new Set(low)].slice(0,4).join(' | '));
    // 5 · geometría
    const ft = sl.querySelector('.ft,.s-footer'), ftTop = ft ? ft.getBoundingClientRect().top : sr.bottom;
    const hdEl = sl.querySelector('.hd,.s-header'), hdBottom = hdEl ? hdEl.getBoundingClientRect().bottom : sr.top + 40;
    const out = [], over = [], clip = [], leaves = [], boxOver = [];
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
        // el texto debe quedar DENTRO de la tarjeta/franja que lo contiene (si no, la pisa otro bloque o se sale del fondo)
        { let a = el.parentElement; while (a && a !== root) { const bg = parse(getComputedStyle(a).backgroundColor); if (bg && bg.a > 0.5) break; a = a.parentElement; }
          if (a && a !== root) { const ra = a.getBoundingClientRect(); if (r.bottom > ra.bottom + 2 || r.right > ra.right + 2) boxOver.push((el.textContent.trim().slice(0,28)) + ' (+' + Math.max(r.bottom-ra.bottom, r.right-ra.right).toFixed(0) + 'px)'); } }
        if (ft && r.bottom > ftTop + 1) over.push(el.tagName.toLowerCase()+'.'+el.className+` (+${(r.bottom-ftTop).toFixed(0)}px)`);
      }
      const o = getComputedStyle(el);
      if (el !== root && /(hidden|clip)/.test(o.overflow+o.overflowY) && (el.scrollHeight > el.clientHeight+2 || el.scrollWidth > el.clientWidth+2) && el.clientHeight>0) clip.push(el.tagName.toLowerCase()+'.'+el.className);
    });
    // bloques (tarjetas, franjas) superpuestos entre sí: uno pisa al otro (p. ej. una tarjeta que crece y queda bajo el banner)
    { const bx = [];
      sl.querySelectorAll('*').forEach(el => { if (decor(el) || el === root) return; const r = el.getBoundingClientRect(); const bgc = parse(getComputedStyle(el).backgroundColor);
        if (r.width >= 50 && r.height >= 50 && bgc && bgc.a > 0.5 && !el.closest('.ft,.s-footer')) bx.push({el, r}); });
      const hit = [];
      for (let i = 0; i < bx.length; i++) for (let j = i+1; j < bx.length; j++) { const A = bx[i], B = bx[j];
        if (A.el.contains(B.el) || B.el.contains(A.el)) continue;
        const w = Math.min(A.r.right, B.r.right) - Math.max(A.r.left, B.r.left), h = Math.min(A.r.bottom, B.r.bottom) - Math.max(A.r.top, B.r.top);
        if (w > 4 && h > 4) hit.push(`${A.el.className.toString().split(' ')[0]||A.el.tagName} × ${B.el.className.toString().split(' ')[0]||B.el.tagName} (${Math.round(w)}×${Math.round(h)}px)`); }
      if (hit.length) S.err.push('Bloques superpuestos (uno pisa a otro): ' + [...new Set(hit)].slice(0,4).join(' | ')); }
    // imágenes (logos, fotos) que se salen de su contenedor inmediato: pisan a sus vecinos aunque sigan dentro de la lámina
    const esc = [];
    sl.querySelectorAll('img').forEach(im => { if (decor(im)) return; const r = im.getBoundingClientRect(), pr = im.parentElement.getBoundingClientRect();
      if (r.width > 1 && (r.left < pr.left-2 || r.right > pr.right+2 || r.top < pr.top-2 || r.bottom > pr.bottom+2)) esc.push((im.alt||im.src.split('/').pop())+` (${Math.max(pr.left-r.left, r.right-pr.right, pr.top-r.top, r.bottom-pr.bottom).toFixed(0)}px)`); });
    if (esc.length) S.err.push('Imagen desborda su contenedor: ' + esc.join(', '));
    if (out.length) S.err.push('Contenido fuera de la lámina: ' + [...new Set(out)].slice(0,4).join(', '));
    if (over.length) S.err.push('Contenido invade el pie de página: ' + [...new Set(over)].slice(0,3).join(', '));
    if (boxOver.length) S.err.push('Texto que se sale de su tarjeta/franja (queda pisado o fuera del fondo): ' + [...new Set(boxOver)].slice(0,4).join(' | '));
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
    R.chrome.push({heights:h, big: h[0] >= 40, ok: Math.abs(a[0]-a[1])/Math.max(...a) <= 0.06 || (h[1] >= h[0]*1.95 && a[1] < a[0]), light: !bg || lum(bg) > 0.55, conf: !!document.querySelector('.badge-confidential')}); }
  { const sepx = document.querySelector('.app-header .cobrand .x'); if (!sepx && ch.length >= 2) R.chrome.push({heights:[0,0], ok:false, msg:'Visor: falta la «×» entre los logos de la barra.'}); }
  { const body = getComputedStyle(document.querySelector('.app-content') || document.body).backgroundColor; const c2 = parse(body); R.chromeBg = c2 && c2.a > 0 ? lum(c2) : null; const hb2 = document.querySelector('.app-header'); const hc = hb2 ? parse(getComputedStyle(hb2).backgroundColor) : null; R.chromeWhite = !hc || (hc.r===255 && hc.g===255 && hc.b===255); R.pageWhite = !c2 || (c2.r===255 && c2.g===255 && c2.b===255); }
  // cabecera de portada: «Fecha» debe ser Mes y Año
  { const meta = [...document.querySelectorAll('.meta div')].find(d => /fecha/i.test(d.textContent)); if (meta) { const v = (meta.querySelector('span')||meta).textContent.trim(); R.fecha = v; } }
  // visor: divisiones por SOMBRA, no por líneas ni bordes (barra superior, barra inferior, recuadro de la lámina y botones)
  R.lines = [];
  { const bw = e => e ? ['Top','Right','Bottom','Left'].reduce((m,k) => Math.max(m, parseFloat(getComputedStyle(e)['border'+k+'Width']) * (getComputedStyle(e)['border'+k+'Style'] === 'none' ? 0 : 1)), 0) : 0;
    const sh = e => e && getComputedStyle(e).boxShadow !== 'none';
    const hd = document.querySelector('.app-header'), ft = document.querySelector('.slides-footer-controls'), sl0 = document.querySelector('.slide.active') || document.querySelector('.slide');
    if (hd && ft && Math.abs(hd.getBoundingClientRect().height - ft.getBoundingClientRect().height) > 1) R.lines.push('Barra superior e inferior del visor con ALTURA distinta (' + hd.getBoundingClientRect().height.toFixed(0) + ' px vs ' + ft.getBoundingClientRect().height.toFixed(0) + ' px): deben medir lo mismo (--bar-h).');
    if (hd && (bw(hd) > 0 || !sh(hd))) R.lines.push('Barra superior del visor: debe separarse con SOMBRA y sin línea/borde.');
    if (ft && (bw(ft) > 0 || !sh(ft))) R.lines.push('Barra inferior del visor: debe separarse con SOMBRA y sin línea/borde.');
    if (sl0 && (bw(sl0) > 0 || parseFloat(getComputedStyle(sl0).outlineWidth) > 0 && getComputedStyle(sl0).outlineStyle !== 'none' || !sh(sl0))) R.lines.push('Recuadro de la presentación: debe separarse con SOMBRA y sin borde/contorno.');
    const bt = [...document.querySelectorAll('.control-btn')]; if (bt.some(b => bw(b) > 0 || !sh(b))) R.lines.push('Botones de la barra inferior: deben verse con SOMBRA y sin borde.'); }
  R.title = document.title; const ic = document.querySelector('link[rel~=icon]'); R.favicon = ic ? ic.getAttribute('href') : null;
  R.count = slides.length;
  document.getElementById('__vf').textContent = JSON.stringify(R);
})();
"""

FORCE_CSS = """
<style id="__vfcss">
 .slide{display:block!important;position:relative!important;opacity:1!important;transform:none!important;zoom:1!important;margin:0 0 20px!important;width:1056px!important;height:594px!important}
 html,body{height:auto!important;overflow:visible!important} .slides-container,.app-content,.slides-viewport{display:block!important;height:auto!important;padding:0!important}
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
        if not c.get('big', True): print('✗ ERROR  Visor: el logo de Campuslands de la barra superior debe ser GRANDE (≥ 40 px de alto); mide', round(c['heights'][0],1), 'px.'); errs += 1
        if c.get('conf'): print('✗ ERROR  Visor: el rótulo «Confidencial» está prohibido.'); errs += 1
    for m in R.get('lines', []): print('✗ ERROR  Visor:', m); errs += 1
    if R.get('pageWhite') is False: print('✗ ERROR  Visor: el fondo de la página debe ser BLANCO #FFFFFF.'); errs += 1
    if R.get('chromeWhite') is False: print('✗ ERROR  Visor: la barra superior debe ser BLANCA #FFFFFF.'); errs += 1
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
