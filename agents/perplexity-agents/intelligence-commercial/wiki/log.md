# Bitácora — Explorador de Campus

Registro cronológico append-only. Prefijo: `## [YYYY-MM-DD] <tipo> |
<descripción>` donde tipo ∈ {setup, enriquecimiento, clasificacion,
redaccion, envio, lint}.

---

## [2026-07-16] setup | Creación del agente Explorador de Campus

Se crea la estructura inicial del agente de inteligencia comercial B2B:
`Perplexity.md` (identidad, flujo de 4 fases, decisiones fundacionales),
`wiki/index.md`, `wiki/perfiles-objetivo.md` (buyer personas) y la carpeta
`prospeccion/` para los lotes de trabajo. Se documentan como reglas fijas:
cero invención de datos firmográficos, y detección real de idioma del contacto
antes de redactar el mensaje.

## [2026-07-16] setup | Actualización de reglas de seguridad y envío autónomo

Se modifican los lineamientos de seguridad en `Perplexity.md` y las habilidades (`control-navegador-linkedin` y `generacion-mensajes-personalizados`) para permitir el envío automático y autónomo de solicitudes de conexión e invitaciones en LinkedIn sin requerir aprobación o revisión previa del usuario por lote o contacto. Se mantiene la restricción de pausas moderadas entre envíos para proteger la cuenta.

## [2026-07-30] lint | Corrección de contenido cruzado y reubicación de archivo suelto

A pedido del usuario, tras la auditoría general del monorepo:

1. **`wiki/perfil-usuario.md` y `wiki/marca-campuslands.md` tenían contenido de
   `PresentationsDesigner`** (audiencia de Directores Generales/CFOs/CTOs de LatAm para
   proyectos a la medida, y guía de paleta/tipografía para diapositivas) — un error de
   copiar y pegar al crear el agente que nunca se adaptó. Se reescribieron ambos con la
   identidad y audiencia reales de este agente (staffing de desarrolladores vía
   "Células de trabajo / Horas" de Full Service, prospectado entre Talento/RR. HH. y
   liderazgo técnico de empresas SaaS en EE. UU.), usando `recursos/Brief
   Fullservice.pdf`, `filtros-busqueda.md` y las plantillas ya existentes de
   `generacion-mensajes-personalizados/SKILL.md` como fuentes.
2. **Se retiraron los wikilinks `[[sistema-diseno]]` y `[[temas-por-cliente]]`**, que
   apuntaban a páginas de `PresentationsDesigner` inexistentes en esta wiki — este
   agente no depende de otro agente para funcionar.
3. **`filtros_estrategia_campuslands.md` estaba suelto en la raíz del repositorio**, sin
   indexar y con otro nombre — se reubicó a `wiki/filtros-busqueda.md`, el nombre que
   `habilidades/control-navegador-linkedin/SKILL.md` ya esperaba (esa skill tenía dos
   referencias rotas a un `filtros-busqueda.md` que nunca había existido). Se agregó a
   `wiki/index.md`.

## [2026-11-04] reorganización | Monorepo: `agents/` y recursos compartidos
Reorganización del monorepo: este agente pasó a `agents/perplexity-agents/intelligence-commercial/` (antes estaba en la raíz del repositorio). Los recursos de Campuslands que se repetían en cada agente (logos horizontal/vertical azul y blanco, isotipo, favicon, `Brief Fullservice.pdf` y Brandbook) se movieron a una sola carpeta compartida, `resources/campuslands-resources/` (desde este agente: `../../../resources/campuslands-resources/`), y se eliminaron las copias locales. Se eliminó `recursos/` (solo contenía la marca compartida). Si el Space de Perplexity necesita el brief o el brandbook, se suben desde `resources/campuslands-resources/`. Las rutas de la documentación de este agente se actualizaron; las entradas anteriores de esta bitácora conservan las rutas de su época.

## [2026-11-04] ajuste | Comandos «!»
Se incorporan los **comandos «!»**: órdenes cortas (`!optimize`, `!notime`, `!plan`…) que el agente ejecuta de forma obligatoria, dentro de sus reglas duras. Este agente tiene 26 comandos; la regla común, la tabla de comandos y su significado aquí están en la sección «Comandos» de `Perplexity.md`. Catálogo completo y decisiones: `resources/comandos/catalogo.md`.
