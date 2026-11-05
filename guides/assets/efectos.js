/* efectos.js — componentes y animaciones de texto de las guías (JavaScript puro, sin dependencias).

   Inspirados en los componentes de 21st.dev (reescritos aquí: el sitio es HTML estático, sin React ni framer-motion):
     · Letter Swap  (danielpetho)  cada letra sale hacia arriba y entra su copia desde abajo al pasar el cursor      → nav, pestañas, botones, filas del índice
     · Wave Text    (kokonutd)     las letras suben en ola al cargar y al pasar el cursor por el título               → título del banner
     · Card Stack   (ruixen.ui)    pila de portadas en 3D: se abre en abanico al pasar el cursor, arrastre, auto-avance
     · Coverflow    (ruixen.ui)    carrusel de logos tipo coverflow: el central de frente, los laterales girados
   Y los de la pestaña «Inicio»: botón «Copiar» en mensajes y comandos, selector (switch) con pastilla deslizante, revelado al
   hacer scroll (repositorios, línea de tiempo, ubicación de archivos).

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

  /* ---------------------------------------------------------------- Inicio: botón «Copiar», selector (switch), revelado y pestañas de la guía */
  var ICO_COPIAR = '<svg class="cp" viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V6a2 2 0 0 1 2-2h9"/></svg>' +
                   '<svg class="ck" viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>';
  function copiarTexto(texto) {
    function respaldo() {                                                        // páginas abiertas desde archivo, sin HTTPS o con el portapapeles bloqueado
      return new Promise(function (ok, mal) {
        var t = document.createElement('textarea');
        t.value = texto; t.setAttribute('readonly', ''); t.style.cssText = 'position:fixed;top:0;left:0;opacity:0';
        document.body.appendChild(t); t.select();
        try { document.execCommand('copy') ? ok() : mal(); } catch (e) { mal(e); }
        document.body.removeChild(t);
      });
    }
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(texto).catch(respaldo);
    return respaldo();
  }
  function botonCopiar(caja) {
    var cab = caja.querySelector('.pr-h, .code-h'), cod = caja.querySelector('pre code');
    if (!cab || !cod || cab.querySelector('.copy')) return;
    var b = document.createElement('button'), et = document.createElement('span'), t = null;
    b.type = 'button'; b.className = 'copy';
    b.innerHTML = ICO_COPIAR; et.textContent = 'Copiar'; et.setAttribute('aria-live', 'polite'); b.appendChild(et);
    b.addEventListener('click', function () {
      copiarTexto(cod.textContent.replace(/\s+$/, '')).then(function () {
        b.classList.add('ok'); et.textContent = 'Copiado';
      }, function () {
        var r = document.createRange(); r.selectNodeContents(cod); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
        et.textContent = 'Selecciona y copia con Ctrl+C';
      });
      clearTimeout(t);
      t = setTimeout(function () { b.classList.remove('ok'); et.textContent = 'Copiar'; }, 2200);
    });
    cab.appendChild(b);
  }

  /* desplazamiento suave hasta un elemento (Lenis si está activo; con «reducir movimiento», directo) */
  window.irA = function (el) {
    if (window.lenis) { if (window.lenis.resize) window.lenis.resize(); window.lenis.scrollTo(el); }      // resize: si cambió el alto de la página (otra pestaña), Lenis no recorta el destino
    else el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
  };

  /* cifras que cuentan hasta su valor ([data-n]) dentro de un panel que se acaba de mostrar */
  function contar(raiz) {
    [].forEach.call(raiz.querySelectorAll('[data-n]'), function (el) {
      var fin = parseInt(el.getAttribute('data-n'), 10) || 0;
      if (reduce || fin < 1) { el.textContent = fin; return; }
      var t0 = null;
      (function paso(t) {
        if (t0 === null) t0 = t;
        var k = Math.min(1, (t - t0) / 700);
        el.textContent = Math.round(fin * (1 - Math.pow(1 - k, 3)));
        if (k < 1) requestAnimationFrame(paso);
      })(performance.now());
    });
  }

  /* paleta: pulsar un color copia su HEX; al pasar sobre una tarjeta se ensancha su tramo de la franja y el brillo sigue al cursor */
  function paleta(raiz) {
    var cards = [].slice.call(raiz.querySelectorAll('.pal-c')), segs = [].slice.call(raiz.querySelectorAll('.pal-bar i'));
    cards.forEach(function (c, i) {
      var et = c.querySelector('.pal-ct'), t = null;
      function on() { if (segs[i]) segs[i].classList.add('hot'); }
      function off() { if (segs[i]) segs[i].classList.remove('hot'); }
      c.addEventListener('mouseenter', on); c.addEventListener('mouseleave', off); c.addEventListener('focus', on); c.addEventListener('blur', off);
      c.addEventListener('mousemove', function (e) {
        var r = c.querySelector('.pal-s').getBoundingClientRect();
        c.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%'); c.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
      });
      c.addEventListener('click', function () {
        copiarTexto(c.getAttribute('data-hex')).then(function () {
          c.classList.add('ok'); et.textContent = 'Copiado ' + c.getAttribute('data-hex');
          clearTimeout(t); t = setTimeout(function () { c.classList.remove('ok'); et.textContent = 'Copiar'; }, 1800);
        }, function () { et.textContent = c.getAttribute('data-hex'); });
      });
    });
  }

  function conmutador(raiz) {
    var tabs = [].slice.call(raiz.querySelectorAll('.sw-bar [role="tab"]')), thumb = raiz.querySelector('.sw-thumb'), actual = -1;
    var paneles = tabs.map(function (t) { return document.getElementById(t.getAttribute('aria-controls')); });
    var clave = 'sw:' + (raiz.getAttribute('data-sw') || '');
    var menu = raiz.classList.contains('menu'), trig = raiz.querySelector('.sw-trig'), rotulo = raiz.querySelector('.sw-cur'), lista = raiz.querySelector('.sw-bar');
    function mover() {
      var t = tabs[actual]; if (!t) return;
      thumb.style.setProperty('--x', t.offsetLeft + 'px'); thumb.style.setProperty('--w', t.offsetWidth + 'px');
      thumb.style.setProperty('--y', t.offsetTop + 'px'); thumb.style.setProperty('--h', t.offsetHeight + 'px');        // variante «cards»: la pastilla también sube y baja
    }
    function ir(i, foco, anim) {
      var primera = actual < 0; actual = i;
      tabs.forEach(function (t, j) {
        var on = j === i;
        t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
        paneles[j].classList.toggle('on', on);
        paneles[j].classList.remove('anim');
        if (on && anim && !reduce) { void paneles[j].offsetWidth; paneles[j].classList.add('anim'); }
      });
      if (primera) { thumb.style.transition = 'none'; mover(); void thumb.offsetWidth; thumb.style.transition = ''; } else mover();
      if (foco) tabs[i].focus();
      if (menu && rotulo) rotulo.innerHTML = tabs[i].innerHTML;                              // el botón del desplegable muestra la opción elegida
      try { sessionStorage.setItem(clave, paneles[i].id); } catch (e) {}
      if (!primera) contar(paneles[i]);
    }
    function porId(id) { for (var i = 0; i < paneles.length; i++) if (paneles[i].id === id) return i; return -1; }
    /* desplegable: botón + lista (listbox). Abre con clic o flechas; Esc, clic fuera o elegir una opción lo cierra y devuelve el foco al botón */
    function abierto() { return raiz.classList.contains('abierto'); }
    function cerrar(foco) { raiz.classList.remove('abierto'); if (trig) { trig.setAttribute('aria-expanded', 'false'); if (foco) trig.focus(); } }
    function abrir() {
      raiz.classList.add('abierto'); trig.setAttribute('aria-expanded', 'true');
      var sel = tabs[actual]; if (sel) setTimeout(function () { sel.focus({ preventScroll: true }); if (sel.scrollIntoView) sel.scrollIntoView({ block: 'nearest' }); }, 30);
    }
    if (menu && trig) {
      lista.setAttribute('role', 'listbox');
      tabs.forEach(function (t, j) { t.setAttribute('role', 'option'); t.removeAttribute('aria-controls'); t.style.setProperty('--o', j); });
      trig.addEventListener('click', function () { if (abierto()) cerrar(false); else abrir(); });
      trig.addEventListener('keydown', function (e) { if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); if (!abierto()) abrir(); } });
      document.addEventListener('click', function (e) { if (abierto() && !raiz.contains(e.target)) cerrar(false); });
      lista.addEventListener('keydown', function (e) {
        var k = e.key, ahora = tabs.indexOf(document.activeElement), n = -1;
        if (k === 'Escape') { e.preventDefault(); cerrar(true); return; }
        if (k === 'Tab') { cerrar(false); return; }
        if (k === 'ArrowDown') n = Math.min(tabs.length - 1, ahora + 1); else if (k === 'ArrowUp') n = Math.max(0, ahora - 1);
        else if (k === 'Home') n = 0; else if (k === 'End') n = tabs.length - 1;
        else if (k.length === 1 && /\S/.test(k)) {                                                    // escribir una letra salta a la opción que empieza así
          for (var d = 1; d <= tabs.length; d++) { var c = (ahora + d) % tabs.length; if (tabs[c].textContent.trim().toLowerCase().indexOf(k.toLowerCase()) === 0) { n = c; break; } }
        }
        if (n >= 0) { e.preventDefault(); tabs[n].focus(); }
      });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { ir(i, false, true); if (menu) cerrar(true); });
      t.addEventListener('keydown', function (e) {
        if (menu) return;
        var k = e.key, n = k === 'ArrowRight' ? (i + 1) % tabs.length : k === 'ArrowLeft' ? (i + tabs.length - 1) % tabs.length : k === 'Home' ? 0 : k === 'End' ? tabs.length - 1 : -1;
        if (n >= 0) { e.preventDefault(); ir(n, true, true); }
      });
    });
    var inicial = 0, guardado = null;
    try { guardado = sessionStorage.getItem(clave); } catch (e) {}
    if (guardado && porId(guardado) >= 0) inicial = porId(guardado);
    var desdeHash = porId(location.hash.slice(1));
    if (desdeHash >= 0) inicial = desdeHash;
    ir(inicial, false, false);
    if (desdeHash >= 0) setTimeout(function () { raiz.scrollIntoView(); }, 60);        // el ancla apuntaba a un panel oculto: ahora que se muestra, vamos a él
    window.addEventListener('hashchange', function () { var i = porId(location.hash.slice(1)); if (i >= 0) { ir(i, false, true); window.irA(raiz); } });
    window.addEventListener('resize', mover);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(mover);
    var barra = raiz.querySelector('.sw-bar');
    if (barra && window.ResizeObserver) new ResizeObserver(mover).observe(barra);          // si el selector estaba oculto (otra pestaña), se coloca al mostrarse
  }

  /* repositorios, línea de tiempo y ubicación de archivos: arrancan cuando se ven; «Ver otra vez» los repite */
  function revelar(el) {
    function encender() { el.classList.add('on'); contar(el.querySelector('.sw-panel.on') || el); }
    [].forEach.call(el.querySelectorAll('.rp-replay'), function (b) {
      b.addEventListener('click', function () { el.classList.remove('on'); void el.offsetWidth; setTimeout(encender, 60); });
    });
    if (reduce || !('IntersectionObserver' in window)) { encender(); return; }
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { encender(); io.disconnect(); } }, { threshold: 0.01, rootMargin: '0px 0px -12% 0px' });      // no un porcentaje alto: en el móvil la tabla de archivos es más alta que la pantalla
    io.observe(el);
  }
  window.revelarTodo = function () { [].forEach.call(document.querySelectorAll('[data-reveal]'), function (e) { e.classList.add('on'); }); };

  function iniciar() {
    letterSwap();
    [].forEach.call(document.querySelectorAll('[data-wave]'), wave);
    [].forEach.call(document.querySelectorAll('.cx'), carrusel);
    [].forEach.call(document.querySelectorAll('.prompt, .code'), botonCopiar);
    [].forEach.call(document.querySelectorAll('[data-sw]'), conmutador);
    [].forEach.call(document.querySelectorAll('.pal'), paleta);
    [].forEach.call(document.querySelectorAll('[data-reveal]'), revelar);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
