---
name: analisis-ia-tokens
description: Determina si el alcance de la licitación requiere servicios de inteligencia artificial, identifica qué actividades los requieren, estima la cantidad de tokens necesarios y calcula el costo estimado con precios vigentes verificados, en escenarios conservador/esperado/alto.
---

# Análisis de IA y Estimación de Tokens

## Cuándo usar esta skill

Como parte del entregable de consideraciones técnicas (`04`), en **toda** licitación
— incluso cuando la conclusión vaya a ser que no se requiere IA, porque esa
conclusión debe quedar escrita y fundamentada.

El entregable `05 - Analisis IA y Tokens.xlsx` se genera **solo si** la conclusión
es que sí se requiere.

No usar esta skill para: estimar horas de desarrollo del componente de IA (eso es
`estimacion-horas`, especialidad `IA`). Esta skill estima **consumo y costo de
tokens**, que es un costo operativo distinto del esfuerzo de construcción.

## Entradas

- `licitaciones/<slug>/00 - Analisis Documental.md` — requerimientos y volúmenes.
- `licitaciones/<slug>/02 - Propuesta Tecnica` — diseño de la solución.
- `wiki/costeo-ia-tokens.md` — precios vigentes y método.
- Muestras reales de documentos o conversaciones que procesará el sistema, si el
  RFP las aporta.

## Procedimiento

### Paso 1 — Decidir si se requiere IA (y dejarlo escrito)

Recorrer la tabla de señales de `wiki/costeo-ia-tokens.md` §1 contra los
requerimientos numerados. Señales típicas: chatbot o asistente conversacional,
clasificación automática de textos, extracción de datos de documentos, resumen
automático, búsqueda semántica / RAG, traducción, análisis de sentimiento,
generación de reportes narrativos, transcripción de audio.

**Distinguir lo que no es IA generativa:** reglas de negocio, validaciones,
automatización de flujos, reportes tabulares y búsquedas por palabra clave se
resuelven con desarrollo convencional. Proponer un LLM donde basta una consulta SQL
infla el costo y es indefendible ante el comité.

- **Si no se requiere IA:** escribir la conclusión y su razón en `04`, y no generar
  `05`. **"No se mencionó" no es una conclusión** — hay que afirmar una u otra cosa.
- **Si se requiere IA:** continuar.

### Paso 2 — Verificar la vigencia de los precios

Antes de calcular, comprobar la fecha de la tabla de precios en
`wiki/costeo-ia-tokens.md` y confirmar los precios vigentes en la documentación
oficial del proveedor. Si están desactualizados, actualizarlos ahí primero y
registrarlo en `wiki/log.md`. **Registrar la fecha de verificación en el propio
entregable `05`.**

Si el RFP impone un proveedor (Azure OpenAI, Bedrock, Vertex AI, modelo local),
**manda el RFP** y se usan los precios de ese proveedor, citando la fuente. Los
precios de plataformas de socios difieren de los de primera parte.

### Paso 3 — Recolectar las variables de volumen

Cada una con su fuente: usuarios/consultas por período, interacciones por usuario,
documentos a procesar y su tamaño, meses de operación incluidos, tamaño del
contexto por consulta.

**Si un dato de volumen no está en ningún documento, preguntar al usuario.** Si el
usuario indica trabajar con un supuesto, declararlo textualmente como supuesto en el
entregable, no como dato del RFP.

### Paso 4 — Contar tokens, no estimarlos a ojo

- Para dimensionar: 1 token ≈ 3–4 caracteres ≈ 0.75 palabras en español.
- **Para cifras que van al costeo: usar el endpoint oficial de conteo de tokens**
  (`/v1/messages/count_tokens`; en Python `client.messages.count_tokens(...)`) sobre
  prompts y documentos representativos.
- **Nunca usar `tiktoken`** ni tokenizadores de otros proveedores: subcuentan los
  tokens de Claude en ~15–20% en texto normal y mucho más en código o texto no
  inglés.

### Paso 5 — Elegir modelo por actividad y justificarlo

- **Haiku** — clasificación, extracción simple, alto volumen y baja complejidad.
- **Sonnet** — la mayoría de cargas productivas: conversación, RAG, resumen,
  extracción estructurada.
- **Opus** — razonamiento complejo, agentes de horizonte largo, calidad sobre costo.

Mezclar modelos por actividad (Haiku para clasificar, Sonnet para responder) es una
optimización legítima y se documenta como tal.

### Paso 6 — Calcular, aplicando caché y batch

```
Tokens input  = (system prompt + contexto + mensaje) × interacciones
Tokens output = respuesta promedio × interacciones

Costo input = (input_no_cacheado      × precio)
            + (input_leído_de_caché   × precio × 0.1)
            + (input_escrito_a_caché  × precio × 1.25)   [TTL 5 min; 2× si TTL 1 h]
Costo output = output_MTok × precio_output
```

- El **caché de prompt** es determinante en chatbots y RAG: si el system prompt y
  el contexto base son estables, ~90% de ahorro en esa porción del input.
  Ignorarlo sobreestima el costo varias veces y produce un precio no competitivo.
- El **Batch API** (50% de descuento) aplica a cargas no interactivas:
  clasificación masiva, procesamiento nocturno de documentos.

### Paso 7 — Costos de IA que no son tokens

Revisar e incluir si aplican: embeddings y base vectorial (RAG), OCR o extracción de
documentos escaneados, transcripción de voz, infraestructura de inferencia si el RFP
exige modelo local (ahí el costo es de cómputo GPU, no de tokens), observabilidad y
evaluación del componente de IA.

### Paso 8 — Construir `05 - Analisis IA y Tokens.xlsx`

Una fila por actividad, con: actividad y requerimiento que cubre, justificación de
por qué requiere IA, modelo propuesto y su justificación, volumen con su fuente,
tokens de input desglosados (system + contexto + mensaje), tokens de output,
porcentaje de input cacheable, tokens/mes, costo mensual USD, meses de operación y
costo total USD.

Al cierre:

- **Total de tokens** y **total de costo** del componente de IA.
- **Tres escenarios**: conservador / esperado / alto, variando el volumen. Un solo
  número puntual en un costeo de tokens es frágil.
- **Margen de contingencia** sobre el escenario esperado, explícito y justificado.
- **Conversión a COP** si el modelo de costos lo exige: con la TRM que el usuario
  indique o la oficial de la fecha de la propuesta, **declarando la tasa y su
  fecha**. Nunca inventar una tasa de cambio.
- **Fecha de verificación de precios.**

### Paso 9 — Trasladar el costo a los modelos de costos

El total del escenario esperado (más contingencia) entra en `06` y en `07`. La
verificación cruzada lo comprueba.

## Salidas

- Conclusión sobre IA escrita en `licitaciones/<slug>/04 - Consideraciones Tecnicas.md`.
- `licitaciones/<slug>/05 - Analisis IA y Tokens.xlsx`, si se requiere IA.
- Costo trasladado a `06` y `07`.

## Errores a evitar

- No pronunciarse sobre IA. La conclusión es obligatoria, sí o no.
- Proponer IA donde basta desarrollo convencional.
- Usar `tiktoken` o una regla de caracteres para las cifras finales.
- Ignorar el caché de prompt y el Batch API: infla el costo hasta volverlo no
  competitivo.
- Inventar volúmenes o tasas de cambio.
- Entregar un solo número puntual sin escenarios ni contingencia.
- Costear tokens y olvidar los costos de IA que no son tokens (embeddings, OCR,
  voz, GPU).
- Confundir el esfuerzo de construir el componente de IA (horas, especialidad `IA`)
  con el consumo operativo de tokens: son dos líneas distintas del costeo.
