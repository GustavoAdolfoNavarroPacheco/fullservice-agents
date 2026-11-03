# -*- coding: utf-8 -*-
"""Desarrollador de Cotizaciones — quote-developer-v2 (Claude Code). Fuente: CLAUDE.md, wiki/*.md, wiki/log.md."""
from kit import *

META = dict(
    slug='quote-developer-v2', carpeta='quote-developer-v2', nombre='Desarrollador de Cotizaciones', corto='cotizaciones',
    rol='Cotizaciones: PDF de alcance + XLSX', icono='calc', paso='5', plataforma='Claude Code',
    resumen='A partir de los alcances de un proyecto genera el PDF de cotización de alcance y llena la plantilla XLSX de costos del equipo Campus.',
    tagline_dev='Jerarquía L/M/N, plantilla XLSX, PDF y verificación de la cotización',
    tagline_usuario='De los alcances de tu proyecto a un PDF y un Excel de cotización',
)


def dev():
    return [
        statement('qué es', 'Del alcance al ~~precio~~',
                  'Agente que, a partir de los **alcances** de un proyecto, produce un **PDF de cotización de alcance** y llena el **XLSX** estipulado por el equipo de Campus.',
                  '2', 'entregables que deben\ncontar el mismo alcance:\nPDF + XLSX',
                  points=['**Nunca inventa alcance:** toda la información técnica sale de lo que el usuario comparte; ante la duda, pregunta.',
                          'La plantilla XLSX trae las fórmulas montadas por Campus: el agente **solo rellena celdas de datos permitidas**.',
                          'Esta es la versión vigente; `quote-developer/` queda como legado (patrón antiguo de 1 submódulo = 1 funcionalidad).'], hs='32pt'),
        tree('arquitectura', 'Arquitectura de ~~carpetas~~', [
            (0, 'dir', 'quote-developer-v2/', ''),
            (1, 'file', 'CLAUDE.md', 'rol, reglas del PDF y del XLSX', 'agente'),
            (1, 'dir', 'wiki/', 'index · log · perfil-usuario · marca-campuslands · diseno-pdf-cotizacion · plantilla-xlsx'),
            (1, 'dir', 'cotizaciones/', 'una carpeta por cliente'),
            (2, 'dir', '<slug-cliente>/<slug-proyecto>/', 'ruta corta (< ~180 caracteres)'),
            (3, 'file', 'Cotizacion de Alcance.pdf', '', 'generado'),
            (3, 'file', 'Cotizacion.xlsx', 'copia de la plantilla maestra', 'generado'),
            (1, 'dir', 'recursos/', '', 'solo lectura'),
            (2, 'file', 'FullServices - Plantilla Cotizaciones.xlsx', 'plantilla maestra: nunca se edita'),
            (2, 'file', 'Logos, brief y brandbook', 'el PDF usa el logo horizontal azul'),
        ], [('sheet', 'Siempre sobre una copia', 'La plantilla maestra no se toca: cada cliente trabaja en `Cotizacion.xlsx`.', 'navy'),
            ('folder', 'Nomenclatura corta', 'Excel falla con rutas largas; el nombre del cliente ya está en la carpeta.'),
            ('history', '`quote-developer/` es legado', 'Congelado en julio de 2026; la jerarquía flexible vive solo aquí.')]),
        flow('ciclo de trabajo', 'Del alcance a la ~~entrega~~', [
            ('inbox', 'Recibir', 'Alcances + razón social. Si hay ambigüedad, pregunta antes de seguir.', 'Sin asumir'),
            ('file', 'PDF de alcance', 'Por módulos, submódulos y funcionalidades, con «Pendiente de costear».', 'Se valida'),
            ('sheet', 'Llenar XLSX', 'Solo L/M/N, días B:K y las dos celdas permitidas.', ''),
            ('refresh', 'Recalcular', 'Recalcula y reescribe el PDF con los precios reales leídos del XLSX.', ''),
            ('shield', 'Verificar y entregar', 'PDF = XLSX, cero errores, wiki y log al día.', 'Gate')],
             read=('Orden', 'El PDF se valida con el usuario antes de llenar el XLSX; los precios solo entran al PDF cuando el XLSX está recalculado')),
        table('jerarquía', 'La jerarquía ~~L / M / N~~', ['Columna', 'Nivel', 'Contenido', 'Cardinalidad'], [
            ['L', 'Módulo', '`NOMBRE - descripción breve`, en una sola celda', 'Una fila por módulo'],
            ['M', 'Submódulo', 'Encabezado de agrupación temática; **sin días propios**', 'Varios por módulo'],
            ['N', 'Funcionalidad', 'Frase autocontenida de **una** capacidad atómica, con sus días en B:K', 'Varias por submódulo (mínimo 1)'],
            ['PDF', 'Espejo exacto', 'Módulo › Submódulo › Funcionalidad › Valor (COP)', 'Nunca más ni menos detalle que el XLSX']],
              '0.8fr 1.2fr 3.4fr 2fr', tf='10pt',
              read=('Veracidad', 'Prohibido agrupar funcionalidades para ahorrar espacio y fragmentar una sola para aparentar detalle')),
        table('especialidades', 'Días por ~~especialidad~~ (B:K)', ['Col', 'Código', 'Especialidad'], [
            ['B', 'DB', 'DB, Líder, Arquitecto, Scrum'], ['C', 'UX', 'Diseño UI/UX'], ['D', 'FM', 'FrontEnd Medium'],
            ['E', 'BS', 'BackEnd Senior'], ['F', 'BM', 'BackEnd Semi-Senior'], ['G', 'QA', 'QA, Test'],
            ['H', 'IM', 'Implementación, Capacitación'], ['I', 'MS', 'Mobile Semi-Senior'], ['J', 'MM', 'Mobile Medium'], ['K', 'IA', 'BackEnd IA']],
              '0.6fr 0.8fr 4fr', tf='9.5pt'),
        table('zonas de la plantilla', 'Qué se llena y qué es ~~intocable~~', ['Zona', 'Regla'], [
            ['Filas 2–5', 'Transversales fijas (Estructura, UX, Implementación y entrega, Agente IA): **siempre** llevan días, estimados por tamaño del proyecto.'],
            ['Filas 6–7', 'Quedan siempre vacías; el desglose del cliente empieza en la fila 8.'],
            ['Columnas A y O:AC, filas 121–140', 'Fórmulas, checkboxes y tabla de costos: no se tocan.'],
            ['`Y{barra gris + 2}`', 'Fórmula `=Y1/0.6` (en la plantilla maestra, `Y122`).'],
            ['`R{barra gris + 3}`', 'Valor `0.1` (AIU 10 %); se confirma por la etiqueta `AIU` en Q.'],
            ['Más filas de las previstas', 'Se **insertan** filas y se verifica que A/X/Y/AB/AC se propaguen.']],
              '2fr 5fr', tf='9.5pt'),
        rules('reglas', 'Reglas de ~~estimación~~ y llenado', [
            ('Cero invención', 'El PDF solo contiene lo que el usuario dio o confirmó.'),
            ('Piso de 0.5 días', 'Menos de 0.5 se redondea a 0.5; por encima, decimales realistas.'),
            ('Días solo en N', 'Cada funcionalidad con su estimado propio; nunca repartir ni promediar.'),
            ('Solo especialidades que participan', 'Las demás celdas quedan vacías, no en 0.'),
            ('Atomicidad', 'Un bullet con «y»/comas se divide solo si son capacidades distintas.'),
            ('Precios leídos, no escritos', 'Se leen con `data_only=True` del XLSX recalculado.'),
            ('No sobrescribir en conflicto', 'Si una celda permitida ya tiene datos reales, se reporta.'),
            ('Estimar como desarrollador', 'Complejidad, integraciones y alcance; nunca un valor genérico.')],
              fs='9pt', tones=['navy', '', '', '', '', '', '', '']),
        cards('el PDF', 'Diseño del ~~PDF~~ de cotización', [
            ('palette', 'Paleta clara de marca', 'Azul `#152F5E`, azul cielo `#418BF3` y blanco; módulos en grid con líneas finas.', ''),
            ('table', 'Tabla de 3 columnas', 'Módulo / Submódulo · Detalle técnico · Valor (COP).', 'navy'),
            ('pen', 'Arial en 3 pesos', 'Módulo 11 pt negrita · Submódulo 10 pt negrita · Funcionalidad 10 pt regular.', ''),
            ('image', 'Logo horizontal azul', 'Arriba a la izquierda, sobre el fondo claro.', ''),
            ('file', 'Nota de contexto técnico', 'Si la fuente trae componente tecnológico o clasificación: nota en cursiva gris, sin precio.', ''),
            ('dollar', 'Precios reales', 'Por funcionalidad y por módulo; el submódulo no lleva precio.', '')],
              fs='9.5pt', row=True),
        checks('verificación', 'Verificación ~~obligatoria~~', [
            ('Recalculo sin errores', 'Con `recalc.py`; solo `A140:A144` (`#NAME?` de `UNIQUE`) es preexistente.'),
            ('PDF y XLSX cuentan lo mismo', 'Ningún módulo, submódulo ni funcionalidad de más o de menos.'),
            ('Días válidos', 'Ninguno menor a 0.5 ni en celda equivocada; ningún submódulo con días.'),
            ('`Y{barra+2}` y `R{barra+3}`', 'Fórmula `=Y1/0.6` calculando número y AIU en `0.1`.'),
            ('Precios del PDF = XLSX', 'Cada línea coincide con su celda de origen.'),
            ('Subtotales y total', 'La suma por módulo y el total general cuadran con el XLSX.')],
               read=('Doble verificación', 'Las diferencias de $1 por redondeo se anotan en el PDF; nunca se ajustan a mano')),
        faq('diagnóstico', 'Síntomas ~~frecuentes~~ y qué hacer', [
            ('`#NAME?` en `A140:A144`', 'Es de la plantilla maestra: `UNIQUE()` no lo soporta LibreOffice. No lo introdujo el llenado.'),
            ('`CLAUDE.md` cita archivos que no existen', '`scripts/recalc.py` y `wiki/flujo-trabajo.md` no están en esta carpeta (deuda conocida): `recalc.py` viene de la skill de xlsx.'),
            ('Excel «no encuentra el archivo»', 'Ruta demasiado larga: usar nomenclatura corta y mantener la ruta bajo ~180 caracteres.'),
            ('Subtotal con $1 de diferencia', 'Redondeo entre suma de líneas y subtotal; el PDF muestra el total exacto del XLSX y lo anota.')],
            fs='9.5pt'),
        close('Una cotización que ~~cuadra~~',
              ['Valida el PDF antes de llenar el XLSX.', 'Recalcula y compara cada precio.', 'Actualiza `wiki/index.md` y `log.md`.'], 'Siguiente paso'),
    ]


def usuario():
    S = 'guía rápida'
    return [
        statement('qué hace', 'De tu alcance a una ~~cotización~~',
                  'Le compartes **lo que el cliente necesita** y te devuelve un PDF con el alcance por módulos y un Excel con las horas y los precios.',
                  '2', 'archivos con el mismo\nalcance: PDF y Excel',
                  points=['Solo escribe lo que tú le dijiste o confirmaste.', 'Si algo no está claro, **te pregunta** antes de estimar.', 'Los precios del PDF salen del Excel, nunca a mano.'], hs='32pt'),
        cards(S, 'Qué ~~necesitas darle~~', [
            ('file', 'Los alcances', 'Texto, notas de reunión, brief o documento del cliente.', ''),
            ('building', 'Razón social', 'El nombre completo del cliente.', 'navy'),
            ('folder', 'Nombre del proyecto', 'Si el cliente tiene varios proyectos, cada uno se cotiza por separado.', ''),
            ('chat', 'Respuestas a sus dudas', 'Si falta un dato para estimar, te lo preguntará.', '')],
              cols=2, fs='11pt', fh='15pt'),
        flow(S, 'Cómo se usa, ~~paso a paso~~', [
            ('inbox', 'Comparte el alcance', 'Pega o adjunta lo que tengas.', 'Tú'),
            ('chat', 'Resuelve dudas', 'Responde lo que no esté claro.', 'Tú'),
            ('file', 'Valida el PDF', 'Primero ves el alcance por módulos, aún sin precios.', 'Tú'),
            ('sheet', 'Se llena el Excel', 'Se calculan horas y costos con el modelo del equipo Campus.', 'Agente'),
            ('dollar', 'Recibes los dos', 'El PDF se actualiza con los precios reales.', 'Agente')],
             read=('Orden', 'Primero el alcance, después el costo: así validas el contenido antes de hablar de precio')),
        prompts(S, 'Qué ~~escribirle~~: ejemplos', [
            ('Empezar', 'Necesito la cotización para Marval. Aquí está el documento de alcances.', 'Adjunta el archivo o pega el texto.'),
            ('Varios proyectos', 'Este cliente tiene dos proyectos. Cotiza primero el de agentes de correo.', 'Cada uno tiene su propia carpeta.'),
            ('Ajustar días', 'Sube a 3 días el desarrollo backend de la funcionalidad de reportes.', 'Se recalcula y se actualiza el PDF.'),
            ('Ver el total', '¿Cuánto da el total del proyecto y qué parte son los transversales?', 'Sale del Excel recalculado.')],
                 fs='10.5pt'),
        cards(S, 'Qué ~~recibes~~', [
            ('file', 'PDF de alcance', 'Módulos, submódulos y funcionalidades con su precio, y el total.', 'navy'),
            ('sheet', 'Excel de cotización', 'Días por especialidad y costo calculado por las fórmulas del equipo.', ''),
            ('alert', 'Lista de pendientes', 'Lo que conviene que valides: distribución de días, solapamientos, datos faltantes.', '')],
              fs='10.5pt', fh='14pt'),
        checks(S, 'Cómo ~~revisar~~ la cotización', [
            ('El PDF y el Excel cuentan lo mismo', 'No falta ni sobra ningún módulo.'),
            ('Los precios coinciden', 'Mismo valor en el PDF y en el Excel.'),
            ('Los días tienen sentido', 'Distribución por especialidad razonable para tu criterio.'),
            ('Los transversales están', 'Estructura, UX, implementación y agente IA siempre llevan días.'),
            ('Entiendes cada pendiente', 'Si algo te suena a duda, pregúntalo antes de enviar.', 'warn'),
            ('El total es el esperado', 'Compáralo con lo que habías hablado.')]),
        faq(S, 'Preguntas ~~frecuentes~~', [
            ('¿Por qué dice «Pendiente de costear»?', 'Porque el Excel aún no está calculado. Cuando lo esté, el PDF muestra los precios reales.'),
            ('¿Puede tocar las fórmulas del Excel?', 'No. Solo llena las celdas de datos permitidas.'),
            ('Hay $1 de diferencia en un subtotal', 'Es redondeo: el PDF usa el total exacto del Excel y lo deja anotado.'),
            ('¿Puedo pedir otro diseño del PDF?', 'Sí, dilo; los clientes pueden pedir una variante puntual.')]),
        close('¿Listo para ~~cotizar~~?',
              ['Reúne los alcances del cliente.', 'Valida el PDF por módulos.', 'Revisa precios y pendientes.'], 'Siguiente paso'),
    ]
