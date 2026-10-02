# Marca Campuslands — normativa para presentaciones (Brandbook 2023)

> **Reconceptualización del 2026-10-02.** Este documento reemplaza al sistema anterior (paleta derivada del logo de cada
> cliente, Playfair/Montserrat). **La fuente normativa es el Brandbook de Campuslands S.A.S.** y se sigue **estrictamente**.
> Orden de prioridad cuando haya conflicto: **1) Brandbook · 2) reglas dadas por el usuario · 3) convenciones del agente.**

**Fuente:** [`recursos/brandbook/Campuslands_Brandbook.pdf`](../recursos/brandbook/Campuslands_Brandbook.pdf) — 27 páginas.
Es **idéntico byte a byte** (SHA-256 `522efe6b…`) a `recursos/Campuslands_Brandbook2023V2._compressed (1).pdf`, que ya
estaba en el repositorio sin haberse aplicado. Las citas `p.N` de abajo remiten a esas páginas.
Logos oficiales en [`recursos/logos-campuslands/`](../recursos/logos-campuslands/README.md).

---

## 1. Reglas del usuario (2026-10-02) — obligatorias

| # | Regla | Cómo se cumple y se comprueba |
|---|---|---|
| R1 | Los **fondos** de toda presentación usan **SIEMPRE y OBLIGATORIAMENTE colores de Campuslands**. | Fondos solo `navy`, `violeta` o `arena` (sólidos o degradados entre colores de la paleta). `verificar_deck.py` rechaza cualquier color de fondo fuera de la paleta. |
| R2 | Logo de Campuslands y logo del cliente con el **mismo tamaño**. | Misma altura (±3 %) de ambos logos recortados al contenido; se mide con `verificar_deck.py` **y** se confirma mirando la lámina. |
| R3 | **Dinamismo e innovación**: nada "plano". | Alternar arquetipos entre láminas contiguas y usar el lenguaje gráfico de marca (§6). Ver [[sistema-diseno]]. |
| R4 | **Máximo 10 láminas**; solo se supera si el usuario lo pide **textualmente**. | `verificar_deck.py` falla con >10 (salvo `--max-slides N` ante pedido textual). |
| R5 | **Elegir el mejor logo de Campuslands** evaluando el **contraste** con el fondo. | `herramientas/elegir_logo.py` (tabla en §3.3). |
| R6 | **Verificaciones visuales rigurosas** de espacios, distribución, colores y fuentes. | Protocolo en [[verificacion]]. |
| R7 | **Cada objeto tiene una razón** para su ubicación y distribución. | Se escribe en el plan y se revisa lámina por lámina ([[verificacion]] §3). |

---

## 2. Identidad (Brandbook p.5)

El **imagotipo** abstrae un **casco de astronauta**: juventud, evolución y futuro; homenaje a la exploración del universo
y a todo lo que implica conquistarlo (espíritu emprendedor, mente abierta, experticia). De ahí el pie de las láminas:
*Exploramos · Despegamos · Conquistamos*. El **slogan** de la marca es **GO FOR IT!** (p.7; no hay archivo del logotipo del
slogan en `recursos/` → no se reproduce con tipografía propia; si hace falta, pedirlo al usuario).

Se llama **Campuslands** (el wordmark es siempre minúscula y viene dentro del logo; **nunca se compone con una fuente**).
Razón social en textos: **Campuslands S.A.S. BIC**.

---

## 3. Logo

### 3.1 Variantes oficiales
Archivos en `recursos/logos-campuslands/` (maestro tal cual llegó + `-recortado` al contenido exacto, sin padding):

| Variante | Archivo | Proporción (recortado) | Uso |
|---|---|---|---|
| Horizontal a color | `campuslands-horizontal-color` | 3,20 : 1 | Fondos **arena** (claros). |
| Horizontal blanco | `campuslands-horizontal-blanco` | 5,05 : 1 | Fondos **navy** y **violeta**. |
| Vertical a color | `campuslands-vertical-color` | 0,91 : 1 | Portadas/cierres verticales sobre arena. |
| Vertical blanco | `campuslands-vertical-blanco` | 0,91 : 1 | Portadas/cierres verticales sobre navy/violeta. |
| Isotipo (casco solo) | `recursos/isotipo-campuslands.png` | — | **Favicon** y usos muy pequeños. |

> ⚠️ El horizontal blanco y el horizontal a color son archivos **oficiales con distinta proporción** (el casco es proporcionalmente
> menor en el blanco). Se usan tal cual; **no se "iguala"** estirándolos. Por eso la regla de tamaño se mide por **altura del
> recorte** y se **confirma a la vista** (§4).
> Los vectoriales (`vectoriales/*.pdf`, `.ai`) son la fuente para impresión o cambios de escala grandes.

### 3.2 Usos incorrectos (p.16) — prohibido
Cambiar los **colores** · **eliminar** elementos (casco o wordmark) · cambiar la **orientación** (rotar) · cambiar la
**distribución** de elementos · **distorsionar** (estirar/comprimir) · cambiar la **tipografía** del wordmark.
Corolarios: nunca recolorear el logo con CSS (`filter`, `mix-blend-mode`, `opacity` que lo apague), nunca fijar `width` **y**
`height` a la vez (solo `height` + `width:auto`), nunca poner el logo a color sobre un fondo donde el extremo claro del casco
desaparezca.

### 3.3 Elección de la versión por contraste (R5)
El logo a color tiene wordmark `#373435` y casco en degradado `#142F5D → #408AF3`. Criterio: texto ≥ **4,5 : 1** y **ambos**
extremos del casco ≥ **2,5 : 1**. Resultado medido (`python3 herramientas/elegir_logo.py --tabla`):

| Fondo | HEX | Logo a color (texto / casco mín.) | Logo blanco | **Decisión** |
|---|---|---|---|---|
| Navy | `#000087` | 1,26 / 1,18 | **15,56** | ✅ **BLANCO** |
| Violeta | `#5E3AE2` | 1,86 / 1,93 | **6,61** | ✅ **BLANCO** |
| Arena | `#E4E4DB` | **9,63** / 2,67 | 1,28 | ✅ **A COLOR** |
| Dorado | `#F4B422` | 6,68 / 1,85 | 1,84 | ❌ ninguno |
| Verde | `#00AA80` | 4,14 / 1,15 | 2,97 | ❌ ninguno |
| Celeste | `#2CAAFF` | 4,87 / 1,35 | 2,53 | ❌ ninguno |

**Consecuencia de diseño:** la zona de los logos (cabecera, portada, cierre) va sobre **navy, violeta o arena**. **Dorado, verde y celeste
son colores de acento** (marcadores, íconos, números, bandas, llamados); **no** se usan como fondo de una zona con logos.

### 3.4 Espacio libre (p.7)
> «El espacio en blanco alrededor del isotipo e imagotipo es el ancho y el alto de la letra **M**.»

Unidad **X = alto de la "m" del wordmark** (medida sobre los archivos, `recursos/logos-campuslands/medidas-logos.json`):
horizontal color **0,2306·H** · vertical color **0,1142·H** · vertical blanco **0,1155·H** · horizontal blanco **0,4545·H**
(H = alto del logo recortado). Mínimo normativo: **X** libre en los cuatro lados. *Decisión de diseño (no del Brandbook):* en
co-branding se usa una separación **≥ 2X** más un divisor fino, y nunca se coloca texto a menos de **X** del logo.

### 3.5 Co-branding (p.6, p.1)
1. **Campuslands aparece primero**, de izquierda a derecha.
2. **Semejanza total en los tamaños** → regla **R2**: misma altura de recorte en cabecera, portada, cierre **y barra del visor**.
3. Espacio adecuado entre logotipos según el espacio libre (§3.4). El Brandbook (p.1) los separa con un **divisor vertical fino**.
4. Si el logo del cliente es muy ancho o muy alto (proporción > 5 : 1 o < 1,3 : 1) puede pedir un ajuste óptico: se **mide el área**
   (el verificador avisa si difiere ×3) y se **decide mirando** la lámina; la altura igual sigue siendo el punto de partida.
5. Logo del cliente: PNG/SVG **transparente**, recortado al contenido, **en la versión que contraste** con el fondo (a color sobre arena;
   blanco/monocromo claro sobre navy/violeta). **No se recolorea**: se pide al usuario la versión adecuada. Si solo existe una
   versión que no contrasta, la lámina cambia de fondo (navy ↔ arena), no el logo.

---

## 4. Colorimetría (p.12)

| Color | HEX | CMYK (como figura en el Brandbook) | Rol en presentaciones |
|---|---|---|---|
| **Navy** | `#000087` | C100 · M93,2 · Y25,65 · K13,72 | **Fondo** principal; panel oscuro. |
| **Violeta** | `#5E3AE2` | C82,22 · M77,41 · Y0 · K0 | **Fondo** secundario; énfasis sobre arena. |
| **Arena** | `#E4E4DB` | C16,36 · M10,89 · Y18,05 · K0,09 | **Fondo** claro. |
| **Dorado** | `#F4B422` | C6,91 · M35,47 · Y91,67 · K0,52 | **Acento**: `</`, números, bandas, marco neón. |
| **Celeste** | `#2CAAFF` | C68,51 · M28,97 · Y0 · K0 | **Acento**: `{ }`, íconos, líneas. |
| **Verde** | `#00AA80` | C77,49 · M0,76 · Y61,5 · K0 | **Acento**: éxito, chevrones, íconos. |

Apoyos (no son colores de marca): **blanco** `#FFFFFF` solo para texto/logo sobre oscuro y **superficie de tarjeta** sobre arena (nunca
como fondo de lámina); **tinta** `#373435` = color del wordmark, para texto sobre arena. Degradados permitidos: solo **entre colores
de la paleta** (p. ej. violeta → navy) y *glows* de un color de la paleta con transparencia.

**Pares de texto verificados** (contraste WCAG; ≥ 4,5 : 1 normal, ≥ 3 : 1 grande ≥ 24 px o negrita ≥ 18,7 px):

| Texto \ Fondo | Navy | Violeta | Arena |
|---|---|---|---|
| Blanco | **15,56** ✅ | **6,61** ✅ | 1,28 ❌ |
| Arena | **12,16** ✅ | **5,16** ✅ | — |
| Dorado | **8,44** ✅ | 3,59 ⚠️ solo grande | 1,44 ❌ |
| Celeste | **6,15** ✅ | 2,61 ❌ | 1,98 ❌ |
| Verde | **5,23** ✅ | 2,22 ❌ | 2,33 ❌ |
| Violeta | 2,36 ❌ | — | **5,16** ✅ |
| Navy | — | 2,36 ❌ | **12,16** ✅ |
| Tinta `#373435` | 1,26 ❌ | 1,86 ❌ | **9,63** ✅ |

---

## 5. Tipografía (p.10)

| Rol (Brandbook) | Familia | Peso | En presentaciones |
|---|---|---|---|
| **Títulos** | **Poppins** | Regular 400 · **Black 900** | Títulos, números grandes, etiquetas `{ }`. Énfasis = *Black Italic* en color de acento. |
| **Cuerpos de texto** | **Roboto Mono** | Regular 400 | Todo texto corrido, listas, pies, migas. Monoespaciada: **más ancha** → tamaños y longitudes de línea se ajustan. |
| **Destacados / Web** | **Nutmeg** | — | Frases destacadas. **Fuente comercial** (W Type Foundry); **no está licenciada en el repo** → mientras tanto cae a Poppins Black. |

Archivos locales en `recursos/fonts/` (`Poppins-Regular/Black/BlackItalic.ttf`, `RobotoMono-VariableFont_wght.ttf`, licencia OFL).
Se copian a `assets/fonts/` de cada deck. **Prohibido**: Playfair Display, DM Serif, Montserrat, Cambria, Calibri, Arial u otras (los
decks previos al 2026-10-02 que las usan son legado, ver [[archivo/README]]).

---

## 6. Lenguaje gráfico de la marca (qué se toma del Brandbook)

| Recurso | Dónde aparece en el Brandbook | Uso en presentaciones |
|---|---|---|
| **`</` dorado** antes del título | p.3, 4, 9, 11, 13, 17 | Prefijo de título de sección (dorado sobre oscuro; **violeta** sobre arena). |
| **`{ etiqueta }`** en celeste, Poppins Black | p.5–7, 12, 15 | Etiquetas/eyebrows (celeste sobre navy; violeta sobre arena; arena sobre violeta). |
| **`<= … =>`** en Roboto Mono | índice p.3, portadas | Subtítulos y viñetas (`=>`). |
| **Migas de pan** `\| campuslands \| brandbook \| guidelines \| sección \|` | encabezado de cada página | Pie de lámina: `\| campuslands \| propuesta \| cliente \| sección \|`. |
| **Numerales grandes translúcidos** | p.3, 5–7, 12 (1–5 en gris) | Número de sección, esquina superior derecha. |
| **Comillas doradas** | p.2 | Lámina de afirmación/cita. |
| **Chevrones `>>`** navy + verde (+ celeste/dorado sobre oscuro) | tarjetas p.19 | Decoración lateral y conectores de proceso. |
| **Marco neón dorado** | post RRSS p.8 | Marco del dato o frase clave (uno por lámina como máximo). |
| **Divisor fino entre logos** | portada p.1 | Co-branding. |
| Fotografía con *overlay* navy/violeta | p.1, 4, 9, 11, 13, 17 | Solo si el usuario entrega fotos reales; no hay fotos en el repo. |

La decoración va con `aria-hidden`, **nunca cruza texto** y se revisa a la vista (la plantilla trae todos estos componentes).

---

## 7. Tono editorial (se mantiene)
Corporativo, directo y persuasivo; **data-driven** (cada afirmación con su cifra y fuente), orientado a **ROI**, ágil. Español.
Las cifras se citan de la fuente (hoja/celda del Excel, brief del usuario); **no se inventan** y las que el usuario da sin respaldo
se marcan como tales al entregar.
