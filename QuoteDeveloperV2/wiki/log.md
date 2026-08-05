# Bitácora — Agente Desarrollador de Cotizaciones

Registro cronológico, append-only. Prefijo `## [YYYY-MM-DD] <tipo> | <descripción>`
con tipo ∈ {setup, build, ajuste, deploy, lint}.

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

Pendiente (resuelto abajo, 2026-08-05/build Comultrasan): primera cotización construida bajo
esta regla se convierte en la nueva "referencia de verdad" de cardinalidad para
`wiki/plantilla-xlsx.md` §2.

## [2026-08-05] build | Financiera Comultrasan — Asistente Conversacional Orbit (Canales Digitales)

Primera cotización construida en el repo `QuoteDeveloperV2` (repo nuevo, sin historial previo:
no traía `wiki/index.md`, `wiki/log.md`, `scripts/` ni ejemplos en `cotizaciones/` — se crearon
en este build). Fuente de alcance: PDF `Propuesta_Comultrasan_Campuslands_v4.pdf` (propuesta
comercial preparada por Gabriela Pedraza Rueda) + transcripción completa de la reunión de
levantamiento de necesidades con Angela Latorre (Jefe de Canales Virtuales y Electrónicos,
Financiera Comultrasan). Usuario confirmó explícitamente incluir los módulos de fase posterior
(Ventas & Crédito, PQRS & Jurídico) como opcionales dentro de la misma cotización.

- **Alcance**: 5 módulos — M1 Agente Orquestador Orbit, M2 Canales Digitales (alcance inicial
  acordado: transferencias Bre-B, pago de crédito, transferencias generales, registro en
  Agencia Virtual, FAQs de uso), M3 Integraciones y Canales de Entrada (WhatsApp Business,
  botón Canales Digitales del portal web, HubSpot), M4 Ventas y Crédito (opcional, fase
  posterior), M5 PQRS y Jurídico (opcional, fase posterior). Cardinalidad de funcionalidades
  por submódulo: 1 a 4, fiel a lo descrito en la propuesta y la transcripción — primera
  cotización de este repo construida bajo la regla de jerarquía flexible (2026-08-05),
  confirmando que la regla funciona con datos reales de cliente.
- **XLSX**: sin necesidad de insertar filas (alcance cupo en las filas 8-44 de las 112
  disponibles antes de la barra gris en fila 120, posición sin cambios respecto a la
  plantilla maestra). Excepciones aplicadas: `Y122='=Y1/0.6'`, `R123=0.1` (ambas confirmadas
  vacías/default antes de escribir). Recalculado con `scripts/recalc.py` (LibreOffice, con los
  fixes de PATH/AF_UNIX de `project-quotedeveloper-xlsx-workflow`): 0 errores fuera de
  `A140:A144` (defecto preexistente conocido de la plantilla). TOTAL general: **$48.378.375
  COP** (`AC1`).
- **PDF**: generado con `reportlab` (no existía script de PDF reutilizable en este repo nuevo;
  se construyó desde cero siguiendo `wiki/diseno-pdf-cotizacion.md` — paleta clara, grid
  completo, jerarquía Módulo→Submódulo→Funcionalidad, Arial 11/10/10). Doble verificación
  contenido-precio: suma de funcionalidades de cada módulo == subtotal del módulo (columna Y
  del XLSX), y suma de todos los módulos + fases transversales == TOTAL general (`AC1`) —
  ambas coincidieron exactamente. Sin logo de cliente (Comultrasan no aportó uno) — solo
  logo Campuslands.
- **Entregables**: `cotizaciones/comultrasan/Financiera Comultrasan - Cotizacion de Alcance.pdf`
  y `cotizaciones/comultrasan/Financiera Comultrasan - Cotizacion.xlsx` (copia de la plantilla
  maestra con las demás hojas de clientes eliminadas antes de trabajar sobre ella).
- **Pendiente para el usuario**: validar los días estimados por especialidad en el XLSX (no
  fueron confirmados línea por línea con Comultrasan, solo el desglose de alcance del PDF);
  decidir si se comparte el logo de Comultrasan para agregarlo al PDF.
