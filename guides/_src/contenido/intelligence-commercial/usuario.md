---
titulo: intelligence-commercial: cómo conectar con los contactos clave
resumen: Requisitos para operar en LinkedIn, funcionamiento, mensajes que se envían y revisión del informe de cada lote.
---

## Descripción general

**Explorador de Campus** (`intelligence-commercial`) toma una lista de empresas, identifica a las personas indicadas dentro de cada una y envía una invitación de LinkedIn con una nota personalizada, en el idioma en que cada persona escribe. Al finalizar entrega un informe con todo lo enviado.

Es la segunda etapa de la prospección: Radar de Campus identifica las empresas y Explorador contacta a las personas.

```stats
5 | tipos de cargo que contacta dentro de cada empresa
2 | idiomas de escritura: inglés y español
0 | aprobaciones solicitadas por mensaje: las invitaciones se envían sin aprobación previa
```

> [!importante] Envío sin aprobación previa
> Explorador **envía las invitaciones sin solicitar aprobación mensaje por mensaje**; es una decisión del equipo para reducir el trabajo manual. Antes de lanzar un lote se debe revisar la plantilla del mensaje (más abajo).

## Cuándo se usa

El agente se usa cuando ya existe una lista de empresas objetivo y se quiere **iniciar conversaciones** con las personas que toman decisiones sobre equipos técnicos. El mensaje ofrece apoyo para escalar equipos de desarrollo, en especial para llevar iniciativas de inteligencia artificial de piloto a producción.

El agente está configurado para la línea de **staffing de desarrolladores** de Full Service y, según sus filtros, prospecta principalmente **startups y scaleups de software en Estados Unidos** de entre 51 y 500 empleados. Para otro tipo de empresa o de país, los filtros se modifican en la configuración del agente, a cargo de quien lo mantiene.

### A quién contacta dentro de cada empresa

```cards
Reclutadores técnicos | Quienes gestionan la contratación de perfiles de desarrollo.
Vicepresidentes de Ingeniería | Responsables del plan técnico y del presupuesto de equipos.
CTO | Directores de tecnología que deciden iniciativas de IA y software.
Líderes de IA | Quienes llevan los proyectos de IA de piloto a producción.
Gerentes de contratación técnica | Enlace entre Recursos Humanos y las áreas técnicas.
```

Si una persona tiene otro cargo, **no se contacta**, aunque aparezca en los resultados. Tampoco se contacta a gobierno, organizaciones sin ánimo de lucro, universidades ni agencias de reclutamiento, por tratarse de clientes poco probables o de competencia.

## Requisitos previos

Prepara tres cosas y revisa una:

- **La lista de empresas.** Normalmente es la que entrega Radar de Campus; también sirve una propia, con los nombres claros.
- **Tu sesión de LinkedIn abierta.** Inicia sesión tú mismo. El agente **nunca escribe contraseñas** ni resuelve verificaciones de seguridad.
- **Cuántas conexiones quieres lograr** en la sesión: una meta numérica.
- **La plantilla del mensaje.** Léela y confirma que estás de acuerdo (más abajo).

## Paso a paso

```lanes
Tú | Entrégale la lista de empresas y la meta de conexiones
Agente | Completa los datos de cada empresa y elige a los contactos adecuados
Agente | Revisa cada perfil, detecta el idioma y escribe el mensaje
Agente | Envía las invitaciones en lotes pequeños, con pausas
Tú | Revisa el informe final
```

### 1. Dale la lista

Pégala en la conversación o adjunta el archivo de Radar de Campus. Dile cuántas conexiones quieres lograr.

### 2. El agente investiga

Completa para cada empresa su sitio web, su tamaño, su sector y su sede. Lo que no encuentra queda en blanco; no lo inventa. Después agrupa las empresas y elige, dentro de cada una, a las personas que encajan con los cinco tipos de contacto.

### 3. Escribe y envía

Para cada persona abre su perfil, mira en qué idioma escribe y redacta el mensaje. Luego pulsa «Conectar» y lo envía. Lo hace **en lotes pequeños y con pausas**, y por eso puede parecer lento: es a propósito, para cuidar tu cuenta.

### 4. Recibes el informe

Al cerrar cada lote te entrega el informe con la fecha, la empresa, la persona, su cargo y el mensaje enviado.

## Ejemplos de conversación

### Un lote completo

```chat
Tú: Aquí está el listado de empresas de Radar de Campus. Enriquécelo, busca los contactos y conéctate con ellos. Quiero lograr 20 conexiones.
Agente: Perfecto. Voy a enriquecer las empresas, clasificar los contactos por perfil y enviar las solicitudes en lotes pequeños. Al final te entrego el informe de divulgación.
```

### Solo preparar, sin enviar

Puedes pedirle que se detenga antes de enviar para revisar tú los contactos elegidos.

```chat
Tú: Enriquece estas 10 empresas y muéstrame los contactos que elegiste. Todavía no envíes nada.
Agente: Listo. Te muestro las empresas enriquecidas y los contactos clasificados por perfil. Avísame cuando quieras que continúe con los mensajes.
```

### Pedir el informe

```chat
Tú: Dame el informe de divulgación con todo lo que has enviado hasta ahora.
Agente: Aquí tienes el informe con fecha, empresa, contacto, cargo y el mensaje enviado en cada caso.
```

### Ajustar el tono

```chat
Tú: El mensaje suena muy comercial. Hazlo más directo y entre pares.
Agente: Entendido. Mantendré un tono breve y consultivo, sin lenguaje de venta.
```

## Cómo es el mensaje

El mensaje parte de una plantilla breve, que el agente adapta a cada persona. Tiene una versión en español y otra en inglés, y usa la que corresponde al idioma real del perfil.

> [!nota] Plantilla en español
> Hola [Nombre], vi tu enfoque en llevar IA de piloto a producción. En Campuslands ayudamos a equipos a escalar con desarrolladores y talento técnico para iniciativas de IA. ¿Valdría la pena una breve charla, o hay alguien más en [Empresa] manejando la contratación técnica?

> [!nota] Plantilla en inglés
> Hi [Nombre], noticed your focus on moving AI from pilot to production. Campuslands helps teams scale with devs and technical talent for AI initiatives. Worth a brief chat, or is someone else at [Empresa] handling technical hiring?

### Cómo decide el idioma

Mira primero **en qué idioma escribe la persona** (su perfil y sus publicaciones recientes). La ubicación y la empresa solo ayudan, porque hay personas que escriben en inglés en Latinoamérica y en español en Estados Unidos. Si no está claro, **usa inglés**. Nunca mezcla los dos idiomas en un mismo mensaje.

### Cómo se adapta

Cambia el nombre y la empresa y, **solo si hay algo real que decir**, ajusta la primera frase (por ejemplo, una publicación reciente de la persona). Mantiene un tono breve, directo y entre pares. No exagera, no promete plazos ni precios y no inventa nada sobre la persona o su empresa.

## Resultados

Cada lote deja cuatro archivos CSV, que se abren en Excel, dentro de la carpeta del lote:

| Archivo | Qué contiene |
|---|---|
| `01-empresas-enriquecidas.csv` | Cada empresa con su sitio web, empleados, ingresos estimados, utilidades, sector, país y la fuente |
| `02-contactos-clasificados.csv` | Las personas elegidas, con su cargo y el enlace a su perfil |
| `03-mensajes-conexion.csv` | El mensaje de cada persona y el idioma detectado |
| `04-informe-divulgacion.csv` | **El informe final**: fecha, empresa, persona, cargo y mensaje enviado |

El informe es el archivo que te interesa para revisar. La fecha es **la del día en que se envió**, no la del día en que lo pediste.

## Cómo revisar lo que hizo

- **¿Las personas son del tipo correcto?** Cargos como CTO, VP de Ingeniería, líderes de IA, reclutamiento técnico o contratación tecnológica.
- **¿Las empresas encajan?** Que no haya gobierno, universidades ni agencias de reclutamiento.
- **¿El idioma del mensaje es el de la persona?** Compara con su perfil.
- **¿El mensaje dice algo que no es cierto?** No debería: solo usa lo que aparece en el perfil.
- **¿Hubo menos conexiones que la meta?** El resumen final te explica por qué.

> [!nota] Revisión por lote
> El informe se revisa al terminar cada lote y no al final del mes: si hay algo por corregir, la plantilla se ajusta antes del siguiente lote.

## Por qué va despacio

Para protegerte. LinkedIn puede limitar o suspender cuentas que actúan como un robot, así que el agente trabaja de otra manera:

- Envía **pocas solicitudes por lote**, no cientos de golpe.
- Hace **pausas** entre cada acción.
- Si LinkedIn muestra un límite, un aviso o una verificación de identidad, **se detiene de inmediato y avisa al usuario**. No intenta sortearlo.

> [!importante] Verificación de identidad en LinkedIn
> La verificación la completa el propio usuario desde su cuenta; el agente no puede ni debe hacerlo. Al terminar, se le pide que continúe. No conviene reintentar de inmediato, porque hacerlo con rapidez aumenta el riesgo.

## Comandos rápidos con «!»

Además de pedirle las cosas con tus palabras, puedes darle una **orden corta** escribiendo `!` antes de la palabra, por ejemplo `!optimize`. Cuando el agente reconoce un comando, **lo cumple siempre**, y lo primero que escribe en su respuesta es qué comandos recibió.

- Puedes escribirlo solo o con un texto: `!optimize los mensajes de conexión`.
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

## Límites del agente

| Si le pides… | Qué pasa | Qué hacer |
|---|---|---|
| Buscar empresas nuevas | No las busca: trabaja con la lista que le das | Usa Radar de Campus |
| Enviar cientos de solicitudes de golpe | Se niega: trabaja por lotes con pausas | Es una protección de tu cuenta |
| Entrar a tu cuenta o escribir tu contraseña | No lo hace nunca | Inicia sesión tú |
| Resolver una verificación o CAPTCHA | No lo hace nunca | Resuélvela tú |
| Inventar datos de una empresa o persona | No los inventa | Si falta un dato, queda en blanco |
| Contactar a personas fuera de los cinco perfiles | Las omite | Avisa si quieres cambiar los perfiles |

## Preguntas frecuentes

**¿Por qué no me pide aprobar cada mensaje?**
Es una decisión del equipo para acelerar la prospección. La forma de mantener el control es revisar la plantilla antes y el informe después.

**¿Puedo pedir que se detenga?**
Sí. Dile que pare o que solo prepare los contactos sin enviar. Puedes retomarlo cuando quieras.

**¿Escribe siempre en inglés?**
No. Escribe en el idioma en que la persona escribe. Solo usa inglés por defecto cuando no hay forma de saber cuál es.

**¿Qué pasa si la persona no acepta la invitación?**
El informe registra lo enviado. La respuesta de la persona sucede dentro de LinkedIn y depende de ella.

**¿Puede contactar a alguien que ya contactó otro lote?**
Cada lote se registra con su fecha. Si te preocupa repetir un contacto, compara los informes de los lotes anteriores antes de lanzar uno nuevo.

**¿Dónde queda todo lo que hizo?**
En la carpeta `prospeccion`, dentro de la subcarpeta del lote.

## Glosario

| Término | Qué significa |
|---|---|
| *Outbound* | Prospección en la que tú tomas la iniciativa de contactar |
| Enriquecer | Completar los datos de una empresa a partir de fuentes públicas |
| Perfil de comprador | Tipo de persona que decide la compra, como un CTO |
| Staffing | Servicio de aportar desarrolladores a los equipos de otra empresa |
| Lote | Grupo pequeño de envíos que se procesan juntos, con pausas |
| CSV | Archivo de tabla que se abre en Excel |

## Solución de problemas

Si el agente se detiene, no responde como esperas o LinkedIn muestra un aviso, avísale a quien mantiene el agente. La guía técnica de Explorador de Campus explica qué revisar en cada caso.
