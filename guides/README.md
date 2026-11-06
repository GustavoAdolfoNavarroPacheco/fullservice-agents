# Guías de los agentes

Dos guías por agente (7 agentes, 14 guías), en **web** y **PDF**, con un estilo editorial inspirado en los documentos de Claude Docs y el blog de Anthropic: fondo marfil, títulos y prosa en serif (párrafos, listas y avisos), interfaz (tablas, tarjetas, pestañas, botones) en sans, enlaces en tinta con subrayado y **un solo acento** (el naranja, solo en el indicador de pestaña, el foco y el pulso del mensaje). Los avisos, pasos, carriles, insignias y botones son neutros (tinta, avena y marfil), sin verdes, rosas ni azules: así el color no compite con el texto.

| Guía | Para quién | Extensión aproximada |
|---|---|---|
| **Guía de desarrollador** | Quien mantiene el agente: arquitectura, ciclos de trabajo, formatos, reglas, scripts, verificación, mantenimiento y problemas frecuentes | 2.700–4.000 palabras · 11–14 páginas |
| **Guía de usuario** | Cualquier persona: qué darle, cómo se usa, ejemplos de conversación, qué recibe y cómo revisarlo | 1.600–2.000 palabras · 8–9 páginas |

## Agentes cubiertos

`prospection-agent` (Radar de Campus) · `intelligence-commercial` (Explorador de Campus) · `presentations-designer` (Estudio de Presentaciones) · `functional-scope` (Alcances Funcionales) · `quote-developer` (Desarrollador de Cotizaciones) · `bidding-agent` (Agente Licitatorio) · `contract-perfectionist` (Perfeccionador de Contratos).

> Cada agente vive en `agents/claude-agents/<agente>/` (Claude Code) o `agents/perplexity-agents/<agente>/` (Perplexity); las guías usan como nombre el de esa carpeta. `quote-developer` es la antigua `quote-developer-v2`: el repositorio ya no tiene una versión 1 aparte.

**Nombres:** cada guía se identifica con el nombre de la carpeta del agente en el repo (título, etiquetas, índice y encabezado del PDF), para saber siempre a cuál se refiere. El nombre descriptivo (por ejemplo, «Radar de Campus») queda como apoyo en el índice y en la primera mención del texto. La marca de la cabecera es «Campuslands | fullservice-agents» (en la fuente serif del banner) y a la derecha lleva un botón de GitHub, con hover animado, que abre el repositorio.

## Abrir

- **Índice:** [`inicio.html`](inicio.html) (pestañas Inicio · Instalación · Guía de usuario · Guía de desarrollador). Las direcciones de la web son limpias (ver «Direcciones» abajo), así que para ver las guías hay que servirlas (`servir.py`), no abrir los archivos directamente.
- **Una guía:** `<agente>/guia-dev.html` o `<agente>/guia-usuario.html`, con índice lateral que sigue la lectura.
- **PDF (A4):** `<agente>/guia-dev.pdf` y `<agente>/guia-usuario.pdf`, con encabezado y «Página X de Y».

## Estructura

```
guides/
├── inicio.html                índice, pestaña «Inicio» (generado)
├── inicio/instalacion.html    el mismo índice, pestaña «Instalación» (generado)
├── inicio/usuario.html        el mismo índice, pestaña de usuario (generado)
├── inicio/desarrollador.html  el mismo índice, pestaña de desarrollador (generado)
├── assets/                    estilo, fuentes (OFL) y logo
├── <agente>/guia-*.html/pdf   guías generadas
└── _src/                      fuente: se edita aquí, no en los HTML
    ├── contenido/<agente>/dev.md · usuario.md    el texto de cada guía (Markdown)
    ├── estilo.css             sistema visual y escala tipográfica
    ├── suave.js               activa el scroll suave (Lenis)
    ├── efectos.js             letter swap, wave text, Card Stack (portadas), Coverflow (logos) y carga de imágenes bajo demanda
    ├── preview.py             genera las imágenes de vista previa del enlace (1200 × 630) con Chrome
    ├── recursos_web.py        genera las portadas (desde los PDF de presentaciones) y los logos a color en WebP
    ├── md.py                  convertidor Markdown → HTML (sin dependencias)
    ├── build.py               genera web, PDF e índice
    ├── servir.py              servidor local con recarga en vivo
    └── probar_web.py          prueba el comportamiento de la web en un navegador real
```

## Ver en local, con recarga en vivo

```bash
python -X utf8 guides/_src/servir.py        # http://localhost:4173  (otro puerto: PORT=5000 python ...)
```

Sirve `guides/` y vigila `_src/contenido/`, `estilo.css`, `suave.js`, `md.py` y `build.py`. Al guardar un cambio reconstruye el HTML (sin PDF, para no tocar los PDF versionados) y el navegador se recarga solo, conservando la posición de lectura. Si el Markdown tiene un error, la página lo muestra en un aviso. En la app de escritorio también se arranca con la configuración `guias` de `.claude/launch.json`.

## Regenerar

```bash
python -X utf8 guides/_src/build.py                      # todas las guías, PDF e índice
python -X utf8 guides/_src/build.py quote-developer   # solo un agente
python -X utf8 guides/_src/build.py --sin-pdf            # solo HTML
```

Requiere Python 3, Chrome y `playwright` (para exportar los PDF).

## Despliegue

`vercel.json` (en la raíz del repositorio) publica solo `guides/`, sin build, con `X-Robots-Tag: noindex`. El resto del repositorio no se sirve.

## Vista previa del enlace

Al pegar un enlace en WhatsApp, Slack, LinkedIn, X o Teams se ve una tarjeta con imagen. Cada página lleva sus etiquetas Open Graph y Twitter (`og:title`, `og:description`, `og:image` absoluta, `twitter:card = summary_large_image`, `canonical`…), que arma `head()` en `build.py`; la dirección base es `SITE` (`https://fullservice-agents.vercel.app`; si cambia el dominio, se cambia ahí).

Las imágenes (`assets/img/preview/`, PNG de 1200 × 630, ~200 KB: bajo el límite de 300 KB de WhatsApp) salen de `python -X utf8 guides/_src/preview.py`, que las dibuja con las mismas fuentes, aros y iconos 3D del banner: una para el índice (`home.png`) y una por cada guía (`<agente>-<usuario|dev>.png`, con su tipo, nombre, titular y plataforma). Se versionan; vuelve a correr el script al cambiar un título, un nombre de agente o el diseño.

Las plataformas guardan la vista previa en caché: tras desplegar, se puede refrescar con el depurador de cada una (p. ej. LinkedIn Post Inspector o el Sharing Debugger de Facebook).

## Direcciones

Sin `index.html`, sin `.html` y sin `#`:

| Dirección | Qué muestra |
|---|---|
| `/inicio` | Índice, pestaña «Inicio» (`/` y `/index.html` redirigen aquí) |
| `/inicio/instalacion` | Índice, pestaña «Instalación» |
| `/inicio/usuario` | Índice, pestaña «Guía de usuario» |
| `/inicio/desarrollador` | Índice, pestaña «Guía de desarrollador» (las pestañas cambian la dirección sin recargar; el antiguo `#dev` se limpia solo) |
| `/<agente>/guia-usuario` · `/<agente>/guia-dev` | Cada guía (con `.html` redirige a la limpia) |
| `/<agente>/guia-usuario.pdf` | El PDF (los archivos conservan su extensión) |

En Vercel lo hacen `cleanUrls` y `redirects` de `vercel.json`; en local, `servir.py` replica las mismas reglas. El índice son cuatro archivos reales (`inicio.html`, `inicio/instalacion.html`, `inicio/usuario.html` e `inicio/desarrollador.html`, la misma página con su propia dirección canónica): así Vercel los sirve sin reescrituras, que con `cleanUrls` fallaban con un 404. El índice lleva `<base href="/">` para que sus enlaces relativos funcionen también bajo `/inicio/desarrollador`.

## Pestañas «Inicio» e «Instalación»

Son las dos primeras pestañas del índice, a la izquierda de «Guía de usuario», y hablan de **todo el repositorio**, no de un agente. Cada una se genera de un Markdown (`_src/contenido/inicio.md` e `instalacion.md`) y se inserta en el índice con su propio índice lateral. **Inicio** explica qué es el repositorio y cómo está organizado. **Instalación** tiene tres partes y una tabla final de problemas:

- **Instalación**, con un *switch* entre «Instalación para usuario» (un mensaje para copiar y dárselo a la IA, que clona todo en el lugar correcto) y «Instalación para desarrollador» (la lista de comandos).
- **Repositorio aparte:** el Estudio de Presentaciones entrega en `Presentaciones`, un repositorio **privado** que llega vacío al clonar el raíz. Explica el clon en la carpeta exacta, el permiso que concede Gustavo (para clonar y para el `push`) y los ~2 minutos que tarda Vercel en publicar.
- **Usarlo como Proyecto** en Claude o Perplexity (y, al final, **Si algo falla** con una tabla de síntomas y soluciones): un selector con los siete agentes muestra, en tres pasos, qué archivo va a dónde (instrucciones, archivos, qué no se sube) y el texto de instrucciones listo para copiar. Los datos están en `PROYECTO` de `build.py`; el test `probar_web.py` comprueba que todos los archivos listados existan.

El mismo «repositorio aparte» está documentado en las guías de `presentations-designer` (usuario: «Cómo funciona la web de presentaciones»; desarrollador: «El repositorio aparte y su publicación») y es regla del agente en su `CLAUDE.md`.

Componentes nuevos (todos en `efectos.js` y `estilo.css`; sin JavaScript se ven completos):

| Bloque en Markdown | Qué hace |
|---|---|
| `::: switch id` · `::: tab clave \| Título \| icono` · `:::` | Selector entre paneles con pastilla deslizante; con `chips` en la primera línea, una fila de opciones; con `menu`, un desplegable. Recuerda la elección, se abre con `#id-clave` y se maneja con flechas |
| ```` ```prompt ```` · ```` ```bash ```` · ```` ```powershell ```` | Mensaje o comandos con botón «Copiar» (portapapeles, con respaldo) |
| ```` ```repos ```` | Los dos repositorios, uno dentro del otro: la carpeta del segundo se «llena» al verse |
| ```` ```publicar ```` | Línea de tiempo animada: los puntos se encienden en orden y el globo marca el tiempo |
| ```` ```proyectos ```` | Desplegable con los siete agentes (nombre de su carpeta, plataforma y rol; se abre con rebote, con teclado: ↑ ↓ Inicio Fin, letras, Intro y Esc) y, para el elegido, una ficha en tres pasos: pegar las instrucciones, subir estos archivos y dejarlos fuera. Las cifras cuentan y los pasos entran en escalera al verse |

Los enlaces `#` del índice lateral y entre pestañas de «Inicio» e «Instalación» se deslizan con el mismo scroll suave de las guías (`window.irA`, sobre Lenis), abriendo antes la pestaña donde está la sección. **Iconos 3D del banner:** cada icono es un bloque macizo: la cara a z = 0 (así no se reescala ni se ve borrosa) y detrás 64 láminas finas (`.ico-s`, generadas en `build.py`) teñidas de `--edge` a `--edge2` que forman el canto. Al entrar el cursor el icono da una vuelta completa **hacia donde se mueve el cursor** (`ART_JS` calcula el eje `--ax`/`--ay` con el movimiento reciente, o con la dirección de entrada si casi no se movía). Las imágenes de la cara son de 480 px (`assets/img/plataforma-*-xl.png`, generadas a partir de `resources/platforms-logos/`).

**Entrada a la web:** la primera vez de cada sesión aparece una cortina (logo, nombre y una línea de color que crece desde el centro) que se abre por la mitad; después la barra superior baja y el contenido sube escalonado. En las demás páginas de la sesión solo queda el escalonado. Todo es CSS (sección «Entrada a la web» de `estilo.css`, con `--e` como espera); el `<head>` decide si hay cortina con `sessionStorage` y `efectos.js` solo anota la marca y retira el nodo. No existe en el PDF ni con «reducir movimiento». Las animaciones de aparición usan `[data-reveal]` y la clase `fx` (la pone un script del `<head>`, para que no haya parpadeo). En el PDF todo sale ya completo (`revelarTodo()`), con los dos paneles de cada *switch*.

## Efectos y componentes

Reescritos en JavaScript puro a partir de los componentes de 21st.dev (el sitio es HTML estático, sin React ni framer-motion; 21st.dev no publica el código sin clave de API):

- **Letter Swap** (danielpetho): barra superior, pestañas, botones y nombre de cada fila del índice (la fila entera lo dispara).
- **Wave Text** (kokonutd): título del banner del índice; entra en ola y repite la ola al pasar el cursor, sin interrumpirse.
- **Card Stack** (ruixen.ui): portadas de las presentaciones en las guías de `presentations-designer`. Abanico al pasar el cursor, arrastre, flechas, teclado y auto-avance (se detiene con el cursor encima).
- **Coverflow** (ruixen.ui): logos de los clientes con sus colores originales (WebP recortado de máx. 280 × 210 px).
- **Social Preview Dock** (ruixen.ui): esquina inferior derecha del pie del índice, con GitHub y LinkedIn. Los iconos crecen al pasar el cursor y muestran una vista previa del perfil (`assets/img/social/*.webp`, hechas de capturas de los perfiles sin los botones que solo ve el dueño ni datos de contacto). Para cambiar enlaces o textos: `DOCK` en `build.py`.

**Carga rápida:** las imágenes de los carruseles no llevan `src`, sino `data-src`; `efectos.js` las descarga cuando el carrusel está a menos de 600 px de la pantalla (primero la activa y sus vecinas, luego a medida que se avanza) y las muestra con un fundido. Antes de imprimir o generar el PDF se cargan todas (`window.cargarImagenes()`).

En el Markdown se insertan con bloques ```` ```cardstack ```` y ```` ```coverflow ````; las listas están en `PORTADAS` y `LOGOS` de `build.py`. Tras añadir un deck o un logo: `python guides/_src/recursos_web.py` y recompilar. Con «reducir movimiento» no hay auto-avance ni ola, y en el PDF los carruseles salen como cuadrícula.

## Comandos «!»

Cada guía de usuario y de desarrollador tiene una sección con los comandos de ese agente. La tabla no se escribe a mano: el bloque ```` ```comandos ```` del Markdown la genera `build.py` desde `resources/comandos/comandos.py`, la misma fuente de la que salen las instrucciones de los agentes. Al cambiar un comando: corre ese script y recompila las guías.

## Scroll suave y barra de scroll

- **Scroll suave:** [Lenis](https://github.com/darkroomengineering/lenis) 1.3.27 (MIT; `assets/lenis.min.js` y su licencia en `assets/LENIS-LICENSE.txt`) activado por `suave.js` en todas las páginas, con los mismos parámetros que el portal de presentaciones. Los enlaces del índice lateral se deslizan a su sección, el índice lateral tiene su propia inercia y todo se apaga con «reducir movimiento» del sistema y al imprimir.
- **Barra de scroll:** fina y redonda, con hover y estado activo, en la página y en las áreas con scroll (tablas y bloques de código anchos). Usa `::-webkit-scrollbar` en Chrome, Edge y Safari y `scrollbar-width` en Firefox.
- **Distribución:** cabecera y cuerpo comparten el mismo contenedor (`--page-w`), el ritmo vertical usa `--space-block` y `--space-section`, y las cifras, tarjetas y pasos eligen sus columnas según cuántos elementos hay (sin tarjetas huérfanas ni flechas colgando).

## Pruebas de la web

```bash
python -X utf8 guides/_src/probar_web.py http://127.0.0.1:4173    # con el servidor local en marcha
```

Comprueba en un navegador real que Lenis está activo, que el scroll de las anclas es progresivo y llega bajo la barra superior, que la rueda tiene inercia, que la cabecera muestra la marca y el botón de GitHub (enlace al repo y animación de hover), que no hay errores de consola, que no hay desborde horizontal en 6 anchos y que solo se usan los tamaños de la escala tipográfica.

## Cómo se escribe una guía

Cada guía es un Markdown con una cabecera mínima:

```
---
titulo: Título de la guía
resumen: Una o dos frases que aparecen bajo el título y en el índice.
---

## Primera sección
```

Además del Markdown habitual (títulos `##` y `###`, listas, tablas, `**negrita**` y `` `código` ``), hay bloques propios:

| Bloque | Qué dibuja |
|---|---|
| `> [!nota]`, `[!importante]`, `[!tip]`, `[!cuidado]` | Aviso con fondo de color |
| ` ```stats ` | Cifras destacadas (`valor \| descripción`) |
| ` ```cards ` | Tarjetas (`título \| texto`) |
| ` ```flow ` | Diagrama de pasos numerados (`título \| texto`) |
| ` ```lanes ` | Carriles: quién hace qué (`Actor \| paso`) |
| ` ```chat ` | Conversación de ejemplo (`Tú: …` y `Agente: …`) |
| ` ```tree ` | Árbol de carpetas, con comentarios tras `#` |

## Reglas de estilo

- **Estándar de contenedores** (última sección de `estilo.css`, modelada en las tablas y gráficas del blog de Anthropic): todo marco lleva una línea de 1 px en tinta, esquinas rectas, fondo marfil y sin sombra; las tablas son una rejilla completa con cabecera y primera columna en semibold; los elementos internos usan una línea suave y el relleno de apoyo; solo botones, etiquetas y círculos son redondeados. Se controla con los tokens `--box-line`, `--box-line-2`, `--box-r`, `--box-pad` y `--box-gap`.
- **Escala tipográfica única de 5 tamaños**, definida en `:root` de `estilo.css`: display (h1), H2 (también las cifras grandes), cuerpo (prosa en serif), interfaz (tablas, tarjetas, botones, conversaciones; sans) y meta (etiquetas, chips, código). El generador **falla** si la hoja de estilos declara un tamaño fuera de esa escala, para que no vuelvan a colarse variaciones sueltas. En el PDF la escala es la misma, en puntos.
- Los subtítulos (h3) usan el tamaño del cuerpo en semibold; la jerarquía se marca con peso, no con tamaños casi iguales.
- El generador también comprueba la hoja de estilos al construir; si el texto usa un glifo que Inter o Source Serif no tienen, hay que reemplazarlo por uno que sí exista.

## Mantener las guías al día

Las guías resumen la configuración de cada agente (`CLAUDE.md`, `Perplexity.md`, habilidades y wiki) a **noviembre de 2026**. Si cambia un agente, se edita el Markdown de su guía y se regenera. Los datos que más caducan: los precios de IA de `bidding-agent`, las rutas y archivos citados y las reglas de marca de `presentations-designer`.

Cada guía Dev incluye, cuando aplica, una sección «Cosas que no están alineadas» con inconsistencias reales entre archivos del propio agente, verificadas contra los archivos.

## Fuentes tipográficas

[Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) e [Inter](https://fonts.google.com/specimen/Inter), ambas con licencia SIL Open Font License, en `assets/fonts/`. Reemplazan a las tipografías propietarias de Anthropic, que no se pueden redistribuir.
