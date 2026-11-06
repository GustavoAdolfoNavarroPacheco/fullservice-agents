---
titulo: multifunctional-agent: cómo unificar facturas y transcribir un audio
resumen: Cómo invocar el agente, qué entregarle en cada funcionalidad, qué hace paso a paso y qué revisar en el Word y el PDF que recibes.
---

## Descripción general

El **Agente Multifuncional** (`multifunctional-agent`) resuelve las tareas operativas que se repiten en Full Service y que no pertenecen a una etapa del flujo comercial. Hoy hace **dos cosas**, y en las dos entrega lo mismo: **un documento Word y un PDF** con el diseño de Campuslands.

```cards
Unificación de facturas | Le das varias facturas o recibos (PDF o imagen) y te devuelve un solo documento con todas, en orden cronológico, una por hoja, bajo el banner de Campuslands.
Transcriptor de audio | Le das el audio de una reunión y te devuelve la transcripción por partes de 5 minutos, con quién habla en cada momento y su marca de tiempo.
```

```stats
2 | funcionalidades: facturas y transcripción de audio
2 | entregables por trabajo: un Word y un PDF idénticos
100 % | local: ni las facturas ni los audios salen de tu equipo
```

> [!nota] Es un agente aparte del flujo comercial
> No es una etapa entre el alcance y el contrato: cualquier persona del equipo lo usa cuando la tarea lo pide. Si transcribes una reunión con un cliente, esa transcripción puede servir después como fuente para el alcance funcional (`functional-scope`).

## Cómo se invoca

Abre Claude Code en la carpeta del repositorio y escribe el comando:

```prompt
/multifunctional-agent
```

También puedes decirle la funcionalidad desde el principio, con o sin archivos:

| Escribes | Qué hace el agente |
|---|---|
| `/multifunctional-agent` | Te hace **la pregunta clave** y espera tu respuesta |
| `/multifunctional-agent facturas` | Empieza la unificación de facturas |
| `/multifunctional-agent audio` | Empieza la transcripción de audio |
| Un mensaje que ya lo deja claro («unifica estas facturas», un `.mp3` adjunto y «transcríbelo») | No pregunta: dice en una línea qué funcionalidad toma y empieza |

### La pregunta clave

Si no dijiste qué quieres, **lo primero que hace el agente es esta pregunta**, y nada más: no pide archivos ni explica antes.

```chat
Tú: /multifunctional-agent
Agente: ¿Con qué funcionalidad quieres proceder? 1. Unificación de facturas: varias facturas, un Word y un PDF en orden cronológico. 2. Transcriptor de audio: un audio, un Word y un PDF con la transcripción por partes y hablantes.
Tú: 1
Agente: Perfecto. Indícame la carpeta o los archivos con las facturas.
```

Contestas «1» o «2» (o eliges la opción en pantalla). Con tu respuesta pide solo lo necesario, sin entrevistas. Al terminar una funcionalidad te ofrece la otra en una línea; **nunca cambia de funcionalidad por su cuenta**.

## Funcionalidad 1: unificación de facturas

### Qué entregarle

Los recibos o facturas que quieres reunir, como **PDF o imagen** (`.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.tif`, `.gif`). Pueden venir con cualquier nombre y mezclados: el agente los ordena por lo que dice cada recibo.

> [!importante] El orden lo manda el recibo, no el nombre del archivo
> Los nombres de archivo suelen estar mal. En el caso que dio origen al agente, dos facturas tenían las horas **cruzadas**: la llamada `13h31m` era el viaje de las 3:31 p. m. y la `15h47m` el de la 1:47 p. m. Ordenar por nombre habría invertido las dos. El agente usa siempre la fecha y la hora que **ve en el recibo** y, si el nombre lo contradice, deja una nota visible en el documento.

### Paso a paso

```lanes
Tú | Dale las facturas (una carpeta o los archivos sueltos)
Agente | Copia los originales a la entrada del lote, sin tocarlos
Agente | Lee cada recibo y propone fecha, proveedor y tipo
Agente | Abre cada recibo a la vista y confirma o corrige esos datos
Agente | Ordena, arma el Word y lo convierte a PDF
Agente | Mira el PDF página por página antes de entregar
Tú | Revisas el resultado y los avisos
```

1. **Recepción.** Crea una carpeta de trabajo para el lote (`trabajos/facturas/<fecha>-<nombre>/`) y copia ahí tus facturas. Tus originales no se mueven, no se renombran y no se editan.
2. **Detección.** Un script lee el texto de cada recibo y propone la fecha, la hora, el proveedor y el tipo.
3. **Confirmación a la vista.** El agente abre **cada** recibo y confirma o corrige lo que propuso el script. En una imagen o un escaneo no hay texto que leer: ahí su lectura a la vista es la única fuente.
4. **Construcción.** Ordena por fecha y hora, genera el Word, lo convierte a PDF y comprueba que cada factura quedó en su hoja.
5. **Revisión visual.** Renderiza el PDF y mira cada página: el banner, el recibo completo y legible, el pie «Pág. N/M».
6. **Entrega.** Te da las rutas del Word y del PDF, una tabla con el orden final y los avisos.

### Qué recibes

El documento sigue siempre el mismo diseño:

- **Una factura por hoja**, sobre la plantilla Word de Campuslands (membrete con logo), en hoja vertical y con tipografía Poppins.
- Sobre cada recibo, un **banner** de una sola franja con cuatro celdas iguales:

| Celda | Qué dice | Ejemplo |
|---|---|---|
| **FACTURA** | Su posición en el lote | `01 / 4` |
| **FECHA** | La fecha del recibo | Mié 28 oct 2026 |
| **TIPO** | Transporte, Alimentación, Hospedaje, Peajes y parqueadero, Combustible, Software y nube u Otro | Transporte |
| **PROVEEDOR** | Quién emitió el recibo | inDrive |

- El recibo se muestra **completo**: solo se le quita el blanco alrededor y se le pone un marco; no se recorta ni se cambia nada de lo que dice.
- Bajo el recibo, una leyenda pequeña con el nombre del archivo original y, si hace falta, una nota.
- Un recibo de dos páginas va una sobre otra en la misma hoja solo si se sigue leyendo bien; si no, una hoja por página con el banner **FACTURA (CONT.)**. Desde tres páginas, siempre una hoja por página.

> [!nota] La hora se usa para ordenar, pero no se imprime
> El banner muestra la fecha y no la hora. La hora sigue sirviendo para ordenar las facturas de un mismo día. Si un recibo no trae hora, queda al final de su día y el agente te lo avisa.

### Ejemplo de conversación

```chat
Tú: /multifunctional-agent facturas. Aquí están los recibos de mi viaje a Bogotá.
Agente: Procedo con la funcionalidad 1: Unificación de facturas. Copié los 4 recibos al lote y los revisé uno por uno.
Agente: Listo: Facturas_28-29_Octubre_2026_Campuslands.docx y .pdf, con 4 hojas. Aviso: en dos archivos el nombre no coincidía con el recibo y usé los datos del recibo; quedó una nota en esas hojas.
```

## Funcionalidad 2: transcriptor de audio

### Qué entregarle

- **Un audio o un video** de la reunión (`.mp3`, `.mp4`, `.m4a`, `.wav`, `.ogg`, `.webm`, `.mkv`…).
- Opcional, pero útil: los **nombres propios y términos del proyecto** que se mencionan en la reunión (personas, entidades, siglas), y **cuántas personas hablan**, si lo sabes. Mejoran el resultado.
- Si ya tienes la transcripción hecha **con marcas de tiempo**, también sirve: el agente la convierte al formato y arma el documento sin transcribir de nuevo.

> [!importante] El audio no sale de tu equipo
> La transcripción corre **en local**. El audio de una reunión con un cliente es información del cliente, así que el agente nunca lo sube a una web, una API ni otra IA, salvo que tú lo pidas expresamente.

### La primera vez: el motor de audio

Para transcribir, el equipo necesita unos programas y unos modelos de voz. Si faltan, el agente **te dice qué instalaría y cuánto pesa, y espera tu «sí»** antes de hacerlo:

| Qué | Para qué | Peso aproximado |
|---|---|---|
| Paquetes de Python (`faster-whisper`, `sherpa-onnx`) | Pasar la voz a texto y separar a los hablantes | Pocos MB |
| Modelo de voz `large-v3-turbo` | La transcripción en sí; se baja la primera vez que se usa | ≈ 1,6 GB |
| Modelos de separación de hablantes | Saber quién habla en cada momento | ≈ 45 MB |

Después de esa primera vez ya no se vuelve a instalar nada.

### Paso a paso

```lanes
Tú | Dale el audio y, si los sabes, nombres propios y número de hablantes
Agente | Prepara la carpeta del trabajo y comprueba el motor local
Agente | Transcribe el audio en tu equipo (puede tardar)
Agente | Lee y corrige la transcripción, sin cambiar lo dicho
Agente | Arma el Word y el PDF y los revisa a la vista
Tú | Revisas los hablantes propuestos y escuchas unos tramos
```

1. **Recepción.** Crea la carpeta `trabajos/transcripciones/<nombre>/` y copia ahí el audio (queda fuera de Git).
2. **Motor.** Comprueba que todo lo necesario esté instalado; si no, pide permiso (ver arriba).
3. **Transcripción.** Pasa el audio a texto con marcas de tiempo y separa a los hablantes. **Tarda**: con el modelo por defecto, del orden de la duración del audio en un computador sin tarjeta gráfica. Para audios largos corre en segundo plano y te avisa el avance.
4. **Revisión.** El agente lee la transcripción completa y corrige solo tres cosas: los **nombres de hablantes** que el audio revele, los **nombres propios o términos mal oídos** (de forma consistente en todo el texto) y las **frases repetidas** por el motor. Lo dudoso queda como `[inaudible]`. Anota cada cambio relevante en un archivo de notas.
5. **Construcción.** Genera el Word y el PDF. Si después alguien corrige el texto, se vuelve a armar el documento sin transcribir otra vez.
6. **Revisión visual.** Mira la primera página, un cambio de parte y la última.
7. **Entrega.** Rutas, duración, número de partes e intervenciones, hablantes propuestos y una advertencia (ver más abajo).

### Cómo es el documento

La estructura es **la de la transcripción de referencia, sin cambios**:

```tree
Transcripción de Audio Completo
  Cuadro de datos          # audio, duración, fecha y participantes
  Parte 1                  # una parte por cada 5 minutos de audio
    [00:00 - 00:02] Hablante 1 (Hombre): texto de la intervención
    [00:43 - 00:45] Hablante 3 (Gabriela): texto de la intervención
  Parte 2                  # los tiempos reinician en 00:00
    [00:00 - 00:04] Hablante 1 (Hombre): …
```

- **Partes de 5 minutos.** Cada parte reinicia el tiempo en `00:00`, y ninguna intervención cruza el corte.
- **Una línea por intervención**, con el tiempo, el hablante y lo que dijo, palabra por palabra.
- **Etiqueta del hablante:** su **nombre** si el audio lo revela; si no, **Hombre** o **Mujer**; si tampoco se sabe, solo «Hablante N».
- Acotaciones no verbales como `[Risas]` o `[Asiente]` solo si la transcripción que tú traes ya las tenía; el motor no las genera y el agente no las inventa.
- Diseño de Campuslands: membrete de la plantilla, título en azul con filete verde, tiempos en verde, hablantes en azul y pie «Página N».

### Ejemplo de conversación

```chat
Tú: Transcribe esta reunión con la Alcaldía. Participan Gabriela y dos personas más; se habla del PETI y de la Alcaldía de Girón.
Agente: Procedo con la funcionalidad 2: Transcriptor de audio. Falta instalar el motor local (≈ 1,6 GB para el modelo de voz y ≈ 45 MB para separar hablantes). ¿Lo instalo?
Tú: Sí.
Agente: Listo. Transcripción de 51 min en 11 partes y 142 intervenciones. Hablantes propuestos: 1 (Hombre), 2 (Hombre), 3 (Gabriela, porque se dirigen a ella por su nombre). Esta transcripción es automática y no está verificada de oído: te sugiero escuchar tres tramos: Parte 1 en 00:43, Parte 3 en 02:10 y Parte 5 en 03:25.
```

### Qué hacer si el resultado sale flojo

| Si pasa esto | Pídele |
|---|---|
| Nombres propios y siglas mal escritas | Que repita con el **vocabulario** del proyecto (nombres, entidades, términos) |
| Más o menos hablantes de los que hay | Que repita indicando **cuántas personas** participan |
| Frases sin sentido o inventadas | Que repita con un modelo más preciso; el modelo `small` es más rápido pero **no sirve para una entrega** |
| Audio de sala con voces que se pisan | Nada lo arregla del todo: mejora con micrófono cercano y una persona a la vez. Escucha los tramos dudosos |

## Qué avisos te dará el agente

Estos avisos van siempre en el mensaje de entrega. No son un trámite: te dicen dónde mirar.

> [!cuidado] La transcripción automática no está verificada de oído
> El agente no puede escuchar el audio. Transcribe con un motor automático y lo revisa leyendo, pero **no contrasta con el sonido**. Con una reunión de varias personas en una sala, espera errores en nombres propios y cifras. Por eso te propone 2 o 3 marcas de tiempo para que las escuches y compares. Para una reunión importante, esa comprobación es tuya.

> [!importante] Los nombres de los hablantes y el género son propuestas
> Un hablante recibe nombre **solo si alguien lo nombra o se dirige a él** en el audio. «Hombre» o «Mujer» es una **estimación por el tono de voz**, no un dato. Los ves marcados como `PROPUESTO` para que los confirmes o corrijas.

Y en facturas:

- **Discrepancias de nombre de archivo.** Cuando el nombre contradice al recibo, ganó el recibo.
- **Facturas sin hora.** Quedaron al final de su día.
- **Fechas dudosas.** Si un recibo no trae fecha, es lo único que el agente te pregunta.

## Cómo revisar el resultado

**Facturas**

- **¿El orden es cronológico según los recibos?** Compara la tabla de entrega con las fechas de los recibos.
- **¿Cada factura está en su hoja?** Y completa, sin partes cortadas.
- **¿El banner coincide con el recibo?** Fecha, tipo y proveedor.
- **¿Se lee bien?** Cada recibo, sobre todo los de dos páginas.

**Transcripción**

- **¿Los nombres propios están bien escritos y todos igual?**
- **¿Los hablantes tienen sentido?** Confirma o corrige los nombres propuestos.
- **¿Las cifras y fechas coinciden con lo que se dijo?** Escucha los tramos que propuso el agente.
- **¿Hay partes de 5 minutos y los tiempos reinician en `00:00`?**

## Comandos rápidos con «!»

Además de pedirle las cosas con tus palabras, puedes darle una **orden corta** escribiendo `!` antes de la palabra, por ejemplo `!validate`. Cuando el agente reconoce un comando, **lo cumple siempre**, y lo primero que escribe en su respuesta es qué comandos recibió.

- Puedes escribirlo solo o con un texto: `!validate las facturas`.
- Puedes combinar varios: `!plan !no-assumptions`.
- Vale para la tarea en curso; en una tarea nueva se escribe de nuevo.
- `!help` muestra la lista de comandos de este agente.

> [!tip] Los más útiles aquí
> `!plan` te muestra cómo procesará el lote o el audio y espera tu aprobación. `!audit` busca discrepancias entre el nombre de cada archivo y el recibo. `!visual-audit` revisa el PDF página por página.

> [!nota] Lo que un comando no cambia
> Un comando no permite saltarse las reglas del agente (no inventar datos, la confidencialidad, las verificaciones obligatorias). Si pides algo que una regla impide, el agente hace todo lo permitido y te dice en una frase qué no pudo y por qué.

Estos son los comandos de este agente:

```comandos
```

## Límites del agente

| Si le pides… | Qué pasa | Qué hacer |
|---|---|---|
| Que ordene las facturas por el nombre del archivo | No lo hace: ordena por lo que dice el recibo | Si el recibo está mal o ilegible, díselo y dile el dato correcto |
| Que invente la fecha de un recibo que no la trae | No lo hace: te la pregunta | Dale la fecha |
| Que rediseñe el banner por su cuenta | No lo hace: el banner vigente solo cambia cuando lo pides | Pídelo expresamente |
| Que suba el audio a una web o a otra IA para transcribirlo | No lo hace sin tu permiso expreso | Si tienes permiso del cliente, díselo de forma explícita |
| Que ponga el nombre a un hablante que nadie nombró | No lo hace: queda «Hombre», «Mujer» o «Hablante N» | Confirma el nombre tú y pídele que lo corrija en todas las líneas |
| Que resuma o «mejore» lo que se dijo | No lo hace: la transcripción es literal | Pide un resumen aparte, como otra tarea |
| Que entregue sin mirar el PDF | No lo hace: siempre lo revisa a la vista | Nada: es una protección |

## Preguntas frecuentes

**¿Por qué me pregunta qué funcionalidad quiero?**
Porque hace dos cosas muy distintas. Si ya se lo dijiste en tu mensaje, no pregunta.

**¿Puedo mezclar facturas de personas o clientes distintos en un lote?**
No lo mezcles. Un lote es un trabajo: el agente no mezcla lotes ni clientes.

**¿Se modifican mis archivos originales?**
Nunca. Se copian a la carpeta de entrada del trabajo y ahí quedan tal cual.

**¿Por qué el banner no muestra la hora?**
Fue una decisión de diseño. La hora sigue usándose para ordenar, pero no se imprime.

**¿Puedo editar el Word?**
Sí. El PDF sale de convertir ese mismo Word, así que son idénticos; si cambias el Word, vuelve a exportar el PDF.

**¿Cuánto tarda una transcripción?**
Más o menos lo que dura el audio, en un computador sin tarjeta gráfica. Una reunión de 50 minutos tarda cerca de 50 minutos; el agente la lanza en segundo plano.

**¿Qué pasa si mi transcripción ya está hecha en otra herramienta?**
Si trae marcas de tiempo, el agente la convierte y arma el documento. Si no las trae, **no las inventa**: te lo dice y te propone transcribir el audio.

**¿Los audios quedan guardados en el repositorio?**
No. Los audios están excluidos de Git por ser pesados y confidenciales; solo se guardan en tu equipo.

## Glosario

| Término | Qué significa |
|---|---|
| Lote | Un conjunto de facturas que se unifican en un solo documento |
| Banner | La franja con número, fecha, tipo y proveedor sobre cada factura |
| Manifiesto | El archivo donde el agente anota fecha, proveedor y tipo de cada factura antes de armar el documento |
| Diarización | Separar quién habla en cada momento de un audio |
| Hablante | Cada voz distinta que el motor detecta en el audio |
| Parte | Un tramo de 5 minutos de la transcripción |
| `PROPUESTO` | Dato que el agente sugiere y tú debes confirmar |
| `[inaudible]` | Un tramo que no se pudo entender y no se inventó |

## Solución de problemas

Si el agente no encuentra tus archivos, revisa que estén en la carpeta que le indicaste. Si la transcripción tarda más de lo esperado, es normal en audios largos: está trabajando en segundo plano. Si algo falla al instalar el motor de audio o al convertir a PDF, avisa a quien mantiene el agente; su guía técnica explica cada pieza.
