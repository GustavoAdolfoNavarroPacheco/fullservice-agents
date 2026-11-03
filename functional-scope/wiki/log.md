# Bitácora

Registro cronológico. Formato: `## [YYYY-MM-DD] <tipo> | <descripción>` con tipo ∈ {setup, alcance, ajuste, lint}.

## [2026-10-29] setup | Creación del agente
Se crea el agente `functional-scope` a partir del *Manual maestro para el agente generador de alcances funcionales* (v1.0, octubre 2026), guardado en `recursos/`.
Se definen `CLAUDE.md` (rol, reglas duras, flujo de 8 etapas, estructura del documento, control de calidad), las plantillas obligatorias del manual (§5.1–5.3) más tres de trabajo
(matriz de información, registro de decisiones, control de calidad), y la carpeta `alcances/` por proyecto. Marca copiada de `contract-perfectionist/recursos/marca/`.

## [2026-10-29] ajuste | Plantilla Word y portada estándar
El usuario entrega `Plantilla Word - Campuslands.docx` y `Portada.docx` (portada de referencia del proyecto Girón v2.0) y pide mejorar distribución, espacios, tamaños de fuente y justificado antes de definirla como estándar, pudiendo aplicar APA.
Respuestas del usuario: (1) la plantilla es la compartida; (2) el repo es privado, **no** hace falta excluir `alcances/`; (3) la salida de este agente **no** alimenta por ahora a `quote-developer-v2` ni `contract-perfectionist`.
Hecho: `recursos/plantilla/` (plantilla y portada original), `scripts/alcance_docx.py` (estilos, portada, control documental, tabla de contenido, tablas APA, fichas funcionales),
`plantillas/Alcance Funcional - Plantilla.docx` y `plantillas/Alcance Funcional - Muestra de formato.docx`. Reglas visuales y portada documentadas en `CLAUDE.md`.
Cambios frente a la portada original: ámbar/azul sueltos → paleta del membrete (azul `#0D497B`, verde `#5DAC6D`); jerarquía de tamaños 27/16/12,5/11/8,5 pt en lugar de 18/13/13/11/9,5; datos de versión, fecha y clasificación pasan a tarjetas ordenadas;
espacios por estilo en vez de espaciados sueltos por párrafo; el estado del documento se añade a la portada (el manual exige que quede claro si es borrador).
Verificación: XML validado; Word por COM se colgó, así que con autorización del usuario se instaló LibreOffice (winget, v26.8.1) y se revisó a la vista cada página de plantilla y muestra (`scripts/previsualizar.py`).
Ajustes hechos tras verla: viñeta discreta «•» (numId 2 de la plantilla) en lugar de «●» grande, y anchos de columna de las tablas de control documental para que «[PENDIENTE DE VALIDACIÓN]» no se parta.
No verificado: la tabla de contenido ya poblada (requiere actualizar el campo en Word) ni cómo se ve en Word (render hecho con LibreOffice; las fuentes y saltos pueden variar mínimamente).

## [2026-10-29] ajuste | Ejemplo de diagnóstico
El usuario pega la descripción del alcance «Plataforma de Inteligencia Financiera y Optimización Operativa» v2.0 (junio 2026) para usarla **solo como ejemplo de diagnóstico, nunca como plantilla**, y adjunta además un PDF de Unidrogas (septiembre 2026) que resultó ser otro proyecto.
Contradicción mostrada al usuario (módulos, cifras, plazo e integraciones distintos); el usuario indicó usar el texto pegado y **olvidar el PDF**, que no se guardó en el repo.
Hecho: `wiki/ejemplos/diagnostico-plataforma-inteligencia-financiera.md` (inventario, matriz, 13 pendientes priorizados, primera respuesta y primer bloque de preguntas); regla 13 en `CLAUDE.md`.
Alcance del ejemplo: fuente única sin documento original ni cotización, por lo que ningún dato pasa de «CONFIRMADO por la fuente»; sin carpeta de proyecto en `alcances/`.

## [2026-10-29] alcance | Ejemplo de diagnóstico: respuestas del bloque 1
Respuestas del usuario: no hay versión posterior a la 2.0; no hay documentación ni acceso de prueba a Maía y Oracle; datos a leer/escribir desconocidos; integración por lote; ninguna alternativa si no es viable.
Registradas como DEC-001 a DEC-005 en `wiki/ejemplos/diagnostico-plataforma-inteligencia-financiera.md`. Cierra PEN-001; se añaden PEN-014 (datos de integración, BLOQUEANTE) y PEN-015 (carga por lote, IMPORTANTE).
Quedan 7 bloqueantes abiertos (PEN-002 a PEN-007 y PEN-014; PEN-002 y PEN-014 son de integraciones). Siguiente: bloque de reglas de negocio.

## [2026-10-29] alcance | Ejemplo de diagnóstico: bloque 2 sin información
El usuario responde «no sé» a las cinco preguntas de reglas de negocio (anomalías, fórmulas, mantenimiento, simulador, acciones tras una anomalía). Registrado como DEC-006; los datos quedan PENDIENTE, sin suposiciones.
Cambios: PEN-008 (mantenimiento) sube a BLOQUEANTE porque sin definirlo no se delimitan alcance ni soporte; nuevo PEN-016 (acciones tras anomalía). Ahora hay 8 bloqueantes abiertos.
Se añade al ejemplo una lista de validaciones por dueño (finanzas del cliente, áreas operativas, administradores de Maía/Oracle, líder técnico y comercial) para no seguir preguntando al usuario lo que no le corresponde. Siguiente: bloque de IA y usuarios.

## [2026-10-29] alcance | Ejemplo de diagnóstico: cierre de la entrevista
El usuario responde «no sé» también al bloque de IA y usuarios (DEC-007). PEN-010 (perfiles y permisos) sube a BLOQUEANTE por tratarse de información financiera.
Resumen: 1 pendiente cerrado, 9 bloqueantes y 6 importantes abiertos. Entrevista en pausa; siguiente paso, reunión con el cliente y los administradores de Maía y Oracle según la lista de validaciones. Documento: solo borrador.


## [2026-10-29] diagnóstico | Alcaldía de Girón — cobro persuasivo con IA (ICA)
El usuario adjunta `Propuesta_Alcaldia_Giron_Campuslands_VF.docx` (propuesta del 2026-10-28) sin instrucciones adicionales. Se abre `alcances/giron-cobro-persuasivo-ica/` y se ejecutan las etapas 1–3 del flujo.
Hecho: `fuentes/` (docx + texto extraído), `trabajo/01-inventario-fuentes.md`, `02-matriz-informacion.md` (49 hechos, 21 módulos MOD-01…21, 14 integraciones INT-01…14, 8 contradicciones CON-001…008), `03-pendientes.md` (25 pendientes) y `04-registro-decisiones.md` (vacío).
Estado de los datos: toda la información queda como PROPUESTO (F1): es una oferta de Campuslands sin firma de la Alcaldía, y las actas de la mesa técnica, la cotización y el requerimiento de la Alcaldía no se aportaron.
Pendientes: 13 BLOQUEANTES (versión vigente, consumos y volúmenes, universo de cartera, qué se entrega en enero, condiciones de inicio, aceptación, SLA/garantía, PI y opción de compra, datos personales, terceros y costos, integraciones sin evidencia, condiciones comerciales, roles y permisos), 11 IMPORTANTES y 1 EDITORIAL.
Hallazgos destacados: cifras de volumen eliminadas del texto («unos contribuyentes», «unos minutos»), diagrama de arquitectura ausente (marcador literal), fee completo desde enero con fases habilitadas hasta junio, «placa» sin sentido claro para ICA, y recaudo (F3) posterior a las campañas (F2).
Control de calidad: no ejecutado (no hay documento). Documento al cliente: **ninguno todavía**; solo borrador cuando se redacte. Siguiente: entrevista, bloque 1 (versión vigente y fuentes).

## [2026-10-29] alcance | Girón — respuestas del bloque 1
Respuestas del usuario: la propuesta del 2026-10-28 es la vigente (DEC-001); no hay por ahora actas de la mesa técnica, cotización ni requerimiento (DEC-002); el entregable es el alcance funcional para el cliente (DEC-003).
Cierra PEN-001; quedan 12 bloqueantes. El usuario añadió el pedido de «quitar eso de "versión" en el archivo»: ambiguo, se pidió aclaración antes de tocar nada. Siguiente: bloque de consumos, universo de cartera y qué se entrega en enero.

## [2026-10-29] alcance | Girón — bloque 2 sin información
El usuario responde «no sé» a consumos (DEC-004), universo de cartera (DEC-005) y qué opera el primer día de enero con el fee (DEC-006). Los tres datos quedan PENDIENTES, sin suposiciones; PEN-002, PEN-003 y PEN-004 siguen BLOQUEANTES y pasan a la lista de validaciones por responsable (comercial, líder técnico, Dirección de ICA).
Además pidió quitar las menciones de «versión» en los archivos de trabajo (DEC-007): aplicado en `trabajo/`, `wiki/index.md` y las entradas de Girón de esta bitácora; la fuente original y las entradas de otros proyectos no se tocaron.
Estado: 12 bloqueantes abiertos, solo borrador. Siguiente: bloque de integraciones y terceros (PEN-010, PEN-011) y de roles y permisos (PEN-013).

## [2026-10-29] alcance | Girón — bloque 3 y criterio «solo el archivo»
El usuario aclara que las respuestas «no sé» no deben importar: todo se construye **únicamente con la propuesta** y no se pregunta lo que no trae (DEC-008). Se mantiene la criticidad de los pendientes, pero su acción pasa a ser marcar `[PENDIENTE DE VALIDACIÓN]` en el borrador y validar con el responsable aparte.
Hecho: `trabajo/06-bloque-3-integraciones-terceros-usuarios.md` (borrador de la sección 6 —matriz de 14 integraciones, terceros y responsabilidades— y de la sección 4 —actores y permisos—, solo con datos de la propuesta); sección «Tratamiento de los pendientes» en `03-pendientes.md`.
Sin cambios en el conteo: 12 bloqueantes abiertos, solo borrador. Siguiente: etapa 5 (resumen de alcance y supuestos para confirmar) y redacción del borrador.

## [2026-10-29] entrega | Girón — borrador v0.1 del alcance funcional
Tras la orden «redactar», se genera `alcances/giron-cobro-persuasivo-ica/entrega/Alcance Funcional - Alcaldía de Girón - v0.1 - 2026-10-29.docx` (borrador) sobre la plantilla corporativa, con `trabajo/construir_borrador.py` y `trabajo/diagrama_arquitectura.py`.
Contenido: portada, control documental, las 16 secciones del manual §4 (fichas RF-001…RF-015, matriz de 14 integraciones, tareas y límites de IA, entregables, calendario, condiciones comerciales transcritas), anexos A–E y referencias. Todo con estado PROPUESTO (fuente única: la propuesta) y unas 119 marcas `[PENDIENTE DE VALIDACIÓN]` donde la propuesta no declara el dato; nada se inventó (DEC-008).
Diagrama de arquitectura: la propuesta no lo traía (marcador literal); se dibujó solo con su descripción y se rotula como PROPUESTO.
Control de calidad (`trabajo/05-control-calidad.md`): 4 de 9 puntos marcados; los demás pendientes por falta de cotización, SLA/garantía, criterios de aceptación medibles y contradicciones de la propuesta sin resolver. 12 bloqueantes abiertos: **solo borrador**.
Verificación visual con LibreOffice (45 páginas); la tabla de contenido hay que actualizarla en Word (clic derecho → Actualizar campo). Pendiente: pedir las revisiones técnica, comercial y jurídica y llevar la lista de validaciones a cada responsable.

## [2026-10-29] ajuste | Menos preguntas, nueva estructura del documento y portada
Instrucciones del usuario: (1) si se comparte un archivo, es todo lo que hay: **no se entrevista por bloques** ni se pregunta lo que el archivo no trae; (2) el documento va como portada (una hoja) · carta de presentación (una hoja) · tabla de contenido (una hoja) · contenido (sin límite) · apartado de firma con mejor diseño, con la firma de la derecha variable por proyecto;
(3) quitar de la portada, en documentos actuales y futuros, las tarjetas **Versión** y **Clasificación**.
Hecho: `CLAUDE.md` (instrucción maestra, reglas duras 5 y 10, flujo etapas 4–6, «Regla de preguntas», formato de la primera respuesta, estructura del documento, reglas visuales, firma); `wiki/manual-operativo.md`; `scripts/alcance_docx.py` (portada de 4 tarjetas, `carta_presentacion`, `firmas`; se eliminó `control_documental`); plantilla y muestra regeneradas.
El manual (§2 etapa 4, §10, §4 portada y control documental) queda sustituido en esos puntos por instrucción del usuario. Firma escaneada de la representante legal guardada en `recursos/marca/` y solo se inserta en documentos listos para firma.
Girón: borrador regenerado con la nueva estructura (44 páginas, sin control documental: la leyenda de estados pasó al resumen ejecutivo; carta de presentación basada en la de la propuesta; firma izquierda fija, derecha con los datos de la propuesta). Una captura del usuario muestra «veintitrés (23)» en la fecha de firma de la propuesta, frente al «(29)» del archivo leído: queda como contradicción abierta (CON-007) y el apartado de firma deja la fecha en blanco.

## [2026-10-29] ajuste | Segunda ronda de formato (portada, «borrador», carta, tabla de contenido, espacios)
Instrucciones del usuario, para el documento de Girón y para los alcances futuros: (1) quitar la tarjeta «Preparado para» de la portada; (2) quitar la tarjeta «Estado del documento»; (3) eliminar del documento toda referencia a «borrador»; (4) repartir mejor la carta de presentación, aprovechando la hoja; (5) generar la tabla de contenido ya hecha, no un campo por actualizar; (6) evitar siempre los espacios vacíos del contenido.
Hecho en `scripts/alcance_docx.py`: portada con dos tarjetas; carta con estilos propios (11 pt, interlineado 1,25), lista de contenido y espacio de firma; tabla de contenido generada al guardar (títulos 1 y 2, sin «Anexo X») con números de página de LibreOffice y campo TOC de Word; sin saltos de página forzados entre secciones; fichas funcionales que fluyen entre páginas con el encabezado repetido (se corrigió que el estilo «Tabla Encabezado» las encadenaba enteras); bloque de firma que no se parte y no fuerza página; `previsualizar.py` ahora avisa de páginas con menos de 60 % de ocupación.
Reglas incorporadas a `CLAUDE.md` y `wiki/manual-operativo.md`. Plantilla y muestra regeneradas. Girón: 38 páginas (antes 44), sin la palabra «borrador» (el entregable «Borrador de política institucional de IA» de la propuesta pasó a «Propuesta de política institucional de IA»); la leyenda de estados y las notas pasaron a lenguaje de documento final con pendientes marcados.
Sigue habiendo 12 bloqueantes: el estado Borrador se mantiene en `wiki/index.md` y `05-control-calidad.md`. Única página con hueco: la 37, antes de la hoja de firma.

## [2026-10-29] ajuste | Girón: sin marcas de pendiente en los criterios de aceptación
El usuario pidió quitar los `[PENDIENTE DE VALIDACIÓN]` de los criterios de aceptación medibles, porque la propuesta ya dice que se definen en el levantamiento de la Fase 1. Aplicado en las 15 fichas, la introducción de la sección 5 y de la sección 10, la tabla de entregables y la nota del plan de pruebas: ahora dicen «se definen en el levantamiento de la Fase 1 (RF-001)». Marcas del documento: de 110 a 90.
Se mantienen otras marcas cercanas que no son criterios de aceptación (si la aceptación condiciona el pago, indicadores de seguimiento, prioridad de requisitos, criterios de clasificación EMPLAZAR). Regla incorporada a `CLAUDE.md` (regla dura 11).

## [2026-10-29] transcripción | alcaldia-giron-cpi (fuera del flujo de alcances)
El usuario pidió una transcripción **solo visual y estructural** del archivo `Propuesta_Alcaldia_Giron_Campuslands_VF.docx` a la estructura estándar (portada, carta, tabla de contenido, contenido, firma), sin cambiar ni una letra del texto salvo el título («PROPUESTA COMERCIAL Y TÉCNICA» → «Alcances Tecnicos y Propuestas Comerciales»), y completar la cláusula de costos: «Los costos del proyecto que no estén contemplados en las primeras fases, pero estén directamente relacionados con la prestación del servicio, serán asumidos por la entidad.» (agregada al final de 9.4).
Hecho en `alcances/alcaldia-giron-cpi/` (`fuentes/`, `trabajo/transcribir.py`, `extraer.py`, `verificar.py`, `entrega/`): 28 páginas; `verificar.py` confirma las 613 líneas de texto idénticas a la fuente (salvo título, cláusula y tabla de contenido). Se conservan tal cual los defectos del original (erratas «Telynx», «Implementacion», «sistema operativo», «&#32;», «&#91;embedded content…\]»), la línea «Versión 2.0 | 28 de octubre de 2026» de la portada y la firma escaneada.
Cambios en `scripts/alcance_docx.py` (no alteran los documentos anteriores): tablas sin título cuando `titulo=None`, celdas con varios párrafos, modo de texto literal (`resaltar=False`), `firmas_lineas` (firma sin etiquetas añadidas) y tabla de contenido con letra mayor si tiene 42 entradas o menos.
Excepción a las reglas de este agente por indicación expresa del usuario («aunque se salga de tus funciones»): no se aplicó el flujo de diagnóstico, la regla de no versión en portada ni las marcas de pendiente.

## [2026-10-29] ajuste | Sin hoja final vacía
El usuario reportó una última hoja vacía. Causa probable: el párrafo obligatorio que Word exige tras la última tabla (de 9 pt con 12 pt de espacio) se desbordaba a una hoja nueva. `scripts/alcance_docx.py` ahora cierra los apartados de firma con un párrafo de 1 pt sin espacios (`_cierre_minimo`). Regenerados `alcaldia-giron-cpi` (28 páginas, texto verificado idéntico) y el alcance funcional de Girón (38 páginas). En LibreOffice la última página de ambos es la de firma; no se pudo comprobar en Word.

## [2026-10-29] ajuste | alcaldia-giron-cpi: sin «Versión 2.0» en la portada
El usuario pidió eliminar «Versión 2.0» de la portada. Se quitó el prefijo «Versión 2.0 | » y quedó solo la fecha «28 de octubre de 2026»; `verificar.py` registra esta diferencia como permitida. El resto del texto sigue idéntico a la fuente.
