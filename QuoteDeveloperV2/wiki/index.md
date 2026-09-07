# Índice de la wiki — Agente Desarrollador de Cotizaciones

Catálogo de todas las páginas de la wiki, organizado por categoría. Se actualiza
en cada ingest/ajuste (ver "Mantener la wiki (Lint)" en `CLAUDE.md`).

## Perfil y flujo de trabajo

- [perfil-usuario.md](perfil-usuario.md) — Rol del agente, regla de oro de veracidad (cero invención) y regla de granularidad fiel (cardinalidad libre de funcionalidades).

## Marca y diseño

- [marca-campuslands.md](marca-campuslands.md) — Identidad de marca general de Campuslands (paleta oscura, tipografía Playfair/Montserrat/Poppins) + §5: sistema de diseño vigente para PDFs de cotización (paleta clara, grid, jerarquía Módulo→Submódulo→Funcionalidad).
- [diseno-pdf-cotizacion.md](diseno-pdf-cotizacion.md) — Espejo consultable de `marca-campuslands.md` §5: paleta exacta, layout de grid, tipografía Arial 11/10/10, reglas de precios en el PDF.

## Plantilla XLSX

- [plantilla-xlsx.md](plantilla-xlsx.md) — Mapeo exacto de la plantilla maestra: filas transversales fijas (2-5), jerarquía flexible L/M/N desde la fila 8, columnas de días por especialidad (B:K), excepciones de la barra gris (Y y R), y verificación obligatoria con `recalc.py`.

## Bitácora

- [log.md](log.md) — Registro cronológico de builds, ajustes y lint de la wiki.
- [entrada-log-sugerida.md](entrada-log-sugerida.md) — Borrador histórico de la entrada de log del ajuste de jerarquía flexible (2026-08-05), incorporado como primera entrada de `log.md`.

## Cotizaciones entregadas (resumen)

- **Marval — Módulo de Agente de IA** (2026-08-14): arquitectura de orquestador + agentes de dominio (Gestión Humana, Soporte de Proyectos, Entregas Digitales, expansión a 5 agentes futuros) + canal Teams, cotizada en dos escenarios paralelos de motor de IA. Ver entrada de log para detalle. `cotizaciones/marval/opcion-a-api/` (API externa, $72.134.483 COP) y `cotizaciones/marval/opcion-b-selfhosted/` (self-hosted, $83.247.225 COP).
- **Financiera Comultrasan** (2026-08-05): asistente conversacional Orbit, Canales Digitales. `cotizaciones/comultrasan/`.
- **Alcaldía Municipal de Girón** (2026-08-06): portafolio de 13 proyectos independientes bajo `cotizaciones/giron/<slug-proyecto>/` — ver resumen con TOTAL por proyecto en `log.md`.
- **Cotizacion_1 — Plataforma de Gestión Territorial (Bucaramanga)** (2026-08-19): registro de líderes y personas, control de duplicados, mapa territorial, dashboard, WhatsApp; sin nombre de cliente. `cotizaciones/cotizacion_1/`, $53.093.652 COP.
- **Relia — Gestión de Cartera y Cobranza** (2026-08-19): saldo a favor, acuerdos de pago, notas crédito Siigo, campañas de cobro, portal del deudor; sin nombre de cliente (fuente menciona a Campuslands, omitido a pedido del usuario). `cotizaciones/relia/`, $14.347.697 COP.
- **La Esmeralda — Sistema de gestión de planta de producción láctea/alimentos** (2026-08-31): 11 módulos (seguridad/usuarios, datos maestros, cestillos y canastillas, materias primas, pedidos y programación, producción y rendimiento, bodega y despachos, incidencias y desperdicios, empaques/compras/proveedores, alertas/reportes/integración, requisitos no funcionales), XLSX ya provisto por el usuario con estructura L/M/N no estándar (precio en M) respetada tal cual. `cotizaciones/la-esmeralda/`, $89.042.874,90 COP — actualización de una cotización anterior (repo predecesor `QuoteDeveloper`) que bajó el AIU de 40% a 10%.
- **Miami Aqua Tours — Auditoría técnica, mejoras de sitio y tracking de conversiones** (2026-09-04): sitio estático en Cloudflare Pages (sin WordPress en el dominio principal, sí en un subdominio separado) con reservas vía widgets de Bókun. 4 módulos: auditoría técnica/rendimiento/seguridad, mejoras de diseño front-end, auditoría y mejoras del WordPress del subdominio, y analítica/tracking de conversiones (GTM, GA4, AnyTrack, persistencia de atribución UTM y registro de conversión sobre reservas de Bókun). Sin contacto nombrado del cliente en el brief — se omitió el bloque de contacto del PDF. `cotizaciones/miami-aqua-tours/`, $15.560.763 COP.
- **Miami Aqua Tours v2 — Implementación de hallazgos del análisis técnico** (2026-09-04): segunda cotización para el mismo cliente, esta vez basada en un documento de análisis técnico mucho más detallado y específico (líneas de código, evidencia de consola, tablas de hallazgos) que reemplaza al brief de alto nivel de la v1 — no es una revisión de la v1, es un alcance nuevo de implementación de los hallazgos. 5 módulos: auditoría técnica y unificación de arquitectura (WordPress/FareHarbor heredado vs. capa generada por `gen.py`), mejoras de frontend y experiencia de usuario, rendimiento y velocidad, seguridad y buenas prácticas, y analítica/tracking de conversiones (GTM, GA4, persistencia de atribución UTM, endpoint server-side por webhook de Bókun, AnyTrack) — 48 funcionalidades en 15 submódulos. El submódulo de integración con Bókun lleva un comentario de celda (Excel) advirtiendo que depende de que Bókun confirme soporte de webhook/API con acceso administrativo a la cuenta (el propio documento fuente lo deja como pendiente de validar). Solo XLSX entregado, sin PDF, a pedido explícito del usuario. `cotizaciones/miami-aqua-tours-v2/`, $30.744.516 COP.
