# -*- coding: utf-8 -*-
"""Contract Perfectionist — contract-perfectionist (Claude Code). Fuente: CLAUDE.md, scripts/README.md."""
from kit import *

META = dict(
    slug='contract-perfectionist', carpeta='contract-perfectionist', nombre='Contract Perfectionist', corto='contratos',
    rol='Redacción de contratos', icono='pen', paso='7', plataforma='Claude Code',
    resumen='Redacta el contrato final de un proyecto a partir de los alcances, la cotización y el contrato madre, listo para firma.',
    tagline_dev='Insumos, cláusulas, script de montaje y gates del contrato',
    tagline_usuario='De alcances y cotización a un contrato listo para firma',
)


def dev():
    return [
        statement('qué es', 'Contratos listos para ~~firma~~',
                  'Redacta el **contrato final** de un proyecto a partir de tres insumos, sin ambigüedad para ninguna de las partes.',
                  '3', 'insumos: alcances,\ncotización y\ncontrato madre',
                  points=['**Nunca inventa:** partes, NIT, representante, alcance, valores y plazos salen literalmente de `recursos/`; si falta, `[PENDIENTE: ...]`.',
                          'El Contrato Madre es **inspiración estructural**, no texto a copiar a ciegas.',
                          'El `.docx` se monta siempre sobre la plantilla corporativa y pasa un gate antes de entregarse.'], hs='32pt'),
        tree('arquitectura', 'Arquitectura de ~~carpetas~~', [
            (0, 'dir', 'contract-perfectionist/', ''),
            (1, 'file', 'CLAUDE.md', 'reglas duras y flujo', 'agente'),
            (1, 'dir', 'recursos/', 'insumos de entrada', 'solo lectura'),
            (2, 'dir', 'alcances/<cliente>/ · cotizaciones/<cliente>/', ''),
            (2, 'dir', 'contrato-madre/', 'plantilla estructural y cláusulas estándar'),
            (2, 'file', 'Contrato - Plantilla Base.docx', 'membrete corporativo'),
            (1, 'dir', 'scripts/', ''),
            (2, 'file', 'build_contract.py', 'build y check'),
            (1, 'dir', 'contratos/<cliente-slug>/', ''),
            (2, 'file', 'Contrato - <Cliente> - <fecha>.docx', '', 'generado'),
            (2, 'file', 'datos.json · verificacion-cruzada.md', '', 'generado'),
            (1, 'dir', 'wiki/', 'index · log · datos-empresa · glosario-clausulas · clientes/'),
        ], [('lock', 'Datos sensibles', '`recursos/` trae NIT, representantes y cifras: confirmar antes de subir el repo a un remoto.', 'navy'),
            ('file', 'Siempre sobre la plantilla', 'Un documento nuevo desde cero, sin membrete, es un defecto de entrega.'),
            ('book', 'Memoria por cliente', '`wiki/clientes/<slug>.md` evita repetir preguntas ya resueltas.')]),
        table('ciclo de trabajo', 'Flujo de ~~seis pasos~~', ['Paso', 'Qué ocurre', 'Salida'], [
            ['1 · Ingesta', 'Lee alcances, cotización, contrato madre y la wiki (`index`, `datos-empresa`, ficha del cliente).', 'Contexto'],
            ['2 · Checklist de datos', 'Lista razón social, NIT, representante, objeto, alcance, cronograma, valor, pago, soporte y garantías; pregunta lo faltante.', 'Preguntas al usuario'],
            ['3 · Borrador', 'Redacta con la arquitectura del contrato madre y ensambla con `build_contract.py build`.', '`.docx` + `datos.json`'],
            ['4 · Verificación cruzada', 'Cada cifra, plazo y alcance se compara con cotización y alcances, con rastro.', '`verificacion-cruzada.md`'],
            ['5 · Gate de calidad', '`build_contract.py check`; si falla, corregir y repetir.', 'Gate aprobado'],
            ['6 · Entrega', 'Guarda en `contratos/<cliente>/`; actualiza índice, log y ficha del cliente.', 'Contrato final']],
              '1.6fr 4.2fr 1.7fr', tf='9.5pt'),
        cols2('cláusulas', 'Arquitectura de ~~cláusulas~~',
              dict(h='Se ajustan a alcances y cotización', icon='file', tone='navy',
                   items=['Consideraciones y objeto', 'Alcance funcional y cronograma', 'Valor y forma de pago', 'Mantenimiento y soporte', 'Garantías', 'Obligaciones y aceptación de entregables']),
              dict(h='Protección estándar: se mantiene', icon='shield',
                   items=['Propiedad intelectual', 'Reserva de información y terceros', 'Fuerza mayor', 'Suspensión y terminación', 'Cláusula penal', 'Vigencia y ley aplicable']),
              fs='11pt', read=('Excepción', 'Las cláusulas de protección solo cambian si el usuario lo indica para ese proyecto')),
        cmds('herramientas', 'Script de ~~montaje~~ y gate', [
            ('Construir', ['python scripts/build_contract.py build --data contratos/<cliente>/datos.json --out "contratos/<cliente>/Contrato - <Cliente> - <YYYY-MM-DD>.docx"'], 'Monta sobre la plantilla corporativa y corre los mismos gates que `check`.'),
            ('Verificar', ['python scripts/build_contract.py check --file "contratos/<cliente>/Contrato - <Cliente> - <YYYY-MM-DD>.docx"'], 'Falla (código ≠ 0) si queda un `[PENDIENTE ...]` o se perdió el membrete o la línea de firma.'),
            ('Opciones', ['--skip-check   ·   pip install python-docx'], '`--skip-check` solo para borradores incompletos, nunca para entrega. El script monta; las cláusulas las redacta el agente.')]),
        table('datos.json', 'Esquema del ~~datos.json~~', ['Campo', 'Descripción'], [
            ['`titulo`', 'Título del contrato.'],
            ['`secciones[].encabezado` · `nivel`', 'Nombre de la cláusula y nivel de título (1 = Heading 1).'],
            ['`secciones[].parrafos`', 'Lista de textos ya redactados, un string por párrafo.'],
            ['`secciones[].tabla`', 'Opcional: `encabezados` y `filas` para cronogramas y formas de pago.'],
            ['`firmantes[]`', '`rol`, `nombre`, `cargo` e `identificacion` (opcional) de cada parte.']],
              '2.6fr 4fr', tf='10pt',
              read=('Registro', 'El `datos.json` queda junto al `.docx` como rastro de qué se generó y para reconstruir una versión posterior')),
        rules('reglas duras', 'Ocho reglas ~~no negociables~~', [
            ('Nunca inventar información', 'Todo dato específico viene de `recursos/`; si no, placeholder explícito.'),
            ('Consultar ante ambigüedad', 'No se asume la interpretación más probable.'),
            ('Madre = estructura', 'El contenido de cada cláusula sigue a alcances y cotización.'),
            ('Discreción y claridad', 'Sin lenguaje comercial ni mezclar clientes: qué, cuándo, cuánto y qué si falla.'),
            ('Diseño corporativo obligatorio', 'Sobre `Contrato - Plantilla Base.docx`, nunca en blanco.'),
            ('Líneas de firma físicas', 'Línea sobre cada nombre, con espacio para firmar.'),
            ('Gate de entrega', 'Sin `check` aprobado no hay versión de entrega.'),
            ('Datos sensibles en el repo', 'Preguntar antes de compartir o subir a un remoto.')],
              fs='9.5pt', tones=['navy', '', '', '', '', '', '', '']),
        table('convención de nombres', 'Convención de ~~nombres~~', ['Caso', 'Patrón'], [
            ['Contrato final', '`contratos/<cliente-slug>/Contrato - <Cliente> - <YYYY-MM-DD>.docx`'],
            ['Revisión sin firmar', '`Contrato - <Cliente> - <YYYY-MM-DD> (v2).docx`, `(v3)`…; el anterior se conserva hasta la versión definitiva.'],
            ['Otrosí o adenda a un contrato firmado', '`Otrosi 1 - <Cliente> - <YYYY-MM-DD>.docx`, numerados; nunca se sobrescribe el original.'],
            ['Slug de cliente', 'Minúsculas, sin espacios ni tildes (`casa-blanca`).'],
            ['Estado en `wiki/index.md`', 'Siempre uno de los valores estandarizados de su leyenda.']],
              '2.2fr 4.6fr', tf='10pt'),
        checks('gates y cierre', 'Al terminar ~~cada contrato~~', [
            ('Gate aprobado', '`check` sin placeholders y con membrete y firma intactos.'),
            ('Verificación cruzada completa', 'Cero discrepancias con cotización y alcances.'),
            ('`wiki/index.md` al día', 'Entrada del cliente con el Estado estandarizado.'),
            ('`wiki/log.md` con la línea', 'Fecha, cliente, qué se generó y confirmación de verificación y gate.'),
            ('Ficha del cliente', 'Datos legales y condiciones particulares confirmadas.'),
            ('Cláusula reutilizable', 'Si surgió una, se documenta en `glosario-clausulas.md` previa validación.')]),
        faq('diagnóstico', 'Síntomas ~~frecuentes~~ y qué hacer', [
            ('El gate falla por un `[PENDIENTE ...]`', 'Resolver el dato con el usuario o la fuente y regenerar; no se entrega con placeholders.'),
            ('El `.docx` perdió el membrete', 'Se montó fuera de la plantilla: volver a construir con `build`, no editar el documento a mano.'),
            ('Una cláusula admite dos lecturas', 'Detenerse y preguntar al usuario antes de redactar esa parte.'),
            ('Reemplazaron el Contrato Madre', 'Registrar el cambio en `glosario-clausulas.md`, sección Historial de versiones.')],
            fs='10pt'),
        close('Un contrato que ~~nadie~~ tiene que interpretar',
              ['Corre el gate antes de entregar.', 'Deja el rastro en wiki y log.', 'Nunca sobrescribas un contrato firmado.'], 'Siguiente paso'),
    ]


def usuario():
    S = 'guía rápida'
    return [
        statement('qué hace', 'Tu redactor de ~~contratos~~',
                  'Con los **alcances** y la **cotización** del proyecto, redacta el contrato final: qué se entrega, cuándo, por cuánto y qué pasa si algo falla.',
                  '0', 'datos inventados:\ntodo sale de tus\ndocumentos',
                  points=['Usa el contrato madre de la empresa como esqueleto de cláusulas.', 'Si falta un dato (NIT, representante…), lo deja marcado y **te lo pregunta**.', 'Entrega un Word con el membrete de Campuslands y líneas de firma.'], hs='32pt'),
        cards(S, 'Qué ~~necesita~~ para empezar', [
            ('file', 'Los alcances del cliente', 'Qué se va a construir.', ''),
            ('calc', 'La cotización', 'Valores, forma de pago y cronograma.', 'navy'),
            ('building', 'Datos de las partes', 'Razón social, NIT y representante legal.', ''),
            ('scale', 'El contrato madre', 'Ya está en el agente: la plantilla de cláusulas de la empresa.', '')],
              cols=2, fs='11pt', fh='15pt'),
        flow(S, 'Cómo se usa, ~~paso a paso~~', [
            ('folder', 'Deja los documentos', 'Alcances y cotización en la carpeta del cliente.', 'Tú'),
            ('chat', 'Pide el contrato', 'Dile el nombre del cliente.', 'Tú'),
            ('help', 'Completa los datos', 'Responde lo que falte o sea ambiguo.', 'Tú'),
            ('eye', 'Revisa el borrador', 'Lee el Word y la verificación cruzada.', 'Tú'),
            ('stamp', 'Firma', 'Imprime o usa firma digital sobre las líneas.', 'Partes')],
             read=('Sin suposiciones', 'Ante una duda, el agente se detiene y pregunta; no elige la lectura más probable')),
        prompts(S, 'Qué ~~escribirle~~: ejemplos', [
            ('Empezar', 'Redacta el contrato de Colbeef con los alcances y la cotización que dejé en recursos.', 'Usa la carpeta del cliente.'),
            ('Completar un dato', 'El NIT del cliente es 900.000.000-0 y firma su gerente general.', 'Reemplaza el `[PENDIENTE: ...]` correspondiente.'),
            ('Ajustar una cláusula', 'Para este proyecto el soporte dura 6 meses, no 12. Actualiza.', 'Las cláusulas de protección solo cambian si lo pides.'),
            ('Cambio tras firmar', 'El cliente pidió un módulo nuevo. Prepara el otrosí.', 'Nunca se sobrescribe el contrato firmado.')],
                 fs='10.5pt'),
        cards(S, 'Qué ~~recibes~~', [
            ('file', 'El contrato en Word', 'Con membrete, cláusulas completas y líneas de firma.', 'navy'),
            ('checkc', 'Verificación cruzada', 'La comparación de cada cifra con tu cotización y alcances.', ''),
            ('book', 'Ficha del cliente', 'Datos legales y condiciones confirmadas para el próximo contrato.', '')],
              fs='10.5pt', fh='14pt'),
        checks(S, 'Cómo ~~revisar~~ el contrato', [
            ('Partes y NIT correctos', 'Razón social, NIT y representante.'),
            ('El objeto es el del proyecto', 'Coincide con los alcances.'),
            ('Valores y pagos', 'Iguales a la cotización, al peso.'),
            ('Cronograma y soporte', 'Fechas, fases, mantenimiento y garantías.'),
            ('No quedan `[PENDIENTE]`', 'El contrato final no puede tener ninguno.', 'warn'),
            ('Las firmas tienen línea', 'Espacio sobre el nombre de cada representante.')],
               read=('Tu decisión', 'Tú apruebas el contenido; el agente redacta y verifica')),
        faq(S, 'Preguntas ~~frecuentes~~', [
            ('¿Qué significa «[PENDIENTE: NIT]»?', 'Que ese dato no estaba en tus documentos. Te lo pedirá y lo reemplazará.'),
            ('¿Puedo editar el Word?', 'Mejor pídeselo al agente: así se mantiene el membrete y pasa la revisión final.'),
            ('Ya está firmado y cambió algo', 'Se hace un otrosí numerado; el contrato original no se toca.'),
            ('¿Se mezclan datos entre clientes?', 'No. Cada contrato es reservado y vive en su carpeta.')]),
        close('¿Listo para ~~contratar~~?',
              ['Reúne alcances y cotización.', 'Completa los datos faltantes.', 'Revisa y firma el contrato.'], 'Siguiente paso'),
    ]
