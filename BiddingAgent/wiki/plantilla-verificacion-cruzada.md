# Plantilla — Verificación Cruzada

Se copia a `licitaciones/<slug>/verificacion-cruzada.md` y se llena antes de
entregar. El objetivo es dejar **rastro auditable** de la verificación, no solo la
afirmación de que se hizo: cada casilla marcada debe ir acompañada de la evidencia
(cifras, conteos, referencias de celda).

---

## Datos

| Campo | Valor |
|---|---|
| Licitación | |
| Entidad solicitante | |
| Identificador del proceso | |
| Fecha de verificación | |
| Versión verificada | |

---

## 1. Cobertura de requerimientos (cero omisiones)

| Verificación | Resultado | Evidencia |
|---|---|---|
| Total de requerimientos en el análisis documental | `N =` | |
| Total de filas en la matriz de cumplimiento | `M =` | |
| **`N == M`** | ☐ | Si no coinciden, listar la diferencia |
| Requerimientos obligatorios en `No cumple` | `n =` | **Bloqueante si n > 0** — reportado al usuario: ☐ |
| Requerimientos en `Cumple parcialmente` | `n =` | Reportados al usuario: ☐ |
| Todas las filas tienen cita de origen | ☐ | |

## 2. Correspondencia propuesta ↔ estimación

| Verificación | Resultado | Evidencia |
|---|---|---|
| Módulos en la propuesta técnica | `=` | |
| Módulos con horas en la estimación | `=` | |
| **Correspondencia 1:1** (ni módulos sin horas, ni horas sin módulo) | ☐ | |
| Todo requerimiento `Cumple` tiene esfuerzo o justificación de por qué no lo requiere | ☐ | |
| Ninguna estimación por debajo del piso mínimo | ☐ | |

## 3. Factibilidad del plazo

| Verificación | Resultado | Evidencia |
|---|---|---|
| Horas totales estimadas | `H =` | |
| Plazo exigido por el RFP | `P =` días hábiles | Cita: |
| Factor horas/persona/día declarado | `J =` | Fuente del factor: |
| Personas requeridas `H / (P × J)` | `=` | |
| Equipo propuesto en la propuesta técnica | `=` | |
| **El cronograma cabe en el plazo** | ☐ | Si no cabe: reportado al usuario con los números ☐ |
| Factibilidad verificada **por especialidad** (ninguna sobrecargada) | ☐ | Especialidad más cargada: |

## 4. Conciliación de los modelos de costos

| Verificación | Resultado | Evidencia |
|---|---|---|
| Total del modelo oficial (`06`) | `A =` | |
| Total del modelo de cotización (`07`) | `B =` | |
| Diferencia `A − B` | `=` | |
| **Cada componente de la diferencia explicado** | ☐ | Desglose: |
| Presupuesto oficial publicado por el RFP (si existe) | `=` | Cita: |
| El total está dentro del presupuesto oficial | ☐ / N/A | Si lo excede: reportado al usuario ☐ |
| Las horas de `03` cuadran con los días de `07` bajo el factor declarado | ☐ | |

## 5. Componente de inteligencia artificial

| Verificación | Resultado | Evidencia |
|---|---|---|
| La conclusión sobre IA está escrita explícitamente en `04` | ☐ | Conclusión: `Requiere IA` / `No requiere IA` |
| La conclusión está fundamentada con cita documental | ☐ | |
| Si requiere IA: `05` existe con los tres escenarios | ☐ / N/A | |
| Si requiere IA: fecha de verificación de precios registrada | ☐ / N/A | Fecha: |
| Si requiere IA: tokens contados con el endpoint oficial (no `tiktoken`) | ☐ / N/A | |
| Si requiere IA: caché de prompt y Batch API considerados donde aplican | ☐ / N/A | |
| Si requiere IA: costo trasladado a `06` y `07` | ☐ / N/A | Monto: |
| Si requiere IA: TRM declarada con su fecha (si se convirtió a COP) | ☐ / N/A | TRM / fecha: |

## 6. Integridad de los archivos

| Verificación | Resultado | Evidencia |
|---|---|---|
| Todos los XLSX recalculan sin errores de fórmula | ☐ | Errores encontrados: |
| Los errores presentes son defectos preexistentes conocidos de la plantilla | ☐ / N/A | Cuáles: |
| No quedan hojas de otros clientes en los archivos entregados | ☐ | |
| Los archivos originales de `recursos/` no fueron modificados | ☐ | |
| El formato del modelo oficial respeta exactamente lo exigido por la empresa | ☐ | |

## 7. Veracidad y confidencialidad

| Verificación | Resultado | Evidencia |
|---|---|---|
| No quedan marcas `[PENDIENTE: …]` sin resolver | ☐ | |
| Ninguna cifra, plazo o capacidad carece de respaldo documental | ☐ | |
| Ninguna afirmación de experiencia o certificación sin respaldo en el brief o confirmación del usuario | ☐ | |
| La propuesta no referencia otras licitaciones ni otros clientes | ☐ | |
| Se respetaron los requisitos de forma del RFP (formato, foliado, nombres de archivo) | ☐ | |

---

## Resultado

☐ **Aprobado para entrega** — todas las verificaciones pasaron.

☐ **No aprobado** — hallazgos pendientes:

1.
2.

## Hallazgos reportados al usuario

| # | Hallazgo | Impacto | Respuesta del usuario |
|---|---|---|---|
| 1 | | | |
