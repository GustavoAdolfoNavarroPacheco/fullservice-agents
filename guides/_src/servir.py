# -*- coding: utf-8 -*-
"""servir.py — sitio local con recarga en vivo.

Uso:   python -X utf8 guides/_src/servir.py        (puerto 4173; otro: PORT=5000 python ...)
Qué hace: sirve guides/ y vigila contenido/**.md, estilo.css, suave.js, efectos.js, md.py y build.py. Al cambiar uno, reconstruye el HTML
(sin PDF, para no tocar los PDF versionados) y el navegador se recarga solo, conservando la posición de lectura.
Si el Markdown tiene un error, la página muestra el aviso en lugar de romperse.
"""
import http.server
import importlib
import io
import json
import os
import pathlib
import socketserver
import sys
import threading
import time

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding='utf-8')
    except Exception:
        pass
import build  # noqa: E402

PORT = int(os.environ.get('PORT', '4173'))
state = {'v': 1, 'error': ''}
WATCH = [SRC / 'contenido', SRC / 'estilo.css', SRC / 'suave.js', SRC / 'efectos.js', SRC / 'md.py', SRC / 'build.py', SRC.parents[1] / 'resources' / 'comandos' / 'comandos.py']

INJECT = b"""<script>(function(){var v=null,msg=null;
try{var y=sessionStorage.getItem('__y');if(y){sessionStorage.removeItem('__y');addEventListener('load',function(){setTimeout(function(){scrollTo(0,+y)},60)})}}catch(e){}
function aviso(t){if(!msg){msg=document.createElement('div');msg.style.cssText='position:fixed;left:16px;right:16px;bottom:16px;z-index:99;padding:14px 18px;border-radius:12px;background:#f8e8ee;color:#7a2f4c;font:14px/1.5 Inter,sans-serif;box-shadow:0 6px 24px rgba(0,0,0,.15)';document.body.appendChild(msg)}msg.textContent=t?'Error al reconstruir: '+t:'';msg.style.display=t?'block':'none'}
setInterval(function(){fetch('/__v',{cache:'no-store'}).then(function(r){return r.json()}).then(function(d){aviso(d.error);if(v===null)v=d.v;else if(d.v!==v){try{sessionStorage.setItem('__y',String(scrollY))}catch(e){}location.reload()}}).catch(function(){})},700)})();</script>"""


def snapshot():
    out = {}
    for w in WATCH:
        files = [w] if w.is_file() else [f for f in w.rglob('*') if f.is_file()]
        for f in files:
            try:
                out[str(f)] = f.stat().st_mtime_ns
            except OSError:
                pass
    return out


def rebuild():
    try:
        importlib.reload(build.md)
        importlib.reload(build)
        build.build(None, False)
        state['error'] = ''
        print('  ✓ reconstruido (v%d)' % (state['v'] + 1), flush=True)
    except BaseException as e:  # incluye SystemExit de las comprobaciones del generador
        state['error'] = str(e) or e.__class__.__name__
        print('  ✗ error al reconstruir:', state['error'], flush=True)
    state['v'] += 1


def vigilar():
    last = snapshot()
    while True:
        time.sleep(0.5)
        now = snapshot()
        if now != last:
            last = now
            time.sleep(0.2)          # deja que termine de guardarse
            rebuild()


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT), **k)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def send_head(self):
        if self.path.split('?')[0] == '/__v':
            data = json.dumps(state).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            return io.BytesIO(data)
        # Mismas direcciones limpias que en Vercel (vercel.json): / y /index.html → /inicio;
        # las páginas se piden sin «.html» (con «.html» se redirige a la limpia).
        raw, _, qs = self.path.partition('?')
        if raw in ('/', '/index', '/index.html'):
            return self.redirigir('/inicio')
        if raw.endswith('.html'):
            return self.redirigir(raw[:-5] + ('?' + qs if qs else ''))
        if '.' not in raw.rsplit('/', 1)[-1] and (ROOT / (raw.lstrip('/') + '.html')).exists():
            self.path = raw + '.html'
        path = pathlib.Path(self.translate_path(self.path))
        if path.is_dir():
            path = path / 'index.html'
        if path.suffix == '.html' and path.exists():
            data = path.read_bytes().replace(b'</body>', INJECT + b'</body>')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            return io.BytesIO(data)
        return super().send_head()

    def redirigir(self, destino):
        self.send_response(307)
        self.send_header('Location', destino)
        self.send_header('Content-Length', '0')
        self.end_headers()
        return None

    def log_message(self, fmt, *args):
        if args and str(args[1]).startswith(('4', '5')):
            super().log_message(fmt, *args)


class Servidor(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == '__main__':
    build.build(None, False)                                   # parte siempre de un HTML al día
    threading.Thread(target=vigilar, daemon=True).start()
    with Servidor(('127.0.0.1', PORT), Handler) as srv:
        print('Guías en http://localhost:%d  ·  vigilando contenido/, estilo.css y suave.js (Ctrl+C para salir)' % PORT, flush=True)
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            pass
