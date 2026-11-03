# -*- coding: utf-8 -*-
"""kit.py — arquetipos de lámina, íconos y ensamblador de guías (sistema v3 de presentations-designer).

Cada función de arquetipo devuelve un dict {cls, section, html}; el Deck añade ghost (numeral), pie con migas y envoltorio.
Texto con formato mínimo: **negrita** y `código` (todo se escapa antes). Nada de fuentes que no sean Poppins.
"""
import html
import re

# ---------------------------------------------------------------- texto
def fmt(s):
    s = html.escape(str(s), quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s


def title_html(t):
    """Título de sección: '</ ' + texto; lo que va entre ~~ ~~ se vuelve acento (Black Italic violeta)."""
    t = html.escape(t, quote=False)
    t = re.sub(r'~~(.+?)~~', r'<span class="em">\1</span>', t)
    return '<span class="mark">&lt;/</span>' + t


# ---------------------------------------------------------------- íconos (trazo uniforme 24×24)
ICONS = {
    'folder': '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    'file': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    'search': '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    'shield': '<path d="M12 2 4 5v6c0 5.2 3.4 9.5 8 11 4.6-1.5 8-5.8 8-11V5z"/><path d="m9 12 2 2 4-4"/>',
    'check': '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    'checkc': '<circle cx="12" cy="12" r="9"/><path d="m8 12.5 3 3 5-6"/>',
    'x': '<path d="M6 6l12 12M18 6 6 18"/>',
    'ban': '<circle cx="12" cy="12" r="9"/><path d="m5.6 5.6 12.8 12.8"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'terminal': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="m7 9 3 3-3 3M13 15h4"/>',
    'book': '<path d="M12 6c-1.5-1.3-3.7-2-6-2H3v14h3c2.3 0 4.5.7 6 2 1.5-1.3 3.7-2 6-2h3V4h-3c-2.3 0-4.5.7-6 2z"/><path d="M12 6v14"/>',
    'list': '<path d="m4 6 1.5 1.5L8 5M4 12l1.5 1.5L8 11M4 18l1.5 1.5L8 17M12 6h8M12 12h8M12 18h8"/>',
    'send': '<path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    'building': '<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2M10 21v-3h4v3"/>',
    'calc': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h.01M12 12h.01M16 12h.01M8 16h.01M12 16h.01M16 16h.01"/>',
    'sheet': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M8 13h8M8 17h8M12 13v6"/>',
    'scale': '<path d="M12 3v18M7 21h10M5 7h14"/><path d="m5 7-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/>',
    'pen': '<path d="m4 20 1-4L16.5 4.5a2.1 2.1 0 0 1 3 3L8 19z"/><path d="m14 7 3 3"/>',
    'present': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M12 16v4M8 20h8M7 12l3-3 3 2 4-4"/>',
    'layers': '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    'cpu': '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    'zap': '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    'alert': '<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17.5h.01"/>',
    'help': '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 0 1 5 .5c0 1.5-2.5 2-2.5 3.5M12 17h.01"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    'gear': '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9 7 7M17 17l2.1 2.1M19.1 4.9 17 7M7 17l-2.1 2.1"/>',
    'refresh': '<path d="M20 11a8 8 0 0 0-14-4L4 9"/><path d="M4 4v5h5"/><path d="M4 13a8 8 0 0 0 14 4l2-2"/><path d="M20 20v-5h-5"/>',
    'eye': '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    'download': '<path d="M12 4v11M7 11l5 5 5-5M5 20h14"/>',
    'upload': '<path d="M12 16V5M7 9l5-5 5 5M5 20h14"/>',
    'db': '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/>',
    'code': '<path d="m8 8-5 4 5 4M16 8l5 4-5 4M14 5l-4 14"/>',
    'spark': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 3v4M17 5h4"/>',
    'bot': '<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 4v4M9 13v2M15 13v2M2 13v3M22 13v3"/><circle cx="12" cy="3.5" r="1"/>',
    'chat': '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 20l1-4.5A8 8 0 1 1 21 12z"/>',
    'flag': '<path d="M5 21V4M5 4h12l-2 4 2 4H5"/>',
    'compass': '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>',
    'radar': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><path d="M12 12 18 6"/>',
    'git': '<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="8" r="2.5"/><path d="M6 8.5v7M18 10.5c0 4-6 3-11 6"/>',
    'table': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 4v16"/>',
    'link': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    'palette': '<path d="M12 3a9 9 0 1 0 0 18c1.2 0 2-.8 2-1.8 0-.5-.2-.9-.5-1.3-.3-.4-.5-.8-.5-1.3 0-1 .8-1.6 1.8-1.6H17a4 4 0 0 0 4-4C21 6.5 17 3 12 3z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7" r="1"/><circle cx="15" cy="7" r="1"/>',
    'image': '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m21 16-5-5-9 9"/>',
    'monitor': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    'history': '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5M12 8v5l3 2"/>',
    'brief': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
    'percent': '<path d="M19 5 5 19"/><circle cx="7" cy="7" r="2.5"/><circle cx="17" cy="17" r="2.5"/>',
    'dollar': '<path d="M12 3v18M16 7.5c0-1.7-1.8-3-4-3s-4 1.3-4 3 1.8 2.8 4 3.5 4 1.8 4 3.5-1.8 3-4 3-4-1.3-4-3"/>',
    'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    'chart': '<path d="M3 3v18h18"/><path d="M8 17v-6M13 17V7M18 17v-3"/>',
    'rocket': '<path d="M5 15c-1.5 1.3-2 5-2 5s3.7-.5 5-2"/><path d="M12 15 9 12a22 22 0 0 1 3-6 12 12 0 0 1 8-3c0 3-1 6-3 8a22 22 0 0 1-5 4z"/><circle cx="15" cy="9" r="1.5"/>',
    'bulb': '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
    'pin': '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    'copy': '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"/>',
    'plus': '<path d="M12 5v14M5 12h14"/>',
    'net': '<circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="19" r="2.5"/><circle cx="19" cy="19" r="2.5"/><path d="M12 7.5v4M12 11.5 6.5 17M12 11.5l5.5 5.5"/>',
    'cloud': '<path d="M7 18a5 5 0 1 1 1.2-9.8A6 6 0 0 1 19.5 11 3.5 3.5 0 0 1 19 18z"/>',
    'stamp': '<path d="M5 21h14M7 17h10v-3a3 3 0 0 0-2-2.8V9a3 3 0 1 0-6 0v2.2A3 3 0 0 0 7 14z"/>',
    'quote': '<path d="M7 17c-2 0-3-1.3-3-3.5C4 10 6 8 9 7M16 17c-2 0-3-1.3-3-3.5 0-3.5 2-5.5 5-6.5"/>',
    'map': '<path d="m3 6 6-2 6 2 6-2v14l-6 2-6-2-6 2z"/><path d="M9 4v14M15 6v14"/>',
    'inbox': '<path d="M3 13h5l1 3h6l1-3h5"/><path d="M5 6l-2 7v5a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-5l-2-7z"/>',
}


def svg(name, cls=''):
    return '<svg viewBox="0 0 24 24" aria-hidden="true"%s>%s</svg>' % ((' class="%s"' % cls) if cls else '', ICONS[name])


TINTS = ['violet', 'sky', 'green', 'gold']


def ic(name, tone='t-violet', size=''):
    return '<span class="ic ic--%s %s">%s</span>' % (tone, size, svg(name))


def card_ic(name, card_tone, i=0, size=''):
    """Ícono con el color que corresponde a la tarjeta que lo contiene."""
    if card_tone == 'navy':
        t = 'gold'
    elif card_tone == 'violet':
        t = 'white'
    elif card_tone in ('gold', 'sky'):
        t = 'navy'
    elif card_tone == 'sand':
        t = 't-violet'
    else:
        t = 't-' + TINTS[i % 4]
    return ic(name, t, size)


FX = ['fx--dots', 'fx--arcs', 'fx--stripes', 'fx--plus', 'fx--chev']


def fx(i=0, tone=''):
    """Decoración discreta por tarjeta (rota para no repetir)."""
    pick = FX[i % len(FX)]
    extra = ' bl' if pick == 'fx--arcs' and i % 2 else ''
    return 'fx %s%s' % (pick, extra)


def card_cls(tone):
    return ('card--' + tone) if tone else ''


LEMA = 'Exploramos · Despegamos · Conquistamos'

DECO = ('<svg class="deco-cover" viewBox="0 0 1056 594" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>'
        '<radialGradient id="cvGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#5E3AE2" stop-opacity=".15"/>'
        '<stop offset="100%" stop-color="#5E3AE2" stop-opacity="0"/></radialGradient></defs>'
        '<circle cx="528" cy="297" r="240" fill="url(#cvGlow)"/><circle class="ring accent" cx="528" cy="297" r="150"/>'
        '<circle class="ring" cx="528" cy="297" r="235"/><circle class="ring r2" cx="528" cy="297" r="320"/>'
        '<circle class="ring r3" cx="528" cy="297" r="410"/>'
        '<path class="blade blade--l" transform="translate(134,134) scale(-.6475 .68)" d="M20 10 L400 240 L20 470 Q190 240 20 10 Z"/>'
        '<path class="blade blade--r" transform="translate(922,134) scale(.6475 .68)" d="M20 10 L400 240 L20 470 Q190 240 20 10 Z"/></svg>')


def reading(label, text, tone='violet', tall=False):
    return ('<div class="card card--%s fx fx--arcs bl reading%s"><b>&lt;= %s</b><span>%s =&gt;</span></div>'
            % (tone, ' tall' if tall else '', html.escape(label), fmt(text)))


def _title(t, cls='sec sec-top'):
    return '<h2 class="%s">%s</h2>' % (cls, title_html(t))


# ================================================================ ARQUETIPOS
def statement(section, title, lede, stat_big, stat_label, points=None, hs=None):
    pts = ''
    if points:
        pts = '<ul class="list" style="margin-top:.2in;max-width:5.6in;--fs:10.5pt">%s</ul>' % ''.join('<li><span>%s</span></li>' % fmt(p) for p in points)
    st = ' style="--hs:%s"' % hs if hs else ''
    body = ('<div class="statement"%s><div><span class="qmark"><svg viewBox="0 0 64 40" aria-hidden="true"><path d="M0 40 14 0h16L20 40zM34 40 48 0h16L54 40z"/></svg></span>'
            '<h2 class="sec">%s</h2><p class="lede">%s</p>%s</div>'
            '<div class="card card--navy neon fx fx--arcs fx--dots stat"><b>%s</b><span>%s</span></div></div>'
            % (st, title_html(title), fmt(lede), pts, html.escape(stat_big), fmt(stat_label).replace('\n', '<br>')))
    return dict(cls='', section=section, html=body)


def cards(section, title, items, cols=3, fs=None, fh=None, read=None, row=False):
    """items: (icono, título, texto, tono) — tono '' | navy | violet | gold | sky | sand."""
    out = []
    for i, it in enumerate(items):
        icon, h, p = it[0], it[1], it[2]
        tone = it[3] if len(it) > 3 else ''
        if row:
            out.append('<div class="card mod row %s %s">%s<div class="t"><h3>%s</h3><p>%s</p></div></div>'
                       % (card_cls(tone), fx(i), card_ic(icon, tone, i), fmt(h), fmt(p)))
        else:
            out.append('<div class="card mod %s %s">%s<h3>%s</h3><p>%s</p></div>'
                       % (card_cls(tone), fx(i), card_ic(icon, tone, i), fmt(h), fmt(p)))
    style = '--cols:%d;' % cols + ('--fs:%s;' % fs if fs else '') + ('--fh:%s;' % fh if fh else '')
    body = _title(title) + '<div class="grid" style="%s">%s</div>' % (style, ''.join(out))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def flow(section, title, steps, read=None, compact=False):
    """steps: (icono, título, texto[, quién])."""
    n = len(steps)
    out = []
    for i, s in enumerate(steps):
        who = ('<div class="who">%s</div>' % html.escape(s[3])) if len(s) > 3 and s[3] else ''
        out.append('<div class="card step fx fx--arcs" style="--r1:40px;--r2:70px;--r3:84px;--r4:110px"><div class="n">%02d</div>%s<h3>%s</h3><p>%s</p>%s</div>'
                   % (i + 1, ic(s[0], 'violet'), fmt(s[1]), fmt(s[2]), who))
    body = _title(title) + '<div class="flow n%d%s">%s</div>' % (n, ' compact' if compact else '', ''.join(out))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def versus(section, title, left, right, arrow=True, fs=None, read=None):
    """left/right: dict(pill, h, items, delta=(big, small)|None, tone='' | navy, no=False)."""
    def panel(p, default_tone):
        tone = p.get('tone', default_tone)
        pill = ('<span class="pill pill--%s" style="align-self:flex-start">%s</span>'
                % ('white' if tone == 'navy' else 'violet', html.escape(p['pill'])))
        lis = ''.join('<li><span>%s</span></li>' % fmt(x) for x in p['items'])
        d = ''
        if p.get('delta'):
            d = '<div class="delta"><b>%s</b><span>%s</span></div>' % (html.escape(p['delta'][0]), fmt(p['delta'][1]))
        return ('<div class="card %s panel %s fx fx--arcs %s">%s<h3>%s</h3><ul class="list">%s</ul>%s</div>'
                % (card_cls(tone), 'no' if p.get('no') else '', 'fx--chev' if tone == 'navy' else 'fx--dots', pill, fmt(p['h']), lis, d))
    go = '<div class="go"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>' if arrow else ''
    style = ' style="--fs:%s%s"' % (fs or '11.5pt', '' if arrow else ';grid-template-columns:1fr 1fr')
    body = _title(title) + '<div class="versus"%s>%s%s%s</div>' % (style, panel(left, ''), go, panel(right, 'navy'))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def tree(section, title, rows, notes, wide=False, tf=None, tg=None):
    """rows: (nivel, tipo, nombre, comentario[, etiqueta]) — tipo dir|file|gen; etiqueta 'solo lectura' | 'agente' | 'generado'."""
    out = []
    for r in rows:
        lv, kind, name, com = r[0], r[1], r[2], r[3]
        tag = ''
        if len(r) > 4 and r[4]:
            cls = {'solo lectura': 'ro', 'agente': 'ag', 'generado': ''}.get(r[4], '')
            tag = '<span class="tag %s">%s</span>' % (cls, html.escape(r[4]))
        icon = 'folder' if kind == 'dir' else 'file'
        out.append('<div class="tn %s" style="--lv:%d">%s<b>%s</b>%s%s</div>'
                   % (kind, lv, svg(icon), html.escape(name), tag, ('<span class="c">%s</span>' % fmt(com)) if com else ''))
    side = []
    for i, n in enumerate(notes):
        tone = n[3] if len(n) > 3 else ''
        side.append('<div class="card %s fx %s">%s<h3>%s</h3><p>%s</p></div>' % (card_cls(tone), FX[(i + 1) % 5], card_ic(n[0], tone, i, 'ic--sm'), fmt(n[1]), fmt(n[2])))
    n = len(rows)
    tf = tf or ('11pt' if n <= 11 else '10.5pt' if n <= 13 else '10pt' if n <= 15 else '9.5pt')
    tg = tg or ('6px' if n <= 11 else '4px' if n <= 13 else '3px' if n <= 15 else '2px')
    style = '--tf:%s;--tg:%s;' % (tf, tg)
    body = (_title(title) + '<div class="tree-wrap%s"><div class="card tree fx fx--dots" style="%s">%s</div><div class="side">%s</div></div>'
            % (' wide' if wide else '', style, ''.join(out), ''.join(side)))
    return dict(cls='', section=section, html=body)


def table(section, title, cols, rows, widths, tf=None, read=None):
    head = '<div class="rw h" style="--cols:%s">%s</div>' % (widths, ''.join('<span>%s</span>' % html.escape(c) for c in cols))
    body_rows = ''.join('<div class="rw b" style="--cols:%s">%s</div>' % (widths, ''.join('<span>%s</span>' % fmt(c) for c in r)) for r in rows)
    style = ' style="--tf:%s"' % tf if tf else ''
    body = _title(title) + '<div class="tbl"%s>%s%s</div>' % (style, head, body_rows)
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def cmds(section, title, items, tone='navy', read=None):
    """items: (etiqueta, [comandos], descripción)."""
    out = []
    for i, it in enumerate(items):
        label, cl, desc = it
        codes = ''.join('<code>%s</code>' % html.escape(c) for c in cl)
        out.append('<div class="card %s cmd fx %s"><div class="k">%s</div><div class="v">%s<p>%s</p></div></div>'
                   % (card_cls(tone), FX[(i + 1) % 5] if i % 2 else 'fx--arcs', html.escape(label), codes, fmt(desc)))
    body = _title(title) + '<div class="cmds%s">%s</div>' % (' light' if tone != 'navy' else '', ''.join(out))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def prompts(section, title, items, cols=2, fs=None, read=None):
    """items: (etiqueta, texto del mensaje[, nota])."""
    colors = ['var(--violet)', 'var(--sky)', 'var(--green)', 'var(--gold)']
    out = []
    for i, it in enumerate(items):
        note = '<p>%s</p>' % fmt(it[2]) if len(it) > 2 and it[2] else ''
        out.append('<div class="card bubble fx %s" style="--c:%s"><span class="label">%s</span><q>%s</q>%s</div>'
                   % (FX[i % 5], colors[i % 4], html.escape(it[0]), fmt(it[1]), note))
    style = '--cols:%d;' % cols + ('--fs:%s;' % fs if fs else '')
    body = _title(title) + '<div class="prompts" style="%s">%s</div>' % (style, ''.join(out))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def faq(section, title, items, cols=2, fs=None, read=None):
    out = []
    for i, (q, a) in enumerate(items):
        out.append('<div class="card qa fx %s"><h3><i>?</i>%s</h3><p>%s</p></div>' % (FX[i % 5], fmt(q), fmt(a)))
    style = '--cols:%d;' % cols + ('--fs:%s;' % fs if fs else '')
    body = _title(title) + '<div class="faq" style="%s">%s</div>' % (style, ''.join(out))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def rules(section, title, items, cols=2, fs=None, tones=None, read=None):
    out = []
    for i, (h, p) in enumerate(items):
        tone = tones[i] if tones and i < len(tones) else ''
        out.append('<div class="card rule %s fx %s"><div class="n">%02d</div><div><h3>%s</h3><p>%s</p></div></div>'
                   % (card_cls(tone), FX[i % 5], i + 1, fmt(h), fmt(p)))
    style = '--cols:%d;' % cols + ('--fs:%s;' % fs if fs else '')
    body = _title(title) + '<div class="rules" style="%s">%s</div>' % (style, ''.join(out))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def checks(section, title, items, cols=2, read=None, kind='ok'):
    """items: (título, texto[, 'warn'|'no'])."""
    out = []
    for i, it in enumerate(items):
        k = it[2] if len(it) > 2 else kind
        mark = svg('x') if k == 'no' else svg('check')
        out.append('<div class="card chk %s fx %s"><span class="ok">%s</span><div><h3>%s</h3>%s</div></div>'
                   % ('' if k == 'ok' else k, FX[i % 5], mark, fmt(it[0]), ('<p>%s</p>' % fmt(it[1])) if it[1] else ''))
    body = _title(title) + '<div class="checks" style="--cols:%d">%s</div>' % (cols, ''.join(out))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def metrics(section, title, items, read=None, text_big=False):
    """items: (icono, etiqueta, grande, unidad, texto, color)."""
    n = len(items)
    out = []
    for i, it in enumerate(items):
        icon, label, big, unit, text = it[:5]
        color = it[5] if len(it) > 5 else TINTS[i % 4]
        cvar = {'violet': 'var(--violet)', 'sky': 'var(--sky)', 'green': 'var(--green)', 'gold': 'var(--gold)'}[color]
        out.append('<div class="card metric fx fx--dots" style="--c:%s;">%s<span class="label">%s</span><b class="n%s">%s<small>%s</small></b><p>%s</p></div>'
                   % (cvar, ic(icon, 't-' + color), html.escape(label), ' t' if text_big else '', html.escape(big), html.escape(unit), fmt(text)))
    body = _title(title) + '<div class="metrics%s">%s</div>' % ((' n%d' % n) if n in (2, 3) else '', ''.join(out))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def cols2(section, title, left, right, fs=None, read=None):
    """left/right: dict(h, items, tone)."""
    def col(c, i):
        tone = c.get('tone', '')
        return ('<div class="card %s fx %s">%s<h3>%s</h3><ul class="list">%s</ul></div>'
                % (card_cls(tone), 'fx--arcs bl' if i else 'fx--dots', card_ic(c.get('icon', 'list'), tone, i), fmt(c['h']),
                   ''.join('<li><span>%s</span></li>' % fmt(x) for x in c['items'])))
    style = ' style="--fs:%s"' % fs if fs else ''
    body = _title(title) + '<div class="cols2"%s>%s%s</div>' % (style, col(left, 0), col(right, 1))
    if read:
        body += reading(*read)
    return dict(cls='', section=section, html=body)


def close(title, steps, tagline, extra=None):
    st = ''.join('<div><b>%d</b><span>%s</span></div>' % (i + 1, fmt(s)) for i, s in enumerate(steps))
    body = (DECO + '<div class="mid"><p class="tagline">%s</p><h2 class="sec">%s</h2><div class="steps">%s</div>'
            '<div class="cobrand"><img data-logo="campuslands" src="../../assets/img/logo-campuslands-color.png" alt="Campuslands"></div></div>'
            % (html.escape(tagline), title_html(title), st))
    return dict(cls='close', section='cierre', html=body, close=True)


# ================================================================ ENSAMBLADOR
SCRIPT_SRC = '../../assets/guia.js'
CSS_SRC = '../../assets/styles.css'
LOGO_SRC = '../../assets/img/logo-campuslands-color.png'
FAV_SRC = '../../assets/img/favicon.png'

KINDS = {
    'dev': dict(label='Guía Dev', pill='gold', crumb='guía dev', aud='Developers', tagline='Cómo está construido, cómo funciona y cómo se mantiene'),
    'usuario': dict(label='Guía de usuario', pill='violet', crumb='guía de usuario', aud='Cualquier persona del equipo', tagline='Cómo usarlo, paso a paso y sin tecnicismos'),
}


def cover_html(meta, kind):
    k = KINDS[kind]
    cell2 = ('Carpeta del agente', meta['carpeta']) if kind == 'dev' else ('Se usa en', meta['plataforma'])
    return (DECO + '<div class="mid"><div class="cobrand"><img data-logo="campuslands" src="%s" alt="Campuslands"></div>'
            '<div class="kind"><span class="pill pill--%s">%s</span><span class="pill pill--navy">%s</span></div>'
            '<h1 class="sec"><span class="mark">&lt;/</span>%s</h1><p class="tagline">%s</p></div>'
            '<div class="meta"><div><small>Dirigida a</small><span>%s</span></div><div><small>%s</small><span>%s</span></div><div><small>Fecha</small><span>%s</span></div></div>'
            % (LOGO_SRC, k['pill'], k['label'], html.escape(meta['rol']), html.escape(meta['nombre']), html.escape(meta.get('tagline_' + kind, k['tagline'])),
               k['aud'], cell2[0], html.escape(cell2[1]), 'Noviembre 2026'))


def render_deck(meta, kind, slides):
    k = KINDS[kind]
    all_slides = [dict(cls='cover', section='portada', html=cover_html(meta, kind), cover=True)] + slides
    out = []
    for i, s in enumerate(all_slides):
        n = i + 1
        active = ' active' if n == 1 else ''
        parts = []
        if not s.get('cover') and not s.get('close'):
            parts.append('<div class="ghost">%02d</div>' % n)
        parts.append(s['html'])
        if not s.get('cover'):
            sec = html.escape(s['section'])
            crumbs = ('| campuslands<i>|</i>%s<i>|</i>%s<i>|</i>%s |' % (k['crumb'], html.escape(meta['corto']), sec)) if not s.get('close') else \
                     ('| campuslands<i>|</i>%s<i>|</i>%s |' % (k['crumb'], html.escape(meta['corto'])))
            parts.append('<div class="ft"><span class="crumbs">%s</span><span class="lema">%s</span></div>' % (crumbs, LEMA))
        out.append('<div class="slide%s" data-slide="%d"><div class="sl %s" data-bg="white">\n  %s</div></div>' % (active, n, s['cls'], '\n  '.join(parts)))
    header = ('<header class="app-header"><div class="cobrand"><img data-logo="campuslands" src="%s" alt="Campuslands">'
              '<span class="pill pill--violet guide-chip">%s · %s</span></div></header>' % (LOGO_SRC, k['label'], html.escape(meta['nombre'])))
    footer = ('<footer class="slides-footer-controls">\n'
              '    <button id="btn-prev-slide" class="control-btn" onclick="navigateSlide(-1)" aria-label="Lámina anterior"><svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2" fill="none"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg></button>\n'
              '    <div class="slide-indicator"><span id="slide-number-display">1 / %d</span><div class="progress-bar-bg"><div id="slide-progress" class="progress-bar-fill"></div></div>\n'
              '      <div class="playback-controls"><button id="btn-autoplay" class="control-btn mini" title="Reproducción automática" onclick="toggleAutoplay()"><svg id="autoplay-icon" viewBox="0 0 24 24" width="16" height="16" fill="currentColor" stroke="none"><polygon points="5 3 19 12 5 21 5 3"/></svg></button></div></div>\n'
              '    <button id="btn-next-slide" class="control-btn" onclick="navigateSlide(1)" aria-label="Lámina siguiente"><svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2" fill="none"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></button>\n'
              '  </footer>' % len(all_slides))
    title = '%s — %s' % (k['label'], meta['nombre'])
    return ('<!DOCTYPE html>\n<html lang="es">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '  <title>%s</title>\n  <link rel="icon" type="image/png" href="%s">\n  <link rel="stylesheet" href="%s">\n</head>\n<body>\n  %s\n'
            '  <main class="app-content"><section class="slides-container" id="slides-container">\n%s\n  </section></main>\n  %s\n  <script src="%s"></script>\n</body>\n</html>\n'
            % (html.escape(title), FAV_SRC, CSS_SRC, header, '\n'.join(out), footer, SCRIPT_SRC)), len(all_slides)
