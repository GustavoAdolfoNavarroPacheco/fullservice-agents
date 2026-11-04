# Comandos `!` de los agentes

Catálogo único. **Generado** por `resources/comandos/comandos.py`: no se edita a mano (edita el script y vuelve a correrlo).

## Regla común

1. Un **comando** es una orden corta del usuario: una palabra precedida de `!` al inicio de un mensaje o de una línea (`!optimize`). El texto que sigue es su objeto (`!optimize el PDF de alcance`); sin texto, actúa sobre el trabajo en curso.
2. **Es obligatorio.** Cuando reconozco un comando lo ejecuto: no pido permiso, no lo reinterpreto ni lo sustituyo por algo más cómodo. Lo único que puede limitarlo es una **regla dura** de este agente (veracidad, marca, confidencialidad, puertas de aprobación o de verificación): entonces hago todo lo que la regla permite y digo en una frase qué no pude y por qué. Un comando nunca autoriza a inventar datos ni a saltarse una verificación obligatoria.
3. **Se combinan** (`!plan !no-assumptions`): se cumplen todos. Los de **modo** (`!notime`, `!think-deep`, `!critical-mode`, `!no-assumptions`, `!strict-mode`, `!double-check`) cambian *cómo* trabajo; los de **acción** (`!plan`, `!audit`, `!final-delivery`…) definen *qué* produzco. Si dos modos chocan, el orden de prioridad es: reglas duras > `!strict-mode` y `!no-assumptions` > `!think-deep`, `!critical-mode` y `!double-check` > `!notime`.
4. **Vigencia:** el comando rige la tarea en curso hasta entregarla; no pasa a tareas nuevas (si se quiere, se repite).
5. **Confirmación:** la primera línea de mi respuesta nombra los comandos recibidos (`Comandos: !optimize, !notime`) y, en una frase, cómo los aplico.
6. **Comando desconocido o que no aplica aquí:** no lo adivino. Si empieza con `!` y no está en la tabla, lo digo, propongo los más parecidos y pregunto. Si es de otro agente o no tiene sentido aquí, lo digo y sugiero el equivalente. `!help` lista los comandos disponibles.
7. **Registro:** si un comando cambió un entregable o la wiki, lo anoto en `wiki/log.md` junto con la acción.

## Matriz: qué comando tiene cada agente

| Comando | Grupo | `prospection-agent` | `intelligence-commercial` | `presentations-designer` | `functional-scope` | `quote-developer` | `bidding-agent` | `contract-perfectionist` |
|---|---|---|---|---|---|---|---|---|
| `!analyze` | General | ● | ● | ● | ● | ● | ● | ● |
| `!research` | General | ● | ● | ● | ● | ● | ● | ● |
| `!plan` | General | ● | ● | ● | ● | ● | ● | ● |
| `!execute` | General | ● | ● | ● | ● | ● | ● | ● |
| `!review` | General | ● | ● | ● | ● | ● | ● | ● |
| `!audit` | General | ● | ● | ● | ● | ● | ● | ● |
| `!validate` | General | ● | ● | ● | ● | ● | ● | ● |
| `!optimize` | General | ● | ● | ● | ● | ● | ● | ● |
| `!compare` | General | ● | ● | ● | ● | ● | ● | ● |
| `!summarize` | General | ● | ● | ● | ● | ● | ● | ● |
| `!document` | General | ● | ● | ● | ● | ● | ● | ● |
| `!prioritize` | General | ● | ● | ● | ● | ● | ● | ● |
| `!help` | General | ● | ● | ● | ● | ● | ● | ● |
| `!notime` | Modos | ● | ● | ● | ● | ● | ● | ● |
| `!think-deep` | Modos | ● | ● | ● | ● | ● | ● | ● |
| `!critical-mode` | Modos | ● | ● | ● | ● | ● | ● | ● |
| `!no-assumptions` | Modos | ● | ● | ● | ● | ● | ● | ● |
| `!double-check` | Modos | ● | ● | ● | ● | ● | ● | ● |
| `!strict-mode` | Modos | ● | ● | ● | ● | ● | ● | ● |
| `!debug` | Técnico y seguridad | · | · | ● | ● | ● | ● | ● |
| `!troubleshoot` | Técnico y seguridad | ● | ● | ● | ● | ● | ● | ● |
| `!security-check` | Técnico y seguridad | ● | ● | ● | ● | ● | ● | ● |
| `!implement` | Técnico y seguridad | · | · | ● | · | · | · | · |
| `!refactor` | Técnico y seguridad | · | · | ● | · | · | · | · |
| `!code-review` | Técnico y seguridad | · | · | ● | · | · | · | · |
| `!performance` | Técnico y seguridad | · | · | ● | · | · | · | · |
| `!deploy-check` | Técnico y seguridad | · | · | ● | · | · | · | · |
| `!rollback` | Técnico y seguridad | · | · | ● | · | · | · | · |
| `!architecture` | Técnico y seguridad | · | · | · | · | · | ● | · |
| `!ui-review` | UX/UI y diseño | · | · | ● | · | · | · | · |
| `!ux-review` | UX/UI y diseño | · | · | ● | · | · | · | · |
| `!redesign` | UX/UI y diseño | · | · | ● | · | · | · | · |
| `!design-system` | UX/UI y diseño | · | · | ● | · | · | · | · |
| `!visual-audit` | UX/UI y diseño | · | · | ● | ● | ● | ● | ● |
| `!responsive-check` | UX/UI y diseño | · | · | ● | · | · | · | · |
| `!accessibility` | UX/UI y diseño | · | · | ● | · | · | · | · |
| `!microinteractions` | UX/UI y diseño | · | · | ● | · | · | · | · |
| `!consistency-check` | UX/UI y diseño | ● | ● | ● | ● | ● | ● | ● |
| `!componentize` | UX/UI y diseño | · | · | ● | · | · | · | · |
| `!breakdown` | Gestión de proyecto | · | · | ● | ● | ● | ● | ● |
| `!roadmap` | Gestión de proyecto | · | · | · | · | · | ● | · |
| `!estimate` | Gestión de proyecto | · | · | · | · | ● | ● | · |
| `!track-progress` | Gestión de proyecto | ● | ● | ● | ● | ● | ● | ● |
| `!risk-analysis` | Gestión de proyecto | · | · | · | ● | ● | ● | ● |
| `!requirements` | Gestión de proyecto | · | · | ● | ● | ● | ● | ● |
| `!generate-report` | Gestión de proyecto | ● | ● | ● | ● | ● | ● | ● |
| `!final-delivery` | Gestión de proyecto | ● | ● | ● | ● | ● | ● | ● |
| `!agent-handoff` | Gestión de proyecto | ● | ● | ● | ● | ● | ● | ● |
| `!second-opinion` | IA avanzada | · | · | ● | ● | ● | ● | ● |
| `!cross-review` | IA avanzada | · | · | ● | ● | ● | ● | ● |
| `!orchestrate` | Multiagente | · | · | ● | ● | ● | ● | ● |
| `!team-review` | Multiagente | · | · | ● | ● | ● | ● | ● |
| `!consensus` | Multiagente | · | · | ● | ● | ● | ● | ● |

● = disponible · = no aplica a ese agente.

## Definiciones


### General

| Comando | Qué hace |
|---|---|
| `!analyze` | Analiza la solicitud, el problema, los documentos o la situación **antes de actuar**: qué se pide, qué hay, qué falta y qué riesgos ve. Entrega hallazgos; no ejecuta ni modifica nada. |
| `!research` | Investiga a fondo el tema, cruza fuentes y entrega lo relevante con **cada dato citado a su fuente**. Sin fuente verificable no es un dato: se marca `[PENDIENTE]`. |
| `!plan` | Entrega un plan de trabajo estructurado (pasos, orden, insumos, entregables, supuestos y puntos de decisión) y **se detiene a esperar aprobación** antes de ejecutarlo. |
| `!execute` | Ejecuta ya lo solicitado o el siguiente paso aprobado del flujo, sin volver a proponer ni a preguntar lo ya decidido. No se salta las puertas de aprobación ni de verificación. |
| `!review` | Revisa el trabajo indicado y entrega oportunidades de mejora priorizadas (qué cambiaría y por qué). No lo modifica salvo que se le pida. |
| `!audit` | Auditoría integral de punta a punta: contradicciones entre documentos, cifras que no cuadran, reglas incumplidas y datos sin fuente. Entrega hallazgos con evidencia y severidad. |
| `!validate` | Comprueba, requisito por requisito, que el resultado cumple lo establecido (reglas duras, insumos, formato). Veredicto «cumple / no cumple» por ítem, con evidencia. |
| `!optimize` | Optimiza lo que se esté desarrollando o ya existe (proceso, solución o resultado): mejora claridad, calidad, consistencia, peso o rendimiento **sin cambiar su alcance ni sus datos**. |
| `!compare` | Compara alternativas con criterios explícitos y recomienda la más conveniente, con el porqué. |
| `!summarize` | Resumen claro y estructurado (lo esencial, decisiones y pendientes) del trabajo, de un documento o de la conversación. |
| `!document` | Documenta lo hecho: actualiza la wiki y la bitácora del agente, o genera la documentación técnica, funcional o ejecutiva que se pida. |
| `!prioritize` | Clasifica actividades, hallazgos o elementos por impacto, importancia y urgencia, y entrega el orden recomendado. |
| `!help` | Lista los comandos disponibles en este agente, agrupados, con su función. |

### Modos

| Comando | Qué hace |
|---|---|
| `!notime` | **Modo prisa:** apresura el desarrollo optimizándolo: agrupa preguntas en un solo mensaje, paraleliza, reutiliza lo ya validado, omite explicaciones y pasos opcionales y responde solo con lo esencial. **Nunca** se salta verificaciones obligatorias, puertas de aprobación ni la veracidad: acelera el camino, no recorta la calidad. |
| `!think-deep` | Análisis más profundo antes de responder: considera alternativas, casos límite y consecuencias, y muestra solo el razonamiento que importa. |
| `!critical-mode` | Modo crítico: cuestiona decisiones, supuestos y su propio trabajo; busca errores y contradicciones antes de entregar y los dice. |
| `!no-assumptions` | No supone: ante un dato faltante o ambiguo pregunta (todas las dudas juntas) en lugar de rellenar o inferir. |
| `!double-check` | Segunda verificación independiente de su propio resultado (releer la fuente, recalcular, comparar) y corrección de lo que encuentre; reporta qué verificó. |
| `!strict-mode` | Sigue al pie de la letra los requisitos e instrucciones dados: sin iniciativas, adiciones ni interpretaciones creativas. |

### Técnico y seguridad

| Comando | Qué hace |
|---|---|
| `!debug` | Identifica la causa de un error de software (script, conversión, verificación) y lo corrige; vuelve a correr la verificación para comprobarlo. |
| `!troubleshoot` | Investiga un problema técnico y determina su **causa raíz**, con evidencia. Diagnostica; no cambia nada. |
| `!security-check` | Revisa seguridad y confidencialidad: datos de otros clientes mezclados, credenciales, datos personales, información que no debe salir del proyecto. |
| `!implement` | Desarrolla la funcionalidad o solución solicitada (código, plantilla, script). |
| `!refactor` | Mejora la estructura del código sin alterar su comportamiento esperado; lo demuestra con la verificación antes y después. |
| `!code-review` | Evalúa calidad, organización y mantenibilidad del código; entrega observaciones priorizadas. |
| `!performance` | Analiza y optimiza el rendimiento: tiempos de carga, peso de archivos, fluidez. |
| `!deploy-check` | Verifica que el proyecto esté listo para publicarse: requisitos, exportación y enlaces comprobados. |
| `!rollback` | Gestiona la reversión controlada de cambios a un estado anterior conocido, sin perder lo nuevo (queda respaldado). |
| `!architecture` | Diseña o evalúa la arquitectura de una solución de software. |

### UX/UI y diseño

| Comando | Qué hace |
|---|---|
| `!ui-review` | Audita visualmente una interfaz y detecta problemas de diseño. |
| `!ux-review` | Evalúa la experiencia de usuario y los flujos de navegación. |
| `!redesign` | Propone y desarrolla un rediseño visual, dentro de las reglas de marca. |
| `!design-system` | Construye, documenta o estandariza el sistema de diseño. |
| `!visual-audit` | Examina proporciones, distribución, tipografía y consistencia visual del entregable, a la vista y página por página. |
| `!responsive-check` | Evalúa cómo se adapta la interfaz a distintos tamaños y dispositivos. |
| `!accessibility` | Evalúa y mejora la accesibilidad: contraste, tamaños, teclado, textos alternativos. |
| `!microinteractions` | Diseña o implementa microinteracciones y animaciones sutiles, sin romper las reglas de marca. |
| `!consistency-check` | Detecta inconsistencias entre secciones, componentes, cifras, nombres y estilos del mismo entregable. |
| `!componentize` | Identifica elementos repetidos y los convierte en componentes reutilizables. |

### Gestión de proyecto

| Comando | Qué hace |
|---|---|
| `!breakdown` | Divide un proyecto o solicitud compleja en actividades específicas, cada una con su entregable y su orden. |
| `!roadmap` | Construye una hoja de ruta de desarrollo con hitos y dependencias. |
| `!estimate` | Estima tiempos, recursos y complejidad, con el método y los supuestos escritos (un número sin método no se entrega). |
| `!track-progress` | Informa el progreso y los pendientes (hecho, en curso, bloqueado, `[PENDIENTE]`) a partir de la bitácora y del trabajo actual. |
| `!risk-analysis` | Identifica riesgos, su probabilidad e impacto, y propone la mitigación de cada uno. |
| `!requirements` | Extrae y estructura requerimientos funcionales y no funcionales de las fuentes, cada uno con su referencia de origen. |
| `!generate-report` | Genera un informe ejecutivo (decisiones, resultado, pendientes) o técnico (método, evidencias, verificaciones) del trabajo. |
| `!final-delivery` | Prepara y valida la entrega final: corre todas las verificaciones obligatorias, completa el checklist de cierre (wiki y bitácora) y entrega solo si todo pasa. |
| `!agent-handoff` | Prepara el traspaso al siguiente agente del flujo comercial: resumen, entregables con su ruta, decisiones tomadas y pendientes. |

### IA avanzada

| Comando | Qué hace |
|---|---|
| `!second-opinion` | Un subagente independiente evalúa el resultado **sin ver tu razonamiento**; se contrasta con el tuyo y se explican las diferencias. |
| `!cross-review` | Otro especialista (subagente con otro rol) revisa el resultado y devuelve observaciones; se aplican las válidas y se informa de las descartadas. |

### Multiagente

| Comando | Qué hace |
|---|---|
| `!orchestrate` | Reparte partes **independientes** del trabajo entre varios subagentes en paralelo y las integra en un solo resultado verificado. |
| `!team-review` | Varios revisores con roles distintos evalúan por separado el mismo resultado y se consolida su evaluación. |
| `!consensus` | Consolida las evaluaciones disponibles (de subagentes o de revisiones previas) en una sola recomendación, con las discrepancias a la vista. |

## Alias (se aceptan y se tratan como otro comando)

| Alias | Equivale a | Matiz |
|---|---|---|
| `!self-correct` | `!double-check` | revisa su propia respuesta, corrige y dice qué cambió |
| `!deep-dive` | `!think-deep` | sobre el tema indicado, con `!research` si hacen falta fuentes |
| `!delegate` | `!orchestrate` | reparte las actividades entre subagentes |
| `!technical-board` | `!team-review` | con revisores técnicos |
| `!design-board` | `!team-review` | con revisores de diseño y marca |
| `!supervisor` | `!audit` | supervisión integral del trabajo |
| `!create-task` | `!breakdown` | cada actividad como tarea con objetivo y entregable |

## Sin función (no se implementan)

| Comando | Motivo |
|---|---|
| `!expert-mode` | Cada agente ya es un especialista con su rol, reglas y wiki; no hay un «modo experto» que activar. |
| `!integrate` | Ningún agente integra módulos o servicios: generan documentos, presentaciones y listados. |
| `!migrate` | No hay sistemas ni datos que migrar; el único traslado (de carpetas) ya se hizo y está documentado. |
| `!workflow` | Cada agente tiene su flujo fijo y documentado; rediseñarlo es trabajo del mantenedor, no un comando del usuario (para documentarlo existe `!document`). |

## Notas de diseño

- `!notime` acelera **sin** recortar verificaciones obligatorias, puertas de aprobación ni veracidad.
- Los comandos de software (`!implement`, `!refactor`, `!code-review`, `!performance`, `!deploy-check`, `!rollback`) y de UX/UI (`!ui-review`, `!ux-review`, `!redesign`, `!design-system`, `!responsive-check`, `!accessibility`, `!microinteractions`, `!componentize`) solo tienen sentido donde hay código y una interfaz: `presentations-designer`.
- `!architecture`, `!roadmap`, `!estimate` encajan en `bidding-agent` (arquitectura, cronograma y horas de la propuesta); `!estimate` también en `quote-developer`.
- Los comandos multiagente y de segunda opinión usan subagentes de Claude Code: no existen en los agentes de Perplexity.
- `!security-check` se adaptó a **confidencialidad y datos sensibles**, que es el riesgo real de estos agentes.
- `!help` no estaba en la lista original: se añadió para que el usuario pueda ver los comandos de cada agente.
