# -*- coding: utf-8 -*-
"""Alcances Funcionales — functional-scope (Claude Code). Fuente: CLAUDE.md, wiki/manual-operativo.md, plantillas/, scripts/."""
from kit import *

META = dict(
    slug='functional-scope', carpeta='functional-scope', nombre='Alcances Funcionales', corto='alcances funcionales',
    rol='Documentos de alcance funcional', icono='target', paso='4', plataforma='Claude Code',
    resumen='Lee las fuentes de un proyecto, detecta contradicciones y vacíos y redacta el documento de alcance funcional para el cliente, sin inventar compromisos.',
    tagline_dev='Flujo, estados, plantillas y control de calidad del alcance funcional',
    tagline_usuario='De tus archivos de proyecto a un alcance listo para revisar',
)


def dev():
    return [
        statement('qué es', 'Alcance ~~sin inventar~~ compromisos',
                  'Actúa como **Product Manager senior y analista de negocio**: analiza las fuentes del proyecto y redacta un documento de alcance funcional de cara al cliente.',
                  '3', 'estados siempre visibles:\nCONFIRMADO · PROPUESTO\n· PENDIENTE',
                  points=['Fuente normativa: `recursos/Manual_Agente_Alcances_Funcionales_Campuslands.docx` (v1.0, oct. 2026); si algo lo contradice, se avisa.',
                          'Un archivo compartido **es todo lo que hay**: no entrevista ni pregunta lo que el archivo no trae.',
                          'No reemplaza la aprobación técnica, comercial, jurídica ni del cliente.'], hs='30pt'),
        tree('arquitectura', 'Arquitectura de ~~carpetas~~', [
            (0, 'dir', 'functional-scope/', ''),
            (1, 'file', 'CLAUDE.md', 'reglas, flujo y diseño del documento', 'agente'),
            (1, 'dir', 'recursos/', 'manual, plantilla Word y marca', 'solo lectura'),
            (1, 'dir', 'plantillas/', 'ficha funcional · trazabilidad · riesgos y pendientes · matrices · .docx base'),
            (1, 'dir', 'scripts/', ''),
            (2, 'file', 'alcance_docx.py', 'constructor del .docx (clase Alcance)'),
            (2, 'file', 'previsualizar.py', 'docx › PDF y un PNG por página'),
            (1, 'dir', 'alcances/<cliente-slug>/', ''),
            (2, 'dir', 'fuentes/', 'insumos del usuario; no se editan', 'solo lectura'),
            (2, 'dir', 'trabajo/', '01 inventario · 02 matriz · 03 pendientes · 04 decisiones · 05 calidad', 'generado'),
            (2, 'dir', 'entrega/', 'documento al cliente, una versión por archivo', 'generado'),
            (1, 'dir', 'wiki/', 'index · log · manual-operativo · ejemplos/'),
        ], [('book', 'El manual manda', '`wiki/manual-operativo.md` lo resume para consulta rápida.', 'navy'),
            ('folder', 'Una carpeta por cliente', 'Si hay varios proyectos: `<cliente>-<proyecto>`.'),
            ('alert', 'Los ejemplos son solo método', '`wiki/ejemplos/` nunca se copia a otro proyecto.')]),
        table('ciclo de trabajo', 'Flujo de ~~ocho etapas~~', ['Etapa', 'Acción', 'Salida en `trabajo/`'], [
            ['1 · Recepción', 'Identifica proyecto, cliente, archivos y versión vigente de cada fuente.', '`01-inventario-fuentes.md`'],
            ['2 · Lectura', 'Extrae requisitos, decisiones, cifras, exclusiones y contradicciones.', '`02-matriz-informacion.md`'],
            ['3 · Diagnóstico', 'Clasifica vacíos: BLOQUEANTE · IMPORTANTE · EDITORIAL.', '`03-pendientes.md`'],
            ['4 · Cierre de vacíos', 'Sin entrevista: lo que falta queda pendiente con responsable.', '`04-registro-decisiones.md`'],
            ['5 · Resumen', 'Alcance y supuestos a la vista, en el chat.', 'Chat'],
            ['6 · Redacción', 'Documento y anexos justo después del diagnóstico.', 'Borrador en `entrega/`'],
            ['7 · Control de calidad', 'Checklist del manual §8, con evidencia.', '`05-control-calidad.md`'],
            ['8 · Entrega', 'Documento editable + resumen de pendientes; wiki y log.', '`entrega/` + `wiki/log.md`']],
              '1.5fr 4fr 2.1fr', tf='9pt'),
        rules('reglas duras', 'Reglas que ~~no se negocian~~', [
            ('Solo lo aportado', 'Nada de memoria ni de «lo típico en proyectos así».'),
            ('Tres estados', 'Nunca presentar una opción sugerida como decisión tomada.'),
            ('Lo futuro no se contrata', 'Hipótesis e ideas de fases futuras van solo en «Fases futuras».'),
            ('No inventar', 'Cifras, fechas, SLA, métricas, integraciones, PI ni responsabilidades.'),
            ('Contradicciones', 'Mostrar ambas versiones con documento, sección y fecha; nunca elegir en silencio.'),
            ('IA con límites', 'Sin exactitud perfecta ni entrenamiento: tarea, fuentes, supervisión humana y trazabilidad.'),
            ('Términos comerciales', 'Precio, garantía, soporte y SLA solo si la fuente los dice; si no, `[PENDIENTE DE VALIDACIÓN]`.'),
            ('Reserva de datos', 'Un cliente por proyecto; no se mezclan datos entre documentos.')],
              fs='9pt', tones=['navy', '', '', '', '', '', '', '']),
        versus('regla de preguntas', 'Regla de ~~preguntas~~ (2026-10-29)',
               dict(pill='Sí hace', h='Trabaja con lo que hay', items=['Diagnostica y **redacta en el mismo turno**', 'Marca lo que falta como pendiente', 'Registra lo que el usuario diga por iniciativa propia', 'Pregunta solo si no puede ni empezar (una pregunta, con opción por defecto)']),
               dict(pill='No hace', h='Lo que dejó de hacer', items=['Entrevistas por bloques', 'Preguntar lo que el archivo no trae', 'Detenerse por un «no sé»', 'Pedir permiso para empezar'], no=True),
               arrow=False, fs='11pt', read=('Excepción', 'Dos archivos que se contradicen y sin fuente principal clara: es la única pregunta válida')),
        table('documento al cliente', 'Estructura ~~obligatoria~~ del documento', ['Parte', 'Regla'], [
            ['1 · Portada', 'Una sola hoja; sin versión, estado ni clasificación; nota legal al pie.'],
            ['2 · Carta de presentación', 'Una hoja repartida por toda la página; lista lo que contiene el documento.'],
            ['3 · Tabla de contenido', 'Una hoja, ya generada: nunca un campo vacío por actualizar.'],
            ['4 · Contenido', 'Resumen ejecutivo › … › anexos y referencias; las secciones sin dato llevan `[PENDIENTE DE VALIDACIÓN]`.'],
            ['5 · Aprobación y firmas', 'Última hoja; columna izquierda fija (Campuslands); la derecha varía por proyecto.']],
              '1.8fr 5fr', tf='10pt',
              read=('Dentro del documento', 'Nunca aparece «borrador» ni «no apto para firma»: el estado vive en el chat, `wiki/index.md` y `05-control-calidad.md`')),
        table('convenciones', '~~Convenciones~~ que no cambian', ['Elemento', 'Convención'], [
            ['Identificadores', '`RF-001` requisitos · `MOD-01` módulos · `INT-01` integraciones · `DEC-001` decisiones · `PEN-001` pendientes. Estables entre versiones.'],
            ['Archivo de entrega', '`Alcance Funcional - <Cliente> - v<N.M> - <YYYY-MM-DD>.docx`; no se sobrescriben versiones.'],
            ['Estados en el índice', 'Borrador · Apto para revisión final · Aprobado por cliente. Nunca «listo para firma» con BLOQUEANTES.'],
            ['Slug de cliente', 'Minúsculas, sin espacios ni tildes, con guiones.'],
            ['Fechas', 'Absolutas (`2026-10-29`), nunca relativas.'],
            ['Versión', 'Solo en el nombre del archivo y en la wiki, jamás dentro del documento.']],
              '1.6fr 5fr', tf='9.5pt'),
        cmds('herramientas', '~~Scripts~~ y plantillas', [
            ('Vista previa', ['python scripts/previsualizar.py "<archivo.docx>" <carpeta>'], 'Genera PDF y un PNG por página (LibreOffice + pypdfium2); avisa de páginas con menos de 60 % de ocupación.'),
            ('Constructor', ['scripts/alcance_docx.py  ›  clase Alcance'], 'Portada, carta, tabla de contenido (se genera sola), fichas funcionales y firmas.'),
            ('Plantilla Word', ['recursos/plantilla/Plantilla Word - Campuslands.docx'], 'El documento se construye **siempre** sobre ella: membrete, márgenes y número de página.')]),
        checks('control de calidad', 'Manual §8: ~~nueve~~ puntos con evidencia', [
            ('Módulos completos', 'Identificador, límite, entradas, salidas y aceptación.'), ('Datos comerciales', 'Coinciden con la propuesta aprobada.'),
            ('Cronograma', 'Dependencias y condiciones de inicio.'), ('Fases futuras', 'No figuran como entregables actuales.'),
            ('Soporte y garantía', 'Distinguen errores de nuevas solicitudes.'), ('Costos recurrentes', 'Y de terceros, identificados o pendientes.'),
            ('Trazabilidad', 'Fuentes, decisiones y versiones.'), ('Sin contradicciones', 'Resumen, tablas, entregables y exclusiones.'),
            ('Estado declarado', 'Borrador o apto para revisión final.')],
               cols=3, read=('Gate', 'Solo después de esto se declara «apto para revisión final»; con BLOQUEANTES abiertos solo hay borrador')),
        faq('diagnóstico', 'Síntomas ~~frecuentes~~ y qué hacer', [
            ('Dos fuentes dicen cosas distintas', 'Se muestran ambas versiones y se listan en pendientes; no se elige la más reciente en silencio.'),
            ('Páginas casi vacías tras generar', '`previsualizar.py` avisa de las de menos de 60 %: recortar o reordenar. La hoja de firma puede quedar sola.'),
            ('Los números de la tabla de contenido difieren en Word', 'Salen de LibreOffice; en Word: clic derecho › Actualizar campo.'),
            ('Piden «listo para firma» con BLOQUEANTES', 'No se declara: se entrega borrador y lista de validaciones por responsable.')],
            fs='10pt'),
        close('Alcance claro, ~~compromisos~~ reales',
              ['Actualiza `wiki/index.md` y `log.md`.', 'Entrega documento, resumen y pendientes.', 'Pide revisión técnica, comercial y jurídica.'], 'Siguiente paso'),
    ]


def usuario():
    S = 'guía rápida'
    return [
        statement('qué hace', 'Tu analista de ~~alcances~~',
                  'Le das los **archivos de un proyecto** (propuestas, actas, cotizaciones, notas) y redacta el documento de alcance para el cliente, listo para revisar.',
                  '0', 'compromisos inventados:\nsolo lo que dicen\ntus archivos',
                  points=['Lee todo, detecta contradicciones y vacíos y redacta **de inmediato**.', 'Lo que no sabe queda marcado como pendiente, con responsable.', 'Entrega un Word editable, no un PDF cerrado.'], hs='32pt'),
        flow(S, 'Cómo se usa, ~~paso a paso~~', [
            ('folder', 'Deja tus archivos', 'En la carpeta del cliente, dentro de `fuentes/`.', 'Tú'),
            ('chat', 'Pide el alcance', 'Dile qué proyecto y qué documento necesitas.', 'Tú'),
            ('file', 'Él redacta', 'Analiza todo y escribe el borrador en el mismo momento.', 'Alcances'),
            ('list', 'Revisas pendientes', 'Lees el resumen y la lista de validaciones por responsable.', 'Tú')],
             read=('Sin entrevista', 'No te hará preguntas sobre lo que tus archivos no traen: lo deja marcado para validar')),
        prompts(S, 'Qué ~~escribirle~~: ejemplos', [
            ('Empezar', 'Tengo la propuesta y las actas del proyecto de la Alcaldía. Haz el alcance funcional.', 'Con los archivos ya en `fuentes/`.'),
            ('Ver lo pendiente', 'Dame la lista de pendientes bloqueantes y quién debe resolver cada uno.', 'Sale del archivo `03-pendientes.md`.'),
            ('Incorporar una decisión', 'El cliente confirmó que el soporte será de 8 a 5. Actualiza el documento.', 'Se registra como decisión y se actualiza todo.'),
            ('Nueva versión', 'Genera la v0.2 con estos cambios, sin borrar la v0.1.', 'Cada versión queda en su propio archivo.')],
                 fs='10.5pt'),
        cards(S, 'Qué ~~recibes~~', [
            ('file', 'El documento en Word', 'Portada, carta, tabla de contenido, secciones, anexos y hoja de firmas.', 'navy'),
            ('list', 'Resumen de cambios', 'Lo más importante que encontró, en pocas líneas.', ''),
            ('alert', 'Registro de pendientes', 'Cada duda, con su prioridad y quién debe resolverla.', ''),
            ('folder', 'Archivos de trabajo', 'Inventario, matriz y control de calidad, por si quieres revisar el método.', '')],
              cols=2, fs='11pt', fh='15pt'),
        cards(S, 'Los ~~tres estados~~ de todo dato', [
            ('checkc', 'CONFIRMADO', 'Hay una fuente o una aprobación que lo respalda.', 'navy'),
            ('bulb', 'PROPUESTO', 'Es una recomendación todavía no aceptada. No es un compromiso.', ''),
            ('help', 'PENDIENTE', 'Falta definirlo. Aparece como `[PENDIENTE DE VALIDACIÓN]`.', 'gold')],
              read=('Clave', 'Un documento con pendientes bloqueantes es un borrador: nunca se declara listo para firma')),
        checks(S, 'Cómo ~~revisar~~ el documento', [
            ('El orden es el esperado', 'Portada, carta, contenido y firmas.'),
            ('Los datos comerciales coinciden', 'Costo, plazo y condiciones frente a tu propuesta aprobada.'),
            ('Las contradicciones se ven', 'Si dos archivos chocan, el documento muestra ambas versiones.', 'warn'),
            ('Lo futuro no es entregable', 'Las ideas de fases siguientes van solo en «Fases futuras».'),
            ('Cada pendiente tiene responsable', 'Revisa que sean las personas correctas.'),
            ('Pasa revisión de tres áreas', 'Técnica, comercial y jurídica antes de enviarlo al cliente.')]),
        faq(S, 'Preguntas ~~frecuentes~~', [
            ('¿Por qué no me hace preguntas?', 'Porque tus archivos son todo lo que hay. Lo que falta queda pendiente en vez de adivinarse.'),
            ('¿Puedo editar el Word?', 'Sí, es editable. Para cambios grandes, pídele una versión nueva.'),
            ('¿Dónde aparece el número de versión?', 'Solo en el nombre del archivo, nunca dentro del documento.'),
            ('¿Cuándo queda «listo para firma»?', 'Cuando no haya pendientes bloqueantes y las tres áreas lo revisen.')]),
        close('¿Listo para ~~definir~~ el alcance?',
              ['Reúne los archivos del proyecto.', 'Pídele el alcance funcional.', 'Resuelve los pendientes con sus responsables.'], 'Siguiente paso'),
    ]
