---
titulo: presentations-designer: cómo crear la presentación de un cliente
resumen: Información de entrada, aprobación del plan, solicitud de ajustes y resultados: un PDF y un link web.
---

## Descripción general

El **Estudio de Presentaciones** (`presentations-designer`) genera presentaciones comerciales para clientes con el diseño oficial de Campuslands. El usuario aporta los alcances y la información del cliente; el agente propone primero un **plan lámina por lámina** y construye el borrador solo después de que el plan se aprueba. El resultado es un **PDF** y un **link web**.

El agente se encarga del formato, la marca y la verificación. Al usuario le corresponde aportar la información correcta y aprobar el plan y el borrador.

```stats
10 | láminas como máximo; cada una responde una pregunta del cliente
1 | plan lámina por lámina, que se aprueba antes de construir el borrador
2 | resultados: un PDF y un link web
```

> [!nota] Orden del proceso
> El proceso sigue siempre el mismo orden: aprobación del plan, construcción del borrador y ajustes. Los cambios de fondo se resuelven en el plan, antes de que la presentación esté armada.

## Cuándo se usa

El agente se usa para elaborar una **presentación comercial** para un cliente: una propuesta, una demostración de solución o una propuesta de plataforma. Está pensado para quien dirige la cuenta, que aporta los datos del cliente y las aprobaciones, mientras el agente realiza el trabajo de diseño.

### Reglas de diseño

El diseño es el mismo para todos los clientes:

- Fondo **blanco** y tipografía **Poppins**.
- Los logos de **Campuslands y del cliente** juntos en la portada y el cierre, con el mismo peso visual y separados por una «×».
- Los colores de la presentación son siempre los de Campuslands. **Del cliente se usa su logo y su contenido**, no sus colores.
- Un máximo de **10 láminas**.

## Ejemplos de presentaciones

Portadas de las presentaciones generadas con el diseño vigente del agente, desde Globant Dojo (29 de septiembre de 2026). Todas comparten el mismo diseño; solo cambian el cliente, el proyecto y el contenido. La pila se puede arrastrar, recorrer con las flechas o abrir en abanico al pasar el cursor.

```cardstack
```

### Logos de clientes

El logo de cada cliente se coloca en la portada y el cierre de su presentación. Se muestran con sus colores originales; el carrusel se recorre con las flechas, arrastrando o pasando el cursor.

```coverflow
```

## Entradas requeridas

Si falta información, el agente te enviará un cuestionario. Puedes adelantarte reuniendo estas seis cosas:

| Bloque | Qué incluir | Ejemplo |
|---|---|---|
| Datos generales | Nombre completo del cliente (con S.A.S. o S.A.), nombre del proyecto, cargo y área de quien recibe la propuesta, y quién lidera la cuenta | *Unidrogas S.A.S.* · *Plataforma de Inteligencia Financiera* · CFO |
| Línea base y dolores | Cifras actuales del problema, los problemas cualitativos y cómo se resume el «hoy» frente al «con la plataforma» | 4 horas manuales por reporte; información en silos |
| Arquitectura y alcance | Qué fuentes de datos se conectan, de 4 a 6 módulos clave y un ejemplo de cómo se usa | SAP, bases SQL; pregunta en lenguaje natural y respuesta de la IA |
| ROI y sector | Ahorro o retorno proyectado y casos de éxito del mismo sector | 25 % de ahorro; casos en el sector financiero |
| Condiciones comerciales | Costo total en COP, plazo en meses, esquema de pago, garantía y soporte | 40 % anticipo, 40 % hito intermedio, 20 % entrega |
| Logo del cliente | PNG o SVG con fondo transparente | `logo-cliente.png` |

> [!importante] La razón social va completa
> El título de la página web lleva la razón social completa del cliente, con su sufijo legal. Si no se la das, el agente te la pedirá; no la adivina.

### Sobre el precio

Si tu fuente es un Excel de cotización, el agente toma el total de inversión de la **celda Y122** del Excel (el precio con el margen comercial completo), no del PDF de alcance, que puede mostrar otra cifra. Si encuentra una diferencia entre ambos, **te consultará antes de construir**. El desglose por módulo es material interno: en la presentación el total aparece como una cifra única, salvo que pidas lo contrario.

## Paso a paso

```lanes
Tú | Comparte los alcances y los datos del cliente
Agente | Te envía el cuestionario si falta información
Tú | Responde y adjunta el logo del cliente
Agente | Presenta el plan lámina por lámina
Tú | Revisa y aprueba el plan
Agente | Construye el borrador completo y lo verifica
Tú | Revisa y pide los ajustes que necesites
Agente | Exporta el PDF, lo publica y te comparte el link
```

### 1. Comparte lo que tienes

Pega o adjunta los alcances, notas de reunión o cotización. Cuanto más completo sea, menos preguntas recibirás.

### 2. Aprueba el plan

Antes de diseñar, el agente te muestra una propuesta **lámina por lámina**: qué dirá cada una, qué tipo de diseño usará y por qué cada bloque está donde está. **No empieza a construir hasta que lo confirmes.** Este es el mejor momento para cambiar el orden, quitar o fusionar láminas.

### 3. Revisa el borrador

El agente entrega la presentación completa, revisada con una herramienta automática y a la vista. La revisión del contenido corresponde al usuario, que conoce al cliente.

### 4. Pide ajustes

Dile qué cambiar. Después de cada ajuste el agente vuelve a verificar la presentación completa, porque un cambio pequeño puede mover el resto.

### 5. Recibe el PDF y el link

Cuando das tu visto bueno, el agente exporta el PDF, registra la presentación en el portal de proyectos, la publica y te comparte el link. Si no pudo confirmar que la publicación ya está activa, **te lo dice**.

> [!importante] Después de publicar, espera unos 2 minutos
> La web tarda **aproximadamente 2 minutos** en mostrar la presentación nueva o los cambios. El agente lo recuerda cada vez que publica. Si el link da error justo después, espera y recarga; está explicado en [Cómo funciona la web de presentaciones](#como-funciona-la-web-de-presentaciones).

## Cómo es el plan por lámina

El plan es una lista corta. Este es un ejemplo ilustrativo de cómo se ve, con datos inventados:

| Lámina | Qué responde | Contenido | Por qué está así |
|---|---|---|---|
| 1 · Portada | ¿De quién y para quién? | Logos de ambas empresas, título y fecha | Es lo primero que ve el cliente |
| 2 · Contexto | ¿Qué le duele? | El problema en una frase y un dato clave | El dato va destacado para que se lea primero |
| 3 · Cifras | ¿Qué tan grande es? | Cuatro números de la línea base | Cuatro es el máximo que se lee de un vistazo |
| 4 · Solución | ¿Qué proponemos? | Los módulos principales | Una cuadrícula agrupa lo que va junto |
| 5 · Inversión | ¿Cuánto y cómo? | Total, esquema de pago y garantía | Una sola cifra, sin desglose por módulo |
| 6 · Cierre | ¿Qué sigue? | Próximos pasos y logos | Cierra con la acción que se le pide al cliente |

> [!nota] Fusionar antes que añadir
> Si el contenido no cabe en 10 láminas, el agente fusiona (por ejemplo, contexto con reto, o inversión con condiciones de pago). Solo pasa de 10 si tú lo pides con esas palabras.

## Ejemplos de conversación

### Empezar

```chat
Tú: Necesito una presentación para Unidrogas S.A.S. sobre una plataforma de inteligencia financiera. Adjunto los alcances y la cotización.
Agente: Perfecto. Antes de proponerte el plan necesito confirmar tres datos: el cargo de quien recibirá la propuesta, el plazo en meses y si mantenemos el esquema de pago 40/40/20. También necesito el logo del cliente en PNG o SVG transparente.
```

### Aprobar el plan

```chat
Tú: El plan está bien. Construye el borrador completo.
Agente: Listo. Construyo el borrador con las 7 láminas del plan y te aviso cuando haya pasado la verificación.
```

### Cambiar el orden o el contenido

```chat
Tú: Pasa la lámina de resultados antes de la de módulos y resume el cierre en una frase.
Agente: Hecho. Reordené las láminas, ajusté el cierre y volví a verificar la presentación completa.
```

### Pedir un rediseño

Si una lámina se ve «plana», no la retoca: la rediseña con otra estructura.

```chat
Tú: La lámina 4 se ve plana. Rediséñala.
Agente: La reestructuro con otro tipo de diseño, nueva jerarquía y íconos, y vuelvo a verificarla.
```

## Resultados

```cards
El PDF | Una página por lámina. Es el archivo portable: se ve igual en cualquier equipo y se envía por correo.
El link web | La versión interactiva, que muestra una lámina a la vez con flechas para avanzar. Se comparte con el cliente.
El plan por lámina | Qué va en cada una y por qué, para que quede registro de las decisiones.
La ficha en el portal | La presentación queda registrada en el catálogo de proyectos de Full Service.
```

> [!importante] PDF y link son obligatorios
> Siempre recibes **los dos**. Ninguno reemplaza al otro: el PDF es el archivo que no cambia; el link es la versión interactiva.

## Cómo revisar el borrador

Tómate unos minutos para recorrer cada lámina con estas preguntas:

- **¿El nombre del cliente está bien escrito?** Razón social completa, con el sufijo legal.
- **¿Cada cifra tiene respaldo?** Si ves un número que no reconoces, pregunta de dónde sale.
- **¿La historia se entiende?** Del problema a la solución y al siguiente paso.
- **¿Los dos logos se ven del mismo tamaño?** Si uno domina, pídelo y se ajusta.
- **¿El total de inversión es el correcto?** Compáralo con tu cotización.
- **¿Hay demasiado texto en alguna lámina?** Pide que la divida o la simplifique.
- **¿Algo suena a promesa que no podemos cumplir?** Pídele que lo reformule.

## Cómo pedir ajustes

Cuanto más concreto seas, mejor. Algunos ejemplos de lo que puedes escribir:

| Quieres… | Puedes decir… |
|---|---|
| Cambiar un texto | «En la lámina 3, cambia “reducción de costos” por “ahorro operativo”» |
| Reordenar | «Pasa la lámina de inversión al final, antes del cierre» |
| Quitar o fusionar | «Une contexto y reto en una sola lámina» |
| Cambiar un número | «El plazo es 5 meses, no 4. Actualiza todas las láminas donde aparezca» |
| Ajustar los logos | «El logo del cliente se ve más grande que el nuestro» |
| Pedir otro diseño | «La lámina 6 se ve plana; hazla con otra estructura» |
| Pasar de 10 láminas | «Necesito 12 láminas en total» (dilo textualmente) |

## Cómo funciona la web de presentaciones

Las presentaciones **no viven en el mismo repositorio que el agente**: están en uno aparte, llamado `Presentaciones`. Cuando el agente termina una, la sube ahí y la web se actualiza sola. Por eso hay tres cosas que debes saber.

### 1. Se instala en dos pasos, y el segundo va en una carpeta exacta

Además de clonar el repositorio de los agentes, hay que clonar `Presentaciones` **dentro** de la carpeta del agente, con el nombre `presentaciones`. Si queda en otro lugar, el agente no encuentra su plantilla ni puede publicar. El paso a paso, con un mensaje listo para dárselo a tu IA, está en [Inicio](../inicio/instalacion#repositorio-aparte-las-presentaciones).

```repos
fullservice-agents | Repositorio 1 | Las instrucciones, la wiki y las herramientas del agente, junto con los demás agentes.
Presentaciones | Repositorio 2 · aparte | Las presentaciones ya hechas y el portal web. Es lo que publica Vercel. | decks/, web/
agents/claude-agents/presentations-designer | presentaciones/
git clone https://github.com/GustavoAdolfoNavarroPacheco/Presentaciones presentaciones
```

### 2. Pide permiso a Gustavo antes de empezar

`Presentaciones` es un repositorio **privado**. Sin permiso no se puede ni clonar ni publicar. Escríbele a **Gustavo Navarro** con tu usuario de GitHub y acepta la invitación que te llegará; el inicio de sesión lo haces tú en el navegador. **Nunca le des tu contraseña ni tus claves a la IA.** Si el agente recibe un error de permisos, se detiene y te lo explica: no intenta rodeos.

### 3. La publicación tarda unos 2 minutos

Cuando el agente sube la presentación, un servicio llamado **Vercel** la construye y la pone en línea. Ese proceso tarda **aproximadamente 2 minutos**.

```publicar
El agente sube la presentación | Los archivos llegan a GitHub.
Vercel lo detecta | Empieza a construir la web.
Construye la web | Compila el portal y copia las presentaciones.
En línea | El link ya muestra la versión nueva.
≈ 2 min
```

Mientras tanto, el link puede dar **404** o mostrar la versión anterior. No significa que algo falló: espera dos minutos y recarga con `Ctrl + F5`. Si pasan más de cinco, avísale al agente o a Gustavo.

### Qué se ve en cada dirección

Todo se publica en `https://fullservicepresentations.vercel.app`, con dos zonas de acceso distinto:

| Dirección | Quién entra | Qué muestra |
|---|---|---|
| `/` | Solo usuarios con cuenta (correo y contraseña) | El **catálogo** de proyectos: buscador, filtros y vista en cuadrícula o lista |
| `/<nombre>` | **Cualquiera con el link** | Una presentación (por ejemplo `/fcv`), lista para enviar al cliente |
| `/<nombre>/<nombre>.pdf` | Cualquiera con el link | El PDF de esa presentación |

- **Compartir con el cliente es seguro:** el cliente abre solo el link de **su** presentación; no ve el catálogo ni los proyectos de otros clientes.
- **Una presentación publicada puede no estar en el catálogo.** Para aparecer allí, el agente la registra; sin ese registro funciona por su link, pero no sale en el buscador.
- **El nombre es la dirección.** Si cambia, cambia el link que ya enviaste.

## El portal de proyectos

Las presentaciones se registran en un portal web de Full Service, donde puedes encontrar los proyectos de todos los clientes. Para entrar, necesitas una cuenta; si todavía no tienes, un administrador debe darte acceso.

### Qué puedes hacer en el portal

- **Buscar y filtrar** proyectos por categoría, cliente o fecha, y verlos en cuadrícula o en lista.
- **Abrir la ficha** de un proyecto, con botones para abrir la presentación, ver el PDF, copiar el enlace y abrir la cotización (si tiene una).
- **Cotizar** desde la ficha, con el cotizador integrado.

### Permisos

| Rol | Puede |
|---|---|
| Propietario | Todo |
| Administrador | Gestionar proyectos y usuarios |
| Usuario | Crear y editar proyectos, y cotizar |
| Visitante | Solo ver: catálogo, fichas, enlaces, PDF y cotizaciones |

> [!nota] Lo que registra el agente queda bloqueado
> En los proyectos que crea el agente, la **fecha**, el **link de la presentación** y el **PDF** aparecen con un candado y no se pueden editar desde el portal. Si algo de eso necesita corregirse, pídeselo al agente.

## Comandos rápidos con «!»

Además de pedirle las cosas con tus palabras, puedes darle una **orden corta** escribiendo `!` antes de la palabra, por ejemplo `!optimize`. Cuando el agente reconoce un comando, **lo cumple siempre**, y lo primero que escribe en su respuesta es qué comandos recibió.

- Puedes escribirlo solo o con un texto: `!optimize la presentación en curso`.
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

## Preguntas frecuentes

**¿Puedo usar los colores de mi cliente?**
No. Los colores son siempre los de Campuslands. Del cliente se usa su logo y su contenido.

**¿Y si necesito más de 10 láminas?**
Pídelo con esas palabras. Antes de aceptar, el agente intentará fusionar contenido.

**¿Por qué me pide el logo transparente?**
Porque sobre fondo blanco un logo con su propio fondo se vería como un cuadro pegado. Si el logo es claro o blanco, te pedirá la versión a color u oscura.

**¿Por qué no se muestra el precio de cada módulo?**
Porque el desglose es material interno. El total aparece como una sola cifra. Si necesitas mostrar el desglose, pídelo expresamente.

**¿Cuánto tarda?**
Depende de la información. Con los datos completos, el plan llega rápido; el borrador se entrega ya verificado.

**El link no abre.**
Si acabas de publicar, espera unos 2 minutos y recarga con `Ctrl + F5`: la web tarda en construirse. Si pasan más de cinco, avísale al agente: él confirma si la publicación ya está activa. Mientras tanto puedes enviar el PDF.

**El agente me dice que no tiene permiso para publicar.**
Falta el acceso al repositorio `Presentaciones`. Pídeselo a Gustavo Navarro con tu usuario de GitHub; el agente se detiene hasta que lo tengas.

**¿Puedo editar el PDF?**
El PDF no se edita. Si necesitas un cambio, pídeselo al agente y se genera de nuevo.

## Glosario

| Término | Qué significa |
|---|---|
| Deck | Una presentación completa |
| Lámina | Cada página de la presentación |
| Co-branding | Mostrar juntos los logos de Campuslands y del cliente |
| ROI | Retorno de inversión: cuánto se gana o se ahorra frente a lo que se invierte |
| Slug | El nombre corto que forma la dirección web de la presentación |
| Razón social | El nombre legal completo de la empresa |
| Portal | La página web donde se registran todos los proyectos |

## Solución de problemas

Si el agente no responde como esperas, repite tu pedido con más contexto. Si algo del diseño te parece incorrecto, descríbelo con una frase concreta («en la lámina 5 el texto se sale de la tarjeta»). Si el problema persiste, avisa a quien mantiene el agente; su guía técnica incluye una tabla de problemas frecuentes.
