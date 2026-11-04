---
titulo: intelligence-commercial: guía técnica
resumen: Cómo funciona por dentro el agente de inteligencia comercial: fases, habilidades, filtros de LinkedIn, formatos, salvaguardas y mantenimiento.
---

## En resumen

**Explorador de Campus** (`intelligence-commercial`) es el agente de inteligencia comercial B2B y prospección saliente (*outbound*) de Campuslands. Parte de una lista de empresas objetivo, la enriquece, identifica a los contactos clave de cada empresa, detecta en qué idioma escribe cada persona y le envía, **de forma autónoma**, una solicitud de conexión de LinkedIn con una nota personalizada.

Esta guía describe cómo está construido: los archivos que lo gobiernan, las cuatro fases del ciclo de trabajo, las cuatro habilidades que se encadenan, los filtros de LinkedIn, los formatos de salida, las salvaguardas para no poner en riesgo la cuenta del usuario y cómo modificarlo con seguridad. Está pensada para quien lo mantiene.

```stats
2.º | eslabón del pipeline de prospección; recibe el listado de Radar de Campus
4 | fases por lote: enriquecer, clasificar, conectar e informar
4 | habilidades encadenadas y 4 CSV numerados por lote
5 | perfiles de comprador válidos para clasificar contactos
```

> [!importante] Lo esencial
> El envío es **autónomo** (sin aprobación por contacto ni por lote), pero **nunca masivo**: siempre en lotes pequeños con pausas. El agente jamás escribe credenciales ni resuelve CAPTCHA, y si LinkedIn muestra un límite o una verificación, **se detiene y avisa**.

## Qué prospecta y a quién

Conviene tener clara la audiencia, porque es distinta de la de los otros agentes del repositorio. Explorador de Campus prospecta específicamente la línea de **staffing de desarrolladores** de Full Service (Células de trabajo y horas, es decir, *staff augmentation*), no los proyectos de software a la medida que ofrecen los agentes de presentaciones, cotizaciones o licitaciones.

| Aspecto | Lo que dice la wiki |
|---|---|
| Producto que se ofrece | Desarrolladores de software y perfiles con capacidades de IA (staffing) |
| Empresas objetivo | Startups y scaleups SaaS y de software en EE. UU. (California, Texas, New York, Florida y Washington), de 51 a 500 empleados y de capital privado |
| Contactos prioritarios | Roles de Talento y RR. HH.: Head of Talent, Talent Acquisition Manager, Lead o Director, VP Talent, Head of People, People Operations Manager, HR Manager, Recruiting Manager, Technical Recruiter |
| Contactos secundarios | CTO, VP de Ingeniería, líderes de IA y gerentes de contratación técnica |
| Gancho del mensaje | Escalar equipos de desarrollo con talento técnico, en especial para llevar iniciativas de IA de piloto a producción |
| Diferenciador real | El talento sale del programa de formación propio de Campuslands (10 meses, cerca de 1.600 horas de programación, más inglés y liderazgo), no de un banco genérico de hojas de vida |

> [!cuidado] No mezclar audiencias
> Usar en un mismo mensaje o material el discurso de proyectos a la medida (dirigido a Directores Generales, CFOs o CTOs en Latinoamérica) y el de staffing (dirigido a Talento y RR. HH. en EE. UU.) sería un error de segmentación. Un hallazgo de lint del 2026-07-30 corrigió justamente un archivo que había heredado, por copiar y pegar, el contenido de otro agente.

## Cómo corre: Perplexity y `Perplexity.md`

Como Radar de Campus, este agente corre en **Perplexity**, con control de navegador. Su archivo de configuración es `Perplexity.md`, equivalente a un `CLAUDE.md`: el agente lo lee al iniciar cada sesión y se co-evoluciona con el usuario. Contiene su identidad, su misión, la tabla de decisiones fundacionales, la estructura de los CSV y el flujo de trabajo en cuatro fases.

La carpeta `.perplexity/` guarda la configuración local del entorno (permisos del equipo donde se ejecuta) y no forma parte del conocimiento del agente.

### El control del navegador

El agente usa mouse y teclado para tres cosas, y solo para esas: **navegar**, **verificar perfiles** y **pulsar «Conectar»** con la nota ya redactada. Todo lo demás está fuera de su alcance:

- Nunca inicia sesión: el usuario debe tener la sesión de LinkedIn abierta.
- Nunca ingresa credenciales, resuelve CAPTCHA ni intenta sortear detección de bots.
- Nunca cambia la configuración de la cuenta.
- Nunca hace *scraping* masivo de perfiles fuera de la búsqueda activa.

## Estructura del repositorio

```tree
intelligence-commercial/
  Perplexity.md                         # identidad, decisiones, fases y CSV
  .perplexity/                          # configuración local del entorno
  habilidades/                          # una carpeta por skill, cada una con su SKILL.md
    control-navegador-linkedin/
    deteccion-idioma/
    generacion-mensajes-personalizados/
    generacion-tabla-registro/
  prospeccion/
    <slug-lote>/                        # un lote por carpeta
      01-empresas-enriquecidas.csv
      02-contactos-clasificados.csv
      03-mensajes-conexion.csv
      04-informe-divulgacion.csv
  wiki/
    index.md                            # catálogo
    log.md                              # bitácora (solo se añade)
    perfil-usuario.md                   # identidad, usuario y audiencia
    perfiles-objetivo.md                # los 5 perfiles de comprador
    filtros-busqueda.md                 # filtros de cuenta y de lead, búsquedas A y B
    marca-campuslands.md                # tono de voz de los mensajes
```

> [!nota] Dónde vive el agente y sus recursos compartidos
> El agente está en `agents/perplexity-agents/intelligence-commercial/`. Los logos, el isotipo, el favicon, el `Brief Fullservice.pdf` y el Brandbook de Campuslands ya no se copian dentro de cada agente: están en `resources/campuslands-resources/`, en la raíz del repositorio (desde la carpeta del agente: `../../../resources/campuslands-resources/`).

## El ciclo de trabajo

El trabajo de cada lote avanza por cuatro fases, y **cada una deja un CSV numerado** que la siguiente consume.

```flow
Enriquecer | Completa sitio web, tamaño, sector y sede de cada empresa. Deja el CSV 01.
Clasificar | Agrupa por sector y país y filtra contactos por perfil. Deja el CSV 02.
Conectar | Verifica el perfil, detecta idioma, redacta y envía la solicitud. Deja el CSV 03.
Informar | Genera el informe final con la fecha real de envío. Deja el CSV 04.
```

### Fase 1 · Enriquecimiento de datos

Para cada empresa de la lista, el agente busca en la web su **sitio web oficial** (dominio principal), su **tamaño** (empleados e ingresos estimados y, si cotiza en bolsa o el dato es público, utilidades) y sus **datos firmográficos** (sector exacto y país de la sede). Si un dato no aparece con confianza razonable, **se deja en blanco y se anota la fuente y la fecha de consulta**. El resultado va a `01-empresas-enriquecidas.csv`.

### Fase 2 · Clasificación y validación

Las empresas se agrupan por sector y país. Dentro de cada una, el agente identifica y filtra los contactos que calzan con los cinco perfiles de comprador (ver más abajo). Se prioriza el cargo exacto sobre el título genérico de LinkedIn, y un mismo contacto nunca se duplica entre perfiles. El resultado va a `02-contactos-clasificados.csv`.

### Fase 3 · Solicitudes de conexión personalizadas

Es la fase delicada y la que usa tres de las cuatro habilidades. Para cada contacto seleccionado:

1. Se abre y verifica su perfil (cargo, empresa, publicaciones recientes).
2. Se **detecta el idioma real** en que escribe.
3. Se redacta el mensaje adaptando la plantilla base.
4. Se pega la nota y se pulsa «Conectar», de forma autónoma.
5. Se registra el envío.

El mensaje y el idioma quedan en `03-mensajes-conexion.csv`.

### Fase 4 · Informe final

Al terminar el flujo, o al cerrar cada lote de envíos, el agente genera o actualiza `04-informe-divulgacion.csv`. La columna Fecha usa **la fecha real de ejecución o de envío**, nunca la fecha en que el usuario pidió el trabajo.

## Las cuatro habilidades

Cada habilidad es un `SKILL.md` con la misma estructura: cuándo usarla, entradas, procedimiento, reglas obligatorias y salida.

| Habilidad | Cuándo entra | Qué recibe | Qué entrega |
|---|---|---|---|
| `control-navegador-linkedin` | Para buscar, verificar perfiles y conectar | Filtro de búsqueda elegido, meta de conexiones de la sesión y mensaje ya redactado | Lista de perfiles contactados con estado: enviado, pendiente o rechazado por filtro |
| `deteccion-idioma` | Justo antes de redactar cada mensaje | Perfil, publicaciones recientes, ubicación y empresa | Etiqueta `EN` o `ES` |
| `generacion-mensajes-personalizados` | Después de detectar el idioma | Etiqueta, nombre, cargo, empresa y contexto adicional | Texto final del mensaje listo para pegar |
| `generacion-tabla-registro` | Tras cada envío confirmado y al cierre | Fecha, empresa, contacto y cargo de cada conexión | Tabla `Fecha, Empresa, Contacto, Cargo` más un resumen de cierre |

### El orden dentro de la fase 3

```flow
Verificar perfil | `control-navegador-linkedin` abre el perfil y revisa cargo, empresa y publicaciones.
Detectar idioma | `deteccion-idioma` devuelve EN o ES. Es un paso obligatorio.
Redactar | `generacion-mensajes-personalizados` adapta la plantilla al contacto.
Enviar | De vuelta en `control-navegador-linkedin`: pega la nota y pulsa Conectar.
Registrar | `generacion-tabla-registro` anota cada envío confirmado.
```

### Detección de idioma, paso a paso

La regla de fondo es que **el idioma en el que la persona escribe activamente pesa más que la interfaz o la ubicación**. El procedimiento es:

1. Leer el idioma del propio perfil: titular, sección «Acerca de» y experiencia.
2. Si hay publicaciones o comentarios recientes, **priorizarlos** como señal principal.
3. Usar la ubicación geográfica y el nombre de la empresa solo como señales de apoyo, nunca como criterio único (hay hispanohablantes en EE. UU. y angloparlantes en Latinoamérica).
4. Si la evidencia es mixta o insuficiente, **usar inglés por defecto** (idioma base de la plantilla) y dejar constancia de la ambigüedad si el usuario pide detalle.
5. Devolver una etiqueta clara: `EN` o `ES`.

> [!nota] Nunca dos idiomas en un mensaje
> No se mezclan idiomas dentro de un mismo mensaje ni se usa una plantilla distinta de la que indica la etiqueta. Ante ambigüedad real, es preferible el inglés a arriesgar un mensaje mal dirigido.

### Generación del mensaje

Las plantillas base viven **solo** en `habilidades/generacion-mensajes-personalizados/SKILL.md`, que es su fuente única (no se duplican en la wiki para que un ajuste no quede desincronizado entre dos archivos).

| Idioma | Plantilla base |
|---|---|
| EN | *Hi [Nombre], noticed your focus on moving AI from pilot to production. Campuslands helps teams scale with devs and technical talent for AI initiatives. Worth a brief chat, or is someone else at [Empresa] handling technical hiring?* |
| ES | *Hola [Nombre], vi tu enfoque en llevar IA de piloto a producción. En Campuslands ayudamos a equipos a escalar con desarrolladores y talento técnico para iniciativas de IA. ¿Valdría la pena una breve charla, o hay alguien más en [Empresa] manejando la contratación técnica?* |

El procedimiento sustituye `[Nombre]` y `[Empresa]` y, **solo si hay algo genuino que decir**, ajusta la frase inicial con contexto verificado (una publicación reciente, una señal de contratación activa, un cambio de trabajo). El tono es **breve, directo, entre pares y consultivo**: nada de lenguaje de venta agresivo, signos de exclamación excesivos ni superlativos. Debe caber en el límite de caracteres de una nota de conexión y **nunca inventar contexto** sobre la persona o la empresa.

## Filtros de LinkedIn

`wiki/filtros-busqueda.md` define lo que `control-navegador-linkedin` aplica en LinkedIn o Sales Navigator.

### Filtros de cuenta

| Filtro | Valor |
|---|---|
| Geografía | Estados Unidos (CA, TX, NY, FL, WA) |
| Industria | Software Development, IT Services and IT Consulting, Technology, Information and Internet |
| Tamaño (*headcount*) | 51–200 y 201–500; no bajar de 50 por falta de presupuesto o estructura recurrente |
| Segmentación interna | Pequeña 50–100 · Mediana 101–250 · Grande 251–500 |
| Tipo | Privately Held |
| Señales de crecimiento | Crecimiento de plantilla, *Hiring on LinkedIn*, financiación reciente |
| Palabras clave | SaaS, software, platform, cloud, AI, data, automation |
| Exclusiones estrictas | Gobierno, organizaciones sin ánimo de lucro, escuelas, universidades, agencias de staffing y de reclutamiento |

### Filtros de contacto

Función Recursos Humanos; antigüedad Manager, Director, VP, CXO o Head; preferiblemente más de 1 año en la empresa y más de 6 meses en el cargo; con actividad en LinkedIn en los últimos 30 días; y grado de conexión de **2.º primero, luego 3.º**.

### Las dos búsquedas predefinidas

| Búsqueda | Prioridad | Cargos | Cuándo usarla |
|---|---|---|---|
| **A** | Alta: talento en SaaS con contratación activa | Head of Talent, Director of Talent Acquisition, Talent Acquisition Manager, Recruiting Manager; señal *Hiring on LinkedIn* | Es el mejor encaje para staffing |
| **B** | Alta o media: *people leaders* en scaleups | Head of People, People Operations Manager, VP People, Chief People Officer | Cuando la empresa tiene estructura de People pero no Talent Acquisition formal |

## Los cinco perfiles de comprador

En la fase 2, `wiki/perfiles-objetivo.md` define a quién se clasifica dentro de cada empresa:

| Perfil | Por qué importa a Campuslands |
|---|---|
| Reclutadores técnicos | Gestionan directamente la contratación de perfiles de desarrollo; primer contacto natural |
| Vicepresidente de Ingeniería | Dueño del plan técnico y del presupuesto de equipos |
| CTO (Director de Tecnología) | Decisor final en iniciativas tecnológicas y de IA |
| Líderes de IA | Llevan proyectos de IA de piloto a producción; son el gancho de la plantilla |
| Gerentes de contratación tecnológica | Puente entre RR. HH. y las áreas técnicas; deciden volumen y perfil de las vacantes |

Un contacto fuera de estos cinco perfiles **no se procesa** en la fase 3, aunque aparezca en la búsqueda inicial. Un mismo contacto se asigna al perfil más específico que aplique.

## Formatos de salida

| Archivo | Fase | Columnas |
|---|---|---|
| `01-empresas-enriquecidas.csv` | 1 | Empresa, Sitio Web, Empleados, Ingresos Estimados, Utilidades, Sector, País Sede, Fuente/Fecha |
| `02-contactos-clasificados.csv` | 2 | Empresa, Sector, País, Nombre, Cargo, URL Perfil |
| `03-mensajes-conexion.csv` | 3 | Empresa, Nombre, Cargo, Idioma Detectado, Mensaje |
| `04-informe-divulgacion.csv` | 4 | Fecha (AAAA-MM-DD), Empresa, Contacto (Nombre), Cargo (Título), Mensaje Personalizado Redactado |

La tabla de registro que entrega `generacion-tabla-registro` al usuario tiene cuatro columnas, `Fecha | Empresa | Contacto | Cargo`, con un resumen que compara las conexiones logradas con la meta solicitada. Nunca registra una conexión que no llevó mensaje enviado: **conexión y mensaje van juntos**. El formato de fecha es siempre `YYYY-MM-DD`.

## Decisiones fundacionales

| Decisión | Qué significa | Por qué |
|---|---|---|
| Envío autónomo | El agente envía las solicitudes sin aprobación previa por contacto ni por lote | Acelera la prospección y reduce la carga manual |
| Sin ráfagas | Lotes pequeños con pausas automáticas entre acciones | LinkedIn limita y puede suspender cuentas con patrones de automatización; proteger la cuenta pesa más que la velocidad |
| Mouse y teclado acotados | Solo navegar, verificar y pulsar «Conectar»; nunca credenciales ni CAPTCHA | No sortear detección de bots ni manejar contraseñas |
| Cero invención | Los datos firmográficos vienen de una fuente; si no, en blanco con fuente y fecha | Los datos alimentan decisiones comerciales reales |
| Idioma detectado | Se escribe en el idioma real del perfil | Coherencia con el contacto; no se traduce mecánicamente |
| Español de trabajo | Comunicación y documentación en español; el mensaje puede salir en inglés | Consistencia con el repositorio |

## Salvaguardas de la cuenta

La cuenta de LinkedIn del usuario es el activo que hay que proteger. Las reglas de `control-navegador-linkedin` son no negociables:

- **Nunca omitir las pausas automáticas** entre envíos.
- **Nunca ráfagas masivas**: se respeta el tamaño de lote.
- **Nunca credenciales ni CAPTCHA.**
- Si LinkedIn muestra **un límite, una advertencia o una verificación de seguridad, el proceso se detiene de inmediato** y se notifica al usuario. No se reintenta de forma agresiva.
- No se conecta con perfiles que caigan en las exclusiones (gobierno, ONG, universidades, agencias de staffing o reclutamiento).

## Cómo se verifica un lote

No hay un script automático; la verificación es una revisión por lote:

- Cada contacto contactado está dentro de los cinco perfiles válidos y de las exclusiones.
- Cada mensaje tiene una etiqueta de idioma detectada **antes** de redactarse.
- Ningún mensaje afirma algo no verificado en el perfil.
- El informe `04` tiene una fila por conexión enviada, con la fecha real.
- Los datos firmográficos con fuente y fecha; los dudosos, en blanco.
- Ningún envío ocurrió tras un aviso de LinkedIn.

## Comandos «!»

Los comandos son órdenes cortas del usuario (`!optimize`, `!notime`…) que el agente debe ejecutar de forma obligatoria, siempre dentro de sus reglas duras. Hay un solo catálogo para todos los agentes y de él salen las instrucciones de cada uno, las bitácoras y las tablas de las guías.

### Dónde vive cada cosa

| Qué | Dónde |
|---|---|
| Catálogo, regla común y qué comandos tiene cada agente | `resources/comandos/comandos.py` (la fuente única; no se edita a mano nada de lo que genera) |
| Catálogo legible, matriz por agente y decisiones | `resources/comandos/catalogo.md` |
| Instrucciones del agente | sección «Comandos (`!`)» de `Perplexity.md`, entre las marcas `<!-- comandos:inicio -->` y `<!-- comandos:fin -->` |
| Tabla de esta guía | se genera del mismo catálogo al compilar las guías |

### La regla común

1. Un comando es una palabra precedida de `!` al inicio de un mensaje o de una línea; el texto que sigue es su objeto.
2. Es obligatorio: el agente no pide permiso ni lo reinterpreta. Solo lo limita una **regla dura** (veracidad, marca, confidencialidad, puertas de aprobación y de verificación); entonces hace lo que la regla permite y dice qué no pudo.
3. Se combinan. Si dos modos chocan, el orden es: reglas duras > `!strict-mode` y `!no-assumptions` > `!think-deep`, `!critical-mode` y `!double-check` > `!notime`.
4. Rige la tarea en curso, no las siguientes.
5. La primera línea de la respuesta nombra los comandos recibidos.
6. Un comando desconocido no se adivina: se propone el más parecido y se pregunta. `!help` lista los disponibles.
7. Si un comando cambió un entregable o la wiki, se anota en `wiki/log.md`.

### Cómo añadir o cambiar un comando

1. Edita `CMDS` (definición), `AGENTES` (a quién aplica y su nota) o `ALIAS` en `resources/comandos/comandos.py`.
2. Corre `python -X utf8 resources/comandos/comandos.py`: reescribe la sección de cada agente, el catálogo y, la primera vez, añade la entrada a su bitácora.
3. Recompila las guías (`python guides/_src/build.py`).
4. `python resources/comandos/comandos.py --verificar` falla si algo quedó desfasado.

### Comandos de este agente

```comandos
```

## Mantenimiento y cambios

La bitácora `wiki/log.md` solo se añade. Cada entrada sigue `## [YYYY-MM-DD] <tipo> | <descripción>` con tipos `setup`, `enriquecimiento`, `clasificacion`, `redaccion`, `envio` y `lint`. El lint periódico busca contradicciones entre páginas, buyer personas desactualizadas, plantillas que ya no reflejan la voz de marca y páginas huérfanas.

| Quiero… | Archivos que hay que tocar |
|---|---|
| Cambiar la plantilla del mensaje | La skill de mensajes (fuente única) y, si cambia el tono, `wiki/marca-campuslands.md` |
| Agregar o quitar un perfil de comprador | `wiki/perfiles-objetivo.md`, `wiki/filtros-busqueda.md` y la fase 2 de `Perplexity.md` |
| Cambiar la geografía o el tamaño de empresas | `wiki/filtros-busqueda.md` y `wiki/perfil-usuario.md` |
| Cambiar columnas de un CSV | `Perplexity.md` y la skill que lo escribe |
| Agregar un idioma | `deteccion-idioma` y `generacion-mensajes-personalizados` |
| Incorporar una regla nueva | `Perplexity.md` y su página de wiki, en el mismo cambio |

## Problemas frecuentes

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| LinkedIn pide verificación o muestra un límite | Detección de actividad automatizada | El agente se detiene y avisa. El usuario resuelve la verificación y se retoma después; no reintentar de inmediato |
| Un contacto no se procesa | No calza con los cinco perfiles o cae en una exclusión | Es el comportamiento esperado |
| El mensaje salió en el idioma equivocado | Evidencia mixta o señal de ubicación sobrevalorada | Revisar `deteccion-idioma`; ante ambigüedad la regla elige inglés |
| Piden mayor velocidad | Contradice la decisión de lotes pequeños | No se ajusta: es una salvaguarda de la cuenta |
| Faltan datos de empresa | No hubo fuente confiable | Es esperado; revisar la columna Fuente/Fecha del CSV 01 |

## Cosas a tener presentes

Al leer los archivos conviene saber que algunas referencias no están del todo alineadas:

- La skill `control-navegador-linkedin` aún se refiere al agente como **CampusScout**, su nombre anterior.
- `Perplexity.md` clasifica por cinco perfiles de comprador, mientras que `filtros-busqueda.md` prioriza los roles de Talento y RR. HH.; la skill pide un «filtro de búsqueda seleccionado» (A, B u otro). Son criterios complementarios que hoy se aplican juntos, pero no están unificados en un solo documento.
- El ICP de `prospection-agent/` es amplio y de cualquier geografía, mientras que el de este agente se centra en EE. UU.; la lista que entrega Radar puede traer empresas que los filtros de cuenta descartan.

## Relación con el resto del pipeline

```flow
Radar de Campus | Entrega el listado de empresas con datos públicos.
Explorador de Campus | Encuentra contactos y los conecta en LinkedIn.
Contacto interesado | La conversación continúa con el equipo comercial.
```

### Referencia rápida de archivos

| Archivo | Para qué lo abres |
|---|---|
| `Perplexity.md` | Identidad, decisiones, fases y CSV |
| `habilidades/*/SKILL.md` | Ajustar un paso concreto del procedimiento |
| `wiki/filtros-busqueda.md` | Cambiar filtros de cuenta, de contacto y búsquedas A y B |
| `wiki/perfiles-objetivo.md` | Cambiar los perfiles de comprador |
| `wiki/marca-campuslands.md` | Ajustar el tono del mensaje |
| `wiki/log.md` | Registrar cambios |
