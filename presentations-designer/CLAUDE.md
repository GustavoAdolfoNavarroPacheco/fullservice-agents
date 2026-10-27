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
   **Barra superior e inferior del visor con LA MISMA ALTURA** (variable `--bar-h`; plantilla: 76 px las dos). El logo de Campuslands de la barra sigue ≥ 40 px.
   **Sin líneas ni bordes — visor Y láminas (2026-10-02):** la barra superior, la barra inferior, el recuadro de la presentación y los botones del visor, **y también las tarjetas y bloques dentro de las láminas**,
   se distinguen **por sombras** (`box-shadow`), nunca con `border`/`outline` ni líneas divisorias (hairlines): sin borde fino en tarjetas, sin líneas en el pie de portada, bajo rótulos («¿Qué incluye?») ni en bloques «Partner»/«delta»
   (se sustituyen por paneles con sombra). **Permitidos:** acentos de color de ≥ 3 px (barras superiores de colores), conectores estructurales del árbol, avatar punteado y el marco neón de UN dato clave.
   **Prohibido el rótulo «Confidencial»** (ni badge, ni óvalo, ni texto). **Sin difuminación celeste** en las esquinas del fondo; el fondo de las láminas es blanco liso (las decoraciones van en los marcos, regla 5).
2. **CO-BRANDING «Campuslands × Cliente» CON IGUAL PESO VISUAL — SOLO EN PORTADA, CIERRE Y BARRA DEL VISOR.** Las **láminas de contenido NO llevan logos** (ni cabecera): el título abre la lámina.
   En la **barra superior del visor** los logos van **grandes** (Campuslands ≥ 40 px de alto; plantilla: 44 px). Campuslands **primero** de izquierda a derecha; entre ambos logos va una **«×»**
   (nunca una línea divisoria), **centrada siempre en vertical** (tolerancia 2 px). A igual altura dos logos no se ven iguales si sus proporciones difieren (Globant 5,09 : 1 vs Campuslands 4,31 : 1 con el logo vigente),
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

> Punto de partida de todo deck nuevo: **copiar `presentaciones/decks/_plantilla-campuslands/`** (ya cumple las reglas y pasa el verificador).
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
│   ├── igualar_logos.py       # factor --k-cliente: iguala el PESO VISUAL (área) de ambos logos
│   ├── colores_marca.py       # 1–3 colores de marca de un logo → campo `colors` del portal (franjas de la tarjeta)
│   └── verificar_cotizador.py # compara la lógica del Cotizador del portal con la del CRM (debe salir «idéntica»)
├── wiki/
│   ├── index.md · log.md · perfil-usuario.md · flujo-trabajo.md · despliegue.md
│   ├── marca-campuslands.md   # NORMATIVA (Brandbook): reglas, logos, color, tipografía, lenguaje gráfico
│   ├── sistema-diseno.md      # tokens, grilla, componentes, arquetipos, anti-patrones
│   ├── verificacion.md        # protocolo de verificación visual (a la vista + herramienta)
│   ├── plantilla-base.md      # biblioteca narrativa ≤10 láminas
│   ├── temas-por-cliente.md   # cliente = logo + contenido (la paleta es siempre Campuslands)
│   └── archivo/               # documentos del sistema v2 (NO usar)
├── presentaciones/      # Repo Git PROPIO (github.com/.../Presentaciones) — lo que Vercel despliega (ver despliegue.md §4). Dos carpetas separadas:
│   ├── web/             # PORTAL privado: Next.js 16 + TypeScript (login con Neon, buscador, catálogo, 404). Las presentaciones se sirven DENTRO de la web
│   │   ├── src/data/decks.ts      # ★ CATÁLOGO (antes decks.js) — TODA presentación nueva necesita su entrada (regla 3)
│   │   ├── src/app · components · lib   # rutas, componentes React/TS, sesión/BD
│   │   ├── public/portal/         # logos de marca del portal (el resto de public/ es copia de decks/, NO se versiona)
│   │   ├── scripts/               # sync-decks.ts (decks/ → public/), db-migrate.ts, create-user.ts
│   │   └── .env.example           # DATABASE_URL (Neon) y AUTH_SECRET
│   └── decks/           # LAS PRESENTACIONES (HTML/CSS/JS estático — siguen en su tecnología)
│       ├── assets/      # recursos compartidos: fuentes, favicon, logos de Campuslands y assets/logos/ (logo del cliente SIN procesar)
│       ├── _plantilla-campuslands/   # ★ PLANTILLA BASE v3 (copiar para cada deck nuevo)
│       ├── _temas-demo/ # histórico (v2); no se agregan tiles
│       └── <slug-cliente>/  # Cada presentación = subcarpeta autocontenida (slug = URL pública /<slug>): index.html, styles.css, script.js, assets/
└── recursos/            # Fuentes inmutables
    ├── brandbook/Campuslands_Brandbook.pdf
    ├── logos-campuslands/   # 4 variantes oficiales (+ recortadas, vectoriales, medidas)
    ├── fonts/               # Poppins (todos los pesos) · legado v2 · README (Nutmeg pendiente)
    └── briefs, logos de clientes, decks de referencia
```

### Reglas de carpetas
- `wiki/`, `herramientas/` y `presentaciones/` son míos para escribir; `recursos/` es solo lectura (fuente de verdad que el usuario provee).
- Cada presentación vive en `presentaciones/decks/<slug>/`, **autocontenida** (lo propio en su `assets/`; fuentes y logos compartidos en `decks/assets/`, referenciados como `../assets/…`).
- **Web y decks no se mezclan:** la tecnología nueva (Next.js/TypeScript, BD) es solo de `presentaciones/web/`; los decks siguen siendo HTML/CSS/JS puro. `web/public/` (salvo `portal/`) es una **copia generada** de `decks/` (`npm run sync:decks`): nunca se edita ni se versiona.
- **El `<slug>` es también la URL pública** (`/<slug>`): **corto y limpio** (`fcv`, `marval`). Si cambia, `git mv` + actualizar portal y wiki en el mismo cambio.

---

## Operaciones

### Construir una presentación (Build)
1. Recibo los **alcances** y datos del cliente (cuestionario en `wiki/flujo-trabajo.md`). **No invento** datos: si faltan, los pido; las cifras se citan de su fuente.
2. Leo `wiki/marca-campuslands.md`, `wiki/sistema-diseno.md`, `wiki/verificacion.md` y `wiki/plantilla-base.md`.
3. ⛔ **Plan antes de diseñar (OBLIGATORIO):** ANTES de escribir HTML/CSS le presento al usuario, **lámina por lámina** (≤ 10): contenido, arquetipo, **fondo**
   (siempre arena; qué bloques van en tarjeta navy/violeta como acento), **factor `--k-cliente`** del logo del cliente, y la **razón de ubicación** de los bloques principales.
   **NO construyo hasta que el usuario confirme.**
4. Elijo un **slug** corto, **copio `presentaciones/decks/_plantilla-campuslands/`** a `presentaciones/decks/<slug>/` y construyo el **borrador completo**: contenido, logo del cliente recortado
   al contenido exacto con el **mismo peso visual** que el de Campuslands (`igualar_logos.py` → `--k-cliente`), `totalSlides`, `<title>` y favicon.
5. 🔍 **Verifico (regla suprema 7):** `python3 herramientas/verificar_deck.py presentaciones/decks/<slug> --pdf presentaciones/decks/<slug>/<slug>.pdf --png-dir /tmp/<slug>-png` → **APROBADO**,
   y reviso **cada PNG a la vista** con la lista de `wiki/verificacion.md` §2. Corrijo y repito hasta cumplir.
6. Muestro el borrador al usuario. Iteramos ajustes; **tras cada ajuste vuelvo a verificar**.
7. Exporto a **PDF** final (ver `wiki/despliegue.md`) y entrego el archivo.
8. Registro (regla 3) y bitácora (`log.md`: lo construido, razón de ubicación de los bloques clave, avisos justificados del verificador).
   > ⛔ **Regla 3 — Registro en DOS lugares, sin excepción** (el tile de `_temas-demo` queda en desuso):
   > (a) listar/actualizar el deck en `wiki/index.md`;
   > (b) darlo de alta en el portal: UN objeto nuevo al inicio del arreglo `DECKS` de **`presentaciones/web/src/data/decks.ts`** (TypeScript tipado; el encabezado del archivo documenta cada campo:
   >     `slug`, `client` (nombre corto; mismo texto para el mismo cliente), `company`, `title`, `desc`, `category` (`ia|software|demos|institucional`), `categoryLabel`, `slides`, `investment`,
   >     `path`, `pdf`, `logo`, **`colors`**, `date` `YYYY-MM-DD`, `keywords`), más la copia del logo del cliente **sin procesar** en `presentaciones/decks/assets/logos/` (`logo: "/assets/logos/<Cliente>.png"`) y sus **colores de marca** (`python3 herramientas/colores_marca.py <logo>` → pegar en `colors`; ver «Franjas de marca» en la sección del portal).
   >     Los colores de las tarjetas los pone el portal según `category` (ya no hay `accentGrad`/`glow`/`dotColor`). Sin esto el deck funciona por su cuenta pero no aparece en el catálogo.
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
1. **Favicon = isotipo de Campuslands SIN texto** (el casco solo): `presentaciones/decks/<slug>/assets/favicon.png`, `<link rel="icon" type="image/png" href="assets/favicon.png">`.
   Maestro: `recursos/isotipo-campuslands.png` / `recursos/favicon-campuslands.png`. (La plantilla ya lo trae.)
2. **`<title>` = razón social COMPLETA del cliente**, con sufijo legal (`Compumax Computer S.A.S.`), sin descripción de la propuesta. Si el usuario no la dio, la **pido** (no la adivino).

### Mantener la wiki (Lint)
Periódicamente reviso contradicciones, información desactualizada, páginas huérfanas y convenciones que ya no usamos, y propongo mejoras. Si el usuario da una regla nueva,
la incorporo **aquí** y en la página de wiki correspondiente en el mismo cambio.

---

## Portal web (`presentaciones/web`) — diseño de waylo.ai (2026-10-27, sustituye al «Sistema de diseño web» anterior)

El **portal** (login, catálogo, 404) **no es una lámina**: replica **1:1 el diseño de `C:\Users\Full Service\dev\waylo.ai`** (fuente de verdad: `src/app/globals.css`, `src/design/`, `src/components/{auth,chat,settings,theme}`), por pedido del usuario. Las láminas y el visor de los decks **no cambian**.
- **Tokens** en `src/app/portal.css` (fuente única, mismos nombres que waylo): paleta clara `--surface #F1F1F1` · `--surface-raised #FFF` · `--text #0A0A0A` · `--text-muted #585858` y **acento celeste `--accent #28AAFB`** (reemplaza el negro de waylo en botones, etiquetas de categoría, íconos de lista, interruptor y foco; el texto sobre el acento es **blanco** por pedido del usuario, aunque da solo 2,6 : 1). **SOLO tema claro** (2026-10-27, pedido del usuario): no hay tema oscuro ni interruptor. `--danger` queda casi negro (los errores no deben ir en azul).
- **Profundidad por SOMBRAS, sin bordes**: `--shadow-soft` (reposo) · `--shadow-solid` (rellenos acento) · `--shadow-raised` (paneles/menús) · `--shadow-inset` (campos, pistas, chips) · `--shadow-pressed`. Prohibido `border`/`outline` decorativo en el portal (solo el foco visible de 3 px y los separadores `h-px` de waylo).
- **Tipografía:** **Manrope** (cuerpo) + **Poppins** (títulos, botones, etiquetas, 500–600). Sin cursiva/Pacifico (excluida por el usuario). Radios 12/16/20/28; espaciado base 4 px en pasos de 8.
- **Movimiento:** `--duration-fast/base/slow/theme` = 220/420/700/1100 ms, `--ease-standard` (0.22,1,0.36,1), `--ease-emphasis` solo para el tema y los checks. Hover único = clase **`lift`** (sube 3 px + sombra elevada por opacidad de `::after`, se hunde al pulsar; solo en `hover:hover`). Solo `transform`/`opacity`; `prefers-reduced-motion` pone las duraciones en 0. Scroll con inercia **Lenis** (`smooth-scroll.tsx`; las áreas con scroll propio —menús, listas, diálogos— llevan `data-lenis-prevent` y **también se deslizan con inercia** gracias a un oyente de rueda delegado en ese mismo archivo, sin tocar cada componente; al llegar al extremo no interceptan). **No poner `data-lenis-prevent` en contenedores que solo desplazan en horizontal** (p. ej. la tabla del Cotizador): taparía el scroll suave de la página justo encima de ellos.
- **Fondo con profundidad (2026-10-27):** el fondo del portal NO es plano: degradado vertical muy suave (`#F7F8F9 → --surface → #ECECED`) + dos resplandores celestes de marca (`--accent` al 15 % arriba-izquierda y 10 % arriba-derecha) + sombra tenue abajo; `background-attachment: fixed` para que las tarjetas «floten». Es solo del `body` (login y 404 lo heredan); campos, pistas y controles siguen usando `--surface` liso.
- **Controles:** botones 48 px (`.btn`, `--sm` 44), cuadrados `.tbtn` de 48 px, campos hundidos de 44 px con halo de foco; menús = superficie elevada `rounded-xl` con animación `popover-in`; opciones múltiples = pista hundida + píldora elevada que se desliza.
- **Tarjeta del catálogo (2026-10-27):** orden de lectura logo (88 px, baldosa blanca) + fecha en una línea con ícono → cliente, título (19 px; 18 en lista) y etiquetas (categoría en celeste suave con texto azul oscuro, para no competir con el botón «Web»; y láminas). **Sin botones de acción (2026-10-27, pedido del usuario): ni Web, ni PDF, ni copiar enlace** — viven en la ficha del proyecto; la tarjeta entera (clic en cualquier parte) abre la ficha. **Sin descripción ni precio** (pedido del usuario; el buscador sí indexa ambos). **PDF en rojo** (`--pdf #D92D20`, ícono y texto); Web en el acento. En lista ancha las columnas se alinean con `subgrid`: desde 840 px de contenido (logo · texto) y desde 1000 px también la fecha.
- ⛔ **Franjas de marca en la tarjeta (regla del usuario, 2026-10-27 — aplica a TODAS las tarjetas):** cada tarjeta lleva, **detrás del contenido**, de arriba abajo, **1–3 franjas verticales con los colores de marca del cliente** (campo `colors` de `decks.ts`, de izquierda a derecha; los toma de **su logo** con `herramientas/colores_marca.py`, o de su propio estilo si no hay logo). Medidas de la demostración del usuario: **24 px de ancho, 20 px entre sí, a 30 px del borde derecho**, en **tinte suave** (30 % del color sobre blanco) **planas, sin sombras** (solo el color con su opacidad baja; el usuario probó sombra interior y la descartó); el contenido (fecha, etiquetas, botones, texto) va por encima. En lista ancha se reservan 150 px a la derecha de la fila para que las franjas no tapen el texto ni la fecha. **Todo deck nuevo debe traer su `colors`** (sin él el portal falla al compilar: el campo es obligatorio en `Deck`). Los colores son del **cliente** (identidad), el resto del diseño sigue siendo del portal. Colores curados: Campuslands = celeste `#2CAAFF` + azul de marca `#000087`; Ve a la Segura (sin logo) = su paleta `#E14FD1`/`#9B5DE5`.
- **Perfil de proyecto (2026-10-27, paso 1 de una implementación mayor por etapas):** al hacer clic en una tarjeta (título o toda la tarjeta) NO se abre la presentación sino su **ficha** `/proyecto/<slug>/` (`src/app/proyecto/[slug]/page.tsx`; **privada**, el `proxy.ts` la protege como `/`). La ficha lleva: barra con «Volver» (conserva filtros y vista del catálogo), cabecera compacta con logo grande + franjas de marca + título + etiquetas (relleno 24/32 px, separación 16 px), las **acciones como botones circulares 1×1 (48 px) abajo a la derecha del banner** (Abrir presentación/demo · Ver PDF en rojo · Copiar enlace · **Excel**, este último **sin funcionalidad por ahora**), con tooltip por `data-tip`; en pantallas ≤ 900 px pasan a una fila bajo las etiquetas, «Más de <cliente>», y un botón **«info»** en la esquina superior derecha de la cabecera que, **al pasar el ratón** (o al tocarlo/activarlo con teclado), despliega el panel **Detalles** (cliente, razón social, categoría, fecha, contenido, archivos; se cierra al salir, con Esc o al pulsar fuera). **Sin resumen en la ficha** y **sin vista previa** de la presentación (el usuario las descartó). Los botones Web/PDF de la tarjeta siguen abriendo el archivo directo. **No muestra inversión** (el usuario la quitó de las tarjetas); el dato sigue en `decks.ts`. Un deck nuevo obtiene su ficha solo, al registrarlo en `decks.ts`.
- ⛔ **COTIZADOR (copia del CRM, 2026-10-27) — debajo del banner de cada ficha.** Es una copia **fiel** de la fase «Cotización» de `crm-campuslands/crm/crm-frontend` (`/fullservice/proyectos/{id}/seguimiento`): Cotizador (estado, unidad días/horas, margen, tabla de costos por perfil con módulos y subtareas, totales, precio sugerido, Exportar PDF, Parámetros) y Tabla de tiempos por meses. **La sección «Observaciones y notas» se quitó de la interfaz a pedido del usuario (2026-10-27)**: el dato sigue en la base y en el PDF si ya existía, pero ya no se edita. **Regla: la LÓGICA no se toca; solo se rehace lo visual.** Archivos: `src/lib/cotizador/` (`formato.ts`, `parametros.ts`, `pdf.ts`, `tipos.ts`, `validacion.ts` = copias del CRM; `servidor.ts`/`validar.ts` = persistencia y comprobación en Neon, código nuevo) y `src/components/cotizador/` (`cotizador.tsx` = `FaseCotizacion.tsx`, `parametros-dialog.tsx`, `currency-input.tsx`, `modal.tsx`). **Si el CRM cambia su cotizador, se vuelve a copiar** y se corre `python3 herramientas/verificar_cotizador.py` (compara la lógica línea a línea con el CRM: debe decir «idéntica») y `npm test` en `web/` (60 pruebas: las 24 originales del CRM sin cambios + las del componente y el diálogo). Diferencias PERMITIDAS y documentadas: (1) la interfaz (sistema de diseño del portal); (2) los datos viven en **Neon** (tablas `cotizaciones` —una por slug— y `parametros_cotizacion` —registro `vigente`—; `npm run db:migrate`) en vez de Firestore, con la misma forma (`cotizacion`, `margenCotizacion`, `observacionesCotizacion`, `estadoCotizacion`) y guardado por acción de servidor con comprobación extra de datos; (3) **sin roles**: `canModify = isCotizador = true` para toda persona con sesión (decisión del usuario), así que se ven «Parámetros» y todos los estados; (4) los Parámetros se leen al abrir la página (en el CRM, suscripción en vivo) y se aplican al guardarlos; (5) el PDF carga `public/portal/logo-cotizacion.png` (el logo del CRM) y se importa solo al exportar. **Manías del CRM conservadas a propósito** (no «corregir» sin decidirlo con el usuario): un margen guardado en 0 se reabre como 40 (`|| 40`); en el modal de exportar, un clic en el TEXTO del nombre de un módulo no cambia la selección (se anula con el clic reenviado al cuadro; sí funciona clicar el cuadro o la tarjeta); dos clics en celdas de mes en el mismo instante solo guardan el último.
- **CREAR PROYECTO (2026-10-27) — página `/nuevo-proyecto/` (privada, no ventana emergente):** el botón **1×1 celeste** (`.tbtn--accent`, ícono carpeta+; es un enlace) a la izquierda de «Ordenar» lleva a ella. **Izquierda: «Vista previa»** de la tarjeta del catálogo (mismas clases, se actualiza al escribir; textos largos sin espacios se parten, nunca se salen) con el **logo editable al hacer clic en él**, como el avatar de un perfil (cámara encima; papelera para quitarlo), y **debajo los «Colores de marca»** (máx. 3 fichas + «+»): al elegir o agregar una se abre **una ventana emergente** con el selector (cuadro de saturación/brillo + matiz, valores **RGB o HSL**, **hexagonal**), **Cuentagotas** (API `EyeDropper`, solo si existe) y **Cargar imagen** / «Usar el logo» (imagen temporal, **nunca se guarda**); esa ventana **cabe sin desplazarse** (selector | valores | imagen en una fila; ~510 px de alto). **Derecha: formulario** con título «Crear proyecto» grande y asteriscos **rojos** (`--pdf`; el `--danger` del portal es casi negro): Cliente, Razón social y Título (con *placeholders*), Categoría y **Fecha**: el interruptor **«Automática»** (día del registro **en hora de Colombia**, calculado en el servidor) va **separado**, en la línea de la etiqueta, y debajo el campo de fecha con su **calendario propio** (`components/date-picker.tsx`, el del navegador no se puede diseñar: mes y año en menús, semanas desde el lunes, abre hacia arriba si no cabe, teclado completo —flechas, Re Pág/Av Pág, Inicio/Fin, Enter, Esc—; no usar `<input type="date">` en el portal). Los **campos de esta página son blancos** (`--surface-raised` con sombra hundida). Al crear lleva a la **ficha** del proyecto nuevo (ahí se cotiza). Los proyectos viven en la tabla `proyectos` de Neon (logo reducido ≤ 320 px / ≤ ~200 KB como data URL, colores `#RRGGBB`, `created_by`), se suman a `decks.ts` con `buildCatalog(creados)` y sin presentación todavía (`path`/`pdf` vacíos): su ficha oculta Abrir/PDF/Copiar enlace y deja Excel + el Cotizador. Todo se valida de nuevo en el servidor (`lib/proyectos/validar.ts`, `app/proyectos/actions.ts`); el slug sale del título y es único (`-2`, `-3`…; nunca una ruta reservada ni un deck del código). Cualquier persona con sesión puede crear. **Aún no hay** editar ni borrar proyectos creados.
- **Panel de filtros (2026-10-27):** un solo grupo a la vez en pestañas (Categoría · Cliente · Fecha) con píldora deslizante y un punto en la pestaña que tenga filtro activo; celdas iguales en 2 columnas (la última impar ocupa todo el ancho); Cliente = buscador + lista con **su propio** scroll dentro de un marco hundido (`scrollbar-gutter: stable both-edges`). Sin botón de pie (se cierra con clic fuera o Esc); la pista es siempre de 2 columnas (una opción impar NO se estira); espacio igual sobre y bajo el buscador (16 px); el scroll de Cliente vive en un contenedor interior (barra fina dentro del marco). Los **filtros activos** son píldoras a la derecha del botón «Filtros», en el mismo renglón. **Animación al filtrar y al cambiar de vista (reglas de fluidez, 2026-10-27):** las tarjetas que quedan se deslizan (FLIP, 800 ms), las que salen se desvanecen en su sitio (copia en una capa propia con el diseño de la vista de origen), las nuevas suben suave, y al cambiar cuadrícula ⇄ lista cada tarjeta se **transforma** en su fila (`translate`+`scale`, contenido nuevo entra al 40 %). Para que NO se sienta «arranca, frena y arranca»: (1) **sin retrasos escalonados** con la tarjeta ya desplazada; (2) curva `cubic-bezier(.3,.2,.15,1)` (arranque inmediato, frenado largo; nunca un inicio casi quieto); (3) el trabajo pesado (clonar tarjetas) se hace **en reposo**, no en el clic; (4) solo se animan las tarjetas que se ven (±240 px); (5) el efecto no se repite si los datos no cambian; (6) `will-change: transform` solo durante el movimiento; posiciones con `offsetLeft/Top`.
- **Logo:** celeste (#2CAAFF) provisto por el usuario, `public/portal/logo-campuslands-horizontal.png` (barras y cabeceras; **recompuesto a pedido del usuario**: casco al 75 % y letras al 150 % → 5,12 : 1; alto en barra 38 px) y `-vertical.png` (marca del login y 404), vía `BrandLogo`; nunca se deforma. Los logos de clientes siempre sobre tile blanco.
- ⛔ **ÍCONOS: todos salen de AnimateIcons (Lucide)** — <https://animateicons.in/icons/lucide>, paquete `@animateicons/react/lucide`. Se envuelven en `src/components/icons.tsx`; no se dibujan SVG propios. Los SVG de los íconos llevan `overflow: visible` (si no, al animarse —eslabones que se separan, flechas que salen— se recortan a los lados). Única excepción: el logotipo «G» de Google (marca, no existe en Lucide; se pinta en un solo tono como en waylo).
- **Verificación del portal:** `npx tsc --noEmit` + revisión a la vista en claro y oscuro a 375/768/1024/1280/1440 px (vista grilla y lista) y auditoría de solapes, desbordes, simetría de márgenes, **centrado de cada ícono** (desvío ≤ 0,5 px), **texto recortado** y ancho mínimo del texto en la lista, barriendo el ancho del contenedor (420→1264 px). Sin celdas desalineadas: la lista usa `subgrid`; sus cortes de diseño son `@container page` (espacio real), no `@media`. Los SVG son `display:block` (si no, dejan holgura de línea y el ícono queda ~3 px arriba). Las etiquetas envuelven, nunca se recortan.

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
