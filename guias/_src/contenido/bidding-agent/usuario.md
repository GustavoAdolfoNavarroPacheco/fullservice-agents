---
titulo: Agente Licitatorio: cómo preparar la propuesta de una licitación
resumen: Qué documentos entregarle, cómo responder sus preguntas, qué recibes y cómo revisar la propuesta antes de radicarla.
---

## En resumen

El **Agente Licitatorio** te ayuda a responder una licitación de software. Tú le entregas los **cuatro documentos oficiales** del proceso; él los lee completos, detecta contradicciones y huecos, y construye la propuesta: el documento técnico, la estimación de horas, las consideraciones técnicas, un análisis de inteligencia artificial si hace falta y los dos modelos de costos llenados.

Su principio es que la propuesta debe poder **defenderse ante el comité evaluador**: cada afirmación se apoya en un documento oficial, y nada se inventa.

```stats
4 | documentos oficiales es todo lo que necesita para empezar
0 | requerimientos olvidados: cada uno tiene su fila de respuesta
2 | modelos de costos que se llenan y se concilian
```

> [!tip] Lo más importante
> Dale **siempre** las aclaraciones del proceso junto con el RFP. Si cotizas sobre un alcance que las aclaraciones ya cambiaron, el error sale caro.

## Para qué sirve

Úsalo cuando Campuslands decida participar en un proceso de licitación o convocatoria formal con requisitos escritos, plazos y un formato oficial de costos. No es para propuestas comerciales informales: para esas están los agentes de presentaciones y de cotizaciones.

### Qué pasa si los documentos se contradicen

Hay un orden de prioridad que el agente aplica siempre:

```flow
Aclaraciones | Gana siempre: es lo más reciente y vinculante.
Adendas | Modificaciones formales al RFP.
RFP original | La base del alcance.
Modelo de costos oficial | Solo manda en la forma de costear.
```

Si una contradicción cambia el alcance o el precio de forma importante, el agente **no decide por su cuenta**: te la presenta y te pregunta.

## Qué necesitas darle

Los **cuatro documentos** del proceso, sin excepción:

```cards
1 · El RFP | El documento oficial con el alcance, los requerimientos, los plazos y los criterios de evaluación.
2 · Las aclaraciones | Las preguntas y respuestas del proceso. Pueden cambiar el alcance y prevalecen sobre el RFP.
3 · El modelo de costos oficial | El formato de costos que exige la empresa que licita. Es el que se radica.
4 · El modelo de costos de cotización | La plantilla interna de Campuslands con la que se calcula el precio real.
```

### Dónde dejarlos

En la carpeta del proceso, dentro de los recursos del agente, con un nombre que identifique la licitación:

```tree
recursos/
  licitaciones/
    <nombre-del-proceso>/       # por ejemplo: ipa-pr10598
      RFP.pdf
      Aclaraciones.pdf
      Modelo de costos oficial.xlsx
      Modelo de costos de cotizacion.xlsx
```

> [!importante] Si falta uno, el agente se detiene
> Si no están los cuatro, te lo dirá y preguntará antes de construir. Si realmente un documento no existe en ese proceso, díselo con claridad: quedará registrado.

## Paso a paso

```lanes
Tú | Deja los cuatro documentos en la carpeta del proceso
Agente | Los lee completos y arma el análisis documental
Agente | Te presenta juntas las dudas que bloquean el avance
Tú | Respóndelas
Agente | Construye la matriz, la propuesta, las horas y los costos
Agente | Verifica todo con una revisión cruzada
Tú | Revisa y decide si radicas
```

### 1. Entrega los documentos

Cuando estén en la carpeta, dile el nombre del proceso y que quieres preparar la propuesta.

### 2. El agente lee y analiza

Lee los cuatro documentos completos y en orden, numera cada requerimiento con su cita (por ejemplo, «RFP §4.2» o «Aclaración P-17»), y detecta plazos, criterios de evaluación y contradicciones. El resultado es el **análisis documental**.

### 3. Responde las dudas

Los documentos de licitación casi siempre tienen huecos, y el agente no los rellena por su cuenta. Te presentará **las preguntas juntas**, indicando qué impacto tiene cada una (en alcance, precio o plazo). Mientras tanto, seguirá avanzando en todo lo que no dependa de tus respuestas.

### 4. Se construye la propuesta

Con tus respuestas, el agente construye en orden: la matriz de cumplimiento, la propuesta técnica, la estimación de horas, las consideraciones técnicas, el análisis de IA (si aplica) y los dos modelos de costos.

### 5. Revisa y decide

Recibes todo con una **verificación cruzada** que demuestra que los documentos se corresponden entre sí. Tú decides si se radica.

## Ejemplos de conversación

### Empezar

```chat
Tú: Analiza la licitación ipa-pr10598. Los cuatro documentos ya están en la carpeta de recursos.
Agente: Verifiqué los cuatro documentos y los leí completos. Numeré los requerimientos y encontré tres contradicciones entre el RFP y las aclaraciones. Tengo cinco preguntas bloqueantes, agrupadas con su impacto en alcance, precio y plazo.
```

### Responder las dudas

```chat
Tú: Sobre tus preguntas: 1) 200 usuarios concurrentes, 2) 12 meses de operación incluidos, 3) los datos deben quedar en Colombia.
Agente: Gracias. Registré las tres respuestas en la ficha de la licitación y continúo con la matriz de cumplimiento.
```

### Llegó una adenda

```chat
Tú: Llegó una adenda al RFP. Vuelve a revisar el alcance y ajusta la propuesta.
Agente: Reanalicé el alcance con la adenda. Cambia dos requerimientos y agrega uno nuevo. Actualicé la matriz, la propuesta y la estimación de horas.
```

### Preguntar por el plazo

```chat
Tú: ¿El cronograma cabe en el plazo que exige el RFP?
Agente: Con las horas estimadas y el equipo propuesto, el plazo es factible. El cálculo está en el archivo de estimación: horas totales, días hábiles exigidos, y personas requeridas frente a las propuestas.
```

## Qué recibes

Todo queda en una carpeta propia del proceso, con archivos numerados:

| Archivo | Qué contiene |
|---|---|
| `00 - Analisis Documental` | Los requerimientos, plazos, criterios de evaluación, contradicciones, supuestos y dudas |
| `01 - Matriz de Cumplimiento` | Cada requerimiento, si se cumple y cómo, y dónde se responde en la propuesta |
| `02 - Propuesta Tecnica` | El documento principal: módulos, arquitectura, metodología, cronograma y equipo |
| `03 - Estimacion de Horas` | Las horas por módulo y por especialidad, validadas contra el plazo |
| `04 - Consideraciones Tecnicas` | Todo lo técnico que hay que tener en cuenta, y la conclusión sobre IA |
| `05 - Analisis IA y Tokens` | Qué actividades usan IA y cuánto costaría (solo si el alcance la requiere) |
| `06 - Modelo de Costos Oficial` | El formato que exige la empresa, llenado: es el que se radica |
| `07 - Modelo de Costos Cotizacion` | El modelo interno con el precio real, llenado |
| `verificacion-cruzada` | La evidencia de que todo cuadra entre sí |

### Una conclusión sobre IA, siempre

Toda propuesta dice por escrito si el alcance requiere servicios de inteligencia artificial y por qué. Si **no** los requiere, el archivo `05` no se genera, pero la razón queda en las consideraciones técnicas. «No se mencionó» nunca es una respuesta.

## Cómo revisar la propuesta

- **La matriz de cumplimiento:** ¿cada requerimiento tiene respuesta? Fíjate en los que dicen **«Cumple parcialmente»** o **«No cumple»**: el agente los declara a propósito para que tú decidas qué hacer.
- **Los obligatorios que no se cumplen** son un bloqueante: pueden significar que el proceso no es viable tal como está planteado.
- **El plazo:** ¿el cronograma cabe en lo que exige el RFP con el equipo propuesto?
- **Las aclaraciones:** ¿la propuesta refleja la versión vigente del proceso?
- **Los dos modelos de costos:** los totales deben cuadrar, y cualquier diferencia debe estar explicada.
- **Los pendientes:** busca las marcas `[PENDIENTE: ...]` y resuélvelas antes de radicar.
- **La conclusión sobre IA:** ¿dice sí o no, y por qué?

> [!nota] La matriz es una herramienta de decisión
> No es un documento de ventas. Si el agente marcara todo como «Cumple», la matriz perdería su valor. Prefiere decirte con claridad qué no se puede cumplir.

## Cuando el plazo no alcanza

Si las horas necesarias no caben en el plazo con el equipo propuesto, el agente **te lo dice con los números** y te presenta las opciones reales: ampliar el equipo (con su impacto en el precio), negociar plazo o alcance mediante aclaraciones, o desistir del proceso. **No ajusta la estimación para que el cronograma «cuadre».**

## Lo que el agente no hace

| Si le pides… | Qué pasa | Qué hacer |
|---|---|---|
| Que invente una certificación, una referencia o una capacidad | No lo hace: solo usa los documentos y el brief de la empresa | Aporta el soporte o déjalo como pendiente |
| Que ignore una aclaración «para simplificar» | No lo hace: las aclaraciones prevalecen | Si crees que hay un error, plantéalo con la cita |
| Que marque un requerimiento como cumplido sin sustento | No lo hace | Dale la información de cómo se cumple |
| Que entregue solo el modelo de costos de cotización | No lo hace: los dos se llenan y se concilian | Asegúrate de tener ambos modelos |
| Que acorte la estimación para que quepa en el plazo | No lo hace | Decide entre ampliar equipo, negociar o desistir |
| Que use información de otra licitación | No lo hace: cada proceso es reservado | Aporta los datos del proceso actual |

## Preguntas frecuentes

**¿Por qué hace tantas preguntas?**
Porque los documentos casi siempre tienen huecos y él no los rellena por su cuenta. Las agrupa para que respondas todo de una vez.

**¿Y si las aclaraciones cambian el alcance?**
Prevalecen. Si el cambio afecta de forma importante el precio o el alcance, te consulta antes de decidir.

**¿Por qué no hay análisis de IA?**
Porque el alcance no la requiere. La razón queda escrita en las consideraciones técnicas; solo se genera el archivo de IA cuando sí hace falta.

**¿Qué es la verificación cruzada?**
Una revisión final que comprueba que todo coincide: que cada requerimiento tiene respuesta, que las horas corresponden a los módulos, que el cronograma cabe en el plazo y que los totales cuadran.

**¿Se mezclan datos entre licitaciones?**
No. Cada proceso vive en su propia carpeta y su información es reservada.

**¿Puedo cambiar algo después de la verificación?**
Sí, pero pídele que vuelva a verificar: un cambio puede afectar las horas, los costos o la matriz.

## Glosario

| Término | Qué significa |
|---|---|
| RFP | *Request for Proposal*: el documento oficial que describe lo que la empresa necesita |
| Aclaraciones | Preguntas y respuestas del proceso, que pueden cambiar el alcance |
| Adenda | Una modificación formal al documento original |
| Matriz de cumplimiento | La tabla que responde cada requerimiento del RFP |
| Modelo de costos | La plantilla de Excel donde se calcula el precio |
| Conciliar | Comparar dos totales y explicar cada diferencia |
| Tokens | La unidad en que se mide el uso de los modelos de IA |
| Radicar | Presentar formalmente la propuesta a la entidad |

## Si algo no funciona

Si el agente no encuentra un documento, revisa que esté en la carpeta del proceso con un nombre claro. Si los totales no cuadran o la propuesta parece incompleta, revisa la verificación cruzada: ahí quedan los hallazgos. Si el problema persiste, avisa a quien mantiene el agente; su guía técnica explica cada habilidad en detalle.
