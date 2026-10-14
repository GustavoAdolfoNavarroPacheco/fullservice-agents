# Estándar de diseño — FullService Campuslands v3 (láminas 2 a 6)

Establecido el 2026-10-14 al rediseñar `presentaciones/fullservice-campuslands-v3/`. Es la gramática única de las láminas de contenido de ese deck (la portada conserva su propio layout).
El contenido no se toca: solo cambia lo visual. Código: bloque «7. SISTEMA DE DISEÑO» de `styles.css`.

## 1. Lienzo y márgenes
| Token | Valor | Regla |
|---|---|---|
| `--m` | 32 px | Margen **igual en los 4 lados** (izquierda, derecha, arriba, abajo). El audit mide `hd.l = hd.t = bd.l = bd.r = bd.b = 32`. |
| `--gut` | 16 px | **Canal único** entre bloques, horizontal y vertical. |
| Rejilla | 12 columnas | `c4 / c5 / c6 / c7 / c8 / c12`. Fila 1 = 4+8 (Staffing) o 4+4+4 (BPO); franja inferior = 7+5; comparativo = 6+6. |
| `--foot-h` | 128 px | Altura **fija** de la franja inferior (Beneficios + Modalidad en L2/L3; banda de cierre en L4). |

## 2. Encabezado único (`.hd`)
Eyebrow (8 pt, Montserrat 700, tracking .3 em) + título (Playfair 20 pt, acento en cursiva Black azul) + subtítulo opcional (Poppins 500 9,5 pt). Siempre arriba a la izquierda, en la misma posición en las 5 láminas. A la derecha, solo la pastilla de conteo (L4–L6). Título en **una sola línea**.

## 3. Cuatro tipos de tarjeta (mismo radio 20 px, padding 18 × 22, barra de acento de 4 px, sombra)
| Tipo | Clase | Uso |
|---|---|---|
| Navy | `.card--navy` | Contenido principal (perfiles, líneas de servicio, LMS, Facturación, agentes, comparativo). |
| Blanca | `.card--white` | Apoyo: ¿Qué es?, ¿Cómo funciona?, Beneficios. |
| Celeste | `.card--hi` | El dato comercial (Modalidad comercial). Máximo **uno por lámina**. |
| Azul | `.card--blue` | Cierre (mensaje + llamado a la acción). |

Cabecera de tarjeta navy: `.ch` = ícono 40 px + (rótulo 7 pt sobre título 13 pt). Si la tarjeta es un contenedor de chips (Perfiles), la cabecera es solo un rótulo.

## 4. Escala tipográfica (fija)
| Rol | Tamaño |
|---|---|
| Título de lámina | 20 pt |
| Título de tarjeta (h3) | 13 pt |
| Título de ítem (pasos, perfiles) | 10 pt / 9 pt |
| **Cuerpo estándar** | **8,5 pt** (todas las láminas salvo el comparativo) |
| Cuerpo del comparativo (texto corto) | 9,5 pt |
| Rótulos / tags | 7 pt, mayúsculas |
| Mínimo absoluto | 7 pt (numerales de lista) — nada por debajo |

## 5. Íconos y numerales (3 + 2 tamaños)
Íconos: `l` 40 (cabecera de tarjeta), `m` 32 (perfiles, minitarjetas), `s` 24 (viñetas de beneficios). Numerales: 32 px (pasos) y 22 px (lista del LMS).

## 6. Esqueleto de las láminas de servicio (L2 Staffing y L3 BPO)
Fila 1 (flexible): ¿Qué es? + contenido principal → fila 2 (a la medida): ¿Cómo funciona? (rótulo a la izquierda, 4 pasos en 4 columnas iguales) → fila 3 (128 px): Beneficios (2 columnas) + Modalidad comercial. Las tarjetas de texto sin relleno suficiente centran su contenido en vertical (mismo aire arriba y abajo).

## 7. Colores
Fondo de lámina `#F2F3F5` (pedido del usuario); texto sobre fondo `--dk #00123A` / `--dk-mid #3F4D78`; tarjetas navy `--panel-a/b`; acento azul `--blue-2`; celeste solo en lo comercial. Sin bordes: todo se separa por sombras.

## 8. Verificación (cada build)
1. `_audit.js` (script de medición, no se versiona): márgenes = 32, canales = 16, sin solapes, sin contenido a < 10 px del borde de su tarjeta, sin texto recortado, fuente mínima.
2. Comparación de textos contra la versión anterior (solo difieren las 4 descripciones de «¿Cómo funciona?» de Staffing, eliminadas por pedido, y «Niveles» → «Niveles de experiencia»).
3. Revisión a la vista de las 5 láminas en el PDF y de una lámina en el visor.
