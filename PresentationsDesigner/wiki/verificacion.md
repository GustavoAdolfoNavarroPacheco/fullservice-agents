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
| Colores de fondo | solo paleta Campuslands | R1 |
| Altura de logos (Campuslands vs cliente) | diferencia ≤ 3 % | R2 |
| Orden de logos | Campuslands a la izquierda | Brandbook p.6 |
| Deformación del logo | proporción dibujada = natural (±3 %) | Brandbook p.16 |
| Versión del logo vs fondo | blanco en navy/violeta · color en arena | R5 |
| Fuentes | solo Poppins 400/900, Roboto Mono 400, Nutmeg · cargadas | Brandbook p.10 |
| Texto mínimo | ≥ 9 px | legibilidad |
| Contraste | ≥ 4,5 : 1 (≥ 3 : 1 si es grande) | accesibilidad |
| Geometría | nada fuera de la lámina, nada sobre el pie, nada recortado | calidad |
| Imagen vs contenedor | ninguna `<img>` excede su caja (logos de cliente, etc.) | calidad |
| Hueco vertical | ≤ 20 % de la lámina (no aplica a portada/cierre centrados) | balance |
| PDF | páginas = láminas; sin fuentes de respaldo | entrega |
| `<head>` | `<title>` = razón social del cliente · favicon = isotipo | CLAUDE.md |

## 2. Revisión a la vista (obligatoria, lámina por lámina)
Abrir cada PNG (`--png-dir`) y mirar, **en este orden**:
1. **Logos:** ¿se ven del mismo tamaño? ¿el de Campuslands va primero? ¿contrastan con el fondo? ¿hay aire alrededor (≥ X de la M)?
2. **Jerarquía:** ¿qué se lee primero, segundo, tercero? ¿coincide con lo que el cliente debe entender?
3. **Espacios:** ¿hay franjas muertas o elementos pegados? ¿el reparto se ve **intencional**?
4. **Color:** ¿el fondo es de la marca? ¿los acentos cumplen los pares de contraste? ¿no hay más de un marco neón?
5. **Tipografía:** ¿Poppins en títulos, Roboto Mono en cuerpo? ¿ningún texto con fuente de respaldo (se ve distinto)?
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
- Portada/cierre centrados: no se mide el hueco superior/inferior.
- Un aviso de hueco se **puede justificar** si el vacío es composición deliberada (p. ej. afirmación con mucho aire); decirlo en la bitácora.
