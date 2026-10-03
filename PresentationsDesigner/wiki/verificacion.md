# Protocolo de verificación visual (R6 · R7)

Toda presentación se **verifica antes de entregarla**: primero con la herramienta (mide), después **a la vista** (juzga).
La herramienta no sustituye la mirada: detecta lo medible; el diseño se decide mirando.

## 1. Comando (siempre, tras cada build y tras cada ajuste)
```bash
python3 herramientas/verificar_deck.py presentaciones/<slug> --pdf presentaciones/<slug>/<slug>.pdf --png-dir /tmp/<slug>-png
python3 herramientas/elegir_logo.py --tabla        # al decidir fondos/logos
```
Debe terminar en **APROBADO (0 errores)**. Los **avisos (⚠)** se resuelven o se justifican por escrito en la bitácora.
Requiere Chromium y `pip install pymupdf`. Si el usuario pidió más de 10 láminas **textualmente**, añadir `--max-slides N`.

| Comprobación | Umbral | Regla |
|---|---|---|
| Nº de láminas | ≤ 10 | R4 |
| Colores de fondo | **blanco `#FFFFFF`**: `data-bg="white"` en toda lámina; barra y página del visor blancas; ningún otro fondo | R1 |
| Peso visual de logos (Campuslands vs cliente) | **áreas iguales ±6 %** (no la altura); si el logo del cliente es vertical y k>2,0, se limita a 2,0× la altura de Campuslands y sale **aviso** (no error) | R2 |
| Pie de la lámina de cierre | sin la palabra «cierre» en `.crumbs` | regla 2026-10-03 |
| «×» entre logos | existe `.x`, no hay `.sep`, centrada en vertical ±2 px, entre ambos logos | R2 |
| Rótulo «Confidencial» | no aparece (ni visor ni láminas) | R8 |
| Logos en láminas de contenido | ninguno (solo portada/cierre, que sí deben llevarlos) | R10 |
| Fondo | sin resplandor celeste (`rgb(44,170,255)`) | R10 |
| Indicadores | sin `NN / TT` ni filas de puntos (`*dots*`, `pager`, `stepper`) en ninguna parte; solo el numeral `.ghost` | R10 |
| Banners/franjas | sin borde dorado | R11 |
| Bloques superpuestos | ninguna tarjeta/franja pisa a otra (≥ 50 px) | calidad |
| Texto dentro de su tarjeta | el texto no sobresale de la tarjeta/franja que lo contiene | calidad |
| Portada: «Fecha» | Mes y Año (no solo el año) | R9 |
| Orden de logos | Campuslands a la izquierda | Brandbook p.6 |
| Deformación del logo | proporción dibujada = natural (±3 %) | Brandbook p.16 |
| Versión del logo vs fondo | a color sobre blanco | R5 |
| Logos del visor | Campuslands ≥ 40 px de alto en la barra superior | R12 |
| Bordes/líneas en láminas | ningún `border` sólido < 2,6 px ni línea de ≤ 2,5 px (acentos ≥ 3 px, neón y punteados permitidos); se usan sombras | R14 |
| Altura de las barras del visor | barra superior = barra inferior (±1 px, `--bar-h`) | R15 |
| Divisiones del visor | barras, recuadro de la lámina y botones con **sombra** y **sin** `border`/`outline` | R13 |
| Fuentes | **solo Poppins** (400/500/600/900) y Nutmeg · cargadas; Roboto Mono = error | R12 |
| Texto mínimo | ≥ 9 px | legibilidad |
| Contraste | ≥ 4,5 : 1 (≥ 3 : 1 si es grande) | accesibilidad |
| Geometría | nada fuera de la lámina, nada sobre el pie, nada recortado | calidad |
| Imagen vs contenedor | ninguna `<img>` excede su caja (logos de cliente, etc.) | calidad |
| Hueco vertical | ≤ 20 % de la lámina (no aplica a portada/cierre centrados) | balance |
| PDF | páginas = láminas; sin fuentes de respaldo | entrega |
| `<head>` | `<title>` = razón social del cliente · favicon = isotipo | CLAUDE.md |

## 2. Revisión a la vista (obligatoria, lámina por lámina)
Abrir cada PNG (`--png-dir`) y mirar, **en este orden**:
1. **Logos:** ¿se ven del mismo tamaño (peso visual, no solo altura)? ¿la «×» está al medio? ¿el de Campuslands va primero? ¿contrastan con el fondo? ¿hay aire alrededor (≥ X de la M)?
2. **Jerarquía:** ¿qué se lee primero, segundo, tercero? ¿coincide con lo que el cliente debe entender?
3. **Espacios:** ¿hay franjas muertas o elementos pegados? ¿el reparto se ve **intencional**?
4. **Color:** ¿el fondo es blanco #FFFFFF? ¿el visor también? ¿las tarjetas se distinguen del fondo (borde/sombra/color)? ¿no hay navy/violeta/arena como fondo? ¿los acentos cumplen los pares de contraste? ¿no hay más de un marco neón?
5. **Tipografía:** ¿todo en Poppins? ¿ningún texto con fuente de respaldo (se ve distinto)?
6b. **Decoración e íconos:** ¿cada tarjeta importante tiene su decoración (anillos/puntos/rayas…) discreta y fuera del texto? ¿cada ícono significa algo y es de la misma familia? ¿el numeral de sección es pequeño y difuminado? ¿el pie está abajo a la izquierda?
6. **Decoración:** ¿cruza algún texto? ¿está recortada a propósito?
7. **Dinamismo:** ¿la lámina cambia de arquetipo/fondo respecto a las vecinas? ¿se siente plana?
También ver **el visor en pantalla** (captura del HTML con `--screenshot`) al menos de la portada y de una interna, porque el visor tiene sus propios logos.

## 3. Registro de razón de ubicación (R7)
En el **plan** y luego en la **bitácora** se deja, por lámina, una línea por bloque relevante:
`lámina 4 · escalera de 4 peldaños a la izquierda→derecha descendente: refleja avance en el tiempo; franja neón al pie: el entregable es lo que el cliente aprueba`.
Si un objeto no tiene razón → se elimina o se mueve.

## 4. Cuándo la herramienta se equivoca (falsos positivos conocidos)
- Decoración (`aria-hidden`, `.ghost`, `.chev`) que sangra: ya se excluye. Si algo decorativo se marca, falta `aria-hidden="true"`.
- Texto solo de símbolos (separadores `|`, `=>`): no se evalúa en contraste (no es contenido).
- Portada/cierre centrados: no se mide el hueco superior/inferior y el hueco entre bloques se tolera hasta 30 % (resto: 20 %).
- Figuras difuminadas `.blob` (`aria-hidden`): se excluyen de las mediciones; **a la vista** hay que comprobar que no queden bajo texto pequeño (pie, fecha) con mal contraste.
- Un aviso de hueco se **puede justificar** si el vacío es composición deliberada (p. ej. afirmación con mucho aire); decirlo en la bitácora.
