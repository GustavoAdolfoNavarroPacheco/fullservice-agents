---
name: enriquecimiento-datos-empresa
description: Completa cada empresa candidata con ubicación, número de empleados, facturación anual y utilidad neta, citando siempre fuente y fecha internamente, sin inventar cifras.
---

# Enriquecimiento de Datos de Empresa

## Cuándo usar esta skill

Para cada empresa candidata que `busqueda-web-empresas` entregue, antes de
que pase a `generacion-listado-resultados`.

## Entradas

- Razón social, sitio web y fuente inicial de la empresa candidata.
- Criterio del formulario de intake (para confirmar que Ubicación, Tamaño,
  Número de empleados y Facturación anual calzan con lo pedido).

## Procedimiento

1. Confirmar la **razón social** exacta (nombre legal registrado), priorizando
   RUES/Cámara de Comercio sobre el nombre comercial si difieren.
2. Confirmar **Ubicación** (ciudad/sede) desde el sitio oficial de la
   empresa o el registro mercantil.
3. Buscar **Número de Empleados**: sitio oficial, prensa, o vacantes/reportes
   públicos que den un rango o cifra estimada.
4. Buscar **Facturación Anual** y **Utilidad Neta**: fuente primaria es la
   Superintendencia de Sociedades (SIREM) para empresas colombianas que
   reportan estados financieros — ver `enlaces-utiles.md`. Anotar el año
   fiscal de la cifra encontrada (puede no ser el año en curso).
5. Anotar la fuente (URL o medio) y la fecha real de la consulta para cada
   dato completado — esto no aparece en la tabla final, pero se guarda en el
   CSV interno para trazabilidad.
6. Si un dato no se encuentra con confianza razonable tras una búsqueda
   razonable, dejar el campo vacío — no completar con estimaciones no
   verificadas ni inferencias sin fuente, especialmente en Facturación
   Anual y Utilidad Neta.

## Reglas obligatorias

- **Cero invención de datos**, en particular de cifras financieras
  (Facturación Anual, Utilidad Neta) — son las más sensibles a inventar por
  error y las que más impactan una decisión comercial equivocada.
- No usar LinkedIn como fuente de enriquecimiento bajo ninguna circunstancia.
- No confundir la fecha de publicación/del estado financiero con la fecha
  de consulta — el CSV interno guarda ambas cuando difieren.
- No forzar una empresa a calzar con Tamaño/Número de empleados/Facturación
  si el dato real encontrado contradice el criterio del formulario — en ese
  caso, se descarta la empresa en vez de listarla igual.

## Salida

Ficha de empresa enriquecida (Fecha, Razón Social, Ubicación, Número de
Empleados, Facturación Anual, Utilidad Neta, Fuente interna), entregada a
`generacion-listado-resultados`.
