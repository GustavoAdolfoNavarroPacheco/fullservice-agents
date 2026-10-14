# Estimación de Horas de Desarrollo

El entregable #2. Debe ser **defendible** (método y supuestos escritos),
**trazable** (cada línea corresponde a un módulo/funcionalidad de la propuesta) y
**factible** (cabe en el plazo exigido por el RFP con el equipo propuesto).

---

## 1. Unidad de estimación: horas, con conversión explícita a días

La licitación pide **horas de desarrollo**, mientras el modelo de costos interno de
FullService trabaja en **días por especialidad**. Ambas vistas deben coexistir y
cuadrar:

- La estimación que se entrega (`03 - Estimacion de Horas.xlsx`) está en **horas**.
- El modelo de cotización interno (`07`) se llena en **días**.
- **La conversión se declara explícitamente en el archivo** (celda o nota
  visible), y el factor se confirma con el usuario en la primera licitación:
  típicamente 8 horas = 1 día hábil, salvo que el RFP o el usuario definan otro
  factor.
- Si el RFP fija su propia definición de día/hora hábil o de jornada, **manda la
  del RFP** y se cita.

> **No hardcodear el factor sin confirmarlo.** Si el usuario no lo ha definido en
> esta licitación ni en una anterior registrada en la ficha, se pregunta.

---

## 2. Especialidades (alineadas con el modelo de costos de FullService)

El modelo interno de costeo de Campuslands discrimina el esfuerzo por estas
especialidades. La estimación de horas usa las mismas para que ambos modelos
cuadren sin reinterpretación:

| Código | Especialidad |
|--------|--------------|
| DB | DB, Líder, Arquitecto, Scrum |
| UX | Diseño UI/UX |
| FM | FrontEnd Medium |
| BS | BackEnd Senior |
| BM | BackEnd Semi-Senior |
| QA | QA, Test |
| IM | Implementación, Capacitación |
| MS | Mobile Semi-Senior |
| MM | Mobile Medium |
| IA | BackEnd IA |

- Solo se llenan las especialidades que **realmente participan** en cada ítem; las
  demás quedan vacías (no en 0).
- **Antes de usar esta tabla, verifico que siga vigente** en el modelo de costos de
  cotización de esta licitación: la plantilla la define y puede cambiar entre
  versiones. Si difiere, manda el archivo y actualizo esta página.

---

## 3. Categorías transversales (siempre presentes)

Todo proyecto lleva esfuerzo que no pertenece a un módulo funcional específico. Se
estima según el **tamaño y complejidad global** del proyecto, no según un bullet
puntual:

| Categoría | Qué cubre |
|-----------|-----------|
| Estructura del proyecto | Setup inicial, liderazgo, arquitectura, gestión y ceremonias Scrum |
| UX y esquema del proyecto | Diseño UX/UI base de todo el sistema |
| Implementación y entrega | Despliegue, entrega, capacitación, transferencia de conocimiento |
| Estructura del agente IA | Scaffolding del componente de IA (solo si el alcance lo requiere) |

A mayor alcance total, mayor esfuerzo transversal. Si el alcance **no** incluye IA,
la línea correspondiente se deja en el piso mínimo con la nota de que no hay
componente de IA en este alcance.

Además, se estima explícitamente el esfuerzo de los requerimientos que la
licitación exige pero que no son "desarrollo" en sentido estricto y suelen
olvidarse:

- Documentación técnica y de usuario exigida por el RFP.
- Capacitación y transferencia de conocimiento.
- Migración de datos desde sistemas existentes.
- Pruebas de carga, seguridad o aceptación exigidas.
- Acompañamiento en puesta en producción y estabilización.
- Meses de operación/soporte incluidos en el alcance.

**Un requerimiento del RFP sin horas asignadas es una omisión**, y la verificación
cruzada lo detecta.

---

## 4. Método de estimación

1. **Descomponer** cada módulo de la propuesta técnica en funcionalidades
   atómicas (unidades de trabajo con esfuerzo propio y distinguible).
2. **Estimar cada funcionalidad con criterio de desarrollador real**: complejidad
   técnica, integraciones externas, volumen de datos, requisitos no funcionales
   asociados y alcance descrito. Nunca un valor genérico por defecto.
3. **Un solo estimado por ítem atómico de trabajo**, en la fila que mejor lo
   represente. Si una fila solo describe o elabora la fila anterior, no lleva
   horas: nunca se duplica el mismo esfuerzo en dos filas.
4. **Distribuir por especialidad** según qué perfiles participan realmente.
5. **Piso mínimo** por ítem y especialidad: el equivalente a 0.5 días (4 horas con
   el factor estándar). Por encima de eso se admite cualquier decimal realista.
6. **Documentar el método y los supuestos** en el propio archivo: base de la
   estimación, factores aplicados, y qué se excluyó.

### Cuando el RFP o un documento fuente ya trae estimaciones
Si el RFP, las aclaraciones o un anexo traen horas/días por actividad, **esas
mandan** y se citan. Si el documento fuente es internamente inconsistente (por
ejemplo, la tabla de detalle no suma lo que dice el resumen), **no elijo por mi
cuenta**: reporto la inconsistencia al usuario con ambas cifras y aplico la que
confirme, registrando la decisión en la ficha de la licitación.

---

## 5. Validación de factibilidad contra el plazo (obligatoria)

Esta validación se ejecuta **antes** de entregar y se deja escrita en el archivo:

```
Horas totales estimadas            = H
Plazo exigido por el RFP           = P días hábiles   (cita del RFP)
Horas hábiles por persona por día  = J                (factor declarado)
Personas requeridas                = H / (P × J)
```

Se compara el resultado contra el equipo propuesto en la propuesta técnica:

- **Cabe** → se documenta el cálculo y se sigue.
- **No cabe** → se reporta al usuario con los números, junto con las opciones
  reales: ampliar el equipo (y su impacto en el precio), negociar el plazo o el
  alcance por la vía de aclaraciones, o desistir. **No se ajusta la estimación
  hacia abajo para que el cronograma cuadre.**

También se verifica la factibilidad **por especialidad**: un total agregado que
cuadra puede esconder, por ejemplo, un único arquitecto con 400 horas en un plazo
de 30 días.

---

## 6. Verificación obligatoria

- Cada módulo/funcionalidad de la propuesta técnica tiene su(s) línea(s) de horas,
  y cada línea pertenece a un módulo. **Correspondencia 1:1.**
- Cada requerimiento numerado del RFP y de las aclaraciones tiene esfuerzo
  asignado o una justificación explícita de por qué no lo requiere.
- Ninguna estimación por debajo del piso mínimo.
- El factor de conversión horas↔días está declarado en el archivo.
- El cálculo de factibilidad contra el plazo está escrito y da un resultado
  compatible con el equipo propuesto.
- Las horas totales del entregable `03` cuadran con los días del modelo de
  cotización `07` bajo el factor declarado.
- El XLSX recalcula sin errores de fórmula, o si se generó con valores estáticos calculados fuera de Excel, esa decisión está documentada explícitamente en `verificacion-cruzada.md`.
