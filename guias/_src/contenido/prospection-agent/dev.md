---
titulo: prospection-agent: guía técnica
resumen: Cómo está construido el agente de prospección de empresas, qué hace cada habilidad, qué formatos entrega y cómo se mantiene.
---

## En resumen

**Radar de Campus** (`prospection-agent`) es el agente de prospección de empresas de Campuslands. Dado un criterio de búsqueda (sector, ciudad, tamaño…), recorre la web abierta, filtra las empresas que encajan con el perfil de cliente de Full Service, completa cada una con datos públicos verificables y entrega un listado en tabla y en CSV.

Esta guía explica **cómo funciona por dentro**: los archivos que lo gobiernan, el ciclo de trabajo en tres fases, las cuatro habilidades que lo componen, los formatos de entrada y salida, las reglas que no se negocian y cómo modificarlo sin romperlo. Está pensada para quien mantiene el agente. Si solo necesitas usarlo, la guía de usuario es más corta y no requiere conocimientos técnicos.

```stats
1.º | eslabón del pipeline comercial: su salida alimenta a Explorador de Campus
3 | fases por búsqueda: intake, búsqueda y enriquecimiento, entrega
4 | habilidades (skills) encadenadas en `habilidades/`
6 | datos fijos en el formulario de entrada
```

> [!importante] Lo esencial en tres líneas
> Trabaja a nivel **empresa**, nunca a nivel persona. Busca solo en la **web abierta**: LinkedIn y Sales Navigator están prohibidos. Y **no inventa datos**: sin fuente verificable, la celda queda vacía.

## Qué hace y qué no hace

El agente cubre un hueco concreto del pipeline: el **descubrimiento de cuentas fuera de LinkedIn**. Todo lo que tenga que ver con personas, mensajes o LinkedIn pertenece a otro agente, Explorador de Campus (`intelligence-commercial/`). Mantener esa frontera limpia es una decisión fundacional: evita trabajo duplicado y protege la cuenta de LinkedIn del usuario.

| | Radar de Campus | Explorador de Campus |
|---|---|---|
| Unidad de trabajo | Empresa (la cuenta) | Persona dentro de la empresa |
| Fuente | Web abierta: buscadores, prensa, directorios, gremios, Supersociedades, sitios corporativos | LinkedIn y Sales Navigator |
| Qué entrega | Tabla de empresas + `01-empresas-encontradas.csv` | `04-informe-divulgacion.csv` con contactos y mensajes enviados |
| Redacta mensajes | No | Sí |
| Identifica cargos o personas | No | Sí |

Si el usuario pide «busca contactos», «escribe un mensaje» o «conéctate en LinkedIn» mientras está en este agente, la instrucción de `Perplexity.md` es **señalar que ese trabajo corresponde a Explorador de Campus** y ofrecer pasarle el listado ya generado.

## Cómo corre: Perplexity y `Perplexity.md`

A diferencia de los otros agentes del repositorio, que corren en Claude Code y se gobiernan con un `CLAUDE.md`, Radar de Campus está pensado para ejecutarse como **agente o Space en Perplexity**. Su archivo de configuración se llama `Perplexity.md` y cumple exactamente el mismo rol que un `CLAUDE.md`: son las instrucciones que el agente lee al iniciar cada sesión y que se co-evolucionan con el usuario.

`Perplexity.md` contiene, en este orden:

1. **Identidad:** nombre (Radar de Campus), rol (prospección B2B a nivel empresa) y relación con los demás agentes.
2. **Misión:** pedir el formulario de 6 datos y entregar un listado enriquecido.
3. **Decisiones fundacionales:** una tabla con cada decisión y su porqué (se resume más abajo).
4. **Deslinde con Explorador de Campus.**
5. **Estructura del CSV interno** y de la tabla entregada.
6. **Flujo de trabajo** en tres fases.
7. **Convenciones de mantenimiento** y de la bitácora.

> [!nota] Una regla de oro para quien edita
> Cualquier regla nueva que el usuario pida se incorpora **en `Perplexity.md` y en la página de wiki correspondiente, en el mismo cambio**. Si solo se actualiza uno de los dos, los archivos se contradicen y el agente pierde coherencia.

## Estructura del repositorio

```tree
prospection-agent/
  Perplexity.md                       # identidad, decisiones, fases y formatos
  habilidades/                        # una carpeta por skill, cada una con su SKILL.md
    formulario-intake/
    busqueda-web-empresas/
    enriquecimiento-datos-empresa/
    generacion-listado-resultados/
  prospeccion/                        # un lote por búsqueda
    <slug-lote>/
      01-empresas-encontradas.csv     # resultado del lote (con columna Fuente)
  recursos/                           # marca Campuslands y brief (solo lectura)
  wiki/
    index.md                          # catálogo de la wiki
    log.md                            # bitácora cronológica (solo se añade)
    perfil-usuario.md                 # quién es el usuario y el perfil de empresa objetivo (ICP)
    formulario-intake.md              # los 6 campos y su regla de obligatoriedad
    enlaces-utiles.md                 # fuentes y directorios de partida
```

Hay tres convenciones que conviene tener presentes:

- **`recursos/` es de solo lectura.** Son fuentes que provee el usuario (logos, brandbook, brief); el agente las lee, nunca las edita.
- **Un lote es una carpeta.** Cada búsqueda guarda su CSV en `prospeccion/<slug-lote>/`, de modo que lotes de criterios distintos nunca se mezclan ni se pisan.
- **El slug describe el criterio real.** Por ejemplo `constructoras-bogota-2026-07-23`: debe poder identificarse meses después sin abrir el archivo.

## El ciclo de trabajo

Cada búsqueda recorre tres fases. El ciclo **se reinicia en la fase 1 con cada búsqueda nueva**, incluso dentro de la misma conversación.

```flow
Intake | Skill `formulario-intake`. Pide o confirma los 6 datos y fija el criterio.
Búsqueda | Skill `busqueda-web-empresas`. Construye consultas y reúne candidatas con fuente.
Enriquecimiento | Skill `enriquecimiento-datos-empresa`. Completa cada ficha con cifras citables.
Entrega | Skill `generacion-listado-resultados`. Tabla de 6 columnas, fuentes y CSV.
```

### Fase 1 · Intake

Antes de ejecutar una sola consulta, el agente pide los seis datos del formulario (ver la sección «El formulario de entrada») y **confirma el criterio completo con el usuario**. Ninguna búsqueda corre sin haber pasado por esta fase al menos una vez en la conversación, aunque sea solo para confirmar datos que el usuario ya dio en su primer mensaje.

### Fase 2 · Búsqueda y enriquecimiento

Es el trabajo pesado, y se divide en dos habilidades:

1. `busqueda-web-empresas` arma las consultas combinando sector y ubicación como base, y aplica tamaño, empleados y facturación como filtros adicionales. Recorre fuentes de la web abierta, registra por cada candidata su razón social, sitio web y la fuente donde apareció, descarta duplicados y aplica las exclusiones del ICP. Sigue hasta acercarse al número de empresas pedido o hasta agotar razonablemente las fuentes.
2. `enriquecimiento-datos-empresa` toma cada candidata y completa ubicación, número de empleados, facturación anual y utilidad neta, **anotando la fuente y la fecha de consulta** de cada dato.

El resultado se guarda en `prospeccion/<slug-lote>/01-empresas-encontradas.csv`.

### Fase 3 · Entrega

`generacion-listado-resultados` consolida las fichas en una tabla de exactamente seis columnas, antepone un resumen (criterios usados, empresas encontradas frente a las solicitadas, fecha de ejecución) y añade al pie una sección de fuentes. Termina preguntando al usuario si quiere **ampliar la búsqueda**, **repetirla con otros criterios** o **pasar el listado a Explorador de Campus**.

## Las cuatro habilidades

Cada habilidad es un `SKILL.md` con la misma anatomía: cuándo usarla, entradas, procedimiento, reglas obligatorias y salida. Se encadenan en orden: la salida de una es la entrada de la siguiente.

| Habilidad | Entrada | Qué produce | Regla que más pesa |
|---|---|---|---|
| `formulario-intake` | Mensaje del usuario (con algunos, todos o ninguno de los 6 datos) | Criterio estructurado de 6 campos, cada uno con valor o «sin restricción» | Nunca buscar sin haber pasado por el formulario |
| `busqueda-web-empresas` | Criterio confirmado + ICP | Lista preliminar: razón social, sitio web y fuente inicial | Nunca LinkedIn; nunca inventar empresas para llegar al número pedido |
| `enriquecimiento-datos-empresa` | Candidata con su fuente inicial | Ficha: fecha, razón social, ubicación, empleados, facturación, utilidad, fuente interna | Cero invención, sobre todo en cifras financieras |
| `generacion-listado-resultados` | Fichas enriquecidas + criterio original | Tabla de 6 columnas + fuentes + CSV en disco | Exactamente 6 columnas, sin añadir otras |

### Detalles que no son obvios

**`formulario-intake`.** Si el usuario ya dio un dato claro, no se repite la pregunta: solo se confirma el resumen mapeado. Un «no sé», «cualquiera» o un campo sin respuesta tras preguntarlo una vez se marca como **sin restricción** y no se insiste. Si falta el número de empresas, se usa **10 por defecto** y se avisa antes de buscar. Si tamaño y número de empleados son contradictorios (por ejemplo «Grande» con «+10 empleados»), el agente pregunta cuál priorizar en vez de asumir.

**`busqueda-web-empresas`.** Descarta de inmediato cualquier resultado que provenga de LinkedIn y busca la misma información en otra fuente. Cada candidata necesita al menos una fuente verificable antes de pasar al enriquecimiento. Si la búsqueda no alcanza el número solicitado, **lo dice explícitamente** en lugar de rellenar con empresas que no calzan.

**`enriquecimiento-datos-empresa`.** Prioriza el RUES o la Cámara de Comercio sobre el nombre comercial para fijar la razón social legal. La fuente primaria de facturación y utilidad es la Superintendencia de Sociedades (SIREM) y se anota el **año fiscal** de la cifra, que puede no ser el año en curso. Si el dato real contradice el criterio del formulario, la empresa **se descarta** en vez de listarla igual.

**`generacion-listado-resultados`.** La columna Fecha es la fecha de ejecución de la búsqueda, no la del dato financiero; esa distinción vive en la fuente interna. Los campos no encontrados van vacíos, nunca con «N/A» como si fuera un dato confirmado.

## El formulario de entrada

El formulario es fijo y se pide siempre en este orden:

| # | Campo | Qué define | Ejemplo |
|---|---|---|---|
| 1 | Número de Empresas | Cuántas filas debe tener la tabla final; también define cuándo detener la búsqueda | `20` |
| 2 | Sector | Industria o vertical | Constructor, Fintech |
| 3 | Ubicación | Ciudad (más país si hay ambigüedad) donde la empresa tiene sede u operación | Bogotá |
| 4 | Tamaño | Categoría cualitativa | Pequeña, Mediana, Grande |
| 5 | Número de empleados | Umbral cuantitativo, normalmente un mínimo | `+100` |
| 6 | Facturación anual | Umbral de ingresos, normalmente un mínimo; COP si no se indica moneda | `$5.000.000.000 o más` |

### Obligatoriedad flexible

Se preguntan siempre los seis campos, pero **ningún dato faltante bloquea la búsqueda**. El único que conviene confirmar es el número de empresas, porque define el punto de parada. Esta decisión nace de que no todos los datos están disponibles desde el inicio y no se quiere frenar el flujo por eso.

### Mapeo directo

Cuando el mensaje inicial ya trae todo, el agente no repite el formulario: confirma el resumen mapeado y avanza.

```chat
Tú: Necesito empresas constructoras en Bogotá, medianas, con más de 100 empleados y facturación de $5.000.000.000 o más. Dame 15.
Agente: Entendido. Busco 15 empresas con este criterio: sector Construcción, ubicación Bogotá, tamaño Mediana, +100 empleados, facturación $5.000.000.000 o más. ¿Confirmas?
```

> [!tip] Tamaño y empleados
> Son dos formas de acotar lo mismo. Si el usuario da ambos y son consistentes, se usan juntos; si chocan, se pregunta. Nunca se elige en silencio.

## Formatos de salida

### CSV interno

`prospeccion/<slug-lote>/01-empresas-encontradas.csv` guarda el lote completo, con una columna extra de trazabilidad:

```tree
Fecha, Razón Social, Ubicación, Número de Empleados, Facturación Anual, Utilidad Neta, Fuente
```

### Tabla entregada al usuario

Tiene **exactamente seis columnas**, en este orden, y no se le agregan otras aunque se hayan usado como criterio de búsqueda (sector o sitio web viven solo en el resumen inicial).

| Fecha (YYYY-MM-DD) | Razón Social | Ubicación | Número de Empleados | Facturación Anual | Utilidad Neta |
|---|---|---|---|---|---|
| 2026-07-23 | *(ejemplo)* Constructora Ejemplo S.A.S. | Bogotá | — | — | — |

La fuente de cada fila no va en la tabla: se publica **debajo**, en una sección «Fuentes» numerada o por empresa, para mantener trazabilidad sin ensuciar las seis columnas principales.

### Qué antecede a la tabla

Un resumen breve con tres datos: los criterios del formulario que se usaron, cuántas empresas se encontraron frente a las solicitadas y la fecha real de ejecución.

## Fuentes de datos

`wiki/enlaces-utiles.md` es un punto de partida, no una lista cerrada: el agente puede y debe encontrar fuentes adicionales relevantes al criterio. Antes de usar cualquier enlace conviene verificar que siga activo, porque directorios y gremios cambian de dominio.

| Tipo | Ejemplos | Para qué sirve |
|---|---|---|
| Datos financieros | Superintendencia de Sociedades (SIREM) | **Fuente primaria** de ingresos y utilidad neta de empresas que reportan en Colombia |
| Registros empresariales | RUES, Cámara de Comercio de Bogotá, Confecámaras | Razón social legal y sede |
| Gremios | ANDI, Fedesoft, Colombia Fintech, ProColombia | Descubrir empresas por sector |
| Directorios de startups | Crunchbase, F6s, Wellfound | Rondas de inversión y tamaño |
| Señales de contratación | Computrabajo, elempleo, Indeed Colombia, Magneto365 | Detectar vacantes técnicas abiertas |
| Prensa | La República, Portafolio, Dinero, Contxto, TechCrunch | Señales de crecimiento o inversión |

> [!importante] La fuente primaria siempre es el sitio oficial
> El sitio web de cada empresa candidata es la fuente primaria para verificar sector, sede y tamaño declarado. Cualquier dato hallado en un directorio se confirma contra él antes de listarlo.

Las cifras de SIREM suelen corresponder al **último año fiscal reportado**. Se anota el año del estado financiero como parte de la fuente. Si la empresa no reporta a Supersociedades o la cifra no es pública, facturación y utilidad quedan vacías: nunca se estiman.

## El perfil de empresa objetivo (ICP)

`wiki/perfil-usuario.md` define qué empresa vale la pena listar. Es la referencia por defecto cuando el usuario deja un campo «sin restricción».

- **Sector:** desarrollo de software, servicios o consultoría IT, tecnología, información e internet y, en general, cualquier empresa que necesite equipo técnico propio (fintech, healthtech, e-commerce, SaaS).
- **Tamaño:** preferentemente 50–500 empleados, con esta segmentación: pequeña (50–100), mediana (101–250), grande (251–500). Por debajo de 50 suele faltar presupuesto o estructura recurrente para staffing.
- **Tipo:** empresa privada.
- **Señales de calificación** (mientras más, mejor prospecto): crecimiento de plantilla, vacantes abiertas para desarrolladores, ronda de inversión reciente, noticias de expansión o transformación digital.

**Exclusiones estrictas:** gobierno, ONGs, colegios y universidades, y agencias de staffing o reclutamiento (competencia directa de Campuslands). Solo se levantan si el usuario lo indica de forma explícita.

## Reglas duras

| Regla | Qué significa en la práctica | Por qué |
|---|---|---|
| Solo web abierta | Prohibido LinkedIn y Sales Navigator, como fuente y como verificación | Esa función ya existe en Explorador de Campus; duplicarla genera trabajo redundante y riesgo para la cuenta |
| Nivel empresa | Nunca nombres de personas ni cargos | Mantener responsabilidades separadas entre agentes |
| Cero invención | Cada dato lleva fuente y fecha; sin confianza razonable, el campo queda vacío y se anota qué se intentó | Los datos, incluidas cifras financieras, alimentan decisiones comerciales reales |
| Formulario flexible | Se piden los 6 campos; un dato desconocido no frena el flujo | No todos los datos están siempre disponibles |
| Entrega acotada | Tablas de empresas; nada de mensajes ni acciones de envío | Ese trabajo es de Explorador de Campus |
| Sin restricción geográfica fija | La ubicación la define el usuario en cada sesión | El caso original es LATAM, pero el agente sirve para cualquier geografía |
| Español | Comunicación y documentación en español; las fuentes pueden quedar en su idioma | Consistencia con el resto del repositorio |

## Cómo se verifica un lote

No hay un script automático: la verificación es una lista que el agente aplica en cada entrega.

- **Cantidad.** El resumen inicial dice cuántas empresas se encontraron frente a las solicitadas.
- **Trazabilidad.** Cada cifra tiene fuente y fecha en el CSV. Sin fuente, no hay dato.
- **Encaje con el criterio.** Sector, ciudad, tamaño y exclusiones coinciden con el formulario confirmado.
- **Contradicciones resueltas.** Si tamaño y empleados chocan, se preguntó cuál priorizar.
- **Formato.** Exactamente seis columnas y la fecha en `YYYY-MM-DD`.
- **Sin duplicados.** Una empresa aparece una sola vez por lote, deduplicada por dominio o razón social normalizada.
- **Sin LinkedIn.** Ninguna fila ni fuente proviene de allí.

## Mantenimiento y cambios

### La wiki

La wiki es el conocimiento que el agente acumula. `index.md` es el catálogo y `log.md` la bitácora, que **solo se añade, nunca se reescribe**. Cada entrada empieza con un prefijo consistente para que se pueda buscar:

```
## [YYYY-MM-DD] <tipo> | <descripción>
```

Los tipos válidos son `setup`, `busqueda`, `enriquecimiento`, `entrega` y `lint`.

### Lint periódico

De vez en cuando conviene revisar: campos del formulario desactualizados frente al ICP vigente, enlaces rotos o gremios que ya no existen en `enlaces-utiles.md`, y páginas huérfanas de la wiki.

### Si quieres cambiar algo, toca esto

| Quiero… | Archivos que hay que tocar |
|---|---|
| Agregar un campo al formulario | `Perplexity.md`, `wiki/formulario-intake.md` y la skill `formulario-intake` |
| Agregar una columna al listado | CSV y tabla en `Perplexity.md`, y la skill `generacion-listado-resultados` |
| Cambiar el perfil de empresa o las exclusiones | `wiki/perfil-usuario.md` (lo leen las skills de búsqueda y enriquecimiento) |
| Sumar o quitar una fuente | `wiki/enlaces-utiles.md`, y revisar enlaces rotos |
| Incorporar una regla nueva del usuario | `Perplexity.md` y su página de wiki, en el mismo cambio |
| Dejar constancia | Una entrada en `wiki/log.md` con el tipo que corresponda |

## Problemas frecuentes

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| La tabla trae menos empresas de las pedidas | Criterios estrechos; el agente no rellena con empresas que no calzan | Es esperable. Ofrecer ampliar la búsqueda o relajar un criterio |
| Facturación o utilidad neta vacías | No hubo fuente confiable, o la empresa no reporta a Supersociedades | No es un fallo. Revisar la columna Fuente del CSV para ver qué se intentó |
| Piden contactos, cargos o mensajes | Fuera del alcance de este agente | Pasar el listado a Explorador de Campus |
| El agente vuelve a pedir el formulario | Es por diseño: cada búsqueda nueva reinicia en la fase 1 | Explicar al usuario que es normal; si ya dio todo en un mensaje, solo confirmará |
| Tamaño y empleados parecen contradecirse | El usuario dio criterios inconsistentes | Responder cuál prioriza; el agente no asume |
| Aparece una fuente de LinkedIn | La skill debió descartarla | Revisar `busqueda-web-empresas` y repetir con otra fuente |

## Relación con el resto del pipeline

Radar de Campus es el **primer eslabón**. Su listado alimenta a Explorador de Campus, que enriquece, clasifica y contacta a las personas de cada empresa. El ICP es el mismo en ambos agentes; lo que cambia es el nivel: aquí se califica la **empresa**, allá la **persona** dentro de la empresa ya calificada.

```flow
Radar de Campus | Descubre y enriquece empresas en la web abierta
Explorador de Campus | Encuentra contactos y envía conexiones en LinkedIn
Estudio de Presentaciones | Prepara la presentación comercial al contacto interesado
```

### Referencia rápida de archivos

| Archivo | Para qué lo abres |
|---|---|
| `Perplexity.md` | Entender o cambiar identidad, decisiones, fases y formatos |
| `habilidades/*/SKILL.md` | Ajustar el procedimiento de un paso concreto |
| `wiki/formulario-intake.md` | Cambiar los campos del formulario o su regla de obligatoriedad |
| `wiki/perfil-usuario.md` | Cambiar el perfil de empresa objetivo y sus exclusiones |
| `wiki/enlaces-utiles.md` | Actualizar fuentes y directorios |
| `wiki/log.md` | Registrar qué se cambió y cuándo |
| `prospeccion/<slug-lote>/` | Consultar resultados de búsquedas anteriores |
