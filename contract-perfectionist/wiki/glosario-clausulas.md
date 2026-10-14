# Glosario de cláusulas estándar

Catálogo de categorías de cláusulas que suelen aparecer en los contratos de la empresa, según la arquitectura del Contrato Madre (`recursos/contrato-madre/`). Sirve como checklist al redactar un contrato nuevo — el **contenido** de cada cláusula sale siempre de los Alcances/Cotización del proyecto, no de este glosario.

| Categoría | Qué cubre | Origen típico del contenido |
|---|---|---|
| Partes y consideraciones | Identificación legal de ambas partes, contexto y motivación del acuerdo | Datos legales del cliente (a confirmar) + resumen de la propuesta/cotización |
| Objeto | Qué se compromete a entregar el contratista | Alcances |
| Naturaleza jurídica | Tipo de obligación (medio vs. resultado), qué garantiza y qué no | Contrato Madre (estándar de la empresa) |
| Alcance funcional | Módulos, funcionalidades, integraciones incluidas y excluidas | Alcances |
| Cronograma y fases | Plazos, hitos, fases de ejecución | Cotización / Alcances |
| Valor y forma de pago | Monto total, hitos de pago, moneda | Cotización |
| Mantenimiento y soporte | Condiciones post-entrega, renovación, qué incluye/excluye | Cotización (si aplica) + Contrato Madre |
| Infraestructura y consumo | Quién asume costos de infraestructura/servicios y por cuánto tiempo | Cotización / Alcances |
| Garantía | Duración y alcance de la garantía post-entrega | Contrato Madre + condiciones específicas de la cotización |
| Obligaciones de cada parte | Qué debe hacer el contratista y qué debe hacer el cliente | Contrato Madre + particularidades del proyecto |
| Aceptación de entregables | Cómo y en qué plazo se valida cada entrega | Contrato Madre |
| Propiedad intelectual / licencia de uso | Titularidad del software, alcance de la licencia otorgada | Contrato Madre (estándar de la empresa) |
| Datos personales | Roles (responsable/encargado) y compromisos de tratamiento | Contrato Madre + normativa aplicable |
| Confidencialidad | Alcance y vigencia de la obligación de reserva | Contrato Madre |
| Servicios de terceros | Deslinde de responsabilidad por proveedores externos | Contrato Madre + terceros mencionados en Alcances |
| Suspensión y terminación | Causales y efectos de suspender o terminar el contrato | Contrato Madre |
| Fuerza mayor | Deslinde por eventos externos | Contrato Madre |
| Cláusula penal | Consecuencia económica de incumplimiento grave | Contrato Madre (validar % o monto con el usuario si cambia) |
| Vigencia | Duración total del acuerdo | Cotización (cronograma) + condiciones de mantenimiento |
| Ley aplicable y controversias | Jurisdicción y mecanismo de resolución de conflictos | Contrato Madre |
| Firmas | Cierre y validez de firmas electrónicas | Contrato Madre |

## Historial de versiones — Contrato Madre

Registro de cambios a `recursos/contrato-madre/Contrato Madre - Plantilla Base.docx` (la plantilla de contenido legal, no la de diseño). Cada vez que se reemplace ese archivo, agregar una entrada aquí con fecha, qué cambió y por qué — para poder saber si un contrato ya generado quedó desactualizado respecto al estándar vigente.

- **[2026-07-09] Versión inicial registrada.** Primera versión del Contrato Madre incorporada al repositorio (commit `03c44e5`). No hay historial de cambios previo a esta fecha; se toma como línea base para futuras comparaciones.

## Ajustes validados por proyecto

_(Cuando un proyecto requiera una variación reutilizable de una cláusula estándar, y el usuario la valide, documentarla aquí con fecha y motivo.)_

- **[2026-07-09] Colbeef — Propiedad intelectual: cesión en vez de licencia.** El estándar del Contrato Madre otorga solo licencia de uso (sin ceder código fuente ni derechos patrimoniales). Para Colbeef, el usuario validó que la propiedad del código y los derechos patrimoniales se **ceden** a EL CLIENTE, según lo pactado específicamente para ese proyecto. Motivo: acuerdo comercial propio del cliente, confirmado por el usuario — no es un cambio de política general de la empresa. Al redactar contratos futuros, seguir usando licencia de uso por defecto salvo que el usuario confirme cesión explícitamente para ese cliente.
