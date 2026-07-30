# Catálogo de la Wiki (Agente Desarrollador de Cotizaciones)

Este es el índice de la documentación que mantengo para desarrollar cotizaciones y alcances técnicos para Campuslands Full Service.

## Archivos Principales

*   [Flujo de Trabajo](flujo-trabajo.md): Paso a paso para la creación de PDF de alcance y XLSX de cotización.
*   [Perfil de Usuario](perfil-usuario.md): Rol, reglas fundacionales y expectativas del agente.
*   [Marca Campuslands](marca-campuslands.md): Directrices de identidad visual, estilo editorial y uso de marca en las cotizaciones (PDF).
*   [Bitácora (Log)](log.md): Registro cronológico de todas las cotizaciones creadas o modificadas.

*(Nota: Adicionalmente, el agente debe seguir el mapeo de la plantilla XLSX y la estructura base tal como se define en `CLAUDE.md` de la raíz del proyecto).*

## Cotizaciones y estimaciones generadas

*   `cotizaciones/compumax/` — Compumax Computer S.A.S.
*   `cotizaciones/multinal/` — Multinal S.A.S. (Escenarios B y C, sin costeo).
*   `cotizaciones/avicampo/` — Avícola el Madroño S.A. (Avicampo).
*   `cotizaciones/la-esmeralda/` — La Esmeralda.
*   `cotizaciones/campus-land-sas-bic/` — Campus Land SAS BIC.
*   `cotizaciones/carnes-casa-blanca/` — Carnes Casa Blanca SAS (TalentoHub).
*   `cotizaciones/ipa-pr10598/` — **Caso especial**: no es una cotización a un cliente externo, sino una
    **estimación interna de Campuslands** para el RFP PR10598 de IPA ("Una Visa por un Sueño"), 26 módulos
    (CT-01..CT-23 + M0 transversal). Reconciliada 2026-07-29 contra el expediente final de licitación
    (matriz de cumplimiento de 70 requerimientos + estimación de horas de BiddingAgent) — TOTAL $120.650.331
    COP. La portada del PDF conserva su framing original ("bid conjunto con Aurena AI") a pedido explícito
    del usuario, aunque el negocio ya decidió licitar en solitario. Ver detalle en `wiki/log.md` (entradas
    2026-07-27 y 2026-07-29).
*   `cotizaciones/gaspais-chilco/` — Gaspaís Chilco (GAS PAÍS) — Plataforma Integral de Gestión HSE-SST,
    9 módulos (8 funcionales + arquitectura/seguridad/servicio), 1.500 usuarios incluyendo contratistas.
