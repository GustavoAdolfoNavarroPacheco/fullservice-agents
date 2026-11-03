# -*- coding: utf-8 -*-
"""Radar de Campus — prospection-agent (Perplexity). Fuente: Perplexity.md, habilidades/*, wiki/formulario-intake.md, wiki/perfil-usuario.md."""
from kit import *

META = dict(
    slug='prospection-agent', carpeta='prospection-agent', nombre='Radar de Campus', corto='radar de campus',
    rol='Prospección de empresas', icono='radar', paso='1', plataforma='Perplexity',
    resumen='Busca en la web abierta las empresas que encajan con el perfil de cliente de Campuslands y entrega un listado con datos públicos verificables.',
    tagline_dev='Instrucciones, habilidades, formatos y reglas del agente de prospección',
    tagline_usuario='Pídele empresas, recibe una tabla lista para usar',
)


def dev():
    S = 'ciclo de trabajo'
    return [
        statement('qué es', 'Prospección ~~a nivel empresa~~',
                  'Agente B2B que **busca, filtra y lista empresas** que califican como prospecto de Campuslands. Trabaja con cuentas, no con personas.',
                  '1.º', 'eslabón del pipeline:\nsu salida alimenta a\nExplorador de Campus',
                  points=['Corre como agente/Space de **Perplexity**: su `Perplexity.md` cumple el rol de un `CLAUDE.md`.',
                          'Fuentes: buscadores, prensa, directorios, gremios, Supersociedades y sitios corporativos. **Nunca LinkedIn.**',
                          'Cero invención: todo dato sale de una fuente consultada; si no, el campo queda vacío.'], hs='32pt'),
        versus('deslinde', 'Dónde ~~termina~~ este agente',
               dict(pill='Radar de Campus', h='Descubre cuentas', items=['Busca **empresas** en la web abierta', 'No usa LinkedIn ni Sales Navigator', 'No identifica personas ni cargos', 'No redacta mensajes', 'Entrega: tabla + `01-empresas-encontradas.csv`']),
               dict(pill='Explorador de Campus', h='Convierte cuentas en contactos', items=['Recibe el listado de empresas', 'Enriquece y busca **contactos** en LinkedIn', 'Clasifica por buyer persona', 'Redacta y envía conexiones', 'Entrega: `04-informe-divulgacion.csv`']),
               fs='10pt', read=('Regla', 'Si piden contactos, mensajes o LinkedIn aquí, el agente lo señala y sugiere pasar el listado a Explorador de Campus')),
        tree('arquitectura', 'Arquitectura de ~~carpetas~~', [
            (0, 'dir', 'prospection-agent/', ''),
            (1, 'file', 'Perplexity.md', 'identidad, decisiones, fases', 'agente'),
            (1, 'dir', 'habilidades/', '4 skills, un SKILL.md cada una'),
            (2, 'file', 'formulario-intake/', ''), (2, 'file', 'busqueda-web-empresas/', ''),
            (2, 'file', 'enriquecimiento-datos-empresa/', ''), (2, 'file', 'generacion-listado-resultados/', ''),
            (1, 'dir', 'prospeccion/', 'un lote por búsqueda'),
            (2, 'dir', '<slug-lote>/', ''), (3, 'file', '01-empresas-encontradas.csv', '', 'generado'),
            (1, 'dir', 'recursos/', 'marca Campuslands y brief', 'solo lectura'),
            (1, 'dir', 'wiki/', 'conocimiento que el agente mantiene'),
            (2, 'file', 'index.md · log.md', 'catálogo y bitácora'),
            (2, 'file', 'perfil-usuario.md', 'ICP y exclusiones'),
            (2, 'file', 'formulario-intake.md', 'los 6 campos'),
            (2, 'file', 'enlaces-utiles.md', 'fuentes y directorios'),
        ], [('file', '`Perplexity.md`, no `CLAUDE.md`', 'Mismo rol: es el archivo que se co-evoluciona con el usuario y se pega como instrucciones del Space.', 'navy'),
            ('folder', 'Un lote = una carpeta', 'Cada búsqueda guarda su CSV en `prospeccion/<slug-lote>/` sin pisar las anteriores.'),
            ('lock', '`recursos/` no se edita', 'Son fuentes que provee el usuario; el agente solo las lee.')]),
        flow(S, 'Tres fases, ~~tres habilidades~~', [
            ('list', 'Fase 1 · Intake', 'Skill `formulario-intake`: pide los 6 datos y **confirma el criterio** antes de buscar nada.', 'Siempre primero'),
            ('search', 'Fase 2 · Búsqueda', 'Skills `busqueda-web-empresas` y `enriquecimiento-datos-empresa`: candidatas + ubicación, empleados, facturación y utilidad, con fuente y fecha internas.', 'Guarda el CSV'),
            ('table', 'Fase 3 · Entrega', 'Skill `generacion-listado-resultados`: resumen inicial + tabla de 6 columnas + CSV, y pregunta si ampliar, repetir o pasar a Explorador.', 'Cierra el lote')],
             read=('Ciclo', 'Cada búsqueda nueva vuelve a la Fase 1; el formulario se repite aunque sea la misma sesión')),
        table('contrato de entrada', 'El formulario: ~~6 campos~~ fijos', ['Campo', 'Qué define', 'Ejemplo'], [
            ['1 · Número de Empresas', 'Meta del lote: cuántas filas debe tener la tabla. Si falta, se usa 10 y se avisa.', '20'],
            ['2 · Sector', 'Industria o vertical a buscar.', 'Constructor, Fintech'],
            ['3 · Ubicación', 'Ciudad (más país si hay ambigüedad) de sede u operación.', 'Bogotá'],
            ['4 · Tamaño', 'Categoría cualitativa.', 'Pequeña / Mediana / Grande'],
            ['5 · Número de empleados', 'Umbral cuantitativo, normalmente un piso.', '+100'],
            ['6 · Facturación anual', 'Piso de ingresos; COP si no se indica moneda.', '$5.000.000.000 o más']],
              '1.7fr 3.2fr 1.6fr', tf='9.5pt',
              read=('Flexible', 'Se preguntan siempre los 6, pero un «no sé» o «cualquiera» deja ese campo sin restricción: nunca bloquea la búsqueda')),
        table('contrato de salida', 'Salida: ~~CSV interno~~ y tabla entregada', ['Columna', 'En el CSV interno', 'En la tabla entregada', 'Regla'], [
            ['Fecha', 'Sí', 'Sí', 'Formato `YYYY-MM-DD`, fecha real de la búsqueda'],
            ['Razón Social', 'Sí', 'Sí', 'Nombre legal tal como figura en la fuente'],
            ['Ubicación', 'Sí', 'Sí', 'Ciudad de sede u operación'],
            ['Número de Empleados', 'Sí', 'Sí', 'Vacío si no hay fuente confiable'],
            ['Facturación Anual', 'Sí', 'Sí', 'Vacío si no hay fuente confiable'],
            ['Utilidad Neta', 'Sí', 'Sí', 'Vacío si no hay fuente confiable'],
            ['Fuente', 'Sí', 'No', 'En la tabla va aparte, como **pie de tabla** para trazabilidad']],
              '1.5fr 1.5fr 1.1fr 3.2fr', tf='9.5pt'),
        rules('reglas duras', 'Seis reglas ~~no negociables~~', [
            ('Solo web abierta', 'Prohibido LinkedIn y Sales Navigator: esa función es de Explorador de Campus.'),
            ('Nivel empresa', 'Nunca nombres de personas ni cargos: eso es la Fase 2 del otro agente.'),
            ('Cero invención', 'Cada dato lleva fuente y fecha. Sin confianza razonable: campo vacío y se anota qué se intentó.'),
            ('Formulario flexible', 'Se piden los 6 campos; un dato desconocido no frena el flujo.'),
            ('Exclusiones del ICP', 'Fuera: gobierno, ONGs, colegios y universidades, agencias de staffing o reclutamiento.'),
            ('Español', 'Comunicación y documentación en español; las fuentes pueden quedar en su idioma.')],
              fs='9.5pt', read=('ICP', 'Perfil ideal por defecto: 50–500 empleados, empresa privada, con señales de crecimiento o vacantes técnicas')),
        cards('calidad', 'Cómo se ~~verifica~~ un lote', [
            ('target', 'Cantidad', 'Empresas encontradas frente a las solicitadas: el resumen inicial debe decir ambas cifras.', ''),
            ('shield', 'Trazabilidad', 'Cada celda de cifra tiene fuente y fecha en el CSV. Sin fuente no hay dato.', 'navy'),
            ('users', 'Encaje con el ICP', 'Sector, ciudad, tamaño y exclusiones coinciden con el formulario confirmado.', ''),
            ('alert', 'Contradicciones', 'Si Tamaño y empleados chocan («Grande» con +10), se pregunta cuál priorizar; no se asume.', ''),
            ('file', 'Formato', 'Tabla con exactamente las 6 columnas y la fecha en `YYYY-MM-DD`.', ''),
            ('refresh', 'Duplicados', 'Una empresa aparece una sola vez por lote.', '')],
              fs='10pt', row=True, read=('Control', 'No hay script automático: la verificación es la lista anterior, aplicada en cada entrega')),
        checks('cómo modificarlo', 'Al ~~cambiar~~ el agente, tocar todo esto', [
            ('Agregar un campo al formulario', 'Actualizar `Perplexity.md`, `wiki/formulario-intake.md` y la skill `formulario-intake`.'),
            ('Agregar una columna al listado', 'Cambiar CSV y tabla en `Perplexity.md` y en la skill `generacion-listado-resultados`.'),
            ('Cambiar el ICP o las exclusiones', 'Editar `wiki/perfil-usuario.md`; lo leen las skills de búsqueda y enriquecimiento.'),
            ('Sumar o quitar una fuente', 'Editar `wiki/enlaces-utiles.md` y revisar enlaces rotos en el lint.'),
            ('Regla nueva del usuario', 'Va en `Perplexity.md` y en su página de wiki, en el mismo cambio.'),
            ('Registrar el cambio', 'Entrada en `wiki/log.md`: `## [YYYY-MM-DD] <tipo> | <descripción>`.')],
               read=('Tipos de bitácora', 'setup · busqueda · enriquecimiento · entrega · lint')),
        faq('diagnóstico', 'Síntomas ~~frecuentes~~ y qué hacer', [
            ('La tabla trae menos empresas de las pedidas', 'Es esperable con criterios estrechos. El agente reporta encontradas vs. solicitadas y ofrece ampliar o relajar un criterio.'),
            ('Facturación o utilidad vacías', 'No es un fallo: no hubo fuente confiable. Revisar el CSV (columna Fuente) para ver qué se intentó.'),
            ('Piden contactos o mensajes', 'Fuera de alcance. Pasar el listado a Explorador de Campus (`intelligence-commercial/`).'),
            ('El agente repite el formulario', 'Es por diseño: cada búsqueda nueva reinicia en la Fase 1, aunque sea la misma sesión.')],
            fs='10pt'),
        close('Del ~~radar~~ al contacto',
              ['Mantén `Perplexity.md` y la wiki sincronizadas.', 'Registra cada cambio en `wiki/log.md`.', 'Entrega el listado a Explorador de Campus.'], 'Siguiente paso'),
    ]


def usuario():
    S = 'guía rápida'
    return [
        statement('qué hace', 'Tu ~~radar~~ de empresas',
                  'Le dices **qué tipo de empresas buscas** y te devuelve una lista ordenada, con datos públicos y la fecha de la búsqueda.',
                  '6 datos', 'es todo lo que\nnecesita para empezar',
                  points=['Busca solo en internet público; **no usa LinkedIn**.', 'Cada cifra viene de una fuente. Si no la encuentra, deja la casilla vacía.', 'Es el primer paso: tu lista sirve luego al Explorador de Campus.'], hs='34pt'),
        cards(S, 'Los ~~6 datos~~ que te pide', [
            ('list', 'Número de empresas', '¿Cuántas quieres en la lista? Si no dices, trae 10.', ''),
            ('building', 'Sector', 'Tipo de negocio. Ej.: constructoras, software, fintech.', 'navy'),
            ('pin', 'Ubicación', 'La ciudad donde deben tener sede u operación. Ej.: Bogotá.', ''),
            ('layers', 'Tamaño', 'Pequeña, mediana o grande.', ''),
            ('users', 'Número de empleados', 'Normalmente un mínimo. Ej.: más de 100.', ''),
            ('dollar', 'Facturación anual', 'Normalmente un mínimo. Ej.: $5.000.000.000 o más.', '')],
              read=('Tranquilo', 'Si no sabes un dato, escribe «no sé» o «cualquiera». La búsqueda sigue igual')),
        flow(S, 'Cómo se usa, ~~paso a paso~~', [
            ('chat', 'Abre el agente', 'Entra al Space de Radar de Campus en Perplexity y saluda.', 'Tú'),
            ('list', 'Responde el formulario', 'Contesta los 6 datos, uno por uno o todos en un solo mensaje.', 'Tú'),
            ('checkc', 'Confirma el resumen', 'Radar te repite lo que entendió. Si está bien, dile que sí.', 'Tú y Radar'),
            ('table', 'Recibe tu tabla', 'Te entrega la lista y te pregunta si amplías, repites o la pasas al Explorador.', 'Radar')],
             read=('Tiempo', 'Si tu primer mensaje ya trae los 6 datos, Radar no repite las preguntas: confirma y busca')),
        prompts(S, 'Qué ~~escribirle~~: ejemplos', [
            ('Todo en un mensaje', 'Necesito empresas constructoras en Bogotá, medianas, con más de 100 empleados y facturación de $5.000.000.000 o más. Dame 15.', 'Radar entiende los 6 datos y empieza.'),
            ('Con datos que no sabes', 'Busca 10 empresas de software en Medellín. El tamaño y la facturación no me importan.', 'Esos dos filtros quedan «sin restricción».'),
            ('Una búsqueda nueva', 'Ahora quiero 20 fintech en Bogotá con más de 50 empleados.', 'Vuelve a pedirte el formulario: es lo normal.'),
            ('Ampliar la lista', 'Amplía la búsqueda anterior con 10 empresas más del mismo sector.', 'Respeta los criterios que ya confirmaste.')],
                 fs='10.5pt'),
        cards(S, 'Qué ~~recibes~~', [
            ('table', 'Una tabla en el chat', 'Fecha, razón social, ubicación, empleados, facturación anual y utilidad neta.', 'navy'),
            ('sheet', 'Un archivo CSV', 'La misma lista en `01-empresas-encontradas.csv`, que se abre en Excel.', ''),
            ('list', 'Un resumen al inicio', 'Qué pediste, cuántas empresas encontró frente a las que pediste y la fecha.', ''),
            ('link', 'Las fuentes', 'Al pie de la tabla queda de dónde salió cada dato, para que puedas comprobarlo.', '')],
              cols=2, fs='11pt', fh='15pt'),
        checks(S, 'Cómo ~~revisar~~ tu lista', [
            ('¿Son del sector y la ciudad que pediste?', 'Si alguna no cuadra, avísale y la quita.'),
            ('¿Los números tienen sentido?', 'Empleados y facturación deben parecerse a lo que esperabas.'),
            ('Los vacíos son normales', 'Significa que no encontró un dato confiable. Prefiere vacío a inventar.', 'warn'),
            ('¿Hay empresas que no van?', 'Gobierno, ONGs, colegios o agencias de reclutamiento no se listan: avísale si ves una.'),
            ('¿Llegó al número pedido?', 'Si trajo menos, te lo dice y puedes pedir que amplíe.'),
            ('¿Cada dato tiene fuente y fecha?', 'Mira el pie de la tabla.')],
               read=('Tu decisión', 'Tú decides qué empresas pasan a la siguiente etapa; Radar solo propone')),
        versus(S, 'Qué ~~sí~~ y qué no hace',
               dict(pill='Sí hace', h='Lo que puedes pedirle', items=['Buscar empresas en la web abierta', 'Completar ubicación, empleados y cifras', 'Entregarte tabla y archivo CSV', 'Ampliar o repetir con otros criterios']),
               dict(pill='No hace', h='Lo que no le pidas', items=['Buscar personas o contactos', 'Escribir mensajes', 'Entrar a LinkedIn', 'Inventar cifras que no encuentre'], no=True),
               arrow=False, fs='12.5pt'),
        faq(S, 'Preguntas ~~frecuentes~~', [
            ('¿Y si no sé la facturación?', 'Escribe «no sé» o «cualquiera». Sigue sin ese filtro.'),
            ('¿Por qué hay casillas vacías?', 'No encontró un dato confiable. Es mejor vacío que un número inventado.'),
            ('¿Me da contactos de las empresas?', 'No. Pasa tu lista al Explorador de Campus, que se encarga de eso.'),
            ('¿Cuántas empresas trae?', 'Las que pidas. Si no dices un número, trae 10 y te lo avisa.')]),
        close('¿Listo para ~~buscar~~?',
              ['Piensa sector, ciudad y tamaño.', 'Escríbele a Radar de Campus.', 'Pasa tu lista a Explorador de Campus.'], 'Siguiente paso'),
    ]
