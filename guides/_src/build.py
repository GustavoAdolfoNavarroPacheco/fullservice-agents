# -*- coding: utf-8 -*-
"""build.py — genera las guías (web + PDF) y el índice a partir de contenido/<agente>/{dev,usuario}.md

Uso:  python -X utf8 guides/_src/build.py [slug ...] [--sin-pdf]
Salida: guides/<agente>/guia-{dev,usuario}.html y .pdf · guides/inicio.html, guides/inicio/instalacion.html, guides/inicio/usuario.html y guides/inicio/desarrollador.html (el índice, con la dirección de cada pestaña)
"""
import html
import json
import pathlib
import re
import sys

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding='utf-8')
    except Exception:
        pass
import md  # noqa: E402
sys.path.insert(0, str(ROOT.parent / 'resources' / 'comandos'))
import comandos  # noqa: E402   (catálogo de comandos «!»: fuente única de las tablas de las guías)

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
FECHA = '3 nov 2026'

# orden del pipeline comercial
AGENTES = [
    dict(slug='prospection-agent', nombre='Radar de Campus', rol='Prospección de empresas', plataforma='Perplexity',
         resumen='Busca en la web abierta las empresas que encajan con el perfil de cliente de Campuslands y entrega un listado con datos públicos verificables.'),
    dict(slug='intelligence-commercial', nombre='Explorador de Campus', rol='Inteligencia comercial en LinkedIn', plataforma='Perplexity',
         resumen='Toma una lista de empresas, encuentra a los contactos clave de cada una y les envía solicitudes de conexión personalizadas.'),
    dict(slug='presentations-designer', nombre='Estudio de Presentaciones', rol='Presentaciones comerciales', plataforma='Claude Code',
         resumen='Construye presentaciones comerciales por cliente bajo el Brandbook de Campuslands, las exporta a PDF y las publica con un link.'),
    dict(slug='functional-scope', nombre='Alcances Funcionales', rol='Documentos de alcance funcional', plataforma='Claude Code',
         resumen='Lee las fuentes de un proyecto, detecta contradicciones y vacíos y redacta el alcance funcional para el cliente, sin inventar compromisos.'),
    dict(slug='quote-developer', nombre='Desarrollador de Cotizaciones', rol='Cotizaciones: PDF + XLSX', plataforma='Claude Code',
         resumen='A partir de los alcances genera el PDF de cotización de alcance y llena la plantilla XLSX de costos del equipo Campus.'),
    dict(slug='bidding-agent', nombre='Agente Licitatorio', rol='Licitaciones y preventa técnica', plataforma='Claude Code',
         resumen='Analiza los cuatro documentos de una licitación y construye la propuesta técnica, la estimación de horas y el análisis de IA.'),
    dict(slug='contract-perfectionist', nombre='Perfeccionador de Contratos', rol='Redacción de contratos', plataforma='Claude Code',
         resumen='Redacta el contrato final de un proyecto a partir de los alcances, la cotización y el contrato madre, listo para firma.'),
]
TIPOS = {'dev': 'Guía de desarrollador', 'usuario': 'Guía de usuario'}

# Galería del presentations-designer. Las imágenes las genera recursos_web.py (portadas desde los PDF de presentaciones/decks, logos desde resources/companies-logos).
PORTADAS = [  # (archivo en assets/img/portadas, cliente, proyecto)
    ('fullservice-campuslands-v3', 'Campuslands', 'FullService Campuslands'),
    ('ai-academy', 'Campuslands AI Academy', 'Deja de usar la IA, empieza a dirigirla'),
    ('avicampo', 'Avicampo', 'Agente de IA en WhatsApp'),
    ('chico', 'Chico Soluciones Logísticas', 'Abastecimiento Penitenciario'),
    ('colbeef-flujo-ia', 'ColBeef', 'Flujo conversacional del Agente IA'),
    ('compumax-asistente-ia', 'Compumax', 'Asistente de IA Inmobiliario'),
    ('comultrasan-orbit', 'Financiera Comultrasan', 'Asistente Conversacional con IA Generativa'),
    ('fcv', 'Fundación Cardiovascular', 'Desarrollo de Software Especializado'),
    ('gaspais-chilco', 'GasPaís', 'Plataforma Integral de Gestión HSE-SST'),
    ('giron-cc-v2', 'Alcaldía de Girón', 'Módulo de Cobranza con Inteligencia Artificial'),
    ('globant-dojo-v3', 'Globant', 'Modelo de desarrollo con dojo'),
    ('greenmetal-fyswap', 'Green Metal', 'Digitalización de la Logística de Salida y Calidad'),
    ('hubux-v2', 'Zona Franca Santander', 'Ecosistema Campuslands en el Hub Tecnológico'),
    ('land-cargo-v2', 'Land Cargo', 'Sistema Integrado TMS + ERP a la Medida'),
    ('marval', 'Marval', 'Un orquestador central, múltiples agentes de IA'),
    ('mchaileh-crm-ia', 'Mchaileh Inmobiliaria', 'CRM Inmobiliario + Asistente de IA'),
    ('miami-aqua-tours-ampliado', 'Miami Aqua Tours', 'Plataforma de Venta y Gestión de Tours'),
    ('multinal-escenario-b', 'Multinal', 'Ecosistema Digital Corporativo'),
    ('palmera-jr', 'Palmera Junior', 'Plataforma segura y vigente con Laravel 13'),
    ('unidrogas', 'Unidrogas', 'Automatización de Contenidos y Formación con IA'),
    ('ve-a-la-segura', 'Ve a la Segura', 'Atención y Venta Automatizada con IA'),
]
LOGOS = [  # (archivo en assets/img/logos, empresa)
    ('alcaldia-de-giron', 'Alcaldía de Girón'), ('avicampo', 'Avicampo'), ('chico-soluciones-logisticas', 'Chico Soluciones Logísticas'),
    ('colbeef', 'ColBeef'), ('compumax', 'Compumax'), ('fcv', 'Fundación Cardiovascular'), ('financiera-comultrasan', 'Financiera Comultrasan'),
    ('gaspais', 'GasPaís'), ('green-metal', 'Green Metal'), ('marval', 'Marval'), ('mchaileh', 'Mchaileh Inmobiliaria'),
    ('miami-aqua-tours', 'Miami Aqua Tours'), ('multinal', 'Multinal'), ('palmera-junior', 'Palmera Junior'), ('unidrogas', 'Unidrogas'),
]
FLECHA_IZQ ='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>'
FLECHA_DER = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>'


def carrusel(clase, etiqueta, tarjetas, extra=''):
    """Estructura común de los dos carruseles (efectos.js los activa; sin JS quedan como cuadrícula)."""
    return ('<div class="cx %s" %s><div class="cx-stage" role="group" aria-roledescription="carrusel" aria-label="%s" tabindex="0">%s</div>'
            '<div class="cx-bar"><button type="button" class="cx-btn cx-prev" aria-label="Anterior">%s</button>'
            '<div class="cx-cap" aria-live="off"><b></b><span></span></div><span class="cx-n"></span>'
            '<button type="button" class="cx-btn cx-next" aria-label="Siguiente">%s</button></div></div>'
            % (clase, extra, html.escape(etiqueta), tarjetas, FLECHA_IZQ, FLECHA_DER))


# Inicio → «Usarlo como Proyecto»: qué archivos de cada agente se suben a un Proyecto de Claude o a un Space de Perplexity y cuáles no.
# wiki = páginas de wiki/ · skills = carpetas de habilidades/ (cada SKILL.md se sube con el nombre de su carpeta) · extras = (ruta o archivo, nota) · no = (ruta, motivo)
PROYECTO = {
    'prospection-agent': dict(
        instr='Perplexity.md', wiki=['index', 'formulario-intake', 'enlaces-utiles', 'perfil-usuario'],
        skills=['busqueda-web-empresas', 'enriquecimiento-datos-empresa', 'formulario-intake', 'generacion-listado-resultados'], extras=[],
        no=[('wiki/log.md', 'La bitácora histórica: ocupa espacio y no cambia lo que el agente hace.'),
            ('prospeccion/', 'Aquí se guardan los listados que entrega; en el Space los recibes en el chat.')]),
    'intelligence-commercial': dict(
        instr='Perplexity.md', wiki=['index', 'filtros-busqueda', 'perfiles-objetivo', 'marca-campuslands', 'perfil-usuario'],
        skills=['control-navegador-linkedin', 'deteccion-idioma', 'generacion-mensajes-personalizados', 'generacion-tabla-registro'], extras=[],
        no=[('wiki/log.md', 'La bitácora histórica: ocupa espacio y no cambia lo que el agente hace.'),
            ('prospeccion/', 'Aquí se guardan los registros de contactos y mensajes; no es información que el agente necesite leer.')]),
    'presentations-designer': dict(
        instr='CLAUDE.md', wiki=['marca-campuslands', 'sistema-diseno', 'estandar-v3-laminas', 'flujo-trabajo', 'verificacion', 'plantilla-base', 'despliegue', 'perfil-usuario', 'temas-por-cliente'],
        skills=[], extras=[('presentaciones/decks/_plantilla-campuslands/', 'Sube sus tres archivos renombrados: index.html como plantilla-index.html, styles.css como plantilla-styles.css y script.js como plantilla-script.js.', 3)],
        no=[('wiki/index.md · wiki/log.md', 'El catálogo y la bitácora históricos pesan casi 400 KB: llenarían el proyecto sin aportar al diseño.'),
            ('herramientas/', 'Son programas para tu computador; el Proyecto no los ejecuta. El verificador lo corres tú.'),
            ('presentaciones/', 'Es el repositorio aparte de las presentaciones: el Proyecto genera archivos nuevos y tú los guardas ahí.'),
            ('recursos/', 'Fuentes y logos: el HTML los enlaza con rutas relativas y se ven cuando lo guardas en su carpeta.')]),
    'functional-scope': dict(
        instr='CLAUDE.md', wiki=['index', 'manual-operativo'], skills=[],
        extras=[('plantillas/ficha-funcional.md · plantillas/matriz-informacion.md · plantillas/matriz-riesgos-pendientes.md · plantillas/matriz-trazabilidad.md · plantillas/registro-decisiones.md · plantillas/control-calidad.md', 'Las seis plantillas de trabajo, tal cual.'),
                ('recursos/Manual_Agente_Alcances_Funcionales_Campuslands.docx', 'El manual que gobierna al agente.'),
                ('plantillas/Alcance Funcional - Plantilla.docx', 'La plantilla Word del documento final.')],
        no=[('scripts/', 'alcance_docx.py arma el Word en tu computador; el Proyecto no lo ejecuta.'),
            ('alcances/', 'Una carpeta por cliente. Sube solo las fuentes del cliente con el que trabajas, en cada chat.'),
            ('recursos/marca/', 'Son firmas escaneadas: datos sensibles que no deben subirse a un servicio externo.'),
            ('wiki/log.md', 'La bitácora histórica.')]),
    'quote-developer': dict(
        instr='CLAUDE.md', wiki=['index', 'plantilla-xlsx', 'diseno-pdf-cotizacion', 'marca-campuslands', 'perfil-usuario'], skills=[],
        extras=[('recursos/FullServices - Plantilla Cotizaciones.xlsx', 'La plantilla maestra de costos del equipo Campus.')],
        no=[('cotizaciones/', 'Las cotizaciones generadas por cliente.'), ('wiki/log.md · wiki/entrada-log-sugerida.md', 'La bitácora y su plantilla de entrada: no cambian el trabajo del agente.')]),
    'bidding-agent': dict(
        instr='CLAUDE.md', wiki=['index', 'flujo-trabajo', 'estimacion-horas', 'consideraciones-tecnicas', 'costeo-ia-tokens', 'estructura-propuesta-tecnica', 'plantilla-verificacion-cruzada', 'marca-campuslands', 'perfil-usuario'],
        skills=['analisis-ia-tokens', 'estimacion-horas', 'ingesta-documentos-licitacion', 'matriz-cumplimiento', 'modelos-costos'],
        extras=[('recursos/licitaciones/<proceso>/', 'Los cuatro documentos oficiales de la licitación en la que trabajas: solo esa, en cada chat.', 4)],
        no=[('recursos/licitaciones/ (otros procesos)', 'Pesan varios MB y no tienen que ver con la licitación actual.'), ('licitaciones/', 'Los entregables generados por proceso.'), ('wiki/log.md', 'La bitácora histórica.')]),
    'contract-perfectionist': dict(
        instr='CLAUDE.md', wiki=['index', 'glosario-clausulas', 'datos-empresa', 'plantilla-verificacion-cruzada'], skills=[],
        extras=[('recursos/contrato-madre/Contrato Madre - Plantilla Base.docx', 'El contrato madre con las cláusulas estándar.'),
                ('recursos/Contrato - Plantilla Base.docx', 'La plantilla base con el membrete corporativo.'),
                ('recursos/alcances/<cliente>/ · recursos/cotizaciones/<cliente>/ · wiki/clientes/<cliente>.md', 'Solo los del cliente cuyo contrato redactas, en cada chat.')],
        no=[('scripts/', 'build_contract.py ensambla el .docx en tu computador; el Proyecto no lo ejecuta.'), ('contratos/', 'Los contratos finales por cliente.'), ('wiki/log.md · CHANGELOG.md', 'Historiales: no cambian el trabajo del agente.')]),
}


def proyectos():
    """Selector de agentes (desplegable) y, para el elegido, una ficha en tres pasos: pegar las instrucciones, subir estos archivos y dejar estos fuera.
    Los datos salen de PROYECTO; el texto de instrucciones se genera con el nombre, el rol y el resumen del agente."""
    def chips(nombres, k, clase=''):
        out = ''
        for n_ in nombres:
            k[0] += 1
            out += '<code class="pj-f%s" style="--k:%d">%s</code>' % (clase, k[0], html.escape(n_))
        return '<span class="pj-fs">%s</span>' % out

    paneles = []
    for ag in AGENTES:
        d = PROYECTO[ag['slug']]
        k = [0]
        claude = ag['plataforma'] == 'Claude Code'
        n_extra = sum(e[2] if len(e) > 2 else len(e[0].split(' · ')) for e in d['extras'])
        subidos = 1 + len(d['wiki']) + len(d['skills']) + n_extra
        fuera = len(d['no'])
        # paso 1: instrucciones
        lim = ('No tienes acceso a mi computador, a Git ni a los scripts del repositorio. No digas que ejecutaste, verificaste o publicaste algo que no pudiste ejecutar. '
               'Cuando una regla mande correr un script o un comando, dame el comando exacto y qué resultado debo esperar. Entrega cada archivo completo y con su nombre final.'
               if claude else
               'Trabaja solo con la búsqueda y las herramientas de Perplexity. Si una regla pide algo que no puedes hacer aquí, dime qué parte no pudiste y cómo la hago yo.')
        prompt = ['Eres «%s» (%s), un agente del flujo comercial de Campuslands (Full Service). %s' % (ag['nombre'], ag['rol'].lower(), ag['resumen']), '',
                  'Antes de responder, lee en los archivos de este proyecto: %s (tus reglas completas)%s. Síguelos al pie de la letra.'
                  % (d['instr'], ' y la wiki' if d['wiki'] else ''), '',
                  'Si te falta información para trabajar, pídemela; no inventes datos.', '', lim]
        paso1 = ('<li class="pj-s" style="--i:0"><span class="pj-n">1</span><div class="pj-b"><h4>Pega las instrucciones</h4>'
                 '<p>En el campo de instrucciones del Proyecto (Claude) o del Space (Perplexity).</p>%s</div></li>' % md.fence('prompt', prompt))
        # paso 2: archivos que se suben
        g = '<div class="pj-g"><span class="pj-gl">Reglas del agente</span>%s</div>' % chips([d['instr']], k, ' pj-main')
        if d['wiki']:
            g += '<div class="pj-g"><span class="pj-gl">Wiki <em>%d</em></span>%s</div>' % (len(d['wiki']), chips(['wiki/%s.md' % w for w in d['wiki']], k))
        if d['skills']:
            g += ('<div class="pj-g"><span class="pj-gl">Habilidades <em>%d</em></span>%s<small>Todas se llaman SKILL.md: súbelas con el nombre de su carpeta.</small></div>'
                  % (len(d['skills']), chips(['%s-SKILL.md' % x for x in d['skills']], k)))
        if d['extras']:
            filas = ''.join('<div class="pj-r">%s<span>%s</span></div>' % (chips(e[0].split(' · '), k), md.inline(e[1])) for e in d['extras'])
            g += '<div class="pj-g"><span class="pj-gl">Plantillas y documentos</span>%s</div>' % filas
        paso2 = ('<li class="pj-s" style="--i:1"><span class="pj-n">2</span><div class="pj-b"><h4>Sube estos archivos <em>%d</em></h4>'
                 '<p>Al conocimiento del Proyecto (Claude) o a los archivos del Space (Perplexity). No admiten carpetas: cada archivo va suelto.</p>%s</div></li>' % (subidos, g))
        # paso 3: lo que se queda fuera
        filas = ''.join('<div class="pj-r">%s<span>%s</span></div>' % (chips(r.split(' · '), k, ' pj-no'), md.inline(n_)) for r, n_ in d['no'])
        paso3 = ('<li class="pj-s" style="--i:2"><span class="pj-n pj-x">3</span><div class="pj-b"><h4>Déjalo fuera</h4><p>No lo subas: no aporta o no se puede usar en un chat.</p>%s</div></li>' % filas)
        cab = ('<div class="pj-h"><img src="@@REL@@assets/img/%s" alt="" width="40" height="40"><div class="pj-t"><b>%s</b><span>%s</span></div>'
               '<div class="pj-st"><span><b data-n="%d">%d</b>archivos para subir</span><span><b data-n="%d">%d</b>se quedan fuera</span></div></div>'
               % ('plataforma-claude.png' if claude else 'plataforma-perplexity.png', html.escape(ag['slug']), html.escape('%s · %s · %s' % (ag['nombre'], ag['plataforma'], d['instr'])), subidos, subidos, fuera, fuera))
        paneles.append((ag['slug'], '%s // %s · %s' % (ag['slug'], ag['plataforma'], ag['rol']), 'claude' if claude else 'pplx',
                        '<div class="pj">%s<ol class="pj-steps">%s%s%s</ol></div>' % (cab, paso1, paso2, paso3)))
    return md._switch('proyecto-agente', paneles, 'menu')



def galeria(kind, rel, ag=None):
    """Card Stack con las portadas / Coverflow con los logos de los clientes / tabla de comandos «!» del agente."""
    if kind == 'comandos':
        return comandos.tabla_html(ag['slug'], md.inline)
    if kind == 'proyectos':
        return proyectos()
    if kind == 'cardstack':
        cards = ''.join('<figure class="cx-card" data-c="%s" data-p="%s"><img data-src="%sassets/img/portadas/%s.webp" width="800" height="450" decoding="async" alt="Portada de la presentación de %s: %s">'
                        '<figcaption>%s · %s</figcaption></figure>'
                        % (html.escape(c), html.escape(p), rel, f, html.escape(c), html.escape(p), html.escape(c), html.escape(p)) for f, c, p in PORTADAS)
        return carrusel('cs', 'Portadas de las presentaciones', cards, 'data-ritmo="3600" data-visibles="3"')
    cards = ''.join('<figure class="cx-card" data-c="%s" data-p=""><span class="cf-logo"><img data-src="%sassets/img/logos/%s.webp" width="280" height="210" decoding="async" alt="Logo de %s"></span>'
                    '<figcaption>%s</figcaption></figure>' % (html.escape(n), rel, f, html.escape(n), html.escape(n)) for f, n in LOGOS)
    return carrusel('cf', 'Logos de las empresas', cards, 'data-ritmo="2800" data-visibles="3"')

# Icono del botón PDF: «FileDown» de AnimateIcons (@animateicons/react, MIT) sobre la forma de Lucide (ISC), pasado a SVG + CSS con los mismos
# fotogramas (la hoja pulsa y la flecha baja, 0,6 s). Avisos de licencia en assets/ICONS-LICENSE.txt.
PDF_ICON = ('<svg class="pdf-ic" viewBox="0 0 24 24" aria-hidden="true"><g class="pdf-all">'
            '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/>'
            '<path d="M14 2v5a1 1 0 0 0 1 1h5"/>'
            '<g class="pdf-arrow"><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/></g></g></svg>')

# Plataforma donde corre el agente, con su icono (resources/platforms-logos/ → guides/assets/img/plataforma-*.png)
PLAT_ICONO = {'Perplexity': 'plataforma-perplexity.png', 'Claude Code': 'plataforma-claude.png'}


def plat(ag, rel):
    nombre = html.escape(ag['plataforma'])
    ico = PLAT_ICONO.get(ag['plataforma'])
    if not ico:
        return nombre
    return '<span class="plat"><img src="%sassets/img/%s" alt="" width="16" height="16">%s</span>' % (rel, ico, nombre)


# Iconos de Claude y Perplexity flotando en 3D a la derecha del banner (decorativos; estilos en estilo.css, parallax en ART_JS)
def _ico(clase, img):
    return ('<div class="ico %s"><span class="ico-glow"></span><div class="ico-tilt"><div class="ico-spin"><div class="ico-float">'
            '<span class="ico-face"><img src="assets/img/%s" alt="" width="160" height="160"></span></div></div></div></div>') % (clase, img)


BANNER_ART = ('<div class="banner-art" aria-hidden="true">' + _ico('ico-claude', 'plataforma-claude-lg.png') + _ico('ico-pplx', 'plataforma-perplexity-lg.png') + '</div>')

ART_JS = """<script>
(function(){
  var ban = document.querySelector('.banner'), art = document.querySelector('.banner-art');
  if(!ban || !art || (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) return;
  function mover(e){
    var r = art.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height / 2;
    var x = Math.max(-1, Math.min(1, (e.clientX - cx) / 420)), y = Math.max(-1, Math.min(1, (e.clientY - cy) / 260));
    art.style.setProperty('--px', x.toFixed(3)); art.style.setProperty('--py', y.toFixed(3));
  }
  ban.addEventListener('pointermove', mover);
  ban.addEventListener('pointerleave', function(){ art.style.setProperty('--px', 0); art.style.setProperty('--py', 0); });
  // animación de hover sin interrupciones: al entrar se reproduce completa y no vuelve a empezar hasta que termina
  [].forEach.call(art.querySelectorAll('.ico'), function(ico){
    var spin = ico.querySelector('.ico-spin'), t = 0;
    function fin(){ ico.classList.remove('anim'); clearTimeout(t); }
    spin.addEventListener('animationend', function(e){ if(e.target === spin) fin(); });
    ico.addEventListener('pointerenter', function(){
      if(ico.classList.contains('anim')) return;
      ico.classList.add('anim'); t = setTimeout(fin, 2400);
    });
  });
})();
</script>
"""

# Pestañas del índice (Guía de usuario / Guía de desarrollador). Sin JavaScript se ven las dos listas seguidas.
TABS_JS = """<script>
(function(){
  var root = document.documentElement; root.classList.add('js');
  var tabs = [].slice.call(document.querySelectorAll('.tabs [role=tab]')), ind = document.querySelector('.tab-ind'), cur = null;
  if(!tabs.length) return;
  var RUTAS = ['/inicio', '/inicio/instalacion', '/inicio/usuario', '/inicio/desarrollador'];
  function mover(){ var t = tabs[cur]; ind.style.setProperty('--x', t.offsetLeft + 'px'); ind.style.setProperty('--w', t.offsetWidth + 'px'); }
  var limpia = /^[/]inicio([/](instalacion|usuario|desarrollador))?[/]?$/.test(location.pathname);      // servida con las direcciones limpias de Vercel
  function url(i){ if(!limpia) return; try{ history.replaceState(null, '', RUTAS[i]); }catch(e){} }
  function ir(i, foco, hash){
    var primera = cur === null; cur = i;
    tabs.forEach(function(t, j){
      var on = j === i; t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if(primera){ ind.style.transition = 'none'; mover(); ind.offsetWidth; ind.style.transition = ''; } else { mover(); }
    var caja = document.querySelector('.tabbar-in');
    if(caja && caja.scrollWidth > caja.clientWidth + 1){ caja.scrollTo({left: tabs[i].offsetLeft - (caja.clientWidth - tabs[i].offsetWidth) / 2, behavior: primera ? 'auto' : 'smooth'}); }      // móvil: la pestaña activa queda a la vista
    if(foco) tabs[i].focus();
    if(hash){ url(i); }
  }
  tabs.forEach(function(t, i){
    t.addEventListener('click', function(){ ir(i, false, true); });
    t.addEventListener('keydown', function(e){
      var k = e.key, n = k === 'ArrowRight' ? (i + 1) % tabs.length : k === 'ArrowLeft' ? (i + tabs.length - 1) % tabs.length : k === 'Home' ? 0 : k === 'End' ? tabs.length - 1 : -1;
      if(n >= 0){ e.preventDefault(); ir(n, true, true); }
    });
  });
  function panelDe(el){
    var s = el && el.closest && el.closest('.panel'); if(!s) return -1;
    for(var j = 0; j < tabs.length; j++){ if(tabs[j].getAttribute('aria-controls') === s.id) return j; }
    return -1;
  }
  var p = location.pathname, h = location.hash, ini = 0, destino = null, antiguo = /^#(dev|usuario|desarrollador)$/.test(h);
  var porRuta = /[/]desarrollador[/]?$/.test(p) ? 3 : /[/]usuario[/]?$/.test(p) ? 2 : /[/]instalacion[/]?$/.test(p) ? 1 : -1;
  if(h.length > 1){ try{ destino = document.getElementById(decodeURIComponent(h.slice(1))); }catch(e){} }
  if(porRuta >= 0){ ini = porRuta; }
  else if(h === '#dev' || h === '#desarrollador'){ ini = 3; }
  else if(destino && panelDe(destino) >= 0){ ini = panelDe(destino); }      // un enlace con #ancla abre la pestaña donde está esa sección
  ir(ini, false, false);
  if(antiguo || (destino && porRuta < 0 && ini > 0)) url(ini);      // enlaces antiguos con # se limpian; los de una sección toman la dirección de su pestaña
  if(destino && !antiguo) setTimeout(function(){ if(destino.offsetParent) destino.scrollIntoView(); }, 80);
  window.addEventListener('resize', mover);
  if(document.fonts && document.fonts.ready) document.fonts.ready.then(mover);
  // el índice lleva <base href="/">: un enlace «#ancla» suelto apuntaría a «/». Se resuelve aquí, sin recargar.
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href^="#"]'); if(!a) return;
    var id = a.getAttribute('href').slice(1), t = id && document.getElementById(id); if(!t) return;
    e.preventDefault(); e.stopPropagation();
    var j = panelDe(t); if(j >= 0 && j !== cur){ ir(j, false, true); }      // la sección está en otra pestaña: se abre
    try{ history.replaceState(null, '', location.pathname + '#' + id); }catch(x){}
    window.dispatchEvent(new Event('hashchange'));
    // desplazamiento suave (el mismo de las guías); si la sección estaba en otra pestaña o panel, se espera a que se muestre
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ if(t.offsetParent && window.irA) window.irA(t); else if(t.offsetParent) t.scrollIntoView(); }); });
  }, true);      // fase de captura: Lenis no procesa este clic (la sección puede estar en una pestaña oculta)
})();
</script>
"""
DL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>'

JS = """<script>
(function(){var l=[].slice.call(document.querySelectorAll('.toc a'));if(!l.length||!('IntersectionObserver'in window))return;
var m={};l.forEach(function(a){m[a.getAttribute('href').slice(1)]=a});
var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){l.forEach(function(a){a.classList.remove('on')});var a=m[e.target.id];if(a)a.classList.add('on')}})},{rootMargin:'-80px 0px -70% 0px'});
document.querySelectorAll('article h2').forEach(function(h){o.observe(h)})})();
</script>"""


SITE = 'https://fullservice-agents.vercel.app'


def head(title, rel, desc=None, path=None, img=None):
    """Cabecera. Con desc/path/img añade la vista previa del enlace (Open Graph y Twitter): imagen de 1200 × 630 de assets/img/preview/ (la genera preview.py)."""
    meta = ''
    if desc is not None:
        e, url, im = html.escape(desc, quote=True), SITE + path, SITE + '/assets/img/preview/' + img
        t = html.escape(title, quote=True)
        alt = html.escape('%s · guías de los agentes de Campuslands' % title.split(' · ')[0], quote=True)
        meta = ('<meta name="description" content="%s">\n<meta name="theme-color" content="#f5f4ed">\n<link rel="canonical" href="%s">\n'
                '<meta property="og:type" content="website">\n<meta property="og:site_name" content="fullservice-agents">\n<meta property="og:locale" content="es_CO">\n'
                '<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n'
                '<meta property="og:image" content="%s">\n<meta property="og:image:type" content="image/png">\n<meta property="og:image:width" content="1200">\n'
                '<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="%s">\n'
                '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="%s">\n<meta name="twitter:description" content="%s">\n'
                '<meta name="twitter:image" content="%s">\n<meta name="twitter:image:alt" content="%s">\n'
                % (e, url, t, e, url, im, alt, t, e, im, alt))
    return ('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>%s</title>\n%s<script>document.documentElement.classList.add("fx")</script>\n<link rel="icon" type="image/png" href="%sassets/img/favicon.png">\n<link rel="stylesheet" href="%sassets/estilo.css">\n</head>\n<body>\n'
            % (html.escape(title), meta, rel, rel))


GH_URL = 'https://github.com/GustavoAdolfoNavarroPacheco/fullservice-agents'
# Botón de GitHub: el relleno (.gh-fill) sube como una ola, el icono se agita y la flecha sale en diagonal al pasar el cursor (todo en CSS)
GH_BTN = ('<a class="gh" href="%s" target="_blank" rel="noopener noreferrer" aria-label="Ver el repositorio en GitHub">'
          '<span class="gh-fill" aria-hidden="true"></span>'
          '<svg class="gh-ic" viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>'
          '<span class="gh-t">GitHub</span>'
          '<svg class="gh-ar" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></a>') % GH_URL


# Social Preview Dock (esquina inferior derecha del pie): iconos que se agrandan al pasar el cursor y muestran una vista previa del perfil.
# Iconos de marca: GitHub (Octicons, MIT) y LinkedIn (Simple Icons, CC0). Las vistas previas son tarjetas HTML/CSS con los datos del perfil (social.json y assets/img/social/avatar.webp).
LI_PATH = ('M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z')
GH_PATH = re.search(r'd="([^"]+)"', GH_BTN).group(1)
SOCIAL = json.loads((SRC / 'social.json').read_text(encoding='utf-8'))   # actividad de GitHub (de la captura del perfil) para la mini cuadrícula
DOCK_GH = ('https://github.com/GustavoAdolfoNavarroPacheco', 'GustavoAdolfoNavarroPacheco')
DOCK_LI = ('https://www.linkedin.com/in/gustavo-adolfo-navarro-pacheco-876b06356/', 'Gustavo Adolfo Navarro Pacheco')


def dock(rel):
    """Dock con GitHub y LinkedIn; cada icono despliega una tarjeta de vista previa hecha con HTML/CSS (no son capturas)."""
    av = '<img class="pv-av" src="%sassets/img/social/avatar.webp" width="112" height="112" loading="lazy" decoding="async" alt="">' % rel
    celdas = ''.join('<i class="l%d"></i>' % v for sem in SOCIAL['semanas'] for v in sem)         # 7 filas × N semanas, por columnas
    total = '{:,}'.format(SOCIAL['total']).replace(',', '.')
    gh = ('<span class="dock-pv dock-pv-gh" aria-hidden="true"><span class="pv-head">%s<span class="pv-id"><b>Gustavo Navarro</b>'
          '<span>%s contribuciones en %d</span></span></span><span class="pv-grid" style="--w:%d">%s</span></span>'
          % (av, total, SOCIAL['anio'], len(SOCIAL['semanas']), celdas))
    li = ('<span class="dock-pv dock-pv-li" aria-hidden="true"><span class="pv-ban"></span>%s<span class="pv-body"><b>%s</b>'
          '<span>Full-Stack Developer · Functional QA · Automation and AI</span><span class="pv-loc">Bucaramanga, Colombia</span></span>'
          '<span class="pv-btn">Ver perfil</span></span>' % (av.replace('class="pv-av"', 'class="pv-av pv-av-lg"'), DOCK_LI[1]))
    def item(clase, red, enlace, icono, vb, tarjeta):
        return ('<a class="dock-i %s" href="%s" target="_blank" rel="noopener noreferrer" aria-label="%s de Gustavo Navarro (se abre en una pestaña nueva)">'
                '<svg viewBox="%s" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>%s</a>' % (clase, enlace, red, vb, icono, tarjeta))
    return ('<nav class="dock" aria-label="Redes de Gustavo Navarro">%s%s</nav>'
            % (item('dock-gh', 'GitHub', DOCK_GH[0], GH_PATH, '0 0 16 16', gh), item('dock-li', 'LinkedIn', DOCK_LI[0], LI_PATH, '0 0 24 24', li)))


def topbar(rel, pdf=None):
    """Barra superior: marca, (en las guías) volver al índice y descargar el PDF, y el botón de GitHub."""
    extra = ''
    if pdf:
        extra = ('<a href="%sinicio">Todas las guías</a><a class="btn" href="%s" download>%s Descargar PDF</a>' % (rel, pdf, DL))
    return ('<header class="top"><div class="top-in"><a class="brand" href="%sinicio"><img src="%sassets/img/logo-campuslands-color.png" alt="Campuslands"><span>fullservice-agents</span></a>'
            '<nav>%s%s</nav></div></header>\n' % (rel, rel, extra, GH_BTN))


def scripts(rel):
    """Scroll suave (Lenis) en todas las páginas; suave.js lo activa."""
    return ('<script src="%sassets/lenis.min.js"></script>\n<script src="%sassets/suave.js"></script>\n<script src="%sassets/efectos.js"></script>' % (rel, rel, rel))


def guide_page(ag, kind, meta, body, toc, words):
    other = 'usuario' if kind == 'dev' else 'dev'
    mins = max(1, round(words / 210))
    title = meta.get('titulo', ag['nombre'])
    tocs = ''.join('<li><a href="#%s">%s</a></li>' % (i, html.escape(t)) for i, t in toc)
    # conversación («lanes»): estilo del chat de la plataforma del agente
    pl = {'Perplexity': ('pplx', 'plataforma-perplexity.png', 'Pregunta lo que quieras…'), 'Claude Code': ('claude', 'plataforma-claude.png', 'Escribe tu mensaje…')}[ag['plataforma']]
    for k_, v_ in (('@@CLS@@', pl[0]), ('@@ICON@@', pl[1]), ('@@HINT@@', pl[2]), ('@@PLAT@@', ag['plataforma']), ('@@SLUG@@', ag['slug']), ('@@REL@@', '../')):
        body = body.replace(k_, v_)
    body = re.sub(r'<!--GAL:(\w+)-->', lambda m: galeria(m.group(1), '../', ag), body)
    page = head('%s · fullservice-agents' % re.sub(r'<[^>]+>', '', md.inline(title)), '../', re.sub(r'<[^>]+>', '', md.inline(meta.get('resumen', ''))),
                '/%s/guia-%s' % (ag['slug'], kind), '%s-%s.png' % (ag['slug'], kind)) + topbar('../', 'guia-%s.pdf' % kind)
    otras = '<a class="btn ghost" href="guia-%s">%s</a>' % (other, TIPOS[other])      # al pie: la otra mirada del agente
    page += ('<div class="shell"><aside class="toc" data-lenis-prevent><p>En esta guía</p><ol>%s</ol></aside>\n<article>\n'
             '<p class="kicker">%s · %s</p>\n<h1>%s</h1>\n<p class="dek">%s</p>\n'
             '<div class="chips"><span>%s</span><span>%s</span><span>%s</span><span>%d min de lectura</span></div>\n%s\n'
             '<div class="more"><span>¿Buscas la otra mirada de este agente?</span><nav>'
             '%s<a class="btn ghost" href="../inicio">Todas las guías</a></nav></div>\n</article></div>\n%s\n%s\n</body>\n</html>\n'
             % (tocs, TIPOS[kind], html.escape(ag['slug']), md.inline(title), md.inline(meta.get('resumen', '')),
                FECHA, TIPOS[kind], plat(ag, '../'), mins, body, otras, scripts('../'), JS))
    return page


def corto(titulo):
    """Título sin el prefijo «<repo>: » (en el índice el nombre del repo ya va a la izquierda de la fila)."""
    t = re.sub(r'^[^:]+:\s*', '', titulo)
    return t[:1].upper() + t[1:]


def panel_md(archivo, pid, tid):
    """Panel del índice hecho con contenido/<archivo> (pestañas «Inicio» e «Instalación»), con su índice lateral."""
    meta, body, toc, words = md.convert((SRC / 'contenido' / archivo).read_text(encoding='utf-8'))
    body = re.sub(r'<!--GAL:(\w+)-->', lambda m: galeria(m.group(1), '', None), body)
    body = body.replace('@@REL@@', '')
    tocs = ''.join('<li><a href="#%s">%s</a></li>' % (i, html.escape(t)) for i, t in toc)
    return ('<section class="panel" id="%s" role="tabpanel" aria-labelledby="%s"><div class="shell"><aside class="toc" data-lenis-prevent><p>En esta página</p><ol>%s</ol></aside>'
            '<article>%s</article></div></section>' % (pid, tid, tocs, body))


def index_page(items, path='/inicio'):
    by = {(ag['slug'], m['tipo']): (m, w) for ag, m, w in items}

    def rows(kind):
        out = ''
        for ag in AGENTES:
            if (ag['slug'], kind) not in by:
                continue
            m, w = by[(ag['slug'], kind)]
            base = '%s/guia-%s' % (ag['slug'], kind)
            nice = '%s - %s.pdf' % ('Guia Desarrollador' if kind == 'dev' else 'Guia Usuario', ag['slug'])
            out += ('<div class="ag"><div><small class="plat-top">%s</small><h3><a class="ag-link" href="%s">%s</a></h3><small class="plat-bot">%s</small></div><p><b>%s</b>%s</p>'
                    '<div class="go"><small>%d min</small>'
                    '<a class="pdf" href="%s.pdf" download="%s" aria-label="Descargar PDF de %s" title="Descargar PDF">%s</a></div></div>\n'
                    % (html.escape(ag['nombre']), base, html.escape(ag['slug']), plat(ag, ''), md.inline(corto(m['titulo'])), md.inline(m['resumen']),
                       max(1, round(w / 210)), base, html.escape(nice), html.escape(ag['slug']), PDF_ICON))
        return out
    page = head('Guías de los agentes · fullservice-agents', '', 'Guías de usuario y de desarrollador de los siete agentes del flujo comercial de Campuslands, de la prospección al contrato. En línea y en PDF.',
                path, 'home.png').replace('<meta charset="UTF-8">\n', '<meta charset="UTF-8">\n<base href="/">\n', 1) + topbar('')
    page += ('<section class="banner"><div class="banner-in"><h1 class="wave" data-wave>fullservice-agents</h1>'
             '<p class="dek">Esta web es la guía de los agentes de este repositorio. Reúne, para cada uno de los siete agentes, '
             'una <strong>guía de usuario</strong>, sin tecnicismos, para quien lo usa todos los días, y una <strong>guía de desarrollador</strong>, '
             'para quien lo mantiene: carpetas, ciclos de trabajo, formatos, reglas y scripts. Si es tu primera vez, empieza por <strong>Inicio</strong> y sigue con <strong>Instalación</strong>: '
             'cómo instalar el repositorio y cómo usar los agentes.</p></div>%s</section>\n'
             '<nav class="tabbar"><div class="tabbar-in"><div class="tabs" role="tablist" aria-label="Secciones">'
             '<button type="button" role="tab" id="tab-inicio" aria-controls="inicio" aria-selected="true">Inicio</button>'
             '<button type="button" role="tab" id="tab-instalacion" aria-controls="instalar" aria-selected="false" tabindex="-1">Instalación</button>'
             '<button type="button" role="tab" id="tab-usuario" aria-controls="usuario" aria-selected="false" tabindex="-1">Guía de usuario</button>'
             '<button type="button" role="tab" id="tab-dev" aria-controls="dev" aria-selected="false" tabindex="-1">Guía de desarrollador</button>'
             '<span class="tab-ind" aria-hidden="true"></span></div></div></nav>\n'
             '<main class="home">%s%s'
             '<section class="panel" id="usuario" role="tabpanel" aria-labelledby="tab-usuario"><h2>Guías de usuario</h2><p class="sub">En el orden del flujo comercial, de la prospección al contrato.</p><div class="agents">%s</div></section>'
             '<section class="panel" id="dev" role="tabpanel" aria-labelledby="tab-dev"><h2>Guías de desarrollador</h2><p class="sub">Cómo está construido cada agente y cómo se mantiene.</p><div class="agents">%s</div></section></main>\n%s'
             '<footer class="site"><span>Campuslands S.A.S. BIC · Full Service</span>%s</footer>\n%s\n</body>\n</html>\n'
             % (BANNER_ART, panel_md('inicio.md', 'inicio', 'tab-inicio'), panel_md('instalacion.md', 'instalar', 'tab-instalacion'), rows('usuario'), rows('dev'), TABS_JS + ART_JS + JS, dock(''), scripts('')))
    return page


def make_pdf(html_path, pdf_path, title):
    from playwright.sync_api import sync_playwright
    hdr = ('<div style="width:100%%;padding:0 20mm;font:8px Arial,sans-serif;color:#87867f">%s</div>' % html.escape(title))
    ftr = ('<div style="width:100%;padding:0 20mm;font:8px Arial,sans-serif;color:#87867f;text-align:right">'
           'Página <span class="pageNumber"></span> de <span class="totalPages"></span></div>')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page()
        pg.goto(html_path.as_uri())
        pg.emulate_media(media='print')
        pg.evaluate('document.fonts.ready')
        pg.evaluate('window.cargarImagenes && window.cargarImagenes()')            # los carruseles cargan sus imágenes bajo demanda: aquí, todas
        pg.evaluate('window.revelarTodo && window.revelarTodo()')                  # los componentes que se animan al verse aparecen ya completos
        pg.wait_for_function('[...document.images].every(i => i.complete)', timeout=30000)
        pg.wait_for_timeout(500)
        pg.pdf(path=str(pdf_path), format='A4', print_background=True, display_header_footer=True, header_template=hdr, footer_template=ftr,
               margin=dict(top='22mm', bottom='20mm', left='20mm', right='20mm'))
        b.close()


def check_scale():
    """La hoja de estilos solo puede usar la escala tipográfica (variables --t-*): evita tamaños sueltos."""
    import re
    css = (SRC / 'estilo.css').read_text(encoding='utf-8')
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r':root\{[^}]*\}', '', css)            # definiciones de la escala
    css = re.sub(r'@media[^{]*\{\s*:root\{[^}]*\}', '@media{', css)   # redefiniciones por ancho / impresión
    bad = [v for v in re.findall(r'font-size:\s*([^;}]+)', css) if not (v.strip().startswith('var(--t-') or v.strip() == 'inherit')]
    if bad:
        raise SystemExit('estilo.css usa tamaños fuera de la escala: %s' % sorted(set(bad)))


def build(only=None, pdf=True):
    check_scale()
    (ROOT / 'assets').mkdir(exist_ok=True)
    (ROOT / 'assets' / 'estilo.css').write_text((SRC / 'estilo.css').read_text(encoding='utf-8'), encoding='utf-8')
    (ROOT / 'assets' / 'suave.js').write_text((SRC / 'suave.js').read_text(encoding='utf-8'), encoding='utf-8')
    (ROOT / 'assets' / 'efectos.js').write_text((SRC / 'efectos.js').read_text(encoding='utf-8'), encoding='utf-8')
    items = []
    for ag in AGENTES:
        for kind in ('dev', 'usuario'):
            src = SRC / 'contenido' / ag['slug'] / ('%s.md' % kind)
            if not src.exists():
                continue
            meta, body, toc, words = md.convert(src.read_text(encoding='utf-8'))
            meta['tipo'] = kind
            items.append((ag, meta, words))
            if only and ag['slug'] not in only:
                continue
            out = ROOT / ag['slug']
            out.mkdir(exist_ok=True)
            hp = out / ('guia-%s.html' % kind)
            hp.write_text(guide_page(ag, kind, meta, body, toc, words), encoding='utf-8')
            print('  %-26s %-8s %5d palabras · %d secciones' % (ag['slug'], kind, words, len(toc)))
            if pdf:
                make_pdf(hp, out / ('guia-%s.pdf' % kind), '%s · %s' % (ag['slug'], TIPOS[kind]))
    # El índice son cuatro archivos reales (misma página; solo cambia su dirección canónica) para que Vercel los sirva con cleanUrls, sin reescrituras.
    (ROOT / 'inicio').mkdir(exist_ok=True)
    (ROOT / 'inicio.html').write_text(index_page(items, '/inicio'), encoding='utf-8')
    (ROOT / 'inicio' / 'instalacion.html').write_text(index_page(items, '/inicio/instalacion'), encoding='utf-8')
    (ROOT / 'inicio' / 'usuario.html').write_text(index_page(items, '/inicio/usuario'), encoding='utf-8')
    (ROOT / 'inicio' / 'desarrollador.html').write_text(index_page(items, '/inicio/desarrollador'), encoding='utf-8')


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    build(args or None, '--sin-pdf' not in sys.argv)
