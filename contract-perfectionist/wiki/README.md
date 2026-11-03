# Wiki

Conocimiento acumulado entre contratos. No es fuente de datos del proyecto (eso vive en `recursos/`) — es memoria de trabajo del agente para mantener consistencia entre contratos.

- `index.md` — catálogo de clientes/contratos generados, con una línea de resumen por cada uno. Se actualiza en cada entrega.
- `log.md` — bitácora cronológica: cada vez que se genera o revisa un contrato, se agrega una entrada.
- `glosario-clausulas.md` — catálogo de cláusulas estándar reutilizables (derivadas del Contrato Madre y de ajustes validados por el usuario en contratos anteriores), con su propósito y en qué casos varían.
- `clientes/<cliente-slug>.md` — ficha por cliente: datos legales ya confirmados (razón social, NIT, representante legal), y cualquier condición particular acordada para ese cliente, para no tener que re-preguntar en contratos futuros del mismo cliente.
- `datos-empresa.md` — datos legales propios de Campuslands S.A.S. BIC (NIT, representante legal, domicilio) que se repiten en todos los contratos como CONTRATISTA. Siempre confirmar vigencia con el usuario antes de reutilizar.
- `plantilla-verificacion-cruzada.md` — checklist a copiar en cada `contratos/<cliente>/` para dejar rastro auditable de que el borrador se contrastó dato por dato contra Alcances y Cotización (paso 4 del flujo).

Antes de redactar un contrato nuevo, revisar `index.md`, `datos-empresa.md` y, si existe, la ficha del cliente en `clientes/` para no repetir preguntas ya resueltas.
