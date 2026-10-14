---
name: matriz-cumplimiento
description: Construye la matriz de cumplimiento requerimiento × respuesta × origen a partir del inventario de requerimientos del análisis documental. Es el gate de "cero requerimientos omitidos" y se llena ANTES de redactar la propuesta técnica.
---

# Matriz de Cumplimiento

## Cuándo usar esta skill

**Inmediatamente después de cerrar el análisis documental y antes de redactar la
propuesta técnica.** Construir la matriz primero fuerza a diseñar la solución
contra la lista completa de requerimientos, en vez de redactar una propuesta y
después descubrir qué quedó afuera.

También se re-ejecuta cuando llega una adenda o aclaración nueva que agrega o
modifica requerimientos.

No usar esta skill para: verificar la propuesta al final (eso es la verificación
cruzada, que *consulta* esta matriz).

## Entradas

- `licitaciones/<slug>/00 - Analisis Documental.md` — el inventario de
  requerimientos numerados con sus citas.
- Las respuestas del usuario a las ambigüedades consultadas.

## Procedimiento

### 1. Una fila por requerimiento, sin excepciones

Se traslada **todo** el inventario del análisis documental: funcionales, no
funcionales, técnicos, de plazo, administrativos, de entregables y de operación.
Ninguna categoría se omite por "no ser desarrollo".

### 2. Columnas de la matriz

| Columna | Contenido |
|---|---|
| **ID** | Identificador estable (`RF-01`, `RNF-07`, `PLZ-03`) |
| **Requerimiento** | Texto resumido pero fiel al documento |
| **Origen** | Cita exacta (`RFP §4.2`, `Aclaración P-17`, `Anexo 3 p.12`) |
| **Obligatorio / Deseable** | Según lo declare el propio documento |
| **Cumplimiento** | `Cumple` / `Cumple parcialmente` / `No cumple` / `No aplica` |
| **Cómo se cumple** | Descripción concreta de la solución, sin lenguaje vago |
| **Módulo / sección** | Dónde se responde en la propuesta técnica (`M3`, §5.2) |
| **Esfuerzo asociado** | Referencia a la línea de la estimación de horas, o `N/A` con razón |
| **Observaciones** | Supuestos, dependencias o riesgos de ese requerimiento |

### 3. Reglas de llenado

- **`Cumple parcialmente` y `No cumple` se declaran, no se disimulan.** Un
  requerimiento que Campuslands no puede cumplir debe estar visible para que el
  usuario decida: negociarlo por aclaraciones, buscar un aliado, o desistir del
  proceso. Ocultarlo es un incumplimiento contractual diferido.
- **`No aplica` siempre lleva razón escrita.**
- **Nada de respuestas vagas.** "Se contempla en la solución" no es cumplimiento;
  hay que decir qué componente lo resuelve y cómo.
- Todo requerimiento marcado `Cumple` debe tener **módulo/sección** y **esfuerzo
  asociado** (o justificación explícita de por qué no requiere esfuerzo).
- Un requerimiento que se descompone en varias funcionalidades puede referenciar
  varias líneas de estimación; se listan todas.

### 4. Formato del archivo

`licitaciones/<slug>/01 - Matriz de Cumplimiento.xlsx`, con las convenciones de
`wiki/marca-campuslands.md` §5: Arial, encabezados con relleno navy y texto blanco,
filtros activos, y una hoja por categoría de requerimiento si el volumen lo
justifica.

### 5. Resumen de cobertura

Al cierre del archivo (hoja o bloque de resumen):

```
Total de requerimientos                 : N
  Cumple                                : n1
  Cumple parcialmente                   : n2   ← revisar con el usuario
  No cumple                             : n3   ← revisar con el usuario
  No aplica                             : n4
Requerimientos obligatorios no cumplidos: n5   ← BLOQUEANTE si n5 > 0
```

**Si hay requerimientos obligatorios en `No cumple`, se reporta al usuario antes de
avanzar.** Puede significar que el proceso no es viable para Campuslands tal como
está planteado.

## Salidas

- `licitaciones/<slug>/01 - Matriz de Cumplimiento.xlsx`
- Reporte al usuario de los requerimientos en `Cumple parcialmente` / `No cumple`.
- Actualización de `wiki/licitaciones/<slug>.md` con el resumen de cobertura.

## Errores a evitar

- Marcar todo como `Cumple` para que la matriz "se vea bien". La matriz es una
  herramienta de decisión, no un documento de ventas.
- Omitir requerimientos administrativos, de entregables o de operación.
- Dejar filas sin cita de origen.
- Construir la matriz después de la propuesta técnica: invierte el control y
  garantiza omisiones.
- Responder con lenguaje genérico que no identifique el componente que cumple el
  requerimiento.
