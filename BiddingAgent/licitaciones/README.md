# licitaciones/ — Entregables generados

Una subcarpeta autocontenida por licitación. El slug es minúsculas, sin espacios ni
tildes, con el identificador del proceso cuando exista (ej. `ipa-pr10598`,
`ecopetrol-lic-2026-014`).

## Contenido de cada carpeta

```
licitaciones/<slug-licitacion>/
├── 00 - Analisis Documental.md            # Fase 1: inventario, contradicciones, supuestos
├── 01 - Matriz de Cumplimiento.xlsx       # Gate de cero requerimientos omitidos
├── 02 - Propuesta Tecnica.pdf             # ENTREGABLE 1
├── 03 - Estimacion de Horas.xlsx          # ENTREGABLE 2
├── 04 - Consideraciones Tecnicas.md       # ENTREGABLE 3 (incluye la conclusión sobre IA)
├── 05 - Analisis IA y Tokens.xlsx         # ENTREGABLE 4 (solo si se requiere IA)
├── 06 - Modelo de Costos Oficial.xlsx     # Formato de la empresa, llenado
├── 07 - Modelo de Costos Cotizacion.xlsx  # Modelo interno, llenado
└── verificacion-cruzada.md                # Rastro auditable de la verificación
```

El prefijo numérico fija el orden de lectura. Si el RFP exige nombres de archivo
específicos para la radicación, se generan **copias** con el nombre exigido y se
conserva la numeración interna para trabajo.

## Los cuatro entregables

| # | Archivo | Qué contiene |
|---|---|---|
| 1 | `02 - Propuesta Tecnica` | Módulos, funcionalidades, alcance, arquitectura, metodología, cronograma y equipo, alineados con los requerimientos y el plazo exigido |
| 2 | `03 - Estimacion de Horas` | Horas por módulo/funcionalidad y especialidad, con método, supuestos y validación de factibilidad contra el plazo |
| 3 | `04 - Consideraciones Tecnicas` | Todo elemento técnico necesario, con la conclusión explícita de si se requiere IA |
| 4 | `05 - Analisis IA y Tokens` | Actividades que requieren IA, estimación de tokens y costo estimado en tres escenarios |

Los archivos `00`, `01`, `06`, `07` y `verificacion-cruzada.md` son el soporte que
hace defendibles esos cuatro.

## Versionado antes de la radicación

Revisiones: sufijo `(v2)`, `(v3)`. Se conserva la versión anterior en la misma
carpeta hasta que la nueva se confirme como definitiva. `wiki/licitaciones/<slug>.md`
siempre apunta a la versión vigente.

## Confidencialidad

Esta carpeta contiene precios, márgenes y estrategia de propuestas en curso. No se
mezcla información entre licitaciones, y ninguna propuesta referencia otra
licitación ni otro cliente. Antes de compartir el repositorio o subirlo a un remoto,
confirmar con el usuario si esta carpeta debe excluirse.
