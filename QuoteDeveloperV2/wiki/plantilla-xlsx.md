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

**Referencia de verdad — B:K, fórmula de Y, zona intocable**: `cotizaciones/compumax/
Compumax Computer S.A.S - Cotizacion.xlsx` sigue siendo válido para las
columnas B:K, la fórmula de Y y el manejo de la zona intocable. **Su columna
L/M/N sigue el patrón antiguo de "1 submódulo = 1 funcionalidad", superado el
2026-08-05** — no usar ese archivo como referencia de cardinalidad.

**Referencia de verdad — cardinalidad L/M/N (desde 2026-08-05)**:
`cotizaciones/comultrasan/Financiera Comultrasan - Cotizacion.xlsx` es la
primera cotización construida bajo la regla de jerarquía flexible: 5 módulos,
con 1 a 4 funcionalidades por submódulo según lo que el alcance real de cada
uno necesitaba (nunca forzado a un patrón fijo). Úsala como ejemplo de
cardinalidad variable real.

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

## 2. Jerarquía flexible de alcance del cliente (columnas L, M, N) — desde la fila 8

**Regla central (vigente desde 2026-08-05 — reemplaza el patrón fijo
anterior):** la cantidad de funcionalidades (N) bajo cada submódulo (M) es
**libre**, tantas como el alcance real necesite. Queda prohibido forzar el
patrón antiguo de "1 submódulo = 1 descripción" — el nivel de detalle debe
reflejar la complejidad real de cada parte del alcance, igual que lo haría
una cotización elaborada a mano.

| Columna | Nivel | Contenido | Cardinalidad |
|---------|-------|-----------|--------------|
| **L** | Módulo | `NOMBRE DEL MÓDULO - descripción breve del módulo`, combinados en una sola celda separados por ` - ` | Una fila por módulo |
| **M** | Submódulo | Encabezado corto de una agrupación temática dentro del módulo (sin días propios) | Puede repetirse varias veces bajo un mismo módulo |
| **N** | Funcionalidad | Frase autocontenida que describe una funcionalidad concreta y atómica (con sus días en B:K, ver §3) | Puede repetirse varias veces bajo un mismo submódulo (mínimo 1) |

Ejemplo de estructura correcta (cardinalidad variable):

```
L: MÓDULO A - descripción breve
M: Submódulo 1
N: Funcionalidad 1 (con sus días)
N: Funcionalidad 2 (con sus días)
N: Funcionalidad 3 (con sus días)
M: Submódulo 2
N: Funcionalidad 1 (con sus días)
L: MÓDULO B - descripción breve
M: Submódulo 1
N: Funcionalidad 1 (con sus días)
N: Funcionalidad 2 (con sus días)
```

- Cada fila (L, M o N) ocupa su propia fila; las otras dos columnas de esa
  fila quedan vacías.
- Criterio de cardinalidad: ¿cuántas funcionalidades atómicas y realmente
  distintas describe el alcance para ese submódulo? Ni una menos, ni una de
  más forzada artificialmente. Debe ser fiel al alcance compartido por el
  usuario (regla de veracidad, ver `perfil-usuario.md`).
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

- **Regla vigente desde 2026-08-05 (reemplaza la anterior): el estimado va
  siempre en la fila de la funcionalidad (N). El submódulo (M) nunca lleva
  días** — es un encabezado de agrupación. Cada funcionalidad N bajo un mismo
  submódulo lleva su propio estimado independiente; nunca se reparte ni se
  promedia un solo estimado entre varias filas N.
- Solo se llenan las columnas de las especialidades que realmente participan
  en esa funcionalidad (las demás quedan vacías, no en 0).
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

## 5. Celdas obligatorias dentro de la zona de fórmulas (excepciones explícitas)

Las únicas dos excepciones documentadas a la regla "todo lo demás es
intocable" (§4). Ambas se ubican en relación a la **barra gris** — la fila
con relleno gris sólido (`#999999`) en la columna L que marca el cierre de la
tabla de alcance (fila 120 en la plantilla maestra, pero se desplaza si se
insertaron filas por un alcance grande).

| Celda (relativa a la barra gris) | En la plantilla maestra (barra gris = fila 120) | Contenido obligatorio | Vigente desde |
|---|---|---|---|
| Columna **Y**, fila `barra_gris + 2` | `Y122` | Fórmula `=Y1/0,6` (interno `=Y1/0.6`) | 2026-07-28 |
| Columna **R**, fila `barra_gris + 3` | `R123` | Valor `0.1` (10%) — reemplaza el default de la plantilla maestra (40%) | 2026-08-05 |

- `R{barra_gris+3}` es la celda de porcentaje **AIU** (etiquetada
  `Q{barra_gris+3}='AIU'` en la misma fila) — se confirma por esa etiqueta
  antes de escribir, no solo por el número de fila.
- Antes de escribir en cualquiera de las dos, se confirma que esté vacía o
  con el valor/fórmula esperado de la plantilla original. Si ya contiene
  datos de una fila real de alcance, no se sobrescribe — se reporta el
  conflicto al usuario.
- Ambas celdas caen dentro de la zona normalmente "intocable" (§4) — son las
  únicas excepciones explícitas a esa regla.

## 5b. Aclaraciones/condiciones sin celda propia (vigente desde 2026-08-06)

Cuando el usuario pide dejar una aclaración o condición comercial sobre una fila o módulo (ej.
"este cobro aplica solo si...") y no hay una celda de texto libre apropiada para eso (y la fila
cae en zona intocable o simplemente no hay dónde escribirlo sin tocar valores/fórmulas), se usa
un **comentario de celda de Excel** (`openpyxl.comments.Comment`) sobre la celda L/M relevante
(módulo o submódulo) — no cambia ningún valor ni fórmula, es metadato adjunto a la celda,
visible al pasar el cursor en Excel. Verificar después de esto que el archivo sigue
recalculando sin errores nuevos y que el comentario sobrevive el recálculo con LibreOffice
(confirmado que sí, en la práctica).

## 6. Verificación obligatoria

- Recalcular con `scripts/recalc.py` (skill de xlsx) y confirmar **cero
  errores** de fórmula, fuera de defectos preexistentes conocidos de la
  plantilla (`A140:A144` — `#NAME?`/`#ERR520` de un `UNIQUE()` no soportado
  por LibreOffice, no relacionado con el llenado del agente).
- Revisar que ningún ítem del PDF quedó sin su fila correspondiente en el
  XLSX y viceversa (a nivel de módulo, submódulo y funcionalidad).
- Confirmar que cada funcionalidad (fila N) tiene sus propios días y que
  ningún submódulo (fila M) quedó con días cargados por error.
- Confirmar que la celda `Y{barra_gris+2}` tiene la fórmula `=Y1/0.6` y que
  recalcula a un valor numérico (no error).
- Confirmar que la celda `R{barra_gris+3}` tiene el valor `0.1` (10%) y que
  se refleja en la columna P (Valor Hora) de la tabla de costos fija.
