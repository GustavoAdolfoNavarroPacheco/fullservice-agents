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

