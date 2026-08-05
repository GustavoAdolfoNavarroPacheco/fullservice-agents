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
