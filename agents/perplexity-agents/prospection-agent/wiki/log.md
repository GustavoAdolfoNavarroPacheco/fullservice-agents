# Bitácora — Radar de Campus

Registro cronológico append-only. Prefijo: `## [YYYY-MM-DD] <tipo> |
<descripción>` donde tipo ∈ {setup, busqueda, enriquecimiento, entrega, lint}.

---

## [2026-07-23] setup | Creación del agente Radar de Campus

Se crea la estructura inicial del agente de prospección de empresas vía web
abierta (sin LinkedIn): `Perplexity.md` (identidad, flujo de 3 fases,
decisiones fundacionales, deslinde explícito con `IntelligenceCommercial`),
`wiki/filtros-busqueda.md` (menú fijo de 4 filtros predefinidos + opción
libre "Otro"), `wiki/perfil-usuario.md` (ICP heredado y adaptado del ICP de
LinkedIn), `wiki/enlaces-utiles.md` (fuentes web permitidas) y 4 skills en
`habilidades/` (menú de filtros, búsqueda web, enriquecimiento, generación
de listado). Se documenta como regla fija: cero invención de datos
firmográficos y prohibición explícita de usar LinkedIn/Sales Navigator —
ese dominio queda reservado para `IntelligenceCommercial`.

## [2026-07-23] setup | Reemplazo del menú de filtros por formulario de intake fijo

Se elimina `wiki/filtros-busqueda.md` (menú de 4 filtros + "Otro") y se
reemplaza por `wiki/formulario-intake.md`: un formulario fijo de 6 datos
(Número de Empresas, Sector, Ubicación, Tamaño, Número de empleados,
Facturación anual) que se pide al **empezar cada conversación**, con regla
de obligatoriedad flexible (si el usuario no sabe un dato, se avanza sin
ese filtro). Se renombra la skill `menu-filtros-busqueda` a
`formulario-intake`. Se cambian las columnas de salida del listado a: Fecha,
Razón Social, Ubicación, Número de Empleados, Facturación Anual, Utilidad
Neta — se retiran Sitio Web, Sector y Señal Relevante de la tabla entregada
al usuario (Sector y Ubicación quedan como criterios de búsqueda del
formulario; la trazabilidad de fuente se mantiene como pie de tabla, no
como columna). Se agrega en `wiki/enlaces-utiles.md` la Superintendencia de
Sociedades (SIREM) como fuente primaria para Facturación Anual y Utilidad
Neta de empresas colombianas.

## [2026-07-30] setup | Recursos de marca Campuslands copiados de IntelligenceCommercial

`recursos/` solo tenía un `.gitkeep`, sin propósito definido. Se copian de
`IntelligenceCommercial/recursos/` los mismos 8 archivos de marca Campuslands
(Brief Fullservice, brandbook, 4 variantes de logo, isotipo, favicon) para
que este agente quede autocontenido como el resto del monorepo, y se retira
el `.gitkeep`. No cambia el flujo de trabajo del agente (no busca contactos
ni redacta mensajes, así que estos archivos son de referencia/identidad, no
insumo directo de ninguna skill actual).

## [2026-11-04] reorganización | Monorepo: `agents/` y recursos compartidos
Reorganización del monorepo: este agente pasó a `agents/perplexity-agents/prospection-agent/` (antes estaba en la raíz del repositorio). Los recursos de Campuslands que se repetían en cada agente (logos horizontal/vertical azul y blanco, isotipo, favicon, `Brief Fullservice.pdf` y Brandbook) se movieron a una sola carpeta compartida, `resources/campuslands-resources/` (desde este agente: `../../../resources/campuslands-resources/`), y se eliminaron las copias locales. Se eliminó `recursos/` (solo contenía la copia de la marca compartida). Las rutas de la documentación de este agente se actualizaron; las entradas anteriores de esta bitácora conservan las rutas de su época.

## [2026-11-04] ajuste | Comandos «!»
Se incorporan los **comandos «!»**: órdenes cortas (`!optimize`, `!notime`, `!plan`…) que el agente ejecuta de forma obligatoria, dentro de sus reglas duras. Este agente tiene 26 comandos; la regla común, la tabla de comandos y su significado aquí están en la sección «Comandos» de `Perplexity.md`. Catálogo completo y decisiones: `resources/comandos/catalogo.md`.
