# Logos oficiales de Campuslands

Fuente: archivos entregados por el usuario (2026-10-02) junto al Brandbook. Normativa de uso: [[marca-campuslands]] §3.

| Archivo (PNG, transparente) | Contenido | Fondo donde se usa |
|---|---|---|
| `campuslands-horizontal-color(.png / -recortado.png)` | casco + wordmark, a color | **arena** |
| `campuslands-horizontal-blanco(...)` | casco + wordmark, blanco | **navy**, **violeta** |
| `campuslands-vertical-color(...)` | casco sobre wordmark, a color | **arena** |
| `campuslands-vertical-blanco(...)` | casco sobre wordmark, blanco | **navy**, **violeta** |
| `vectoriales/` | 2 PDF vectoriales (horizontal) + `.ai` editable (22 páginas) | impresión / escalas grandes |
| `medidas-logos.json` | proporción y **unidad X (alto de la "m")** de cada variante | cálculo de espacio libre |

- Los **`-recortado.png`** están cortados al contenido exacto (sin padding): son los que se copian a `assets/` de cada deck.
- Elegir la variante con `python3 herramientas/elegir_logo.py <fondo>` (contraste). Dorado, verde y celeste **no** son fondos válidos para logos.
- **Nunca** recolorear, rotar, estirar, recortar elementos ni cambiar la distribución (Brandbook p.16).
- **Logo horizontal a color vigente (reemplazo del usuario, 2026-10-02): 2000 × 464 px, 4,31 : 1.** Sustituye al del Brandbook (3,20 : 1), que se conserva en `archivo/campuslands-horizontal-color-brandbook*.png`. Sobre blanco: texto 12,3 : 1; casco 1,36 – 14,2 : 1 (mediana 3,25 : 1; el reflejo celeste claro `#8BEBFF` es el punto más pálido). El archivo trae una **astilla oscura de 2 px** (columnas 637–638) entre el casco y la «c» —artefacto del archivo entregado, sin tocar; a 44–64 px de alto mide ≈ 1 px—. `elegir_logo.py` conserva las constantes del degradado del Brandbook.
- El horizontal blanco (5,05 : 1) y el horizontal a color (4,31 : 1) son archivos con con **proporciones distintas**; no se igualan estirando. Con **tema claro obligatorio** (2026-10-02) se usa el **horizontal a color**. El peso visual frente al logo del cliente se iguala por **área** con `herramientas/igualar_logos.py`.
- Los logos antiguos de `recursos/` (`Logo Campuslands ... Horizontal/Vertical Azul/Blanco.png`) son los mismos archivos con otros nombres; **usar esta carpeta**.

- **Logos de cliente verticales** (p. ej. escudo de Girón, 0,65 : 1): igualar el área exigiría k > 2,5 y un logo demasiado alto para la barra del visor; `igualar_logos.py` limita k a 2,0 y avisa. El verificador lo reporta como aviso.
