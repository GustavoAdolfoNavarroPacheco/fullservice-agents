# Flujo de Trabajo (Proceso Licitatorio)

Tres fases: **ingesta y análisis** → **construcción de los cuatro entregables** →
**verificación y entrega**. La fase 2 no empieza hasta que la fase 1 esté cerrada.

---

## Fase 1 — Ingesta y análisis integral

### 1.1 Verificación de insumos
El usuario deposita los documentos oficiales en
`recursos/licitaciones/<slug-licitacion>/`. Verifico que estén los **cuatro**:
RFP, aclaraciones/preguntas y respuestas, modelo de costos oficial, y segundo
modelo de costos (cotización). **Si falta alguno, pregunto antes de continuar.**
Si el usuario confirma que ese proceso no tiene alguno de ellos, lo registro
explícitamente en el análisis documental y en `log.md`.

### 1.2 Lectura completa e integral
Leo los cuatro documentos **enteros**, en este orden:

1. **RFP** — para entender el alcance base.
2. **Aclaraciones** — para corregir esa lectura con lo que prevalece.
3. **Modelo de costos oficial** — para conocer la estructura que exige la empresa.
4. **Modelo de costos de cotización** — para conocer el motor de precio interno.

**Nunca genero un entregable con una lectura parcial de los documentos.** Esta es
la instrucción central del rol: análisis integral antes de cualquier respuesta.

### 1.3 Extracción y numeración de requerimientos
Extraigo **todos** los requerimientos con su cita de origen, clasificados en:

- Funcionales (RF)
- No funcionales (RNF): rendimiento, disponibilidad, seguridad, escalabilidad, usabilidad
- Técnicos: stack, integraciones, infraestructura, migración de datos
- De plazo: fechas, hitos, entregables intermedios
- Legales/administrativos: pólizas, certificaciones, experiencia acreditable
- De entregables: documentación, capacitación, transferencia de conocimiento
- De operación y soporte: SLA, mesa de ayuda, garantía, mantenimiento

Cada uno recibe un identificador estable (`RF-01`, `RNF-07`, `PLZ-03`) que se usa
en todos los entregables posteriores.

### 1.4 Análisis documental (`00 - Analisis Documental.md`)
Documento de trabajo con:

- **Datos del proceso**: entidad solicitante, identificador de la licitación,
  objeto, fechas clave (cierre, adjudicación, inicio), presupuesto oficial si se
  publica.
- **Inventario de requerimientos** numerados con cita de origen.
- **Plazos y hitos** exigidos.
- **Criterios de evaluación** y su ponderación (define dónde vale la pena
  invertir esfuerzo en la propuesta).
- **Contradicciones y precedencias**: cada contradicción detectada, la cita de
  ambos documentos, y la lectura adoptada según la jerarquía documental.
- **Supuestos** explícitos, cada uno con su justificación documental.
- **Ambigüedades a consultar** con el usuario, agrupadas.

### 1.5 Consulta de ambigüedades
Presento al usuario las ambigüedades bloqueantes **juntas** y espero respuesta.
Mientras espero, avanzo en todo lo que no dependa de ellas. Las respuestas se
registran en `wiki/licitaciones/<slug>.md` para no volver a preguntarlas.

---

## Fase 2 — Los cuatro entregables

### 2.1 Matriz de cumplimiento (`01 - Matriz de Cumplimiento.xlsx`)
**Se llena antes de la propuesta técnica**, no después. Es el gate de "cero
requerimientos omitidos": una fila por requerimiento, con cómo lo cumple la
propuesta, en qué módulo/sección se responde, y la cita de origen. Ver
`habilidades/matriz-cumplimiento/SKILL.md`.

### 2.2 Propuesta técnica (`02 - Propuesta Tecnica.pdf`)
Según `estructura-propuesta-tecnica.md`: entendimiento del requerimiento,
solución propuesta por módulos, arquitectura, stack, integraciones, seguridad y
cumplimiento, metodología, cronograma alineado al plazo exigido, equipo,
entregables, y supuestos/exclusiones. Diseño visual según
`marca-campuslands.md`.

### 2.3 Estimación de horas (`03 - Estimacion de Horas.xlsx`)
Horas por módulo/funcionalidad y por especialidad, con el método y los supuestos
documentados, la conversión horas↔días explícita, y la **validación de
factibilidad contra el plazo del RFP**. Ver `estimacion-horas.md`.

### 2.4 Consideraciones técnicas (`04 - Consideraciones Tecnicas.md`)
Recorro el checklist completo de `consideraciones-tecnicas.md` y documento cada
elemento técnico necesario. Cierra con la **conclusión explícita sobre IA**: si el
alcance requiere servicios de inteligencia artificial o no, y por qué, con cita
documental.

### 2.5 Análisis de IA y tokens (`05 - Analisis IA y Tokens.xlsx`)
**Solo si 2.4 concluyó que se requiere IA.** Actividades que la requieren,
estimación de tokens por actividad con su método, y costo estimado con los
precios vigentes de `costeo-ia-tokens.md`. Si no se requiere IA, dejo la
constancia escrita en `04` y no genero este archivo.

### 2.6 Modelos de costos (`06` y `07`)
Lleno el **modelo oficial** en el formato exacto que exige la empresa (copiando
el archivo original, nunca editándolo) y el **modelo de cotización** interno, y
**concilio ambos totales**. Los costos de IA de `05` deben aparecer en ambos. Ver
`habilidades/modelos-costos/SKILL.md`.

---

## Fase 3 — Verificación y entrega

### 3.1 Verificación cruzada (`verificacion-cruzada.md`)
Con rastro auditable, no solo la afirmación de que se hizo:

- [ ] Todo requerimiento del RFP y de las aclaraciones tiene fila en la matriz con respuesta. **Cero omisiones.**
- [ ] Las horas de `03` corresponden 1:1 con los módulos de `02`: ni módulos sin horas, ni horas sin módulo.
- [ ] El cronograma de `02` cabe en el plazo exigido con el equipo propuesto y las horas de `03`.
- [ ] Los totales de `06` y `07` están conciliados y la diferencia está explicada.
- [ ] Los costos de IA de `05` están incluidos en `06` y `07`.
- [ ] Los XLSX recalculan sin errores de fórmula (salvo defectos preexistentes conocidos, documentados), o si se generaron con valores estáticos calculados fuera de Excel, esa decisión está documentada explícitamente en `verificacion-cruzada.md`.
- [ ] Ninguna cifra, plazo o capacidad de la propuesta carece de respaldo documental.
- [ ] No quedan marcas `[PENDIENTE: …]` sin resolver.
- [ ] La propuesta no referencia otras licitaciones ni mezcla información de otros clientes.

### 3.2 Entrega y registro
Entrego los archivos en `licitaciones/<slug>/`, actualizo `wiki/index.md`,
creo/actualizo `wiki/licitaciones/<slug>.md` con las decisiones y el estado, y
agrego la entrada correspondiente a `wiki/log.md`.
