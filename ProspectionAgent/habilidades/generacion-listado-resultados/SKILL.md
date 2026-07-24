---
name: generacion-listado-resultados
description: Consolida las empresas enriquecidas de un lote en una tabla Markdown con las 6 columnas fijas (Fecha, Razón Social, Ubicación, Número de Empleados, Facturación Anual, Utilidad Neta) y un CSV, y las entrega al usuario como cierre de la búsqueda.
---

# Generación de Listado de Resultados

## Cuándo usar esta skill

Al consolidar todas las empresas enriquecidas de un lote de búsqueda, o al
cierre de la sesión si el usuario pide un corte parcial.

## Entradas

- Fichas de empresa enriquecidas por `enriquecimiento-datos-empresa`.
- Criterio del formulario de intake original (los 6 campos).

## Procedimiento

1. Consolidar todas las fichas en una tabla Markdown con **exactamente**
   estas columnas, en este orden:

   | Fecha (YYYY-MM-DD) | Razón Social | Ubicación | Número de Empleados | Facturación Anual | Utilidad Neta |
   |---|---|---|---|---|---|

2. **Fecha** usa la fecha real de ejecución de la búsqueda (no la del dato
   financiero, que puede ser de un año fiscal anterior — esa distinción va
   en la fuente interna, no en esta columna).
3. Anteponer un resumen breve: criterios del formulario usados, empresas
   encontradas vs. Número de Empresas solicitado, y fecha real de ejecución.
4. Debajo de la tabla, agregar una sección **Fuentes** con la fuente/URL de
   cada fila (numerada o por nombre de empresa), para mantener trazabilidad
   sin ensuciar las 6 columnas principales.
5. Guardar el contenido completo (incluida la columna de fuente) como
   `prospeccion/<slug-lote>/01-empresas-encontradas.csv`, usando un slug
   descriptivo del criterio (ej. `constructoras-bogota-2026-07-23`).
6. No mezclar en una misma tabla/CSV empresas de criterios de búsqueda
   distintos sin distinguirlos claramente (usar lotes separados).
7. Entregar la tabla al usuario y preguntar si quiere: ampliar la búsqueda,
   repetir el formulario con otros criterios, o pasar el listado a
   Explorador de Campus (`IntelligenceCommercial/`) para la fase de contactos.

## Reglas obligatorias

- La tabla entregada al usuario tiene **exactamente 6 columnas** — no
  agregar Sector, Sitio Web u otras columnas fuera de este spec, aunque se
  hayan usado como criterios de búsqueda (esos van solo en el resumen inicial).
- No inventar ni completar filas con datos no verificados — usar exactamente
  lo que entregó `enriquecimiento-datos-empresa`; campos no encontrados van
  vacíos, no con "N/A" inventado como si fuera un dato confirmado.
- Formato de fecha siempre `YYYY-MM-DD`.
- El slug del lote debe reflejar el criterio real usado, para que sea
  identificable meses después sin abrir el archivo.

## Salida

Tabla en Markdown de 6 columnas + sección de fuentes, entregada al usuario,
más el archivo `prospeccion/<slug-lote>/01-empresas-encontradas.csv`
guardado en disco (con columna de fuente adicional para trazabilidad interna).
