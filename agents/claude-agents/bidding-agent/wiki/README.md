# wiki/

Conocimiento acumulado entre licitaciones. No es fuente de datos de un proceso
(eso vive en `recursos/`) — es la memoria de trabajo del agente para mantener
consistencia y método entre propuestas.

| Archivo | Contenido |
|---|---|
| `index.md` | Catálogo de la wiki y de las licitaciones procesadas, con su estado. **Se lee primero.** |
| `log.md` | Bitácora cronológica append-only: cada ingesta, propuesta, ajuste y lint. |
| `flujo-trabajo.md` | Las tres fases del proceso: ingesta y análisis, construcción de los cuatro entregables, verificación y entrega. |
| `perfil-usuario.md` | Rol del agente, insumos, entregables y reglas de oro. |
| `estructura-propuesta-tecnica.md` | Anatomía de secciones de la propuesta técnica. |
| `estimacion-horas.md` | Método de estimación, especialidades, conversión horas↔días, validación de factibilidad. |
| `consideraciones-tecnicas.md` | Checklist de 15 bloques que se recorre completo en toda licitación. |
| `costeo-ia-tokens.md` | Precios vigentes por modelo, método de estimación de tokens, escenarios. **Verificar vigencia antes de cada costeo.** |
| `marca-campuslands.md` | Paleta, logotipos, layout, convenciones de XLSX y nomenclatura de archivos. |
| `licitaciones/<slug>.md` | Ficha por licitación: datos del proceso, decisiones tomadas, ambigüedades resueltas, mapeo de los modelos de costos, estado. |

## Antes de empezar una licitación

Leer `index.md`, luego `flujo-trabajo.md`, y — si ya se trabajó con esa entidad o
ese proceso antes — la ficha en `licitaciones/` para no repetir preguntas ya
resueltas.

## Antes de costear IA

Verificar la fecha de la tabla de precios en `costeo-ia-tokens.md` y confirmar los
precios vigentes. Los precios de los modelos caducan.
