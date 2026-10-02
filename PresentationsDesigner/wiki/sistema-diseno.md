# Sistema de diseño v3 — Brandbook Campuslands

> Reemplaza al sistema v2 (archivado en [[archivo/README]]). Normativa de marca: [[marca-campuslands]]. Protocolo de revisión: [[verificacion]].
> **Punto de partida de todo deck nuevo:** copiar `presentaciones/_plantilla-campuslands/` (7 láminas de ejemplo que ya cumplen
> todas las reglas y pasan el verificador) y reemplazar contenido; **no** partir de un deck de cliente anterior.

---

## 1. Principios
1. **Marca primero.** Fondos, color, tipografía y logos salen del Brandbook; el cliente solo aporta su logo y su contenido.
2. **Dinámico, no plano.** Cada lámina cambia de arquetipo respecto a la contigua y usa al menos un recurso del lenguaje gráfico de marca.
3. **Cada objeto tiene un porqué.** Posición, tamaño y color responden a una jerarquía que se puede explicar en una frase (§7).
4. **Se verifica, no se supone.** Todo se mide con `verificar_deck.py` y se mira a la vista ([[verificacion]]).
5. **Máximo 10 láminas** (salvo pedido textual del usuario).

## 2. Tokens (`:root`) — copiar de la plantilla
```css
--violet:#5E3AE2; --gold:#F4B422; --green:#00AA80; --navy:#000087; --sky:#2CAAFF; --sand:#E4E4DB;   /* paleta oficial */
--white:#FFFFFF; --ink:#373435;                       /* apoyos: texto/logo sobre oscuro · texto sobre arena */
--bg-sand:   radial-gradient(60% 60% at 0% 100%, rgba(94,58,226,.13), transparent 62%), #E4E4DB;   /* ÚNICO fondo de lámina y del visor; SIN difuminación celeste arriba-derecha */
--font-title:'Poppins'; --font-body:'Roboto Mono'; --font-accent:'Nutmeg','Poppins';
--logo-h:30px;  --logo-h-cover:64px;                  /* alto del logo de Campuslands */
--k-cliente:<√(ratio Campuslands / ratio cliente)>;   /* igualar_logos.py: alto del cliente = alto Campuslands × k → ÁREAS IGUALES */
```
**TEMA CLARO OBLIGATORIO (web y presentación):** el único fondo de lámina permitido es `sand` — `data-bg="sand"` en la raíz de la lámina — y el visor
(barras y página) también es arena. Todo color de un fondo debe ser de la paleta (los *glows* usan el `rgb` de un color de la paleta con alfa).
Navy/violeta/dorado/verde/celeste existen **solo como tarjetas, franjas, íconos, acentos y figuras difuminadas** sobre la arena.
**Prohibido** como fondo de lámina o de visor: navy, violeta, blanco, gris frío, negro, colores derivados del cliente, dorado/verde/celeste a pantalla completa.
**Prohibido** el rótulo/badge/óvalo «Confidencial».

## 3. Grilla y estructura
- Lámina nativa **1056 × 594 px** (11 × 6,1875 in a 96 dpi) = tamaño del PDF. Padding lateral `.62in`, vertical `.42in / .38in`.
- `.sl[data-bg]` (raíz) → contenido (el título abre la lámina) · `.ft` (pie). Portada y cierre: sin cabecera, co-branding centrado.
- **Láminas de contenido: sin cabecera de logos** (el verificador rechaza logos en láminas de contenido). El co-branding vive solo en portada, cierre y barra del visor, con la «×» (`.x`) centrada y el logo del cliente a `--k-cliente`.
  Numeral de sección translúcido (`.ghost`) arriba a la derecha.
- **Pie:** izquierda *Exploramos · Despegamos · Conquistamos* · centro migas `| campuslands | propuesta | cliente | sección |` · **sin** indicador `NN / TT` a la derecha.
- **Portada y cierre:** co-branding **centrado y grande** (`--logo-h-cover`), título con `</`, fondo `.deco-cover` (anillos concéntricos + resplandor central violeta + dos hojas laterales violeta/celeste, baja saturación; sin chevrones ni manchas), sin cabecera.
  Pie de portada en **Poppins** (etiquetas Black, valores Regular) con «Fecha» = **Mes Año** (p. ej. «Octubre 2026»).
- El deck se entrega en el **visor de una lámina a la vez** (`script.js`, `zoom` y no `transform:scale()`); la barra superior del visor también
  lleva «Campuslands × Cliente» con el mismo peso visual y es **clara**. El PDF oculta el visor (`@media print`).

## 4. Tipografía (resumen; detalle en [[marca-campuslands]] §5)
| Elemento | Fuente | Tamaño orientativo |
|---|---|---|
| Título de portada / cierre | Poppins Black | 38–44 pt |
| Título de sección | Poppins Black (`.sec`) con `</` y una palabra en *Black Italic* de acento | 26–29 pt (hasta 38 pt en afirmación) |
| Número grande / métrica | Poppins Black | 36–78 pt |
| Etiqueta | Poppins Black en celeste/violeta/arena `{ … }` | 9–9,5 pt |
| Cuerpo, listas, pies, migas | Roboto Mono 400 | 9–12 pt (**mínimo 9 px**; pie 7,5 pt) |

Roboto Mono es ancha: líneas más cortas, tamaños un punto por encima de lo que se usaría con una proporcional.

## 5. Componentes (clases de la plantilla)
| Componente | Clase | Cuándo |
|---|---|---|
| Co-branding | `.cobrand` (+ `.sep`) | Cabecera, portada, cierre, visor. |
| Título de sección | `.sec` + `.mark` (`</`) + `.em` (acento) | Toda lámina interna. |
| Etiqueta / lista / subtítulo | `.label` · `.code-list` (`=>`) · `.tagline` (`<= … =>`) | Jerarquía secundaria. |
| Numeral fantasma | `.ghost` | Esquina sup. derecha de cada lámina interna. |
| Tarjeta | `.card` (blanca sobre arena) · `.card--navy` (acento oscuro: dato clave, panel «Con la propuesta») | Agrupar contenido. |
| Métrica | `.metric` (barra superior de color) | Cifras (4 por lámina como máximo). |
| Peldaño de proceso | `.step` + `.go` | Secuencias (escalera + chevrón conector). |
| Panel antes/después | `.panel--hoy` / `.panel--nuevo` + `.delta` | Comparaciones con indicador de impacto. |
| Módulo con ícono | `.mod` + `.ico--{sky,gold,green,violet,navy}` | Cuadrículas de capacidades. |
| Franja de lectura | `.reading` | Cierra una lámina con la conclusión (una por lámina). |
| Marco neón | `.neon` | **Un** dato o tarjeta clave por lámina. **Nunca** en banners/franjas (`.reading`, notas): sin borde dorado. |
| Fondo de portada/cierre | `<svg class="deco-cover">` (`.ring`, `.ring.accent`, `.blade--l/--r`; `aria-hidden`) | Solo en portada y cierre; copiar el bloque `DECO` de la plantilla. |
| Chevrones | `.chev` (`aria-hidden`) | Solo conectores puntuales; ya no decoran la portada. |
| Comilla | `.qmark` | Afirmación/cita. |
| Chips | `.pill--{gold,sky,green,violet}` | Estados y categorías. |

## 6. Arquetipos y ritmo (R3 — dinamismo)
Arquetipos de la plantilla: **portada · afirmación · métricas · proceso (escalera) · antes/después · módulos · cierre**. Otros válidos:
timeline, diagrama de capas, tabla de planes, mapa, comparador de opciones, galería de logos/clientes.
- **No repetir** el mismo arquetipo en láminas contiguas.
- **El fondo no cambia** (tema claro): el ritmo sale de alternar arquetipos y de dónde se usan las **tarjetas de acento** navy/violeta (p. ej. navy para el dato clave o la conclusión).
- Variar el protagonista (izquierda/centro/derecha) y la escala (un número gigante *vs.* una cuadrícula densa).
- Animar solo `transform`, `opacity`, `clip-path`.

## 7. Razón de ubicación (R7)
Cada objeto debe poder responder: *¿por qué está aquí, a este tamaño y con este color?* Respuestas válidas: «es lo primero que debe leer el
cliente», «agrupa lo que se compara», «cierra con la conclusión», «da respiro entre dos bloques densos». Se escribe en el **plan** (por lámina)
y se revisa en [[verificacion]] §3. Lo que no tenga razón se quita.

## 8. Balance de espacio (se mantiene y se mide)
Ni vacío ni apretado. El verificador avisa si hay un **hueco vertical > 20 %** de la lámina (entre bloques, bajo la cabecera o sobre el pie;
excepto portada/cierre centrados). Orden de corrección: más contenido útil → tarjetas/tipografía más grandes → más `gap`. Nunca "rellenar".

## 9. Contraste de texto
Usar solo los pares de [[marca-campuslands]] §4 (✅). Sobre arena: títulos navy, acentos violeta, cuerpo tinta; el dorado **no** es texto sobre arena (solo íconos/barras). Sobre tarjeta navy: blanco, dorado y celeste.

## 10. Lecciones técnicas vigentes
- **Fuentes y PDF:** las `@font-face` de láminas ocultas no se descargan solas; `script.js` ejecuta `preloadAllFonts()` y el export usa
  `--virtual-time-budget`. Roboto Mono (variable) sale como **Type3** en el PDF: es normal; lo que se vigila es que **no** aparezcan
  Liberation/Georgia/Times/Arial.
- **Densidad con Roboto Mono:** es ~25 % más ancha que una proporcional; una lámina que cabía con tipografías anteriores debe **partirse en dos** (caso Globant: LMS + facturación → 2 láminas) en lugar de reducir por debajo de 9 px.
- **Logos en `<img>`:** solo `height` + `width:auto` (el del cliente: `calc(var(--lh)*var(--k-cliente))`); el logo del cliente se recorta a su contenido (alfa) y se prueba que no se deforme.
- **Imágenes de placeholder** no deben usar fuentes del sistema (generar PNG con Poppins) para no contaminar el PDF.
- **Decoración** (`aria-hidden`, `.ghost`, `.chev`) sangra a propósito y queda fuera de las mediciones de desborde; el texto nunca.
- **Impresión:** `@page{size:11in 6.1875in; margin:0}` + `print-color-adjust:exact`.

## 11. Anti-patrones (cero tolerancia)
Fondos oscuros o fuera de paleta (tema claro obligatorio) · rótulo «Confidencial» · línea divisoria `|` entre logos (va «×») · «×» descentrada · logos de distinto peso visual (misma altura con proporciones distintas) o deformados · chevrones laterales o manchas difuminadas en la portada · logos arriba a la izquierda en láminas de contenido · difuminación celeste arriba a la derecha · indicador de página «NN / TT» · borde dorado en banners · tarjetas que se pisan o texto que se sale de su tarjeta · pie de portada en Roboto Mono o fecha solo con el año · Playfair/Montserrat/
otras tipografías · todas las láminas con el mismo arquetipo · texto corrido centrado · decoración sobre texto · más de 10 láminas sin pedido
textual · tarjetas con 40 % de aire muerto · subrayados/`hr` decorativos bajo títulos · color plano donde la marca pide el recurso gráfico.
