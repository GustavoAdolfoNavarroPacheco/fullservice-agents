# Guías de los agentes

Dos guías por agente (7 agentes, 14 guías), en **web** y **PDF**, con un estilo editorial inspirado en los documentos de Claude Docs y el blog de Anthropic: títulos en serif, texto en sans, fondo blanco, tablas crema, avisos y diagramas ligeros.

| Guía | Para quién | Extensión aproximada |
|---|---|---|
| **Guía de desarrollador** | Quien mantiene el agente: arquitectura, ciclos de trabajo, formatos, reglas, scripts, verificación, mantenimiento y problemas frecuentes | 2.700–4.000 palabras · 11–14 páginas |
| **Guía de usuario** | Cualquier persona: qué darle, cómo se usa, ejemplos de conversación, qué recibe y cómo revisarlo | 1.600–2.000 palabras · 8–9 páginas |

## Agentes cubiertos

`prospection-agent` (Radar de Campus) · `intelligence-commercial` (Explorador de Campus) · `presentations-designer` (Estudio de Presentaciones) · `functional-scope` (Alcances Funcionales) · `quote-developer` (Desarrollador de Cotizaciones) · `bidding-agent` (Agente Licitatorio) · `contract-perfectionist` (Perfeccionador de Contratos).

> Cada agente vive en `agents/claude-agents/<agente>/` (Claude Code) o `agents/perplexity-agents/<agente>/` (Perplexity); las guías usan como nombre el de esa carpeta. `quote-developer` es la antigua `quote-developer-v2`: el repositorio ya no tiene una versión 1 aparte.

**Nombres:** cada guía se identifica con el nombre de la carpeta del agente en el repo (título, etiquetas, índice y encabezado del PDF), para saber siempre a cuál se refiere. El nombre descriptivo (por ejemplo, «Radar de Campus») queda como apoyo en el índice y en la primera mención del texto. La marca de la cabecera es «Campuslands | fullservice-agents» (en la fuente serif del banner) y a la derecha lleva un botón de GitHub, con hover animado, que abre el repositorio.

## Abrir

- **Índice:** [`index.html`](index.html) (funciona sin servidor).
- **Una guía:** `<agente>/guia-dev.html` o `<agente>/guia-usuario.html`, con índice lateral que sigue la lectura.
- **PDF (A4):** `<agente>/guia-dev.pdf` y `<agente>/guia-usuario.pdf`, con encabezado y «Página X de Y».

## Estructura

```
guides/
├── index.html                 índice (generado)
├── assets/                    estilo, fuentes (OFL) y logo
├── <agente>/guia-*.html/pdf   guías generadas
└── _src/                      fuente: se edita aquí, no en los HTML
    ├── contenido/<agente>/dev.md · usuario.md    el texto de cada guía (Markdown)
    ├── estilo.css             sistema visual y escala tipográfica
    ├── suave.js               activa el scroll suave (Lenis)
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

- **Escala tipográfica única de 7 tamaños** (más las cifras grandes), definida en `:root` de `estilo.css`: display, H2, lead, cuerpo, interfaz y meta. El generador **falla** si la hoja de estilos declara un tamaño fuera de esa escala, para que no vuelvan a colarse variaciones sueltas. En el PDF la escala es la misma, en puntos.
- Los subtítulos (h3) usan el tamaño del cuerpo en semibold; la jerarquía se marca con peso, no con tamaños casi iguales.
- El generador también comprueba la hoja de estilos al construir; si el texto usa un glifo que Inter o Source Serif no tienen, hay que reemplazarlo por uno que sí exista.

## Mantener las guías al día

Las guías resumen la configuración de cada agente (`CLAUDE.md`, `Perplexity.md`, habilidades y wiki) a **noviembre de 2026**. Si cambia un agente, se edita el Markdown de su guía y se regenera. Los datos que más caducan: los precios de IA de `bidding-agent`, las rutas y archivos citados y las reglas de marca de `presentations-designer`.

Cada guía Dev incluye, cuando aplica, una sección «Cosas que no están alineadas» con inconsistencias reales entre archivos del propio agente, verificadas contra los archivos.

## Fuentes tipográficas

[Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) e [Inter](https://fonts.google.com/specimen/Inter), ambas con licencia SIL Open Font License, en `assets/fonts/`. Reemplazan a las tipografías propietarias de Anthropic, que no se pueden redistribuir.
