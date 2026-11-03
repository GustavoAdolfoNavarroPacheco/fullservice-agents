# Guías de los agentes

Dos guías por agente (7 agentes, 14 guías), en **visor web** y **PDF**, con el sistema de diseño v3 de `presentations-designer` (láminas 1056 × 594 px, Poppins, fondo blanco, sombras en lugar de bordes, logo de Campuslands a color).

| Guía | Para quién | Láminas |
|---|---|---|
| **Guía Dev** | Quien mantiene el agente: carpetas, ciclos de trabajo, reglas, scripts, verificación y mantenimiento | 12 |
| **Guía de usuario** | Cualquier persona: qué darle, cómo se usa, qué escribirle, qué recibe y cómo revisarlo | 9–10 |

## Agentes cubiertos

`prospection-agent` (Radar de Campus) · `intelligence-commercial` (Explorador de Campus) · `presentations-designer` (Estudio de Presentaciones) · `functional-scope` (Alcances Funcionales) · `quote-developer-v2` (Desarrollador de Cotizaciones) · `bidding-agent` (Agente Licitatorio) · `contract-perfectionist` (Contract Perfectionist).

> `quote-developer/` (v1) queda fuera: es el legado congelado de `quote-developer-v2/`.

## Abrir

- **Portal:** abrir [`index.html`](index.html) (funciona sin servidor, también desde un hosting estático).
- **Una guía:** `<agente>/dev/index.html` o `<agente>/usuario/index.html`; teclas ← → para cambiar de lámina.
- **PDF:** `<agente>/dev/guia-dev.pdf` y `<agente>/usuario/guia-usuario.pdf`.

## Estructura

```
guias/
├── index.html                 portal (generado)
├── assets/                    estilos, visor, fuentes Poppins, logo (compartidos)
├── <agente>/dev/              index.html + guia-dev.pdf
├── <agente>/usuario/          index.html + guia-usuario.pdf
└── _src/                      fuente: se edita aquí, no en los HTML
    ├── kit.py                 arquetipos de lámina, íconos, ensamblador
    ├── base.css · extras.css  CSS de la plantilla v3 + componentes de guías
    ├── portal.py              landing
    ├── agentes/<agente>.py    contenido de las dos guías de cada agente
    ├── build.py               genera los HTML
    └── verificar.py           verificar_deck.py + PDF + hojas de contacto
```

## Regenerar

```bash
python -X utf8 guias/_src/build.py                   # todas las guías y el portal
python -X utf8 guias/_src/build.py quote-developer-v2  # solo un agente
python -X utf8 guias/_src/verificar.py               # verificador oficial + PDF de las 14
```

`verificar.py` ejecuta `presentations-designer/herramientas/verificar_deck.py` (necesita Chrome y Playwright) y exporta el PDF de cada guía. Tras un cambio de contenido hay que **regenerar y volver a mirar las láminas**: un texto más largo puede romper el reparto.

## Reglas aplicadas (y dónde se apartan)

Se siguen las reglas de `presentations-designer/CLAUDE.md`: tema claro, Poppins en todo, tarjetas sin bordes, decoración `.fx`, un ícono con significado por elemento, numeral `.ghost`, migas en el pie, `verificar_deck.py` en APROBADO y revisión a la vista.

Diferencias deliberadas respecto a un deck comercial:

- **Sin logo de cliente:** son documentos internos; la portada y el cierre llevan solo el logo de Campuslands (el verificador lo marca como aviso, no como error).
- **Hasta 12 láminas** en las guías Dev (`--max-slides 12`); las de usuario no pasan de 10. La regla de 10 es de los decks comerciales.

## Mantener las guías al día

Las guías resumen el `CLAUDE.md` / `Perplexity.md` de cada agente a noviembre de 2026. Si cambia la configuración de un agente, actualizar su `_src/agentes/<agente>.py` y regenerar. Hallazgos de lint que ya constan en las guías Dev (sección «Síntomas frecuentes»): `presentations-designer/CLAUDE.md` cita `wiki/verificacion.md` y `wiki/temas-por-cliente.md`, y `quote-developer-v2/CLAUDE.md` cita `wiki/flujo-trabajo.md` y `scripts/recalc.py`; ninguno existe hoy en esas carpetas.
