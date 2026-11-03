# Ejemplo de diagnóstico — Plataforma de Inteligencia Financiera y Optimización Operativa (v2.0, junio 2026)

> ⛔ **Solo ejemplo de método.** Muestra cómo se hace un diagnóstico (etapas 1–3 del flujo y primera respuesta del manual §10). **Nunca es plantilla universal:** no se copian de aquí módulos,
> integraciones, cifras, plazos ni condiciones a otro proyecto. Los datos pertenecen exclusivamente a este caso y deben validarse frente a cualquier versión posterior.

**Fuente única:** descripción del alcance v2.0 (junio de 2026) que el usuario pegó el 2026-10-29. No se dispone del documento original, de la cotización ni de la propuesta comercial. Cliente: no indicado en la fuente.

## 1. Inventario de fuentes (etapa 1)

| # | Fuente | Versión / fecha | Estado |
|---|---|---|---|
| F1 | Descripción del alcance «Plataforma de Inteligencia Financiera y Optimización Operativa» (texto del usuario) | 2.0 · junio de 2026 | **Vigente**: el usuario confirmó el 2026-10-29 que no existe versión posterior (DEC-001) |
| F3 | Respuestas del usuario en la entrevista, bloque 1 | 2026-10-29 | Registradas en el §4 |
| F2 | Cotización / propuesta comercial | — | **No aportada** |

## 2. Matriz de información (etapa 2)

| # | Bloque | Dato declarado | Fuente | Estado |
|---|---|---|---|---|
| 1 | Alcance | Diez módulos | F1 | CONFIRMADO (por F1) — los diez **no están enumerados** |
| 2 | Alcance | Capacidades nombradas: integraciones con Maía y Oracle, OCR, dashboards, IA conversacional, arriendos, simulación, análisis de mercado | F1 | CONFIRMADO (por F1) — siete temas, sin detallar |
| 3 | Comercial | COP 88.000.000 | F1 | CONFIRMADO (por F1) — sin IVA, hitos ni forma de pago |
| 4 | Proyecto | 3,5 meses de desarrollo **más** pruebas | F1 | CONFIRMADO (por F1) — duración de pruebas no declarada |
| 5 | Operación | Un mes de soporte correctivo | F1 | CONFIRMADO (por F1) — inicio y exclusiones no declarados |
| 6 | Datos e integraciones | La versión 2.0 es la vigente; no hay versión posterior | F3 | CONFIRMADO (usuario, 2026-10-29) |
| 7 | Datos e integraciones | No hay documentación ni acceso de prueba a Maía y Oracle | F3 | CONFIRMADO (usuario). Responsables de cada sistema: no indicados |
| 8 | Datos e integraciones | Frecuencia de las integraciones: por **lote** | F3 | CONFIRMADO (usuario). Periodicidad, ventana y volumen: no indicados |
| 9 | Datos e integraciones | **No se acepta alternativa** si una integración no es viable (ej. carga de archivos) | F3 | CONFIRMADO (usuario) |
| 10 | Datos e integraciones | Datos a leer y escribir en Maía y Oracle | F3 | **PENDIENTE** — el usuario no lo sabe |
| 11 | Reglas de negocio | Criterios de anomalías, fórmulas financieras, alcance de «mantenimiento», variables del simulador y acciones tras una anomalía | F3 | **PENDIENTE** — el usuario no lo sabe (bloque 2 completo) |
| 12 | IA y usuarios | Perfiles de usuario, fuentes de la IA conversacional, quién valida sus recomendaciones y qué nunca debe recomendar o ejecutar | F3 | **PENDIENTE** — el usuario no lo sabe (bloque 3 completo) |

«CONFIRMADO (por F1)» = respaldado por la fuente, **no** aprobado por el cliente. Sin contradicciones internas detectadas. Respuestas de los bloques 1 a 3 incorporadas en las filas 6–12.

## 3. Pendientes priorizados (etapa 3)

| ID | Criticidad | Tema | Riesgo o dato faltante | Impacto | Responsable | Acción / decisión |
|---|---|---|---|---|---|---|
| PEN-001 | ~~BLOQUEANTE~~ **CERRADO** | Versión vigente | Resuelto: la v2.0 es la vigente (DEC-001) | — | Usuario | — |
| PEN-002 | BLOQUEANTE | Integraciones | Maía y Oracle sin documentación ni acceso de prueba (DEC-002); campos a leer/escribir desconocidos (PEN-014); autenticación y propietarios sin definir; **sin alternativa aceptada** si no son viables (DEC-004) | Viabilidad, plazo, costo, cumplimiento del alcance | Cliente + técnico | PROPUESTO: prueba de acceso a ambos sistemas **antes** de comprometer el alcance, como condición de inicio |
| PEN-003 | BLOQUEANTE | Alcance vs. esfuerzo | Diez módulos no enumerados frente a 3,5 meses y COP 88.000.000 | Plazo, costo | Líder técnico + comercial | Listar módulos y contrastar con la estimación y la propuesta |
| PEN-004 | BLOQUEANTE | Reglas de negocio | Criterios de anomalías y fórmulas financieras sin definir; el usuario no los conoce (DEC-006) | Aceptación | **Cliente (finanzas)**: no responde el usuario | Definir umbrales, fórmulas y ejemplos con quien las usa hoy |
| PEN-005 | BLOQUEANTE | IA conversacional | Fuentes autorizadas, supervisión humana, trazabilidad y límites de las recomendaciones sin definir; el usuario no los conoce (DEC-007) | Responsabilidades | Cliente + técnico | Definir fuentes, validación y qué **no** recomienda |
| PEN-006 | BLOQUEANTE | Aceptación | Entregables y criterios de aceptación no declarados | Aceptación | Usuario + cliente | Matriz de entregables por fase |
| PEN-007 | BLOQUEANTE | Costos y titularidad | Costos de terceros (licencias de Maía/Oracle, OCR, consumo de IA) y propiedad del código no declarados | Costo, responsabilidades | Comercial + jurídico | Confirmar y marcar recurrentes |
| PEN-008 | **BLOQUEANTE** (sube de IMPORTANTE) | Mantenimiento | No se sabe qué cubre el «mantenimiento» (DEC-006): sin definirlo no se puede delimitar alcance, costo ni soporte, ni separar errores de solicitudes nuevas | Alcance, costo, operación | Usuario + comercial | Precisar cobertura y exclusiones |
| PEN-009 | IMPORTANTE | Simulador | Variables, escenarios y salidas; el usuario no los conoce (DEC-006) | Alcance | Cliente | Definir con ejemplos |
| PEN-010 | **BLOQUEANTE** (sube de IMPORTANTE) | Usuarios | Perfiles, datos y acciones por perfil sin definir (DEC-007); la plataforma maneja información financiera y sin permisos no se puede definir privacidad ni visibilidad | Seguridad, privacidad, alcance | Cliente (patrocinador) | Matriz de permisos |
| PEN-011 | IMPORTANTE | OCR | Tipos de documento, volumen y campos a extraer; sin promesa de exactitud | Alcance | Cliente | Muestra de documentos |
| PEN-012 | IMPORTANTE | Análisis de mercado y arriendos | Fuentes de datos y procesos cubiertos | Alcance, costo | Cliente | Definir fuentes y límites |
| PEN-013 | IMPORTANTE | Cronograma y pagos | Fases, hitos, duración de pruebas e hitos de pago | Plazo | Usuario | Confirmar |
| PEN-014 | BLOQUEANTE | Datos de integración | Qué datos se leen y cuáles se escriben en Maía y Oracle: el usuario no lo sabe (DEC-003) | Viabilidad, alcance, costo | Cliente + técnico | Levantar campos o tablas con el administrador de cada sistema |
| PEN-016 | IMPORTANTE | Anomalías | Qué ocurre al detectar una anomalía (notificar, bloquear, pedir aprobación humana) (DEC-006) | Alcance, responsabilidades | Cliente | Definir flujo y responsable |
| PEN-015 | IMPORTANTE | Carga por lote | Periodicidad, ventana horaria, volumen por lote y manejo de errores (DEC-005) | Plazo, operación | Cliente + técnico | Definir con el administrador de cada sistema |

## 4. Primera respuesta (manual §10) y primer bloque de preguntas

> He revisado la información disponible del proyecto. Identifiqué 10 módulos y 5 datos declarados en la fuente. Antes de estructurar el alcance necesito resolver 7 puntos críticos (estado actual: 7 bloqueantes abiertos, ver §3).
> Empecemos por **integraciones y versión vigente**: (1) ¿Existe una versión posterior a la 2.0? (2) ¿Hay documentación o acceso de prueba a Maía y a Oracle, y quién administra cada una?
> (3) ¿Qué datos se leen y cuáles se escriben (campos o tablas)? (4) ¿Qué volumen y frecuencia (lote o tiempo real) se esperan? (5) Si una integración no resulta viable, ¿qué alternativa se acepta dentro del alcance (por ejemplo, carga de archivos)?

Orden de los siguientes bloques, según las pautas del usuario: reglas de negocio (anomalías, fórmulas, simulador) → IA (perfiles, fuentes, validación, límites) → verificación de los diez módulos frente al esfuerzo y la propuesta → entregables, aceptación, costos externos y propiedad del código.

## 5. Registro de decisiones y respuestas (etapa 4)

| ID | Fecha | Bloque | Decisión o respuesta | Quién | Afecta a |
|---|---|---|---|---|---|
| DEC-001 | 2026-10-29 | Versión | No existe versión posterior a la 2.0; es la vigente | Usuario | Todo el alcance |
| DEC-002 | 2026-10-29 | Integraciones | No hay documentación ni acceso de prueba a Maía y Oracle | Usuario | PEN-002 |
| DEC-003 | 2026-10-29 | Integraciones | Datos a leer y escribir: se desconocen («no sé») | Usuario | PEN-014 |
| DEC-004 | 2026-10-29 | Integraciones | Ninguna alternativa aceptada si la integración no es viable | Usuario | PEN-002 |
| DEC-005 | 2026-10-29 | Integraciones | Frecuencia de integración: por lote | Usuario | PEN-015 |

**Lectura del agente (PROPUESTO, no decidido):** sin acceso de prueba, sin campos conocidos y sin alternativa aceptada, el alcance depende por completo de dos sistemas que nadie ha probado.
Si alguna integración falla, no hay ruta de salida dentro del alcance. Conviene que el equipo técnico y comercial decida si se exige una prueba de acceso antes de firmar y qué pasa con el precio y el plazo si no resulta viable.

| DEC-006 | 2026-10-29 | Reglas de negocio | El usuario no conoce los criterios de anomalías, las fórmulas financieras, el alcance de «mantenimiento», las variables del simulador ni las acciones tras una anomalía | Usuario | PEN-004, PEN-008, PEN-009, PEN-016 |

### Lista de validaciones para el cliente (en lugar de seguir preguntando al usuario)
Cinco bloques seguidos sin dato indican que la información no está en manos del usuario. Se agrupa lo que debe responder **el cliente o el equipo técnico**, con su dueño, para una sola reunión:

| Dueño | Qué debe aportar | Pendientes |
|---|---|---|
| Finanzas del cliente | Qué es una anomalía (umbrales, comparación con histórico), fórmulas que debe calcular la plataforma, quién las valida, y qué pasa al detectar una | PEN-004, PEN-016 |
| Áreas operativas del cliente | Qué significa «mantenimiento» en su proceso; variables y resultados del simulador | PEN-008, PEN-009 |
| Administradores de Maía y Oracle | Documentación, acceso de prueba, campos o tablas a leer y escribir, autenticación, periodicidad y volumen por lote | PEN-002, PEN-014, PEN-015 |
| Líder técnico + comercial de Campuslands | Enumerar los diez módulos y contrastarlos con 3,5 meses y COP 88.000.000; decidir si se exige prueba de acceso antes de comprometer el alcance | PEN-003, PEN-002 |

**Estado del documento si se redactara hoy:** solo **borrador**, con las secciones afectadas marcadas `[PENDIENTE DE VALIDACIÓN]`. No puede declararse apto para revisión final con 8 bloqueantes abiertos.

| DEC-007 | 2026-10-29 | IA y usuarios | El usuario no conoce los perfiles de usuario, las fuentes de la IA, quién valida sus recomendaciones ni sus límites | Usuario | PEN-005, PEN-010 |

Se añade a la lista anterior un dueño más: **patrocinador del cliente** → perfiles y permisos (PEN-010), fuentes de la IA, quién valida sus recomendaciones y qué nunca debe recomendar o ejecutar (PEN-005).

## 6. Resumen de pendientes (cierre de la entrevista)

La entrevista queda **en pausa**: el usuario no tiene la información de los bloques 2 y 3, y seguir preguntándole no la produce. El siguiente paso es la reunión con el cliente y los administradores de Maía y Oracle.

| | Cantidad | Pendientes |
|---|---|---|
| Cerrados | 1 | PEN-001 |
| **Bloqueantes abiertos** | **9** | PEN-002, 003, 004, 005, 006, 007, 008, 010, 014 |
| Importantes abiertos | 6 | PEN-009, 011, 012, 013, 015, 016 |
| Editoriales | 0 | — |

**Estado del documento:** solo **borrador**. Para pasar a «apto para revisión final» hay que resolver al menos los nueve bloqueantes. Revisiones aún sin solicitar: técnica (integraciones y esfuerzo), comercial (precio y plazo vs. los diez módulos) y jurídica (propiedad del código, costos de terceros, tratamiento de datos financieros).

## 7. Qué enseña este ejemplo (y qué no)
- Una fuente con datos declarados **sin documento original** da estado «CONFIRMADO por la fuente», nunca «aprobado».
- Se pregunta primero lo que desbloquea viabilidad (integraciones) y la versión vigente.
- Se señala lo que **no** está: aquí, los diez módulos sin enumerar y la ausencia de criterios de aceptación.
- Cuando el usuario no tiene la información, el agente deja de preguntarle, entrega la lista de validaciones por dueño y no avanza más allá del borrador.
- Un «no sé» se registra como PENDIENTE con su dueño, no se rellena con una suposición.
- Una respuesta que cierra una salida («ninguna alternativa») se convierte en riesgo explícito, sin suavizarla.
- No se transfiere nada de este caso a otro proyecto.
