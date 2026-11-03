# 05 · Control de calidad previo a la entrega (manual §8)

Proyecto: Alcaldía de Girón — cobro persuasivo con IA (ICA) · Documento: v0.1 (borrador) · Fecha: 2026-10-29
Archivo: `entrega/Alcance Funcional - Alcaldía de Girón - v0.1 - 2026-10-29.docx` (38 páginas; tabla de contenido ya generada). Estructura: portada · carta de presentación · tabla de contenido · contenido · aprobación y firmas. Sin la palabra «borrador» dentro del documento (el estado se lleva aquí y en la wiki).
Cada punto lleva evidencia. Un punto sin evidencia no se marca.

| ✔ | Control | Evidencia / observación |
|---|---|---|
| [ ] | Cada módulo tiene identificador, límite, entradas, salidas y aceptación | **Parcial.** RF-001…RF-015 (= MOD-01…15) con ficha uniforme: identificador, entradas, flujo, salidas y dependencias presentes. Criterios de aceptación **medibles** declarados como «se definen en el levantamiento de la Fase 1 (RF-001)» en todas las fichas, sin marca de pendiente (ajuste del usuario); límites cuantitativos ausentes (PEN-002, PEN-003, PEN-006, PEN-019) |
| [ ] | Los datos comerciales coinciden con la versión aprobada de la propuesta | **No verificable.** No se aportó cotización (DEC-002). $50.000.000 y $540.000.000 transcritos de la propuesta; retenciones, vigencia presupuestal y desglose pendientes (PEN-012) |
| [ ] | El cronograma contempla dependencias y condiciones de inicio | **Parcial.** §11.1 lista los 14 insumos de la Alcaldía; fecha, responsable y efecto de un retraso pendientes (PEN-005); qué opera en enero pendiente (PEN-004); dependencia F1/F2 y recaudo F3 señaladas en §3.4 |
| [x] | Las funcionalidades futuras no aparecen como entregables actuales | Fase 4 solo en §3.3 (tabla «Ampliación del servicio»); la tabla de entregables (§10) no incluye ningún módulo de Fase 4; RF-012 y RF-014 aclaran que acuerdos y conciliación no están incluidos |
| [ ] | Soporte y garantía distinguen errores de nuevas solicitudes | **No.** §13 recoge «control de cambios» para lo ajeno al alcance, pero SLA y garantía están pendientes (PEN-007) |
| [x] | Costos recurrentes y de terceros identificados o marcados como pendientes | §6.2 y §14.2: servicios incluidos en el fee identificados; APIs de Cámara de Comercio, geocodificación y volumen de consumos marcados `[PENDIENTE DE VALIDACIÓN]` (PEN-002, PEN-010) |
| [x] | Fuentes, decisiones y versiones trazables | Cada ficha cita sección de la propuesta; estados PROPUESTO/PENDIENTE en todas las tablas; Anexo E (DEC-001, 002, 003, 008); `trabajo/02-matriz-informacion.md` mapea hechos → fuente |
| [ ] | Sin contradicciones entre resumen, tablas, entregables y exclusiones | **No resueltas.** Las contradicciones de la propuesta se muestran con ambas versiones (exclusiones §3.2, respaldos §6.3, cascada F1/F2 §3.4, cuenta WhatsApp §6.1, consumos §6.2) pero ninguna está decidida (CON-001…CON-008) |
| [x] | Resumen de pendientes entregado; se indica borrador o apto para revisión final | §1.1 y §15.3 del documento; `03-pendientes.md` (25 pendientes, validaciones por responsable); estado: **Borrador** |

**Pendientes BLOQUEANTES abiertos:** 12 (PEN-002 a PEN-013) → el documento es **solo borrador**; no puede declararse «apto para revisión final» ni «listo para firma».
**Revisiones solicitadas:** técnica [ ] · comercial [ ] · jurídica [ ] (PI, datos personales, garantías) — aún no solicitadas a los responsables.
**Estado resultante:** Borrador.

## Verificación visual (2026-10-29)
`scripts/previsualizar.py` (LibreOffice → PDF/PNG): 38 páginas revisadas a la vista en hojas de contacto y de cerca las modificadas.
Corregido tras verlas: columna «Estado» que partía «PROPUESTO», filas y notas huérfanas en páginas casi vacías, matriz del Anexo B con columnas angostas, figura de arquitectura (etiquetas pisadas).
Tabla de contenido generada con los números de página de LibreOffice; sin revisar el aspecto exacto en Word (el render es de LibreOffice; los saltos de página pueden variar).
Única página con espacio libre: la 37 (56 % ocupada), porque el apartado de firma, que no se parte, no cabe en lo que resta y va solo en la 38.
