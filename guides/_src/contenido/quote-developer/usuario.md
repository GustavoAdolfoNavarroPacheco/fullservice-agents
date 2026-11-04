---
titulo: quote-developer: cómo obtener el PDF y el Excel de una cotización
resumen: Qué necesitas darle al agente, qué recibes, cómo validar el alcance y los precios, y cómo pedir ajustes.
---

## En resumen

El **Desarrollador de Cotizaciones** (`quote-developer`) convierte lo que tu cliente necesita en dos archivos que cuentan lo mismo: un **PDF** con el alcance del proyecto dividido por módulos y con su precio, y un **Excel** con las horas de trabajo de cada especialidad y el costo calculado por las fórmulas del equipo.

Tú compartes los alcances; el agente redacta, estima y llena los archivos. Primero validas el contenido del PDF y después se calculan los precios, para que nunca discutas un precio sobre un alcance que todavía no estaba claro.

```stats
2 | archivos que recibes: un PDF de alcance y un Excel de cotización
0 | alcance inventado: solo escribe lo que tú le diste o confirmaste
3 | niveles de detalle: módulo, submódulo y funcionalidad
```

> [!tip] Si solo tienes un minuto
> Pásale el documento de alcances y el nombre completo del cliente. Si algo no está claro, te lo preguntará antes de estimar.

## Para qué sirve

Úsalo cuando tengas el alcance de un proyecto y necesites **cotizarlo**: describir qué se va a construir, cuánto esfuerzo requiere cada parte y cuánto cuesta. Funciona para proyectos pequeños, de un solo módulo, y para portafolios grandes de varios proyectos.

### Cómo se organiza una cotización

Toda cotización tiene la misma estructura, de lo general a lo específico:

```flow
Módulo | Una gran área del proyecto. Por ejemplo, «Gestión de usuarios».
Submódulo | Una agrupación dentro del módulo. Por ejemplo, «Roles y permisos».
Funcionalidad | Una capacidad concreta, con su propio esfuerzo y su propio precio.
```

La cantidad de funcionalidades que tiene cada submódulo **depende de lo que el alcance realmente describe**: una, o varias. El agente nunca fuerza un número fijo, ni junta varias cosas distintas en una para ahorrar espacio.

## Antes de empezar

Reúne:

- **Los alcances del proyecto:** un documento, notas de reunión, el brief o el texto que describe lo que el cliente necesita.
- **El nombre o razón social del cliente.**
- **El nombre del proyecto,** si el cliente tiene varios y quieres cotizarlos por separado.
- Si existe, un **documento con esfuerzo ya estimado** (por ejemplo, horas por rol): el agente lo usa como base en lugar de estimar desde cero.

> [!importante] Todo sale de lo que tú compartes
> El agente no completa huecos con texto genérico. Si falta un dato para cotizar con precisión, **te lo pregunta**. Contesta con lo que sepas; si no lo sabes, dilo para que quede registrado.

## Paso a paso

```lanes
Tú | Comparte los alcances y el nombre del cliente
Agente | Te pregunta lo que no esté claro
Agente | Redacta el PDF de alcance, aún sin precios
Tú | Revisa y valida el contenido del PDF
Agente | Llena el Excel y calcula los costos
Agente | Actualiza el PDF con los precios reales y verifica
Tú | Revisa los precios y los pendientes
```

### 1. Comparte el alcance

Pega o adjunta lo que tengas. Si el cliente tiene varios proyectos, dile cuál quieres cotizar primero.

### 2. Responde las dudas

Si hay una ambigüedad (por ejemplo, no queda claro si dos funcionalidades son la misma), el agente te preguntará antes de seguir. Prefiere preguntar a asumir.

### 3. Valida el PDF

Primero recibes el PDF con el alcance por módulos y, en la columna de valor, la leyenda **«Pendiente de costear»**. Este es el momento de decir si falta algo, sobra algo o está mal explicado. **Aún no hay precios.**

### 4. Se calculan los costos

Con tu validación, el agente llena el Excel: estima los días de cada funcionalidad por especialidad (diseño, backend, frontend, QA…) y las fórmulas del equipo calculan los costos.

### 5. Recibes el PDF con precios

El agente reemplaza «Pendiente de costear» por los precios reales, leídos del Excel, nunca escritos a mano. Y comprueba que cada precio y cada total del PDF coincida con el Excel.

## Ejemplos de conversación

### Empezar

```chat
Tú: Necesito la cotización para Marval. Aquí está el documento de alcances.
Agente: Perfecto. Antes de redactar necesito confirmar el nombre completo del cliente y si hay un solo proyecto o varios. ¿Hay algún documento con esfuerzo ya estimado?
```

### Un cliente con varios proyectos

```chat
Tú: Este cliente tiene dos proyectos. Cotiza primero el de agentes de correo.
Agente: Listo. Lo guardo como un proyecto independiente, con su propio PDF y su propio Excel, en la carpeta del cliente.
```

### Ajustar días

```chat
Tú: Sube a 3 días el desarrollo backend de la funcionalidad de reportes.
Agente: Actualicé los días de esa funcionalidad, recalculé el Excel y volví a generar el PDF con los precios nuevos.
```

### Dejar una condición comercial

```chat
Tú: El cobro del módulo 3 aplica solo si el cliente aporta el servidor. Déjalo anotado.
Agente: Agregué la aclaración como un comentario en el Excel, sin modificar ningún valor ni fórmula.
```

### Ver el total

```chat
Tú: ¿Cuánto da el total del proyecto y qué parte son los costos transversales?
Agente: El total es el calculado por el Excel. Los transversales (estructura, diseño base, implementación y agente de IA) suman el valor que aparece en la banda correspondiente del PDF.
```

## Qué recibes

```cards
PDF de cotización de alcance | Módulos, submódulos y funcionalidades, cada una con su precio, los subtotales por módulo y el total general.
Excel de cotización | El esfuerzo en días por especialidad y el costo calculado con las fórmulas del equipo Campus.
Lista de pendientes | Lo que conviene que valides: distribución de días, posibles solapamientos entre módulos y datos que falten.
```

### Los costos que siempre aparecen

Además de los módulos del cliente, toda cotización incluye **cuatro costos transversales** que no vienen de una funcionalidad concreta, sino del proyecto como un todo:

| Costo transversal | Qué cubre |
|---|---|
| Estructura del proyecto | Arranque, liderazgo, arquitectura y organización del trabajo |
| UX y esquema del proyecto | Diseño de la experiencia y de la interfaz base de todo el sistema |
| Implementación y entrega del sistema | Despliegue, entrega y capacitación general |
| Estructura del agente de IA | La base del asistente de IA, si el proyecto lo incluye |

Se estiman según el tamaño del proyecto: a más alcance, más esfuerzo transversal.

## Cómo revisar la cotización

- **¿El PDF y el Excel cuentan lo mismo?** No debe faltar ni sobrar ningún módulo, submódulo ni funcionalidad.
- **¿Los precios coinciden?** Cada línea y cada total del PDF debe ser igual al del Excel.
- **¿Los días tienen sentido?** Revisa la distribución por especialidad con tu criterio: ¿la parte de backend o de diseño se ve razonable?
- **¿Cada funcionalidad es realmente una sola cosa?** Y a la vez, ¿no se juntaron dos capacidades distintas?
- **¿Entiendes cada pendiente?** Si algo te suena a duda, pregúntalo antes de enviar.
- **¿El total es el que esperabas?** Compáralo con lo que habías hablado con el cliente.

> [!nota] El mínimo de cada estimación es medio día
> Ninguna funcionalidad se estima en menos de 0,5 días, aunque el esfuerzo real parezca menor. Es una regla del equipo.

## Cómo pedir ajustes

| Quieres… | Puedes decir… |
|---|---|
| Cambiar el esfuerzo de algo | «Sube a 2 días el diseño de la funcionalidad de reportes» |
| Quitar o agregar una funcionalidad | «Agrega la exportación a Excel en el submódulo de reportes» |
| Separar una funcionalidad | «Divide “carga y validación de archivos” en dos funcionalidades» |
| Dejar una condición | «Anota que este cobro depende de la integración con Siigo» |
| Cambiar el diseño del PDF | «Este cliente prefiere fondo blanco con barras azules» |
| Cotizar otro proyecto del mismo cliente | «Ahora cotiza el proyecto de archivo de tránsito» |

## Comandos rápidos con «!»

Además de pedirle las cosas con tus palabras, puedes darle una **orden corta** escribiendo `!` antes de la palabra, por ejemplo `!optimize`. Cuando el agente reconoce un comando, **lo cumple siempre**, y lo primero que escribe en su respuesta es qué comandos recibió.

- Puedes escribirlo solo o con un texto: `!optimize el PDF de la cotización`.
- Puedes combinar varios: `!plan !no-assumptions`.
- Vale para la tarea en curso; en una tarea nueva se escribe de nuevo.
- `!help` muestra la lista de comandos de este agente.

> [!tip] Los dos más usados
> `!optimize` mejora lo que se esté haciendo sin cambiar su alcance ni sus datos. `!notime` acelera el trabajo: menos preguntas sueltas y menos explicaciones, pero nunca se salta una verificación obligatoria.

> [!nota] Lo que un comando no cambia
> Un comando no permite saltarse las reglas del agente (no inventar datos, la marca, la confidencialidad, las aprobaciones y verificaciones obligatorias). Si pides algo que una regla impide, el agente hace todo lo permitido y te dice en una frase qué no pudo y por qué.

Estos son los comandos de este agente:

```comandos
```

## Lo que el agente no hace

| Si le pides… | Qué pasa | Qué hacer |
|---|---|---|
| Que invente una funcionalidad para completar el alcance | No lo hace: solo incluye lo que tú diste | Compártele la fuente donde aparece |
| Que modifique las fórmulas del Excel | No lo hace: solo llena las celdas de datos | Si una fórmula debe cambiar, hazlo con el equipo que mantiene la plantilla |
| Que ponga un precio «de referencia» sin calcularlo | No lo hace: los precios salen del Excel | Pídele que llene y recalcule el Excel |
| Que junte varias funcionalidades en una para acortar el PDF | No lo hace: pierde fidelidad con el alcance | Si de verdad es una sola capacidad, díselo |
| Que reparta un mismo estimado entre varias funcionalidades | No lo hace: cada una lleva su propio estimado | Dale el esfuerzo de cada una |

## Preguntas frecuentes

**¿Por qué el PDF dice «Pendiente de costear»?**
Porque el Excel todavía no estaba calculado. Cuando lo esté, el PDF se actualiza con los precios reales.

**¿Por qué hay una diferencia de un peso entre un subtotal y la suma de sus líneas?**
Es redondeo. El PDF usa el total exacto del Excel y deja una nota; no se ajusta a mano.

**¿Puede el agente cotizar sin que yo valide el PDF primero?**
Está diseñado para que primero valides el alcance. Es mejor corregir contenido antes de calcular costos.

**¿El Excel incluye IVA?**
Depende de la fuente y del modelo del equipo. Si tienes dudas sobre qué incluye el total, pregúntaselo al agente para que lo confirme con el Excel.

**¿Puedo pedir que el PDF no lleve el nombre del cliente?**
Sí. En algunos casos se han entregado cotizaciones sin nombre de cliente a pedido del usuario.

**¿Dónde quedan los archivos?**
En la carpeta del cliente dentro de `cotizaciones`, con los nombres `Cotizacion de Alcance.pdf` y `Cotizacion.xlsx`. Si el cliente tiene varios proyectos, cada uno tiene su subcarpeta.

## Glosario

| Término | Qué significa |
|---|---|
| Alcance | Lo que incluye el proyecto y lo que no |
| Módulo | Una gran área del proyecto |
| Submódulo | Una agrupación de funcionalidades dentro de un módulo |
| Funcionalidad | Una capacidad concreta del sistema |
| Costos transversales | Los costos del proyecto como un todo, que no pertenecen a un módulo concreto |
| Especialidad | El tipo de trabajo: diseño, backend, frontend, QA, implementación, móvil, IA |
| AIU | Administración, imprevistos y utilidad: un porcentaje que se suma al costo (10 % en las cotizaciones) |
| COP | Pesos colombianos |

## Si algo no funciona

Si los totales no cuadran, si falta una funcionalidad o si el agente no responde como esperas, descríbele el problema con el módulo o la funcionalidad concreta. Si el comportamiento se repite, avisa a quien mantiene el agente; su guía técnica explica cómo se verifican el PDF y el Excel.
