# Theming por Cliente — Paleta derivada del logo

> **Regla nueva (2026-07-07):** cada presentación usa una **paleta propia derivada del
> logo del cliente**, incluyendo el **fondo oscuro teñido** hacia el color de marca. Se
> conserva el mismo *estilo* de la plantilla (dark premium, gradientes, fuentes locales,
> layouts); lo único que cambia por cliente es un bloque acotado de tokens. Ver
> [[sistema-diseno]] (contrato de tokens) y [[marca-campuslands]] (la paleta cian/violeta
> pasa a ser solo el tema *default* de Campuslands, no la de todos los decks).

Prueba visual de la gama: [`presentaciones/_temas-demo/index.html`](file:///C:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/_temas-demo/index.html)
(misma lámina, 6 paletas con fondo teñido distinto).

---

## 1. Contrato de theme-tokens (lo único que cambia por cliente)

El resto de `styles.css` es **idéntico** entre decks. Solo se re-definen estos tokens en
`:root`:

```
--bg-0 --bg-1 --bg-2 --bg-deep          /* fondo oscuro TEÑIDO al hue de marca */
--bg-glow-a --bg-glow-b                  /* glows con acentos de marca */
--cyan --blue --violet --magenta         /* 4 paradas del set (nombres se conservan) */
--grad-brand --grad-cyan --grad-violet   /* gradientes construidos con esas 4 paradas */
--card-border                            /* rgba del hue a ~.14–.20 */
--text-mid --text-lo --text-faint        /* tinte MUY leve hacia el hue */
--dot-confidential --dot-confidential-glow /* punto "Confidencial"/acento cálido */
```

> **Cambio estructural obligatorio:** se introduce `--bg-deep` (antes el color profundo
> `#0B1120` estaba *hardcodeado* en `.slide`, `.glow-a`, `.glow-b`). El nuevo `styles.css`
> usa `var(--bg-deep)` en esos tres lugares para que el fondo sea 100% tematizable.

---

## 2. Receta: del logo a la paleta

> **Estándar vigente desde 2026-07-10 (Regla 2 de `CLAUDE.md`): fondo gris claro neutro y frío
> + gradiente de marca superpuesto.** Los pasos 4–5 de abajo reflejan este estándar. Los decks
> construidos antes de esta fecha usan el sistema oscuro legado (fondo casi negro teñido) y
> **no se migran** salvo pedido explícito del usuario — ver nota al final.

1. **Extrae** 1–2 colores dominantes del logo (los de marca; ignora negros/grises
   neutros). Define el **hue base H** (y un hue secundario si aplica).
2. **Gradiente insignia (`--grad-brand`):** 3–4 paradas **análogas** alrededor de H
   (rota ±25–55°), de claro-brillante a medio. Deriva `--grad-cyan` (2 paradas frías del
   set) y `--grad-violet` (2 alternas) para variar entre láminas.
3. **Sólidos** `--cyan/--blue/--violet/--magenta`: remapea a las 4 paradas, pero **profundizadas
   para contraste sobre claro** (p. ej. un naranja de marca vívido se oscurece a un naranja
   quemado para texto/labels legibles en blanco). Los nombres se conservan por compatibilidad.
4. **Fondos** `--bg-0/1/2/deep`: **gris claro neutro y frío**, gama `#E2E4E9` → `#FFFFFF`
   (`--bg-2`, el de las tarjetas, siempre el más claro/blanco). No se tiñe con el hue de marca
   directamente — el color de marca vive en el `--bg-wash`, no en la base.
5. **`--bg-wash` (nuevo, obligatorio):** `linear-gradient` diagonal con 3–4 paradas de los
   colores de marca en `rgba(...,.05–.09)`, superpuesto sobre la base gris junto a los dos
   `--bg-glow-a/b` radiales (también bajados a alpha **.08–.12** en este estándar claro, más
   suaves que en el sistema oscuro). Así el fondo "respira" el gradiente de marca sin perder
   neutralidad. Ver receta completa en `presentaciones/multinal-escenario-b/styles.css`.
6. **Texto:** `--text-hi` casi negro (`#14161B`–`#1A1D23`), `--text-mid/lo/faint` grises fríos
   descendentes, **nunca** blanco/crema (eso era del sistema oscuro).
7. **Bordes** `--card-border`: `rgba(20,25,35,.08–.12)` — neutro oscuro suave, no del hue de marca.
8. **Logo Campuslands:** recortar el PNG maestro a su contenido visible (bbox) + padding
   simétrico ~6% antes de copiarlo a `assets/` del deck — el archivo maestro trae relleno
   transparente irregular que lo hace ver chico/asimétrico si se usa tal cual.

### Reglas de seguridad
- **Legibilidad primero:** con fondo claro, todo texto de color (`--cyan`, `--violet`, etc.)
  debe profundizarse hasta pasar contraste AA sobre blanco — nunca copiar tal cual un tono
  vívido de marca pensado para fondo oscuro.
- **Marca cálida** (ámbar/rojo/naranja): el punto "Confidencial" y alertas se ponen en un
  **acento frío** (cian/azul) para que resalte; con marca fría, el punto sigue en ámbar.
- **Dos clientes con el mismo color** (p. ej. GreenMetal y Mchaileh, ambos verdes): sepáralos
  por **trayectoria de gradiente + wash** para que no se vean iguales.
- **Decoraciones (esquinas, anillos, glows, wash):** verificar SIEMPRE en el navegador antes de
  entregar — un decorativo pensado para fondo oscuro (opacidad, color) puede volverse invisible
  o chocar visualmente sobre fondo claro.
- **Legado oscuro:** los decks previos a 2026-07-10 (Miami Aqua Tours, GreenMetal, Mchaileh,
  Compumax, Ve a la Segura) mantienen su fondo oscuro teñido tal cual — no se retocan salvo
  que el usuario lo pida explícitamente para ese cliente.

---

## 3. Catálogo de paletas por cliente

Bloques listos para pegar en el `:root` de cada `styles.css` (ver valores completos en la
demo). Solo se muestran los tokens que cambian.

### Campuslands — default (tech · azul-violeta)
```css
--bg-0:#05070F; --bg-1:#0A0E1A; --bg-2:#0D1424; --bg-deep:#0B1120;
--bg-glow-a:rgba(53,208,240,.12); --bg-glow-b:rgba(139,92,246,.12);
--cyan:#35D0F0; --blue:#4A7DFF; --violet:#8B5CF6; --magenta:#C05CF6;
--grad-brand:linear-gradient(100deg,#35D0F0 0%,#4A7DFF 42%,#8B5CF6 76%,#C05CF6 100%);
--grad-cyan:linear-gradient(120deg,#35D0F0,#4A7DFF);
--grad-violet:linear-gradient(120deg,#6E8BFF,#C05CF6);
```

### Compumax — azul de marca
```css
--bg-0:#04070E; --bg-1:#061019; --bg-2:#0A1622; --bg-deep:#07172A;
--bg-glow-a:rgba(27,155,215,.14); --bg-glow-b:rgba(46,107,240,.12);
--cyan:#35D0F0; --blue:#1B9BD7; --violet:#2E6BF0; --magenta:#6E8BFF;
--grad-brand:linear-gradient(100deg,#35D0F0 0%,#1B9BD7 40%,#2E6BF0 74%,#6E8BFF 100%);
--grad-cyan:linear-gradient(120deg,#35D0F0,#1B9BD7);
--grad-violet:linear-gradient(120deg,#2AC0E8,#4A7DFF);
--card-border:1px solid rgba(90,150,210,.18);
--text-mid:#BFD3E6; --text-lo:#7690A8; --text-faint:#45566B;
```

### GreenMetal — verde lima/teal
```css
--bg-0:#040A06; --bg-1:#07130D; --bg-2:#0B1B14; --bg-deep:#08160F;
--bg-glow-a:rgba(47,224,194,.13); --bg-glow-b:rgba(55,200,113,.12);
--cyan:#2FE0C2; --blue:#37C871; --violet:#7BD13B; --magenta:#A6E22E;
--grad-brand:linear-gradient(100deg,#A6E22E 0%,#37C871 42%,#1FB6A6 74%,#2FE0C2 100%);
--grad-cyan:linear-gradient(120deg,#2FE0C2,#37C871);
--grad-violet:linear-gradient(120deg,#8BD84A,#1FB6A6);
--card-border:1px solid rgba(120,200,160,.18);
--text-mid:#C3D6C9; --text-lo:#7E9187; --text-faint:#495A50;
```

### Mchaileh — verde hoja/esmeralda de marca (distinto de GreenMetal)
> Derivado del logo real: verde **lima** (techo izq.) + verde **hoja/esmeralda** (cuerpo y
> subrayado). Se diferencia de GreenMetal por trayectoria: GreenMetal es **lima-forward → teal**
> (termina cian-menta); Mchaileh es **hoja/kelly-forward → esmeralda** (se queda en verde, sin
> teal) sobre un fondo **bosque teñido**. Aplicado al deck el 2026-07-08 (reemplaza el bloque
> anterior esmeralda→azul, que introducía un azul ajeno a la marca).
```css
--bg-0:#040A06; --bg-1:#08140C; --bg-2:#0C1F14; --bg-deep:#081A0F;
--bg-glow-a:rgba(64,200,96,.13); --bg-glow-b:rgba(155,213,52,.10);
--cyan:#4FD07A; --blue:#34C24E; --violet:#1FA95F; --magenta:#8CC63E; --lime:#9BD534;
--brand-green:#3DAE48;
--grad-brand:linear-gradient(100deg,#9BD534 0%,#4FD07A 38%,#22B06B 72%,#1FA95F 100%);
--grad-cyan:linear-gradient(120deg,#4FD07A,#22B06B);
--grad-violet:linear-gradient(120deg,#8CC63E,#1FA95F);
--card-border:1px solid rgba(110,190,130,.16);
--text-mid:#C6DBC9; --text-lo:#7C9683; --text-faint:#47604F;
```

### Ve a la Segura — "concierto" (violeta-negro · rosa→magenta→violeta→índigo)
```css
--bg-0:#0A0612; --bg-1:#120B1E; --bg-2:#1A1129; --bg-deep:#150D22;
--bg-glow-a:rgba(255,111,184,.13); --bg-glow-b:rgba(139,92,246,.13);
--cyan:#FF6FB8; --blue:#E14FD1; --violet:#9B5DE5; --magenta:#6C63FF;
--grad-brand:linear-gradient(100deg,#FF6FB8 0%,#E14FD1 38%,#9B5DE5 72%,#6C63FF 100%);
--grad-cyan:linear-gradient(120deg,#FF6FB8,#E14FD1);
--grad-violet:linear-gradient(120deg,#9B5DE5,#6C63FF);
--card-border:1px solid rgba(180,130,220,.18);
--text-mid:#DCC9EC; --text-lo:#8E7CA3; --text-faint:#55465F;
--lime:#4ADE80; /* check "✓" verde-menta, más fresco que el lima por defecto sobre violeta */
```
Usado sin logo oficial (evento/boletería, sin PNG de marca): wordmark recreado con `.wm` en vez de
`<img>` — ver contrato de wordmark abajo.

### Multinal — naranja del ícono → índigo del wordmark (referencia del estándar claro)
> Derivado del logo real: naranja vivo (`#FF7A00`, óvalos del isotipo) hacia el índigo-violeta
> del wordmark (`#312883`). Marca **cálida** → el punto "Confidencial" se pone en cian frío
> por la regla de seguridad. **Primer deck en fondo gris claro + `--bg-wash`** (estándar desde
> 2026-07-10). Usado en `presentaciones/multinal-escenario-b/`.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(255,122,0,.09); --bg-glow-b:rgba(59,42,140,.09);
--bg-wash:linear-gradient(135deg, rgba(255,155,61,.07) 0%, rgba(255,122,0,.05) 32%, rgba(122,90,209,.05) 66%, rgba(59,42,140,.07) 100%);
--cyan:#A6480A; --blue:#FF7A00; --violet:#5A3FBF; --magenta:#3B2A8C;
--grad-brand:linear-gradient(100deg,#FF9B3D 0%,#FF7A00 38%,#7A5AD1 72%,#3B2A8C 100%);
--grad-cyan:linear-gradient(120deg,#FF9B3D,#FF7A00);
--grad-violet:linear-gradient(120deg,#7A5AD1,#3B2A8C);
--card-border:1px solid rgba(20,25,35,.10);
--text-hi:#14161B; --text-mid:#3D4451; --text-lo:#6B7280; --text-faint:#9CA3AF;
--dot-confidential:#0E8FB0; --dot-confidential-glow:rgba(14,143,176,.45);
```

### Ejemplos de rango (para marcas fuera de la gama fría)
**Cálido (ámbar/coral)** — punto Confidencial en cian:
```css
--bg-0:#0C0703; --bg-1:#160D06; --bg-2:#20140A; --bg-deep:#1A0F07;
--bg-glow-a:rgba(245,148,60,.14); --bg-glow-b:rgba(224,72,106,.12);
--grad-brand:linear-gradient(100deg,#FFC24B 0%,#F5943C 40%,#F0663C 74%,#E0486A 100%);
--dot-confidential:#35D0F0; --dot-confidential-glow:rgba(53,208,240,.7);
```
**Púrpura/magenta:**
```css
--bg-0:#08050F; --bg-1:#100A1B; --bg-2:#160F24; --bg-deep:#130C22;
--bg-glow-a:rgba(181,123,255,.14); --bg-glow-b:rgba(224,92,192,.12);
--grad-brand:linear-gradient(100deg,#B57BFF 0%,#8B5CF6 40%,#C05CF6 74%,#E05CC0 100%);
```

---

### Colbeef — rojo del wordmark → verde del isotipo (cárnica: producto → campo)
> Derivado del logo real: **rojo** (`#D93A2E`/`#B8341F`, wordmark "Colbeef") hacia **verde**
> (`#2E8B4F`/`#1B5E33`, isotipo). Marca **cálida** (rojo) → el punto "Confidencial" se pone en
> verde profundo (acento frío frente al rojo, por la regla de seguridad). Fondo gris claro +
> `--bg-wash` (estándar desde 2026-07-10). Usado en `presentaciones/colbeef-plan-trabajo/`.
> **Nota técnica:** evitar `background-clip:text` (gradiente) en números/labels grandes con
> `white-space:nowrap` — Chrome headless puede pintar un recuadro visible alrededor del texto
> al exportar a PDF (ver `.stat-card .big` en `presentaciones/colbeef-plan-trabajo/styles.css`,
> resuelto usando color sólido `--cyan`/`--violet` en vez de gradiente para esos elementos).
> **Reutilizada sin cambios (2026-09-10)** en `presentaciones/colbeef-flujo-ia/` (mismo cliente,
> documento distinto) — no se rederivó la paleta. Ese deck usa la técnica de texto en gradiente
> vía SVG (§5.2) para **todos** sus títulos desde el primer build, no solo como mitigación
> posterior: el patrón `<em class="gradient-text">` con texto negro en la misma línea (portada y
> los 17 `s-title` internos) sí disparó el bug de hairline en el PDF exportado, confirmando que
> el bug no es exclusivo de números/labels — aplica a cualquier `<em>` en gradiente mezclado con
> texto normal en una misma línea.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(217,58,46,.09); --bg-glow-b:rgba(27,94,51,.09);
--bg-wash:linear-gradient(135deg, rgba(224,74,58,.07) 0%, rgba(184,52,31,.05) 32%, rgba(46,139,79,.05) 66%, rgba(27,94,51,.07) 100%);
--cyan:#8A1F1F; --blue:#D93A2E; --violet:#2E8B4F; --magenta:#1B5E33;
--grad-brand:linear-gradient(100deg,#E2543F 0%,#D93A2E 34%,#4CAA6A 68%,#1B5E33 100%);
--grad-cyan:linear-gradient(120deg,#E2543F,#B8341F);
--grad-violet:linear-gradient(120deg,#4CAA6A,#1B5E33);
--card-border:1px solid rgba(20,25,35,.10);
--dot-confidential:#1B7A4A; --dot-confidential-glow:rgba(27,122,74,.45);
```

### Avicampo — sol amarillo → naranja de marca → verde "frescura" (avícola)
> Derivado del logo real: **amarillo** del sol (`#FDB913`) → **naranja** vivo del wordmark
> "avicampo" (`#FF8A00`) → **verde** de la línea "El sabor de la frescura" (`#4CAF50`/`#1B5E33`).
> Narrativa de marca completa (sol/calor → campo/frescura), distinta de Multinal (naranja→índigo)
> y Colbeef (rojo→verde). Marca **cálida** (naranja) → el punto "Confidencial" se pone en verde
> profundo (acento frío frente al naranja, por la regla de seguridad). Fondo gris claro +
> `--bg-wash` (estándar desde 2026-07-10). Usado en `presentaciones/avicampo/`.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(255,140,0,.09); --bg-glow-b:rgba(30,155,77,.09);
--bg-wash:linear-gradient(135deg, rgba(253,185,19,.07) 0%, rgba(255,138,0,.06) 30%, rgba(46,157,68,.05) 65%, rgba(27,94,51,.07) 100%);
--cyan:#A85A0E; --blue:#FF8A00; --violet:#2E9D44; --magenta:#1B5E33;
--grad-brand:linear-gradient(100deg,#FDB913 0%,#FF8A00 34%,#4CAF50 68%,#1B5E33 100%);
--grad-cyan:linear-gradient(120deg,#FDB913,#FF8A00);
--grad-violet:linear-gradient(120deg,#66BB6A,#1B5E33);
--card-border:1px solid rgba(20,25,35,.10);
--dot-confidential:#1B7A4A; --dot-confidential-glow:rgba(27,122,74,.45);
```
> **Nota técnica (2026-07-22):** en títulos internos (`.s-title`) donde el `<em>` en gradiente
> queda mezclado en la misma línea que texto negro normal, Chrome headless dibuja un hairline
> sutil bajo el gradiente al exportar a PDF (mismo bug ya documentado para Colbeef). Se resolvió
> con dos clases de acento **sólido** (`.title-accent` / `.title-accent--green`, alternando
> naranja/verde) en vez de `.gradient-text` para esos `<em>` mezclados — el gradiente se conserva
> en la portada (línea propia) y en la cifra de inversión (corrida corta aislada), donde no
> presentó el defecto.

### Gas País — amarillo → verde → azul (blend real del isotipo, Oil & Gas)
> Derivado del logo real: el isotipo funde un pétalo **amarillo** (`#FFD400`) y uno **azul**
> (`#0161B8`) en **verde** (`#4FA647`) donde se superponen; el wordmark "GasPaís" es un **verde
> bosque** sólido (`#0B5E2B`). El `--grad-brand` seguí literalmente esa transición
> amarillo→verde→azul en vez de forzar solo 2 colores. Marca **mixta** (cálido+frío) → el punto
> "Confidencial" se pone en **dorado** (`--cyan` profundizado) para contrastar sobre el fondo
> verde/azul-dominante. Fondo gris claro + `--bg-wash` (estándar desde 2026-07-10). Usado en
> `presentaciones/gaspais-chilco/`.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(255,212,0,.09); --bg-glow-b:rgba(1,97,184,.09);
--bg-wash:linear-gradient(135deg, rgba(255,212,0,.06) 0%, rgba(79,166,71,.05) 34%, rgba(11,90,39,.05) 68%, rgba(1,97,184,.07) 100%);
--cyan:#A87A00; --blue:#2F8F3E; --violet:#0E7A3E; --magenta:#0A5CA8;
--grad-brand:linear-gradient(100deg,#FFD400 0%,#4FA647 34%,#0E7A3E 68%,#0161B8 100%);
--grad-cyan:linear-gradient(120deg,#FFD400,#4FA647);
--grad-violet:linear-gradient(120deg,#0E7A3E,#0161B8);
--card-border:1px solid rgba(20,25,35,.10);
--dot-confidential:#C98A00; --dot-confidential-glow:rgba(201,138,0,.45);
```
> **Nota técnica (2026-07-29):** se confirmó que el bug de hairline de `background-clip:text`
> (ver §5 [[sistema-diseno]]) persiste **incluso con el elemento en `display:inline`** — se
> probó también sin itálica, sin `color:transparent` redundante, con `background-size:112%`
> (mitigación de Colbeef) y con `line-height:1`; ninguna variante lo eliminó. Se confirmó que el
> mismo artefacto ya existe, más sutil, en el PDF ya entregado de `presentaciones/avicampo/`
> (portada). Es un bug sistémico de Chrome headless con este patrón CSS en export a PDF, no
> específico de este deck.
>
> **Resuelto (2026-07-30):** se adoptó como estándar el texto en gradiente vía SVG
> (`<text fill="url(#...)">`) en vez de `background-clip:text` — ver §5.2 de
> [[sistema-diseno]] para el snippet y la nota de verificación. Todo deck nuevo debe usar
> esta técnica para títulos/portadas en gradiente; los decks ya entregados con el artefacto
> conocido (Avicampo, Gas País) no se regeneran retroactivamente salvo pedido explícito.

### Comultrasan — teal del banner → verde→lima del swoosh (financiera cooperativa)
> Derivado del logo real: **teal** (`#0B6667`, banda "Financiera") funde hacia el **verde→lima**
> del swoosh bajo el wordmark "COMULTRASAN" (`#3FAA46`→`#8DC63F`). Marca **fría** (teal+verde) →
> el punto "Confidencial" se queda en el **ámbar** por defecto (regla de seguridad). Fondo gris
> claro + `--bg-wash` (estándar desde 2026-07-10). Usado en `presentaciones/comultrasan-orbit/`.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(20,140,135,.10); --bg-glow-b:rgba(76,170,62,.10);
--bg-wash:linear-gradient(135deg, rgba(11,102,103,.07) 0%, rgba(20,130,114,.05) 32%, rgba(63,170,70,.05) 66%, rgba(141,198,63,.07) 100%);
--cyan:#0B6667; --blue:#14826E; --violet:#3FAA46; --magenta:#8DC63F;
--grad-brand:linear-gradient(100deg,#0B6667 0%,#14826E 34%,#3FAA46 68%,#8DC63F 100%);
--grad-cyan:linear-gradient(120deg,#0B6667,#14826E);
--grad-violet:linear-gradient(120deg,#3FAA46,#8DC63F);
--card-border:1px solid rgba(20,25,35,.10);
--dot-confidential:#F5A623; --dot-confidential-glow:rgba(245,166,35,.45);
```
> **Nota técnica:** el PNG del logo del cliente traía el fondo "blanco" con alfa uniforme ~50%
> (`rgba(255,255,255,128)`) en vez de transparencia real — un patrón nuevo, distinto del "fondo
> blanco opaco" ya documentado. Se reconstruyó el canal alfa por umbral de blancura (pixels cercanos
> a `#FFFFFF` → alfa 0; contenido de color/negro → alfa 255, con rampa lineal para el antialiasing)
> antes de recortar al bbox + padding simétrico ~8%. Si aparece este mismo patrón en otro logo,
> aplicar la misma reconstrucción de alfa en vez de solo recortar al bbox.

### Marval — azul claro del ícono → azul del wordmark → azul marino profundo
> Derivado del logo real: el isotipo "M/W" degrada de **azul claro** (`#4888C8`, trazo exterior)
> a **azul marino profundo** (`#003058`, punta), con relleno plateado/metálico; el wordmark
> "MARVAL" es un **azul vívido sólido** (`#1068B0`). Marca monocromática **fría** (azul) →
> el punto "Confidencial" se pone en **ámbar** por defecto (regla de seguridad). Fondo gris
> claro + `--bg-wash` (estándar desde 2026-07-10). Usado en `presentaciones/marval/`, deck con
> **switch de Escenario A / Escenario B** en la barra superior (API externa vs. modelo propio
> de IA) — primer deck con este patrón de shell interactivo con navegación de láminas y
> exportación a **dos PDFs** (uno por escenario) desde el mismo `index.html`.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(72,136,200,.09); --bg-glow-b:rgba(6,42,79,.09);
--bg-wash:linear-gradient(135deg, rgba(111,168,220,.07) 0%, rgba(72,136,200,.06) 32%, rgba(16,104,176,.05) 66%, rgba(6,42,79,.07) 100%);
--cyan:#0B3A6B; --blue:#1068B0; --violet:#2E6FA8; --magenta:#062A4F; --steel:#5B7A99;
--grad-brand:linear-gradient(100deg,#6FA8DC 0%,#4888C8 34%,#1068B0 68%,#062A4F 100%);
--grad-cyan:linear-gradient(120deg,#6FA8DC,#1068B0);
--grad-violet:linear-gradient(120deg,#4888C8,#062A4F);
--card-border:1px solid rgba(20,25,35,.10);
--dot-confidential:#C2570A; --dot-confidential-glow:rgba(194,87,10,.45);
```

### FCV — teal clínico → verde vital → dorado energía → magenta/burdeos cardio
> Derivado del logo real: el isotipo (árbol/corazón de hojas) trae **6 colores** — el más diverso
> tematizado hasta ahora (teal `#009CB4`, verde `#78B448`, dorado `#F0A830`, magenta `#E43084`,
> burdeos `#901830`, navy `#243078`, extraídos por muestreo de píxeles del PNG). En vez de usarlos
> como arcoíris plano, se narran como **"cuidado clínico → vida → energía → corazón"**: el
> `--grad-brand` recorre teal→verde→dorado→magenta; el burdeos queda como ancla oscura para el
> token `--magenta` (texto/bordes, ya de por sí muy oscuro y AA-seguro sin profundizar más); navy
> queda sin usar (reserva). Marca **mixta** (fría: teal/verde + cálida: dorado/magenta) → punto
> confidencial en **dorado** (mismo criterio que Gas País). Fondo gris claro + `--bg-wash`
> (estándar desde 2026-07-10). Usado en `presentaciones/fcv/`.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(0,156,180,.09); --bg-glow-b:rgba(228,48,132,.09);
--bg-wash:linear-gradient(135deg, rgba(0,156,180,.06) 0%, rgba(120,180,72,.05) 32%, rgba(240,168,48,.05) 66%, rgba(228,48,132,.07) 100%);
--cyan:#00707F; --blue:#4C7A2E; --violet:#8F5F08; --magenta:#901830;
--grad-brand:linear-gradient(100deg,#009CB4 0%,#78B448 36%,#F0A830 68%,#E43084 100%);
--grad-cyan:linear-gradient(120deg,#009CB4,#78B448);
--grad-violet:linear-gradient(120deg,#F0A830,#E43084);
--card-border:1px solid rgba(20,25,35,.10);
--dot-confidential:#C98A00; --dot-confidential-glow:rgba(201,138,0,.45);
```
> **Nota técnica — wordmark del cliente demasiado claro para fondo claro (nueva, 2026-08-26):**
> el logo trae un wordmark/tagline en gris neutro `#A4A7AD` que, sobre el estándar de fondo claro
> (`#F2F3F5→#FFFFFF`), medía solo **2.17:1 de contraste** (por debajo del piso AA de 3:1) — se veía
> lavado. Se oscureció **solo** los píxeles de baja saturación (`max(r,g,b)-min(r,g,b) < 20`, es
> decir el gris neutro, dejando intactas las hojas de color) multiplicando RGB × 0.66 antes de
> recortar al bbox + padding. Resultado: gris `#6C6E72`, **5.1:1 de contraste**, AA-seguro. Si otro
> logo trae un wordmark/tagline gris claro sobre este estándar de fondo, aplicar la misma
> corrección dirigida por saturación en vez de solo recortar al bbox.
> **Nota técnica — bug de ancho en texto SVG en gradiente (nueva, 2026-08-26):** al calcular el
> `viewBox` de un `<svg class="gt"><text>` (ver §5.2 de [[sistema-diseno]]), el **alto** (1083) es
> una constante de la fuente (Playfair Display Black Italic a 1000px) y es independiente del
> **ancho** — el ancho debe ser el `getBBox().width` **real** medido en el navegador, sin
> reescalarlo por la proporción alto-medido/1083. Reescalar el ancho (como se hizo por error en
> el primer intento de este deck) produce una caja más angosta que el glifo real; con
> `overflow:visible` el glifo se pinta igual pero **se monta sobre el texto siguiente en la misma
> línea** (bug visible solo cuando hay texto después del SVG en el mismo elemento — passthrough
> silencioso si el SVG es lo último antes de cerrar la etiqueta). Caso real: la lámina "Perfil del
> Desarrollador" renderizaba "Un enfoque du,ain mismo desarrollador" en vez de "Un enfoque dual,
> un mismo desarrollador". Verificar siempre exportando a PDF y leyendo el resultado, no solo el
> HTML en el navegador.

### Miami Aqua Tours — naranja del isotipo → azul aqua del wordmark/olas (tracking y optimización)
> Derivado del logo real (muestreo de píxeles del PNG): **naranja** (`#E0780A`, círculo/script "Miami")
> hacia el **azul aqua** (`#3C96C8`, texto "AQUA"/olas), con anclas `#FFA94D`→`#1B4F6E`. Narrativa de
> marca: **atardecer de Miami → océano aqua**. Es un deck nuevo (tracking/atribución/optimización del
> sitio, no la propuesta de reservas ya tematizada en `miami-aqua-tours-ampliado/` con la paleta
> cian/violeta *default* de Campuslands, previa a esta regla) — por eso deriva su propia paleta en
> vez de reutilizar la existente. Marca **mixta** (cálido: naranja + frío: azul) → el punto
> "Confidencial" se pone en **azul profundo** (mismo criterio que Multinal/Colbeef/Avicampo: el lado
> frío del par gana el acento). Fondo gris claro + `--bg-wash` (estándar desde 2026-07-10). Usado en
> `presentaciones/miami-aqua-tracking/`.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(224,120,10,.09); --bg-glow-b:rgba(45,130,180,.09);
--bg-wash:linear-gradient(135deg, rgba(255,169,77,.07) 0%, rgba(224,120,10,.05) 32%, rgba(60,150,200,.05) 66%, rgba(27,79,110,.07) 100%);
--cyan:#A85A06; --blue:#E0780A; --violet:#2C7BA6; --magenta:#1B4F6E;
--grad-brand:linear-gradient(100deg,#FFA94D 0%,#E0780A 34%,#3C96C8 68%,#1B4F6E 100%);
--grad-cyan:linear-gradient(120deg,#FFA94D,#E0780A);
--grad-violet:linear-gradient(120deg,#3C96C8,#1B4F6E);
--card-border:1px solid rgba(20,25,35,.10);
--dot-confidential:#1B4F6E; --dot-confidential-glow:rgba(27,79,110,.45);
```
> **Nota técnica — SVG en gradiente por muestreo real, no estimado (2026-09-04):** para las 10
> láminas de este deck se estimó primero el `viewBox` width de cada `<svg class="gt"><text>` por una
> heurística de píxeles/carácter (~500–535px/car a 1000px de fuente), y se confirmó visualmente en
> Chrome headless (export a PDF) que la estimación para "cinco frentes" quedó **~700px sobredimensionada**
> — el texto real terminaba antes del borde derecho del viewBox, así que el gradiente (que va de 0% a
> 100% del viewBox) solo alcanzaba a mostrarse hasta un tono intermedio, sin llegar al azul final.
> Se corrigió midiendo `getBBox().width` real de cada `<text>` en el navegador (con
> `document.fonts.ready` esperado y las láminas temporalmente visibles vía `display:block` para que
> el layout no diera 0) y reemplazando cada `viewBox` por el ancho medido exacto. Confirma la regla ya
> documentada para FCV: **nunca estimar el `viewBox` a ojo para el build final** — medir siempre en
> vivo antes de exportar a PDF, no solo para depurar un bug ya detectado.

### Alcaldía de Girón — oro brillante → oro → bronce → bronce oscuro (escudo heráldico monocromático)
> Derivado del logo real: el escudo del municipio (corona, cuarteles con castillos/leones,
> laurel) es **monocromático dorado/bronce** (`#B8903A` dominante, H≈41° por muestreo de
> píxeles) — no hay un segundo color de marca real que extraer. Se sigue el patrón ya usado en
> Marval (mono-azul): el `--grad-brand` recorre solo tonalidad/luminosidad dentro del mismo hue
> (oro brillante → bronce oscuro), sin inventar un segundo hue. Marca **cálida** (oro) → el punto
> "Confidencial" se pone en **azul institucional frío** `#0E5C8A` (regla de seguridad; también
> nace de la asociación con "gobierno/institucional", igual que el resto de acentos fríos usados
> para gobierno). Fondo gris claro + `--bg-wash` (estándar desde 2026-07-10). Primer deck con
> **shell de barra lateral retráctil** en vez del switch de escenarios en la barra superior — ver
> nota en [[sistema-diseno]] §6 y `presentaciones/giron/`. Tipografía: estándar v2 (Playfair
> Display + Montserrat + Poppins) — se probó Poppins como fuente única a pedido inicial del
> usuario, pero se revirtió minutos después a pedido del mismo usuario; ver nota abajo.
```css
--bg-0:#F2F3F5; --bg-1:#E9EBEF; --bg-2:#FFFFFF; --bg-deep:#E2E4E9;
--bg-glow-a:rgba(217,163,46,.10); --bg-glow-b:rgba(14,92,138,.08);
--bg-wash:linear-gradient(135deg, rgba(240,194,78,.07) 0%, rgba(217,163,46,.05) 32%, rgba(122,85,16,.05) 66%, rgba(74,54,8,.07) 100%);
--cyan:#8A5A0E; --blue:#A9781A; --violet:#7A5510; --magenta:#4A3608;
--grad-brand:linear-gradient(100deg,#F0C24E 0%,#D9A32E 36%,#A9781A 68%,#7A5510 100%);
--grad-cyan:linear-gradient(120deg,#F0C24E,#D9A32E);
--grad-violet:linear-gradient(120deg,#A9781A,#7A5510);
--card-border:1px solid rgba(20,25,35,.10);
--dot-confidential:#0E5C8A; --dot-confidential-glow:rgba(14,92,138,.45);
```
> **Nota de tipografía (2026-09-07, revertida el mismo día):** el usuario pidió primero cambiar a
> **Poppins como fuente única** (display + labels + cuerpo) para este deck; minutos después, tras
> ver el resultado, pidió explícitamente volver a las fuentes de siempre ("volvamos a las fuentes
> usadas en las anteriores presentaciones"). El deck final de Girón usa el **estándar v2 sin
> cambios**: Playfair Display (display, con la técnica de texto en gradiente por SVG de §5.2 de
> [[sistema-diseno]]) + Montserrat (labels/eyebrows) + Poppins (cuerpo). No se adopta ningún
> cambio de fuente por defecto a partir de este deck — quedó como un experimento descartado.
> **Nota de estructura (2026-09-07, revisada dos veces):** el usuario aclaró que **cada una de
> las 13 cotizaciones es una presentación individual y debe tener su propia portada** — el primer
> build las trataba como una sola lámina de contenido cada una, sin portada. Una segunda ronda de
> ajustes agregó además una **portada dedicada para el Resumen General** (antes el resumen y la
> portada general compartían una sola lámina): la lámina 1 es ahora una portada pura con el
> **lockup grande de logos Campuslands × Girón** (`.cover--main`, alturas desiguales — 42px vs
> 84px — porque el escudo de Girón es vertical y necesita más alto para verse con el mismo peso
> visual que el wordmark horizontal de Campuslands) y el título/kicker/meta; la lámina 2 pasa a
> ser el índice de 3 columnas (`.cover--index`, con footer en vez de meta). Estructura final:
> **28 láminas** = portada + resumen + 13 pares (portada + contenido) por cotización, navegadas
> con el **sidebar izquierdo retráctil** (una sola lista en el orden real de las láminas, sin
> subgrupos temáticos — se abandonó el agrupado por categoría porque no coincidía con el orden
> de navegación y el usuario pidió "reordenar en orden las slides") más una **barra inferior de
> prev/next + progreso** para moverse entre la portada y el contenido de una misma solución. El
> PDF exportado son 28 páginas físicas (sidebar/header/barra inferior ocultos en `@media print`,
> igual que el resto de la familia de shells).
> **Indicador de sidebar animado:** el nav-item activo ya no cambia de fondo instantáneamente —
> una pastilla (`#navIndicator`, `position:absolute` dentro de `.sidebar-nav`) se desliza hasta
> la posición del item activo vía `transform:translateY()` con `transition` (patrón ya usado en
> el `.scenario-pill` de Marval, adaptado aquí a una lista vertical en vez de un switch
> horizontal). Se recalcula en cada navegación y también al expandir/colapsar el sidebar (el
> colapso oculta las etiquetas de grupo y reacomoda los items verticalmente sin transición
> propia, así que la pastilla se reposiciona de inmediato, no con delay).
> **Sin ninguna cifra de inversión/precio** en ninguna lámina, a pedido explícito del usuario —
> el Excel fuente traía 13 cotizaciones con costeo completo por especialidad/hora, del cual solo
> se usó la jerarquía de alcance (módulo → submódulo → funcionalidad), nunca las cifras.

## 4. Aplicación

- **Decks nuevos:** derivar la paleta del logo en el paso de plan (ver [[flujo-trabajo]] y
  el CLAUDE.md raíz) y pegar el bloque de theme-tokens antes de construir.
- **Decks existentes** (Compumax, GreenMetal, Mchaileh, Miami): pueden re-tematizarse con
  su bloque de esta página cuando el usuario lo pida (cambia solo `:root` + los 3 usos de
  `--bg-deep`; el resto no se toca).
- ⛔ **Registro obligatorio (regla 2026-07-08):** cada vez que se tematiza una empresa
  (nueva o re-tematizada), su paleta **debe** quedar registrada en dos lugares: (1) el
  **catálogo** de esta página (bloque de tokens) y (2) el **demo de temas**
  `presentaciones/_temas-demo/index.html` (un tile con su gradiente y fondo). Además, la
  presentación se lista/actualiza en [[index]]. Ver también el CLAUDE.md raíz.
