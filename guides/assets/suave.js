/* suave.js — scroll suave con Lenis para todas las páginas de las guías.
   Mismo tacto que el portal de presentaciones (duración 1,25 s, curva exponencial de frenado largo).
   - Los enlaces ancla (índice lateral, «Todas las guías»…) se deslizan a su sección, con el desfase de la barra superior (scroll-padding-top del CSS).
   - Las áreas con scroll propio llevan data-lenis-prevent (Lenis no las toca) y reciben aquí su propia inercia.
   - Se apaga con «reducir movimiento» del sistema y al imprimir. */
(function () {
  'use strict';
  if (typeof Lenis === 'undefined') return;
  var mq = function (q) { return window.matchMedia && window.matchMedia(q).matches; };
  if (mq('(prefers-reduced-motion: reduce)') || mq('print')) return;

  var lenis = new Lenis({
    duration: 1.25,
    easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
    smoothWheel: true,
    anchors: true                                    // el desfase de la barra superior lo da scroll-padding-top (CSS)
  });
  window.lenis = lenis;
  (function raf(time) { lenis.raf(time); requestAnimationFrame(raf); })(performance.now());

  /* Inercia en las áreas internas (p. ej. el índice lateral cuando es más alto que la pantalla). */
  var TAU = 95, estados = new WeakMap();
  function areaDesplazable(inicio) {
    if (!(inicio instanceof Element)) return null;
    var frontera = inicio.closest('[data-lenis-prevent]');
    if (!frontera) return null;
    for (var el = inicio; el; el = el.parentElement) {
      if (el.scrollHeight > el.clientHeight + 1 && /(auto|scroll)/.test(getComputedStyle(el).overflowY)) return el;
      if (el === frontera) break;
    }
    return null;
  }
  document.addEventListener('wheel', function (e) {
    if (e.defaultPrevented || e.ctrlKey || Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;
    var el = areaDesplazable(e.target);
    if (!el) return;
    var st = estados.get(el) || { objetivo: el.scrollTop, raf: 0 };
    estados.set(el, st);
    var max = el.scrollHeight - el.clientHeight, actual = st.raf ? st.objetivo : el.scrollTop;
    var unidad = e.deltaMode === 1 ? 40 : e.deltaMode === 2 ? el.clientHeight : 1;
    var sig = Math.min(max, Math.max(0, actual + e.deltaY * unidad));
    if (sig === actual) return;                      // en el extremo no se intercepta: sigue el encadenado normal
    e.preventDefault();
    st.objetivo = sig;
    if (st.raf) return;
    var prev = performance.now();
    (function paso(ahora) {
      var dt = Math.min(64, ahora - prev); prev = ahora;
      var falta = st.objetivo - el.scrollTop;
      if (Math.abs(falta) < 0.5 || !el.isConnected) { el.scrollTop = st.objetivo; st.raf = 0; return; }
      var avance = falta * (1 - Math.exp(-dt / TAU));
      if (Math.abs(avance) < 1) avance = (falta < 0 ? -1 : 1) * Math.min(1, Math.abs(falta));
      el.scrollTop += avance;
      st.raf = requestAnimationFrame(paso);
    })(prev);
  }, { passive: false });
})();
