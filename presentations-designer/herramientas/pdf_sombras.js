// ---- PDF / impresión: sombras difuminadas → sombras vectoriales escalonadas ----
// Chrome exporta box-shadow/text-shadow con desenfoque como máscaras de luminosidad (SMask); varios visores de PDF de celular
// no las soportan y pintan rectángulos grises alrededor de cada tarjeta. Las sombras sin desenfoque son vectores simples.
// Cubre elementos y pseudoelementos (::before/::after), sombras externas e internas (inset). Solo actúa al imprimir/exportar.
(function pdfSafeShadows() {
    const saved = [];
    let styleEl = null;
    function split(s) { const out = []; let d = 0, cur = ''; for (const ch of s) { if (ch === '(') d++; if (ch === ')') d--; if (ch === ',' && d === 0) { out.push(cur.trim()); cur = ''; } else cur += ch; } if (cur.trim()) out.push(cur.trim()); return out; }
    function parse(one) {
        const m = one.match(/(rgba?\([^)]*\))/); if (!m) return null;
        const inset = /inset/.test(one);
        const nums = one.replace(m[1], '').replace('inset', '').trim().split(/\s+/).map(parseFloat);
        const c = m[1].match(/[\d.]+/g).map(Number);
        return { inset, x: nums[0] || 0, y: nums[1] || 0, blur: nums[2] || 0, c, a: c.length > 3 ? c[3] : 1 };
    }
    function convertBox(shadow) {
        const out = [];
        split(shadow).forEach((one) => {
            const s = parse(one);
            if (!s || s.blur <= 0) { out.push(one); return; }
            const n = Math.min(6, Math.max(3, Math.round(s.blur / 6)));
            for (let i = 1; i <= n; i++) {
                const k = i / n;
                if (s.inset) out.push(`inset ${(s.x * k).toFixed(1)}px ${(s.y * k).toFixed(1)}px 0 ${(s.blur / 2 * k).toFixed(1)}px rgba(${s.c[0]},${s.c[1]},${s.c[2]},${(s.a * 0.8 / n).toFixed(4)})`);
                else out.push(`${(s.x * k).toFixed(1)}px ${(s.y * k).toFixed(1)}px 0 ${(s.blur / 7 * k).toFixed(1)}px rgba(${s.c[0]},${s.c[1]},${s.c[2]},${(s.a * 0.9 / n).toFixed(4)})`);
            }
        });
        return out.join(', ');
    }
    function convertText(shadow) {
        const out = [];
        split(shadow).forEach((one) => {
            const s = parse(one);
            if (!s || s.blur <= 0) { out.push(one); return; }
            for (let i = 1; i <= 4; i++) out.push(`${(s.x * i / 4).toFixed(1)}px ${(s.y * i / 4).toFixed(1)}px 0 rgba(${s.c[0]},${s.c[1]},${s.c[2]},${(s.a * 0.2).toFixed(3)})`);
        });
        return out.join(', ');
    }
    function before() {
        if (saved.length || styleEl) return;
        let css = '', id = 0;
        document.body.querySelectorAll('*').forEach((el) => {
            if (el.classList && el.classList.contains('slide')) return;   // el marco de la lámina no lleva sombra en el PDF
            const cs = getComputedStyle(el), bs = cs.boxShadow, ts = cs.textShadow;
            if (bs && bs !== 'none' && /\d+px/.test(bs)) { saved.push([el, 'box-shadow', el.style.boxShadow]); el.style.setProperty('box-shadow', convertBox(bs), 'important'); }
            if (ts && ts !== 'none' && /\d+px/.test(ts)) { saved.push([el, 'text-shadow', el.style.textShadow]); el.style.setProperty('text-shadow', convertText(ts), 'important'); }
            ['::before', '::after'].forEach((ps) => {
                const pc = getComputedStyle(el, ps), pb = pc.boxShadow, pt = pc.textShadow;
                if ((pb && pb !== 'none' && /\d+px/.test(pb)) || (pt && pt !== 'none' && /\d+px/.test(pt))) {
                    const tag = 'pdfsh' + (++id); el.setAttribute('data-pdfsh', (el.getAttribute('data-pdfsh') || '') + ' ' + tag);
                    css += `[data-pdfsh~="${tag}"]${ps}{` + ((pb && pb !== 'none') ? `box-shadow:${convertBox(pb)} !important;` : '') + ((pt && pt !== 'none') ? `text-shadow:${convertText(pt)} !important;` : '') + '}\n';
                    saved.push([el, 'data-pdfsh', null]);
                }
            });
        });
        styleEl = document.createElement('style'); styleEl.textContent = css; document.head.appendChild(styleEl);
    }
    function after() {
        while (saved.length) { const [el, prop, v] = saved.pop(); if (prop === 'data-pdfsh') el.removeAttribute('data-pdfsh'); else if (v) el.style.setProperty(prop, v); else el.style.removeProperty(prop); }
        if (styleEl) { styleEl.remove(); styleEl = null; }
    }
    window.addEventListener('beforeprint', before);
    window.addEventListener('afterprint', after);
    if (window.matchMedia) { const mq = window.matchMedia('print'); const h = (e) => (e.matches ? before() : after()); if (mq.addEventListener) mq.addEventListener('change', h); else if (mq.addListener) mq.addListener(h); }
})();

// Fuerza la carga de todas las @font-face (las de láminas ocultas no se piden solas y el PDF caería a Liberation/Georgia).
(function preloadFontsForPdf() { if (document.fonts) document.fonts.forEach((face) => { face.load().catch(() => {}); }); })();
