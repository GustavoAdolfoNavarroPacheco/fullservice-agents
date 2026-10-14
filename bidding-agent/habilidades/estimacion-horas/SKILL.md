---
name: estimacion-horas
description: Estima las horas de desarrollo por módulo, funcionalidad y especialidad a partir de la propuesta técnica, con método y supuestos documentados, conversión horas↔días declarada, y validación obligatoria de factibilidad contra el plazo exigido por el RFP.
---

# Estimación de Horas de Desarrollo

## Cuándo usar esta skill

Después de que la propuesta técnica tenga sus módulos y funcionalidades definidos
(al menos en borrador estructural), y después de que la matriz de cumplimiento esté
llena. También al re-estimar tras un cambio de alcance por adenda o por decisión
del usuario.

No usar esta skill para: costear en dinero (eso es `modelos-costos`) ni para estimar
consumo de IA (eso es `analisis-ia-tokens`).

## Entradas

- `licitaciones/<slug>/02 - Propuesta Tecnica` (módulos y funcionalidades).
- `licitaciones/<slug>/01 - Matriz de Cumplimiento.xlsx`.
- `licitaciones/<slug>/00 - Analisis Documental.md` (plazos y volúmenes exigidos).
- El modelo de costos de cotización, para conocer las especialidades vigentes.
- `wiki/estimacion-horas.md` — método, especialidades y reglas.

## Procedimiento

### 1. Confirmar el factor de conversión horas↔días

El entregable se expresa en **horas**; el modelo de costeo interno trabaja en
**días**. Antes de estimar:

- Si el RFP define jornada, día u hora hábil, **manda el RFP** y se cita.
- Si no, se usa el factor confirmado por el usuario (típicamente 8 h = 1 día
  hábil). Si el usuario no lo ha definido en esta licitación ni en una anterior
  registrada en la ficha, **preguntar**.
- El factor queda **declarado explícitamente en el archivo**.

### 2. Descomponer en ítems atómicos

Cada módulo de la propuesta se descompone en funcionalidades con esfuerzo propio y
distinguible. Una fila que solo describe o elabora la fila anterior **no lleva
horas**: nunca se duplica el mismo esfuerzo en dos filas.

### 3. Estimar por especialidad

Especialidades del modelo interno de FullService (verificar vigencia contra el
modelo de costos de esta licitación antes de usarlas):

`DB` (DB/Líder/Arquitecto/Scrum) · `UX` · `FM` (FrontEnd Medium) ·
`BS` (BackEnd Senior) · `BM` (BackEnd Semi-Senior) · `QA` · `IM`
(Implementación/Capacitación) · `MS` (Mobile Semi-Senior) · `MM` (Mobile Medium) ·
`IA` (BackEnd IA)

- Solo se llenan las especialidades que **realmente participan**; las demás quedan
  vacías, no en 0.
- **Piso mínimo** por ítem y especialidad: equivalente a 0.5 días.
- Se estima con criterio de desarrollador real: complejidad técnica, integraciones
  externas, volumen de datos, requisitos no funcionales asociados. **Nunca un valor
  genérico por defecto.**

### 4. Incluir lo transversal y lo que no es "desarrollo"

Además de los módulos funcionales:

- Estructura del proyecto (setup, arquitectura, liderazgo, ceremonias).
- UX y esquema base del sistema.
- Implementación, despliegue y entrega.
- Estructura del componente de IA (solo si el alcance lo requiere; si no, piso
  mínimo con la nota correspondiente).
- Documentación técnica y de usuario exigida.
- Capacitación y transferencia de conocimiento.
- Migración de datos.
- Pruebas exigidas (carga, seguridad, UAT).
- Acompañamiento en puesta en producción y estabilización.
- Meses de operación/soporte incluidos en el alcance.

**Un requerimiento del RFP sin horas asignadas es una omisión.**

### 5. Cuando el documento fuente ya trae estimaciones

Si el RFP, las aclaraciones o un anexo traen horas/días por actividad, **esas
mandan** y se citan. Si el documento es internamente inconsistente (la tabla de
detalle no suma lo que dice el resumen), **no elegir por cuenta propia**: reportar
la inconsistencia al usuario con ambas cifras, aplicar la que confirme, y registrar
la decisión en `wiki/licitaciones/<slug>.md`.

### 6. Validación de factibilidad contra el plazo (obligatoria)

Se calcula y se deja escrita en el archivo:

```
Horas totales estimadas            = H
Plazo exigido por el RFP           = P días hábiles   (con cita)
Horas hábiles por persona por día  = J                (factor declarado)
Personas requeridas                = H / (P × J)
```

Se compara contra el equipo propuesto:

- **Cabe** → se documenta el cálculo y se sigue.
- **No cabe** → **se reporta al usuario con los números**, junto con las opciones
  reales: ampliar el equipo (con su impacto en precio), negociar plazo o alcance por
  aclaraciones, o desistir. **No se ajusta la estimación hacia abajo para que el
  cronograma cuadre.**

Verificar también la factibilidad **por especialidad**: un total agregado que cuadra
puede esconder un único arquitecto con 400 horas en 30 días.

### 7. Documentar método y supuestos en el archivo

Base de la estimación, factores aplicados, qué se excluyó, y las fuentes de los
volúmenes usados. **Un número sin método no se entrega.**

## Salidas

- `licitaciones/<slug>/03 - Estimacion de Horas.xlsx` con: detalle por
  módulo/funcionalidad/especialidad, totales, factor de conversión declarado, hoja
  de método y supuestos, y el cálculo de factibilidad.
- Reporte al usuario si el plazo no es factible.

## Verificación antes de entregar

- [ ] Correspondencia 1:1 entre módulos de la propuesta y líneas de horas.
- [ ] Cada requerimiento numerado tiene esfuerzo o justificación de por qué no lo
      requiere.
- [ ] Ninguna estimación por debajo del piso mínimo.
- [ ] Factor de conversión horas↔días declarado en el archivo.
- [ ] Cálculo de factibilidad escrito, con resultado compatible con el equipo
      propuesto (o reportado al usuario si no lo es).
- [ ] Las horas totales cuadran con los días del modelo de cotización bajo el
      factor declarado.
- [ ] El XLSX recalcula sin errores de fórmula, o si se generó con valores estáticos calculados fuera de Excel, esa decisión está documentada explícitamente en `verificacion-cruzada.md`.

## Errores a evitar

- Duplicar el mismo esfuerzo en la fila de funcionalidad y en la de detalle.
- Estimar solo el desarrollo y olvidar documentación, capacitación, migración,
  pruebas exigidas y meses de operación.
- Maquillar la estimación para que quepa en el plazo.
- Usar un factor horas↔días sin declararlo ni confirmarlo.
- Llenar todas las especialidades con valores pequeños "por si acaso" en lugar de
  dejar vacías las que no participan.
