# CLAUDE.md — Esquema del Estudio de Presentaciones

Este archivo me dice **cómo trabajar** en este repositorio. Léelo al inicio de cada
sesión. Es el archivo de configuración que co-evolucionamos con el usuario.

---

## Mi rol

Soy el **agente de presentaciones HTML/CSS** del usuario. Construyo presentaciones
comerciales/ventas para **Campuslands** (servicios "Full Service"), las despliego en
Vercel y entrego un link al cliente. El usuario cura, dirige y aprueba; yo hago todo
el trabajo de construcción, despliegue y mantenimiento de esta wiki.

---

## Decisiones fundacionales (no cambiar sin avisar al usuario)

| Tema | Decisión | Por qué |
|------|----------|---------|
| Stack | **HTML/CSS puro, estático, autocontenido** | Control total del diseño, sin dependencias. |
| Entrega | **PDF exportado del HTML** (Chrome headless) + **despliegue en Vercel con link compartido** — ambos son obligatorios en toda presentación, ninguno reemplaza al otro | El PDF es el archivo portable que recibe el cliente (idéntico siempre, offline, imprimible). El link de Vercel es la versión interactiva que se comparte en el chat al terminar cada build/ajuste (ver regla 10 más abajo). |
| Quién exporta | **Yo (Claude) corro el comando** de export a PDF | El usuario quiere los mínimos pasos posibles. |
| Flujo | **Borrador completo → luego ajustes** | El usuario revisa el resultado entero y después iteramos. |
| Idioma | **Español** | Toda comunicación y contenido en español. |

---

## Arquitectura del repositorio

```
/
├── CLAUDE.md                  # Este esquema (cómo trabajo)
├── wiki/                      # Conocimiento que YO mantengo (el usuario lee, yo escribo)
│   ├── index.md               # Catálogo de toda la wiki
│   ├── log.md                 # Bitácora cronológica (append-only)
│   ├── perfil-usuario.md
│   ├── flujo-trabajo.md
│   ├── despliegue.md
│   ├── marca-campuslands.md   # Colores, tipografías, logo, tono
│   ├── sistema-diseno.md      # Tokens CSS, componentes, convenciones
│   └── plantilla-base.md      # Análisis de la estructura base del usuario
├── presentaciones/      # Repo Git PROPIO y distinto del raíz (github.com/.../Presentaciones)
│   │                    # — es la carpeta que Vercel despliega. Detalle completo de esta
│   │                    # arquitectura (2 repos Git anidados + auto-commit) en despliegue.md §4.
│   ├── index.html       # Portal principal: catálogo con login/buscador/filtros. Arreglo JS
│   │                    # `decksData` — TODA presentación nueva necesita su entrada aquí (ver
│   │                    # Regla 3 más abajo), o no aparece en el catálogo aunque funcione sola.
│   ├── assets/logos/    # Copia SIN procesar del logo de cada cliente (recursos/<Cliente>.png)
│   │                    # para las tarjetas del portal — distinta del logo recortado del deck.
│   ├── _temas-demo/     # Catálogo visual de paletas por cliente
│   └── <slug-cliente>/  # Cada presentación = una subcarpeta autocontenida (slug = URL /<slug>)
│       ├── index.html
│       ├── styles.css
│       └── assets/
└── recursos/            # Fuentes inmutables: logos, briefs, decks de referencia
```

### Reglas de carpetas
- `wiki/` y `presentaciones/` son míos para escribir; `recursos/` es solo lectura
  (fuente de verdad que el usuario provee).
- Cada presentación vive en `presentaciones/<slug>/` y es **autocontenida y
  desplegable por sí sola**.
- **El `<slug>` es también la URL pública** (`/<slug>`, resuelta por Vercel sin rewrite si el
  nombre de carpeta coincide exacto con el `cleanSlug` del portal) — elegirlo **corto y limpio**
  desde el plan inicial (ej. `fcv`, `marval`), no una frase larga. Si cambia después, renombrar
  con `git mv` (no copiar) y actualizar el portal + `wiki/*.md` en el mismo cambio.

---

## Operaciones

### Construir una presentación (Build)
1. Recibo los **alcances** del proyecto + datos del cliente.
2. Leo `wiki/marca-campuslands.md`, `wiki/sistema-diseno.md`, `wiki/plantilla-base.md` y `wiki/temas-por-cliente.md`.
3. 🎨 **REGLA OBLIGATORIA — Paleta por cliente:** derivo la paleta del deck (**fondo gris claro
   frío + gradiente de marca incluidos**) del **logo del cliente**, siguiendo la receta y el
   contrato de tokens de `wiki/temas-por-cliente.md`. Cada empresa debe verse distinta; el
   naranja/índigo de Multinal es solo la referencia de la receta, no un color fijo. La incluyo
   en el plan del paso 4.
   > **Regla 2 (2026-07-10, reemplaza la de 2026-07-08):** el **fondo estándar de toda
   > presentación nueva es gris claro neutro y frío** (`--bg-0/1/2/deep` en la gama `#E2E4E9` →
   > `#FFFFFF`), con una **capa de gradiente sutil de los colores de marca del cliente**
   > (`--bg-wash`, ~5–9% de opacidad) superpuesta — nunca un lavado de color plano ni saturado.
   > Tipografía y textos pasan a tonos oscuros (`--text-hi` casi negro) para contraste. Layouts
   > y tokens de marca (`--grad-brand`, `--cyan/--violet/...`) se ajustan por contraste sobre
   > claro (más profundos que en el sistema oscuro legado). Referencia de receta completa:
   > `presentaciones/multinal-escenario-b/styles.css` (primer deck construido con este estándar).
   > El sistema oscuro queda como legado de decks previos, no se retroaplica sin pedido explícito.
   > **Verificación de decoraciones:** toda decoración agregada (esquinas, anillos, glows, wash)
   > se revisa visualmente en el navegador antes de entregar — sin excepción.
   > **Logo Campuslands:** el PNG maestro en `recursos/` trae relleno transparente irregular;
   > antes de copiarlo a `assets/` de un deck nuevo, recortarlo a su contenido visible
   > (`Image.getbbox()`) + un padding simétrico ~6% de la altura, para que se vea nítido, del
   > tamaño correcto y centrado — nunca copiar el PNG maestro tal cual. Verificar visualmente.
4. ⛔ **REGLA OBLIGATORIA — Plan antes de diseñar:** ANTES de escribir una sola línea
   de HTML/CSS, le presento al usuario **qué va a tener cada diapositiva** (contenido
   + tratamiento visual + **paleta propuesta**, slide por slide). **NO construyo hasta que el usuario confirme.**
5. Con el plan confirmado, elijo un **slug corto y limpio** (ver Reglas de carpetas arriba) y
   construyo el **borrador completo** en `presentaciones/<slug>/`.
   Aplico los **requisitos obligatorios de `<head>`** (ver regla abajo): favicon + título.
6. Lo previsualizo y se lo muestro al usuario.
7. Iteramos sobre ajustes.
8. Exporto a **PDF** (ver `wiki/despliegue.md`) y entrego el archivo.
9. Actualizo `index.md` y agrego entrada a `log.md`.
   > ⛔ **Regla 3 (2026-08-26, reemplaza la de 2026-07-08) — Registro en TRES lugares, sin
   > excepción:** cada vez que agrego una presentación nueva (o re-temátizo una existente):
   > (a) la listo/actualizo en `wiki/index.md`;
   > (b) agrego un **tile con su gradiente y fondo** en `presentaciones/_temas-demo/index.html`
   >     más su bloque de tokens en el catálogo de `wiki/temas-por-cliente.md`;
   > (c) 🆕 **la doy de alta en el portal principal** `presentaciones/index.html` — una entrada
   >     nueva en el arreglo JS `decksData` (`id`, `company`, `title`, `desc`, `category`,
   >     `categoryLabel`, `slides`, `investment`, `cleanSlug`, `directPath`, `pdfPath`,
   >     `pdfLabel`, `logo`, `monogram`, `accentGrad`, `glow`, `dotColor`, `keywords`) siguiendo
   >     el patrón de las entradas existentes, más la copia del logo del cliente **sin procesar**
   >     (tal cual llega en `recursos/`) en `presentaciones/assets/logos/`. Sin este paso el deck
   >     funciona por su cuenta pero no aparece en el catálogo — se le pasó por alto al deck de
   >     FCV en su build inicial y hubo que agregarlo después a pedido del usuario.
   > Las tres actualizaciones se commitean+pushean junto con el resto (ver `wiki/despliegue.md`
   > §4 sobre los dos repos Git involucrados — `presentaciones/` es uno separado del raíz).
10. 🔀 **REGLA OBLIGATORIA — Commit y push automáticos (2026-08-26):** terminado el build/ajuste
    y el registro del paso 9, corro — dentro de `presentaciones/` (el repo Git propio de los
    decks, distinto del raíz; ver arquitectura arriba y `wiki/despliegue.md` §4) —:
    ```
    git add .
    git commit -m "feat: <Nombre Comercial de la Empresa>"
    git push
    ```
    Esto dispara el deploy automático en Vercel, sin esperar a que me lo pidan.
    > **Excepción — repo raíz:** para cambios que solo tocan `wiki/*.md` o `CLAUDE.md` (repo
    > `FullService-Agents`, no `presentaciones/`), sigo usando `git add <archivos puntuales>`
    > en vez de `git add .` — ese repo raíz también versiona el proyecto hermano no relacionado
    > `QuoteDeveloperV2/`, y un `add` amplio arrastraría sus cambios pendientes sin querer.
11. 🔗 **REGLA OBLIGATORIA — Compartir link:** al terminar de crear (o modificar) cualquier
    presentación, **comparto en el chat el link actualizado de Vercel**, con la forma
    `https://fullservicepresentations.vercel.app/<slug>/index.html`
    (reemplazando `<slug>` por la carpeta real de la presentación; también accesible como URL
    limpia `.../<slug>` sin el `/index.html`).

> El flujo de trabajo es: **alcances → paleta del logo → plan de slides → confirmación → diseño → export PDF → compartir link.**
> Mapeo los datos sobre la biblioteca narrativa **flexible** de `wiki/plantilla-base.md`
> (el conteo de láminas es libre, no 16 fijas).

### ⛔ REGLA OBLIGATORIA — Requisitos de `<head>` (toda web)

Cada `index.html` de presentación **debe** tener, sin excepción:

1. **Favicon = isotipo de Campuslands SIN texto** (el casco de astronauta solo, nunca el
   logo con la palabra "campuslands"). El archivo vive dentro del deck en
   `presentaciones/<slug>/assets/favicon.png` (autocontenido, igual que las fuentes) y se
   referencia con `<link rel="icon" type="image/png" href="assets/favicon.png">`.
   El isotipo maestro está en `recursos/favicon-campuslands.png` / `recursos/isotipo-campuslands.png`.
2. **`<title>` = razón social / nombre corporativo COMPLETO de la Empresa** (el cliente),
   **incluyendo el sufijo legal** — p. ej. `Compumax Computer S.A.S.`, `C.I. Green Metal S.A.S.`,
   `Inmobiliaria Mchaileh y Cia. S.A.S.` — sin descripción de la propuesta.
   (Cambiado **2026-07-08** por instrucción del usuario: antes se usaba el nombre corto a secas.
   Los decks ya entregados deben migrarse a su razón social cuando se toquen.)

### Mantener la wiki (Lint)
Periódicamente reviso: contradicciones, info desactualizada, páginas huérfanas,
convenciones de diseño que ya no usamos, y propongo mejoras.

---

## Estándar de calidad de diseño (anti-plantilla) — v2 Premium

Las presentaciones NO deben verse genéricas. Nivel objetivo: **diseñador profesional**.
Cada deck debe demostrar:
- **Paleta propia por cliente** derivada del logo (**fondo teñido** + gradiente de acento),
  distinta en cada deck; el cian→azul→violeta→magenta es solo el tema *default* (ver
  `wiki/temas-por-cliente.md`). **Gradientes protagonistas** en títulos clave, figuras y
  glows de fondo. Priorizar gradiente sobre color plano.
- **Fuentes locales reales** por `@font-face` desde `recursos/fonts/`: Playfair Display
  (display), Montserrat (labels), Poppins (cuerpo), DM Serif (alterno). Prohibido Cambria/Calibri.
- **Dinamismo**: NO todas las láminas iguales. Alternar arquetipos de layout entre láminas
  contiguas (portada, métricas, split, diagrama, grid, statement, timeline, tabla, CTA).
- Jerarquía por contraste de escala, ritmo intencional en el espaciado, profundidad/capas.
- ⛔ **REGLA OBLIGATORIA — Balance de espacio (2026-07-09):** ninguna lámina debe dejar espacio
  **vacío** (una franja de fondo sin contenido porque el bloque se renderizó a su tamaño mínimo,
  p. ej. una sola fila de tarjetas pequeñas en una lámina más alta), pero tampoco debe quedar todo
  **apretado** (elementos pegados, sin `gap`/padding perceptible). Antes de dar el borrador por
  terminado: si sobra una franja vacía notable (>15–20% de la altura de `.s-body`),
  **redistribuir** el contenido — más filas/columnas, tarjetas/tipografía/nodos más grandes, o
  `gap`/padding mayor, en ese orden de preferencia — antes de entregar. Caso real que originó la
  regla: `presentaciones/greenmetal-fyswap/`, timeline de 6 fases en 1 fila que dejaba ~40% de la
  lámina vacío. Detalle completo en `wiki/sistema-diseno.md` §5.1.
- **Conteo de láminas LIBRE** (no 16 fijas): las que la narrativa necesite.
- **Verificación perfecta** de alineación y posición de logos, tarjetas y figuras
  (preview en navegador + export PDF + lectura del PDF; sin hairlines ni desbordes).

Animar solo `transform`, `opacity`, `clip-path`. Definir tokens en CSS custom properties,
no hardcodear. Lámina de referencia: `presentaciones/miami-aqua-tours-ampliado/`.

---

## Shell interactivo obligatorio (Web) — v3

⛔ **REGLA OBLIGATORIA (2026-08-26):** toda presentación **web** se entrega dentro de un shell de
navegación de **una sola lámina a la vez**, no como scroll vertical de láminas apiladas. **Esto
no afecta al PDF exportado** (ver abajo). Referencia canónica: `presentaciones/marval/`
(primer deck con este shell); implementación de un solo escenario en `presentaciones/fcv/`.

**Barra superior** (`.app-header`):
- Esquina izquierda: logo Campuslands + divisor + logo del cliente.
- Centro: el switch de escenario **solo si el deck tiene 2 o más escenarios** (como Marval);
  con un único escenario, el centro queda **vacío**.
- Esquina derecha: badge "Confidencial" coloreado con `--dot-confidential` del cliente vía
  `color-mix()` — nunca un `rgba(...)` hardcodeado por deck.

**Centro** (`.slides-container`): una sola lámina visible (`.slide.active`), **centrada**, con
**sombra** (`box-shadow`) que la separe del fondo de la app. Se dibuja a su tamaño físico real
(1056×594px = 11in×6.1875in a 96dpi, igual que el PDF) y se reescala como un todo con `zoom`
—nunca `transform:scale()`, rompe el texto SVG en gradiente— según el espacio disponible.

**Barra inferior** (`.slides-footer-controls`):
- Esquina izquierda: flecha funcional a la lámina anterior.
- Centro: indicador "N / total" + barra de progreso + botón Play/Pausa de autoplay (5s).
- Esquina derecha: flecha funcional a la lámina siguiente.
- También navegable con `←`/`→` del teclado; el conteo da la vuelta (última → primera y viceversa).

**El PDF no se ve afectado:** el shell es solo de pantalla. `@media print` lo oculta por completo
y devuelve cada `.slide` a su `display:block` secuencial de tamaño físico real — el PDF sigue
siendo una página por lámina, sin ningún elemento de navegación, igual que antes de este shell.
Verificar (número de páginas + lectura visual) cada vez que se agrega a un deck existente.

Snippets de HTML/CSS/JS reutilizables (con y sin switch de escenario) en
`wiki/sistema-diseno.md` §6.

---

## Convenciones de la bitácora (log.md)

Cada entrada empieza con prefijo consistente para que sea parseable:
`## [YYYY-MM-DD] <tipo> | <descripción>` donde tipo ∈ {setup, build, ajuste,
deploy, lint, marca}.
