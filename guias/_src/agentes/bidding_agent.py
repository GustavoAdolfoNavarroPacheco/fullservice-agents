# -*- coding: utf-8 -*-
"""Agente Licitatorio — bidding-agent (Claude Code). Fuente: CLAUDE.md, habilidades/*, wiki/estimacion-horas.md, wiki/costeo-ia-tokens.md."""
from kit import *

META = dict(
    slug='bidding-agent', carpeta='bidding-agent', nombre='Agente Licitatorio', corto='agente licitatorio',
    rol='Licitaciones y preventa técnica', icono='flag', paso='6', plataforma='Claude Code',
    resumen='Analiza los cuatro documentos de una licitación y construye la propuesta técnica, la estimación de horas, las consideraciones técnicas y el análisis de IA.',
    tagline_dev='Documentos, jerarquía, habilidades y verificación cruzada de una licitación',
    tagline_usuario='De los documentos de la licitación a una propuesta completa',
)


def dev():
    return [
        statement('qué es', 'Licitaciones ~~defendibles~~',
                  'Especialista en **licitaciones, preventa técnica y estimación**: analiza el proceso completo y produce los cuatro entregables de una propuesta.',
                  '0', 'requerimientos omitidos:\nla matriz de cumplimiento\nes el gate',
                  points=['**Fuente de verdad: solo la documentación suministrada**; todo ítem cita su origen (`RFP §4.2`, `Aclaración P-17`).',
                          'Los dos modelos de costos (oficial y de cotización) se llenan **y se concilian**.',
                          'Toda propuesta declara por escrito si requiere IA, con su justificación.'], hs='32pt'),
        table('entradas', 'Los ~~cuatro documentos~~ de entrada', ['#', 'Documento', 'Qué aporta', 'Obligatorio'], [
            ['1', 'RFP', 'Alcance, requerimientos funcionales y no funcionales, plazos, criterios de evaluación y condiciones.', 'Sí'],
            ['2', 'Aclaraciones / preguntas y respuestas', 'Correcciones y **cambios de alcance**; prevalecen sobre el RFP.', 'Sí'],
            ['3', 'Modelo de costos oficial', 'Formato y reglas de costeo que exige la empresa solicitante.', 'Sí'],
            ['4', 'Modelo de costos de cotización', 'El modelo interno con el que Campuslands calcula el precio real.', 'Sí']],
              '0.4fr 2.2fr 4.4fr 1fr', tf='10pt',
              read=('Regla', 'Si falta alguno de los cuatro, se reporta y se pregunta antes de construir; no se supone su contenido')),
        flow('jerarquía documental', 'Quién ~~prevalece~~ en una contradicción', [
            ('chat', 'Aclaraciones', 'Lo más reciente y vinculante.', '1.º'),
            ('file', 'Adendas', 'Modificaciones formales al RFP.', '2.º'),
            ('book', 'RFP original', 'Base del alcance.', '3.º'),
            ('sheet', 'Modelo oficial', 'Solo para forma y estructura de costeo.', '4.º'),
            ('layers', 'Anexos técnicos', 'Detalle de apoyo.', '5.º')],
             read=('El error más costoso', 'Cotizar un alcance que las aclaraciones ya modificaron. Toda contradicción se registra con la cita de ambos documentos')),
        tree('arquitectura', 'Arquitectura de ~~carpetas~~', [
            (0, 'dir', 'bidding-agent/', ''),
            (1, 'file', 'CLAUDE.md', 'rol, jerarquía, flujo y reglas duras', 'agente'),
            (1, 'dir', 'habilidades/', '5 skills: ingesta · matriz · horas · costos · IA y tokens'),
            (1, 'dir', 'recursos/licitaciones/<slug>/', 'los 4 documentos oficiales', 'solo lectura'),
            (1, 'dir', 'licitaciones/<slug-licitacion>/', ''),
            (2, 'file', '00 – 07 (análisis, matriz, propuesta, horas, ...)', '', 'generado'),
            (2, 'file', 'verificacion-cruzada.md', 'rastro auditable', 'generado'),
            (1, 'dir', 'wiki/', ''),
            (2, 'file', 'flujo-trabajo · estructura-propuesta-tecnica', ''),
            (2, 'file', 'estimacion-horas · consideraciones-tecnicas', ''),
            (2, 'file', 'costeo-ia-tokens', 'precios que caducan'),
            (2, 'file', 'licitaciones/<slug>.md', 'ficha por licitación'),
        ], [('lock', 'Originales intactos', 'El modelo oficial se **copia** a `06` y se trabaja sobre la copia.', 'navy'),
            ('folder', 'Slug con el identificador', 'Ej. `ipa-pr10598`; minúsculas, sin espacios ni tildes.'),
            ('shield', 'Información reservada', 'Una licitación no se mezcla con otra: hay precios y estrategia.')]),
        flow('ciclo de trabajo', 'Tres fases, ~~catorce pasos~~', [
            ('search', 'Ingesta y análisis', 'Verifica los 4 documentos, los lee completos, numera cada requerimiento y consulta las ambigüedades bloqueantes.', 'Pasos 1–5'),
            ('layers', 'Los 4 entregables', 'Matriz › propuesta › horas › consideraciones › IA › modelos de costos.', 'Pasos 6–11'),
            ('shield', 'Verificación y entrega', 'Verificación cruzada con rastro, entrega y actualización de wiki y bitácora.', 'Pasos 12–14')],
             read=('Orden clave', 'La matriz de cumplimiento se llena **antes** de la propuesta técnica: diseña la solución contra la lista completa')),
        table('salidas', 'Qué deja cada ~~licitación~~', ['Archivo', 'Contenido', 'Skill'], [
            ['00 Analisis Documental.md', 'Requerimientos, plazos, contradicciones, supuestos y ambigüedades', 'ingesta'],
            ['01 Matriz de Cumplimiento.xlsx', 'Requerimiento × respuesta × origen', 'matriz-cumplimiento'],
            ['02 Propuesta Tecnica.pdf', 'Módulos, arquitectura, metodología, cronograma y equipo', '—'],
            ['03 Estimacion de Horas.xlsx', 'Horas por módulo y especialidad, con conversión a días', 'estimacion-horas'],
            ['04 Consideraciones Tecnicas.md', 'Checklist técnico y conclusión explícita sobre IA', '—'],
            ['05 Analisis IA y Tokens.xlsx', 'Actividades con IA, tokens y costo (solo si aplica)', 'analisis-ia-tokens'],
            ['06 · 07 Modelos de Costos', 'Oficial y de cotización, llenados y conciliados', 'modelos-costos'],
            ['verificacion-cruzada.md', 'Evidencia de cada comprobación', 'plantilla en wiki']],
              '2.3fr 3.8fr 1.5fr', tf='9pt'),
        rules('reglas duras', 'Diez reglas, ~~cinco~~ que más pesan', [
            ('Nunca inventar', 'Faltante = `[PENDIENTE: qué falta]` y se reporta.'),
            ('Cero requerimientos omitidos', 'Sin fila en la matriz, la propuesta no está lista.'),
            ('Las aclaraciones prevalecen', 'Se revisan antes de dar firme cualquier lectura del RFP.'),
            ('El plazo es una restricción', 'Si no es factible, se dice con números; no se maquilla.'),
            ('Dos modelos, conciliados', 'No se entrega uno sin el otro; la diferencia se explica.'),
            ('Conclusión explícita sobre IA', '«No se mencionó» no es una conclusión.'),
            ('Estimaciones con método', 'Un número sin método ni supuestos no se entrega.'),
            ('Toda decisión se fundamenta', 'Cita del documento o nota de decisión del usuario.')],
              fs='9pt', tones=['navy', '', '', '', '', '', '', '']),
        cards('estimación', 'Estimación ~~defendible~~', [
            ('clock', 'Horas con conversión explícita', 'El entregable va en horas; el modelo interno en días. Factor típico 8 h = 1 día, a confirmar con el usuario.', 'navy'),
            ('users', 'Especialidades del modelo', 'DB · UX · FM · BS · BM · QA · IM · MS · MM · IA: las mismas en ambos modelos.', ''),
            ('target', 'Factibilidad contra el plazo', 'Las horas y el equipo deben caber en el plazo del RFP; si no, se reporta.', ''),
            ('cpu', 'IA solo si hace falta', 'Señales: chatbot, clasificación, extracción, RAG, voz. Costo en tres escenarios.', ''),
            ('alert', 'Precios que caducan', '`costeo-ia-tokens.md` se verifica y actualiza antes de cada costeo.', ''),
            ('sheet', 'Valores vs. fórmulas', 'Si se entregan valores estáticos, se documenta y cómo regenerar el modelo vivo.', '')],
              fs='9.5pt', row=True),
        checks('verificación cruzada', 'Seis ~~comprobaciones~~ antes de entregar', [
            ('Matriz completa', 'Todo requerimiento del RFP y de las aclaraciones tiene respuesta.'),
            ('Horas 1:1 con módulos', 'Ni módulos sin horas ni horas sin módulo.'),
            ('Cronograma factible', 'Cabe en el plazo del RFP con el equipo y las horas propuestas.'),
            ('Totales conciliados', '`06` y `07` cuadran y la diferencia está explicada.'),
            ('IA incluida en costos', 'Los costos de `05` están en ambos modelos.'),
            ('Sin errores de fórmula', '`#REF!`, `#DIV/0!`, `#NAME?` salvo defectos documentados.')],
               read=('Evidencia', 'La verificación deja rastro auditable en `verificacion-cruzada.md`, no solo la afirmación de que se hizo')),
        faq('diagnóstico', 'Síntomas ~~frecuentes~~ y qué hacer', [
            ('Falta uno de los cuatro documentos', 'Se reporta y se pregunta. Si el usuario confirma que no existe, queda escrito en el análisis y en el log.'),
            ('RFP y aclaraciones se contradicen', 'Se registra con ambas citas; si cambia alcance o precio, se pregunta antes de resolver.'),
            ('El plazo no parece factible', 'Se entrega la estimación real con los números y se advierte al usuario.'),
            ('Precios de IA desactualizados', 'Confirmar vigentes en la documentación del proveedor, actualizar la wiki y anotar en `log.md`.')],
            fs='9.5pt'),
        close('Una propuesta que se ~~defiende~~',
              ['Mantén `CLAUDE.md` y las skills alineados.', 'Revisa la fecha de los precios de IA.', 'Registra cada licitación en `wiki/log.md`.'], 'Siguiente paso'),
    ]


def usuario():
    S = 'guía rápida'
    return [
        statement('qué hace', 'Tu equipo de ~~licitaciones~~',
                  'Le entregas **los documentos oficiales** del proceso y construye la propuesta completa: técnica, horas, consideraciones y, si aplica, inteligencia artificial.',
                  '4', 'documentos son todo lo\nque necesita para empezar',
                  points=['Lee todo antes de escribir y numera cada requerimiento.', 'Si los documentos se contradicen, **gana el más reciente** (las aclaraciones) y lo deja anotado.', 'No inventa nada: lo que falta queda marcado para que lo resuelvas.'], hs='32pt'),
        cards(S, 'Los ~~4 documentos~~ que necesita', [
            ('book', 'RFP', 'El documento oficial con el alcance, los plazos y los criterios de evaluación.', ''),
            ('chat', 'Aclaraciones', 'Preguntas y respuestas del proceso. Pueden cambiar el alcance.', 'navy'),
            ('sheet', 'Modelo de costos oficial', 'El formato que exige la empresa que licita.', ''),
            ('calc', 'Modelo de costos de cotización', 'El modelo interno con el que Campuslands calcula el precio real.', '')],
              cols=2, fs='11pt', fh='15pt',
              read=('Importante', 'Si falta alguno, el agente te lo dice y pregunta antes de construir nada')),
        flow(S, 'Cómo se usa, ~~paso a paso~~', [
            ('folder', 'Deja los 4 documentos', 'En `recursos/licitaciones/<nombre-del-proceso>/`.', 'Tú'),
            ('chat', 'Pide el análisis', 'Dile cómo se llama el proceso.', 'Tú'),
            ('help', 'Responde las dudas', 'Te agrupa las preguntas bloqueantes para resolverlas juntas.', 'Tú'),
            ('layers', 'Recibe la propuesta', 'Los cuatro entregables y los dos modelos de costos.', 'Agente'),
            ('shield', 'Revisa y aprueba', 'Con la verificación cruzada a la vista.', 'Tú')],
             read=('Sin esperas', 'Mientras esperas tus respuestas, avanza en todo lo que no depende de ellas')),
        prompts(S, 'Qué ~~escribirle~~: ejemplos', [
            ('Empezar', 'Analiza la licitación ipa-pr10598. Los cuatro documentos ya están en la carpeta de recursos.', 'Empieza por la ingesta y el análisis documental.'),
            ('Resolver dudas', 'Sobre tus preguntas: 1) 200 usuarios, 2) 12 meses de operación, 3) datos en Colombia.', 'Respóndelas juntas, numeradas.'),
            ('Una adenda nueva', 'Llegó una adenda al RFP. Vuelve a revisar el alcance y ajusta la propuesta.', 'Repite el análisis con el cambio.'),
            ('Ver el estado', '¿El cronograma cabe en el plazo que exige el RFP?', 'Responde con los números de la estimación.')],
                 fs='10.5pt'),
        cards(S, 'Qué ~~recibes~~', [
            ('book', 'Propuesta técnica', 'Módulos, arquitectura, metodología, cronograma y equipo.', 'navy'),
            ('clock', 'Estimación de horas', 'Por módulo y especialidad, validada contra el plazo.', ''),
            ('bulb', 'Consideraciones técnicas', 'Qué hay que contemplar y si el alcance requiere IA.', ''),
            ('cpu', 'Análisis de IA', 'Tokens y costo estimado, solo si la IA hace falta.', ''),
            ('list', 'Matriz de cumplimiento', 'Cada requerimiento y cómo se responde.', ''),
            ('calc', 'Dos modelos de costos', 'El oficial y el de cotización, conciliados.', '')],
              fs='10pt', row=True),
        checks(S, 'Cómo ~~revisar~~ la propuesta', [
            ('Cada requerimiento tiene respuesta', 'Mira la matriz: no debe haber filas sin respuesta.'),
            ('El plazo cabe', 'El cronograma cuadra con lo que exige el RFP.'),
            ('Las aclaraciones están aplicadas', 'Nada se cotizó contra un alcance ya cambiado.', 'warn'),
            ('Los totales cuadran', 'Los dos modelos de costos tienen la diferencia explicada.'),
            ('Hay una conclusión sobre IA', 'Dice sí o no, y por qué.'),
            ('Lo pendiente está a la vista', 'Revisa los `[PENDIENTE: ...]` antes de radicar.')]),
        faq(S, 'Preguntas ~~frecuentes~~', [
            ('¿Por qué hace tantas preguntas?', 'Los documentos de licitación casi siempre tienen huecos y él no los rellena por su cuenta.'),
            ('¿Y si las aclaraciones cambian el alcance?', 'Prevalecen. Si cambian precio o alcance de forma importante, te consulta.'),
            ('¿Por qué no hay análisis de IA?', 'Si el alcance no la requiere, queda escrito por qué; no se genera ese archivo.'),
            ('¿Se mezclan datos entre licitaciones?', 'No. Cada proceso vive en su propia carpeta y su información es reservada.')]),
        close('¿Listo para ~~licitar~~?',
              ['Reúne los 4 documentos.', 'Responde las dudas bloqueantes.', 'Revisa la verificación cruzada y radica.'], 'Siguiente paso'),
    ]
