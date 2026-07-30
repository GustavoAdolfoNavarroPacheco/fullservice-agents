# Bitácora

Registro cronológico de contratos generados o revisados. Formato: `## [YYYY-MM-DD] <cliente> | <acción>`.

<!-- Ejemplo:
## [2026-07-09] casa-blanca | contrato generado
Contrato de desarrollo de software con IA a la medida, a partir de Alcances v1 y Cotización aprobada del 2026-05-12.
-->

## [2026-07-09] colbeef | contrato generado
Contrato de prestación de servicios de desarrollo e implementación de un sistema de automatización operativa con IA (gestión de casos, agente de voz/WhatsApp, integraciones ERP/correo/API) para Colbeef S.A.S. Redactado sobre la arquitectura y cláusulas de protección del Contrato Madre vigente, con una variación validada por el usuario: cesión de código fuente y derechos patrimoniales a EL CLIENTE (en vez de la licencia de uso estándar). Alcance funcional tomado de la cotización interna de costeo (`recursos/cotizaciones/colbeef/`); valor ($80.000.000 COP + IVA), forma de pago (40/20/20) y plazo (5 meses con Fase 0) confirmados por el usuario a partir de un contrato de referencia previo (`recursos/alcances/colbeef/`), usado únicamente como insumo de datos, no copiado como plantilla. Pendiente: fecha de firma (dejada en blanco) y revisión legal externa antes de enviar a firma.

## [2026-07-30] colbeef | verificación cruzada retroactiva + datos.json

A pedido del usuario (auditoría general del monorepo), se completaron los dos artefactos de trabajo que faltaban desde la generación original del contrato (2026-07-09), hecha con scripts ad hoc anteriores a `scripts/build_contract.py`: `contratos/colbeef/datos.json` (reconstrucción del contenido del `.docx` en el esquema JSON, solo para registro — no se usó para regenerar el archivo) y `contratos/colbeef/verificacion-cruzada.md` (comparación dato por dato contra la referencia y la cotización interna).

La verificación cruzada encontró que el contrato entregado difiere de `recursos/alcances/colbeef/Referencia - Contrato previo Colbeef...pdf` en varios puntos de protección contractual: garantía de 90 días sin pólizas (la referencia exigía 4 pólizas: cumplimiento, buen manejo de anticipo, calidad, RC extracontractual), cláusula penal del 10% en vez de 20%, y ausencia de cláusula de no competencia. No se pudo determinar si esta simplificación fue una decisión de negociación deliberada u una omisión — queda como pendiente para que el usuario lo confirme antes de la firma definitiva (ver `wiki/clientes/colbeef.md`, que ya anotaba "revisión legal externa" como pendiente).

También se detectó, de paso, que `recursos/cotizaciones/colbeef/Cotizacion - Colbeef SAS.xlsx` contiene hojas con datos comerciales de otros clientes (Bairós, Aleja Hooy, Rápido San Pedro, Cajasan) en el mismo archivo — contradice la regla de no mezclar información entre clientes. No se modificó (es de solo lectura); reportado al usuario para su decisión.
