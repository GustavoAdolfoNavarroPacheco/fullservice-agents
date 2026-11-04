# -*- coding: utf-8 -*-
"""md.py — convertidor mínimo de Markdown a HTML para las guías (sin dependencias).

Soporta: portada en frontmatter, ## ### ####, párrafos, listas anidadas, tablas, citas/avisos [!nota|importante|tip|cuidado],
código con ``` y bloques propios: tree · flow · lanes · chat · stats · cards.
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
        msgs = []
        for l in body:
            m = re.match(r'^([^\s:][^:]{0,24}):\s+(.*)$', l)
            if m:
                msgs.append([m.group(1), m.group(2)])
            elif l.strip() and msgs:
                msgs[-1][1] += ' ' + l.strip()
        return '<div class="chat">%s</div>' % ''.join(
            '<div class="%s"><b>%s</b>%s</div>' % ('u' if a.lower() in ('tú', 'tu', 'usuario', 'yo') else 'g', html.escape(a), inline(t)) for a, t in msgs)
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
    return '<pre><code>%s</code></pre>' % html.escape('\n'.join(body))


# ---------------------------------------------------------------- listas
LI = re.compile(r'^(\s*)([-*]|\d+\.)\s+(.*)$')


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
    return (l.startswith('```') or l.startswith('#') or l.startswith('>') or LI.match(l) or l.startswith('<!--')
            or (l.lstrip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|?[\s:\-|]+\|?\s*$', lines[i + 1])))


def blocks(lines, toc=None):
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
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
