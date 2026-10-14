# Changelog del agente

Registro de cambios a la infraestructura/proceso de ContractPerfectionist (scripts, reglas de `CLAUDE.md`, estructura del repo). No confundir con `wiki/log.md`, que registra contratos generados/revisados, no cambios al agente mismo.

## [2026-07-14] Implementación de mejoras de flujo

A partir de una revisión general del repo (`Mejoras Sugeridas - ContractPerfectionist.md`), tras generar un único contrato real (Colbeef, 2026-07-09) que sirvió de caso de prueba:

- **Generador reutilizable**: `scripts/build_contract.py` — ensambla el `.docx` sobre la plantilla corporativa, agrega líneas de firma con borde real, y corre gates de calidad (placeholders sin resolver, membrete/firma perdidos) antes de considerar un contrato listo para entrega. Reemplaza los scripts ad hoc (`scratch/build_contract.py`, `build_contract_v2.py`) que se usaron para Colbeef y que no habían quedado versionados.
- **Fichas de datos reutilizables**: `wiki/clientes/colbeef.md` (datos legales confirmados del cliente) y `wiki/datos-empresa.md` (datos legales propios de Campuslands, que se repiten en todo contrato) — antes documentados en `wiki/README.md` pero nunca poblados.
- **Checklist de verificación cruzada auditable**: `wiki/plantilla-verificacion-cruzada.md`, a copiar por cliente, para que el paso 4 del flujo deje rastro dato-por-dato en vez de una afirmación genérica.
- **Estados estandarizados** en `wiki/index.md` (`Borrador` / `Pendiente revisión legal` / `Pendiente firma` / `Firmado`).
- **Historial de versiones del Contrato Madre** en `wiki/glosario-clausulas.md`, con entrada inicial de línea base.
- **Convención de nombres para revisiones y otrosí** en `CLAUDE.md` (antes solo cubría el archivo original).
- **Reorganización de `recursos/`**: assets de marca movidos a `recursos/marca/`; se agregó `.gitignore` para excluir artefactos temporales de conversión/inspección.
- **Reglas nuevas en `CLAUDE.md`** (8 y 9): gate de entrega obligatorio (`build_contract.py check`) y nota de confidencialidad sobre datos de clientes versionados en git.

Motivo: el único contrato generado hasta ahora dependió por completo de trabajo manual no repetible (scripts en `scratch/` nunca commiteados, verificación visual vía conversión a PDF, fichas de cliente documentadas pero vacías). Este cambio busca que el segundo contrato — y todos los siguientes — reutilicen esa infraestructura en vez de rehacerla.
