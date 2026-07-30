---
name: modelos-costos
description: Llena el modelo de costos oficial que exige la empresa solicitante y el segundo modelo de costos (el de cotización interno de Campuslands), y concilia ambos totales dejando la diferencia explicada. Nunca edita los archivos originales de recursos/.
---

# Modelos de Costos (oficial + cotización)

## Cuándo usar esta skill

Después de que la estimación de horas esté completa y validada, y después del
análisis de IA si el alcance lo requiere (sus costos deben entrar en ambos modelos).

No usar esta skill para: estimar esfuerzo (eso es `estimacion-horas`).

## Entradas

- `recursos/licitaciones/<slug>/` — el modelo de costos **oficial** de la empresa y
  el **segundo modelo** (cotización). **Solo lectura.**
- `licitaciones/<slug>/03 - Estimacion de Horas.xlsx`.
- `licitaciones/<slug>/05 - Analisis IA y Tokens.xlsx`, si existe.
- `licitaciones/<slug>/04 - Consideraciones Tecnicas.md` — para los costos que no
  son desarrollo (infraestructura, licencias, servicios recurrentes, capacitación,
  operación).

## Procedimiento

### 1. Copiar, nunca editar el original

```
recursos/licitaciones/<slug>/<modelo oficial>   → licitaciones/<slug>/06 - Modelo de Costos Oficial.xlsx
recursos/licitaciones/<slug>/<modelo cotización> → licitaciones/<slug>/07 - Modelo de Costos Cotizacion.xlsx
```

Los archivos de `recursos/` son fuentes inmutables. Todo el trabajo va sobre las
copias.

### 2. Mapear la estructura de cada modelo antes de escribir

Para cada archivo: identificar qué celdas son de **entrada de datos** y qué celdas
son de **fórmula**, columna por columna y fila por fila. Documentar el mapeo en
`wiki/licitaciones/<slug>.md` la primera vez.

**Regla dura: no se tocan las fórmulas.** Solo se llenan las celdas de datos que el
modelo espera. Si el alcance necesita más filas de las que trae el modelo, se
**insertan filas** y se verifica que las fórmulas se hayan propagado correctamente
a las filas nuevas antes de recalcular.

### 3. Llenar el modelo oficial (`06`)

- Se respeta **exactamente** el formato, las líneas y las reglas que exige la
  empresa solicitante. Este es el archivo que se radica: un desvío de formato puede
  descalificar la propuesta.
- Si el modelo oficial pide una desagregación que el modelo interno no produce
  directamente (por ejemplo, costo por perfil-hora en lugar de por especialidad-día),
  se hace la conversión y **se documenta el mapeo** en una hoja aparte o en la
  ficha de la licitación.
- Si el modelo oficial exige líneas que Campuslands no cotiza o que no aplican, se
  consulta al usuario antes de dejarlas en cero o en blanco.

### 4. Llenar el modelo de cotización (`07`)

- Es el motor de precio real: se llena con el desglose por módulo, funcionalidad,
  detalle técnico y días por especialidad, tomados de la estimación de horas y
  convertidos con el factor declarado.
- **Confidencialidad:** si la plantilla trae hojas de otros clientes o procesos, se
  **eliminan** antes de trabajar. La hoja de trabajo se renombra con el
  identificador de la licitación.
- Convenciones de fuente y formato según `wiki/marca-campuslands.md` §5 (Arial
  11 bold / 10 bold / 10 regular por nivel de jerarquía, explícito).

### 5. Incluir los costos que no son desarrollo

Ambos modelos deben contemplar, cuando apliquen:

- Infraestructura (si va en el precio y no la provee la empresa solicitante).
- Licencias de software de terceros.
- Servicios recurrentes: mensajería, APIs, firma electrónica, mapas.
- **Consumo de IA** — desde `05`, incluido el margen de contingencia.
- Certificaciones y auditorías exigidas.
- Capacitación y transferencia de conocimiento.
- Meses de operación y soporte incluidos en el alcance.
- Pólizas y garantías exigidas por el RFP.
- Contingencia, explícita y justificada.

### 6. Conciliar ambos modelos (obligatorio)

```
Total del modelo oficial      (06) = A
Total del modelo de cotización (07) = B
Diferencia                          = A − B
```

La conciliación se documenta con:

- El detalle de qué compone la diferencia (impuestos, margen, líneas que un modelo
  agrupa y el otro desagrega, redondeos, costos que un modelo no contempla).
- **Cada componente de la diferencia explicado.** Una diferencia sin explicar es un
  error de llenado, no una particularidad de los modelos.
- Si la diferencia no se puede explicar, **se reporta al usuario** antes de
  entregar.

### 7. Recalcular y verificar

- Recalcular ambos archivos y confirmar **cero errores de fórmula** (`#REF!`,
  `#DIV/0!`, `#NAME?`, `#N/A`), salvo defectos preexistentes conocidos de la
  plantilla, que se documentan explícitamente como preexistentes.
- Si el modelo se reconstruye con valores calculados fuera de Excel (por ejemplo
  en Python) en vez de fórmulas vivas, esta verificación no aplica en el sentido
  estricto — se documenta explícitamente esa decisión en `verificacion-cruzada.md`,
  incluyendo que el archivo no queda "vivo" y cómo regenerarlo si el usuario
  necesita un modelo editable para negociar después de la adjudicación.
- Verificar que los precios calculados sean coherentes con los días/horas
  ingresados (revisión por muestreo de líneas, no solo el total).
- Verificar que el total del modelo oficial esté dentro del presupuesto oficial de
  la licitación, si el RFP lo publica. Si lo excede, **reportarlo al usuario de
  inmediato**: puede significar que hay que revisar alcance o estrategia.

## Salidas

- `licitaciones/<slug>/06 - Modelo de Costos Oficial.xlsx`
- `licitaciones/<slug>/07 - Modelo de Costos Cotizacion.xlsx`
- Sección de conciliación en `licitaciones/<slug>/verificacion-cruzada.md`.
- Mapeo de estructura de los modelos en `wiki/licitaciones/<slug>.md`.

## Errores a evitar

- **Editar los archivos de `recursos/`.**
- Tocar fórmulas del modelo en lugar de llenar solo las celdas de datos.
- Insertar filas sin verificar que las fórmulas se propagaron.
- Entregar un modelo sin el otro, o sin la conciliación.
- Dejar hojas de otros clientes en el archivo entregado (falla de
  confidencialidad).
- Olvidar trasladar el costo de IA a los dos modelos.
- No comparar el total contra el presupuesto oficial cuando el RFP lo publica.
