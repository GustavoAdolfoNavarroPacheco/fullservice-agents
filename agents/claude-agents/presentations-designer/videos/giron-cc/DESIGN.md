# DESIGN.md — Módulo de Cobranza con IA (Girón)

Fuente de verdad visual del video. Deriva de `CLAUDE.md` (reglas supremas 1–8) y de `wiki/marca-campuslands.md` (Brandbook). Ante conflicto, gana `CLAUDE.md`.

## Concepto
Propuesta comercial en movimiento: cada lámina del deck se convierte en una escena con su propio arquetipo, y cada cambio de escena es una transición distinta. Los textos y cifras son los del deck, literales.

## Tokens
| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#FFFFFF` | fondo de **toda** escena (regla 1) |
| `--navy` | `#000087` | títulos, tarjetas navy, numerales |
| `--violet` | `#5E3AE2` | acentos, `</`, énfasis, tarjetas violeta |
| `--gold` | `#F4B422` | acentos, íconos, badges, tarjetas doradas |
| `--sky` | `#2CAAFF` | acentos, íconos |
| `--green` | `#00AA80` | viñetas, íconos de éxito |
| `--sand` | `#E4E4DB` | solo acento, nunca fondo de escena |
| `--ink` | `#373435` | cuerpo de texto sobre blanco (tinta del wordmark) |

Sin `#000` ni `#FFF` como texto de cuerpo; el blanco es solo superficie de tarjeta y texto sobre oscuro.

## Tipografía
Poppins en todo el video: 400 · 500 · 600 · 900 y Black Italic (`assets/fonts/`). Títulos 900 a 62 px (lámina) y 110 px (portada). Cuerpo 21 px, pies 19 px. Nutmeg no se usa (sin licencia en el repo).

## Forma y profundidad
- **Sin bordes ni líneas.** Tarjetas y paneles se separan por `box-shadow` (`--sh-card`).
- Radio de tarjeta 26 px. Acentos de color ≥ 3 px (barra de transición, franjas) permitidos.
- Decoración `.arcs` (anillos concéntricos) en las esquinas de las tarjetas, alfa ≤ .3, fuera del texto.

## Logos
- Solo en portada y cierre (regla 2), a color (regla 3), sin recolorear ni distorsionar.
- Campuslands `4,31 : 1` a 64 px de alto. Girón es vertical (`0,65 : 1`): alto = 2 × Campuslands (tope del deck, `--k-cliente:2`).
- «×» centrada en vertical entre los dos logos.

## Pie y marcas
- Migas `| campuslands | propuesta | giron | … |` abajo a la izquierda; lema *Exploramos · Despegamos · Conquistamos* abajo a la derecha.
- Numeral fantasma pequeño y difuminado arriba a la derecha (opacidad .07).
- Marca `</` (violeta) antes de cada título.
- Prohibido el rótulo «Confidencial».

## Movimiento
- Entradas con `gsap.fromTo` (estado inicial explícito), 0.3–1.0 s, cascadas ≤ 0,5 s en total por grupo.
- Ambiente continuo y finito: anillos discontinuos girando, decorativos flotando, contadores, trazos que se dibujan, pulsos.
- **Transiciones** (la escena que entra hace la transición; no hay fundidos de salida salvo el cierre):
  1. Portada → 2: iris circular con anillo dorado.
  2. 2 → 3: empuje horizontal.
  3. 3 → 4: barrido vertical con barra violeta.
  4. 4 → 5: zoom con desenfoque.
  5. 5 → 6: diagonal.
  6. 6 → 7: cortina dorada y violeta.
  7. 7 → 8: giro 3D.
  8. 8 → 9: iris rectangular.
- Sin repeticiones infinitas; `repeat` siempre finito. Sin `Math.random`, sin `Date.now`.

## Densidad
Máximo 4 tarjetas por fila. Textos de tarjeta 20–21 px. Ninguna lámina sin respiración: márgenes laterales 110 px, pie a 38 px del borde inferior.
