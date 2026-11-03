---
titulo: Radar de Campus: cómo buscar empresas prospecto
resumen: Qué necesitas decirle, qué recibes y cómo revisar la lista de empresas que te entrega el agente de prospección.
---

## En resumen

**Radar de Campus** es el agente que te ayuda a encontrar empresas que podrían ser clientes de Campuslands. Tú le dices qué tipo de empresas buscas (por ejemplo, «constructoras medianas en Bogotá») y él te devuelve una lista ordenada, con datos públicos de cada empresa y la fecha de la búsqueda.

No necesitas saber de programación para usarlo. Basta con escribirle como le escribirías a un compañero que va a investigar por ti.

```stats
6 | datos son todo lo que necesita para empezar
0 | cifras inventadas: si no encuentra un dato, lo deja vacío
1.º | paso del flujo comercial: tu lista pasa después a Explorador de Campus
```

> [!tip] Si solo tienes un minuto
> Escribe qué sector buscas, en qué ciudad y cuántas empresas quieres. Si no sabes el resto (tamaño, empleados, facturación), dilo y sigue igual.

## Para qué sirve

Úsalo cuando necesites **una lista de empresas para empezar a prospectar**: saber cuáles existen, dónde están, cuántas personas emplean y, si es público, cuánto facturan. Es el primer paso antes de buscar a las personas con quienes conversar.

Radar busca únicamente en **internet público**: buscadores, prensa, directorios de empresas, gremios y la Superintendencia de Sociedades. **No entra a LinkedIn.**

### Qué tipo de empresas considera buenas

Por defecto busca empresas privadas que probablemente necesiten equipos técnicos: software, tecnología, fintech, e-commerce, y en general cualquier empresa con necesidad de desarrolladores. Prefiere las de **50 a 500 empleados**. Prioriza las que muestran señales de crecimiento, como vacantes abiertas, rondas de inversión o noticias de expansión.

**Por defecto no lista:** entidades de gobierno, ONGs, colegios y universidades, ni agencias de reclutamiento o staffing (son competencia directa). Si por algún motivo quieres incluirlas, díselo explícitamente.

## Antes de empezar: los 6 datos

Radar te pedirá estos seis datos, siempre en este orden. No tienes que saberlos todos.

| Dato | Qué es | Ejemplo |
|---|---|---|
| Número de empresas | Cuántas quieres en la lista | `15` |
| Sector | A qué se dedican | Constructoras, software, fintech |
| Ubicación | Ciudad donde tienen sede u operación | Bogotá |
| Tamaño | Pequeña, mediana o grande | Mediana |
| Número de empleados | Normalmente un mínimo | Más de 100 |
| Facturación anual | Normalmente un mínimo, en pesos si no dices otra moneda | $5.000.000.000 o más |

> [!nota] ¿Y si no sé alguno?
> Escribe «no sé», «cualquiera» o «no importa». Radar lo anota como «sin restricción» y busca igual. Solo te insistirá una vez por dato, y si no dices cuántas empresas quieres, trae 10 y te lo avisa.

### Una pequeña trampa: tamaño y empleados

Son dos formas de decir lo mismo. Si dices «Grande» pero «más de 10 empleados», no encajan. En ese caso Radar te preguntará cuál prefieres que use. No lo decide por su cuenta.

## Paso a paso

```lanes
Tú | Abre el agente en Perplexity y salúdalo
Agente | Te pide los 6 datos, o los confirma si ya los diste
Tú | Responde y confirma el resumen
Agente | Busca, completa los datos y arma la tabla
Tú | Revisa la lista y decide qué sigue
```

### 1. Abre el agente

Entra al Space de Radar de Campus en Perplexity y salúdalo, o escribe directamente lo que necesitas.

### 2. Responde el formulario

Puedes contestar uno por uno o escribirlo todo en un solo mensaje. Si ya diste todos los datos en tu primer mensaje, Radar **no repite las preguntas**: te muestra un resumen y te pide confirmar.

### 3. Confirma el resumen

Antes de buscar, Radar te repite lo que entendió, con los datos que dejaste «sin restricción» marcados como tales. Si algo está mal, corrígelo aquí. Después de tu confirmación empieza a buscar.

### 4. Recibe tu lista

Radar busca, completa cada empresa con información pública y te entrega una tabla. Puede tardar un poco: está revisando varias fuentes por cada empresa.

### 5. Decide qué sigue

Al final te pregunta si quieres **ampliar** la búsqueda, **repetirla con otros criterios** o **pasar la lista a Explorador de Campus**.

## Ejemplos de conversación

### Todo en un mensaje

```chat
Tú: Necesito empresas constructoras en Bogotá, medianas, con más de 100 empleados y facturación de $5.000.000.000 o más. Dame 15.
Agente: Entendido. Busco 15 empresas: sector Construcción, Bogotá, tamaño Mediana, +100 empleados, facturación $5.000.000.000 o más. ¿Confirmas?
Tú: Sí, confirmo.
```

### Con datos que no conoces

```chat
Tú: Busca 10 empresas de software en Medellín. El tamaño y la facturación no me importan.
Agente: Perfecto. Número: 10 · Sector: software · Ubicación: Medellín · Tamaño: sin restricción · Empleados: ¿hay un mínimo? · Facturación: sin restricción.
Tú: No hay mínimo de empleados.
```

### Sin decir cuántas empresas

```chat
Tú: Busca fintech en Bogotá, medianas.
Agente: No me diste un número de empresas, así que traeré 10 por defecto. ¿Te parece bien? Si prefieres otra cantidad, dímela.
```

### Una búsqueda nueva en la misma conversación

Cada búsqueda nueva vuelve a empezar por el formulario. Es normal y es intencional: así cada lista responde a un criterio claro.

```chat
Tú: Ahora quiero 20 empresas de e-commerce en Cali con más de 50 empleados.
Agente: Empecemos una búsqueda nueva. Número: 20 · Sector: e-commerce · Ubicación: Cali · Empleados: +50. ¿El tamaño y la facturación quedan sin restricción?
```

## Qué recibes

Al terminar, Radar te entrega cuatro cosas.

```cards
Un resumen | Qué criterios usó, cuántas empresas encontró frente a las que pediste y la fecha de la búsqueda.
Una tabla en el chat | Seis columnas: fecha, razón social, ubicación, número de empleados, facturación anual y utilidad neta.
Las fuentes | Debajo de la tabla, de dónde salió cada dato, para que puedas comprobarlo.
Un archivo CSV | La misma lista guardada como `01-empresas-encontradas.csv`, que se abre en Excel.
```

### Cómo se ve la tabla

La siguiente tabla es **solo un ejemplo ilustrativo**, con una empresa inventada para mostrar el formato:

| Fecha | Razón Social | Ubicación | Número de Empleados | Facturación Anual | Utilidad Neta |
|---|---|---|---|---|---|
| 2026-11-03 | Constructora Ejemplo S.A.S. | Bogotá | 140 | $8.200.000.000 | $430.000.000 |
| 2026-11-03 | Otra Empresa de Ejemplo S.A. | Bogotá | 220 | | |

Fíjate en que la segunda fila tiene **dos casillas vacías**. No es un error: significa que Radar no encontró esa cifra en una fuente confiable y prefirió dejarla vacía antes que inventarla.

> [!importante] La fecha de la tabla es la de tu búsqueda
> No es la fecha del dato financiero. Las cifras de facturación suelen corresponder al último año que la empresa reportó, que puede ser el año anterior. Ese detalle queda anotado en las fuentes.

## Cómo revisar tu lista

Antes de usar la lista, tómate un par de minutos para revisar:

- **¿Son del sector y la ciudad que pediste?** Si alguna no cuadra, avísale y la retira.
- **¿Los números tienen sentido?** Empleados y facturación deben parecerse a lo que esperabas.
- **¿Hay empresas que no deberían estar?** Gobierno, ONGs, colegios o agencias de reclutamiento no se listan por defecto. Si ves una, avísale.
- **¿Llegó al número pedido?** Si trajo menos, te lo dirá. Es mejor una lista corta y verdadera que una larga con relleno.
- **¿Cada dato tiene fuente?** Mira la sección de fuentes debajo de la tabla.

> [!nota] Tú decides
> Radar propone la lista; tú decides qué empresas pasan a la siguiente etapa.

## Qué hacer después

```flow
Ampliar | Pídele más empresas del mismo criterio.
Repetir | Cambia sector, ciudad o tamaño y empieza una búsqueda nueva.
Pasar a Explorador | Entrega la lista al agente que busca contactos en LinkedIn.
```

- **Ampliar:** «Amplía la búsqueda anterior con 10 empresas más del mismo sector». Respeta los criterios que ya confirmaste.
- **Repetir con otros criterios:** empieza una búsqueda nueva. Radar guarda cada una por separado.
- **Pasar a Explorador de Campus:** copia o adjunta tu lista. Explorador enriquece las empresas, busca a las personas indicadas en cada una y les escribe en LinkedIn.

## Lo que Radar no hace

| Si le pides… | Qué pasa | Qué hacer |
|---|---|---|
| Contactos o nombres de personas | No los busca: trabaja solo a nivel empresa | Pásale la lista a Explorador de Campus |
| Escribir mensajes de presentación | No los redacta | Eso lo hace Explorador de Campus |
| Buscar en LinkedIn | No entra a LinkedIn bajo ninguna circunstancia | Usa Explorador de Campus |
| Cifras que no encontró | No las inventa; deja la casilla vacía | Si es crítica, búscala por tu cuenta en la fuente que prefieras |

## Preguntas frecuentes

**¿Por qué me vuelve a pedir el formulario si ya lo llené?**
Porque cada búsqueda nueva empieza de cero. Si tu mensaje ya trae todos los datos, solo te pedirá confirmar.

**¿Por qué hay casillas vacías?**
Porque no encontró un dato confiable. Radar prefiere una casilla vacía a un número que podría estar mal.

**La lista trae menos empresas de las que pedí.**
Pasa cuando el criterio es muy estrecho. Radar te lo dice y no rellena con empresas que no cumplen. Puedes pedirle que amplíe o que relaje un criterio.

**¿Puedo pedirle empresas de otro país?**
Sí. La ubicación la defines tú en cada búsqueda. Si la ciudad puede confundirse, agrega el país.

**¿Las cifras son actuales?**
Son las más recientes que publica la fuente, normalmente del último año fiscal reportado. Al pie de la tabla queda la fuente de cada una.

**¿Dónde queda guardada mi lista?**
En el archivo CSV de la búsqueda, dentro de la carpeta `prospeccion` del agente, en una subcarpeta con un nombre que describe el criterio (por ejemplo, `constructoras-bogota-2026-11-03`).

## Glosario

| Término | Qué significa |
|---|---|
| Prospecto | Empresa que podría llegar a ser cliente |
| Razón social | Nombre legal registrado de la empresa |
| ICP | Perfil de empresa ideal para Campuslands |
| Supersociedades / SIREM | Entidad y sistema donde las empresas reportan sus estados financieros en Colombia |
| RUES | Registro oficial de empresas en Colombia |
| CSV | Archivo de tabla que se abre en Excel |
| Lote | Una búsqueda completa, con su propia carpeta y su propio archivo |

## Si algo no funciona

Si el agente no responde como esperas, repite tu mensaje con los seis datos completos. Si el comportamiento se repite o parece una falla, avisa a quien mantiene el agente; la guía técnica de Radar de Campus tiene una tabla de problemas frecuentes y qué revisar en cada caso.
