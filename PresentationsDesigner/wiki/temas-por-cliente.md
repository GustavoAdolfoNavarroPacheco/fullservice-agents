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
