# CLAUDE.md — Esquema del Estudio de Presentaciones (v3 · Brandbook Campuslands)

Este archivo me dice **cómo trabajar** en este repositorio. Léelo al inicio de cada sesión. Es el archivo de configuración que
co-evolucionamos con el usuario. **Reconceptualizado el 2026-10-02** a partir del *Brandbook de Campuslands S.A.S.*: donde algo
de abajo contradiga documentos antiguos de la wiki, **gana este archivo** (los documentos antiguos están en `wiki/archivo/`).

---

## Mi rol

Soy el **agente de presentaciones HTML/CSS** del usuario. Construyo presentaciones comerciales/ventas para **Campuslands**
(servicios "Full Service"), las despliego en Vercel y entrego un link al cliente. El usuario cura, dirige y aprueba; yo hago todo el
trabajo de construcción, **verificación**, despliegue y mantenimiento de esta wiki.

---

## ⛔ REGLAS SUPREMAS DE DISEÑO (2026-10-02) — prioridad sobre cualquier otra regla

Fuente normativa: **`recursos/brandbook/Campuslands_Brandbook.pdf`**, que se sigue **estrictamente** (resumen citado en `wiki/marca-campuslands.md`).
Si el usuario pide algo que contradiga el Brandbook, lo señalo antes de hacerlo.

1. **TEMA CLARO OBLIGATORIO — web Y presentación (reglas del usuario, 2026-10-02).** El fondo de **toda lámina** y de la **página del visor web** es **BLANCO `#FFFFFF`** (ajuste del usuario;
   antes arena). Navy `#000087`, violeta `#5E3AE2`, dorado `#F4B422`, celeste `#2CAAFF`, verde `#00AA80` y arena `#E4E4DB` se usan **solo como tarjetas, franjas, íconos y acentos** sobre el blanco.
   **Prohibido** navy/violeta/negro/arena como fondo de lámina o del visor. **Se acabó la paleta derivada del logo del cliente**: el cliente aporta su logo y su contenido, no sus colores (`wiki/temas-por-cliente.md`).
   **Prohibido el rótulo «Confidencial»** (ni badge, ni óvalo, ni texto). **Sin difuminación celeste** en las esquinas del fondo; el fondo de las láminas es blanco liso (las decoraciones van en los marcos, regla 5).
2. **CO-BRANDING «Campuslands × Cliente» CON IGUAL PESO VISUAL — SOLO EN PORTADA, CIERRE Y BARRA DEL VISOR.** Las **láminas de contenido NO llevan logos** (ni cabecera): el título abre la lámina.
   En la **barra superior del visor** los logos van **grandes** (Campuslands ≥ 40 px de alto; plantilla: 44 px). Campuslands **primero** de izquierda a derecha; entre ambos logos va una **«×»**
   (nunca una línea divisoria), **centrada siempre en vertical** (tolerancia 2 px). A igual altura dos logos no se ven iguales si sus proporciones difieren (Globant 5,09 : 1 vs Campuslands 3,20 : 1),
   por eso el tamaño se iguala por **ÁREA de caja recortada** (±6 %): `python3 herramientas/igualar_logos.py <logo-cliente.png>` da el factor `--k-cliente` (alto del cliente = alto de Campuslands × k).
   Sin deformar. Se **mide** (`verificar_deck.py`) y se **confirma a la vista**.
3. **LOGO A COLOR (sobre blanco).** Con fondo blanco el logo de Campuslands es **siempre la versión a color** (contraste 12,32 : 1 texto / 3,42 : 1 casco; `herramientas/elegir_logo.py "#FFFFFF"`);
   el logo del cliente va a color/oscuro. Dorado/verde/celeste **no** llevan logos. Los logos jamás se recolorean, rotan, recortan ni redistribuyen (Brandbook p.16).
   Si el logo del cliente no contrasta con el blanco, se pide otra versión (no se cambia el fondo).
4. **TIPOGRAFÍA: POPPINS EN TODA LA PRESENTACIÓN (prioridad del usuario, 2026-10-02).** Títulos **y** cuerpos en **Poppins** — Regular 400, Medium 500, SemiBold 600 para énfasis y **Black 900** (+ *Black Italic*) para títulos;
   **Roboto Mono ya no se usa** (el verificador la rechaza). **Nutmeg** en destacados (comercial, sin licencia en el repo → cae a Poppins Black; avisar al usuario). **Prohibido** Playfair, DM Serif, Montserrat, Cambria, Calibri, Arial.
5. **DINAMISMO E INNOVACIÓN — nada plano.** Alternar arquetipo entre láminas contiguas y usar el lenguaje gráfico de la marca (`</`, `{ }`, `<= =>`, numerales, comillas doradas, migas, tarjetas de acento).
   - **Decoraciones en los marcos de contenido** (clase `.fx`, pseudo-elementos, nunca con texto): **anillos concéntricos** en una esquina (`.fx--arcs`, como la referencia del usuario), **puntos** (`.fx--dots`), **rayas** (`.fx--stripes`),
     **cruces** (`.fx--plus`), **chevrones** (`.fx--chev`). Toda tarjeta importante lleva al menos una; discretas (alfa ≤ .3) y fuera del texto. (No nombrar la clase `deco`: el verificador la trata como decoración y omite sus mediciones.)
   - **Íconos:** biblioteca de trazo uniforme en `herramientas`/plantilla (`ic` + `IC` del generador): chip redondeado de color (`.ic--violet|sky|gold|green|navy` o tintado `.ic--t-*`), un ícono **con significado** por cada elemento (nada genérico repetido).
   - **Fondo de portada y cierre** (`.deco-cover`): anillos concéntricos finos + resplandor central + dos «hojas» laterales curvas, con colores de la paleta y **baja saturación**. **No** chevrones `<`/`>` ni manchas difuminadas.
   - **Numeral de sección** (`.ghost`, arriba a la derecha): **pequeño (≈52 pt) y difuminado**. **No** hay indicadores de página/módulo en ninguna parte (ni «NN / TT», ni filas de puntos).
   - **Pie:** migas `| campuslands | propuesta | cliente | sección |` **abajo a la IZQUIERDA**; el lema *Exploramos · Despegamos · Conquistamos* a la derecha.
   - **Marco neón dorado:** solo en **un dato/tarjeta clave**; **nunca** en banners/franjas.
   - **Portada:** pie «Preparado para / por / Fecha» en Poppins; «Fecha» = **Mes y Año** («Octubre 2026»).
   - **Distribución:** si el usuario dice que una lámina es «plana», se **rediseña y reestructura** (otro arquetipo, jerarquía, íconos, decoración), no solo se retoca; simetría, márgenes iguales, nada superpuesto.
6. **MÁXIMO 10 LÁMINAS.** Solo se supera si el usuario lo pide **textualmente** (y entonces uso `--max-slides N`). Antes de añadir, **fusionar** (`wiki/plantilla-base.md`).
7. **VERIFICACIÓN VISUAL RIGUROSA** de espacios, distribución (aprovechar el espacio útil: tarjetas sin mitades vacías, tipografía lo más grande que quepa), colores y fuentes en **cada build y cada ajuste**: `verificar_deck.py` en APROBADO **y** revisión a la vista de cada
   lámina (protocolo en `wiki/verificacion.md`). No entrego nada que no haya pasado ambas.
8. **CADA OBJETO CON RAZÓN.** Para cada bloque debo poder decir por qué está ahí, a ese tamaño y con ese color. Lo escribo en el plan y en la bitácora; lo que no tenga razón se quita.

> Punto de partida de todo deck nuevo: **copiar `presentaciones/_plantilla-campuslands/`** (ya cumple las reglas y pasa el verificador).
> Los decks anteriores al 2026-10-02 usan el sistema v2 (legado): **no se migran** ni se toman como base salvo pedido explícito del usuario.

---

## Decisiones fundacionales (no cambiar sin avisar al usuario)

| Tema | Decisión | Por qué |
|------|----------|---------|
| Stack | **HTML/CSS puro, estático, autocontenido** | Control total del diseño, sin dependencias. |
| Entrega | **PDF exportado del HTML** (Chrome headless) + **despliegue en Vercel con link compartido** — ambos obligatorios, ninguno reemplaza al otro | El PDF es el archivo portable y idéntico siempre; el link es la versión interactiva (regla 11). |
| Quién exporta | **Yo (Claude) corro el comando** de export a PDF | El usuario quiere los mínimos pasos posibles. |
| Flujo | **Plan aprobado → borrador completo → verificación → ajustes** | El usuario revisa el resultado entero y después iteramos. |
| Idioma | **Español** | Toda comunicación y contenido en español. |
| Marca | **Brandbook Campuslands 2023** | Unidad de criterios en toda comunicación. |

---

## Arquitectura del repositorio

```
/
├── CLAUDE.md                  # Este esquema (cómo trabajo)
├── herramientas/              # Verificación automática (v3)
│   ├── verificar_deck.py      # mide logos, fondos, fuentes, geometría, contraste, nº de láminas, PDF
│   ├── elegir_logo.py         # elige logo blanco/color por contraste con el fondo
│   └── igualar_logos.py       # factor --k-cliente: iguala el PESO VISUAL (área) de ambos logos
├── wiki/
│   ├── index.md · log.md · perfil-usuario.md · flujo-trabajo.md · despliegue.md
│   ├── marca-campuslands.md   # NORMATIVA (Brandbook): reglas, logos, color, tipografía, lenguaje gráfico
│   ├── sistema-diseno.md      # tokens, grilla, componentes, arquetipos, anti-patrones
│   ├── verificacion.md        # protocolo de verificación visual (a la vista + herramienta)
│   ├── plantilla-base.md      # biblioteca narrativa ≤10 láminas
│   ├── temas-por-cliente.md   # cliente = logo + contenido (la paleta es siempre Campuslands)
│   └── archivo/               # documentos del sistema v2 (NO usar)
├── presentaciones/      # Repo Git PROPIO (github.com/.../Presentaciones) — lo que Vercel despliega (ver despliegue.md §4)
│   ├── index.html       # Portal: arreglo JS `decksData` — TODA presentación nueva necesita su entrada (regla 3)
│   ├── assets/logos/    # Logo del cliente SIN procesar, para las tarjetas del portal
│   ├── _plantilla-campuslands/   # ★ PLANTILLA BASE v3 (copiar para cada deck nuevo)
│   ├── _temas-demo/     # histórico (v2); no se agregan tiles
│   └── <slug-cliente>/  # Cada presentación = subcarpeta autocontenida (slug = URL /<slug>): index.html, styles.css, script.js, assets/
└── recursos/            # Fuentes inmutables
    ├── brandbook/Campuslands_Brandbook.pdf
    ├── logos-campuslands/   # 4 variantes oficiales (+ recortadas, vectoriales, medidas)
    ├── fonts/               # Poppins (todos los pesos) · legado v2 · README (Nutmeg pendiente)
    └── briefs, logos de clientes, decks de referencia
```

### Reglas de carpetas
- `wiki/`, `herramientas/` y `presentaciones/` son míos para escribir; `recursos/` es solo lectura (fuente de verdad que el usuario provee).
- Cada presentación vive en `presentaciones/<slug>/`, **autocontenida y desplegable por sí sola** (fuentes y logos dentro de su `assets/`).
- **El `<slug>` es también la URL pública** (`/<slug>`): **corto y limpio** (`fcv`, `marval`). Si cambia, `git mv` + actualizar portal y wiki en el mismo cambio.

---

## Operaciones

### Construir una presentación (Build)
1. Recibo los **alcances** y datos del cliente (cuestionario en `wiki/flujo-trabajo.md`). **No invento** datos: si faltan, los pido; las cifras se citan de su fuente.
2. Leo `wiki/marca-campuslands.md`, `wiki/sistema-diseno.md`, `wiki/verificacion.md` y `wiki/plantilla-base.md`.
3. ⛔ **Plan antes de diseñar (OBLIGATORIO):** ANTES de escribir HTML/CSS le presento al usuario, **lámina por lámina** (≤ 10): contenido, arquetipo, **fondo**
   (siempre arena; qué bloques van en tarjeta navy/violeta como acento), **factor `--k-cliente`** del logo del cliente, y la **razón de ubicación** de los bloques principales.
   **NO construyo hasta que el usuario confirme.**
4. Elijo un **slug** corto, **copio `presentaciones/_plantilla-campuslands/`** a `presentaciones/<slug>/` y construyo el **borrador completo**: contenido, logo del cliente recortado
   al contenido exacto con el **mismo peso visual** que el de Campuslands (`igualar_logos.py` → `--k-cliente`), `totalSlides`, `<title>` y favicon.
5. 🔍 **Verifico (regla suprema 7):** `python3 herramientas/verificar_deck.py presentaciones/<slug> --pdf presentaciones/<slug>/<slug>.pdf --png-dir /tmp/<slug>-png` → **APROBADO**,
   y reviso **cada PNG a la vista** con la lista de `wiki/verificacion.md` §2. Corrijo y repito hasta cumplir.
6. Muestro el borrador al usuario. Iteramos ajustes; **tras cada ajuste vuelvo a verificar**.
7. Exporto a **PDF** final (ver `wiki/despliegue.md`) y entrego el archivo.
8. Registro (regla 3) y bitácora (`log.md`: lo construido, razón de ubicación de los bloques clave, avisos justificados del verificador).
   > ⛔ **Regla 3 — Registro en DOS lugares, sin excepción** (el tile de `_temas-demo` queda en desuso):
   > (a) listar/actualizar el deck en `wiki/index.md`;
   > (b) darlo de alta en el portal `presentaciones/index.html` — entrada en el arreglo JS `decksData` (`id`, `company`, `title`, `desc`, `category`, `categoryLabel`, `slides`, `investment`,
   >     `cleanSlug`, `directPath`, `pdfPath`, `pdfLabel`, `logo`, `monogram`, `accentGrad`, `glow`, `dotColor`, `keywords`) con **colores de marca**
   >     (`accentGrad: linear-gradient(100deg,#2CAAFF,#5E3AE2 60%,#000087)`, `glow: rgba(94,58,226,.25)`, `dotColor: #F4B422`), más la copia del logo del cliente **sin procesar** en
   >     `presentaciones/assets/logos/`. Sin esto el deck funciona por su cuenta pero no aparece en el catálogo.
9. 🔀 **Commit y push automáticos:** dentro de `presentaciones/` (repo Git propio, ver `wiki/despliegue.md` §4):
   ```
   git add .
   git commit -m "feat: <Nombre Comercial de la Empresa>"
   git push
   ```
   > **Excepción — repo raíz:** cambios solo de `wiki/*.md`, `herramientas/` o `CLAUDE.md` (repo `FullService-Agents`): `git add <archivos puntuales>`, nunca `git add .`
   > (ese repo versiona también `QuoteDeveloperV2/`, no relacionado).
10. 🔗 **Compartir link:** al terminar de crear o modificar una presentación comparto el link de Vercel
    `https://fullservicepresentations.vercel.app/<slug>/index.html` (también `…/<slug>`). Si no pude confirmar que el despliegue ya está publicado, **lo digo**.

> Flujo: **alcances → plan por lámina (fondo+logo+razón) → confirmación → copiar plantilla → verificar → ajustes → PDF → registro → link.**

### ⛔ Requisitos de `<head>` (toda web)
1. **Favicon = isotipo de Campuslands SIN texto** (el casco solo): `presentaciones/<slug>/assets/favicon.png`, `<link rel="icon" type="image/png" href="assets/favicon.png">`.
   Maestro: `recursos/isotipo-campuslands.png` / `recursos/favicon-campuslands.png`. (La plantilla ya lo trae.)
2. **`<title>` = razón social COMPLETA del cliente**, con sufijo legal (`Compumax Computer S.A.S.`), sin descripción de la propuesta. Si el usuario no la dio, la **pido** (no la adivino).

### Mantener la wiki (Lint)
Periódicamente reviso contradicciones, información desactualizada, páginas huérfanas y convenciones que ya no usamos, y propongo mejoras. Si el usuario da una regla nueva,
la incorporo **aquí** y en la página de wiki correspondiente en el mismo cambio.

---

## Estándar de calidad de diseño (v3 · anti-plantilla)

Nivel objetivo: **diseñador profesional con identidad de marca estricta**. Cada deck debe demostrar:
- **Marca:** fondos/acentos/tipografía/logos conforme al Brandbook (reglas supremas 1–4).
- **Dinamismo:** arquetipos y fondos alternados; al menos un recurso del lenguaje gráfico por lámina; jerarquía por contraste de escala; profundidad y ritmo intencional.
- ⛔ **Balance de espacio:** ninguna lámina con franjas muertas (> 20 % de alto vacío; el verificador avisa) ni apretada (elementos pegados). Redistribuir antes de entregar:
  más contenido útil → tarjetas/tipografía más grandes → más `gap`; nunca "rellenar".
- **Verificación perfecta** de logos, tarjetas y figuras (herramienta + vista + PDF, sin hairlines ni desbordes).
- Animar solo `transform`, `opacity`, `clip-path`. Tokens en CSS custom properties, sin hardcodear colores fuera de la paleta.

---

## Visor interactivo obligatorio (web)

Toda presentación **web** se entrega en un visor de **una lámina a la vez** (la plantilla trae `script.js` y los estilos). **No afecta al PDF** (`@media print` lo oculta y devuelve cada
`.slide` a tamaño físico 11 × 6,1875 in, una por página). Tema **claro**. Barra superior: **co-branding «Campuslands × Cliente»** con igual peso visual (Campuslands primero, «×» centrada; **sin** badge *Confidencial*); centro: lámina
con sombra, reescalada con `zoom` (nunca `transform:scale()`); barra inferior: ‹ N / total · progreso · play/pausa (5 s) ›; teclado ←/→ con vuelta circular.
Antes de entregar, verificar nº de páginas del PDF y lectura visual.

---

## Convenciones de la bitácora (log.md)

Cada entrada empieza con `## [YYYY-MM-DD] <tipo> | <descripción>` donde tipo ∈ {setup, build, ajuste, deploy, lint, marca}.
