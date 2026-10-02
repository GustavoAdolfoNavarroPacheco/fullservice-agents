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
3. **Colores y Fuentes:** Confirmar que los fondos sean los de Campuslands y que las tipografías sean **Poppins** y **Roboto Mono** (sin fuentes de respaldo). Lo comprueba `herramientas/verificar_deck.py --pdf …` (ver [[verificacion]]); aun así se mira cada lámina.
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
| `PresentationsDesigner/presentaciones/` | `github.com/.../Presentaciones` (repo **distinto**, propio) | Todos los decks (`presentaciones/<slug>/`), el portal `presentaciones/index.html` y `_temas-demo/` — es la raíz que Vercel despliega | Hay un **auto-commit/push en segundo plano** (mensajes genéricos `feat: updates`) que a veces ya sube los archivos nuevos de un deck sin intervención. **No asumir que ya corrió** — verificar con `git status`/`git log -1` antes de decidir si hace falta commitear a mano (como pasó con el rename a `/fcv`: el primer build sí se auto-subió, el rename posterior no, y hubo que commitear manualmente). |
| `PresentationsDesigner/` (esta carpeta) | ninguno (no tiene `.git` propio) | — | Los comandos `git` ejecutados aquí sin `-C` resuelven al repo de arriba (`FullService-Agents`), no a `presentaciones/`. |

**Implicaciones prácticas:**
* `wiki/*.md` se commitea en el repo **de arriba** (`FullService-Agents`); los archivos del deck
  (`presentaciones/<slug>/**`, `presentaciones/index.html`, `presentaciones/assets/logos/*`) se
  commitean en el repo **de `presentaciones/`**. Un solo `git add -A` en la carpeta equivocada
  puede arrastrar cambios sin relación de `QuoteDeveloperV2/` — usar siempre rutas de archivo
  explícitas.
* El **portal** `presentaciones/index.html` (catálogo con login, buscador y filtros) mantiene su
  propio arreglo `decksData` en JS con una entrada por deck (`id`, `company`, `title`, `desc`,
  `category`, `slides`, `investment`, `cleanSlug`, `directPath`, `pdfPath`, `logo`, `monogram`,
  `accentGrad`, `glow`, `dotColor`, `keywords`). **Registrar cada deck nuevo ahí también** (no solo
  en `wiki/index.md`) — se pasó por alto en el build inicial de FCV y hubo que agregarlo después a
  pedido del usuario. El logo del cliente para la tarjeta del portal es una copia **sin procesar**
  de `recursos/<Cliente>.png` en `presentaciones/assets/logos/` (no el PNG recortado/tratado que
  vive dentro de `presentaciones/<slug>/assets/`).
* **URL limpia `/slug`:** para que funcione (Vercel resuelve `/slug` → `/slug/index.html` por
  defecto, sin rewrite en `vercel.json`), el nombre de la carpeta debe **ser exactamente** el
  `cleanSlug` usado en el portal — ambos deben coincidir. Si el usuario pide cambiar la URL,
  renombrar la carpeta (`git mv`, no copiar) y actualizar `directPath`/`pdfPath`/`cleanSlug` en el
  portal y todas las rutas en `wiki/*.md` en el mismo cambio.
