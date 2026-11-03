# Guías de los agentes

Dos guías por agente (7 agentes, 14 guías), en **web** y **PDF**, con un estilo editorial inspirado en los documentos de Claude Docs y el blog de Anthropic: títulos en serif, texto en sans, fondo blanco, tablas crema, avisos y diagramas ligeros.

| Guía | Para quién | Extensión aproximada |
|---|---|---|
| **Guía Dev** | Quien mantiene el agente: arquitectura, ciclos de trabajo, formatos, reglas, scripts, verificación, mantenimiento y problemas frecuentes | 2.700–4.000 palabras · 11–14 páginas |
| **Guía de usuario** | Cualquier persona: qué darle, cómo se usa, ejemplos de conversación, qué recibe y cómo revisarlo | 1.600–2.000 palabras · 8–9 páginas |

## Agentes cubiertos

`prospection-agent` (Radar de Campus) · `intelligence-commercial` (Explorador de Campus) · `presentations-designer` (Estudio de Presentaciones) · `functional-scope` (Alcances Funcionales) · `quote-developer-v2` (Desarrollador de Cotizaciones) · `bidding-agent` (Agente Licitatorio) · `contract-perfectionist` (Contract Perfectionist).

> `quote-developer/` (v1) queda fuera: es el legado congelado de `quote-developer-v2/`.

## Abrir

- **Índice:** [`index.html`](index.html) (funciona sin servidor).
- **Una guía:** `<agente>/guia-dev.html` o `<agente>/guia-usuario.html`, con índice lateral que sigue la lectura.
- **PDF (A4):** `<agente>/guia-dev.pdf` y `<agente>/guia-usuario.pdf`, con encabezado y «Página X de Y».

## Estructura

```
guias/
├── index.html                 índice (generado)
├── assets/                    estilo, fuentes (OFL) y logo
├── <agente>/guia-*.html/pdf   guías generadas
└── _src/                      fuente: se edita aquí, no en los HTML
    ├── contenido/<agente>/dev.md · usuario.md    el texto de cada guía (Markdown)
    ├── estilo.css             sistema visual y escala tipográfica
    ├── md.py                  convertidor Markdown → HTML (sin dependencias)
    └── build.py               genera web, PDF e índice
```

## Regenerar

```bash
python -X utf8 guias/_src/build.py                      # todas las guías, PDF e índice
python -X utf8 guias/_src/build.py quote-developer-v2   # solo un agente
python -X utf8 guias/_src/build.py --sin-pdf            # solo HTML
```

Requiere Python 3, Chrome y `playwright` (para exportar los PDF).

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
