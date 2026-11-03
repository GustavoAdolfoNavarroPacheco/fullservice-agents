# -*- coding: utf-8 -*-
"""Explorador de Campus — intelligence-commercial (Perplexity). Fuente: Perplexity.md, habilidades/*, wiki/perfiles-objetivo.md."""
from kit import *

META = dict(
    slug='intelligence-commercial', carpeta='intelligence-commercial', nombre='Explorador de Campus', corto='explorador de campus',
    rol='Inteligencia comercial en LinkedIn', icono='compass', paso='2', plataforma='Perplexity',
    resumen='Toma una lista de empresas, encuentra a los contactos clave de cada una y les envía solicitudes de conexión personalizadas en LinkedIn.',
    tagline_dev='Fases, habilidades, CSV y salvaguardas de la prospección en LinkedIn',
    tagline_usuario='De una lista de empresas a conversaciones iniciadas',
)


def dev():
    return [
        statement('qué es', 'Inteligencia comercial ~~outbound~~',
                  'Enriquece una lista de empresas, identifica **contactos clave** y redacta y **envía de forma autónoma** solicitudes de conexión personalizadas en LinkedIn.',
                  '4', 'fases y 4 CSV\npor cada lote',
                  points=['Corre en **Perplexity** con control de navegador; sus instrucciones viven en `Perplexity.md`.',
                          'Recibe el listado de Radar de Campus (`prospection-agent/`).',
                          'El mensaje se escribe en el **idioma real del perfil**, no por traducción mecánica.'], hs='32pt'),
        tree('arquitectura', 'Arquitectura de ~~carpetas~~', [
            (0, 'dir', 'intelligence-commercial/', ''),
            (1, 'file', 'Perplexity.md', 'identidad, decisiones, fases, CSV', 'agente'),
            (1, 'dir', 'habilidades/', '4 skills'),
            (2, 'file', 'control-navegador-linkedin/', 'buscar, verificar, conectar'),
            (2, 'file', 'deteccion-idioma/', 'inglés o español'),
            (2, 'file', 'generacion-mensajes-personalizados/', ''),
            (2, 'file', 'generacion-tabla-registro/', ''),
            (1, 'dir', 'prospeccion/<slug-lote>/', 'un lote por carpeta'),
            (2, 'file', '01 a 04: los cuatro CSV del lote', '', 'generado'),
            (1, 'dir', 'recursos/', 'marca Campuslands y brief', 'solo lectura'),
            (1, 'dir', 'wiki/', ''),
            (2, 'file', 'perfil-usuario.md · marca-campuslands.md', 'audiencia y tono'),
            (2, 'file', 'perfiles-objetivo.md · filtros-busqueda.md', 'buyer personas y filtros'),
            (2, 'file', 'index.md · log.md', 'catálogo y bitácora'),
        ], [('file', 'Un lote, cuatro CSV', 'Numerados 01–04: cada fase deja su archivo y el siguiente lo consume.', 'navy'),
            ('folder', '`recursos/` no se edita', 'Marca y brief son fuentes del usuario.'),
            ('users', 'Wiki = criterio', '`perfiles-objetivo.md` decide a quién se contacta; `marca-campuslands.md`, cómo se le habla.')]),
        flow('ciclo de trabajo', 'Cuatro fases, ~~cuatro CSV~~', [
            ('db', 'Enriquecer', 'Sitio web, empleados, ingresos, utilidades públicas, sector y país.', 'CSV 01'),
            ('target', 'Clasificar', 'Agrupa por sector y país y filtra contactos de los 5 perfiles.', 'CSV 02'),
            ('send', 'Conectar', 'Revisa el perfil, detecta idioma, redacta y envía con nota.', 'CSV 03'),
            ('table', 'Informar', 'Actualiza el informe con la fecha real de envío.', 'CSV 04')],
             read=('Contrato', 'Cada fase solo corre si la anterior dejó su CSV; un dato firmográfico sin fuente se deja en blanco con la fuente consultada')),
        table('contrato de datos', 'Columnas de ~~cada CSV~~', ['Archivo', 'Columnas'], [
            ['01-empresas-enriquecidas', 'Empresa · Sitio Web · Empleados · Ingresos Estimados · Utilidades · Sector · País Sede · Fuente/Fecha'],
            ['02-contactos-clasificados', 'Empresa · Sector · País · Nombre · Cargo · URL Perfil'],
            ['03-mensajes-conexion', 'Empresa · Nombre · Cargo · Idioma Detectado · Mensaje'],
            ['04-informe-divulgacion', 'Fecha (AAAA-MM-DD) · Empresa · Contacto (Nombre) · Cargo (Título) · Mensaje Personalizado Redactado']],
              '1.6fr 4.4fr', tf='10pt',
              read=('Entrega final', 'El archivo 04 es el formato de entrega: la columna Fecha usa la fecha real de ejecución o envío')),
        flow('habilidades', 'Fase 3 por dentro: ~~cinco pasos~~', [
            ('eye', 'Verificar', '`control-navegador-linkedin` abre el perfil y revisa cargo, empresa y publicaciones.', 'Skill 1'),
            ('globe', 'Detectar idioma', '`deteccion-idioma`: obligatoria; ningún mensaje se redacta sin ella.', 'Skill 2'),
            ('pen', 'Redactar', '`generacion-mensajes-personalizados` adapta la plantilla base ES/EN al contacto.', 'Skill 3'),
            ('send', 'Enviar', 'De vuelta en `control-navegador-linkedin`: pega la nota y pulsa «Conectar».', 'Skill 1'),
            ('table', 'Registrar', '`generacion-tabla-registro` anota cada envío confirmado.', 'Skill 4')],
             read=('Orden', 'Verificar › idioma › redactar › enviar › registrar, perfil por perfil y en lotes pequeños')),
        table('buyer personas', 'A quién se contacta: ~~5 perfiles~~', ['Perfil', 'Por qué importa a Campuslands'], [
            ['Reclutadores técnicos', 'Gestionan la contratación de perfiles de desarrollo; primer contacto natural.'],
            ['Vicepresidente de Ingeniería', 'Dueño del roadmap técnico y del presupuesto de equipos.'],
            ['CTO (Director de Tecnología)', 'Decisor final en iniciativas tecnológicas y de IA.'],
            ['Líderes de IA', 'Llevan proyectos de IA de piloto a producción: el gancho de la plantilla.'],
            ['Gerentes de contratación tecnológica', 'Puente entre RR. HH. y las áreas técnicas; deciden volumen y perfil.']],
              '2fr 4fr', tf='10pt',
              read=('Criterio', 'Se prioriza el cargo exacto sobre el título genérico; un contacto no se duplica entre perfiles y quien no calza no se procesa')),
        rules('reglas duras', 'Decisiones ~~fundacionales~~', [
            ('Envío autónomo', 'Envía las solicitudes sin aprobación previa por contacto ni por lote (decisión del usuario).'),
            ('Sin ráfagas', 'Lotes pequeños con pausas automáticas: LinkedIn puede suspender cuentas con patrones de automatización.'),
            ('Mouse y teclado acotados', 'Solo navegar, verificar perfiles y pulsar «Conectar». Nunca credenciales ni CAPTCHA.'),
            ('Cero invención', 'Los datos firmográficos salen de una fuente; si no, en blanco con fuente y fecha.'),
            ('Idioma detectado', 'Se escribe en el idioma real del perfil y de sus publicaciones recientes.'),
            ('Español de trabajo', 'Comunicación y documentación en español; el mensaje puede salir en inglés.')],
              fs='9.5pt', tones=['navy', '', '', '', '', '']),
        checks('protección de la cuenta', 'Antes de ~~cada lote~~', [
            ('Tamaño de lote respetado', 'Nunca recorrer toda la lista de resultados de golpe.'),
            ('Pausas automáticas activas', 'No omitirlas entre envíos: protegen la reputación de la cuenta.'),
            ('Sesión iniciada por el usuario', 'El agente no escribe contraseñas ni resuelve CAPTCHA.'),
            ('Contactos dentro de los 5 perfiles', 'Los demás no pasan a la Fase 3.'),
            ('Idioma detectado antes de redactar', 'Sin etiqueta de idioma no hay mensaje.'),
            ('Registro al día', 'Cada envío confirmado queda en la tabla de registro.')],
               read=('Prioridad', 'Proteger la cuenta de LinkedIn del usuario va por encima de la velocidad')),
        checks('cómo modificarlo', 'Al ~~cambiar~~ el agente, tocar todo esto', [
            ('Cambiar la plantilla de mensaje', '`Perplexity.md` (Fase 3), skill de mensajes y `wiki/marca-campuslands.md`.'),
            ('Agregar un buyer persona', '`wiki/perfiles-objetivo.md`, `wiki/filtros-busqueda.md` y la Fase 2 de `Perplexity.md`.'),
            ('Cambiar columnas de un CSV', '`Perplexity.md` y la skill que lo escribe.'),
            ('Agregar un idioma', 'Skill `deteccion-idioma` y la skill de mensajes.'),
            ('Regla nueva del usuario', 'En `Perplexity.md` y su página de wiki, en el mismo cambio.'),
            ('Registrar el cambio', '`wiki/log.md` con tipo: setup · enriquecimiento · clasificacion · redaccion · envio · lint.')]),
        faq('diagnóstico', 'Síntomas ~~frecuentes~~ y qué hacer', [
            ('LinkedIn pide verificación o CAPTCHA', 'El agente se detiene: no resuelve bot-detection. Lo resuelve el usuario y se retoma el lote.'),
            ('Un contacto no calza con los 5 perfiles', 'No se procesa en Fase 3, aunque aparezca en la búsqueda inicial.'),
            ('El mensaje salió en el idioma equivocado', 'Revisar la skill `deteccion-idioma`: la etiqueta se decide con perfil y publicaciones.'),
            ('Piden más velocidad', 'No: los lotes pequeños y las pausas son una decisión fundacional, no un ajuste.')],
            fs='10pt'),
        close('De la lista al ~~diálogo~~',
              ['Mantén `Perplexity.md` y la wiki sincronizadas.', 'Revisa el CSV 04 tras cada lote.', 'Registra todo en `wiki/log.md`.'], 'Siguiente paso'),
    ]


def usuario():
    S = 'guía rápida'
    return [
        statement('qué hace', 'Tu explorador de ~~contactos~~',
                  'Le das una **lista de empresas**; él encuentra a las personas indicadas en cada una y les envía una invitación de LinkedIn escrita a su medida.',
                  '5', 'tipos de contacto\nque busca en cada empresa',
                  points=['Detecta si la persona escribe en inglés o español y se lo escribe así.', 'Envía **sin pedirte permiso por cada mensaje**: revisa antes la plantilla.', 'Al final te entrega un informe de todo lo enviado.'], hs='32pt'),
        cards(S, '~~A quién~~ busca en cada empresa', [
            ('users', 'Reclutadores técnicos', 'Quienes contratan perfiles de desarrollo.', ''),
            ('layers', 'VP de Ingeniería', 'Dueños del plan técnico y del presupuesto de equipos.', 'navy'),
            ('cpu', 'CTO', 'Directores de tecnología que deciden iniciativas de IA y software.', ''),
            ('bot', 'Líderes de IA', 'Quienes llevan la IA de piloto a producción.', ''),
            ('brief', 'Gerentes de contratación técnica', 'El puente entre Recursos Humanos y las áreas técnicas.', ''),
            ('ban', 'Otros cargos', 'No los contacta, aunque aparezcan en la búsqueda.', 'sand')],
              fs='10pt', row=True, read=('Sin repetir', 'Una misma persona no se contacta dos veces ni cuenta en dos perfiles')),
        flow(S, 'Cómo se usa, ~~paso a paso~~', [
            ('list', 'Dale tu lista', 'Las empresas que te entregó Radar de Campus, o las tuyas.', 'Tú'),
            ('search', 'Él investiga', 'Completa datos de cada empresa y elige a los contactos correctos.', 'Explorador'),
            ('send', 'Escribe y envía', 'En lotes pequeños y con pausas, para cuidar tu cuenta de LinkedIn.', 'Explorador'),
            ('table', 'Recibes el informe', 'Fecha, empresa, contacto, cargo y mensaje enviado.', 'Explorador')],
             read=('Tu cuenta', 'Tú inicias sesión en LinkedIn: el agente nunca escribe contraseñas ni resuelve verificaciones')),
        prompts(S, 'Qué ~~escribirle~~: ejemplos', [
            ('Empezar', 'Aquí está el listado de empresas de Radar de Campus. Enriquécelo, busca los contactos y conéctate con ellos.', 'Corre las cuatro fases en orden.'),
            ('Solo preparar', 'Enriquece estas 10 empresas y muéstrame los contactos que elegiste.', 'Útil si quieres mirar antes de enviar.'),
            ('Pedir el informe', 'Dame el informe de divulgación con todo lo enviado hasta ahora.', 'Entrega el archivo 04 con fechas reales.'),
            ('Ajustar el tono', 'El mensaje suena muy comercial. Hazlo más directo y entre pares.', 'La plantilla base ya es conversacional.')],
                 fs='10.5pt'),
        prompts(S, 'Así suena el ~~mensaje~~', [
            ('Plantilla en español', 'Hola [Nombre], vi tu enfoque en llevar IA de piloto a producción. En Campuslands ayudamos a equipos a escalar con desarrolladores y talento técnico para iniciativas de IA. ¿Valdría la pena una breve charla, o hay alguien más en [Compañía] manejando la contratación técnica?'),
            ('Plantilla en inglés', 'Hi [Nombre], noticed you\'re focused on taking AI from pilot to production. Campuslands helps teams scale with developers and technical talent for AI initiatives. Worth a quick chat, or is someone else at [Compañía] handling technical hiring?')],
                 cols=1, fs='10.5pt', read=('Se adapta', 'Cada mensaje se ajusta al rol, la empresa y, si aplica, una publicación reciente de la persona')),
        checks(S, 'Antes de ~~empezar~~', [
            ('Tengo mi lista de empresas', 'Nombres claros; mejor si vienen de Radar de Campus.'),
            ('Inicié sesión en LinkedIn', 'Lo hago yo. El agente no maneja contraseñas.'),
            ('Leí la plantilla del mensaje', 'Sale sin pedirte aprobación por contacto.', 'warn'),
            ('Sé que va por lotes', 'Es lento a propósito: protege tu cuenta.'),
            ('Sé dónde queda el informe', '`prospeccion/<lote>/04-informe-divulgacion.csv`.'),
            ('Revisaré el informe al final', 'Ahí ves a quién se escribió y qué se envió.')]),
        versus(S, 'Qué ~~sí~~ y qué no hace',
               dict(pill='Sí hace', h='Lo que puedes pedirle', items=['Completar datos de cada empresa', 'Elegir los contactos adecuados', 'Escribir en el idioma de cada persona', 'Enviar y registrar las invitaciones']),
               dict(pill='No hace', h='Lo que no le pidas', items=['Enviar miles de solicitudes de golpe', 'Escribir tu contraseña o resolver CAPTCHA', 'Inventar cifras de las empresas', 'Buscar empresas nuevas (eso es Radar)'], no=True),
               arrow=False, fs='12.5pt'),
        faq(S, 'Preguntas ~~frecuentes~~', [
            ('¿Por qué va tan despacio?', 'Envía en lotes pequeños con pausas. LinkedIn puede suspender cuentas que actúan como robot.'),
            ('¿Me pide permiso antes de enviar?', 'No. Por eso conviene revisar antes la plantilla del mensaje.'),
            ('LinkedIn me pidió verificar mi identidad', 'Hazlo tú mismo; el agente no puede hacerlo y se detiene hasta que sigas.'),
            ('¿Dónde veo lo enviado?', 'En el informe final: fecha, empresa, contacto, cargo y mensaje.')]),
        close('¿Listo para ~~conectar~~?',
              ['Ten tu lista de empresas.', 'Entra a LinkedIn con tu cuenta.', 'Pídele el informe al terminar.'], 'Siguiente paso'),
    ]
