# -*- coding: utf-8 -*-
"""md.py — convertidor mínimo de Markdown a HTML para las guías (sin dependencias).

Soporta: portada en frontmatter, ## ### ####, párrafos, listas anidadas, tablas, citas/avisos [!nota|importante|tip|cuidado],
código con ``` y bloques propios: tree · flow · lanes · chat · stats · cards · prompt · bash/powershell (con botón «Copiar») ·
repos · publicar · paleta, y el contenedor «::: switch» (selector entre paneles).
"""
import html
import re
import unicodedata


def slug(t):
    t = unicodedata.normalize('NFD', t)
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')


def inline(s):
    codes = []

    def keep(m):
        codes.append(m.group(1))
        return '\x00%d\x00' % (len(codes) - 1)
    s = re.sub(r'`([^`]+)`', keep, s)
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a class="l" href="\2">\1</a>', s)
    return re.sub(r'\x00(\d+)\x00', lambda m: '<code>%s</code>' % html.escape(codes[int(m.group(1))], quote=False), s)


def frontmatter(text):
    meta = {}
    lines = text.splitlines()
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                body = '\n'.join(lines[i + 1:])
                return meta, body
            if ':' in lines[i]:
                k, v = lines[i].split(':', 1)
                meta[k.strip()] = v.strip()
    return meta, text


# ---------------------------------------------------------------- bloques propios
ICONOS_SW = {
    'user': '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/></svg>',
    'terminal': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="m7 9 3 3-3 3M13 15h4"/></svg>',
    'claude': '<img src="@@REL@@assets/img/plataforma-claude.png" alt="" width="18" height="18">',
    'pplx': '<img src="@@REL@@assets/img/plataforma-perplexity.png" alt="" width="18" height="18">',
}
def _pairs(body):
    out = []
    for l in body:
        if not l.strip():
            continue
        a, _, b = l.partition('|')
        out.append((a.strip(), b.strip()))
    return out


def fence(kind, body):
    if kind == 'tree':
        rows = []
        for l in body:
            m = re.match(r'^(.*?)(\s{2,}#\s?(.*))?$', l.rstrip())
            name, com = m.group(1), m.group(3)
            lead = len(name) - len(name.lstrip())
            nm = html.escape(name.strip())
            cls = 'd' if name.strip().endswith('/') else ''
            row = ' ' * lead + ('<span class="%s">%s</span>' % (cls, nm) if cls else nm)
            if com is not None:
                pad = max(2, 34 - len(name))
                row += ' ' * pad + '<span class="c"># %s</span>' % html.escape(com)
            rows.append(row)
        return '<pre class="tree"><code>%s</code></pre>' % '\n'.join(rows)
    if kind == 'flow':
        vertical = bool(body and body[0].strip() == '@vertical')
        items = _pairs(body[1:] if vertical else body)
        lis = ''.join('<li><b>%s</b><span>%s</span></li>' % (inline(a), inline(b)) for a, b in items)
        n = len(items)
        cols = 2 if n <= 2 else (n if n <= 4 else (3 if n <= 6 else 4))        # filas equilibradas; sin flecha al final de fila
        return '<ol class="flow%s">%s</ol>' % (' v' if vertical else ' c%d' % cols, lis)
    if kind == 'lanes':
        steps = _pairs(body)
        actors = []
        for a, _ in steps:
            if a not in actors:
                actors.append(a)
        cells = ['<div class="a" style="grid-row:1;grid-column:%d">%s</div>' % (k + 1, inline(a)) for k, a in enumerate(actors)]
        for i, (a, t) in enumerate(steps):
            r = actors.index(a)
            cells.append('<div class="s l%d" style="grid-row:%d;grid-column:%d"><i>%d</i>%s</div>' % (r % 3, i + 2, r + 1, i + 1, inline(t)))
        return '<div class="lanes" style="grid-template-columns:repeat(%d,minmax(0,1fr))">%s</div>' % (len(actors), ''.join(cells))
    if kind == 'chat':
        # «Tú: …» / «Agente: …»: se dibuja como el chat de la plataforma del agente (Claude o Perplexity).
        # Los @@…@@ los rellena build.py con la plataforma de cada guía (icono, nombre, estilo y texto del cuadro de escritura).
        msgs = []
        for l in body:
            m = re.match(r'^([^\s:][^:]{0,24}):\s+(.*)$', l)
            if m:
                msgs.append([m.group(1), m.group(2)])
            elif l.strip() and msgs:
                msgs[-1][1] += ' ' + l.strip()
        out = ''
        for a, t in msgs:
            if a.lower() in ('tú', 'tu', 'usuario', 'yo'):
                out += '<div class="cw-m u"><div class="cw-t">%s</div></div>' % inline(t)
            else:
                out += ('<div class="cw-m a"><div class="cw-who"><img class="cw-av" src="@@REL@@assets/img/@@ICON@@" alt=""><span>@@PLAT@@</span></div>'
                        '<div class="cw-t">%s</div></div>' % inline(t))
        return ('<div class="chat @@CLS@@" role="group" aria-label="Ejemplo de conversación"><div class="cw-h"><img src="@@REL@@assets/img/@@ICON@@" alt=""><b>@@PLAT@@</b><span>@@SLUG@@</span></div>'
                '<div class="cw-b">%s</div><div class="cw-in" aria-hidden="true"><span>@@HINT@@</span><b class="cw-send"><svg viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg></b></div></div>' % out)
    if kind in ('cardstack', 'coverflow', 'comandos', 'proyectos'):                                      # componentes: los dibuja build.py (necesita las rutas de los recursos)
        return '<!--GAL:%s-->' % kind
    if kind == 'prompt':                                                                    # mensaje para pegar en una IA: tarjeta con botón «Copiar» (lo añade efectos.js)
        return ('<div class="prompt"><div class="pr-h"><span class="pr-dot" aria-hidden="true"></span>Mensaje para tu IA<em>cópialo y pégalo en el chat</em></div>'
                '<pre data-lenis-prevent><code>%s</code></pre></div>' % html.escape('\n'.join(body).strip('\n')))     # data-lenis-prevent: la rueda desplaza el cuadro, no la página
    if kind in ('bash', 'powershell', 'sh', 'shell'):                                       # comandos: bloque con etiqueta y botón «Copiar»
        etiqueta = 'PowerShell' if kind == 'powershell' else 'Terminal'
        return ('<div class="code"><div class="code-h"><span>%s</span></div><pre><code>%s</code></pre></div>'
                % (etiqueta, html.escape('\n'.join(body).strip('\n'))))
    if kind == 'paleta':
        return _paleta(body)
    if kind == 'repos':
        return _repos(body)
    if kind == 'publicar':
        return _publicar(body)
    if kind == 'stats':
        items = _pairs(body)
        n = len(items)
        cls = 'n%d' % n if n in (2, 3, 4) else ''
        if n == 4 and max(len(b) for _, b in items) > 60:
            cls += ' w'                                                         # textos largos: 2 × 2 en lugar de 4 columnas
        return '<div class="stats %s">%s</div>' % (cls, ''.join('<div><b>%s</b><span>%s</span></div>' % (html.escape(a), inline(b)) for a, b in items))
    if kind == 'cards':
        items = _pairs(body)
        n = len(items)
        cls = 'c1' if n == 1 else ('c2' if n in (2, 4) else '')                 # 2 o 4 tarjetas: 2 columnas; el resto: 3
        return '<div class="cards %s">%s</div>' % (cls, ''.join('<div><b>%s</b><span>%s</span></div>' % (inline(a), inline(b)) for a, b in items))
    # cualquier otro bloque de código (CSS, HTML, JSON, texto sin lenguaje…): el mismo aspecto de consola y botón «Copiar»
    nombres = {'css': 'CSS', 'html': 'HTML', 'js': 'JavaScript', 'javascript': 'JavaScript', 'ts': 'TypeScript', 'json': 'JSON', 'py': 'Python', 'python': 'Python',
               'yaml': 'YAML', 'yml': 'YAML', 'text': 'Texto', 'txt': 'Texto', 'sql': 'SQL', 'md': 'Markdown', 'diff': 'Diff'}
    etiqueta = nombres.get(kind, kind.upper() if kind else 'Código')
    return ('<div class="code"><div class="code-h"><span>%s</span></div><pre><code>%s</code></pre></div>'
            % (etiqueta, html.escape('\n'.join(body).strip('\n'))))


def _luminancia(hx):
    """Luminancia relativa WCAG de un color #RRGGBB."""
    c = [int(hx[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def _contraste(a, b):
    la, lb = _luminancia(a), _luminancia(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def _paleta(body):
    """Paleta de colores: una franja proporcional y una tarjeta por color (se copia el HEX al pulsar). Líneas: Nombre | #HEX | Rol."""
    segs, cards = '', ''
    for i, l in enumerate(x for x in body if x.strip()):
        nombre, hx, rol = [x.strip() for x in l.split('|', 2)]
        hx = hx.strip('`').upper()
        texto = '#FFFFFF' if _contraste(hx, '#FFFFFF') >= _contraste(hx, '#141413') else '#141413'      # texto de la muestra: el que mejor se lee sobre el color
        segs += '<i style="--c:%s;--i:%d"></i>' % (hx, i)
        cards += ('<button type="button" class="pal-c" style="--c:%s;--t:%s;--i:%d" data-hex="%s" aria-label="%s %s: copiar el color">'
                  '<span class="pal-s"><span class="pal-ct" aria-live="polite">Copiar</span></span><b>%s</b><code>%s</code><span class="pal-r">%s</span></button>'
                  % (hx, texto, i, hx, html.escape(nombre), hx, html.escape(nombre), hx, inline(rol)))
    return '<div class="pal" data-reveal><div class="pal-bar" aria-hidden="true">%s</div><div class="pal-g">%s</div></div>' % (segs, cards)


def _repos(body):
    """Dos repositorios y una carpeta: el repositorio 1 trae la carpeta del segundo VACÍA y el segundo se clona dentro de ella. Se dibuja como dos pasos
    (antes y después) con el estado de la carpeta. Líneas: repositorio 1 | etiqueta | descripción  ·  repositorio 2 | etiqueta | descripción | contenido (separado por comas)
    ·  ruta | carpeta  ·  comando."""
    ln = [l.strip() for l in body if l.strip()]
    a = [x.strip() for x in ln[0].split('|')]
    b = [x.strip() for x in ln[1].split('|')]
    ruta, carpeta = [x.strip() for x in ln[2].split('|')]
    cmd = ln[3] if len(ln) > 3 else ''
    raiz = ruta.strip('/').split('/')[-1] + '/'
    contenido = [f.strip() for f in (b[3].split(',') if len(b) > 3 else []) if f.strip()]
    e = html.escape

    def arbol(nuevo):
        lineas = ['<span class="rp-l rp-root">%s</span>' % e(raiz), '<span class="rp-l">├─ … archivos del agente</span>',
                  '<span class="rp-l rp-dir">└─ %s</span>' % e(carpeta)]
        if nuevo:
            for i, f in enumerate(contenido):
                lineas.append('<span class="rp-l rp-new" style="--i:%d">   %s %s</span>' % (i, '└─' if i == len(contenido) - 1 else '├─', e(f)))
        else:
            lineas.append('<span class="rp-l rp-hole">   └─ (vacía)</span>')
        return '<div class="rp-tree">%s</div>' % ''.join(lineas)

    return ('<figure class="repos" data-reveal>'
            '<p class="rp-path"><small>Ruta dentro del repositorio 1</small><code>%s</code></p>'
            '<div class="rp-cols">'
            '<div class="rp-a"><p class="rp-step">Paso 1 · clonar el repositorio 1</p>'
            '<div class="rp-h"><span class="rp-n">1</span><b>%s</b><i>%s</i></div><p class="rp-d">%s</p>'
            '<p class="rp-lab">Así queda la carpeta</p>%s'
            '<p class="rp-nota">La carpeta <code>%s</code> llega <b>vacía</b>: Git no trae el contenido del repositorio 2.</p></div>'
            '<div class="rp-go" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>'
            '<div class="rp-b"><p class="rp-step">Paso 2 · clonar el repositorio 2 dentro de esa carpeta</p>'
            '<div class="rp-h"><span class="rp-n">2</span><b>%s</b><i>%s</i></div><p class="rp-d">%s</p>'
            '<p class="rp-lab">Así queda la carpeta</p>%s'
            '<p class="rp-nota">Su contenido queda <b>dentro</b> de <code>%s</code>, con ese nombre exacto.</p></div>'
            '</div>'
            '<figcaption><span class="rp-cmd"><small>Comando del paso 2</small><code>%s</code></span></figcaption></figure>'
            % (e(ruta.strip('/')), e(a[0]), e(a[1]), inline(a[2]), arbol(False), e(carpeta),
               e(b[0]), e(b[1]), inline(b[2]), arbol(True), e(carpeta), e(cmd)))


def _publicar(body):
    """Línea de tiempo animada (los puntos se encienden en orden mientras avanza la barra). Líneas: paso | detalle, y una última «≈ tiempo»."""
    tiempo, items = '≈ 2 min', []
    for l in body:
        if not l.strip():
            continue
        if l.strip().startswith('≈'):
            tiempo = l.strip()
            continue
        x, _, y = l.partition('|')
        items.append((x.strip(), y.strip()))
    n = len(items)
    lis = ''.join('<li style="--i:%d"><span class="pub-dot">%d</span><b>%s</b><span>%s</span></li>' % (i, i + 1, inline(x), inline(y)) for i, (x, y) in enumerate(items))
    return ('<figure class="pub" data-reveal style="--n:%d;--k:%d"><ol>%s<li class="pub-run" aria-hidden="true"><span class="pub-time">%s</span></li></ol>'
            '<figcaption><span>Animación ilustrativa de los pasos; el tiempo real es de aproximadamente %s.</span><button type="button" class="rp-replay">Ver otra vez</button></figcaption></figure>'
            % (n, max(1, n - 1), lis, html.escape(tiempo), html.escape(tiempo.lstrip('≈ '))))


def _switch(sid, paneles, variante=''):
    """Selector entre paneles (pestañas con un «interruptor» deslizante). Sin JavaScript y al imprimir se ven todos los paneles, cada uno con su título.
    variante: '' (dos o tres opciones a todo el ancho), 'chips' (fila de opciones) o 'menu' (desplegable: un botón con la opción elegida y una lista animada; cada opción puede llevar subtítulo: «Nombre // subtítulo»).
    El contenido de un panel es una lista de líneas de Markdown o, si es un texto, HTML ya hecho."""
    variante = 'chips' if variante is True else (variante or '')
    bar, cuerpo = '', ''
    for i, (clave, titulo, icono, lineas) in enumerate(paneles):
        on = i == 0
        nombre, _, sub = titulo.partition(' // ')
        etiqueta = ('<span class="sw-l"><b>%s</b><small>%s</small></span>' % (inline(nombre), inline(sub))) if sub else '<span>%s</span>' % inline(nombre)
        bar += ('<button type="button" role="tab" id="%s-tab-%s" aria-controls="%s-%s" aria-selected="%s"%s>%s%s</button>'
                % (sid, clave, sid, clave, 'true' if on else 'false', '' if on else ' tabindex="-1"', ICONOS_SW.get(icono, ''), etiqueta))
        cuerpo += ('<div class="sw-panel%s" role="tabpanel" id="%s-%s" aria-labelledby="%s-tab-%s"><p class="sw-title">%s</p>%s</div>'
                   % (' on' if on else '', sid, clave, sid, clave, inline(nombre), lineas if isinstance(lineas, str) else blocks(lineas)))
    rotulo = html.escape(' / '.join(re.sub(r'<[^>]+>', '', inline(t.partition(' // ')[0])) for _, t, _, _ in paneles))
    barra = '<div class="sw-bar" role="tablist"%s aria-label="%s">%s<span class="sw-thumb" aria-hidden="true"></span></div>' % (' data-lenis-prevent' if variante == 'menu' else '', rotulo, bar)
    if variante == 'menu':                                   # el botón y la lista los activa efectos.js; sin JavaScript se ven todos los paneles
        barra = ('<div class="sw-menu"><button type="button" class="sw-trig" aria-haspopup="listbox" aria-expanded="false" aria-label="%s"><span class="sw-cur"></span>'
                 '<svg class="sw-chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></button>%s</div>' % (rotulo, barra))
    return ('<div class="sw%s" data-sw="%s"%s>%s%s</div>' % (' ' + variante if variante else '', sid, ' data-reveal' if variante == 'menu' else '', barra, cuerpo))


# ---------------------------------------------------------------- listas
LI =re.compile(r'^(\s*)([-*]|\d+\.)\s+(.*)$')


def parse_list(lines, i):
    m = LI.match(lines[i])
    base = len(m.group(1))
    tag = 'ol' if m.group(2)[0].isdigit() else 'ul'
    items = []
    while i < len(lines):
        m = LI.match(lines[i])
        if not m or len(m.group(1)) != base:
            break
        text = m.group(3)
        i += 1
        sub = ''
        while i < len(lines):
            l = lines[i]
            if not l.strip():
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and LI.match(lines[j]) and len(LI.match(lines[j]).group(1)) >= base:
                    i = j
                    continue
                break
            m2 = LI.match(l)
            if m2 and len(m2.group(1)) > base:
                s, i = parse_list(lines, i)
                sub += s
                continue
            if m2:
                break
            if l.startswith(' ' * (base + 2)):
                text += ' ' + l.strip()
                i += 1
                continue
            break
        items.append('<li>%s%s</li>' % (inline(text), sub))
    return '<%s>%s</%s>' % (tag, ''.join(items), tag), i


LABELS = {'nota': 'Nota', 'importante': 'Importante', 'tip': 'Consejo', 'cuidado': 'Cuidado'}


def is_block_start(lines, i):
    l = lines[i]
    return (l.startswith('```') or l.startswith('#') or l.startswith('>') or l.startswith(':::') or LI.match(l) or l.startswith('<!--')
            or (l.lstrip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|?[\s:\-|]+\|?\s*$', lines[i + 1])))


def blocks(lines, toc=None):
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = re.match(r'^:::\s*switch\s+([\w-]+)(?:\s+(chips))?\s*$', line)                         # «::: switch id» · «::: tab clave | Título | icono» · «:::»
        if m:
            j, paneles = i + 1, []
            while j < len(lines) and lines[j].strip() != ':::':
                t = re.match(r'^:::\s*tab\s+([\w-]+)\s*\|\s*([^|]+?)\s*(?:\|\s*(\w+)\s*)?$', lines[j])
                if t:
                    paneles.append([t.group(1), t.group(2), t.group(3) or '', []])
                elif paneles:
                    paneles[-1][3].append(lines[j])
                j += 1
            out.append(_switch(m.group(1), [tuple(p) for p in paneles], m.group(2) == 'chips'))
            i = j + 1
            continue
        m = re.match(r'^```(\w*)\s*$', line)
        if m:
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            out.append(fence(m.group(1), lines[i + 1:j]))
            i = j + 1
            continue
        if line.startswith('<!--'):
            if 'salto' in line:
                out.append('<div style="break-after:page"></div>')
            i += 1
            continue
        m = re.match(r'^(#{2,4})\s+(.*)$', line)
        if m:
            lvl, text = len(m.group(1)), m.group(2).strip()
            sid = slug(re.sub(r'[`*]', '', text))
            if lvl == 2 and toc is not None:
                toc.append((sid, re.sub(r'[`*]', '', text)))
            out.append('<h%d id="%s">%s</h%d>' % (lvl, sid, inline(text), lvl))
            i += 1
            continue
        if line.lstrip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|?[\s:\-|]+\|?\s*$', lines[i + 1]):
            def cells(l):
                l = l.strip().strip('|')
                return [c.strip() for c in re.split(r'(?<!\\)\|', l)]
            head = cells(line)
            j = i + 2
            rows = []
            while j < len(lines) and lines[j].lstrip().startswith('|'):
                rows.append(cells(lines[j]))
                j += 1
            th = ''.join('<th>%s</th>' % inline(c) for c in head)
            tb = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c.replace('\\|', '|')) for c in r) for r in rows)
            out.append('<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tb))
            i = j
            continue
        if line.startswith('>'):
            j = i
            q = []
            while j < len(lines) and lines[j].startswith('>'):
                q.append(re.sub(r'^>\s?', '', lines[j]))
                j += 1
            kind, title = 'nota', None
            m = re.match(r'^\[!(\w+)\]\s*(.*)$', q[0])
            if m:
                kind, title = m.group(1).lower(), m.group(2).strip() or None
                q = q[1:]
            label = title or LABELS.get(kind, 'Nota')
            inner = blocks(q)
            out.append('<div class="callout %s">%s%s</div>' % (kind, ('<span class="t">%s</span>' % html.escape(label)) if (m or title) else '', inner))
            i = j
            continue
        if LI.match(line):
            s, i = parse_list(lines, i)
            out.append(s)
            continue
        j = i
        para = []
        while j < len(lines) and lines[j].strip() and not (j > i and is_block_start(lines, j)):
            para.append(lines[j].strip())
            j += 1
        out.append('<p>%s</p>' % inline(' '.join(para)))
        i = j
    return '\n'.join(out)


def convert(text):
    meta, body = frontmatter(text)
    toc = []
    h = blocks(body.splitlines(), toc)
    words = len(re.sub(r'<[^>]+>', ' ', h).split())
    return meta, h, toc, words
