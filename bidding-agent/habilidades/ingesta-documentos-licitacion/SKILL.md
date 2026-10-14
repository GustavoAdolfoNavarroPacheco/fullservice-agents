---
name: ingesta-documentos-licitacion
description: Verifica que estén los 4 documentos oficiales de la licitación (RFP, aclaraciones, modelo de costos oficial, modelo de costos de cotización), los lee completos en orden, extrae y numera todos los requerimientos con su cita de origen, y produce el análisis documental con contradicciones, supuestos y ambigüedades a consultar.
---

# Ingesta de Documentos de Licitación

## Cuándo usar esta skill

**Siempre, como primer paso de toda licitación nueva**, antes de que cualquier otra
skill se ejecute. También al recibir una adenda o un documento de aclaraciones
adicional sobre una licitación ya en curso (ahí se re-ejecuta el análisis de
contradicciones y se actualiza el inventario de requerimientos).

No usar esta skill para: retomar una licitación cuyo análisis documental ya está
cerrado y aprobado por el usuario (en ese caso se lee
`licitaciones/<slug>/00 - Analisis Documental.md` y
`wiki/licitaciones/<slug>.md`, en vez de re-analizar desde cero).

## Entradas

- Los cuatro documentos oficiales en `recursos/licitaciones/<slug-licitacion>/`:
  1. RFP
  2. Documento de aclaraciones / preguntas y respuestas
  3. Modelo de costos oficial de la empresa solicitante
  4. Segundo modelo de costos (el de cotización)
- El slug de la licitación (minúsculas, sin espacios ni tildes, con el
  identificador del proceso cuando exista).

## Procedimiento

### 1. Verificar los cuatro insumos

Listar el contenido de `recursos/licitaciones/<slug>/` e identificar qué documento
corresponde a cada uno de los cuatro roles. **Si falta alguno, detenerse y
preguntar al usuario** — no inferir el contenido de un documento ausente. Si el
usuario confirma que ese proceso no incluye alguno, registrarlo explícitamente en
el análisis y en `wiki/log.md`.

### 2. Leer los cuatro documentos completos, en orden

RFP → aclaraciones → modelo de costos oficial → modelo de costos de cotización.

**Nunca generar un entregable con una lectura parcial.** El análisis integral antes
de cualquier respuesta es la instrucción central del rol.

Para documentos no textuales, usar la herramienta adecuada según el formato (PDF,
DOCX, XLSX). Para los modelos de costos, mapear la estructura real de celdas,
columnas y fórmulas — no solo leer los encabezados.

### 3. Extraer y numerar todos los requerimientos

Un identificador estable por requerimiento, que se usará en todos los entregables:

| Prefijo | Categoría |
|---|---|
| `RF-nn` | Funcional |
| `RNF-nn` | No funcional (rendimiento, disponibilidad, seguridad, escalabilidad, usabilidad) |
| `TEC-nn` | Técnico (stack, integraciones, infraestructura, migración) |
| `PLZ-nn` | De plazo (fechas, hitos, entregables intermedios) |
| `ADM-nn` | Legal/administrativo (pólizas, certificaciones, experiencia acreditable) |
| `ENT-nn` | De entregables (documentación, capacitación, transferencia) |
| `OPS-nn` | De operación y soporte (SLA, mesa de ayuda, garantía, mantenimiento) |

Cada requerimiento lleva: identificador, texto (resumido pero fiel), **cita de
origen** (`RFP §4.2`, `Aclaración P-17`, `Anexo Técnico 3 p.12`), y si es
obligatorio o deseable según el propio documento.

### 4. Detectar contradicciones y aplicar la jerarquía documental

Contrastar el RFP contra las aclaraciones requerimiento por requerimiento. Para
cada contradicción: citar ambos documentos, aplicar la jerarquía (aclaraciones →
adendas → RFP → modelo de costos oficial → anexos) y registrar la lectura adoptada.

**Si la contradicción cambia materialmente el alcance o el precio, no resolverla
por cuenta propia: reportarla al usuario y preguntar.**

### 5. Producir `00 - Analisis Documental.md`

Con estas secciones:

1. **Datos del proceso** — entidad, identificador, objeto (transcrito literalmente),
   fechas clave, presupuesto oficial si se publica.
2. **Inventario de documentos recibidos** — los cuatro, con su archivo y fecha; y
   constancia de cualquier ausencia confirmada por el usuario.
3. **Inventario de requerimientos** — numerados, con cita de origen.
4. **Plazos y hitos** exigidos.
5. **Criterios de evaluación** y su ponderación.
6. **Estructura de los dos modelos de costos** — qué líneas y qué reglas exige cada
   uno, y dónde difieren entre sí.
7. **Contradicciones y precedencias** — cada una con ambas citas y la lectura
   adoptada.
8. **Supuestos** — cada uno con su justificación documental.
9. **Ambigüedades a consultar** — agrupadas, con el impacto de cada una (alcance,
   precio, plazo).

### 6. Consultar las ambigüedades bloqueantes

Presentar las preguntas al usuario **juntas**, indicando el impacto de cada una.
Mientras se espera respuesta, avanzar en lo que no dependa de ellas. Registrar las
respuestas en `wiki/licitaciones/<slug>.md` para no volver a preguntarlas.

## Salidas

- `licitaciones/<slug>/00 - Analisis Documental.md`
- `wiki/licitaciones/<slug>.md` creado con los datos del proceso y el estado
  `Ingesta` o `En consulta`.
- Entrada en `wiki/log.md` con prefijo `ingesta`.
- Lista de preguntas al usuario, si hay ambigüedades bloqueantes.

## Errores a evitar

- **Cotizar contra el RFP sin haber leído las aclaraciones.** El error más caro del
  proceso.
- Leer solo los encabezados de los modelos de costos sin mapear su estructura real
  de celdas y fórmulas.
- Rellenar un dato faltante con un supuesto no declarado.
- Omitir requerimientos "administrativos" o de entregables por no ser desarrollo:
  también consumen esfuerzo y deben costearse.
- Empezar a redactar la propuesta técnica antes de cerrar el análisis documental.
