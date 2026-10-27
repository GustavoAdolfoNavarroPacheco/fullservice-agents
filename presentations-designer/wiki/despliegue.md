# Guía de Despliegue y Exportación a PDF

Este documento detalla las especificaciones técnicas necesarias para compilar y exportar de forma exitosa las presentaciones desarrolladas en HTML/CSS a archivos PDF limpios y de alta calidad mediante Google Chrome headless.

---

## 1. Configuración CSS Obligatoria para Impresión

Para garantizar que el archivo PDF simule perfectamente una diapositiva en formato horizontal y evite desbordamientos no deseados o márgenes por defecto del navegador, se deben aplicar las siguientes directivas CSS en `styles.css`:

```css
/* Configuración de Página */
@page {
  /* Dimensiones estándar para una proporción de pantalla 16:9 */
  size: 11in 6.1875in; /* Relación de aspecto 16:9 en pulgadas */
  margin: 0; /* Remueve los cabezales y pies de página por defecto de Chrome */
}

/* Optimización de Medios de Impresión */
@media print {
  html, body {
    width: 11in;
    height: 6.1875in;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact; /* Preserva colores de fondo e imágenes */
    print-color-adjust: exact;
    background-color: #0A0E1A !important; /* Asegura fondo premium en export */
  }

  /* Control de Saltos de Página */
  .slide {
    width: 11in;
    height: 6.1875in;
    page-break-after: always; /* Obliga a cada diapositiva a ser una hoja de PDF */
    break-after: page;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
  }
}
```

---

## 2. Comando de Exportación a PDF

Para generar el PDF, el agente de Claude ejecutará el comando directo a través del shell de Windows (`powershell`), localizando el ejecutable de Google Chrome.

### Estructura del Comando en Windows (PowerShell):

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --disable-gpu --print-to-pdf="C:\Users\Full Service\Downloads\PresentationsDesigner\presentaciones\<slug-cliente>\<slug-cliente>.pdf" --no-margins "file:///C:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/<slug-cliente>/index.html"
```

> [!IMPORTANT]
> * **Rutas Absolutas:** Google Chrome Headless requiere rutas absolutas para el parámetro `--print-to-pdf` y para el archivo de origen `file:///`.
> * **no-margins:** La bandera `--no-margins` es crítica para evitar que Chrome fuerce márgenes blancos alrededor de la lámina.
> * **Carga de fuentes (2026-09-29):** añadir `--virtual-time-budget=8000` (o más) y mantener `preloadAllFonts()` en `script.js`: las `@font-face` de láminas ocultas no se descargan solas y el PDF caería a fuentes de respaldo.

---

## 3. Proceso de Verificación del PDF

Tras la compilación, el agente debe validar visualmente el archivo PDF:
1. **Número de Páginas:** Debe coincidir exactamente con el número de láminas del deck (máximo 10; p. ej. 7 láminas = 7 páginas).
2. **Corte de Diapositiva:** Asegurarse de que el texto de una diapositiva no se desborde al inicio de la siguiente debido a un padding excesivo.
3. **Colores y Fuentes:** Confirmar que los fondos sean los de Campuslands y que la tipografía sea **Poppins** únicamente (sin fuentes de respaldo ni Roboto Mono). Lo comprueba `herramientas/verificar_deck.py --pdf …` (ver [[verificacion]]); aun así se mira cada lámina.
4. **Si el Browser pane no puede tomar screenshots** ("pane no desplegado"): verificar por DOM
   (`getBoundingClientRect` para overflow/gap contra el footer) + exportar a PDF y leerlo con
   PyMuPDF (`page.get_pixmap(dpi=150)` por lámina, `dpi=600` con `clip` para zoom a títulos en
   gradiente) en vez de insistir con la captura del navegador. Caso real: sesión FCV (2026-08-26).

---

## 4. Arquitectura real de repos Git (descubierta 2026-08-26 — leer antes de hacer `git push`)

El proyecto vive en **tres repos Git anidados**, no uno solo. Antes de commitear, verificar con
`git rev-parse --show-toplevel` en qué repo se está parado:

| Carpeta | Repo / remoto | Qué contiene | Cómo se sube |
| :--- | :--- | :--- | :--- |
| `FullService Agents - Gustavo Navarro/` (una carpeta arriba de este proyecto) | `github.com/.../FullService-Agents` | Este proyecto (`PresentationsDesigner/`, incluida `wiki/`) **y** el proyecto hermano no relacionado `QuoteDeveloperV2/` | **Manual:** el agente hace `git add` de archivos puntuales (nunca `-A`/`.`) + `commit` + `push`. |
| `PresentationsDesigner/presentaciones/` | `github.com/.../Presentaciones` (repo **distinto**, propio) | `decks/` (todos los decks `presentaciones/decks/<slug>/`, `assets/` y `_temas-demo/`) y `web/` (portal Next.js + TypeScript) — Vercel despliega **`web/`** (Root Directory = `web`, con «Include source files outside of Root Directory» activado porque la web lee `../decks`) | Hay un **auto-commit/push en segundo plano** (mensajes genéricos `feat: updates`) que a veces ya sube los archivos nuevos de un deck sin intervención. **No asumir que ya corrió** — verificar con `git status`/`git log -1` antes de decidir si hace falta commitear a mano (como pasó con el rename a `/fcv`: el primer build sí se auto-subió, el rename posterior no, y hubo que commitear manualmente). |
| `PresentationsDesigner/` (esta carpeta) | ninguno (no tiene `.git` propio) | — | Los comandos `git` ejecutados aquí sin `-C` resuelven al repo de arriba (`FullService-Agents`), no a `presentaciones/`. |

**Implicaciones prácticas:**
* `wiki/*.md` se commitea en el repo **de arriba** (`FullService-Agents`); los archivos del deck
  (`presentaciones/decks/<slug>/**`, `presentaciones/decks/assets/logos/*`, `presentaciones/web/**`) se
  commitean en el repo **de `presentaciones/`**. Un solo `git add -A` en la carpeta equivocada
  puede arrastrar cambios sin relación de `QuoteDeveloperV2/` — usar siempre rutas de archivo
  explícitas.
* El **portal** `presentaciones/web/` (Next.js 16 + TypeScript; login, buscador, filtros por categoría/cliente/fecha, vista cuadrícula/lista) lee su catálogo de **`web/src/data/decks.ts`**
  (`DECKS`, una entrada por deck: `slug`, `client`, `company`, `title`, `desc`, `category`,
  `categoryLabel`, `slides`, `investment`, `path`, `pdf`, `logo`, `date`, `keywords`; el encabezado
  del archivo documenta cada campo). **Registrar cada deck nuevo ahí también** (no solo
  en `wiki/index.md`) — se pasó por alto en el build inicial de FCV y hubo que agregarlo después a
  pedido del usuario. El logo del cliente para la tarjeta del portal es una copia **sin procesar**
  de `recursos/<Cliente>.png` en `presentaciones/decks/assets/logos/` (no el PNG recortado/tratado que
  vive dentro de `presentaciones/decks/<slug>/assets/`).
* **URL limpia `/slug`:** `web/next.config.ts` genera solo las rewrites `/<slug>/` → `<slug>/index.html` leyendo las carpetas de `web/public/` (copia de `decks/` que hace `npm run sync:decks` en `dev`/`build`); el nombre de la carpeta debe **ser exactamente** el
  `slug` usado en el portal — ambos deben coincidir. Si el usuario pide cambiar la URL,
  renombrar la carpeta (`git mv`, no copiar) y actualizar `path`/`pdf`/`slug` en el
  portal y todas las rutas en `wiki/*.md` en el mismo cambio.

### Web (Next.js) — acceso, base de datos y despliegue (2026-10-27)
* **Acceso:** solo el portal `/` es privado; **las presentaciones `/<slug>/` y sus PDF son públicas** (se comparten con clientes). `src/proxy.ts` protege únicamente `/`.
* **Login real en servidor:** usuarios en **Neon** (Postgres), contraseñas con **bcrypt**, sesión en cookie `httpOnly` firmada (JWT, `jose`); 5 fallos → bloqueo de 5 min por correo/IP. Esquema: `web/db/schema.sql`.
* **Variables de entorno** (`web/.env.local` en local; *Settings → Environment Variables* en Vercel): `DATABASE_URL` (Neon, conexión *pooled*) y `AUTH_SECRET`
  (≥ 32 caracteres aleatorios; generar con `node -e "console.log(require('crypto').randomBytes(48).toString('base64url'))"`). **Nunca** se versionan.
* **Alta de usuarios:** `cd presentaciones/web && npm run db:migrate` (una vez) y `npm run user:create -- correo "Nombre"` (pide la contraseña por terminal).
* **Vercel:** Framework *Next.js*, Root Directory `web`, «Include source files outside of Root Directory» activado, Node ≥ 22.18. El build ejecuta `sync:decks` solo.
* **Desarrollo local:** `cd presentaciones/web && npm run dev` (puerto 3000). Más detalle en `presentaciones/README.md`.
