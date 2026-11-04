# 01 · Inventario de fuentes (etapa 1 · Recepción)

**Proyecto:** Servicio inteligente de cobro persuasivo y fiscalización tributaria con IA (Industria y Comercio — ICA)
**Cliente:** Alcaldía Municipal de Girón (Santander) · **Proveedor:** Campuslands S.A.S. BIC · Full Service
**Slug:** `giron-cobro-persuasivo-ica` · **Recibido:** 2026-10-29 · **Tipo de documento a producir:** alcance funcional para el cliente (DEC-003)

## Fuentes recibidas

| # | Fuente | Fecha | Estado | Observaciones |
|---|---|---|---|---|
| F1 | `fuentes/Propuesta_Alcaldia_Giron_Campuslands_VF.docx` — «Propuesta comercial y técnica» con carta de presentación, 12 secciones y anexo técnico integral | **28 de octubre de 2026** (el bloque de firma dice «veintitrés (29) días del mes de octubre de 2026») | **Vigente**: confirmado por el usuario el 2026-10-29 (DEC-001) | Documento de Campuslands, **sin firma ni aceptación** de la Alcaldía. Se declara «actualizado según acuerdos de la mesa técnica», pero **no se aportan las actas**. Cédula del alcalde en blanco. |
| F1-t | `fuentes/…texto-extraido.txt` | — | Copia de trabajo | Extracción de texto del F1 (todas las secciones, tablas y listas de verificación). No es fuente independiente. |

Contenido de F1 revisado íntegramente: texto, 12 tablas, listas de insumos, encabezados y pies. Las imágenes del .docx son solo el membrete. El marcador
«[embedded content: arquitectura · on-premise y servicios en la nube]» (§ Arquitectura del servicio) es **texto literal**: el **diagrama de arquitectura no está** en el documento.

## Fuentes que se mencionan pero NO se aportaron

| # | Fuente mencionada | Dónde se cita en F1 | Por qué importa |
|---|---|---|---|
| X1 | Actas de la **mesa técnica** («acuerdos de la mesa técnica») | Anexo técnico (§12, encabezado) | Es la única base declarada de los ajustes de capacidad, conectividad y condiciones comerciales; sin ella no se puede citar nada como acordado con el cliente |
| X2 | **Requerimiento de la Alcaldía** (fuentes de fiscalización y campos) | Fase 1 · Fiscalización | Define las fuentes, los campos del listado de omisos y la columna EMPLAZAR |
| X3 | **Cotización / estudio de costos** de Campuslands | §9 (propuesta económica) | Regla 12: los datos comerciales deben cuadrar con la cotización aprobada; la propuesta no desglosa el fee |
| X4 | **Estudios previos / análisis del sector** de la Alcaldía | §9.5 | La razonabilidad del precio «deberá sustentarse» en ellos |
| X5 | **Formato de creación de clientes** de Campuslands; **formato de registro de visita** de la Alcaldía; **procedimientos escritos** de cobro y fiscalización | §10; Fase 3 · Gestión de visitas; Insumos | Insumos que alimentan campos, reglas y flujo |
| X6 | **Concepto jurídico** (Ley 2300 de 2023, datos personales) y **TRD** de retención de grabaciones | Insumos; Responsabilidades | Condiciona horarios, frecuencia, grabación y retención |
| X7 | **Informe técnico anexo** | §1, §9.6 | La propuesta lo trata como anexo propio: está en el mismo .docx (§12), no como archivo separado |

## Alcance de este expediente
- Fuente única: **F1**. Todo dato extraído queda como **«PROPUESTO por F1»** (oferta de Campuslands, no aceptada por la Alcaldía) salvo que el usuario confirme otra cosa. No se registra nada como CONFIRMADO con el cliente.
- El usuario confirmó (2026-10-29) que no dispone por ahora de X1 (actas), X3 (cotización) ni X2 (requerimiento): DEC-002.
