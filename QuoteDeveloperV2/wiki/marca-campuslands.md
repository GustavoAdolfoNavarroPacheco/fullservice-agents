# Marca Campuslands Full Service

Este documento establece las directrices de identidad visual, el tono editorial y las normas de aplicación de marca para las cotizaciones y documentos. El lenguaje visual es *premium, con gradientes y tipografía de carácter*.

---

## 1. Tono y Estilo Editorial (Voz de Marca)

Corporativo, sofisticado y persuasivo. Tecnología enterprise que resuelve problemas reales.

*   **Data-driven:** cada afirmación respaldada por métricas (*"ahorro de 4 h manuales"*, *"ROI en 6 meses"*).
*   **Orientación al ROI:** la narrativa destaca valor comercial/financiero, no solo el logro técnico.
*   **Agilidad:** metodologías modernas, despliegue continuo e IA aplicada.

---

## 2. Paleta de Colores

La base es oscura, con acentos en gradientes y ámbar. Las cotizaciones PDF usarán esta estética para mantener coherencia visual.

### Fondos
| Token | Hex | Uso |
| :--- | :--- | :--- |
| `--bg-0` | `#05070F` | Base más profunda. |
| `--bg-1` | `#0A0E1A` | Base estándar de documento. Prohibido negro puro `#000000`. |
| `--bg-2` | `#0D1424` | Superficies elevadas (tablas, paneles). |

### Texto
| Token | Hex | Uso |
| :--- | :--- | :--- |
| `--text-hi` | `#FFFFFF` | Títulos, números clave. |
| `--text-mid` | `#C3CBDA` | Cuerpo destacado, subtítulos. |
| `--text-lo` | `#7A8699` | Descripciones, viñetas. |

### Acentos y gradientes
| Token | Valor | Uso |
| :--- | :--- | :--- |
| `--cyan` | `#35D0F0` | Eyebrows, labels, íconos. |
| `--blue` | `#4A7DFF` | Paso medio. |
| `--violet` | `#8B5CF6` | Paso alto. |
| `--grad-brand` | `linear-gradient(100deg,#35D0F0,#4A7DFF,#8B5CF6,#C05CF6)` | **Gradiente insignia.** |

---

## 3. Tipografía Oficial

Las fuentes utilizadas son:

| Rol | Familia | Pesos usados |
| :--- | :--- | :--- |
| **Display / Títulos** | **Playfair Display** | 700, 900, italic 400/900 |
| **Labels / Eyebrows** | **Montserrat** | 500, 600, 700 |
| **Cuerpo / Viñetas** | **Poppins** | 300, 400, 500, 600 |

---

## 4. Uso de Logotipos

*   **Logo Campuslands:** Se debe usar `Logo Campuslands Horizontal Blanco.png` (transparente) sobre fondos oscuros, o `Logo Campuslands Horizontal Azul.png` sobre fondos claros (ver sección 5). En los documentos PDF, va ubicado arriba a la izquierda.
*   **Logo Cliente:** Arriba a la derecha, manteniendo proporción y verificando contraste contra el fondo.

---

## 5. Diseño de PDFs de Cotización — estándar vigente (desde 2026-07-17)

**Esta sección reemplaza las secciones 2 y 3 específicamente para el PDF de Cotización de Alcance.** La paleta oscura con gradientes (sección 2) y la tipografía Playfair/Montserrat/Poppins (sección 3) quedan como referencia de marca general de Campuslands, pero **todo PDF de cotización generado a partir de ahora debe usar esta paleta clara y este layout de grid**, sin excepción, salvo pedido explícito del usuario en contrario.

Origen: instrucción explícita del usuario (2026-07-17), usando como referencia visual el PDF ya entregado `cotizaciones/la-esmeralda/La Esmeralda - Cotizacion de Alcance.pdf` (fondo blanco, azules, líneas horizontales) — el estándar actual va un paso más allá: **grid completo** (líneas horizontales y verticales) con toques de gris, no solo separadores horizontales.

### Paleta (obligatoria, colores exactos de marca)

| Token | Hex | Uso |
| :--- | :--- | :--- |
| `--navy` | `#152F5E` | Header de tabla, bandas de TOTAL, títulos, footer del logo/marca. |
| `--azul-cielo` | `#418BF3` | Bandas de módulo, acentos, eyebrow, footer del texto. |
| `--blanco` | `#FFFFFF` | Fondo de página y de filas de ítem. |
| `--gris-linea` | `#D6DCE5` (aprox.) | Líneas delgadas del grid (horizontales y verticales) entre celdas. |
| `--gris-texto` | `#5B6B84` (aprox.) | Texto secundario / detalle técnico, dentro del rango gris-azulado de marca. |

No usar la paleta oscura (`--bg-0/1/2`, cian/violeta/magenta de la sección 2) en cotizaciones nuevas.

### Layout — grid con líneas delgadas

*   La tabla de 3 columnas (Módulo/Submódulo · Detalle técnico · Valor COP) lleva **líneas delgadas grises** (`--gris-linea`, ~0.5pt) tanto entre filas **como entre columnas**, formando un grid visible tipo hoja de cálculo — no solo separadores horizontales como en versiones anteriores.
*   Header de tabla: fondo `--navy`, texto blanco.
*   Banda de módulo: fondo `--azul-cielo`, texto blanco, con el grid gris también visible en sus bordes.
*   Fila de submódulo: texto en negrita, sin precio propio, distinguible de las filas de funcionalidad de abajo.
*   Filas de funcionalidad (bullets, cada una con su propio precio): fondo `--blanco`, texto en navy/gris, grid gris delgado alrededor de cada celda.
*   Fila TOTAL: fondo `--navy`, texto blanco.
*   Fondo de página: blanco. Barra superior de cada página en azules de marca (navy + azul cielo), no gradiente multicolor.

### Jerarquía de contenido (vigente desde 2026-08-05 — reemplaza el patrón fijo anterior)

**Módulo → Submódulo → Funcionalidad(es)**, con cardinalidad libre en cada nivel — un submódulo puede tener una o varias funcionalidades, según lo que el alcance real necesite. Queda prohibido forzar el patrón antiguo de "1 submódulo = 1 funcionalidad". Ver el mapeo exacto en `wiki/plantilla-xlsx.md` §2 (espejo 1:1 con el XLSX).

### Tipografía del PDF de cotización (vigente desde 2026-08-05)

Fuente **Arial** en toda la tabla de alcance (distinta de la tipografía de marca general de la sección 3, que no aplica a cotizaciones):

| Nivel | Tamaño | Peso |
| :--- | :--- | :--- |
| Módulo | 11 pt | Negrita |
| Submódulo | 10 pt | Negrita |
| Funcionalidad / Detalle técnico | 10 pt | Regular |

### Precios en el PDF

A partir de ahora, **todo PDF de cotización lleva los precios reales en COP** (ya no "Pendiente de costear" por defecto) — se toman directamente de las fórmulas ya calculadas del XLSX correspondiente (columna A, `data_only=True` tras recalcular), nunca capturados a mano. Antes de insertarlos en el PDF, el agente hace una **doble verificación**:
1. Cada precio de línea en el PDF coincide exactamente con la celda de origen en el XLSX recalculado.
2. La suma de los ítems de cada módulo coincide con el subtotal mostrado en la banda de ese módulo, y la suma de todos los módulos (incluyendo las filas transversales 2-5) coincide exactamente con el TOTAL general del XLSX.

La mecánica de recálculo con LibreOffice está en `wiki/plantilla-xlsx.md` § Verificación obligatoria.
