# Banner de las facturas

Especificación del banner vigente (**v2**, 2026-11-06) que encabeza cada factura del documento unificado. La v1 (dos barras: marca + datos, con HORA) venía de
«Facturas_28-29_Octubre_2026_Campuslands.docx»; el usuario pidió que fuera **simétrico**, sin la barra superior y sin hora. **Lo seguirá mejorando**: por eso vive aislado.

## Cómo cambiarlo

Todo el diseño está en **un solo archivo**: [`scripts/factura_banner.py`](../scripts/factura_banner.py). `facturas.py` solo llama a
`agregar_banner(doc, indice, total, datos, ancho_twips, continuacion)` y no conoce colores, fuentes ni medidas.

- Cambiar colores, tipografía o número de columnas → constantes al inicio del archivo (`AZUL`, `FONDO`, `DIVISOR`, `ETIQUETA`, `VALOR`, `FUENTE`, `N_COLUMNAS`).
- Rediseñar (logo como imagen, otros campos, otra estructura) → reescribir `agregar_banner` conservando su firma. Si el nuevo banner es más alto, subir `RESERVA_VERTICAL_TW` en `facturas.py` (espacio que se reserva por hoja para banner + leyenda); `construir` reduce las imágenes solo si no caben.
- Si hace falta un dato nuevo en el banner (p. ej. el total de la factura), se agrega a `DatosFactura` y al manifiesto.
- Después: `python -X utf8 scripts/autoprueba.py` y revisar a la vista el PDF.

El agente **no** modifica el banner por iniciativa propia (regla dura 5).

## Diseño vigente (v2)

Una **sola franja simétrica**: tabla de Word de **cuatro celdas iguales** (25 % cada una), contenido centrado, mismo filete azul `0D497B` de 1,5 pt arriba y abajo, divisores finos `C9D6E3` entre celdas, fondo `EEF3F8` (paleta del membrete de la plantilla). Tipografía **Poppins**.

| Celda | Etiqueta (6,5 pt, negrita, espaciada, `5B6B7F`) | Valor |
|---|---|---|
| 1 | **FACTURA** (o **FACTURA (CONT.)** en las hojas extra de una factura) | `01` en azul 13 pt negrita + ` / 4` |
| 2 | **FECHA** | «Mié 28 oct 2026» (día abreviado; 8,5 pt negrita) |
| 3 | **TIPO** | «Transporte» |
| 4 | **PROVEEDOR** | «inDrive» |

- Se quitó la barra superior (marca «CAMPUSLANDS · Construyendo talento»): el logo ya lo trae el membrete de la plantilla.
- **La hora ya no se imprime** (ni en el banner ni en las notas). Sigue usándose para **ordenar**.
- La v1 estaba desequilibrada (fecha ancha a la izquierda, columnas desiguales, filete solo a la izquierda).

## Resto de la hoja

- **Plantilla Word de Campuslands** (membrete con logo arriba y dirección abajo), hoja Carta **vertical**, márgenes de la plantilla. Todas las hojas son verticales.
- Debajo del banner, el recibo recortado de su blanco, con marco gris azulado, a todo el ancho del banner (mismo borde izquierdo y derecho) y ajustado al espacio libre.
- Recibo de 2 páginas: una sobre otra en la misma hoja si conservan ≥ 85 % de legibilidad; si no (caso habitual), una hoja por página con «FACTURA (CONT.)». De 3 o más: una hoja por página.
- Leyenda en cursiva de 7 pt: `Archivo original: <nombre> · <nota>`. La nota aparece cuando el nombre del archivo contradice al recibo («El nombre del archivo no coincide con lo que dice el recibo; se usaron los datos del recibo») o cuando el agente la escribe en el manifiesto (sin horas).
- Pie: `Pág. N/M` a la derecha, sobre el pie del membrete (corto a propósito para no pisar la línea verde del membrete).
- **Poppins incrustada** en el Word (`comun.incrustar_fuente`) y cargada desde `recursos/fuentes/` al generar el PDF: se ve igual en cualquier equipo.

## Datos de cada factura

Salen del recibo (regla dura 1), no del nombre del archivo. Ver `manifiesto.json` en la sección «Funcionalidad 1» de `CLAUDE.md`.
Ejemplo de por qué: en el caso de origen, `28102026 - 13h31m - inDrive.pdf` era en realidad el viaje de las **3:31 p. m.** y `28102026 - 15h47m - inDrive.pdf` el de la **1:47 p. m.**; ordenar por nombre habría invertido las facturas 1 y 2.
