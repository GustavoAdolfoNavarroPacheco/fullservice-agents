# -*- coding: utf-8 -*-
"""Comandos «!» de los agentes: catálogo único y generador.

FUENTE ÚNICA. Aquí se definen los comandos, qué agentes los tienen y qué significan en cada uno. De esta fuente salen:
  · la sección «Comandos» de cada CLAUDE.md / Perplexity.md (entre las marcas  <!-- comandos:inicio --> … <!-- comandos:fin -->)
  · resources/comandos/catalogo.md (catálogo completo, matriz por agente y decisiones)
  · las tablas de las guías web (guides/_src/build.py importa este módulo)
  · una entrada en wiki/log.md de cada agente (una sola vez)

Uso:   python resources/comandos/comandos.py            reescribe las secciones, el catálogo y las bitácoras
       python resources/comandos/comandos.py --verificar   comprueba que nada está desfasado (sale con 1 si lo está)

Para añadir o cambiar un comando: edita CMDS / AGENTES abajo y vuelve a correr el script. No edites a mano lo que está entre las marcas.
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
FECHA = '2026-11-04'
M_INI = '<!-- comandos:inicio (generado por resources/comandos/comandos.py; no editar a mano) -->'
M_FIN = '<!-- comandos:fin -->'

# ----------------------------------------------------------------------------------------------------------------------------------
# REGLA COMÚN (idéntica en todos los agentes)
# ----------------------------------------------------------------------------------------------------------------------------------
REGLA = [
    'Un **comando** es una orden corta del usuario: una palabra precedida de `!` al inicio de un mensaje o de una línea (`!optimize`). '
    'El texto que sigue es su objeto (`!optimize el PDF de alcance`); sin texto, actúa sobre el trabajo en curso.',
    '**Es obligatorio.** Cuando reconozco un comando lo ejecuto: no pido permiso, no lo reinterpreto ni lo sustituyo por algo más cómodo. '
    'Lo único que puede limitarlo es una **regla dura** de este agente (veracidad, marca, confidencialidad, puertas de aprobación o de verificación): '
    'entonces hago todo lo que la regla permite y digo en una frase qué no pude y por qué. Un comando nunca autoriza a inventar datos ni a saltarse una verificación obligatoria.',
    '**Se combinan** (`!plan !no-assumptions`): se cumplen todos. Los de **modo** (`!notime`, `!think-deep`, `!critical-mode`, `!no-assumptions`, `!strict-mode`, `!double-check`) '
    'cambian *cómo* trabajo; los de **acción** (`!plan`, `!audit`, `!final-delivery`…) definen *qué* produzco. Si dos modos chocan, el orden de prioridad es: '
    'reglas duras > `!strict-mode` y `!no-assumptions` > `!think-deep`, `!critical-mode` y `!double-check` > `!notime`.',
    '**Vigencia:** el comando rige la tarea en curso hasta entregarla; no pasa a tareas nuevas (si se quiere, se repite).',
    '**Confirmación:** la primera línea de mi respuesta nombra los comandos recibidos (`Comandos: !optimize, !notime`) y, en una frase, cómo los aplico.',
    '**Comando desconocido o que no aplica aquí:** no lo adivino. Si empieza con `!` y no está en la tabla, lo digo, propongo los más parecidos y pregunto. '
    'Si es de otro agente o no tiene sentido aquí, lo digo y sugiero el equivalente. `!help` lista los comandos disponibles.',
    '**Registro:** si un comando cambió un entregable o la wiki, lo anoto en `wiki/log.md` junto con la acción.',
]

# ----------------------------------------------------------------------------------------------------------------------------------
# CATÁLOGO: nombre -> (grupo, definición)
# ----------------------------------------------------------------------------------------------------------------------------------
G_GEN, G_ING, G_UX, G_PM, G_IA, G_MULTI, G_MODO = 'General', 'Técnico y seguridad', 'UX/UI y diseño', 'Gestión de proyecto', 'IA avanzada', 'Multiagente', 'Modos'
GRUPOS = [G_GEN, G_MODO, G_ING, G_UX, G_PM, G_IA, G_MULTI]

CMDS = {
    # ---- general
    'analyze': (G_GEN, 'Analiza la solicitud, el problema, los documentos o la situación **antes de actuar**: qué se pide, qué hay, qué falta y qué riesgos ve. Entrega hallazgos; no ejecuta ni modifica nada.'),
    'research': (G_GEN, 'Investiga a fondo el tema, cruza fuentes y entrega lo relevante con **cada dato citado a su fuente**. Sin fuente verificable no es un dato: se marca `[PENDIENTE]`.'),
    'plan': (G_GEN, 'Entrega un plan de trabajo estructurado (pasos, orden, insumos, entregables, supuestos y puntos de decisión) y **se detiene a esperar aprobación** antes de ejecutarlo.'),
    'execute': (G_GEN, 'Ejecuta ya lo solicitado o el siguiente paso aprobado del flujo, sin volver a proponer ni a preguntar lo ya decidido. No se salta las puertas de aprobación ni de verificación.'),
    'review': (G_GEN, 'Revisa el trabajo indicado y entrega oportunidades de mejora priorizadas (qué cambiaría y por qué). No lo modifica salvo que se le pida.'),
    'audit': (G_GEN, 'Auditoría integral de punta a punta: contradicciones entre documentos, cifras que no cuadran, reglas incumplidas y datos sin fuente. Entrega hallazgos con evidencia y severidad.'),
    'validate': (G_GEN, 'Comprueba, requisito por requisito, que el resultado cumple lo establecido (reglas duras, insumos, formato). Veredicto «cumple / no cumple» por ítem, con evidencia.'),
    'optimize': (G_GEN, 'Optimiza lo que se esté desarrollando o ya existe (proceso, solución o resultado): mejora claridad, calidad, consistencia, peso o rendimiento **sin cambiar su alcance ni sus datos**.'),
    'compare': (G_GEN, 'Compara alternativas con criterios explícitos y recomienda la más conveniente, con el porqué.'),
    'summarize': (G_GEN, 'Resumen claro y estructurado (lo esencial, decisiones y pendientes) del trabajo, de un documento o de la conversación.'),
    'document': (G_GEN, 'Documenta lo hecho: actualiza la wiki y la bitácora del agente, o genera la documentación técnica, funcional o ejecutiva que se pida.'),
    'prioritize': (G_GEN, 'Clasifica actividades, hallazgos o elementos por impacto, importancia y urgencia, y entrega el orden recomendado.'),
    'help': (G_GEN, 'Lista los comandos disponibles en este agente, agrupados, con su función.'),
    # ---- modos
    'notime': (G_MODO, '**Modo prisa:** apresura el desarrollo optimizándolo: agrupa preguntas en un solo mensaje, paraleliza, reutiliza lo ya validado, omite explicaciones y pasos opcionales y responde solo con lo esencial. '
                       '**Nunca** se salta verificaciones obligatorias, puertas de aprobación ni la veracidad: acelera el camino, no recorta la calidad.'),
    'think-deep': (G_MODO, 'Análisis más profundo antes de responder: considera alternativas, casos límite y consecuencias, y muestra solo el razonamiento que importa.'),
    'critical-mode': (G_MODO, 'Modo crítico: cuestiona decisiones, supuestos y su propio trabajo; busca errores y contradicciones antes de entregar y los dice.'),
    'no-assumptions': (G_MODO, 'No supone: ante un dato faltante o ambiguo pregunta (todas las dudas juntas) en lugar de rellenar o inferir.'),
    'double-check': (G_MODO, 'Segunda verificación independiente de su propio resultado (releer la fuente, recalcular, comparar) y corrección de lo que encuentre; reporta qué verificó.'),
    'strict-mode': (G_MODO, 'Sigue al pie de la letra los requisitos e instrucciones dados: sin iniciativas, adiciones ni interpretaciones creativas.'),
    # ---- ingeniería
    'debug': (G_ING, 'Identifica la causa de un error de software (script, conversión, verificación) y lo corrige; vuelve a correr la verificación para comprobarlo.'),
    'troubleshoot': (G_ING, 'Investiga un problema técnico y determina su **causa raíz**, con evidencia. Diagnostica; no cambia nada.'),
    'security-check': (G_ING, 'Revisa seguridad y confidencialidad: datos de otros clientes mezclados, credenciales, datos personales, información que no debe salir del proyecto.'),
    'implement': (G_ING, 'Desarrolla la funcionalidad o solución solicitada (código, plantilla, script).'),
    'refactor': (G_ING, 'Mejora la estructura del código sin alterar su comportamiento esperado; lo demuestra con la verificación antes y después.'),
    'code-review': (G_ING, 'Evalúa calidad, organización y mantenibilidad del código; entrega observaciones priorizadas.'),
    'performance': (G_ING, 'Analiza y optimiza el rendimiento: tiempos de carga, peso de archivos, fluidez.'),
    'deploy-check': (G_ING, 'Verifica que el proyecto esté listo para publicarse: requisitos, exportación y enlaces comprobados.'),
    'rollback': (G_ING, 'Gestiona la reversión controlada de cambios a un estado anterior conocido, sin perder lo nuevo (queda respaldado).'),
    'architecture': (G_ING, 'Diseña o evalúa la arquitectura de una solución de software.'),
    # ---- ux/ui
    'ui-review': (G_UX, 'Audita visualmente una interfaz y detecta problemas de diseño.'),
    'ux-review': (G_UX, 'Evalúa la experiencia de usuario y los flujos de navegación.'),
    'redesign': (G_UX, 'Propone y desarrolla un rediseño visual, dentro de las reglas de marca.'),
    'design-system': (G_UX, 'Construye, documenta o estandariza el sistema de diseño.'),
    'visual-audit': (G_UX, 'Examina proporciones, distribución, tipografía y consistencia visual del entregable, a la vista y página por página.'),
    'responsive-check': (G_UX, 'Evalúa cómo se adapta la interfaz a distintos tamaños y dispositivos.'),
    'accessibility': (G_UX, 'Evalúa y mejora la accesibilidad: contraste, tamaños, teclado, textos alternativos.'),
    'microinteractions': (G_UX, 'Diseña o implementa microinteracciones y animaciones sutiles, sin romper las reglas de marca.'),
    'consistency-check': (G_UX, 'Detecta inconsistencias entre secciones, componentes, cifras, nombres y estilos del mismo entregable.'),
    'componentize': (G_UX, 'Identifica elementos repetidos y los convierte en componentes reutilizables.'),
    # ---- gestión
    'breakdown': (G_PM, 'Divide un proyecto o solicitud compleja en actividades específicas, cada una con su entregable y su orden.'),
    'roadmap': (G_PM, 'Construye una hoja de ruta de desarrollo con hitos y dependencias.'),
    'estimate': (G_PM, 'Estima tiempos, recursos y complejidad, con el método y los supuestos escritos (un número sin método no se entrega).'),
    'track-progress': (G_PM, 'Informa el progreso y los pendientes (hecho, en curso, bloqueado, `[PENDIENTE]`) a partir de la bitácora y del trabajo actual.'),
    'risk-analysis': (G_PM, 'Identifica riesgos, su probabilidad e impacto, y propone la mitigación de cada uno.'),
    'requirements': (G_PM, 'Extrae y estructura requerimientos funcionales y no funcionales de las fuentes, cada uno con su referencia de origen.'),
    'generate-report': (G_PM, 'Genera un informe ejecutivo (decisiones, resultado, pendientes) o técnico (método, evidencias, verificaciones) del trabajo.'),
    'final-delivery': (G_PM, 'Prepara y valida la entrega final: corre todas las verificaciones obligatorias, completa el checklist de cierre (wiki y bitácora) y entrega solo si todo pasa.'),
    'agent-handoff': (G_PM, 'Prepara el traspaso al siguiente agente del flujo comercial: resumen, entregables con su ruta, decisiones tomadas y pendientes.'),
    # ---- IA avanzada / multiagente (solo Claude Code: usan subagentes)
    'second-opinion': (G_IA, 'Un subagente independiente evalúa el resultado **sin ver tu razonamiento**; se contrasta con el tuyo y se explican las diferencias.'),
    'cross-review': (G_IA, 'Otro especialista (subagente con otro rol) revisa el resultado y devuelve observaciones; se aplican las válidas y se informa de las descartadas.'),
    'orchestrate': (G_MULTI, 'Reparte partes **independientes** del trabajo entre varios subagentes en paralelo y las integra en un solo resultado verificado.'),
    'team-review': (G_MULTI, 'Varios revisores con roles distintos evalúan por separado el mismo resultado y se consolida su evaluación.'),
    'consensus': (G_MULTI, 'Consolida las evaluaciones disponibles (de subagentes o de revisiones previas) en una sola recomendación, con las discrepancias a la vista.'),
}

# alias: se aceptan y se tratan como el comando indicado (nombre -> (comando real, matiz))
ALIAS = {
    'self-correct': ('double-check', 'revisa su propia respuesta, corrige y dice qué cambió'),
    'deep-dive': ('think-deep', 'sobre el tema indicado, con `!research` si hacen falta fuentes'),
    'delegate': ('orchestrate', 'reparte las actividades entre subagentes'),
    'technical-board': ('team-review', 'con revisores técnicos'),
    'design-board': ('team-review', 'con revisores de diseño y marca'),
    'supervisor': ('audit', 'supervisión integral del trabajo'),
    'create-task': ('breakdown', 'cada actividad como tarea con objetivo y entregable'),
}

# comandos del listado original que NO se implementan, con el motivo
SIN_FUNCION = {
    'expert-mode': 'Cada agente ya es un especialista con su rol, reglas y wiki; no hay un «modo experto» que activar.',
    'integrate': 'Ningún agente integra módulos o servicios: generan documentos, presentaciones y listados.',
    'migrate': 'No hay sistemas ni datos que migrar; el único traslado (de carpetas) ya se hizo y está documentado.',
    'workflow': 'Cada agente tiene su flujo fijo y documentado; rediseñarlo es trabajo del mantenedor, no un comando del usuario (para documentarlo existe `!document`).',
}

# ----------------------------------------------------------------------------------------------------------------------------------
# AGENTES: qué comandos tiene cada uno y qué significan ahí
# ----------------------------------------------------------------------------------------------------------------------------------
BASE = ['help', 'analyze', 'research', 'plan', 'execute', 'review', 'audit', 'validate', 'optimize', 'compare', 'summarize', 'document', 'prioritize',
        'notime', 'think-deep', 'critical-mode', 'no-assumptions', 'double-check', 'strict-mode',
        'troubleshoot', 'security-check', 'consistency-check', 'track-progress', 'generate-report', 'final-delivery', 'agent-handoff']
CLAUDE = BASE + ['debug', 'breakdown', 'requirements', 'visual-audit', 'second-opinion', 'cross-review', 'orchestrate', 'team-review', 'consensus']

AGENTES = {
    'prospection-agent': dict(
        nombre='Radar de Campus', plataforma='Perplexity', archivo='agents/perplexity-agents/prospection-agent/Perplexity.md', wiki='agents/perplexity-agents/prospection-agent/wiki',
        aplica=BASE,
        notas={
            'analyze': 'Analiza el pedido contra el formulario de 6 datos y el perfil de cliente ideal antes de buscar; dice qué falta o es contradictorio.',
            'research': 'Es su trabajo central: búsqueda en la web abierta (sin LinkedIn), solo datos públicos, cada uno con su enlace de origen.',
            'plan': 'Presenta los criterios de búsqueda, las fuentes y la forma del listado, y espera el visto bueno antes de buscar.',
            'validate': 'Comprueba cada empresa contra los criterios confirmados (sector, ubicación, tamaño, facturación) y cada dato contra su fuente.',
            'optimize': 'Afina los criterios y la consulta de búsqueda, o deja la tabla más limpia y sin duplicados; no cambia el perfil que pediste.',
            'prioritize': 'Ordena las empresas por encaje con el perfil, de mayor a menor, y dice por qué.',
            'compare': 'Compara empresas entre sí, o dos estrategias de búsqueda, con criterios explícitos.',
            'double-check': 'Vuelve a abrir la fuente de cada dato dudoso y confirma que sigue vigente.',
            'security-check': 'Revisa que el listado solo lleve datos públicos y de empresas; ningún dato personal ni privado.',
            'consistency-check': 'Revisa que todas las filas tengan las mismas columnas, formatos y criterios.',
            'final-delivery': 'Entrega el listado final con todas las columnas completas o marcadas `[PENDIENTE]`, y pregunta qué sigue (ampliar, repetir o pasar a Explorador de Campus).',
            'agent-handoff': 'Prepara el listado para **Explorador de Campus** (`intelligence-commercial`): tabla de empresas con las columnas que ese agente espera.',
            'troubleshoot': 'Averigua por qué una búsqueda no devuelve resultados o devuelve empresas que no encajan.',
        }),
    'intelligence-commercial': dict(
        nombre='Explorador de Campus', plataforma='Perplexity', archivo='agents/perplexity-agents/intelligence-commercial/Perplexity.md', wiki='agents/perplexity-agents/intelligence-commercial/wiki',
        aplica=BASE,
        notas={
            'analyze': 'Analiza la lista de empresas y la meta de conexiones antes de empezar: qué datos faltan, qué contactos encajan.',
            'research': 'Enriquece cada empresa con datos públicos y busca a los contactos clave, citando la fuente.',
            'plan': 'Presenta el plan de lotes (cuántas invitaciones por lote, pausas, orden) y espera aprobación antes de enviar nada.',
            'execute': 'Avanza al siguiente lote aprobado. **Nunca** envía invitaciones sin que el plan de lotes y el mensaje estén aprobados.',
            'validate': 'Valida cada contacto (cargo, empresa, idioma detectado) y cada mensaje contra las reglas del agente antes del envío.',
            'optimize': 'Mejora los mensajes personalizados o el orden de los contactos; no cambia la meta de conexiones ni el ritmo seguro de envío.',
            'prioritize': 'Ordena contactos y empresas por probabilidad de respuesta e importancia comercial.',
            'notime': 'Agrupa los pasos y reduce explicaciones, pero **mantiene los lotes pequeños y las pausas**: el ritmo de LinkedIn es una regla de seguridad.',
            'security-check': 'Revisa el riesgo para la cuenta de LinkedIn (ritmo, volumen, mensajes repetidos) y que no se filtren datos personales en el informe.',
            'troubleshoot': 'Diagnostica por qué falla una acción de navegador en LinkedIn o por qué un perfil no se pudo leer.',
            'consistency-check': 'Revisa que los CSV mantengan columnas, formatos y estados coherentes entre fases.',
            'final-delivery': 'Cierra con el informe final (envíos, aceptaciones, pendientes) y los CSV completos.',
            'agent-handoff': 'Prepara el traspaso a **Estudio de Presentaciones** (`presentations-designer`) cuando hay un contacto interesado: empresa, contacto, contexto de la conversación.',
        }),
    'presentations-designer': dict(
        nombre='Estudio de Presentaciones', plataforma='Claude Code', archivo='agents/claude-agents/presentations-designer/CLAUDE.md', wiki='agents/claude-agents/presentations-designer/wiki',
        aplica=[c for c in CLAUDE if c not in ('requirements',)] + ['requirements', 'implement', 'refactor', 'code-review', 'performance', 'deploy-check', 'rollback',
                                                                    'ui-review', 'ux-review', 'redesign', 'design-system', 'responsive-check', 'accessibility', 'microinteractions', 'componentize'],
        notas={
            'analyze': 'Analiza los alcances y datos del cliente: qué mensaje, qué cifras, qué falta; no diseña todavía.',
            'plan': 'Es el **plan lámina por lámina** (máx. 10): pregunta que responde cada una, contenido y diseño. Espera aprobación antes de construir.',
            'execute': 'Construye el borrador del plan **ya aprobado**. Sin plan aprobado no construye: lo pide.',
            'optimize': 'Pule la presentación en curso (ritmo, texto, jerarquía, peso) sin cambiar el plan aprobado ni las reglas de marca.',
            'validate': 'Corre `verificar_deck.py` y la revisión a la vista de cada lámina contra las reglas supremas del Brandbook.',
            'audit': 'Auditoría de la presentación completa: marca, cifras, logos, láminas fuera de las reglas, coherencia entre láminas.',
            'notime': 'Agrupa preguntas, construye por bloques y reduce explicaciones. **No** se salta el plan aprobado ni la verificación automática y a la vista.',
            'final-delivery': 'Verificación completa, PDF, registro en el portal y publicación con link; solo entrega si la publicación está confirmada.',
            'deploy-check': 'Comprueba antes de publicar: requisitos de `<head>`, visor interactivo, PDF exportado, registro en el portal y enlace que abre.',
            'rollback': 'Vuelve la presentación a una versión anterior con git, conservando la nueva en una rama o copia.',
            'performance': 'Mide y reduce el peso y el tiempo de carga de la presentación (imágenes, fuentes, scripts) y del portal.',
            'redesign': 'Rediseña una lámina o sección **dentro del Brandbook v3** (fondo blanco, Poppins, colores Campuslands); nunca cambia las reglas de marca.',
            'design-system': 'Documenta o ajusta el sistema de diseño v3 en `wiki/sistema-diseno.md` y la plantilla base.',
            'ui-review': 'Revisa a la vista láminas y visor: jerarquía, alineación, espaciado, legibilidad.',
            'ux-review': 'Evalúa el recorrido de quien ve la presentación: navegación del visor, ritmo, claridad del mensaje.',
            'visual-audit': 'Examina cada lámina a la vista: proporciones, distribución, tipografía, logos (mismo peso visual) y consistencia.',
            'responsive-check': 'Comprueba el visor y el portal en distintos anchos de pantalla.',
            'accessibility': 'Revisa contraste, tamaños de texto, navegación por teclado y textos alternativos del visor y las láminas.',
            'microinteractions': 'Propone o implementa transiciones y animaciones del visor que respeten las reglas de marca y no distraigan.',
            'componentize': 'Convierte bloques repetidos de láminas en componentes de la plantilla base reutilizables.',
            'consistency-check': 'Revisa que nombres, cifras, logos y estilos sean idénticos en todas las láminas y en el PDF.',
            'security-check': 'Revisa que no se mezclen datos de otros clientes, que el portal limite el acceso y que las presentaciones confidenciales no queden públicas.',
            'implement': 'Desarrolla la herramienta, plantilla o mejora del portal pedida, verificada con las herramientas del repositorio.',
            'code-review': 'Revisa el código de la plantilla, el visor, los scripts y el portal (`presentaciones/web`).',
            'refactor': 'Reordena código del visor, scripts o plantilla sin cambiar lo que producen; lo demuestra con `verificar_deck.py`.',
            'requirements': 'Extrae de los alcances los datos que la presentación necesita (6 bloques) y señala lo que falta.',
            'team-review': 'Revisores con rol de **diseño/marca**, **contenido y veracidad** y **técnico (HTML/visor)**, cada uno por separado.',
            'orchestrate': 'Reparte láminas o verificaciones independientes entre subagentes; la integración y la verificación final las hace el agente principal.',
            'agent-handoff': 'Prepara el traspaso a **Desarrollador de Cotizaciones** (`quote-developer`) con la presentación aprobada, sus datos y decisiones.',
            'troubleshoot': 'Averigua por qué falla una verificación, la exportación a PDF o la publicación.',
            'debug': 'Corrige el fallo encontrado en scripts, plantilla o visor y repite la verificación.',
        }),
    'functional-scope': dict(
        nombre='Alcances Funcionales', plataforma='Claude Code', archivo='agents/claude-agents/functional-scope/CLAUDE.md', wiki='agents/claude-agents/functional-scope/wiki',
        aplica=CLAUDE + ['risk-analysis'],
        notas={
            'analyze': 'Lee las fuentes del cliente y detecta contradicciones, vacíos y supuestos sin redactar todavía el documento.',
            'plan': 'Presenta la estructura del documento de alcance y la lista de preguntas pendientes; espera aprobación.',
            'requirements': 'Es el núcleo del agente: extrae requerimientos funcionales y no funcionales con su fuente, y marca lo ambiguo.',
            'validate': 'Aplica el **control de calidad** del manual (§8) al documento: estructura obligatoria, trazabilidad y cero compromisos inventados.',
            'audit': 'Busca contradicciones entre las fuentes y entre estas y el documento; entrega hallazgos con evidencia.',
            'no-assumptions': 'Refuerza la política de faltantes: lo que no está en las fuentes se pregunta o queda `[PENDIENTE]`, nunca se completa.',
            'risk-analysis': 'Riesgos del alcance: requisitos ambiguos, dependencias externas, supuestos frágiles y su mitigación.',
            'breakdown': 'Divide el alcance en módulos y funcionalidades atómicas.',
            'visual-audit': 'Revisa a la vista el documento entregado (portada, tablas, jerarquía, paginación).',
            'final-delivery': 'Control de calidad completo, documento final con el formato de entrega y wiki/bitácora al día.',
            'track-progress': 'Informa estados y pendientes del documento y quién debe resolver cada uno.',
            'agent-handoff': 'Prepara el traspaso a **Desarrollador de Cotizaciones** (`quote-developer`): alcance aprobado, módulos y supuestos.',
            'team-review': 'Revisores con rol **funcional**, **QA (contradicciones y vacíos)** y **comunicación con el cliente**.',
        }),
    'quote-developer': dict(
        nombre='Desarrollador de Cotizaciones', plataforma='Claude Code', archivo='agents/claude-agents/quote-developer/CLAUDE.md', wiki='agents/claude-agents/quote-developer/wiki',
        aplica=CLAUDE + ['estimate', 'risk-analysis'],
        notas={
            'analyze': 'Analiza los alcances: módulos, funcionalidades y lo que falta para estimar; no llena nada todavía.',
            'plan': 'Presenta la estructura de módulos/funcionalidades y el criterio de estimación; espera aprobación antes de llenar el XLSX.',
            'estimate': 'Días por especialidad y funcionalidad, con el método y los supuestos escritos; respeta las celdas y fórmulas intocables de la plantilla.',
            'validate': 'Verificación obligatoria: suma de módulos + transversales = total del XLSX = total del PDF, fórmulas intactas y sin errores nuevos.',
            'double-check': 'Recalcula los totales del XLSX y los compara con el PDF, cifra por cifra.',
            'optimize': 'Ordena y afina la estructura del XLSX y el PDF sin cambiar días ni precios.',
            'requirements': 'Extrae de los alcances la jerarquía módulo → submódulo → funcionalidad con su referencia.',
            'risk-analysis': 'Riesgos de la estimación: funcionalidades ambiguas, dependencias, supuestos de precio.',
            'visual-audit': 'Revisa a la vista el PDF de cotización (diseño vigente, tablas, paginación).',
            'final-delivery': 'XLSX y PDF verificados, precios coherentes entre ambos, wiki y bitácora al día.',
            'agent-handoff': 'Prepara el traspaso a **Perfeccionador de Contratos** (`contract-perfectionist`): cotización aprobada y su ruta.',
            'team-review': 'Revisores con rol **costos (XLSX)**, **alcance (PDF frente a la fuente)** y **marca y diseño**.',
        }),
    'bidding-agent': dict(
        nombre='Agente Licitatorio', plataforma='Claude Code', archivo='agents/claude-agents/bidding-agent/CLAUDE.md', wiki='agents/claude-agents/bidding-agent/wiki',
        aplica=CLAUDE + ['estimate', 'risk-analysis', 'roadmap', 'architecture'],
        notas={
            'analyze': 'Ingesta y análisis documental de los cuatro documentos (RFP, aclaraciones, modelo oficial, modelo de cotización); las aclaraciones prevalecen.',
            'plan': 'Presenta cómo construirá los cuatro entregables y las dudas que bloquean; espera respuesta antes de construir.',
            'requirements': 'Construye la matriz de cumplimiento: cada requerimiento del RFP y de las aclaraciones con su respuesta y referencia.',
            'validate': 'Comprueba cobertura (ningún requerimiento sin fila), trazabilidad y que el plazo sea factible con el equipo propuesto.',
            'audit': 'Verificación cruzada: propuesta, horas, costos y modelos conciliados entre sí y con el RFP.',
            'estimate': 'Horas por módulo y especialidad, o tokens y costo de IA, con método y supuestos escritos.',
            'architecture': 'Diseña o evalúa la arquitectura de la solución de la propuesta técnica, con su justificación.',
            'roadmap': 'Cronograma de la propuesta, factible dentro del plazo exigido.',
            'risk-analysis': 'Riesgos del proceso y de la solución: plazos, ambigüedades, dependencias, descalificación.',
            'security-check': 'Confidencialidad: cada proceso es confidencial; no mezcla información de una licitación con otra.',
            'final-delivery': 'Matriz completa, los cuatro entregables y los dos modelos conciliados, con la verificación cruzada hecha.',
            'agent-handoff': 'Si se adjudica, prepara el traspaso a **Perfeccionador de Contratos** (`contract-perfectionist`) con la propuesta y el modelo de costos radicado.',
            'orchestrate': 'Ingesta de los documentos y construcción de entregables independientes en paralelo; la conciliación y la verificación cruzada las hace el agente principal.',
            'team-review': 'Revisores con rol **técnico (arquitectura y horas)**, **costos** y **cumplimiento frente al RFP**.',
        }),
    'contract-perfectionist': dict(
        nombre='Perfeccionador de Contratos', plataforma='Claude Code', archivo='agents/claude-agents/contract-perfectionist/CLAUDE.md', wiki='agents/claude-agents/contract-perfectionist/wiki',
        aplica=CLAUDE + ['risk-analysis'],
        notas={
            'analyze': 'Analiza alcances, cotización y Contrato Madre: datos duros, cifras y lo que falta antes de redactar.',
            'plan': 'Presenta el checklist de datos y la estructura de cláusulas; espera confirmación antes de redactar.',
            'validate': 'Corre la verificación cruzada (cada cifra, plazo y alcance frente a la fuente) y el gate `build_contract.py check`.',
            'audit': 'Busca contradicciones entre el contrato, la cotización, los alcances y el Contrato Madre.',
            'risk-analysis': 'Riesgos contractuales: cláusulas de protección omitidas, ambigüedades, discrepancias de cifras o plazos.',
            'security-check': 'Los datos de clientes son confidenciales: revisa que no se mezclen entre clientes y qué carpetas no deben compartirse.',
            'visual-audit': 'Revisa a la vista el `.docx` (membrete, líneas de firma, numeración, formato corporativo).',
            'debug': 'Corrige fallos de `build_contract.py` (placeholders sin resolver, membrete o firma perdidos) y repite el gate.',
            'final-delivery': 'Verificación cruzada y gate superados, contrato en su carpeta con el nombre convenido, wiki y bitácora al día.',
            'agent-handoff': 'Cierra el flujo: prepara el paquete para revisión legal y firma (contrato, verificación cruzada y pendientes).',
            'team-review': 'Revisores con rol **jurídico (cláusulas)**, **comercial (cifras frente a la cotización)** y **forma (plantilla corporativa)**.',
        }),
    'multifunctional-agent': dict(
        nombre='Agente Multifuncional', plataforma='Claude Code', archivo='agents/claude-agents/multifunctional-agent/CLAUDE.md', wiki='agents/claude-agents/multifunctional-agent/wiki',
        aplica=[c for c in CLAUDE if c not in ('requirements', 'breakdown')],
        notas={
            'analyze': 'Revisa los archivos de entrada y dice qué detectó (facturas: fechas, horas y proveedores; audio: duración y motor disponible) sin generar nada todavía.',
            'plan': 'Presenta cómo procesará el lote o el audio (orden esperado, modelo de voz, dudas) y espera aprobación antes de generar.',
            'validate': 'Facturas: orden cronológico por el recibo, una factura por hoja y banner igual al recibo. Transcripción: estructura de la referencia, partes de 5 min y etiquetas de hablante.',
            'audit': 'Busca discrepancias entre el nombre de cada archivo y lo que dice el recibo, fechas dudosas, facturas sin hora y hablantes sin respaldo en el audio.',
            'double-check': 'Facturas: relee cada recibo y lo compara con su banner. Transcripción: contrasta una muestra de líneas con sus marcas de tiempo.',
            'visual-audit': 'Renderiza el PDF y lo revisa página por página: banner, recibo completo y legible, pie «Página N de M»; en la transcripción, partes, hablantes y membrete.',
            'security-check': 'Confidencialidad: recibos con datos personales y audios de reuniones con clientes; comprueba que nada salió del equipo (todo es local) ni quedó versionado en git.',
            'optimize': 'Mejora la calidad del resultado (p. ej. repetir la transcripción con un modelo más preciso o con vocabulario) sin cambiar el contenido ni el diseño vigente.',
            'debug': 'Corrige fallos de los scripts (LibreOffice, ffmpeg, modelos de voz, lectura de un recibo) y repite la verificación.',
            'final-delivery': 'Word y PDF verificados a la vista, avisos incluidos, wiki y bitácora al día y la autoprueba superada si se tocó código.',
            'agent-handoff': 'Prepara el traspaso de una transcripción de reunión con cliente a **Alcances Funcionales** (`functional-scope`) como fuente de `alcances/<cliente>/fuentes/`.',
            'orchestrate': 'Reparte lotes de facturas o tramos de audio independientes entre subagentes; la integración y la verificación final las hace el agente principal.',
            'team-review': 'Revisores con rol **datos (fechas, horas, orden)**, **diseño (banner y membrete)** y **fidelidad (transcripción literal)**.',
        }),
}

NOTA_PERPLEXITY_MULTI = ('Este agente corre en Perplexity y **no tiene subagentes**: los comandos multiagente (`!orchestrate`, `!delegate`, `!cross-review`, `!second-opinion`, '
                         '`!team-review`, `!technical-board`, `!design-board`, `!consensus`, `!supervisor`) no existen aquí; para una segunda mirada usa `!double-check` o `!critical-mode`.')


# ----------------------------------------------------------------------------------------------------------------------------------
# RENDER
# ----------------------------------------------------------------------------------------------------------------------------------
def disponibles(slug):
    a = AGENTES[slug]
    orden = {g: i for i, g in enumerate(GRUPOS)}
    return sorted(dict.fromkeys(a['aplica']), key=lambda c: (orden[CMDS[c][0]], list(CMDS).index(c)))


def definicion(slug, cmd):
    """Definición genérica + lo que significa en este agente."""
    d = CMDS[cmd][1]
    n = AGENTES[slug]['notas'].get(cmd)
    return d + (' **Aquí:** ' + n if n else '')


def alias_de(slug):
    """Alias que funcionan en este agente (su comando real está disponible)."""
    disp = set(AGENTES[slug]['aplica'])
    return {a: v for a, v in ALIAS.items() if v[0] in disp}


def seccion_md(slug):
    a = AGENTES[slug]
    L = ['## Comandos (`!`)', '']
    L += ['%d. %s' % (i + 1, t) for i, t in enumerate(REGLA)]
    L += ['', '### Comandos disponibles en %s' % a['nombre']]
    grupo = None
    for c in disponibles(slug):
        g = CMDS[c][0]
        if g != grupo:
            grupo = g
            L += ['', '**%s**' % g, '', '| Comando | Qué hago aquí |', '|---|---|']
        L.append('| `!%s` | %s |' % (c, definicion(slug, c).replace('|', '\\|')))
    al = alias_de(slug)
    if al:
        L += ['', '**Alias** (funcionan igual que el comando indicado): ' + '; '.join('`!%s` → `!%s` (%s)' % (k, v[0], v[1]) for k, v in al.items()) + '.']
    if a['plataforma'] == 'Perplexity':
        L += ['', NOTA_PERPLEXITY_MULTI]
    L += ['', '**Sin función en ningún agente:** ' + ', '.join('`!%s`' % k for k in SIN_FUNCION) + '. Si se escribe uno, lo digo y propongo el equivalente.',
          '', 'Catálogo completo y decisiones: `resources/comandos/catalogo.md` (carpeta compartida del repositorio).']
    return '\n'.join(L)


def tabla_html(slug, esc):
    """Tablas para las guías web (agrupadas). `esc` convierte texto Markdown mínimo a HTML (lo pasa build.py)."""
    out = ''
    grupo = None
    for c in disponibles(slug):
        g = CMDS[c][0]
        if g != grupo:
            if grupo:
                out += '</tbody></table></div>'
            grupo = g
            out += '<h4>%s</h4><div class="tw"><table class="cmd"><thead><tr><th>Comando</th><th>Qué hace aquí</th></tr></thead><tbody>' % g
        out += '<tr><td><code>!%s</code></td><td>%s</td></tr>' % (c, esc(definicion(slug, c)))
    return out + '</tbody></table></div>'


def catalogo_md():
    L = ['# Comandos `!` de los agentes', '',
         'Catálogo único. **Generado** por `resources/comandos/comandos.py`: no se edita a mano (edita el script y vuelve a correrlo).', '',
         '## Regla común', '']
    L += ['%d. %s' % (i + 1, t) for i, t in enumerate(REGLA)]
    slugs = list(AGENTES)
    L += ['', '## Matriz: qué comando tiene cada agente', '', '| Comando | Grupo | ' + ' | '.join('`%s`' % s for s in slugs) + ' |', '|---|---|' + '---|' * len(slugs)]
    for c in CMDS:
        L.append('| `!%s` | %s | ' % (c, CMDS[c][0]) + ' | '.join('●' if c in AGENTES[s]['aplica'] else '·' for s in slugs) + ' |')
    L += ['', '● = disponible · = no aplica a ese agente.', '', '## Definiciones', '']
    grupo = None
    for c in CMDS:
        g = CMDS[c][0]
        if g != grupo:
            grupo = g
            L += ['', '### %s' % g, '', '| Comando | Qué hace |', '|---|---|']
        L.append('| `!%s` | %s |' % (c, CMDS[c][1].replace('|', '\\|')))
    L += ['', '## Alias (se aceptan y se tratan como otro comando)', '', '| Alias | Equivale a | Matiz |', '|---|---|---|']
    L += ['| `!%s` | `!%s` | %s |' % (k, v[0], v[1]) for k, v in ALIAS.items()]
    L += ['', '## Sin función (no se implementan)', '', '| Comando | Motivo |', '|---|---|']
    L += ['| `!%s` | %s |' % (k, v) for k, v in SIN_FUNCION.items()]
    L += ['', '## Notas de diseño', '',
          '- `!notime` acelera **sin** recortar verificaciones obligatorias, puertas de aprobación ni veracidad.',
          '- Los comandos de software (`!implement`, `!refactor`, `!code-review`, `!performance`, `!deploy-check`, `!rollback`) y de UX/UI (`!ui-review`, `!ux-review`, `!redesign`, `!design-system`, '
          '`!responsive-check`, `!accessibility`, `!microinteractions`, `!componentize`) solo tienen sentido donde hay código y una interfaz: `presentations-designer`.',
          '- `!architecture`, `!roadmap`, `!estimate` encajan en `bidding-agent` (arquitectura, cronograma y horas de la propuesta); `!estimate` también en `quote-developer`.',
          '- Los comandos multiagente y de segunda opinión usan subagentes de Claude Code: no existen en los agentes de Perplexity.',
          '- `!security-check` se adaptó a **confidencialidad y datos sensibles**, que es el riesgo real de estos agentes.',
          '- `!help` no estaba en la lista original: se añadió para que el usuario pueda ver los comandos de cada agente.', '']
    return '\n'.join(L)


# ----------------------------------------------------------------------------------------------------------------------------------
# ESCRITURA
# ----------------------------------------------------------------------------------------------------------------------------------
def _leer(p):
    raw = p.read_bytes().decode('utf-8')
    nl = '\r\n' if '\r\n' in raw else '\n'
    return raw.replace('\r\n', '\n'), nl


def _escribir(p, txt, nl):
    p.write_bytes(txt.replace('\n', nl).encode('utf-8'))


def actualizar_instrucciones(slug):
    p = RAIZ / AGENTES[slug]['archivo']
    txt, nl = _leer(p)
    # sangría del ancla (Perplexity.md de prospection está sangrado 3 espacios)
    ancla = re.search(r'^( *)## (Convenciones de la bitácora|Al terminar cada (contrato|entrega))', txt, re.M)
    if not ancla:
        raise SystemExit('Sin ancla en %s' % p)
    sg = ancla.group(1)
    bloque = '\n'.join((sg + l if l else l) for l in (M_INI + '\n\n' + seccion_md(slug) + '\n\n' + M_FIN).split('\n')) + '\n\n'
    pat = re.compile(r'^ *' + re.escape(M_INI) + r'.*?' + re.escape(M_FIN) + r'\n\n?', re.S | re.M)
    nuevo = pat.sub(lambda m: bloque, txt) if pat.search(txt) else txt[:ancla.start()] + bloque + txt[ancla.start():]
    cambio = nuevo != txt
    if cambio:
        _escribir(p, nuevo, nl)
    return cambio


def actualizar_bitacora(slug):
    p = RAIZ / AGENTES[slug]['wiki'] / 'log.md'
    txt, nl = _leer(p)
    if '| Comandos «!»' in txt:
        return False
    n = len(disponibles(slug))
    entrada = ('\n## [%s] ajuste | Comandos «!»\n'
               'Se incorporan los **comandos «!»**: órdenes cortas (`!optimize`, `!notime`, `!plan`…) que el agente ejecuta de forma obligatoria, dentro de sus reglas duras. '
               'Este agente tiene %d comandos; la regla común, la tabla de comandos y su significado aquí están en la sección «Comandos» de `%s`. '
               'Catálogo completo y decisiones: `resources/comandos/catalogo.md`.\n' % (FECHA, n, pathlib.Path(AGENTES[slug]['archivo']).name))
    _escribir(p, txt.rstrip('\n') + '\n' + entrada, nl)
    return True


def main():
    verificar = '--verificar' in sys.argv
    cambios = []
    cat = RAIZ / 'resources' / 'comandos' / 'catalogo.md'
    nuevo = catalogo_md()
    if not cat.exists() or cat.read_text(encoding='utf-8') != nuevo:
        cambios.append('catalogo.md')
        if not verificar:
            cat.write_text(nuevo, encoding='utf-8')
    for slug in AGENTES:
        if verificar:
            p = RAIZ / AGENTES[slug]['archivo']
            txt, _ = _leer(p)
            m = re.search(re.escape(M_INI) + r'(.*?)' + re.escape(M_FIN), txt, re.S)
            if not m or seccion_md(slug).strip() not in re.sub(r'(?m)^ +', '', m.group(1)):
                cambios.append(AGENTES[slug]['archivo'])
        else:
            if actualizar_instrucciones(slug):
                cambios.append(AGENTES[slug]['archivo'])
            if actualizar_bitacora(slug):
                cambios.append(AGENTES[slug]['wiki'] + '/log.md')
    print(('DESFASADO: ' if verificar and cambios else 'Actualizado: ' if cambios else 'Todo al día. ') + ', '.join(cambios))
    if verificar and cambios:
        sys.exit(1)


if __name__ == '__main__':
    main()
