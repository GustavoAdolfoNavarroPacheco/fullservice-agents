---
workflow: general-video
flow: automation
storyboard: no
message: "Campuslands propone un Módulo de Cobranza con IA para Industria y Comercio de Girón: cuatro fases, un piloto y arranque tras la firma."
audience: "Alcaldía Municipal de Girón (Dirección de Industria y Comercio y TIC)"
aspect: 16:9
language: es
length: ~100s
angle: presentación comercial animada, 1 escena por lámina del deck
---

## Intent

Video de la presentación `presentaciones/giron-cc/` (9 láminas): «Módulo de Cobranza con Inteligencia Artificial», propuesta de Campuslands S.A.S. BIC para la Alcaldía Municipal de Girón. El video **no modifica el deck**: sus textos, cifras y estructura se toman literalmente de `presentaciones/giron-cc/index.html`.

Tono profesional y dinámico: la propuesta se ve en movimiento, con transiciones marcadas entre escenas y mucho detalle animado, sin perder legibilidad de cifras ni de textos.

## Formato

- 1920 × 1080 (16:9), **120 fps**, MP4, calidad **great** (`--quality delivery`, CRF alto).
- ~100 s, 9 escenas, sin narración ni música (no se proveyó audio).

## Escenas (1 por lámina)

| # | t (s) | Lámina del deck | Entrada / salida |
|---|-------|-----------------|------------------|
| 1 | 0–11 | Portada | anillos que se dibujan, hojas que flotan, logos co-brand, título por palabras · salida: iris dorado |
| 2 | 11–20 | Cuatro fases, una ruta | 4 tarjetas en flip 3D escalonado, anillos, franja «Transversal» · salida: empuje horizontal |
| 3 | 20–30 | Fase 1: entender, diseñar y depurar la data | 3 columnas, ítems entran en cascada, badges «Nuevo/Ajustado» que rebotan · salida: barrido vertical con barra violeta |
| 4 | 30–40 | Fase 1: la cartera en tiempo real | 3 tarjetas + contador «7.000 deudores» · salida: zoom con blur |
| 5 | 40–53 | Fase 2: contacto automático en cascada | flujo WhatsApp → Correo → Llamada con trazos que se dibujan, contador a 1.000 llamadas, 4 tarjetas · salida: diagonal |
| 6 | 53–63 | Fase 3: escalamiento y piloto | 3 tarjetas + franja de 3 ítems · salida: cortina dorada + violeta |
| 7 | 63–75 | Fase 4: ampliaciones posteriores | 6 tarjetas en grilla, cobro coactivo en navy con chevrones · salida: giro 3D |
| 8 | 75–87 | Fuera de alcance e insumos | 2 columnas, marcas de verificación que se dibujan · salida: iris rectangular |
| 9 | 87–100 | ¿Cuándo empezamos? | pasos 1-2-3 conectados, valor $209.976.550 COP con contador, 9 roles entrando · cierre |

## Estilo (Brandbook Campuslands, reglas supremas de `CLAUDE.md`)

- Fondo **blanco** `#FFFFFF` en todas las escenas. Navy `#000087`, violeta `#5E3AE2`, dorado `#F4B422`, celeste `#2CAAFF`, verde `#00AA80` solo en tarjetas, íconos y acentos. Arena `#E4E4DB` solo como acento.
- **Poppins** en todo el video (400/500/600/900 + Black Italic), desde `assets/fonts/`.
- Sin bordes ni líneas: las tarjetas se separan por **sombra**. Acentos de color ≥ 3 px permitidos.
- Co-branding «Campuslands × Alcaldía» **solo** en portada y cierre; las láminas de contenido no llevan logos. Los logos van a color, sin recolorear.
- **Sin** rótulo «Confidencial».
- Pie: migas `| campuslands | propuesta | giron | … |` a la izquierda y lema «Exploramos · Despegamos · Conquistamos» a la derecha. Numeral fantasma pequeño y difuminado.

## Assets

- `presentaciones/giron-cc/assets/logo-campuslands-color.png` — logo Campuslands a color (portada, cierre). Se copia a `assets/`.
- `presentaciones/giron-cc/assets/logo-cliente-color.png` — logo Alcaldía de Girón (portada, cierre). Se copia a `assets/`.
- `presentaciones/giron-cc/assets/fonts/Poppins-*.ttf` — tipografía. Se copia a `assets/fonts/`.

## Customizations

- **Transiciones dinámicas**: cada cambio de escena usa una transición distinta (iris, empuje, barrido, zoom con blur, diagonal, cortina, giro, iris inverso).
- **Muchas animaciones, de todo tipo**: entradas 3D, trazos que se dibujan, contadores, cascadas, flotación de decorativos, rebotes, shimmer en tarjetas navy, conectores animados.

## Notes

- **Paleta: Campuslands, no la del deck.** `presentaciones/giron-cc/styles.css` usa dorados y cafés (`--violet:#8A5A0E`, `--gold:#F0C24E`, `--navy:#4A3608`) derivados del logo del cliente. `CLAUDE.md` regla 1 prohíbe esa paleta. El video usa la paleta Campuslands. **Inferido, no confirmado** — el usuario puede pedir la paleta del deck.
- Cifras y textos literales del deck, sin inventar datos: «unos 7.000 deudores», «1.000 llamadas diarias», «$209.976.550 COP», «Octubre 2026».
- Ninguna escena inventa contenido fuera del deck.
- Render: `--fps 120 --quality delivery --resolution 1080p` (solo tras aprobación de la vista previa).
