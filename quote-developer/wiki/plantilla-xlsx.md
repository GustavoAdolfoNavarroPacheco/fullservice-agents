# Mapeo de la plantilla XLSX de cotización

> **Fuente canónica: `CLAUDE.md` § Reglas del XLSX.** Ese archivo es el que el
> agente lee al inicio de cada sesión y el que manda si alguna vez difiere de
> esta página. Esta página existe para que el árbol de archivos de `CLAUDE.md`
> sea preciso y para tener el mapeo consultable desde el catálogo de la wiki
> (`wiki/index.md`) — se actualiza junto con `CLAUDE.md` en cada ajuste (ver
> "Mantener la wiki (Lint)" en `CLAUDE.md`).

La plantilla maestra (`recursos/FullServices - Plantilla Cotizaciones.xlsx`,
hoja `Plantilla`) ya trae **todas las fórmulas de costeo montadas** por el
equipo Campus (columnas A, P:AC, fila 121 en adelante, etc.). El agente solo
llena dos tipos de celda; todo lo demás queda intacto, tal cual viene en la
plantilla.

**Referencia de verdad**: `cotizaciones/compumax/Compumax Computer S.A.S -
Cotizacion.xlsx` es un ejemplo ya llenado y aprobado por el usuario como
correcto. Las reglas de abajo están calcadas de ese archivo.

## 1. Filas fijas 2-5: categorías transversales (SIEMPRE llenar)

La plantilla ya trae estas 4 etiquetas fijas en `L2:L5` — no se renombran, no
se borran, y siempre llevan una estimación de días, aunque no vengan de un
bullet específico del PDF (son fases/costos transversales de todo proyecto:
gestión, UX base, despliegue, y estructura del agente IA):

| Fila | Texto fijo en L | Qué cubre |
|------|------------------|-----------|
| 2 | `Estructura del proyecto` | Setup inicial, liderazgo/arquitectura, scrum |
| 3 | `UX y esquema del proyecto` | Diseño UX/UI base de todo el sistema |
| 4 | `Implementación y entrega del sistema` | Despliegue, entrega, capacitación general |
| 5 | `Estructura del agente IA` | Scaffolding del agente/asistente IA (si aplica) |

Se estiman días razonables aquí en función del tamaño y complejidad general
del proyecto (no de un bullet puntual) — a mayor alcance total, mayor esfuerzo
transversal.

Las **filas 6 y 7 quedan siempre vacías** (espacio reservado de la plantilla).
El desglose de módulos del cliente empieza en la **fila 8**.

## 2. Jerarquía de alcance del cliente (columnas L, M, N) — desde la fila 8

| Columna | Nivel | Contenido | Ejemplo (de Compumax) |
|---------|-------|-----------|------------------------|
| **L** | Módulo | `NOMBRE DEL MÓDULO - descripción breve del módulo`, combinados en una sola celda separados por ` - ` | `DESCUBRIMIENTO Y ANÁLISIS - Levantar requerimientos con las áreas involucradas, modelar los procesos principales...` |
| **M** | Funcionalidad (el ítem de trabajo, equivalente al bullet `•` del PDF) | Nombre corto de la funcionalidad | `Talleres de levantamiento` |
| **N** | Detalle técnico | Frase larga que elabora/describe la funcionalidad de la fila M inmediatamente arriba | `Talleres de levantamiento con las áreas de marketing, comercial y TI.` |

- Cada ítem ocupa su propia fila; las otras dos columnas de esa fila quedan
  vacías.
- El patrón típico (visto en Compumax) es: fila del **módulo** (L) → luego,
  para cada bullet del PDF, un par de filas consecutivas: la de arriba con el
  nombre corto en **M** (+ sus días en B:K), la de abajo con el detalle
  técnico completo en **N** (sin días — es solo texto descriptivo).
- No hay numeración `M1./M2.` en la columna L (a diferencia del PDF) — solo el
  nombre del módulo seguido de su descripción.

## 3. Días estimados por especialidad (columnas B:K)

| Col | Código | Especialidad |
|-----|--------|--------------|
| B | DB | DB, Líder, Arquitecto, Scrum |
| C | UX | Diseño UI/UX |
| D | FM | FrontEnd Medium |
| E | BS | BackEnd Senior |
| F | BM | BackEnd Semi-Senior |
| G | QA | QA, Test |
| H | IM | Implementación, Capacitación |
| I | MS | Mobile Semi-Senior |
| J | MM | Mobile Medium |
| K | IA | BackEnd IA |

- Un solo estimado por ítem atómico de trabajo, en la fila que mejor lo
  represente. En el caso típico (funcionalidad + su detalle técnico en la
  fila de abajo), el estimado va en la fila **M**; la fila **N** de detalle
  queda sin días — nunca se duplica el mismo esfuerzo en M y en N.
- Si el alcance describe varios sub-ítems técnicos realmente independientes
  bajo un mismo encabezado, sí se estima cada fila N por separado — el
  criterio es si esa fila describe un trabajo propio y distinto, o solo
  explica la fila de arriba.
- Solo se llenan las columnas de las especialidades que realmente participan
  en ese ítem (las demás quedan vacías, no en 0).
- **Piso mínimo: 0.5.** Por encima de eso, cualquier decimal realista.

## 4. Todo lo demás: intocable

- No se tocan columnas A, O:AC (fórmulas, checkboxes, resumen), ni las filas
  121-140 (tabla de costos por especialidad, totales, `M1..M10` de fila 140).
- No se rellena `O1` (descripción del proyecto) ni `W1` (fecha) salvo pedido
  explícito del usuario.
- Si el alcance necesita más filas de las que trae la plantilla en blanco, se
  **insertan filas** (nunca se sobrescribe la zona de fórmulas de resumen) y
  se verifica que las fórmulas de las columnas A/X/Y/AB/AC se hayan propagado
  correctamente en las filas nuevas antes de recalcular.

## 5. Celda obligatoria de la fórmula del Agente IA (vigente desde 2026-07-28)

En todo XLSX de cotización se escribe la fórmula `=Y1/0,6` (interno:
`=Y1/0.6`) en la columna **Y**, en la fila que está **2 posiciones debajo de
la "barra gris"** — la fila con relleno gris sólido (`#999999`) en la columna
L que marca el cierre de la tabla de alcance. En la plantilla maestra esa
barra está en la fila 120 (celda destino `Y122`), pero no es una fila fija:
si el alcance del cliente es grande y se insertaron filas, la barra gris se
desplaza y la celda destino se mueve con ella — siempre `barra_gris + 2`,
siempre columna Y.

- Antes de escribir, se confirma que esa celda esté vacía. Si ya contiene una
  fórmula (porque la tabla de alcance se extendió y esa fila pasó a ser una
  fila real de datos), no se sobrescribe — se reporta el conflicto al usuario.
- Esta celda cae dentro de la zona normalmente "intocable" (§4) — es la única
  excepción explícita a esa regla.

## 6. Verificación obligatoria

- Recalcular con `scripts/recalc.py` (skill de xlsx) y confirmar **cero
  errores** de fórmula, fuera de defectos preexistentes conocidos de la
  plantilla (`A140:A144` — `#NAME?`/`#ERR520` de un `UNIQUE()` no soportado
  por LibreOffice, no relacionado con el llenado del agente).
- Revisar que ningún ítem del PDF quedó sin su fila correspondiente en el
  XLSX y viceversa.
- Confirmar que la celda `Y{barra_gris+2}` tiene la fórmula `=Y1/0.6` y que
  recalcula a un valor numérico (no error).
