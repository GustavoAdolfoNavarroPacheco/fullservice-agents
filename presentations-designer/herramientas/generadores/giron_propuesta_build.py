#!/usr/bin/env python3
# Generador del deck «Propuesta Alcaldía de Girón». El texto sale LITERAL del docx (paras.json); aquí solo se le da forma.
import json, re, html, sys, os

TMP = os.path.dirname(os.path.abspath(__file__))
DECK = r'C:\Users\Full Service\dev\fullservice-agents\presentations-designer\presentaciones\decks\giron-propuesta'
P = json.load(open(os.path.join(TMP, 'paras.json'), encoding='utf8'))
FIT = {}
if os.path.exists(os.path.join(TMP, 'fit.json')):
    FIT = json.load(open(os.path.join(TMP, 'fit.json')))

def L(n): return P[n - 1].replace('\xa0', ' ').strip()
def esc(s): return html.escape(s, quote=False)
def fm(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s, flags=re.S)
    return s.replace('\n', '<br>')
def nb(s): return s.replace('**', '')
def bl(n):
    s = L(n)
    for pre in ('• ', '☐ '):
        if s.startswith(pre): return s[len(pre):].strip()
    return s

# ---------- íconos (trazo uniforme, 24×24) ----------
IC = {
 'doc': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 'shield': '<path d="M12 2 4 5v6c0 5.2 3.4 9.5 8 11 4.6-1.5 8-5.8 8-11V5z"/><path d="m9 12 2 2 4-4"/>',
 'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 'chart': '<path d="M3 3v18h18"/><path d="M8 17v-6M13 17V7M18 17v-3"/>',
 'cloud': '<path d="M7 18a5 5 0 1 1 1.2-9.8A6 6 0 0 1 19.5 11 3.5 3.5 0 0 1 19 18z"/>',
 'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 'chip': '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
 'zap': '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 'search': '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 'layers': '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
 'folder': '<path d="M3 7a2 2 0 0 1 2-2h4l2 3h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
 'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'chat': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 'map': '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 'check': '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
 'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 'sliders': '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
 'server': '<rect x="2" y="3" width="20" height="8" rx="2"/><rect x="2" y="13" width="20" height="8" rx="2"/><path d="M6 7h.01M6 17h.01"/>',
 'lock': '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
 'coin': '<circle cx="12" cy="12" r="10"/><path d="M15 9.5a3 3 0 0 0-3-1.5c-1.7 0-3 .9-3 2.2 0 3 6 1.6 6 4.6 0 1.3-1.3 2.2-3 2.2a3 3 0 0 1-3-1.5M12 6v2M12 16v2"/>',
 'wrench': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94z"/>',
 'book': '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
 'flag': '<path d="M4 22V4M4 4h13l-2 4 2 4H4"/>',
 'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>',
 'link': '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
 'bot': '<rect x="3" y="8" width="18" height="12" rx="3"/><path d="M12 8V4M8 4h8M9 14h.01M15 14h.01"/>',
 'pen': '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4z"/>',
 'db': '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5M3 12c0 1.7 4 3 9 3s9-1.3 9-3"/>',
 'cart': '<circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>',
 'globe': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/>',
 'ban': '<circle cx="12" cy="12" r="10"/><path d="m4.9 4.9 14.2 14.2"/>',
 'plug': '<path d="M12 22v-5M9 8V2M15 8V2M18 8v5a6 6 0 0 1-12 0V8z"/>',
 'clip': '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2M9 14l2 2 4-4"/>',
 'trend': '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
 'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'handshake': '<path d="m11 17 2 2a1 1 0 0 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 0 0 3-3l-3.9-3.9a3 3 0 0 0-4.2 0l-.9.9a1 1 0 0 1-1.4 0l-.4-.4"/><path d="m21 3 1 11h-2M3 3 2 14l6.5 6.5a1 1 0 0 0 3-3M3 4h8"/>',
}
TONES = ['violet', 'sky', 'gold', 'green', 'navy']
def ic(name, tone='violet', extra=''):
    return f'<span class="ic ic--{tone} {extra}"><svg viewBox="0 0 24 24" aria-hidden="true">{IC[name]}</svg></span>'

# ---------- bloques ----------
def lines_html(nums):
    """Convierte números de línea en párrafos / listas (literal)."""
    out, ul = [], []
    def flush():
        nonlocal ul
        if ul:
            out.append('<ul class="list">' + ''.join(f'<li>{fm(x)}</li>' for x in ul) + '</ul>'); ul = []
    for n in nums:
        raw = L(n)
        if raw.startswith('• '): ul.append(raw[2:].strip())
        else:
            flush(); out.append(f'<p>{fm(raw)}</p>')
    flush()
    return ''.join(out)

def wlen(nums): return sum(len(L(n)) for n in nums)

def blk(h, nums, icn=None, kind='', fx='fx--arcs', tone='violet', lbl=None, raw=None, w=None, fl=None):
    body = raw if raw is not None else lines_html(nums)
    wt = w if w is not None else max(wlen(nums) if nums else 200, 140)
    tone_cls = tone
    FL = (lambda wt: fl if fl else f'{wt} 1 0')
    if kind in ('card--navy',): tone_cls = 'gold'
    if kind in ('card--violet',): tone_cls = 'gold'
    if h:
        head = f'<div class="bh">{ic(icn, tone_cls) if icn else ""}<h3>{fm(h)}</h3></div>'
        inner = (f'<span class="lbl">{esc(lbl)}</span>' if lbl else '') + head + body
        return wt, f'<div class="card blk {kind} fx {fx}" style="flex:{FL(wt)}">{inner}</div>'
    if icn:
        return wt, f'<div class="card blk row {kind} fx {fx}" style="flex:{FL(wt)}">{ic(icn, tone_cls)}<div class="tx">{body}</div></div>'
    return wt, f'<div class="card blk {kind} fx {fx}" style="flex:{FL(wt)}">{body}</div>'

def vcol(*blocks, fl=None):
    wt = sum(b[0] for b in blocks)
    return wt, f'<div class="vcol" style="flex:{fl or str(wt)+" 1 0"}">' + ''.join(b[1] for b in blocks) + '</div>'

def vstack(*blocks):
    return ''.join(b[1] for b in blocks)

def area(inner, cls=''):
    return f'<div class="area {cls}">{inner}</div>'

def hrow(*cols):
    tot = sum(c[0] for c in cols)
    # los anchos se reparten según el texto, con piso para que ninguna columna quede minúscula
    parts = []
    for c in cols:
        share = max(c[0] / tot, 0.3)
        parts.append(c[1].replace(f'flex:{c[0]} 1 0', f'flex:{share:.3f} 1 0', 1))
    return '<div class="hrow">' + ''.join(parts) + '</div>'

def vrows(*blocks):
    return '<div class="vcol" style="flex:1">' + ''.join(b[1] for b in blocks) + '</div>'

def table(h0, r0, r1, ncols, widths=None, center_last=False, style=''):
    head = [L(h0 + i) for i in range(ncols)]
    rows = [[L(r0 + k * ncols + i) for i in range(ncols)] for k in range((r1 - r0 + 1) // ncols)]
    cg = ''
    if widths: cg = '<colgroup>' + ''.join(f'<col style="width:{w}%">' for w in widths) + '</colgroup>'
    th = ''.join(f'<th>{fm(nb(c))}</th>' for c in head)
    body = ''
    for r in rows:
        tds = ''.join(f'<td{" class=c" if (center_last and i == ncols - 1) else ""}>{fm(c)}</td>' for i, c in enumerate(r))
        body += f'<tr>{tds}</tr>'
    return f'<div class="tblw" style="{style}"><table class="tbl">{cg}<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'

def tblw_weight(h0, r0, r1): return sum(len(L(n)) for n in range(h0, r1 + 1))

def steps_list(nums, navy_first=False, label_split=True):
    items = ''
    for k, n in enumerate(nums):
        s = L(n)
        m = re.match(r'^(\d+)\.\s+(.*)$', s, flags=re.S)
        num, rest = (m.group(1), m.group(2)) if m else (str(k + 1), s)
        if label_split and ':' in rest and rest.index(':') < 40:
            a, b = rest.split(':', 1)
            rest_html = f'<b>{esc(a)}:</b>{esc(b)}'
        else:
            rest_html = esc(rest)
        cl = 'card--navy' if (navy_first and k == 0) else ''
        items += f'<div class="card stp fx fx--dots {cl}"><span class="nn">{num}</span><div class="tx">{rest_html}</div></div>'
    rows = (len(list(nums)) + 1) // 2
    return f'<div class="steps7" style="grid-template-rows:repeat({rows},minmax(0,1fr))">{items}</div>'

# ---------- láminas ----------
SL = []   # (html_inner, crumb, mx, mn)
def title_html(t):
    t = nb(t)
    if '—' in t:
        a, b = t.split('—', 1)
        return f'{esc(a.strip())} — <span class="em">{esc(b.strip())}</span>'
    w = t.split(' ')
    if len(w) <= 3: return f'<span class="em">{esc(t)}</span>'
    k = 2
    return esc(' '.join(w[:-k])) + ' <span class="em">' + esc(' '.join(w[-k:])) + '</span>'

def add(title, crumb, inner, mx=13.5, mn=8.0):
    SL.append(dict(title=title, crumb=crumb, inner=inner, mx=mx, mn=mn))

# ---- 2 · Carta ----
def letter():
    parts = L(10).split('\n')
    sg = L(13).split('\n')
    to = f'<div class="to">{esc(parts[0])}<b>{esc(parts[1])}</b></div>'
    body = f'<p>{fm(L(11))}</p><p>{fm(L(12))}</p>'
    sig = f'<div class="sg">{esc(sg[0])}<b>{esc(sg[1])}</b>{esc(sg[2])}<br>{esc(sg[3])}</div>'
    return area(f'<div class="card letter fx fx--arcs"><div class="dt">{esc(L(9))}</div>{to}{body}{sig}</div>')
add(L(8), 'carta', letter(), mx=14.5)

# ---- 1 ----
add(L(14), 'objeto', area(vrows(
    blk(None, [15], 'target', tone='violet', fx='fx--arcs fx--dots'),
    blk(None, [16], 'ban', kind='card--navy', fx='fx--arcs fx--chev'))), mx=15)
# ---- 2 ----
add(L(17), 'alcance de IA', area(vrows(
    blk(None, [18], 'bot', tone='violet', fx='fx--arcs fx--dots'),
    blk(None, [19], 'cloud', kind='card--violet', fx='fx--arcs fx--dots'))), mx=14)
# ---- 3 ----
add(L(20), 'calendario', area(table(21, 23, 32, 2, [27, 73])), mx=14)
# ---- 4 ----
add(L(33), 'arquitectura', area(vrows(
    blk(None, [34], 'server', tone='sky', fx='fx--arcs fx--dots'),
    blk(None, [35], 'db', kind='card--navy', fx='fx--arcs fx--chev'))), mx=14)
# ---- 5 ----
add(L(36), 'consumos', area(vrows(
    blk(None, [37], 'coin', tone='gold', fx='fx--arcs fx--dots'),
    blk(None, [38], 'layers', kind='card--violet', fx='fx--arcs fx--dots'))), mx=14)
# ---- 6 y 7 ----
add(L(39), 'seguimiento y soporte', area(
    table(40, 42, 47, 2, [27, 73], style='flex:none') +
    blk(L(48), [49], 'mail', kind='card--navy', tone='gold', fx='fx--arcs fx--dots')[1]), mx=12.5)
# ---- 8 ----
add(L(50), 'equipo', area(table(51, 53, 68, 2, [28, 72])), mx=12)
# ---- 9 intro + 9.1 ----
add(L(69), 'propuesta económica', area(vrows(
    blk(None, [70], 'coin', tone='gold', fx='fx--arcs fx--dots'),
    blk(nb(L(71)), [72], 'handshake', kind='card--navy', fx='fx--arcs fx--chev'))), mx=13.5)
# ---- 9.2 ----
def comp_cards():
    icons = ['layers', 'bot', 'phone', 'sliders', 'users', 'wrench']
    kinds = ['card--navy', '', '', '', '', 'card--violet']
    tones = ['gold', 'violet', 'sky', 'gold', 'green', 'gold']
    cells = []
    for i, n in enumerate(range(74, 80)):
        a, b = L(n).split(':', 1)
        cells.append(f'<div class="card blk {kinds[i]} fx fx--arcs" style="flex:1 1 0"><div class="bh">{ic(icons[i], tones[i])}<h3>{esc(a)}</h3></div><p>{esc(b.strip())}</p></div>')
    return f'<div class="hrow">{"".join(cells[:3])}</div><div class="hrow">{"".join(cells[3:])}</div>'
add(nb(L(73)), 'componentes del valor', area(comp_cards()), mx=12.5)
# ---- 9.3 ----
add(nb(L(80)), 'capacidad operativa', area(vrows(
    blk(None, [81], 'target', tone='violet', fx='fx--arcs fx--dots'),
    blk(None, [82], 'trend', kind='card--navy', fx='fx--arcs fx--chev'))), mx=14)
# ---- 9.4 y 9.5 ----
add(nb(L(83)), 'distribución económica', area(hrow(
    blk(None, [84], 'handshake', tone='sky', fx='fx--arcs fx--dots'),
    blk(nb(L(85)), [86], 'doc', kind='card--navy', fx='fx--arcs fx--chev'))), mx=13.5)
# ---- 9.6 (a) con precios ----
def price_cards():
    c1 = (f'<div class="card price card--navy neon fx fx--arcs" style="flex:1 1 0"><span class="pl">{esc(L(93))}</span>'
          f'<span class="pv">{esc(L(94))}</span><span class="pc">{esc(nb(L(92)))}</span></div>')
    c2 = (f'<div class="card price card--violet fx fx--arcs" style="flex:1 1 0"><span class="pl">{esc(L(95))}</span>'
          f'<span class="pv">{esc(L(96))}</span><span class="pc">{esc(nb(L(92)))}</span></div>')
    return f'<div class="hrow" style="flex:none;height:1.5in">{c1}{c2}</div>'
add(nb(L(87)), 'condiciones comerciales', area(price_cards() + hrow(
    blk(None, [88], 'coin', tone='gold', fx='fx--arcs', w=300),
    blk(None, [89], 'cart', tone='violet', fx='fx--arcs', w=300),
    blk(None, [90], 'calendar', tone='sky', fx='fx--arcs fx--dots', w=600))), mx=13)
# ---- 9.6 (b) ----
add(nb(L(87)), 'condiciones comerciales', area(vrows(
    blk(None, [97], 'calendar', tone='gold', fx='fx--arcs fx--dots'),
    blk(None, [98], 'cart', kind='card--navy', fx='fx--arcs fx--chev'))), mx=14)
# ---- 10 y 11 ----
add(L(99), 'contratación y exclusiones', area(hrow(
    blk(None, [100], 'pen', tone='violet', fx='fx--arcs fx--dots'),
    blk(L(101), [102], 'ban', kind='card--navy', fx='fx--arcs fx--chev'))), mx=14)
# ---- 12 Anexo (intro) ----
add(L(103), 'anexo técnico', area(vrows(
    blk(None, [104], 'doc', tone='violet', fx='fx--arcs fx--dots'),
    blk(None, [105], 'book', kind='card--navy', fx='fx--arcs fx--chev', w=250))), mx=15)
# ---- Objeto y alcance ----
add(L(106), 'objeto y alcance del servicio', area(
    hrow(blk(None, [107, 108], 'target', tone='violet', fx='fx--arcs fx--dots'),
         blk(None, [109, 110, 111, 112, 113], None, tone='sky', fx='fx--arcs fx--dots')) +
    blk(None, [114], 'ban', kind='card--navy', fx='fx--arcs fx--chev', w=250, fl='none')[1]), mx=12.5)
# ---- Flujo ----
add(L(115), 'flujo del servicio', area(steps_list(range(116, 123), navy_first=False)), mx=13)
# ---- IA ----
add(L(123), 'inteligencia artificial', area(
    blk(None, [124], 'bot', kind='card--navy', fx='fx--arcs fx--dots', w=300, fl='none')[1] +
    table(125, 128, 142, 3, [20, 46, 34]) +
    blk(None, [143], 'cloud', tone='sky', fx='fx--arcs fx--dots', w=120, fl='none')[1]), mx=11)
# ---- Arquitectura ----
def arch_html():
    left = ['Aplicación', 'Base de datos', 'Workers']
    right = ['Voz', 'Telefonía', 'WhatsApp', 'Correo', 'Modelo de lenguaje']
    arrow = f'<div class="ar"><span>HTTPS</span><svg viewBox="0 0 24 24">{IC["arrow"]}</svg><svg viewBox="0 0 24 24" style="transform:scaleX(-1)">{IC["arrow"]}</svg><span>webhooks</span></div>'
    return (f'<div class="arch"><div class="card card--navy pn"><span class="pt" style="color:var(--gold)">Servidores de la Alcaldía</span><div class="chips">' +
            ''.join(f'<span class="chip">{c}</span>' for c in left) + f'</div></div>{arrow}<div class="card card--violet pn"><span class="pt" style="color:var(--gold)">Servicios en la nube</span><div class="chips">' +
            ''.join(f'<span class="chip">{c}</span>' for c in right) + '</div></div></div>')
add(L(144), 'arquitectura del servicio', area(
    f'<div style="flex:none">{arch_html()}</div>' +
    '<div class="vcol" style="flex:1">' + blk(None, [145], 'server', tone='violet', fx='fx--arcs fx--dots')[1] + blk(None, [147], 'link', tone='sky', fx='fx--arcs fx--chev')[1] + '</div>'), mx=13)
# ---- Stack ----
add(L(148), 'stack tecnológico', area(
    blk(None, [149], 'chip', tone='violet', fx='fx--arcs', w=200, fl='none')[1] + table(150, 153, 185, 3, [31, 41, 28]) +
    blk(None, [186], 'plug', kind='card--navy', fx='fx--arcs', w=100, fl='none')[1]), mx=10.5)
# ---- Componentes ----
add(L(187), 'componentes y licencias', area(
    blk(None, [188], 'cart', kind='card--navy', fx='fx--arcs fx--dots', w=200, fl='none')[1] + table(189, 192, 212, 3, [38, 22, 40])), mx=11)
# ---- Consumo ----
add(L(213), 'consumo incluido', area(
    blk(None, [214], 'coin', tone='gold', fx='fx--arcs fx--dots', w=200, fl='none')[1] + table(215, 218, 229, 3, [20, 44, 36]) +
    blk(None, [230], 'flag', kind='card--violet', fx='fx--arcs', w=80, fl='none')[1]), mx=11.5)
# ---- Ruta ----
add(L(231), 'ruta de implementación', area(
    blk(None, [232], 'calendar', tone='sky', fx='fx--arcs fx--dots', w=150, fl='none')[1] + table(233, 236, 250, 3, [22, 50, 28])), mx=12)
# ---- Fase 1 ----
add(L(251), 'fase 1', area(
    blk(None, [252], 'eye', kind='card--navy', fx='fx--arcs fx--dots', w=180, fl='none')[1] +
    hrow(blk(L(253), range(254, 260), 'search', tone='violet', fx='fx--arcs fx--dots'),
         blk(L(260), range(261, 267), 'server', tone='sky', fx='fx--arcs fx--dots'))), mx=12)
add(L(251), 'fase 1', area(hrow(
    blk(L(267), range(268, 274), 'search', tone='violet', fx='fx--arcs fx--dots'),
    blk(L(274), range(275, 279), 'folder', tone='sky', fx='fx--arcs fx--dots'))), mx=12)
add(L(251), 'fase 1', area(hrow(
    blk(L(279), range(280, 284), 'chart', tone='green', fx='fx--arcs fx--dots'),
    blk(L(284), range(285, 291), 'map', tone='gold', fx='fx--arcs fx--dots'))), mx=12)
# ---- Fase 2 ----
add(L(291), 'fase 2', area(
    blk(None, [292, 293], 'zap', kind='card--navy', fx='fx--arcs fx--dots', w=250, fl='none')[1] +
    steps_list(range(294, 299), label_split=False).replace('style="grid-template-rows:repeat(3,minmax(0,1fr))"', 'style="grid-auto-flow:row;grid-template-rows:none;flex:1"') +
    ''), mx=11.5)
add(L(291), 'fase 2', area(hrow(
    blk(L(299), [300] + list(range(301, 307)), 'zap', tone='violet', fx='fx--arcs fx--dots'),
    blk(L(307), [308] + list(range(309, 316)), 'phone', tone='sky', fx='fx--arcs fx--dots'))), mx=11.5)
add(L(291), 'fase 2', area(hrow(
    blk(L(316), range(317, 322), 'chat', tone='green', fx='fx--arcs fx--dots', w=600),
    vcol(blk(L(322), range(323, 326), 'mail', tone='gold', fx='fx--arcs fx--dots'),
         blk(L(326), range(327, 330), 'chart', kind='card--navy', fx='fx--arcs fx--chev')))), mx=12.5)
# ---- Fase 3 ----
add(L(330), 'fase 3', area(
    blk(None, [331], 'users', kind='card--navy', fx='fx--arcs fx--dots', w=150, fl='none')[1] +
    hrow(blk(L(332), range(333, 337), 'clip', tone='violet', fx='fx--arcs fx--dots'),
         blk(L(337), [338] + list(range(339, 344)), 'map', tone='gold', fx='fx--arcs fx--dots'))), mx=12)
add(L(330), 'fase 3', area(hrow(
    blk(L(344), [345] + list(range(346, 350)), 'coin', tone='green', fx='fx--arcs fx--dots'),
    blk(L(350), [351], 'shield', kind='card--navy', fx='fx--arcs fx--chev'))), mx=13)
# ---- Transversales ----
add(L(352), 'componentes transversales', area(
    blk(None, [353], 'layers', kind='card--violet', fx='fx--arcs fx--dots', w=100, fl='none')[1] +
    hrow(blk(L(354), range(355, 362), 'lock', tone='violet', fx='fx--arcs fx--dots'),
         blk(L(362), range(363, 366), 'bot', tone='sky', fx='fx--arcs fx--dots'))), mx=12.5)
add(L(352), 'componentes transversales', area(hrow(
    blk(L(366), range(367, 372), 'check', tone='green', fx='fx--arcs fx--dots'),
    blk(L(372), [373] + list(range(374, 382)), 'server', tone='sky', fx='fx--arcs fx--dots'))), mx=11.5)
add(L(352), 'componentes transversales', area(hrow(
    blk(L(382), range(383, 386), 'users', tone='violet', fx='fx--arcs fx--dots'),
    blk(L(386), [387] + list(range(388, 392)), 'wrench', kind='card--navy', fx='fx--arcs fx--chev'))), mx=13)
# ---- Integraciones ----
add(L(392), 'integraciones', area(
    blk(None, [393], 'plug', tone='violet', fx='fx--arcs', w=120, fl='none')[1] + table(394, 398, 449, 4, [27, 30, 33, 10], center_last=True)), mx=10)
# ---- Infraestructura ----
add(L(450), 'infraestructura', area(
    blk(None, [451], 'server', tone='sky', fx='fx--arcs fx--dots', w=300, fl='none')[1] +
    blk(None, [452], None, kind='card--navy', fx='fx--arcs', w=40, fl='none')[1] +
    table(453, 458, 477, 5, [22, 10, 14, 24, 30]) +
    blk(None, [478], 'db', tone='gold', fx='fx--arcs fx--dots', w=100, fl='none')[1]), mx=11.5)
add(L(450), 'responsabilidades', area(table(479, 482, 505, 3, [14, 45, 41])), mx=10)
# ---- Insumos ----
def chk():
    its = ''.join(f'<div class="card it">{esc(bl(n))}</div>' for n in range(508, 522))
    return '<div class="chk" style="grid-template-rows:repeat(7,minmax(0,1fr))">' + its + '</div>'
add(L(506), 'insumos y accesos', area(
    blk(None, [507], 'folder', kind='card--navy', fx='fx--arcs', w=40, fl='none')[1] + chk()), mx=11.5)
# ---- Fuera de alcance ----
add(L(522), 'fuera de alcance', area(hrow(
    blk(None, [523] + list(range(524, 527)), 'ban', kind='card--navy', fx='fx--arcs fx--chev'),
    blk(None, [527], 'flag', tone='violet', fx='fx--arcs fx--dots', w=200))), mx=13.5)
add(L(522), 'ampliaciones (fase 4)', area(table(528, 530, 541, 2, [27, 73])), mx=12)
# ---- Seguimiento ----
add(L(542), 'seguimiento del servicio', area(
    blk(None, [543], 'clip', kind='card--navy', fx='fx--arcs fx--dots', w=200, fl='none')[1] +
    hrow(blk(None, [544], 'server', tone='sky', fx='fx--arcs fx--dots', w=300),
         blk(None, [545], 'coin', tone='gold', fx='fx--arcs fx--dots', w=300))), mx=15)
# ---- Equipo ----
add(L(546), 'equipo', area(table(547, 549, 564, 2, [30, 70])), mx=12)
# ---- Componentes de valor ----
add(L(565), 'componentes de valor', area(
    blk(None, [566], 'layers', kind='card--navy', fx='fx--arcs fx--dots', w=100, fl='none')[1] +
    blk(None, [567, 568, 569, 570, 571, 572], None, tone='violet', fx='fx--arcs fx--dots')[1]), mx=14)
# ---- Entregables ----
add(L(573), 'entregables y aceptación', area(
    blk(None, [574], 'check', kind='card--violet', fx='fx--arcs', w=120, fl='none')[1] + table(575, 577, 598, 2, [76, 24], center_last=True)), mx=12)

# ---- Formalización (PDF final enviado a la Alcaldía; texto literal) ----
FORM_1 = ('Para formalizar se propone una mesa técnica, jurídica y financiera que valide el inventario de funcionalidades '
          'disponibles en enero de 2027, el cronograma de entregas posteriores, criterios de aceptación, infraestructura, '
          'parámetros de consumo incluido, niveles de servicio, tratamiento de datos y términos de transferencia de la opción '
          'de compra con marca blanca.')
FORM_2 = 'Se firma su aceptación a los veintitrés (23) días del mes de octubre de 2026 en el municipio de Girón, Santander.'
def formal():
    sigs = ('<div class="sigs">'
            '<div class="card sig fx fx--dots"><div class="sp"></div><div class="bar"></div><b class="nm">YESENIA MERCHÁN</b><span>C.C. No. 1.065.866.676</span><span>Representante Legal</span><span class="co">CAMPUSLANDS S.A.S. BIC</span></div>'
            '<div class="card sig fx fx--dots"><div class="sp"></div><div class="bar"></div><b class="nm">CAMPO ELÍAS RAMIREZ</b><span>C.C. No.</span><span>Alcalde</span><span class="co">ALCALDÍA DE GIRÓN</span></div>'
            '</div>')
    top = ('<div class="vcol" style="flex:1">'
           f'<div class="card blk fx fx--arcs fx--dots row" style="flex:3 1 0">{ic("handshake","violet")}<div class="tx"><p>{esc(FORM_1)}</p></div></div>'
           f'<div class="card blk card--navy fx fx--arcs fx--chev row" style="flex:1.3 1 0">{ic("pen","gold")}<div class="tx"><p>{esc(FORM_2)}</p></div></div>'
           '</div>')
    return area(top + sigs)
add('Formalización de la propuesta', 'formalización', formal(), mx=13.5)

# =============== ensamblado ===============
CRUMB = lambda c: f'<div class="ft"><span class="crumbs">| campuslands<i>|</i>propuesta<i>|</i>giron<i>|</i>{esc(c)} |</span><span class="lema">Exploramos · Despegamos · Conquistamos</span></div>'
COBRAND = '<div class="cobrand"><img data-logo="campuslands" src="../assets/logo-campuslands-color.png" alt="Campuslands"><span class="x" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19"/></svg></span><img data-logo="cliente" src="assets/logo-cliente-color.png" alt="Alcaldía Municipal de Girón"></div>'
DECO = '<svg class="deco-cover" viewBox="0 0 1056 594" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><radialGradient id="cvGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#5E3AE2" stop-opacity=".15"/><stop offset="100%" stop-color="#5E3AE2" stop-opacity="0"/></radialGradient></defs><circle cx="528" cy="297" r="240" fill="url(#cvGlow)"/><circle class="ring accent" cx="528" cy="297" r="150"/><circle class="ring" cx="528" cy="297" r="235"/><circle class="ring r2" cx="528" cy="297" r="320"/><circle class="ring r3" cx="528" cy="297" r="410"/><path class="blade blade--l" transform="translate(134,134) scale(-.6475 .68)" d="M20 10 L400 240 L20 470 Q190 240 20 10 Z"/><path class="blade blade--r" transform="translate(922,134) scale(.6475 .68)" d="M20 10 L400 240 L20 470 Q190 240 20 10 Z"/></svg>'

def cover():
    sub = L(2)
    para = L(3)
    return (f'<div class="slide active" data-slide="1"><div class="sl cover" data-bg="white">{DECO}'
            f'<div class="mid">{COBRAND}<h1 class="sec"><span class="mark">&lt;/</span>Propuesta comercial y <span class="em">técnica</span></h1>'
            f'<p class="sub">{esc(sub)}</p><p class="tagline">Versión 2.0</p><p class="note">Para revisión técnica, jurídica, financiera y contractual</p></div>'
            f'<div class="meta"><div><small>Preparado para</small><span>Alcaldía Municipal de Girón<br>Industria y Comercio (ICA)</span></div>'
            f'<div><small>Preparado por</small><span>Campuslands S.A.S. BIC · Full Service</span></div>'
            f'<div><small>Fecha</small><span>Octubre 2026</span></div></div></div></div>')

def build(fit_mode=False):
    out = [cover()]
    for i, s in enumerate(SL, start=2):
        fs = FIT.get(str(i), min(s['mx'], 11))
        out.append(f'<div class="slide" data-slide="{i}"><div class="sl" data-bg="white" data-mx="{s["mx"]}" data-mn="{s["mn"]}" style="--fs:{fs}pt">'
                   f'<div class="ghost">{i:02d}</div><h2 class="sec sec-top"><span class="mark">&lt;/</span>{title_html(s["title"])}</h2>'
                   f'{s["inner"]}{CRUMB(s["crumb"])}</div></div>')
    n = len(out)
    head = ('<!DOCTYPE html>\n<html lang="es">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '  <title>Alcaldía Municipal de Girón</title>\n  <link rel="icon" type="image/png" href="assets/favicon.png">\n  <link rel="stylesheet" href="styles.css">\n</head>\n<body>\n'
            f'  <header class="app-header">{COBRAND}</header>\n  <main class="app-content"><section class="slides-container" id="slides-container">\n')
    foot = (f'  </section></main>\n  <footer class="slides-footer-controls">\n'
            '    <button id="btn-prev-slide" class="control-btn" onclick="navigateSlide(-1)" aria-label="Lámina anterior"><svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2" fill="none"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg></button>\n'
            f'    <div class="slide-indicator"><span id="slide-number-display">1 / {n}</span><div class="progress-bar-bg"><div id="slide-progress" class="progress-bar-fill"></div></div>\n'
            '      <div class="playback-controls"><button id="btn-autoplay" class="control-btn mini" title="Reproducción automática" onclick="toggleAutoplay()"><svg id="autoplay-icon" viewBox="0 0 24 24" width="16" height="16" fill="currentColor" stroke="none"><polygon points="5 3 19 12 5 21 5 3"/></svg></button></div></div>\n'
            '    <button id="btn-next-slide" class="control-btn" onclick="navigateSlide(1)" aria-label="Lámina siguiente"><svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2" fill="none"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></button>\n'
            '  </footer>\n  <script src="script.js"></script>\n')
    if fit_mode:
        foot += '<script>' + open(os.path.join(TMP, 'fit.js'), encoding='utf8').read() + '</script>\n'
    foot += '</body>\n</html>\n'
    return head + '\n'.join(out) + '\n' + foot, n

if __name__ == '__main__':
    fit_mode = len(sys.argv) > 1 and sys.argv[1] == 'fit'
    htm, n = build(fit_mode)
    target = os.path.join(DECK, 'index_fit.html' if fit_mode else 'index.html')
    open(target, 'w', encoding='utf8').write(htm)
    if not fit_mode:
        p = os.path.join(DECK, 'script.js')
        s = open(p, encoding='utf8').read()
        s = re.sub(r'totalSlides:\s*\d+', f'totalSlides: {n}', s)
        open(p, 'w', encoding='utf8').write(s)
    print('slides', n, '->', target)
