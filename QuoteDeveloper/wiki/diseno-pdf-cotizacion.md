# Sistema de diseño del PDF de cotización

> **Fuente canónica: `CLAUDE.md` § Reglas del PDF y `wiki/marca-campuslands.md`
> §5.** Esta página consolida ambas en un solo lugar para que el árbol de
> archivos de `CLAUDE.md` sea preciso y para tener el sistema de diseño
> consultable desde el catálogo de la wiki. Se actualiza junto con esos dos
> archivos en cada ajuste (ver "Mantener la wiki (Lint)" en `CLAUDE.md`).

Estándar vigente desde 2026-07-17. Reemplaza la paleta oscura con gradiente
(esa sigue siendo la identidad de marca general de Campuslands, pero no se usa
en cotizaciones) y cualquier variante clara anterior sin grid completo.

## Paleta (obligatoria, colores exactos de marca)

| Token | Hex | Uso |
| :--- | :--- | :--- |
| `--navy` | `#152F5E` | Header de tabla, bandas de TOTAL, títulos, footer del logo/marca. |
| `--azul-cielo` | `#418BF3` | Bandas de módulo, acentos, eyebrow, footer del texto. |
| `--blanco` | `#FFFFFF` | Fondo de página y de filas de ítem. |
| `--gris-linea` | `#D6DCE5` (aprox.) | Líneas delgadas del grid (horizontales y verticales) entre celdas. |
| `--gris-texto` | `#5B6B84` (aprox.) | Texto secundario / detalle técnico. |

No se usa la paleta oscura (`--bg-0/1/2`, cian/violeta/magenta) en
cotizaciones nuevas.

## Layout — grid con líneas delgadas

- Tabla de 3 columnas: `Módulo / Funcionalidad` | `Detalle técnico` | `Valor
  (COP)`, en ese orden fijo.
- **Líneas delgadas grises** (`--gris-linea`, ~0.5pt) tanto entre filas como
  entre columnas, formando un grid visible tipo hoja de cálculo — no solo
  separadores horizontales.
- Header de tabla: fondo `--navy`, texto blanco.
- Banda de módulo (`M1. NOMBRE DEL MÓDULO` + descripción corta): fondo
  `--azul-cielo`, texto blanco, grid gris visible en sus bordes.
- Filas de ítem (bullets `• Funcionalidad` con su detalle técnico): fondo
  `--blanco`, texto navy/gris, grid gris delgado alrededor de cada celda.
- Fila TOTAL: fondo `--navy`, texto blanco.
- Fondo de página: blanco. Barra superior de cada página en azules de marca
  (navy + azul cielo), no gradiente multicolor.
- El número de módulos y de bullets por módulo es libre — depende del alcance
  real del proyecto, no hay un conteo fijo.

## Logotipo

- Campuslands (`Logo Campuslands Horizontal Azul.png`, para este fondo claro)
  arriba a la izquierda.
- Logo del cliente arriba a la derecha, manteniendo proporción y verificando
  contraste contra el fondo.

## Precios en el PDF (vigente desde 2026-07-17)

Todo PDF de cotización lleva los **precios reales en COP** — ya no "Pendiente
de costear" por defecto (ese placeholder solo se usa si el XLSX
correspondiente todavía no existe o no está recalculado). Se toman
directamente de las fórmulas ya calculadas del XLSX correspondiente (columna
A, `data_only=True` tras recalcular), nunca capturados a mano.

Doble verificación antes de insertarlos en el PDF:
1. Cada precio de línea en el PDF coincide exactamente con la celda de origen
   en el XLSX recalculado.
2. La suma de los ítems de cada módulo coincide con el subtotal mostrado en
   la banda de ese módulo, y la suma de todos los módulos (incluidas las
   filas transversales 2-5) coincide exactamente con el TOTAL general del
   XLSX.

## Contenido

- **100% verídico**: solo lo que el usuario compartió o confirmó
  explícitamente. Cero relleno genérico de IA.
