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
- **Nomenclatura corta (vigente desde 2026-08-06)**: Excel tiene un límite de
  ruta propio más estricto que el de Windows (260) — confirmado con Excel real
  vía COM, una ruta de ~236 caracteres falla con "no hemos encontrado el
  archivo" aunque el archivo sea válido. Nombres de archivo/carpeta cortos y
  sin tildes (el contenido interno sigue en español con tildes normales). Para
  un cliente con **múltiples proyectos** (cotizaciones separadas por
  proyecto): `cotizaciones/<slug-cliente>/<slug-proyecto>/` con archivos
  simplemente `Cotizacion.xlsx` y `Cotizacion de Alcance.pdf` (sin repetir
  cliente/proyecto en el nombre — ya está en la ruta). Mantener la ruta
  completa bajo ~180 caracteres.

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
- **Estructura de tabla**: 3 columnas — `Módulo / Submódulo` | `Detalle
  técnico` | `Valor (COP)`.
- **Jerarquía flexible (vigente desde 2026-08-05 — reemplaza el patrón fijo
  anterior)**: `Módulo → Submódulo → Funcionalidad(es)`, con **cardinalidad
  libre en cada nivel**:
  - Cada módulo (`M1. NOMBRE DEL MÓDULO`) lleva su descripción corta.
  - Dentro de un módulo puede haber **uno o varios submódulos** (encabezados
    de agrupación temática, sin precio propio).
  - Dentro de cada submódulo puede haber **una o varias funcionalidades**
    (bullets `•`), cada una en su propia fila con su propio precio en la
    columna `Valor (COP)`. **Nunca se fuerza "1 submódulo = 1 funcionalidad"**
    — la cantidad de bullets depende exclusivamente de cuántas funcionalidades
    atómicas y realmente distintas describe el alcance para ese submódulo.
    Prohibido agrupar varias funcionalidades en un solo bullet para ahorrar
    espacio, y prohibido fragmentar una sola funcionalidad en bullets
    artificiales para aparentar más detalle — la cardinalidad refleja
    fielmente el alcance real (regla de veracidad, ver `wiki/perfil-usuario.md`).
  - Esta jerarquía es un espejo exacto de la del XLSX (`wiki/plantilla-xlsx.md`
    §2): Módulo=L, Submódulo=M, Funcionalidad=N. El PDF nunca debe mostrar
    menos ni más nivel de detalle que el que efectivamente quedó cargado en el
    XLSX correspondiente.
  - La columna `Valor (COP)` lleva el **precio real por fila de funcionalidad
    y por módulo** (ver "Precios en el PDF" abajo). El submódulo, al no llevar
    días propios (ver `wiki/plantilla-xlsx.md` §3), tampoco lleva precio en su
    propia fila. Solo se usa "Pendiente de costear" si el XLSX correspondiente
    todavía no existe o no está recalculado.
- **Tipografía (vigente desde 2026-08-05)**: fuente Arial en toda la tabla de
  alcance, con tres pesos fijos según el nivel:

  | Nivel | Tamaño | Peso |
  | :--- | :--- | :--- |
  | Módulo | 11 pt | Negrita |
  | Submódulo | 10 pt | Negrita |
  | Funcionalidad / Detalle técnico | 10 pt | Regular |

- **Orden fijo**: Módulo → Submódulo → Funcionalidad (Detalle técnico) → Valor
  (COP).
- **Contenido 100% verídico**: solo lo que el usuario compartió o confirmó
  explícitamente. Cero relleno genérico de IA.
- El número de módulos, de submódulos por módulo, y de funcionalidades por
  submódulo es libre — depende del alcance real del proyecto, no hay un
  conteo fijo ni un patrón repetido artificialmente.
- **Atomicidad de bullets compuestos (vigente desde 2026-08-06)**: un bullet
  de la fuente que une varias cosas con "y"/comas se divide en funcionalidades
  separadas solo si cada una es una capacidad genuinamente distinta
  (verbos/acciones diferentes). No se divide cuando el bullet enumera
  dimensiones/niveles de una sola capacidad (ej. "por series, subseries,
  expedientes y dependencias" = una taxonomía, una funcionalidad). Ver
  `wiki/marca-campuslands.md` §5.
- **Nota de contexto técnico (vigente desde 2026-08-06)**: si el documento
  fuente trae "Componente tecnológico principal" y/o "Clasificación" por
  producto, se agrega como nota informativa en cursiva gris bajo el objetivo
  del PDF (sin precio, fuera de la tabla de alcance). Se omite si la fuente
  no trae esos datos.

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

> **Referencia de verdad — vigente y superada**: `cotizaciones/compumax/
> Compumax Computer S.A.S - Cotizacion.xlsx` fue el ejemplo aprobado por el
> usuario para las columnas B:K, la fórmula de Y, y el manejo de la zona
> intocable — eso sigue vigente. **Pero su columna L/M/N sigue el patrón
> antiguo de "1 submódulo = 1 funcionalidad" (superado el 2026-08-05, ver §2 y
> §3)** — no la uso como referencia de cardinalidad. Para cardinalidad
> variable (varios N por M), me guío por la regla de §2, no por un archivo de
> ejemplo específico.

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

### 2. Jerarquía flexible de alcance del cliente (columnas L, M, N) — desde la fila 8

**Regla central (vigente desde 2026-08-05 — reemplaza el patrón fijo
anterior):** la cantidad de funcionalidades (N) bajo cada submódulo (M) es
**libre**, tantas como el alcance real necesite. **Queda prohibido forzar el
patrón antiguo de "1 submódulo = 1 descripción"** — el nivel de detalle debe
reflejar la complejidad real de cada parte del alcance, igual que lo haría
una cotización elaborada a mano.

| Columna | Nivel | Contenido | Cardinalidad |
|---------|-------|-----------|--------------|
| **L** | Módulo | `NOMBRE DEL MÓDULO - descripción breve del módulo`, **combinados en una sola celda** separados por ` - ` | Una fila por módulo |
| **M** | Submódulo | Encabezado corto de una agrupación temática dentro del módulo (sin días propios) | Puede repetirse varias veces bajo un mismo módulo — tantas agrupaciones distintas como existan |
| **N** | Funcionalidad | Frase autocontenida que describe **una** funcionalidad concreta y atómica (con sus días en B:K, ver §3) | Puede repetirse varias veces bajo un mismo submódulo — tantas funcionalidades distintas como existan (mínimo 1) |

Ejemplo de estructura correcta (cardinalidad variable, no un patrón fijo):

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

- Cada fila de módulo (L), submódulo (M) o funcionalidad (N) ocupa su propia
  fila; las otras dos columnas de esa fila quedan **vacías**.
- El criterio de cardinalidad es: ¿cuántas funcionalidades atómicas y
  realmente distintas describe el alcance para ese submódulo? Ni una menos
  (no resumir dos funcionalidades reales en una sola fila N), ni una de más
  forzada artificialmente para aparentar más detalle. La cardinalidad debe
  ser fiel al alcance compartido por el usuario (regla de veracidad, ver
  `wiki/perfil-usuario.md`).
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

- **Regla general (vigente desde 2026-08-05 — reemplaza la regla anterior):
  el estimado de días va siempre en la fila de la funcionalidad (N). El
  submódulo (M) nunca lleva días** — es un encabezado de agrupación, no una
  unidad de esfuerzo. Como cada submódulo puede tener varias funcionalidades
  (§2), cada una lleva su propio estimado independiente: **nunca se reparte
  ni se promedia un solo estimado entre varias filas N**.
- Solo lleno las columnas de las especialidades que realmente participan en
  esa funcionalidad (las demás quedan vacías, no en 0).
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

### 5. Celdas obligatorias dentro de la zona de fórmulas (excepciones explícitas)

Son las **únicas** dos excepciones documentadas a la regla "todo lo demás es
intocable" (§4). Ambas se ubican **en relación a la "barra gris"** — la fila
con relleno gris sólido (`#999999`) en la columna L que marca el cierre de la
tabla de alcance (en la plantilla maestra esa barra está en la fila 120, pero
**no es una fila fija**: si el alcance del cliente es grande y se insertaron
filas, la barra gris se desplaza y ambas celdas se mueven con ella).

| Celda (relativa a la barra gris) | En la plantilla maestra (barra gris = fila 120) | Contenido obligatorio | Vigente desde |
|---|---|---|---|
| Columna **Y**, fila `barra_gris + 2` | `Y122` | Fórmula `=Y1/0,6` (interno `=Y1/0.6`) | 2026-07-28 |
| Columna **R**, fila `barra_gris + 3` | `R123` | Valor `0.1` (10%) — reemplaza el default de la plantilla maestra (40%) | 2026-08-05 |

- Para ubicar la barra gris: es la fila con `fill` gris sólido (`#999999`) en
  la columna L, justo antes del bloque de fórmulas fijas de costeo (P:AC,
  filas 121+ en la plantilla original).
- `R{barra_gris+3}` es la celda de porcentaje **AIU** (etiquetada `Q{barra_gris+3}='AIU'`
  en la misma fila; en la plantilla maestra, `Q123`) — la confirmo por esa
  etiqueta antes de escribir, no solo por el número de fila.
- Antes de escribir en cualquiera de las dos, confirmo que esté vacía o que
  contenga el valor/fórmula esperado de la plantilla original. Si ya contiene
  datos de una fila real de alcance (porque la tabla se extendió más allá de
  donde yo esperaba), **no la sobrescribo** — reporto el conflicto al usuario
  en vez de asumir.
- Ambas celdas caen dentro de la zona normalmente "intocable" (columnas O:AC,
  §4) — son las únicas excepciones explícitas a esa regla.

### 6. Verificación obligatoria

- Recalculo con `scripts/recalc.py` (skill de xlsx) y confirmo **cero errores**
  de fórmula (fuera de defectos preexistentes conocidos de la plantilla, ver
  fila `A140:A144` — `#NAME?`/`#ERR520` de un `UNIQUE()` no soportado por
  LibreOffice, no relacionado con mi llenado).
- Reviso que ningún ítem del PDF quedó sin su fila correspondiente en el XLSX
  y viceversa (a nivel de módulo, submódulo y funcionalidad).
- Confirmo que cada funcionalidad (fila N) tiene sus propios días y que
  ningún submódulo (fila M) quedó con días cargados por error.
- Confirmo que la celda `Y{barra_gris+2}` tiene la fórmula `=Y1/0.6` y que
  recalcula a un valor numérico (no error).
- Confirmo que la celda `R{barra_gris+3}` tiene el valor `0.1` (10%) y que se
  refleja correctamente en la columna P (Valor Hora) de la tabla de costos
  fija.

---

## Mantener la wiki (Lint)

Periódicamente reviso: contradicciones, info desactualizada, páginas huérfanas,
convenciones de diseño que ya no usamos, y propongo mejoras.

---

## Convenciones de la bitácora (log.md)

Cada entrada empieza con prefijo consistente para que sea parseable:
`## [YYYY-MM-DD] <tipo> | <descripción>` donde tipo ∈ {setup, build, ajuste,
deploy, lint}.
