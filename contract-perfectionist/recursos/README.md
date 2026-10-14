# Recursos

Insumos de entrada. El agente **solo** toma datos de aquí (o de lo que el usuario aporte directamente en la conversación) — nunca inventa.

- `marca/` — assets de identidad corporativa de Campuslands (logos, isotipo, favicon, brandbook, brief). Referencia visual únicamente — no son insumo de datos para redactar cláusulas; el membrete ya está integrado en `Contrato - Plantilla Base.docx`.
- `contrato-madre/` — plantilla(s) maestra(s) de la empresa. Fuente de la arquitectura de cláusulas y de las cláusulas estándar de protección (propiedad intelectual, confidencialidad, garantías, terminación, fuerza mayor, cláusula penal). Si hay varias versiones, la más reciente es la vigente salvo indicación contraria del usuario.
- `Contrato - Plantilla Base.docx` — **plantilla de diseño corporativo** (no confundir con el Contrato Madre, que es de contenido legal). Trae el membrete de Campuslands ya integrado en el encabezado de sección (logo, franjas azul/verde, dirección en el pie) y los márgenes/tipografía correctos. Todo `.docx` de contrato final se construye abriendo este archivo como base, nunca desde un documento en blanco.
- `alcances/<cliente-slug>/` — documento(s) de alcance funcional del proyecto para ese cliente (qué se construye, módulos, integraciones, exclusiones).
- `cotizaciones/<cliente-slug>/` — cotización aprobada del proyecto (valor, forma de pago, cronograma/fases).

Un contrato nunca se redacta sin que existan al menos un archivo de alcance y uno de cotización para ese `<cliente-slug>`, además del contrato madre vigente.
