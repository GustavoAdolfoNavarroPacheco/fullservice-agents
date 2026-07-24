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
