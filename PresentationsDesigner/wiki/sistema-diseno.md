# Sistema de Diseño y Tokens CSS (v2 — Premium con gradientes)

Reglas de maquetación, tokens y patrones para construir decks HTML/CSS de nivel
"diseñador profesional", con **dinamismo entre láminas**, **gradientes** y **fuentes
locales**. La lámina de referencia verificada es
`presentaciones/miami-aqua-tours-ampliado/`. Ver marca en [[marca-campuslands]] y
narrativa flexible en [[plantilla-base]].

---

## 1. Fuentes locales (`@font-face`)

⚠️ **REGLA DE AUTOCONTENCIÓN (obligatoria — evita el bug de tipografías en Vercel):**
las fuentes de cada deck viven **dentro** de su propia carpeta, en
`presentaciones/<slug>/assets/fonts/`, y se referencian con ruta relativa **local**
`assets/fonts/…`. **NUNCA** usar `../../recursos/fonts/`: esa ruta sube fuera de la
carpeta del deck y, al desplegar la presentación desde su propia raíz (Vercel), los
`.ttf` dan 404 y el navegador cae a fuentes de respaldo. `recursos/fonts/` es solo la
**fuente de verdad**; al crear un deck se copian a `assets/fonts/` los pesos que se usen.

Al construir: `mkdir -p assets/fonts` y copiar desde `recursos/fonts/` los `.ttf` usados.
Bloque canónico (cargar solo los pesos que se usen):

```css
@font-face { font-family:'Playfair Display'; src:url('assets/fonts/PlayfairDisplay-Bold.ttf')       format('truetype'); font-weight:700; font-style:normal; font-display:swap; }
@font-face { font-family:'Playfair Display'; src:url('assets/fonts/PlayfairDisplay-Black.ttf')      format('truetype'); font-weight:900; font-style:normal; font-display:swap; }
@font-face { font-family:'Playfair Display'; src:url('assets/fonts/PlayfairDisplay-Italic.ttf')     format('truetype'); font-weight:400; font-style:italic; font-display:swap; }
@font-face { font-family:'Playfair Display'; src:url('assets/fonts/PlayfairDisplay-BlackItalic.ttf')format('truetype'); font-weight:900; font-style:italic; font-display:swap; }
@font-face { font-family:'DM Serif Display'; src:url('assets/fonts/DMSerifDisplay-Regular.ttf')     format('truetype'); font-weight:400; font-style:normal; font-display:swap; }
@font-face { font-family:'Montserrat';       src:url('assets/fonts/Montserrat-Medium.ttf')          format('truetype'); font-weight:500; font-style:normal; font-display:swap; }
@font-face { font-family:'Montserrat';       src:url('assets/fonts/Montserrat-SemiBold.ttf')        format('truetype'); font-weight:600; font-style:normal; font-display:swap; }
@font-face { font-family:'Montserrat';       src:url('assets/fonts/Montserrat-Bold.ttf')            format('truetype'); font-weight:700; font-style:normal; font-display:swap; }
@font-face { font-family:'Poppins';          src:url('assets/fonts/Poppins-Light.ttf')              format('truetype'); font-weight:300; font-style:normal; font-display:swap; }
@font-face { font-family:'Poppins';          src:url('assets/fonts/Poppins-Regular.ttf')            format('truetype'); font-weight:400; font-style:normal; font-display:swap; }
@font-face { font-family:'Poppins';          src:url('assets/fonts/Poppins-SemiBold.ttf')           format('truetype'); font-weight:600; font-style:normal; font-display:swap; }
```

---

## 2. Tokens (`:root`)

```css
:root{
  --bg-0:#05070F; --bg-1:#0A0E1A; --bg-2:#0D1424; --bg-deep:#0B1120; /* fondo profundo — TEMATIZABLE por cliente, ver [[temas-por-cliente]] */
  --bg-glow-a:rgba(53,208,240,.12); --bg-glow-b:rgba(139,92,246,.12);
  --text-hi:#FFFFFF; --text-mid:#C3CBDA; --text-lo:#7A8699; --text-faint:#4A5468;
  --cyan:#35D0F0; --blue:#4A7DFF; --violet:#8B5CF6; --magenta:#C05CF6; --amber:#F5A623; --lime:#A6E22E;
  --grad-brand:linear-gradient(100deg,#35D0F0 0%,#4A7DFF 42%,#8B5CF6 76%,#C05CF6 100%);
  --grad-cyan:linear-gradient(120deg,#35D0F0,#4A7DFF);
  --grad-violet:linear-gradient(120deg,#6E8BFF,#C05CF6);
  --font-display:'Playfair Display',Georgia,serif;
  --font-serif-alt:'DM Serif Display',Georgia,serif;
  --font-label:'Montserrat','Segoe UI',sans-serif;
  --font-body:'Poppins','Segoe UI',sans-serif;
  --slide-w:11in; --slide-h:6.1875in; --pad:0.72in; --radius:14px;
}
```

### Fondo con vida (usar en `.slide`, variando ángulos por lámina)
```css
background:
  radial-gradient(120% 90% at 82% 18%, var(--bg-glow-a) 0%, transparent 45%),
  radial-gradient(120% 120% at 12% 92%, var(--bg-glow-b) 0%, transparent 50%),
  linear-gradient(150deg, var(--bg-0) 0%, var(--bg-1) 55%, var(--bg-deep) 100%);
```

> **Fondo tematizable:** `.slide`, `.glow-a` y `.glow-b` usan `var(--bg-deep)` (nunca un
> color profundo hardcodeado). Cada cliente tiñe `--bg-0/1/2/-deep` + glows hacia el hue de
> su logo. Receta, contrato de tokens y catálogo de paletas en [[temas-por-cliente]].

---

## 3. Utilidades de marca (copiar tal cual)

* **Texto en gradiente — usar SVG, no `background-clip:text`** (estándar desde 2026-07-30, ver §5.2 "Solución del hairline"): `<svg><text fill="url(#grad-brand-svg)">...</text></svg>` con el `<linearGradient>` definido una vez en el `<svg>`. El viejo método CSS (`background:var(--grad-brand); -webkit-background-clip:text; ...`) queda como legado — no usar en piezas nuevas.
* **Eyebrow** — `font-family:var(--font-label); font-weight:600; font-size:9.5pt; letter-spacing:.34em; text-transform:uppercase; color:var(--cyan);`
* **Marco de brackets** — 4 `<span class="corner tl/tr/bl/br">` con `border` en 2 lados, color `rgba(74,125,255,.55)`.
* **Anillos concéntricos** — contenedor `.deco-rings` con 3–4 `<span>` circulares de `border rgba(120,150,220,.06–.20)` para profundidad.
* **Badge confidencial** — Montserrat 600 + `::before` punto ámbar con `box-shadow` glow.
* **Barra/píldora de acento** — `background:var(--grad-brand); border-radius:99px;` para separadores intencionales (no líneas planas).

El código de referencia completo vive en
`presentaciones/miami-aqua-tours-ampliado/styles.css`; clónalo como punto de partida.

---

## 4. Dinamismo: NO todas las láminas iguales

La grilla base es flexible, no una plantilla única. Alterna estos arquetipos de layout
para dar ritmo (mín. 4 tratamientos distintos por deck):

1. **Portada** — grid `auto 1fr auto`: topbar (logos) / cuerpo (título gradiente) / meta 4-col.
2. **Métricas** — números gigantes Playfair en tarjetas `--bg-2` con borde superior en gradiente.
3. **Split 2 columnas** — texto a la izq, figura/diagrama a la der (o invertido en la siguiente).
4. **Diagrama de capas / flujo** — bloques conectados, cada capa con su gradiente.
5. **Grid de módulos** — cuadrícula de tarjetas con ícono + título + detalle.
6. **Cita / statement** — una frase enorme centrada con palabra clave en gradiente (respiración total).
7. **Timeline** — fases horizontales con hitos y una línea guía en `--grad-cyan`.
8. **Tabla antes/después** — dos columnas contrastadas (rojo tenue vs verde/cian).
9. **Cierre / CTA** — asimétrico, gran gradiente, datos de contacto.

Reglas de ritmo: varía el **ángulo del glow**, cuál **gradiente** domina, y la
**posición** del bloque protagonista (izq / centro / der) entre láminas contiguas.

---

## 5. Anti-patrones (CERO TOLERANCIA)

* 🛑 **Subrayados/`hr` decorativos bajo títulos.** Jerarquiza con escala, peso, itálica y gradiente.
* 🛑 **Barras rectangulares planas** como separadores en header/footer. El header/footer flotan sobre el fondo. Si necesitas separador, usa una **píldora en gradiente**, no un bloque plano.
* 🛑 **Texto corrido centrado.** Alinear a la izquierda. El centro se reserva para el título de portada, métricas individuales o láminas tipo "statement".
* 🛑 **Desbordamiento / falta de aire.** Deja ≥30% de aire negativo. Si no cabe, **divide en más láminas** (el conteo es libre; ver [[plantilla-base]]).
* 🛑 **Espacio vacío/muerto sin usar.** Tan grave como el desbordamiento (regla añadida 2026-07-09,
  ver §5.1 **Balance de espacio**): un bloque de contenido (timeline, grid, lista) que ocupa solo una
  fracción de la altura disponible y deja el resto de la lámina en blanco es un defecto de diseño, no
  "aire". Corrige redistribuyendo el contenido (más filas/columnas, tarjetas más grandes) antes de
  entregar.
* 🛑 **Color plano donde debería haber gradiente.** Priorizar gradientes (marca).
* 🛑 **Reusar la misma paleta entre clientes.** Cada deck deriva su paleta —**fondo incluido**— del logo del cliente (ver [[temas-por-cliente]]). El cian/violeta es solo el tema *default* de Campuslands.
* 🛑 **Logos deformados o sobre caja innecesaria.** Fijar solo `height`; verificar transparencia.

### 5.1 Balance de espacio: ni vacío ni apretado (regla obligatoria, 2026-07-09)

El objetivo es que cada lámina se sienta **intencionalmente compuesta**, no que el contenido
simplemente "quepa". Dos fallas opuestas, igual de graves:

* **Vacío:** un componente (timeline, grid de tarjetas, lista) renderizado a su tamaño mínimo/por
  defecto dentro de una lámina más alta, dejando una franja de fondo sin nada debajo. Caso real:
  `presentaciones/greenmetal-fyswap/` — 6 fases en una sola fila de tarjetas pequeñas dejaban ~40%
  de la lámina vacío debajo.
* **Apretado:** elementos pegados unos a otros, sin `gap`/padding perceptible, o texto que casi toca
  el borde de su tarjeta o el footer.

**Cómo decidir, antes de dar el borrador por terminado:**
1. Mide (o estima) qué porcentaje de la altura de `.s-body` ocupa el contenido real.
2. Si sobra una franja vacía notable (más del ~15–20% de la altura sin ningún elemento), **redistribuye**:
   reparte el contenido en más filas/columnas (p. ej. 6 ítems en 1 fila → 2 filas de 3), agranda
   tarjetas/tipografía/nodos, o añade `gap`/padding generoso entre bloques — en ese orden de preferencia.
3. Si en cambio los elementos quedan pegados o el texto roza sus bordes, **agranda el espaciado**
   (`gap`, `padding`, `margin-top`) antes que reducir tamaños de fuente.
4. El punto de referencia es el **aire negativo objetivo (~25–35% de la lámina)** ya exigido en el
   anti-patrón de desbordamiento — pero repartido de forma intencional (respiración entre bloques),
   nunca como una franja residual sin diseñar al final o al costado.

### 5.2 Texto en gradiente para print — usar SVG, no `background-clip:text` (solución de fondo, 2026-07-30)

**Historial del bug:** el texto en gradiente con `background-clip:text` dibuja un
**hairline** (o, en casos peores, una caja/línea de color sólido) alrededor del texto al
exportar a PDF con Chrome headless. Se intentaron varias mitigaciones a lo largo del
tiempo — elemento `inline` en vez de `block` (portada de Miami Aqua Tours),
`display:inline-block; width:fit-content` (Miami Aqua Tours v2),
`background-size:112% 100%; background-position:0 0` (Colbeef) — pero el defecto **persistió
incluso combinando todas ellas** en el título interno de Gas País Chilco (2026-07-29), y ya
existía de forma más sutil en el PDF entregado de Avicampo. Quedó documentado como "bug
sistémico de Chrome headless, no de un deck en particular", pendiente de una solución de
fondo.

**Solución adoptada:** renderizar el texto en gradiente como **SVG `<text>` con
`fill="url(#id)"` apuntando a un `<linearGradient>`**, en vez de aplicar
`background-clip:text` sobre una caja HTML. El SVG no pasa por el mismo pipeline de
compositing/máscara que produce el hairline en el exportador de PDF de Chrome — es una capa
de pintura distinta (paint server de SVG sobre los propios contornos del glifo).

```html
<svg class="grad-svg" viewBox="0 0 W H" style="height:1em; display:inline; vertical-align:baseline; overflow:visible;">
  <defs>
    <linearGradient id="gradBrand" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="var(--cyan)"/>
      <stop offset="33%" stop-color="var(--blue)"/>
      <stop offset="66%" stop-color="var(--violet)"/>
      <stop offset="100%" stop-color="var(--magenta)"/>
    </linearGradient>
  </defs>
  <text x="0" y="0.8em" fill="url(#gradBrand)" style="font: italic 900 1em 'Playfair Display', serif;">texto en gradiente</text>
</svg>
```

Ajustar el `viewBox` (ancho `W` aproximado al texto, alto `H` = tamaño de fuente) y el
tamaño en `font:` del `<text>` para que calce con el resto de la línea; `stop-color` puede
usar los tokens CSS de marca directamente (los custom properties se heredan dentro del SVG
inline).

**Verificación hecha esta sesión (2026-07-30):** se armó una reproducción fiel del caso que
falló en Gas País (título `.s-title` real, Playfair Display Black Italic vía `@font-face`
local, gradiente mezclado en la misma línea que texto negro, exportado con el mismo comando
de Chrome headless de `wiki/despliegue.md`) comparando la versión CSS actual contra la
versión SVG propuesta, inspeccionando el PDF resultante a 8x/~576dpi con PyMuPDF y un barrido
de píxeles buscando líneas horizontales finas. **No se logró reproducir el hairline en
ninguna de las dos versiones en esta sesión** (posible diferencia de versión de Chrome u otra
condición no replicada) — así que no hay una comparación "antes roto / después arreglado" 100%
concluyente. Aun así, se adopta el SVG como estándar desde ahora porque (a) da un resultado
visualmente idéntico al CSS en la prueba, (b) es estructuralmente inmune a esta clase de bug
por no usar `background-clip:text`, y (c) es la solución que la propia wiki venía señalando
como pendiente. Si el hairline reaparece en un deck nuevo pese a usar SVG, reportarlo — sería
evidencia de que la causa real es otra.

---

## 6. Shell interactivo obligatorio (Web) — una lámina a la vez

> **Obligatorio desde 2026-08-26** (ver CLAUDE.md raíz). Reemplaza el scroll vertical de láminas
> apiladas: la web ahora navega **una lámina a la vez**, con barra superior, viewport centrado y
> barra inferior con controles. Referencia canónica **con** switch de escenario:
> `presentaciones/marval/`. Referencia **sin** switch (un solo escenario):
> `presentaciones/fcv/`. **No afecta el PDF** — ver §7.

### 6.1 Esqueleto HTML

Cada lámina que antes era `<section class="slide cover">…</section>` /
`<section class="slide internal glow-a">…</section>` pasa a ser un **wrapper de paginación**
(`.slide`, con `data-slide="N"`) que envuelve el contenido original ahora bajo `.slide-inner`
(que conserva las clases `cover` / `internal glow-a` / etc. tal cual):

```html
<body>
  <svg width="0" height="0" style="position:absolute" aria-hidden="true">…defs de gradBrand…</svg>

  <!-- ===== BARRA SUPERIOR ===== -->
  <header class="app-header">
    <div class="header-left">
      <img src="assets/logo-campuslands.png" alt="Campuslands Full Service">
      <div class="logo-divider"></div>
      <img src="assets/logo-cliente.png" alt="[Cliente]" class="logo-client">
    </div>
    <div class="header-center">
      <!-- SOLO si hay 2+ escenarios: .scenario-selector con .scenario-pill + N .scenario-btn
           (ver presentaciones/marval/index.html líneas 31-37 y script.js switchScenario()).
           Con un único escenario, este div queda vacío. -->
    </div>
    <div class="header-right">
      <span class="badge-confidential">Confidencial</span>
    </div>
  </header>

  <!-- ===== CONTENIDO ===== -->
  <main class="app-content">
    <section class="slides-viewport">
      <div class="slides-container" id="slides-container">

        <div class="slide active" data-slide="1">
          <div class="slide-inner cover"> <!-- contenido original de la portada, sin cambios --> </div>
        </div>

        <div class="slide" data-slide="2">
          <div class="slide-inner internal glow-a"> <!-- contenido original de la lámina, sin cambios --> </div>
        </div>
        <!-- … resto de láminas … -->

      </div>
    </section>
  </main>

  <!-- ===== BARRA INFERIOR ===== -->
  <footer class="slides-footer-controls">
    <button id="btn-prev-slide" class="control-btn" onclick="navigateSlide(-1)" aria-label="Lámina anterior">…svg flecha izq…</button>
    <div class="slide-indicator">
      <span id="slide-number-display">1 / N</span>
      <div class="progress-bar-bg"><div id="slide-progress" class="progress-bar-fill"></div></div>
      <div class="playback-controls">
        <button id="btn-autoplay" class="control-btn mini" onclick="toggleAutoplay()">…svg play/pausa…</button>
      </div>
    </div>
    <button id="btn-next-slide" class="control-btn" onclick="navigateSlide(1)" aria-label="Lámina siguiente">…svg flecha der…</button>
  </footer>

  <script src="script.js"></script>
</body>
```

### 6.2 CSS reutilizable (adaptar solo los tokens de color del cliente)

```css
:root{ --header-h:68px; --footer-h:68px; /* … resto de tokens del cliente … */ }

html{ height:100%; }
body{
  height:100vh; overflow:hidden; background:var(--bg-0); color:var(--text-hi);
  display:flex; flex-direction:column;
  background-image:
    radial-gradient(120% 90% at 82% 0%, var(--bg-glow-a) 0%, transparent 45%),
    radial-gradient(120% 90% at 8% 100%, var(--bg-glow-b) 0%, transparent 50%),
    var(--bg-wash);
  background-attachment:fixed;
}

.app-header{ flex:none; height:var(--header-h); padding:0 34px; display:flex; align-items:center;
  justify-content:space-between; background:rgba(255,255,255,.86); backdrop-filter:blur(12px);
  border-bottom:1px solid rgba(20,25,35,.10); position:relative; z-index:50; }
.header-left{ display:flex; align-items:center; gap:16px; }
.header-left img{ height:24px; width:auto; object-fit:contain; }
.header-left img.logo-client{ height:30px; }
.logo-divider{ width:1px; height:26px; background:rgba(20,25,35,.14); }

/* Badge "Confidencial" — color-mix() deriva el pill directo del token del cliente,
   sin necesitar un rgba() hardcodeado nuevo por deck */
.badge-confidential{ display:inline-flex; align-items:center; gap:8px; font-weight:700; font-size:10px;
  letter-spacing:.18em; text-transform:uppercase; color:var(--dot-confidential);
  background:color-mix(in srgb, var(--dot-confidential) 10%, transparent);
  border:1px solid color-mix(in srgb, var(--dot-confidential) 28%, transparent);
  border-radius:99px; padding:7px 16px; }
.badge-confidential::before{ content:""; width:7px; height:7px; border-radius:50%;
  background:var(--dot-confidential); box-shadow:0 0 8px 1px var(--dot-confidential-glow); }

.app-content{ flex:1; min-height:0; display:flex; }
.slides-viewport{ flex:1; display:flex; }
.slides-container{ flex:1; position:relative; display:flex; align-items:center;
  justify-content:center; padding:22px 40px; min-width:0; }

/* La lámina se dibuja a su tamaño físico real (11in×6.1875in = 1056×594px a 96dpi, igual que
   el PDF) y se reescala con zoom — NUNCA transform:scale(), que combinado con el texto SVG en
   gradiente produce recortes de renderizado en Chrome headless (ver §5.2). */
.slide{ position:absolute; width:1056px; height:594px; zoom:var(--slide-scale,1); display:none;
  opacity:0; transform:translateY(16px); transition:opacity .45s ease, transform .45s ease;
  border-radius:var(--radius); overflow:hidden; box-shadow:0 20px 60px rgba(0,0,0,.22); }
.slide.active{ display:block; opacity:1; transform:translateY(0); }
.slide-inner{ width:100%; height:100%; overflow:hidden; position:relative; /* + el fondo con
  glows/wash que antes vivía directo en .slide */ }

.slides-footer-controls{ flex:none; height:var(--footer-h); padding:0 34px; display:flex;
  align-items:center; justify-content:space-between; background:rgba(255,255,255,.86);
  backdrop-filter:blur(12px); border-top:1px solid rgba(20,25,35,.10); position:relative; z-index:50; }
.control-btn{ background:none; border:1px solid rgba(20,25,35,.14); color:var(--text-hi);
  width:42px; height:42px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
.control-btn:hover{ background:var(--blue); border-color:var(--blue); color:#fff; }
.control-btn.mini{ width:34px; height:34px; }
.control-btn.active{ background:var(--grad-brand); border-color:transparent; color:#fff; }
.slide-indicator{ display:flex; align-items:center; gap:18px; flex:1; max-width:520px; margin:0 26px; }
.progress-bar-bg{ flex:1; height:6px; background:rgba(20,25,35,.07); border-radius:3px; overflow:hidden; }
.progress-bar-fill{ height:100%; width:10%; background:var(--grad-brand); transition:width .3s ease; }
```

### 6.3 JS reutilizable (sin switch de escenario)

Para un deck de **un solo escenario**, el estado es mínimo — sin `SCENARIO_DATA`, sin clases
`body.scenario-x`, sin parámetro `?escenario=`. Copiar tal cual desde
`presentaciones/fcv/script.js` (30 líneas): `resizeSlideStage()` (calcula `--slide-scale` según
el tamaño de `#slides-container`), `updateSlideDisplay()` (toggle de `.active` + número + barra
de progreso), `navigateSlide(dir)` (da la vuelta en los extremos), `toggleAutoplay()` (interval
de 5s, alterna ícono play/pausa), listener de teclado `←`/`→`, y el `resize`/`DOMContentLoaded`
inicial. Para un deck **con 2+ escenarios**, partir en cambio de
`presentaciones/marval/script.js`, que además trae `switchScenario()`, `applyScenarioContent()`,
`moveScenarioPill()` y el filtro por `data-scenario` en `isSlideVisible()`.

---

## 7. Grilla base e impresión (PDF — no lo toca el shell)

El shell del §6 es **solo de pantalla**. `@media print` lo oculta por completo y cada `.slide`
recupera su tamaño físico real en secuencia — el PDF exportado queda idéntico a como se veía
antes de tener shell (una página por lámina, sin barra superior/inferior).

```css
.slide{
  position:relative; width:var(--slide-w); height:var(--slide-h);
  overflow:hidden; border-radius:var(--radius); page-break-after:always; break-after:page;
}
@page{ size:11in 6.1875in; margin:0; }
@media print{
  html,body{ width:11in; height:auto; overflow:visible; background:none; background-image:none;
    padding:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .app-header, .slides-footer-controls{ display:none !important; }
  .app-content, .slides-viewport{ display:block; height:auto; }
  .slides-container{ display:block; padding:0; }
  .slide{ display:block !important; position:relative; width:11in; height:6.1875in; zoom:1;
    opacity:1; transform:none; margin:0 auto; border-radius:0; box-shadow:none;
    page-break-after:always; break-after:page; overflow:hidden; }
  .slide:last-child{ page-break-after:auto; break-after:auto; }
}
```

> Si el deck tiene 2+ escenarios (como Marval), agregar además el filtro por `data-scenario` y
> la clase `body.scenario-a`/`body.scenario-b` para que cada export a PDF incluya solo las
> láminas de su escenario — ver `presentaciones/marval/styles.css` §17.

---

## 8. Verificación obligatoria antes de entregar

1. **Preview en navegador** (`preview_start` + servidor estático) y captura de cada lámina.
2. **Export a PDF** con Chrome headless (ver [[despliegue]]) y **leer el PDF** para revisar
   fidelidad: colores, gradientes, fuentes locales aplicadas, y **ningún hairline**.
3. **Alineación:** verificar posición de logos, tarjetas y figuras (usar `preview_inspect`
   sobre bounding boxes si hay duda). Nada desalineado ni desbordado.
4. El nº de páginas del PDF debe igualar el nº de láminas construidas.
5. **Chequeo contra el borde de `.slide` NO basta.** En el grid `.internal` (filas fijas
   `38px 1fr 20px`), el contenido de `.s-body` puede desbordar *dentro* de la caja de `.slide`
   e invadir visualmente la fila del `.s-footer` sin que ningún elemento cruce el borde exterior
   de la lámina — un check de "overflow contra `.slide`" no lo detecta. Medir siempre, por cada
   lámina interna, el **gap entre el último elemento de `.s-body` y el `top` de `.s-footer`**
   (debe ser positivo, no solo ≥0 en el borde exterior). Caso real: `presentaciones/ve-a-la-segura/`
   tenía una lámina de cierre con -367px de colisión con el footer que este chequeo adicional detectó.
6. **Shell interactivo (§6) no debe filtrarse al PDF:** tras agregar o tocar el shell, reexportar
   y releer el PDF — debe verse **idéntico** a como se veía sin shell (sin barra superior/inferior,
   sin controles, cada lámina a tamaño completo). Comparar visualmente contra la versión anterior
   si existe. Caso real: `presentaciones/fcv/` (2026-08-26), verificado sin diferencias.
