---
titulo: Alcances Funcionales: cómo obtener el documento de alcance de un proyecto
resumen: Qué archivos entregarle, qué recibes, cómo leer los estados y los pendientes y cómo revisar el documento antes de enviarlo al cliente.
---

## En resumen

El **Agente de Alcances Funcionales** lee los archivos de un proyecto (propuestas, actas de reunión, cotizaciones, notas, correos) y redacta con ellos el **documento de alcance funcional** que se entrega al cliente: qué incluye el proyecto, qué no, cómo se aceptará cada entrega y qué falta por definir.

Su regla principal es **no inventar compromisos**. Todo lo que escribe sale de tus archivos; lo que no está, queda marcado como pendiente para que alguien lo resuelva. Y trabaja rápido: analiza todo y te entrega un borrador en el mismo momento, sin entrevistarte.

```stats
0 | compromisos inventados: solo lo que dicen tus archivos
3 | estados para cada dato: confirmado, propuesto o pendiente
1 | documento en Word editable, más un resumen y la lista de pendientes
```

> [!tip] Si solo tienes un minuto
> Deja los archivos del proyecto en la carpeta del cliente y escríbele: «Haz el alcance funcional de este proyecto». Eso es todo lo que necesita para empezar.

## Para qué sirve

Úsalo cuando tengas un proyecto con información dispersa (una propuesta aprobada, varias actas, una cotización) y necesites **un único documento claro** para el cliente y para el equipo técnico. Es especialmente útil cuando las fuentes se contradicen o tienen vacíos, porque el agente los detecta y los muestra en lugar de ocultarlos.

### Qué no es

No reemplaza la aprobación de nadie. El documento resultante necesita revisión **técnica, comercial y jurídica** antes de firmarse, y el agente la pide donde corresponde. Tampoco es un contrato: es la descripción funcional del proyecto.

## Antes de empezar

Reúne y deja en la carpeta del cliente todo lo que tengas del proyecto:

- **La propuesta o cotización aprobada**: es la referencia para precio, plazo y condiciones.
- **Las actas de reunión y correos** relevantes.
- **Notas** que expliquen lo que el cliente espera.
- **Versiones anteriores del documento**, si existen.

> [!importante] Lo que compartes es todo lo que hay
> El agente asume que los archivos que le das **son toda la información disponible**. No te hará preguntas sobre lo que falta: lo marcará como pendiente. Por eso conviene que no omitas ningún documento importante.

### Dónde dejar los archivos

Cada proyecto tiene su carpeta dentro de `alcances`, con tres subcarpetas:

```tree
alcances/
  <nombre-del-cliente>/
    fuentes/      # aquí van tus archivos; el agente no los modifica
    trabajo/      # el agente deja aquí su análisis
    entrega/      # aquí queda el documento Word
```

## Paso a paso

```lanes
Tú | Deja los archivos en la carpeta fuentes del cliente
Tú | Pídele el alcance funcional del proyecto
Agente | Lee todo, detecta contradicciones y vacíos
Agente | Redacta el documento y te entrega un resumen
Tú | Revisa los pendientes con sus responsables
```

### 1. Deja los archivos

Cópialos a `fuentes/` dentro de la carpeta del cliente.

### 2. Pídele el alcance

Dile el nombre del proyecto y qué documento necesitas. Si hay más de una versión de un archivo, puedes indicarle cuál es la vigente.

### 3. El agente analiza y redacta

Lee todo, arma una matriz con cada dato y su fuente, clasifica los vacíos y escribe el documento **en el mismo turno**. Solo te preguntará algo si, sin la respuesta, no puede ni empezar (por ejemplo, si dos archivos se contradicen y no sabe cuál es el principal). Entonces te hará **una sola pregunta** y te dirá qué asumirá por defecto.

### 4. Recibe el resumen

Te responde con un mensaje corto: cuántos módulos identificó, cuántos pendientes bloqueantes encontró, qué archivo redactó y los hallazgos más importantes, con la ruta a la lista de validaciones.

### 5. Resuelve los pendientes

Cada pendiente tiene un responsable asignado. Cuando alguien lo resuelva, cuéntaselo al agente y actualizará el documento.

## Ejemplos de conversación

### Empezar

```chat
Tú: Tengo la propuesta y las actas del proyecto de la Alcaldía. Haz el alcance funcional.
Agente: He revisado la información del proyecto. Identifiqué 8 módulos y 6 pendientes bloqueantes. Redacté el borrador solo con lo que dicen las fuentes; lo que no dicen está marcado como pendiente de validación. La lista de validaciones por responsable está en la carpeta de trabajo.
```

### Ver lo pendiente

```chat
Tú: Dame la lista de pendientes bloqueantes y quién debe resolver cada uno.
Agente: Aquí están los 6 pendientes bloqueantes, con su impacto y el responsable de cada uno: integración con el sistema de recaudo, condiciones de soporte, titularidad de los desarrollos…
```

### Incorporar una decisión

```chat
Tú: El cliente confirmó que el soporte será de lunes a viernes de 8 a 5. Actualiza el documento.
Agente: Registré la decisión, cambié el estado del soporte a confirmado en las secciones que lo mencionan y actualicé la lista de pendientes.
```

### Una versión nueva

```chat
Tú: Genera la versión 0.2 con estos cambios, sin borrar la 0.1.
Agente: Listo. La versión 0.2 quedó en la carpeta de entrega; la 0.1 se conserva sin cambios.
```

## Qué recibes

```cards
El documento en Word | Editable, con portada, carta de presentación, tabla de contenido, 16 secciones, anexos y hoja de firmas.
Un resumen de cambios | Lo más importante que encontró el agente, en pocas líneas.
El registro de pendientes | Cada duda, con su prioridad y el responsable que debe resolverla.
Los archivos de trabajo | Inventario de fuentes, matriz de información, decisiones y control de calidad, por si quieres revisar el método.
```

### Cómo es el documento

Siempre tiene el mismo orden:

1. **Portada.** Título, cliente, quién prepara el documento y la fecha.
2. **Carta de presentación.** Una hoja que explica qué contiene el documento.
3. **Tabla de contenido.** Ya generada, lista para usar.
4. **Contenido.** Resumen ejecutivo, contexto, alcance, usuarios y permisos, requerimientos funcionales, integraciones, IA, requerimientos no funcionales, arquitectura, entregables y aceptación, cronograma, capacitación, garantía y soporte, condiciones comerciales, supuestos y riesgos, y anexos.
5. **Aprobación y firmas.** La hoja final, con espacio para ambas partes.

> [!nota] Lo que no verás dentro del documento
> No lleva número de versión (esa información está en el nombre del archivo), ni clasificación, ni la palabra «borrador». El estado del documento te lo dice el agente en el chat.

## Los tres estados de cada dato

Todo lo que se afirma en el documento tiene un estado, para que nunca confundas una idea con un compromiso:

```cards
CONFIRMADO | Hay un documento o una aprobación que lo respalda. Se puede tratar como acordado.
PROPUESTO | Es una recomendación que todavía nadie aceptó. No es un compromiso.
PENDIENTE | Falta definirlo. Aparece como «[PENDIENTE DE VALIDACIÓN]» y tiene un responsable.
```

### Qué tan graves son los pendientes

| Nivel | Significa | Qué pasa |
|---|---|---|
| **Bloqueante** | Impide definir alcance, costo, plazo, aceptación o responsabilidades | Mientras haya alguno abierto, el documento es solo un borrador |
| **Importante** | Afecta la operación o la experiencia, pero no impide avanzar | Se resuelve durante la revisión |
| **Editorial** | Es un asunto de redacción o presentación | Se corrige al final |

## Cómo revisar el documento

- **¿El orden es el esperado?** Portada, carta, tabla de contenido, contenido y firmas.
- **¿Los datos comerciales coinciden con tu propuesta aprobada?** Costo, plazo y condiciones deben ser exactamente los acordados.
- **¿Las contradicciones están a la vista?** Si dos archivos chocan, el documento debe mostrar **las dos versiones**, con su fuente, no elegir una en silencio.
- **¿Lo futuro está donde corresponde?** Las ideas para fases siguientes solo aparecen en «Fases futuras», nunca como entregables actuales.
- **¿Cada pendiente tiene responsable?** Revisa que sean las personas correctas.
- **¿Hay promesas que no podemos cumplir?** El agente evita frases como «garantizará ahorro», pero revisa igual.
- **¿Pasó la revisión de las tres áreas?** Técnica, comercial y jurídica, antes de enviarlo al cliente.

### Estados del documento

| Estado | Qué significa |
|---|---|
| Borrador | Hay pendientes bloqueantes abiertos o no pasó el control de calidad |
| Apto para revisión final | Pasó el control de calidad; faltan las revisiones técnica, comercial y jurídica |
| Aprobado por cliente | El cliente lo validó o firmó |

> [!importante] Nunca «listo para firma» con bloqueantes abiertos
> Si te piden un documento para firma y todavía hay pendientes bloqueantes, el agente te entregará un borrador con la lista de validaciones, no un documento «listo». Es una protección: firmar con vacíos genera problemas después.

## Lo que el agente no hace

| Si le pides… | Qué pasa | Qué hacer |
|---|---|---|
| Que invente una cifra, un plazo o un nivel de servicio | No lo hace: lo marca como pendiente | Consigue el dato con el responsable y avísale |
| Que redacte el precio, la garantía o el soporte «como suele ser» | No lo hace: solo escribe lo que dice la fuente | Aporta la propuesta o el acuerdo donde aparece |
| Que ponga una idea futura como entregable | No lo hace: va en «Fases futuras» | Si ya se acordó, entrégale la fuente que lo confirma |
| Que elija entre dos versiones contradictorias | Muestra ambas y espera que alguien decida | Dile cuál prevalece y quién lo confirmó |
| Que declare el documento «listo para firma» con bloqueantes | No lo hace | Resuelve primero los pendientes |

## Preguntas frecuentes

**¿Por qué no me hace preguntas?**
Porque asume que tus archivos son todo lo que hay. Lo que falta queda como pendiente en lugar de adivinarse.

**¿Puedo editar el Word?**
Sí, es editable. Para cambios grandes o de estructura, pídele una versión nueva: así queda registrada y actualiza las matrices.

**¿Dónde aparece el número de versión?**
Solo en el nombre del archivo (por ejemplo, `v0.2`), nunca dentro del documento.

**¿Qué hago con un pendiente?**
Pásaselo a su responsable. Cuando lo resuelva, cuéntale al agente la decisión y de dónde viene (acta, correo, mensaje).

**¿Se pueden usar los ejemplos de otros proyectos?**
No. Los ejemplos de la wiki sirven para enseñar el método de análisis; sus módulos, cifras y condiciones no se trasladan a ningún otro proyecto.

**¿El documento tiene mi firma?**
Solo si pides un documento listo para firma. En los borradores la firma de la representante legal no se inserta.

## Glosario

| Término | Qué significa |
|---|---|
| Alcance funcional | La descripción de lo que hará el sistema y lo que no |
| Módulo | Un conjunto de funcionalidades relacionadas (por ejemplo, «Reportes») |
| Ficha funcional | La descripción uniforme de una funcionalidad: objetivo, flujo, reglas, salidas y cómo se acepta |
| Criterio de aceptación | La prueba observable que demuestra que algo se entregó bien |
| Integración | La conexión del sistema con otro sistema |
| SLA | Nivel de servicio acordado, como tiempos de respuesta |
| Pendiente bloqueante | Un dato faltante que impide cerrar el alcance |
| Trazabilidad | Poder saber de dónde sale cada dato |

## Si algo no funciona

Si el agente no encuentra un archivo, revisa que esté en la carpeta `fuentes` del cliente. Si el documento te parece incompleto, revisa primero la lista de pendientes: lo que falta suele estar ahí. Si el comportamiento se repite o parece una falla, avisa a quien mantiene el agente; su guía técnica explica el flujo completo.
