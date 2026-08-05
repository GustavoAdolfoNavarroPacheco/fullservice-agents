## [2026-08-05] ajuste | Jerarquía flexible Módulo→Submódulo→Funcionalidad(es) + nuevas reglas de XLSX

A pedido explícito del usuario, tras detectar que las cotizaciones nuevas quedaban más
cortas en volumen de información que las elaboradas a mano (comparación directa:
`CasaBlanca` —desarrollada por el agente, patrón fijo "1 submódulo = 1 descripción"— vs.
`Allied Steel` —hecha a mano, cardinalidad libre de bullets por submódulo—, ambas en
`FullServices_NAL_2026.xlsx`):

1. **Jerarquía de columnas L/M/N reinterpretada**: L=Módulo (sin cambio), **M pasa de
   "Funcionalidad" a "Submódulo"** (encabezado de agrupación, puede repetirse varias veces
   bajo un mismo módulo), **N pasa de "Detalle técnico de una M" a "Funcionalidad atómica"**
   (puede repetirse varias veces bajo un mismo submódulo — mínimo 1, sin techo). Prohibido
   forzar el patrón antiguo de 1 par M+N por bullet. Actualizado en `CLAUDE.md` §Reglas del
   XLSX/PDF y en los espejos `wiki/plantilla-xlsx.md`, `wiki/diseno-pdf-cotizacion.md`,
   `wiki/marca-campuslands.md` §5 y `wiki/perfil-usuario.md`.
2. **Días estimados (B:K) reasignados**: antes iban en la fila M; ahora van **siempre en
   cada fila N** (funcionalidad), nunca en M (submódulo, que no representa una unidad de
   esfuerzo). Cada N bajo un mismo M lleva su propio estimado independiente.
3. **Tipografía formalizada**: Arial — Módulo 11pt negrita, Submódulo 10pt negrita,
   Funcionalidad/Detalle técnico 10pt regular. Ya se aplicaba de facto (ver entradas previas
   del log) pero no estaba documentada explícitamente; ahora vive en `wiki/marca-campuslands.md`
   §5 y `wiki/diseno-pdf-cotizacion.md`.
4. **Nueva excepción a la zona intocable**: además de `Y{barra_gris+2}` (`=Y1/0.6`), se
   agrega `R{barra_gris+3}` = `0.1` (10%, celda de porcentaje AIU) — reemplaza el default de
   la plantilla maestra (40%). Documentado en `CLAUDE.md` §Reglas del XLSX §5 y en
   `wiki/plantilla-xlsx.md` §5.
5. **Referencia de verdad actualizada**: `cotizaciones/compumax/Compumax Computer S.A.S -
   Cotizacion.xlsx` sigue siendo válido para B:K, la fórmula de Y y la zona intocable, pero
   **ya no es referencia de cardinalidad L/M/N** (sigue el patrón antiguo, superado). No se
   reprocesan cotizaciones ya entregadas — este ajuste aplica hacia adelante.

Pendiente: primera cotización construida bajo esta regla se convierte en la nueva
"referencia de verdad" de cardinalidad para `wiki/plantilla-xlsx.md` §2.
