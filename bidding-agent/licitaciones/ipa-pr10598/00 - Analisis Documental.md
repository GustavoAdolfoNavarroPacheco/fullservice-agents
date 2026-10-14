# 00 — Análisis Documental · RFP No. PR10598 (IPA Colombia)

**Estado: EN CONSULTA.** Hay decisiones bloqueantes pendientes de respuesta del
usuario (sección 9). Este documento no se considera cerrado hasta resolverlas.

> ⚠️ **Alerta de plazo.** El RFP vence el **30 de julio de 2026, 2:00 pm**. Hoy es
> 29 de julio de 2026. Queda menos de un día hábil para radicar. Ver sección 4.

---

## 1. Datos del proceso

| Campo | Valor | Fuente |
|---|---|---|
| Entidad | Asociación Innovations for Poverty Action (IPA) Colombia | RFP p.4 |
| Proceso | RFP No. PR10598 | RFP p.1 |
| Objeto | Diseño, desarrollo e implementación de un agente de IA a través de WhatsApp para brindar apoyo sobre procedimientos de regularización migratoria (transición PPT → Visa R) a refugiados y migrantes venezolanos en Colombia, en el marco del proyecto "Una Visa por un Sueño" | RFP p.1, §1.1 |
| Naturaleza del proyecto | El agente es un **brazo de tratamiento de un ensayo controlado aleatorizado (ECA)**, no un producto comercial. Estabilidad, consistencia y auditabilidad total del comportamiento durante el estudio son requisito de validez interna del experimento | RFP §1.1 |
| Fecha de emisión RFP | 21 de julio de 2026 | RFP p.4 |
| Fecha límite de preguntas | 23 de julio de 2026, 2:00 pm (ya cerrada; Q&A publicado) | RFP p.4 |
| Fecha de publicación de respuestas | 27 de julio de 2026 | Aclaraciones p.1 |
| **Plazo de recepción de propuestas** | **30 de julio de 2026, 2:00 pm** | RFP p.4 |
| Dirección de envío | co_propuestas@poverty-action.org, asunto "Propuesta RFP No. PR10598 - NOMBRE DEL OFERENTE", un solo correo, un solo .zip con subcarpetas en PDF | RFP §2.1, §5.2 |
| Tipo de adjudicación | Contrato de precios mixtos (fijos y variables) | RFP p.4, §1.3 |
| Duración de ejecución | 4 meses (desarrollo, integración KB, evaluación de precisión, piloto, despliegue, escalado, informes) + 30 días de soporte de estabilización POSTERIOR y fuera de esos 4 meses | RFP §11.1.5; Aclaración P64 |
| Presupuesto oficial publicado | No se declara techo presupuestal. "Los oferentes deberían proponer lo que consideren un precio justo" | RFP §11.3 (Aclaraciones) |
| Base de la adjudicación | Mejor valor: 85 puntos técnicos + 15 puntos de costo (ver §5) | RFP §5.1 |

---

## 2. Inventario de documentos recibidos

| # | Rol esperado | Documento recibido | Fecha | Estado |
|---|---|---|---|---|
| 1 | RFP | `01_IPA_PR10598_RFP_OFICIAL_2026-07-21.pdf` (37 pág., incluye como Anexo 11.1 el Alcance de Trabajo y como Anexo 11.3 la Propuesta Económica) | 21-jul-2026 | ✅ Completo |
| 2 | Aclaraciones / Q&A | `Documento de Aclaraciones - Preguntas y Respuestas (QA) RFP No. PR10598.pdf` (66 preguntas, varias con enmienda) | 27-jul-2026 | ✅ Completo |
| 3 | Modelo de costos oficial de la empresa | **No se recibió un archivo separado.** El formato de costeo exigido por IPA está **embebido en el propio RFP**, Anexo 11.3 "Propuesta económica" (p.30-35): tabla de 7 componentes de costo con columnas Especificaciones / Cantidad / Precio unitario / Precio Total / Moneda. | 21-jul-2026 (parte del RFP) | ⚠️ Se usará la tabla del RFP como el "modelo oficial" — **confirmar con el usuario en §9** |
| 4 | Segundo modelo de costos (cotización interna) | **No se recibió.** Se recibieron en su lugar dos archivos relacionados que **no son la plantilla estándar de cotización de FullService**: ver detalle abajo. | — | ❌ Falta — **bloqueante, ver §9** |

### Documentos adicionales recibidos (no corresponden a ninguno de los 4 roles obligatorios)

**A. `01_IPA_AMBITO_TRABAJO_OFICIAL_2026-06-23 (borrador previo, superado por el RFP).docx`**
Es un borrador del alcance de trabajo fechado **23 de junio de 2026**, casi un mes
antes de la emisión oficial del RFP (21-jul-2026). Su contenido es una versión
anterior del actual Anexo 11.1 del RFP, con **cifras ya superadas**: habla de
**1.000 usuarios** y **~16.000 mensajes salientes**, mientras el RFP oficial y las
Aclaraciones fijan **800 usuarios** y **~12.800 mensajes salientes**. Se trata como
antecedente histórico únicamente; **ninguna cifra de este archivo se usa** en los
entregables. Ver contradicción C-01 en §7.

**B. `2026-07-28_Modelo_Costos_TCO_IPA_v0_3_JP (borrador interno Aurena AI, no aprobado).xlsx`**
Es un modelo de costeo y TCO muy detallado (16 hojas: supuestos, precios de
proveedor investigados, costo cargado por rol, cuatro "capas" de costo alineadas
con los 7 componentes del formulario de IPA, escenarios Bajo/Base/Alto, matriz
económica, cuatro niveles de precio, sensibilidad, contingencia por riesgo y flujo
de caja), fechado **28 de julio de 2026** (ayer). El propio archivo se declara a sí
mismo: *"USO INTERNO · BORRADOR v0.3 · NO APROBADO"*, preparado por **Juan Pablo
Pérez Mejía, de una firma identificada como "Aurena AI"**, para una *"reunión
interna Aurena–Campus Lands"*. Trae una hoja de reconciliación (`13`) explícitamente
vacía en la columna "Estimación Campus Lands", a la espera de una estimación de una
persona identificada como **"Héctor"**.

Este archivo **no es la plantilla estándar de cotización de FullService** que
`habilidades/modelos-costos/SKILL.md` espera como insumo 4, pero contiene
investigación de precios de proveedor (Anthropic, Meta/WhatsApp, AWS) e ingeniería
de costos ya alineada con el RFP y sus aclaraciones, que puede ahorrar trabajo
significativo si el usuario confirma su uso. Ver bloqueante B-02 en §9.

**C. Cotización previa en el repositorio hermano `QuoteDeveloper`**
Se detectó (fuera de `recursos/`, en el monorepo) una carpeta
`QuoteDeveloper/cotizaciones/ipa-pr10598/` con `IPA PR10598 - Cotizacion.xlsx` y
`IPA PR10598 - Cotizacion de Alcance.pdf`, aparentemente de un trabajo previo sobre
este mismo proceso. No se ha abierto su contenido todavía porque no fue aportada
como insumo de esta licitación y podría corresponder al alcance antiguo de 1.000
usuarios. Ver bloqueante B-02 en §9.

---

## 3. Inventario de requerimientos

Identificador estable para usar en la matriz de cumplimiento (`01`). Cobertura
completa de RFP + Aclaraciones; el nivel de atomización aquí es de "actividad", la
matriz de cumplimiento (Fase 2) hará la correspondencia 1:1 fila por fila.

### RF — Funcionales

| ID | Requerimiento | Origen |
|---|---|---|
| RF-01 | Diseñar/desarrollar agente de IA que interactúe por WhatsApp (texto, imagen, video) guiando en trámites de regularización migratoria | RFP §11.1.2-3 |
| RF-02 | Integración con WhatsApp mediante API oficial o proveedor autorizado (Cloud API / BSP) | RFP §11.1.4-I |
| RF-03 | Arquitectura LLM + recuperación sobre la base de conocimiento (RAG o carga de KB completa, ~14.000 tokens); el oferente elige y justifica | RFP §11.1.4-I; RFP p.24 |
| RF-04 | Control de versiones de prompts, flujos, configuración del modelo y KB, con aprobación previa de IPA ante cualquier cambio durante el estudio | RFP §11.1.4-I |
| RF-05 | Registro completo de conversaciones (timestamp, ID seudonimizado, versión del agente), exportable en formato estructurado (CSV) | RFP §11.1.4-I |
| RF-06 | Estructurar la base de conocimiento de IPA (orientación semanal, FAQ, elegibilidad, documentación, costos, plazos) | RFP §11.1.4-2 |
| RF-07 | Respuestas restringidas exclusivamente al contenido validado por IPA; rechazo de preguntas fuera de alcance | RFP §11.1.4-2 |
| RF-08 | Proceso de actualización versionado de la KB con aprobación previa de IPA y publicación sin redistribución completa | RFP §11.1.4-2 |
| RF-09 | Derivación de consultas no sensibles no resueltas al canal humano del proveedor, SLA 4 horas hábiles (L-V 8:00-17:00 Colombia); si no está en contenido validado, escalar a IPA | RFP §11.1.4-3; Aclaración P6 |
| RF-10 | Detección de casos sensibles: mensaje aprobado (sin asesoría legal) + notificación a IPA en ≤15 min, 24/7, por WhatsApp Y correo, con identificador, fecha/hora, tipo de caso y transcripción | RFP §11.1.4-3; Aclaración P7 |
| RF-11 | Detección y reporte periódico (mín. semanal) de señales de abandono/inactividad | RFP §11.1.4-3 |
| RF-12 | Conjunto de preguntas representativas (construido por el proveedor, clave validada por IPA) antes del piloto; reporte de tasa de correctas/incorrectas/rechazadas en desarrollo, piloto e implementación | RFP §11.1.4-4; Aclaración P12, P50 |
| RF-13 | Comportamiento de rechazo definido para preguntas fuera de alcance, en particular asesoría legal | RFP §11.1.4-4 |
| RF-14 | Umbral mínimo de precisión (a definir junto con IPA antes del piloto) como gate go/no-go; ventana de remediación de 1-2 semanas si no se alcanza | RFP §11.1.4-4; Aclaración P11, P53-55 |
| RF-15 | Diseño y pruebas de UX para baja alfabetización; nivel de lectura objetivo definido y medido; manejo de español coloquial LatAm y variantes venezolanas | RFP §11.1.4-5 |
| RF-16 | Fase piloto con ~10 usuarios definidos por IPA; informe piloto con métricas y recomendación go/no-go | RFP §11.1.4-6 |
| RF-17 | Fase de implementación a ~800 usuarios (grupo de tratamiento 4); monitoreo de entrega, volumen, resolución, abandono y precisión | RFP §11.1.4-7; Aclaración P60 (corrige de 1.000 a 800) |
| RF-18 | El agente interactúa exclusivamente con los usuarios asignados por IPA (lista de números); no con grupo de control ni otros brazos | RFP §11.1.2; Aclaración P13 |
| RF-19 | Envío proactivo de contenido semanal según guía de IPA + respuesta a interacciones entrantes (espontáneas o reactivas) | Aclaración P26 |
| RF-20 | Integración de multimedia (imágenes/video) suministrado por IPA en formato final, alojado directamente (no por enlaces); sin procesamiento de imágenes ni notas de voz entrantes del usuario | RFP §11.1.6; Aclaración P23, P38 |
| RF-21 | Soporte a la transferencia del agente a organización implementadora al finalizar: código, infraestructura, cuenta/número WhatsApp, KB, prompts, flujos, credenciales admin, documentación completa | RFP §11.1.4-7, §11.1.4-9 |

### RNF — No funcionales

| ID | Requerimiento | Origen |
|---|---|---|
| RNF-01 | Disponibilidad 24/7, escalable, consistente; estabilidad de comportamiento exigida por la validez interna del ECA | RFP §1.1 |
| RNF-02 | Infraestructura dimensionada para ~12.800 mensajes salientes + ~11.200 consultas entrantes (14/usuario), con altas escalonadas en 8 semanas sobre base constante de 800 usuarios | RFP §11.1.2; Aclaración P5, P59 |
| RNF-03 | Alta disponibilidad, balanceo de carga, monitoreo, recuperación ante fallos, tiempo de respuesta, sin degradación en conversaciones múltiples | RFP §5.1 A9 |
| RNF-04 | Herramientas de monitoreo del agente: desempeño, consumo, errores, métricas operativas | RFP §5.1 A10 |
| RNF-05 | Trazabilidad/auditabilidad completa de cambios en prompts, configuración, flujos y KB durante todo el estudio | RFP §5.1 A7 |
| RNF-06 | Seguridad: segmentación, autenticación, autorización, gestión de credenciales, protección de APIs | RFP §5.1 D1 |
| RNF-07 | Cifrado en tránsito/reposo; retención/eliminación de datos; controles de acceso; lista completa de subprocesadores | RFP §5.1 D2 |
| RNF-08 | Declarar ubicación de almacenamiento/procesamiento y transferencias transfronterizas (sin prohibición absoluta, pero exige declaración) | RFP §5.1 D3; Aclaración P21 |
| RNF-09 | Garantía de que el proveedor del modelo de lenguaje no entrena con datos de conversación y retiene al mínimo (basta acreditar términos comerciales vigentes) | RFP §5.1 D4; Aclaración P20 |
| RNF-10 | Límite de mensajería de WhatsApp Business (250 destinatarios únicos/24h en portafolio nuevo) obliga a gestionar el escalado de límites para alcanzar 800 usuarios | Investigación de mercado (no es texto del RFP; se documenta como consideración técnica) |

### TEC — Técnicos

| ID | Requerimiento | Origen |
|---|---|---|
| TEC-01 | Integración con WhatsApp Business API oficial o BSP autorizado | RFP §11.1.4-I |
| TEC-02 | Decisión de arquitectura RAG vs. contexto completo, justificada | RFP p.24 |
| TEC-03 | Escenario común de tokens obligatorio para costeo: entrada 8.200 (RAG) / 20.200 (KB completa); salida ~350; KB ~14.000 | RFP p.30-31 |
| TEC-04 | Decisión sobre uso de razonamiento extendido, justificada, con su efecto en costo/latencia declarado | RFP p.31 |
| TEC-05 | Exportación de registros en formato estructurado | RFP §11.1.4-I |
| TEC-06 | Provisión, verificación de negocio y gestión de la cuenta/número de WhatsApp Business durante el contrato, con transferencia al final | Aclaración P8 |
| TEC-07 | Vía redundante de notificación de casos sensibles (WhatsApp + correo), monitoreada 24/7 | Aclaración P7 |
| TEC-08 | Sin requerimiento de procesar audio entrante ni generar audio saliente (salvo el ya embebido en videos entregados) | Aclaración P38 |

### PLZ — De plazo

| ID | Requerimiento | Origen |
|---|---|---|
| PLZ-01 | **Recepción de propuestas: 30-jul-2026, 2:00 pm** | RFP p.4 |
| PLZ-02 | Plazo total de ejecución: 4 meses desde firma | RFP §11.1.5 |
| PLZ-03 | Entregables 1-3 (agente, documentación, informe precisión pre-piloto): 30 días desde firma | RFP §6 |
| PLZ-04 | Entregable 4 (informe piloto): 60 días desde firma | RFP §6 |
| PLZ-05 | Entregables 5-6 (informe despliegue, paquete de traspaso): 120 días desde firma | RFP §6 |
| PLZ-06 | Soporte de estabilización de 30 días POSTERIOR al traspaso, fuera de los 4 meses | Aclaración P64 |
| PLZ-07 | Fase de levantamiento/línea base al inicio, dentro de los 4 meses (no los extiende) | Aclaración P40-42 |
| PLZ-08 | IPA acepta cada entregable en 10 días hábiles; paga máx. 8 días calendario después; demoras de IPA extienden plazos dependientes sin penalizar al proveedor | Aclaración P62 |
| PLZ-09 | Pólizas exigidas dentro de los 5 días siguientes a la firma del contrato | RFP §4.2 |

### ADM — Legal / administrativo

| ID | Requerimiento | Origen |
|---|---|---|
| ADM-01 | **No se aceptan consorcios ni uniones temporales — un único oferente (persona jurídica)** | Aclaración P3, P31-34 |
| ADM-02 | Documentos legales: certificado de existencia y rep. legal (≤30 días), RUT (2026), cédula rep. legal, EEFF comparativos 2 años, certificación bancaria (2026), 3 certificaciones de contratos similares **a nombre del oferente** (no de aliados), últimos 5 años, mín. 70% avance si en ejecución, antecedentes judiciales del rep. legal | RFP §5.2-III; Aclaración P2, P37 |
| ADM-03 | Pólizas post-adjudicación: cumplimiento 30% + calidad 30% + salarios 10% del valor total CON impuestos; buen manejo de anticipo 100% solo si se pide anticipo | RFP §4.2; Aclaración P17, P18 |
| ADM-04 | DPA firmado conforme Ley 1581/2012 y normas de IPA — requisito habilitante | RFP §5.2-X, §11.1.4-8 |
| ADM-05 | IPA propietaria de todo lo producido bajo el contrato; PI preexistente/reutilizable/terceros bajo licencia perpetua y transferible a IPA para este proyecto; se exige inventario de PI preexistente | RFP §11.1.4-9; Aclaración P58 |
| ADM-06 | Validez de precios: 90 días calendario | RFP §2.2 |
| ADM-07 | Propuesta en español, un correo, un .zip, PDF, formato de 10 secciones (I-X) | RFP §2.1, §5.2 |
| ADM-08 | No se admiten ofertas parciales — oferta por la totalidad del alcance | RFP §2.1 |
| ADM-09 | Confidencialidad absoluta de información de IPA y datos de sujetos humanos (Ley 1581/2012, Decretos 1377/2013 y 1074/2015) | RFP §8 |
| ADM-10 | Certificación de ética en la adquisición (sin pagos indebidos ni a terroristas) | RFP §10 |

### ENT — De entregables

| ID | Requerimiento | Origen |
|---|---|---|
| ENT-01…06 | Los 6 entregables contractuales de la tabla RFP §6 (agente funcional; documentación KB/flujos/prompts/config; informe precisión pre-piloto; informe piloto; informe de despliegue con registros exportables y análisis de abandono; paquete de traspaso) | RFP §6 |
| ENT-07 | Documentación requerida por el Comité de Ética (IRB) de IPA para protección de datos, si el Comité lo solicita | Aclaración P14 |

### OPS — De operación y soporte

| ID | Requerimiento | Origen |
|---|---|---|
| OPS-01 | Canal de respuesta humana SLA 4h hábiles, L-V 8:00-17:00 Colombia, dotado por el proveedor, costo en línea recurrente | RFP §11.1.4-3; Aclaración P6 |
| OPS-02 | Guardia 24/7 de notificación/monitoreo de casos sensibles (15 min, WhatsApp+correo) | Aclaración P7 |
| OPS-03 | Soporte de estabilización de 30 días posterior al traspaso | RFP §6, entregable 6 |
| OPS-04 | Costos operativos del ECA (mensajería, modelo, hosting, soporte humano) a cargo del proveedor en costos recurrentes; costos post-transferencia fuera del contrato y deben divulgarse | RFP §11.1.6 |
| OPS-05 | Monitoreo y reporte de métricas de rendimiento durante todo el despliegue | RFP §11.1.4-7 |

---

## 4. Plazos y hitos

Ver tabla en §1 y requerimientos `PLZ-*`. El punto crítico inmediato: **quedan
menos de 24 horas para radicar** (hoy 29-jul-2026, cierre 30-jul-2026 2:00 pm).
Esto no cambia el alcance ni el rigor exigido por `CLAUDE.md`, pero sí exige
priorizar el orden de trabajo: primero cerrar los bloqueantes de §9, luego avanzar
en paralelo la matriz de cumplimiento y la propuesta técnica (que no dependen de
esas respuestas en su mayoría), y dejar el costeo final para el último tramo una
vez fijados los supuestos de negocio.

## 5. Criterios de evaluación

| Criterio | Puntos | Foco |
|---|---|---|
| A. Enfoque técnico y metodológico | 20 (15 subcriterios A1-A15) | Arquitectura, RAG/KB, control de versiones, precisión, UX, multimedia |
| B. Enfoque de gestión | 15 | Equipo (5) + factibilidad del cronograma (10, el subcriterio individual más alto de todo el RFP) |
| C. Capacidades corporativas / experiencia | 20 | Años de experiencia, 2 proyectos de IA generativa, 2 de integración conversacional, 2 de despliegue multiusuario, experiencia evaluando LLMs |
| D. Seguridad y protección de datos | 15 | Arquitectura de seguridad, cifrado/retención, residencia de datos, garantía de no entrenamiento |
| E. Transferencia de conocimiento | 15 | Plan de transferencia, documentación/activos, capacitación, portabilidad, soporte 30 días, mecanismo de actualización sin desarrollo complejo |
| F. Costo | 15 | Menor costo total = 15 puntos, proporcional hacia arriba (fórmula no textual, ver Anexo 10.3) |
| **Total** | **100** | |

Nota: el subcriterio individual de mayor peso es **B2 — factibilidad del
cronograma (10 puntos)**. La estimación de horas y el cronograma deben ser
particularmente robustos y defendibles.

## 6. Estructura del formulario de costos (Anexo 11.3 del RFP, con la Enmienda del Q&A)

| Componente | Contenido | Base de cotización | ¿Entra al total evaluado? |
|---|---|---|---|
| 1. Implementación y desarrollo único | 11 subrenglones (diseño, desarrollo, integración WhatsApp, RAG/KB, KB, flujos, UX, reportes, seguridad, pruebas/piloto, implementación) | Costo único fijo | Sí |
| 2. Costos recurrentes de operación | Infraestructura, licencias, servicios | **Valor GLOBAL del periodo** (corregido por Aclaración P15 — el RFP original pedía por usuario/mes) | Sí |
| 3. Costos variables por consumo | Tokens, mensajes WhatsApp, imagen/video, almacenamiento, etc. | **Por usuario**, consolidado × 800 usuarios × volumen del escenario común (Aclaración P15, P61) | Sí |
| 4. Costo de transferencia | Documentación, manuales, capacitación, traspaso admin | Costo único fijo | Sí |
| 5. Impuestos | % y a qué rubros aplica | — | Sí (parte del total) |
| 6. Servicios opcionales | Hora adicional de desarrollo/soporte/funcionalidad | Tarifa por hora | **No** |
| 7. Mantenimiento post-traspaso | — | Informativo | **No** |

Conversión a COP con TRM = 3.350 **solo para efectos de evaluación económica**
(RFP p.35). Ningún rubro puede figurar en dos componentes a la vez (Aclaración
P16).

## 7. Contradicciones y precedencias

**C-01 — Volumen de usuarios y mensajes.** El borrador `Ámbito de Trabajo Oficial`
(23-jun-2026) declara 1.000 usuarios y ~16.000 mensajes salientes. El RFP oficial
(21-jul-2026), Anexo 11.1.2, ya corrige a 800 usuarios pero conserva por error la
cifra de "~16.000 mensajes salientes" (aritméticamente inconsistente: 16
msg/usuario × 800 = 12.800, no 16.000). La Aclaración P60 (con enmienda) resuelve
definitivamente: **800 usuarios, ~12.800 mensajes salientes programados** (16 por
usuario, distribución no uniforme); la cifra de 16.000 correspondía al supuesto
anterior de 1.000 usuarios. **Jerarquía aplicada:** Aclaración > RFP > borrador
previo. **Cifras vigentes usadas en todos los entregables: 800 usuarios, ~12.800
mensajes salientes, 14 consultas entrantes/usuario (rango 12-18) → ~11.200
consultas totales.**

**C-02 — Estructura del componente 2 de costos.** El texto original del Anexo 11.3
pedía expresar el costo operativo recurrente "por usuario y por mes, tomando como
base 800 usuarios". La Aclaración P15 (marcada expresamente "Sí, requiere
enmienda") corrige: el componente 2 se cotiza como **valor global** del periodo, y
es el componente 3 el que se expresa por usuario y se multiplica por 800. **Se
aplica la Aclaración** sobre el texto original del Anexo.

**C-03 — Vigencia de tarifas de proveedores dentro de la ventana del contrato.**
No es una contradicción documental sino un riesgo de costeo detectado (ver Q&A y
vigilancia propia de mercado): la tarifa introductoria de los modelos de lenguaje
de última generación vence antes de que el contrato probablemente inicie
operación, y Meta anuncia un cambio de cobro de mensajes de servicio de WhatsApp
a partir de octubre de 2026. **Se debe cotizar con las tarifas vigentes en el
momento de la ejecución, no con las promocionales de hoy** — ver
`wiki/costeo-ia-tokens.md`, que se actualizará con los precios verificados al
momento de construir el entregable 05.

Ninguna de estas contradicciones cambia el alcance en un sentido que requiera
detener el trabajo; C-01 y C-02 ya están resueltas por la jerarquía documental.

## 8. Supuestos declarados (pendientes de decisión de negocio, no de lectura documental)

Estos supuestos no son ambigüedades de lectura del RFP — son decisiones de
propuesta/precio que el RFP deja explícitamente abiertas al oferente. Se
construirán con la mejor práctica y se declararán por escrito en la propuesta,
pero **el usuario debe fijarlos** antes de cerrar el costeo (ver §9):

- Tasa de derivación al canal humano (consultas que el agente no resuelve).
- Arquitectura RAG vs. carga de KB completa (impacto de costo estimado
  marginal, decisión principalmente de riesgo/calidad de respuesta).
- Uso o no de "razonamiento extendido" del modelo.
- Margen comercial objetivo.
- Propuesta o no de pago anticipado (activa la póliza de buen manejo de
  anticipo al 100%, pero mejora el flujo de caja).
- ~~Tarifa de IVA aplicable a este objeto contractual~~ — **Resuelto
  (2026-07-29):** el usuario confirmó que el servicio de software en la nube no
  causa IVA. En su lugar, aplica retención en la fuente y de ICA sobre cada pago
  (tarifas exactas aún `[PENDIENTE]` de confirmar con contable — ver `06`, hoja
  "Retenciones").
- Factor de conversión horas↔días para la estimación (primera licitación de
  este agente; no hay precedente registrado en la wiki).

## 9. Ambigüedades y decisiones bloqueantes a consultar con el usuario

Ver mensaje de chat adjunto a este análisis — se agrupan y se presentan
directamente al usuario porque determinan cómo se arma el resto del expediente
(quién firma, qué modelo de costos se llena, cuáles certificaciones de experiencia
son válidas). Mientras se resuelven, se avanza en lo que no depende de ellas:
matriz de cumplimiento y borrador de propuesta técnica (Fase 2).
