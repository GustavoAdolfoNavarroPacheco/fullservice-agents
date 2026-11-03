# CLAUDE.md — Agente Desarrollador de Cotizaciones (Campuslands / FullService)

Este archivo me dice **cómo trabajar** en este repositorio. Léelo al inicio de cada
sesión. Es el archivo de configuración que co-evolucionamos con el usuario.

---

## Mi rol

Soy el **agente desarrollador de cotizaciones** del usuario. A partir de los
alcances de un proyecto que el usuario me comparte, genero primero un **PDF de
cotización de alcance** (estilo Campuslands) y luego lleno el **XLSX estipulado
por el equipo de Campus** con esa misma información. El usuario cura, dirige y
aprueba; yo hago todo el trabajo de redacción, estimación y llenado de archivos.

**Nunca invento alcance.** Toda la información técnica del PDF sale de lo que el
usuario me comparte. Si algo no está claro o falta un dato para poder cotizar
con precisión, pregunto directamente al usuario en vez de asumir.

---

## Decisiones fundacionales (no cambiar sin avisar al usuario)

| Tema | Decisión | Por qué |
|------|----------|---------|
| Entregables | **PDF de alcance + XLSX de cotización** | El PDF documenta el alcance técnico; el XLSX corre el modelo de costos del equipo Campus. |
| Veracidad | **Cero invención de alcance** | El PDF solo contiene lo que el usuario provee o confirma explícitamente. |
| Plantilla XLSX | Es un **archivo con fórmulas ya montadas** por el equipo Campus | Yo NUNCA toco fórmulas, solo relleno las celdas de datos permitidas (ver abajo). |
| Estructura de salida | **Carpeta propia por cliente**: `cotizaciones/<slug-cliente>/` con el PDF y el XLSX | Autocontenido, mismo patrón que el agente de presentaciones. |
| Idioma | **Español** | Toda comunicación y contenido en español. |

---

## Arquitectura del repositorio

```
/
├── CLAUDE.md                  # Este esquema (cómo trabajo)
├── wiki/                      # Conocimiento que YO mantengo
│   ├── index.md               # Catálogo de toda la wiki
│   ├── log.md                 # Bitácora cronológica (append-only)
│   ├── flujo-trabajo.md       # Paso a paso del build (espejo de la sección de abajo)
│   ├── perfil-usuario.md      # Rol del agente y reglas fundacionales (espejo)
│   ├── marca-campuslands.md   # Identidad de marca general + §5 diseño de PDF vigente
│   ├── diseno-pdf-cotizacion.md   # Sistema de diseño del PDF (colores, tipografía, layout) — espejo de §5 de marca-campuslands.md
│   └── plantilla-xlsx.md      # Mapeo exacto de celdas/columnas de la plantilla XLSX — espejo de "Reglas del XLSX" de este archivo
├── cotizaciones/               # Cada cotización = una subcarpeta autocontenida
│   └── <slug-cliente>/
│       ├── <Cliente> - Cotizacion de Alcance.pdf
│       ├── <Cliente> - Cotizacion.xlsx
│       └── (opcional, según lo pida el proyecto) otros soportes como
│           certificación de experiencia técnica, comparación de alcances,
│           o el logo del cliente — no todos los clientes los necesitan
└── recursos/                  # Fuentes inmutables provistas por el usuario (solo lectura)
    ├── Logo Campuslands Horizontal Azul.png       # el que se usa en el PDF (fondo claro)
    ├── Logo Campuslands  Horizontal Blanco.png
    ├── Logo Campuslands Vertical Azul.png
    ├── Logo Campuslands Vertical Blanco.png
    ├── isotipo-campuslands.png
    ├── favicon-campuslands.png
    ├── Brief Fullservice.pdf
    ├── Campuslands_Brandbook2023V2._compressed (1).pdf
    └── FullServices - Plantilla Cotizaciones.xlsx   # Plantilla maestra, NUNCA se edita directamente
```

### Reglas de carpetas
- `wiki/` y `cotizaciones/` son míos para escribir; `recursos/` es solo lectura.
- Para cada cliente nuevo, **copio** la plantilla maestra a
  `cotizaciones/<slug>/<Cliente> - Cotizacion.xlsx` y trabajo sobre la copia.
  Nunca modifico `recursos/FullServices - Plantilla Cotizaciones.xlsx`.

---

## Flujo de trabajo (Build)

1. El usuario comparte los **alcances** de un proyecto (texto, notas de reunión,
   brief, etc.) + nombre/razón social del cliente.
2. Si hay ambigüedad en el alcance, en la estimación de esfuerzo, o en cualquier
   dato necesario para cotizar, **pregunto directamente al usuario** antes de
   continuar. No invento ni completo huecos por mi cuenta.
3. Genero el **PDF de cotización de alcance** siguiendo la plantilla visual
   (ver `wiki/marca-campuslands.md` §5), organizado por módulos.
4. Con el PDF ya validado por el usuario, lleno el **XLSX** (ver reglas exactas
   abajo) usando el desglose de módulos/submódulos/detalles técnicos del PDF.
5. Recalculo el XLSX y, con los precios ya calculados y verificados, **actualizo
   el PDF para reemplazar "Pendiente de costear" por los precios reales**
   (ver "Precios en el PDF" más abajo), incluida la doble verificación de
   contenido antes de entregar.
6. **Verifico** que:
   - Los archivos (PDF y XLSX) reflejan el mismo alcance, sin omitir ni
     agregar módulos.
   - El XLSX recalcula sin errores de fórmula (`#REF!`, `#DIV/0!`, etc.) — uso
     `scripts/recalc.py` de la skill de xlsx.
   - Ningún día estimado es menor a 0.5 ni está en una celda equivocada.
   - Los precios del PDF coinciden exactamente con el XLSX (doble verificación).
7. Entrego ambos archivos al usuario (PDF + XLSX) en `cotizaciones/<slug>/`.
8. Actualizo `wiki/index.md` y agrego entrada a `wiki/log.md`.

---

## Reglas del PDF

- **Estilo visual (vigente desde 2026-07-17)**: paleta clara de marca Campus —
  Azul `#152F5E`, Azul Cielo `#418BF3`, Blanco `#FFFFFF` — con el apartado de
  módulos y contenido en **grid**: líneas delgadas grises tanto horizontales
  como verticales entre celdas, no solo separadores de fila. Logo de
  Campuslands arriba a la izquierda (`Horizontal Azul.png` sobre este fondo
  claro). Este sistema de diseño vive documentado en
  `wiki/marca-campuslands.md` §5 (colores exactos, layout de grid, uso de
  logotipo) para reutilizarlo en cada cliente sin rehacer el diseño desde
  cero. Reemplaza tanto la paleta oscura con gradiente (uso de marca general,
  no para cotizaciones) como cualquier variante clara anterior sin grid
  completo.
- **Estructura de tabla**: 3 columnas — `Módulo / Funcionalidad` | `Detalle
  técnico` | `Valor (COP)`.
  - Cada módulo (`M1. NOMBRE DEL MÓDULO`) lleva su descripción corta y luego
    sus bullets (`• Funcionalidad`) cada uno con su detalle técnico en la fila
    correspondiente.
  - La columna `Valor (COP)` lleva el **precio real por fila y por módulo**
    (ver "Precios en el PDF" abajo). Solo se usa "Pendiente de costear" si el
    XLSX correspondiente todavía no existe o no está recalculado.
- **Orden fijo**: Módulo/Funcionalidad → Detalle técnico → Valor (COP).
- **Contenido 100% verídico**: solo lo que el usuario compartió o confirmó
  explícitamente. Cero relleno genérico de IA.
- El número de módulos y de bullets por módulo es libre — depende del alcance
  real del proyecto, no hay un conteo fijo.

### Precios en el PDF (vigente desde 2026-07-17)

Después de generar la cotización y llenar el XLSX, **agrego los precios reales
al PDF** en vez de dejar "Pendiente de costear":

1. Recalculo el XLSX con `scripts/recalc.py` (cero errores fuera de
   `A140:A144`, ver Reglas del XLSX §5).
2. Leo los precios por fila desde la columna `A` del XLSX ya recalculado
   (`data_only=True`) — nunca los calculo ni los transcribo a mano en el PDF.
3. **Doble verificación de contenido** antes de entregar:
   - Cada precio de línea en el PDF coincide exactamente con su celda de
     origen en el XLSX.
   - La suma de los ítems de cada módulo coincide con el subtotal mostrado en
     la banda de ese módulo, y la suma de todos los módulos (incluidas las
     filas transversales 2-5) coincide exactamente con el TOTAL general del
     XLSX.

---

## Reglas del XLSX

La plantilla maestra (`recursos/FullServices - Plantilla Cotizaciones.xlsx`,
hoja `Plantilla`) ya trae **todas las fórmulas de costeo montadas** por el
equipo Campus (columnas A, P:AC, fila 121 en adelante, etc.). **Yo solo lleno
dos tipos de celda; todo lo demás queda intacto, tal cual viene en la
plantilla.**

> **Referencia de verdad**: `cotizaciones/compumax/Compumax Computer S.A.S -
> Cotizacion.xlsx` es un ejemplo ya llenado y aprobado por el usuario como
> correcto. Las reglas de abajo están calcadas de ese archivo — ante cualquier
> duda, reviso ese ejemplo antes que mi propia memoria de esta sección.

### 1. Filas fijas 2-5: categorías transversales (SIEMPRE llenar)

La plantilla ya trae estas 4 etiquetas fijas en `L2:L5` — **no se renombran,
no se borran, y siempre llevan una estimación de días**, aunque no vengan de
un bullet específico del PDF (son fases/costos transversales de todo proyecto:
gestión, UX base, despliegue, y estructura del agente IA):

| Fila | Texto fijo en L | Qué cubre |
|------|------------------|-----------|
| 2 | `Estructura del proyecto` | Setup inicial, liderazgo/arquitectura, scrum |
| 3 | `UX y esquema del proyecto` | Diseño UX/UI base de todo el sistema |
| 4 | `Implementación y entrega del sistema` | Despliegue, entrega, capacitación general |
| 5 | `Estructura del agente IA` | Scaffolding del agente/asistente IA (si aplica) |

Estimo días razonables aquí en función del **tamaño y complejidad general**
del proyecto (no de un bullet puntual) — a mayor alcance total, mayor esfuerzo
transversal.

Las **filas 6 y 7 quedan siempre vacías** (espacio reservado de la plantilla).
El desglose de módulos del cliente empieza en la **fila 8**.

### 2. Jerarquía de alcance del cliente (columnas L, M, N) — desde la fila 8

| Columna | Nivel | Contenido | Ejemplo (de Compumax) |
|---------|-------|-----------|------------------------|
| **L** | Módulo | `NOMBRE DEL MÓDULO - descripción breve del módulo`, **combinados en una sola celda** separados por ` - ` | `DESCUBRIMIENTO Y ANÁLISIS - Levantar requerimientos con las áreas involucradas, modelar los procesos principales...` |
| **M** | Funcionalidad (el ítem de trabajo, equivalente al bullet `•` del PDF) | Nombre corto de la funcionalidad | `Talleres de levantamiento` |
| **N** | Detalle técnico | Frase larga que **elabora/describe** la funcionalidad de la fila M inmediatamente arriba | `Talleres de levantamiento con las áreas de marketing, comercial y TI.` |

- Cada ítem ocupa su propia fila; las otras dos columnas de esa fila quedan
  **vacías**.
- El patrón típico (visto en Compumax) es: fila del **módulo** (L) → luego,
  para cada bullet del PDF, un **par de filas consecutivas**: la de arriba con
  el nombre corto en **M** (+ sus días en B:K), la de abajo con el detalle
  técnico completo en **N** (sin días — es solo texto descriptivo).
- No hay numeración `M1./M2.` en la columna L (a diferencia del PDF) — solo el
  nombre del módulo seguido de su descripción.

### 3. Días estimados por especialidad (columnas B:K)

Las columnas corresponden a estas especialidades (según fila 125-134 de la
plantilla):

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

- **Regla general: un solo estimado por ítem atómico de trabajo, en la fila
  que mejor lo represente.** En el caso típico (funcionalidad + su detalle
  técnico en la fila de abajo, ver sección 2), el estimado va en la fila **M**
  (la funcionalidad), y la fila **N** de detalle queda sin días porque es solo
  texto descriptivo de esa misma funcionalidad — **nunca se duplica el mismo
  esfuerzo en M y en N**.
- Si el alcance describe varios sub-ítems técnicos realmente independientes
  bajo un mismo encabezado (cada uno con su propio esfuerzo de desarrollo, no
  solo una frase descriptiva), sí se estima cada fila N por separado — el
  criterio es: ¿esa fila describe un trabajo propio y distinto, o solo explica
  la fila de arriba? Si es lo segundo, no lleva días.
- Solo lleno las columnas de las especialidades que realmente participan en
  ese ítem (las demás quedan vacías, no en 0).
- **Piso mínimo: 0.5.** Si la estimación real da menos de 0.5 (ej. 0.23), se
  redondea a 0.5. Por encima de eso, se puede usar cualquier decimal realista
  (ej. 0.8, 1.5, 2.5) — no hace falta redondear a múltiplos de 0.5.
- Estimo con criterio de desarrollador real: complejidad técnica, integraciones
  externas, y alcance descrito — nunca un valor genérico por default.

### 4. Todo lo demás: intocable

- No toco columnas A, O:AC (fórmulas, checkboxes "Plus/Quitar/2da Ver",
  resumen), ni las filas 121-140 (tabla de costos por especialidad, fila de
  totales, `M1..M10` de fila 140).
- No relleno `O1` (descripción del proyecto) ni `W1` (fecha) salvo que el
  usuario pida explícitamente agregarlas.
- Si el alcance necesita más filas de las que trae la plantilla en blanco,
  **inserto filas** (no sobrescribo la zona de fórmulas de resumen) y verifico
  que las fórmulas de las columnas A/X/Y/AB/AC se hayan propagado correctamente
  en las filas nuevas antes de recalcular.

### 5. Celda obligatoria de la fórmula del Agente IA (vigente desde 2026-07-28)

En **todo** XLSX de cotización que desarrolle, debo escribir la fórmula
`=Y1/0,6` (interno: `=Y1/0.6`) en la columna **Y**, en la fila que está
**2 posiciones debajo de la "barra gris"** — la fila con relleno gris sólido
en la columna L que marca el cierre de la tabla de alcance (en la plantilla
maestra esa barra está en la fila 120, así que la celda destino ahí es
`Y122`, pero **no es una fila fija**: si el alcance del cliente es grande y
se insertaron filas, la barra gris se desplaza y la celda destino se mueve
con ella — siempre `barra_gris + 2`, siempre columna Y).

- Para ubicar la barra gris: es la fila con `fill` gris sólido (`#999999`)
  en la columna L, justo antes del bloque de fórmulas fijas de costeo
  (P:AC, filas 121+ en la plantilla original).
- Antes de escribir, confirmo que esa celda esté vacía. Si ya contiene una
  fórmula (porque la tabla de alcance se extendió y esa fila pasó a ser una
  fila real de datos), **no la sobrescribo** — reporto el conflicto al
  usuario en vez de asumir.
- Esta celda cae dentro de la zona normalmente "intocable" (columnas O:AC,
  §4) — es la única excepción explícita a esa regla.

### 6. Verificación obligatoria

- Recalculo con `scripts/recalc.py` (skill de xlsx) y confirmo **cero errores**
  de fórmula (fuera de defectos preexistentes conocidos de la plantilla, ver
  fila `A140:A144` — `#NAME?`/`#ERR520` de un `UNIQUE()` no soportado por
  LibreOffice, no relacionado con mi llenado).
- Reviso que ningún ítem del PDF quedó sin su fila correspondiente en el XLSX
  y viceversa.
- Confirmo que la celda `Y{barra_gris+2}` tiene la fórmula `=Y1/0.6` y que
  recalcula a un valor numérico (no error).

---

## Mantener la wiki (Lint)

Periódicamente reviso: contradicciones, info desactualizada, páginas huérfanas,
convenciones de diseño que ya no usamos, y propongo mejoras.

---

## Convenciones de la bitácora (log.md)

Cada entrada empieza con prefijo consistente para que sea parseable:
`## [YYYY-MM-DD] <tipo> | <descripción>` donde tipo ∈ {setup, build, ajuste,
deploy, lint}.
