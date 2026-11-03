# -*- coding: utf-8 -*-
"""Estudio de Presentaciones — presentations-designer (Claude Code). Fuente: CLAUDE.md, wiki/*.md, herramientas/."""
from kit import *

META = dict(
    slug='presentations-designer', carpeta='presentations-designer', nombre='Estudio de Presentaciones', corto='estudio de presentaciones',
    rol='Presentaciones comerciales HTML/CSS', icono='present', paso='3', plataforma='Claude Code',
    resumen='Construye presentaciones comerciales por cliente bajo el Brandbook de Campuslands, las exporta a PDF y las publica con un link.',
    tagline_dev='Marca, plantilla, verificador, PDF y portal de las presentaciones',
    tagline_usuario='De los alcances de tu cliente a una presentación con PDF y link',
)


def dev():
    return [
        statement('qué es', 'Decks ~~HTML/CSS~~ bajo Brandbook',
                  'Agente que construye presentaciones comerciales para **Campuslands Full Service**: HTML/CSS puro, estático y autocontenido, con PDF exportado y link en Vercel.',
                  '10', 'láminas como máximo\n(salvo pedido textual)',
                  points=['Marca estricta: **Brandbook Campuslands 2023**; si el usuario contradice la marca, el agente lo señala antes de hacerlo.',
                          'Entrega doble y obligatoria: **PDF** (Chrome headless) y **link** desplegado; ninguno reemplaza al otro.',
                          'Nada se entrega sin pasar `verificar_deck.py` **y** la revisión a la vista.'], hs='32pt'),
        tree('arquitectura', 'Arquitectura de ~~carpetas~~', [
            (0, 'dir', 'presentations-designer/', ''),
            (1, 'file', 'CLAUDE.md', 'reglas supremas y operaciones', 'agente'),
            (1, 'dir', 'herramientas/', 'verificar_deck · elegir_logo · igualar_logos · colores_marca · verificar_cotizador'),
            (1, 'dir', 'presentaciones/', 'repo Git propio: lo que Vercel despliega'),
            (2, 'dir', 'decks/', 'HTML/CSS/JS estático'),
            (3, 'dir', '_plantilla-campuslands/', 'copiar para todo deck nuevo'),
            (3, 'dir', '<slug-cliente>/', 'index.html · styles.css · script.js · assets/'),
            (2, 'dir', 'web/', 'portal Next.js 16 + TypeScript'),
            (3, 'file', 'src/data/decks.ts', 'catálogo: toda deck nueva se registra aquí'),
            (1, 'dir', 'recursos/', 'brandbook, logos, fuentes Poppins, briefs', 'solo lectura'),
            (1, 'dir', 'wiki/', 'marca · sistema-diseno · despliegue · flujo-trabajo · log'),
        ], [('git', 'Dos repositorios', '`presentaciones/` tiene su propio historial y remote; los commits de decks se hacen dentro.', 'navy'),
            ('layers', 'Web y decks no se mezclan', 'La tecnología nueva es solo del portal; `web/public/` es copia generada de `decks/`.'),
            ('link', 'El slug es la URL', '`/<slug>`: corto y limpio. Si cambia, `git mv` y actualizar portal y wiki.')]),
        flow('ciclo de trabajo', 'Del alcance al ~~link~~', [
            ('inbox', 'Recibir', 'Alcances y cuestionario estándar. Si falta un dato estratégico, se pide.', 'Sin inventar'),
            ('list', 'Plan por lámina', 'Contenido, arquetipo, `--k-cliente` y razón de ubicación. **No se construye sin confirmación.**', 'Gate 1'),
            ('copy', 'Borrador', 'Copiar `_plantilla-campuslands/` y construir las ≤10 láminas completas.', ''),
            ('shield', 'Verificar', '`verificar_deck.py` en APROBADO y cada PNG revisado a la vista.', 'Gate 2'),
            ('rocket', 'Entregar', 'PDF final, registro en 2 lugares, commit/push y link de Vercel.', 'Candado')],
             read=('Iteración', 'Tras cada ajuste del usuario se vuelve a verificar: un cambio de texto puede romper el reparto de una lámina')),
        rules('reglas supremas', 'Ocho reglas de ~~diseño~~', [
            ('Tema claro obligatorio', 'Fondo `#FFFFFF`; navy, violeta, dorado, celeste y verde solo como tarjetas y acentos. Sin bordes: sombras.'),
            ('Co-branding con igual peso', 'Campuslands × Cliente solo en portada, cierre y barra del visor; áreas iguales con `--k-cliente`.'),
            ('Logo a color', 'Sobre blanco, siempre el de color; nunca recolorear, rotar ni deformar.'),
            ('Poppins en todo', 'Regular, Medium, SemiBold y Black. Roboto Mono, Montserrat, Playfair y Arial prohibidas.'),
            ('Nada plano', 'Alternar arquetipos, decoración `.fx`, un ícono con significado por elemento.'),
            ('Máximo 10 láminas', 'Más solo si el usuario lo pide textualmente (`--max-slides N`).'),
            ('Verificación visual', 'Script + vista en cada build y cada ajuste.'),
            ('Cada objeto con razón', 'Posición, tamaño y color se explican en el plan y en la bitácora.')],
              fs='9pt', tones=['navy', '', '', '', '', '', '', '']),
        table('tokens de marca', 'Paleta ~~oficial~~ y su rol', ['Color', 'HEX', 'Rol en presentaciones'], [
            ['Blanco', '`#FFFFFF`', 'Único fondo de lámina y de la página del visor'],
            ['Navy', '`#000087`', 'Títulos y tarjetas de acento (nunca fondo)'],
            ['Violeta', '`#5E3AE2`', 'Énfasis, números, `</`, tarjetas de acento'],
            ['Dorado', '`#F4B422`', 'Íconos, barras y marco neón (no es texto sobre blanco)'],
            ['Celeste', '`#2CAAFF`', 'Íconos y detalles; `{ }`'],
            ['Verde', '`#00AA80`', 'Éxito, chevrones, íconos'],
            ['Arena', '`#E4E4DB`', 'Paneles de apoyo, nunca fondo de lámina'],
            ['Tinta', '`#373435`', 'Color del texto de cuerpo sobre blanco']],
              '1.2fr 1.2fr 4fr', tf='9.5pt'),
        cards('componentes', 'Arquetipos y ~~lenguaje gráfico~~', [
            ('present', 'Siete arquetipos base', 'Portada · afirmación · métricas · proceso · antes/después · módulos · cierre.', ''),
            ('palette', 'Decoraciones `.fx`', 'Anillos, puntos, rayas, cruces y chevrones: discretas, fuera del texto. No nombrar la clase `deco`.', 'navy'),
            ('code', 'Símbolos de marca', '`</`, `{ }`, `<= =>`, migas en el pie, comillas doradas, numeral `.ghost`.', ''),
            ('image', 'Fondo de portada y cierre', '`.deco-cover`: anillos, resplandor y dos hojas laterales; sin chevrones ni manchas.', ''),
            ('zap', 'Marco neón', 'Solo UN dato clave por lámina; nunca en banners ni franjas.', ''),
            ('monitor', 'Visor de una lámina', '`script.js` con `zoom` (no `transform:scale()`); el PDF lo oculta con `@media print`.', '')],
              fs='9.5pt', row=True),
        cmds('herramientas', 'Herramientas y ~~comandos~~', [
            ('Verificar', ['python3 herramientas/verificar_deck.py presentaciones/decks/<slug> --pdf presentaciones/decks/<slug>/<slug>.pdf --png-dir /tmp/<slug>-png'], 'Mide láminas, fondos, logos, fuentes, geometría, contraste y PDF; código 1 si hay errores.'),
            ('Logos', ['python3 herramientas/igualar_logos.py <logo-cliente.png>'], 'Da el factor `--k-cliente` (±6 % de área). Además: `elegir_logo.py` (contraste) y `colores_marca.py` (campo `colors` del portal).'),
            ('Exportar PDF', ['chrome.exe --headless --disable-gpu --no-margins --virtual-time-budget=8000 --print-to-pdf="<ruta absoluta>.pdf" "file:///<ruta>/index.html"'], 'Rutas absolutas; el tiempo virtual evita caer a fuentes de respaldo.'),
            ('Cotizador', ['python3 herramientas/verificar_cotizador.py'], 'Compara la lógica del Cotizador del portal con la del CRM: debe decir «idéntica».')]),
        checks('qué mide el verificador', 'Ocho ~~comprobaciones~~ automáticas', [
            ('Número de láminas', 'Máximo 10 por defecto.'), ('Fondos', 'Lámina y visor, en blanco.'),
            ('Logos', 'Peso visual y «×» centrada.'), ('Tipografía', 'Solo Poppins, mínimo 9 px.'),
            ('Geometría', 'Sin desbordes ni huecos > 20 %.'), ('Contraste', 'WCAG 4.5 : 1 (3 : 1 grande).'),
            ('`<head>`', 'Título = razón social; favicon.'), ('PDF', 'Páginas = láminas, sin fuentes de respaldo.')],
               cols=2, read=('Después', 'APROBADO no basta: se mira cada PNG y se justifica su reparto')),
        cards('registro y publicación', 'Registro ~~obligatorio~~ y candado', [
            ('book', '`wiki/index.md`', 'Listar o actualizar el deck.', ''),
            ('code', '`web/src/data/decks.ts`', 'Un objeto nuevo al inicio de `DECKS`: slug, cliente, título, categoría, láminas, path, pdf, logo, `colors`, date.', 'navy'),
            ('image', 'Logo sin procesar', 'Copia en `decks/assets/logos/` y colores con `colores_marca.py`.', ''),
            ('git', 'Commit y push', 'Dentro de `presentaciones/`: `git add .` y `feat: <Nombre Comercial>`. Repo raíz: solo archivos puntuales.', ''),
            ('lock', 'Candado del agente', '`date`, `path` y `pdf` los fija el agente; en el portal salen bloqueados. Deben ir correctos desde el inicio.', ''),
            ('link', 'Link final', '`fullservicepresentations.vercel.app/<slug>/`. Si no se pudo confirmar el despliegue, se dice.', '')],
              fs='9.5pt', row=True),
        faq('diagnóstico', 'Síntomas ~~frecuentes~~ y qué hacer', [
            ('El verificador marca logos de distinto peso', 'Correr `igualar_logos.py` con el logo recortado del cliente y aplicar `--k-cliente`.'),
            ('El PDF usa Liberation o Georgia', 'Falta `--virtual-time-budget` o `preloadAllFonts()` en `script.js`.'),
            ('`CLAUDE.md` cita páginas de wiki inexistentes', '`wiki/verificacion.md` y `temas-por-cliente.md` no existen hoy: deuda conocida. El protocolo vive en `CLAUDE.md` y `sistema-diseno.md`.'),
            ('El total de la cotización no cuadra', 'Usar la celda `Y122` del XLSX (≈ `Y1 ÷ 0.6`), no el total del PDF generado.')],
            fs='9.5pt'),
        close('Marca, ~~verificación~~ y link',
              ['Mantén `CLAUDE.md` y la wiki sincronizadas.', 'Registra deck en `decks.ts` y `index.md`.', 'Comparte el link solo si el despliegue está publicado.'], 'Siguiente paso'),
    ]


def usuario():
    S = 'guía rápida'
    return [
        statement('qué hace', 'Presentaciones listas para ~~vender~~',
                  'Le compartes los **alcances de tu cliente** y el estudio diseña una presentación con la marca de Campuslands, en PDF y con un link para enviar.',
                  '10', 'láminas como máximo,\ncada una con su razón de ser',
                  points=['Usa siempre el diseño oficial de Campuslands: fondo blanco y logos de ambas empresas.', 'Primero te muestra un **plan lámina por lámina**; no construye hasta que lo apruebes.', 'No inventa cifras: si falta un dato, te lo pide.'], hs='32pt'),
        cards(S, 'Qué ~~necesitas darle~~', [
            ('building', 'Datos generales', 'Nombre completo del cliente, nombre del proyecto, cargo del receptor y quién lidera la cuenta.', ''),
            ('alert', 'Línea base y dolores', 'Cifras actuales del problema y el «hoy» frente al «con la plataforma».', 'navy'),
            ('layers', 'Alcance de la solución', 'Fuentes de datos, de 4 a 6 módulos clave y un ejemplo de uso.', ''),
            ('chart', 'ROI y sector', 'Ahorro o retorno proyectado y casos de éxito del mismo sector.', ''),
            ('dollar', 'Condiciones comerciales', 'Costo total, plazo, esquema de pago, garantía y soporte.', ''),
            ('image', 'Logo del cliente', 'En PNG o SVG con fondo transparente.', '')],
              fs='10pt', row=True, read=('Cuestionario', 'Si algo falta, el agente te envía el cuestionario estándar en vez de suponerlo')),
        flow(S, 'Cómo se usa, ~~paso a paso~~', [
            ('inbox', 'Comparte alcances', 'Pega o adjunta lo que tengas del cliente.', 'Tú'),
            ('list', 'Responde dudas', 'Completa el cuestionario con lo que falte.', 'Tú'),
            ('checkc', 'Aprueba el plan', 'Revisa lámina por lámina: contenido y orden. Nada se construye antes.', 'Tú'),
            ('eye', 'Revisa el borrador', 'Mira el resultado y pide los ajustes que quieras.', 'Tú'),
            ('rocket', 'Recibe PDF y link', 'Listos para enviar al cliente.', 'Estudio')],
             read=('Orden', 'Plan aprobado › borrador completo › revisión › ajustes › PDF y link')),
        prompts(S, 'Qué ~~escribirle~~: ejemplos', [
            ('Empezar', 'Necesito una presentación para Unidrogas S.A.S. sobre una plataforma de inteligencia financiera. Estos son los alcances y la cotización.', 'Adjunta los archivos o pega el texto.'),
            ('Aprobar el plan', 'El plan está bien. Construye el borrador completo.', 'Sin esta frase no empieza a diseñar.'),
            ('Cambiar el orden', 'Pasa la lámina de resultados antes de la de módulos y resume el cierre.', 'Siempre con un máximo de 10 láminas.'),
            ('Pedir un rediseño', 'La lámina 4 se ve plana. Rediséñala con otra estructura.', 'No la retoca: la reestructura.')],
                 fs='10.5pt'),
        cards(S, 'Qué ~~recibes~~', [
            ('file', 'El PDF', 'Una página por lámina: el archivo portable, igual en cualquier equipo.', 'navy'),
            ('globe', 'Un link web', 'La versión interactiva en el visor, lista para compartir.', ''),
            ('list', 'El plan por lámina', 'Qué va en cada una y por qué está ahí.', ''),
            ('book', 'La ficha en el portal', 'Tu presentación queda registrada en el catálogo de proyectos.', '')],
              cols=2, fs='11pt', fh='15pt'),
        checks(S, 'Cómo ~~revisar~~ el borrador', [
            ('Nombre del cliente correcto', 'Razón social completa, con sufijo legal.'),
            ('Cada cifra tiene fuente', 'Si ves un número sin respaldo, pregunta de dónde sale.'),
            ('El orden cuenta una historia', 'Del problema a la solución y al siguiente paso.'),
            ('Los dos logos se ven del mismo tamaño', 'Si uno domina, pídelo y se ajusta.'),
            ('Cabe en 10 láminas', 'Si necesitas más, dilo con esas palabras.', 'warn'),
            ('El total de inversión es el correcto', 'Verifícalo contra tu cotización.')],
               read=('Tu decisión', 'Tú apruebas el plan y el resultado; el estudio construye y verifica')),
        faq(S, 'Preguntas ~~frecuentes~~', [
            ('¿Puedo usar los colores de mi cliente?', 'No: la marca es siempre Campuslands. Del cliente solo se usa su logo.'),
            ('¿Y si necesito más de 10 láminas?', 'Pídelo con esas palabras. Antes, el estudio intenta fusionar contenido.'),
            ('¿Cuánto cobra la presentación por módulo?', 'No muestra precio por módulo salvo que lo pidas; el total va como cifra única.'),
            ('¿Por qué me pide el logo transparente?', 'Con fondo blanco, un logo con fondo propio se vería como un cuadro pegado.')]),
        close('¿Listo para ~~presentar~~?',
              ['Reúne alcances y cotización.', 'Aprueba el plan lámina por lámina.', 'Envía el PDF o el link al cliente.'], 'Siguiente paso'),
    ]
