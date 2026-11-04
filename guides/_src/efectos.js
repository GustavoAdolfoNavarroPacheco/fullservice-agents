/* efectos.js — componentes y animaciones de texto de las guías (JavaScript puro, sin dependencias).

   Inspirados en los componentes de 21st.dev (reescritos aquí: el sitio es HTML estático, sin React ni framer-motion):
     · Letter Swap  (danielpetho)  cada letra sale hacia arriba y entra su copia desde abajo al pasar el cursor      → nav, pestañas, botones, filas del índice
     · Wave Text    (kokonutd)     las letras suben en ola al cargar y al pasar el cursor por el título               → título del banner
     · Card Stack   (ruixen.ui)    pila de portadas en 3D: se abre en abanico al pasar el cursor, arrastre, auto-avance
     · Coverflow    (ruixen.ui)    carrusel de logos tipo coverflow: el central de frente, los laterales girados

   Los carruseles ponen en cada tarjeta --o (posición respecto a la activa) y --s (signo); el CSS hace el resto.
   Con «reducir movimiento» no hay auto-avance ni ola, y los cambios son instantáneos. */
(function () {
  'use strict';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------------- Letter Swap */
  function partir(el, anfitrion) {
    var texto = el.textContent;
    if (!texto.trim() || el.getAttribute('data-ls-ok')) return;
    var enlace = el.closest('a,button');
    if (enlace && !enlace.hasAttribute('aria-label')) enlace.setAttribute('aria-label', (enlace.textContent || '').replace(/\s+/g, ' ').trim());
    el.setAttribute('data-ls-ok', '1');
    anfitrion.setAttribute('data-ls', '');
    var frag = document.createDocumentFragment(), i = 0;
    texto.split(/(\s+)/).forEach(function (parte) {
      if (!parte) return;
      if (/^\s+$/.test(parte)) { frag.appendChild(document.createTextNode(' ')); return; }
      var palabra = document.createElement('span');
      palabra.className = 'ls-wd';
      palabra.setAttribute('aria-hidden', 'true');
      Array.from(parte).forEach(function (ch) {
        var caja = document.createElement('span'), c = document.createElement('span');
        caja.className = 'ls-o';
        c.className = 'ls-c';
        c.textContent = ch;
        c.setAttribute('data-c', ch);
        c.style.setProperty('--i', i++);
        caja.appendChild(c);
        palabra.appendChild(caja);
      });
      frag.appendChild(palabra);
    });
    el.textContent = '';
    el.appendChild(frag);
  }

  /* anfitrión (lo que recibe el cursor) → elemento con el texto; null = los nodos de texto directos del anfitrión */
  var SWAP = [
    ['.top nav > a:not(.gh)', null], ['.brand', 'span'], ['.gh', '.gh-t'],
    ['.tabs [role="tab"]', null], ['.ag', '.ag-link'], ['.more .btn', null]
  ];
  function letterSwap() {
    SWAP.forEach(function (par) {
      [].forEach.call(document.querySelectorAll(par[0]), function (host) {
        if (par[1]) {
          var t = host.querySelector(par[1]);
          if (t) partir(t, host);
          return;
        }
        [].slice.call(host.childNodes).forEach(function (n) {
          if (n.nodeType === 3 && n.nodeValue.trim()) {
            var s = document.createElement('span');
            s.className = 'ls-t';
            s.textContent = n.nodeValue.trim();
            host.replaceChild(s, n);
            partir(s, host);
          }
        });
      });
    });
  }

  /* ---------------------------------------------------------------- Wave Text */
  function wave(el) {
    var texto = el.textContent.trim(), i = 0;
    el.setAttribute('aria-label', texto);
    el.textContent = '';
    var palabra = document.createElement('span');
    palabra.className = 'ls-wd';
    palabra.setAttribute('aria-hidden', 'true');
    Array.from(texto).forEach(function (ch) {
      var s = document.createElement('span');
      s.className = 'wv';
      s.textContent = ch;
      s.style.setProperty('--i', i++);
      palabra.appendChild(s);
    });
    el.appendChild(palabra);
    if (reduce) return;
    var total = (i - 1) * 45 + 1000, ocupado = false;
    function ola(clase, ms) {                                   // la ola no se interrumpe: hasta que termina no se repite
      if (ocupado) return;
      ocupado = true;
      el.classList.add(clase);
      setTimeout(function () { el.classList.remove(clase); ocupado = false; }, ms);
    }
    ola('wv-in', (i - 1) * 38 + 900);
    el.addEventListener('pointerenter', function () { ola('wv-on', total); });
  }

  /* ---------------------------------------------------------------- carruseles (Card Stack y Coverflow) */
  var cargadores = [];
  function cargarTodo() { cargadores.forEach(function (f) { f(); }); }
  window.cargarImagenes = cargarTodo;               // build.py la llama antes de generar el PDF
  window.addEventListener('beforeprint', cargarTodo);

  function carrusel(raiz) {
    var escena = raiz.querySelector('.cx-stage'), tarjetas = [].slice.call(escena.querySelectorAll('.cx-card'));
    var n = tarjetas.length, act = 0, visibles = parseInt(raiz.getAttribute('data-visibles') || '3', 10);
    var ritmo = parseInt(raiz.getAttribute('data-ritmo') || '0', 10);   // ms entre avances; 0 = sin auto-avance
    var cap = raiz.querySelector('.cx-cap'), cuenta = raiz.querySelector('.cx-n');
    var prev = raiz.querySelector('.cx-prev'), sig = raiz.querySelector('.cx-next');
    if (n < 2) return;

    /* imágenes bajo demanda: nada se descarga hasta que el carrusel está cerca de la pantalla; entonces primero la activa y sus vecinas, y el resto a medida que se avanza */
    var cerca = !('IntersectionObserver' in window);
    function cargar(i) {
      var im = tarjetas[((i % n) + n) % n].querySelector('img[data-src]');
      if (!im) return;
      im.addEventListener('load', function () { im.classList.add('ok'); }, { once: true });
      im.src = im.getAttribute('data-src');
      im.removeAttribute('data-src');
    }
    function precargar() {
      if (!cerca) return;
      cargar(act);
      for (var k = 1; k <= visibles + 1; k++) { cargar(act + k); cargar(act - k); }
    }
    cargadores.push(function () { tarjetas.forEach(function (_, i) { cargar(i); }); });   // para imprimir / PDF: todas
    if (!cerca) new IntersectionObserver(function (es, ob) { if (es[0].isIntersecting) { cerca = true; precargar(); ob.disconnect(); } }, { rootMargin: '600px 0px' }).observe(raiz);

    function pintar() {
      tarjetas.forEach(function (c, i) {
        var o = i - act;
        if (o > n / 2) o -= n;
        if (o < -n / 2) o += n;
        c.style.setProperty('--o', o);
        c.style.setProperty('--a', Math.abs(o));
        c.style.setProperty('--s', o === 0 ? 0 : (o > 0 ? 1 : -1));
        c.setAttribute('data-pos', o === 0 ? '0' : 'x');
        if (Math.abs(o) > visibles) c.setAttribute('data-h', ''); else c.removeAttribute('data-h');
        c.setAttribute('aria-hidden', o === 0 ? 'false' : 'true');
      });
      var c = tarjetas[act];
      if (cap) { cap.querySelector('b').textContent = c.getAttribute('data-c') || ''; var s = cap.querySelector('span'); if (s) s.textContent = c.getAttribute('data-p') || ''; }
      if (cuenta) cuenta.textContent = ('0' + (act + 1)).slice(-2) + ' / ' + ('0' + n).slice(-2);
      precargar();
    }
    function ir(i) { act = ((i % n) + n) % n; pintar(); }

    prev.addEventListener('click', function () { ir(act - 1); });
    sig.addEventListener('click', function () { ir(act + 1); });
    raiz.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { ir(act - 1); e.preventDefault(); }
      else if (e.key === 'ArrowRight') { ir(act + 1); e.preventDefault(); }
      else if (e.key === 'Home') { ir(0); e.preventDefault(); }
      else if (e.key === 'End') { ir(n - 1); e.preventDefault(); }
    });

    /* arrastre: la tarjeta activa sigue al puntero (--dx) y, al soltar, pasa a la siguiente o a la anterior */
    var ini = null, movido = false;
    escena.addEventListener('pointerdown', function (e) {
      if (e.button !== 0 || (e.target.closest && e.target.closest('button'))) return;
      ini = { x: e.clientX, id: e.pointerId }; movido = false;
    });
    escena.addEventListener('pointermove', function (e) {
      if (!ini) return;
      var dx = e.clientX - ini.x;
      if (!movido && Math.abs(dx) > 6) { movido = true; escena.classList.add('drag'); try { escena.setPointerCapture(ini.id); } catch (_) {} }
      if (movido) { raiz.style.setProperty('--dx', (dx * 0.7) + 'px'); raiz.style.setProperty('--r', (dx * 0.7 / 60).toFixed(2)); }
    });
    function soltar(e) {
      if (!ini) return;
      var dx = e.clientX - ini.x;
      ini = null;
      escena.classList.remove('drag');
      raiz.style.setProperty('--dx', '0px'); raiz.style.setProperty('--r', '0');
      if (movido) { if (dx < -45) ir(act + 1); else if (dx > 45) ir(act - 1); }
    }
    escena.addEventListener('pointerup', soltar);
    escena.addEventListener('pointercancel', soltar);
    escena.addEventListener('click', function (e) {                // tocar una tarjeta lateral la trae al frente
      if (movido) { movido = false; e.preventDefault(); return; }
      var c = e.target.closest && e.target.closest('.cx-card');
      if (c) { var i = tarjetas.indexOf(c); if (i !== act) ir(i); }
    });

    /* auto-avance: solo con la sección a la vista, y se detiene con el cursor o el foco encima */
    var timer = null, enVista = false, quieto = false;
    function reloj() {
      var debe = ritmo > 0 && !reduce && enVista && !quieto;
      if (debe && !timer) timer = setInterval(function () { ir(act + 1); }, ritmo);
      if (!debe && timer) { clearInterval(timer); timer = null; }
    }
    if (ritmo > 0 && !reduce) {
      raiz.addEventListener('pointerenter', function () { quieto = true; reloj(); });
      raiz.addEventListener('pointerleave', function () { quieto = false; reloj(); });
      raiz.addEventListener('focusin', function () { quieto = true; reloj(); });
      raiz.addEventListener('focusout', function () { quieto = false; reloj(); });
      if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { enVista = es[0].isIntersecting; reloj(); }, { threshold: 0.3 }).observe(raiz);
    }
    raiz.classList.add('listo');
    pintar();
  }

  function iniciar() {
    letterSwap();
    [].forEach.call(document.querySelectorAll('[data-wave]'), wave);
    [].forEach.call(document.querySelectorAll('.cx'), carrusel);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
