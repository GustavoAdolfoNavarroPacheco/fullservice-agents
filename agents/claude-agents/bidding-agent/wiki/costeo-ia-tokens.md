# Costeo de IA y Estimación de Tokens

Método para el entregable #4: **qué actividades requieren IA, cuántos tokens
consumen y cuánto cuestan**.

> ⚠️ **Los precios de esta página caducan.** Antes de usarlos en un costeo nuevo,
> verifico la fecha de la tabla y confirmo los precios vigentes en la
> documentación oficial del proveedor. Si están desactualizados, los actualizo
> aquí antes de costear y lo registro en `log.md`.

---

## 1. Primero: ¿realmente se requiere IA?

La conclusión se toma en `04 - Consideraciones Tecnicas.md` y debe ser
**explícita y fundamentada en los documentos**. Se requiere IA cuando el alcance
incluye actividades como:

| Señal en el RFP / aclaraciones | Tipo de uso de IA |
|---|---|
| Chatbot, asistente virtual, agente conversacional, atención por WhatsApp | Generación conversacional |
| Clasificación o categorización automática de textos, tickets, documentos | Clasificación |
| Extracción de datos de documentos, facturas, formularios, PDFs escaneados | Extracción estructurada (+ OCR si son imágenes) |
| Resumen automático de textos, actas, expedientes | Resumen |
| Búsqueda semántica, "preguntas sobre documentos", base de conocimiento | RAG (recuperación + generación) |
| Traducción automática | Traducción |
| Análisis de sentimiento, priorización automática | Clasificación |
| Recomendaciones personalizadas basadas en lenguaje natural | Generación |
| Transcripción de audio o llamadas | Voz a texto (servicio distinto, no tokens de LLM) |
| Generación de reportes narrativos o insights en texto | Generación |

**Si ninguna de estas señales está presente**, la conclusión es que el alcance
**no requiere servicios de IA**, se deja constancia escrita en `04` con esa
justificación, y **no** se genera el entregable `05`. "No se mencionó" no es una
conclusión válida: hay que afirmar una u otra cosa.

**Ojo con lo que no es IA generativa:** reglas de negocio, validaciones,
automatización de flujos, reportes tabulares y búsquedas por palabra clave se
resuelven con desarrollo convencional. Proponer un LLM donde basta una consulta SQL
infla el costo y es indefendible ante el comité.

---

## 2. Precios de referencia (Claude · Anthropic) — actualizados 2026-07-29

Precios por **millón de tokens (MTok)**, en USD, API de primera parte:

| Modelo | ID | Contexto | Input $/MTok | Output $/MTok |
|---|---|---|---|---|
| Claude Opus 5 | `claude-opus-5` | 1M | 5.00 | 25.00 |
| Claude Sonnet 5 | `claude-sonnet-5` | 1M | 3.00 (2.00 promocional hasta 2026-08-31) | 15.00 (10.00 promocional) |
| Claude Haiku 4.5 | `claude-haiku-4-5` | 200K | 1.00 | 5.00 |

**Descuentos y multiplicadores que cambian el costo real:**

| Mecanismo | Efecto sobre el precio de input |
|---|---|
| **Lectura de caché de prompt** | ~0.1× (90% de ahorro) — aplica al prefijo reutilizado |
| **Escritura de caché** (TTL 5 min) | 1.25× |
| **Escritura de caché** (TTL 1 hora) | 2× |
| **Batch API** (procesamiento asíncrono) | 50% de descuento sobre input y output |

- El **caché de prompt** es determinante en costeos de chatbots y RAG: si el
  system prompt y el contexto base son estables, el 90% del input se cobra a 0.1×.
  Ignorarlo sobreestima el costo varias veces.
- El **Batch API** aplica a cargas no interactivas (clasificación masiva,
  procesamiento nocturno de documentos): 50% de descuento a cambio de latencia.
- Si el RFP exige un proveedor específico (Azure OpenAI, Bedrock, Vertex AI, un
  modelo local), **manda el RFP** y se usan los precios de ese proveedor,
  citando la fuente. Los precios de plataformas de socios difieren de los de
  primera parte.

### Selección de modelo por actividad
Se elige por exigencia real de la tarea, y se justifica en el entregable:

- **Haiku** — clasificación, extracción simple, tareas de alto volumen y baja
  complejidad donde importa el costo y la latencia.
- **Sonnet** — la mayoría de cargas productivas: conversación, RAG, resumen,
  extracción estructurada.
- **Opus** — razonamiento complejo, agentes de horizonte largo, tareas donde la
  calidad domina sobre el costo.

Mezclar modelos por actividad (Haiku para clasificar, Sonnet para responder) es una
optimización legítima y se documenta como tal.

---

## 3. Método de estimación de tokens

### 3.1 Regla de conversión (aproximación de trabajo)
Para español, **1 token ≈ 3–4 caracteres ≈ 0.75 palabras**. Es una aproximación
para dimensionar; **no se usa para facturar**.

**Para cifras precisas se usa el endpoint oficial de conteo de tokens**
(`/v1/messages/count_tokens` — en Python: `client.messages.count_tokens(...)`)
sobre prompts y documentos representativos del proyecto. **Nunca se usa `tiktoken`
ni tokenizadores de otros proveedores**: subcuentan los tokens de Claude en
~15–20% en texto normal y mucho más en código o texto no inglés.

Cuando el RFP aporta muestras de los documentos o conversaciones reales que
procesará el sistema, se cuentan esos y la estimación deja de ser aproximada.

### 3.2 Fórmula por actividad

```
Tokens de input  = (tokens de system prompt + tokens de contexto + tokens de mensaje)
                   × interacciones
Tokens de output = tokens de respuesta promedio × interacciones

Costo = (input_MTok × precio_input) + (output_MTok × precio_output)
```

Ajustado por caché y batch cuando apliquen:

```
Costo input = (input_no_cacheado × precio) 
            + (input_leído_de_caché × precio × 0.1)
            + (input_escrito_a_caché × precio × 1.25)
```

### 3.3 Variables de volumen — de dónde salen
Todas deben provenir del RFP, de las aclaraciones o de una confirmación explícita
del usuario. **Cada una se declara como supuesto con su fuente:**

| Variable | Fuente típica |
|---|---|
| Usuarios / consultas por período | RFP (capacidad exigida) o aclaraciones |
| Interacciones por usuario | Aclaraciones, o supuesto de trabajo declarado |
| Documentos a procesar y su tamaño | RFP, anexos, muestras |
| Meses de operación incluidos | Plazo contractual del RFP e hitos de pago |
| Tamaño del contexto por consulta | Diseño de la solución propuesta |

**Si un dato de volumen no está en ningún documento, se pregunta al usuario.** Si
el usuario indica trabajar con un supuesto, se declara textualmente como supuesto
en el entregable, no como dato del RFP.

### 3.4 Estructura del entregable `05`

Una fila por actividad de IA, con:

| Columna | Contenido |
|---|---|
| Actividad | Qué hace y qué requerimiento cubre (`RF-xx`) |
| Justificación de IA | Por qué requiere IA y no desarrollo convencional |
| Modelo propuesto | Con justificación de la elección |
| Volumen | Interacciones/documentos por mes, con su fuente |
| Tokens input / interacción | Desglosado: system + contexto + mensaje |
| Tokens output / interacción | Promedio estimado |
| % de input cacheable | Y su efecto en el costo |
| Tokens/mes (input y output) | Cálculo |
| Costo mensual USD | Cálculo |
| Meses de operación | Del plazo contractual |
| **Costo total USD** | |

Y al cierre:

- **Total de tokens** y **total de costo** del componente de IA.
- **Escenarios**: conservador / esperado / alto, variando el volumen. Un solo
  número puntual en un costeo de tokens es frágil; los escenarios muestran el
  rango y protegen el margen.
- **Margen de contingencia** sobre el escenario esperado, explícito y justificado.
- **Conversión a COP** si el modelo de costos lo exige: se usa la TRM que el
  usuario indique o la oficial de la fecha de la propuesta, **declarando la tasa y
  su fecha en el archivo**. Nunca se inventa una tasa de cambio.

### 3.5 Costos de IA que no son tokens
Se revisan y, si aplican, se incluyen:

- Almacenamiento y consulta de **embeddings / base vectorial** (en RAG).
- **OCR** o extracción de documentos escaneados.
- **Transcripción de voz** (si el alcance incluye llamadas o audio).
- Infraestructura de inferencia si el RFP exige **modelo local o on-premise** — ahí
  el costo es de cómputo (GPU), no de tokens, y se costea como infraestructura.
- Observabilidad, evaluación y monitoreo del componente de IA.

---

## 4. Reglas del costeo de IA

1. **Toda cifra de volumen tiene fuente documental o es un supuesto declarado.**
2. **El método de cálculo queda escrito en el archivo**, no solo el resultado.
3. **Se verifica la vigencia de los precios** antes de costear y se registra la
   fecha de verificación en el entregable.
4. **Se aplican caché y batch cuando corresponda**; ignorarlos produce un costo
   inflado e indefendible.
5. **Los escenarios son obligatorios**: conservador, esperado y alto.
6. **El costo de IA se traslada a los dos modelos de costos** (`06` y `07`); la
   verificación cruzada lo comprueba.
7. **Si no se requiere IA, se dice explícitamente** en `04` y no se genera `05`.
