# Marca Campuslands Full Service

Este documento establece las directrices de identidad visual, el tono editorial y las
normas de aplicación de marca para todas las presentaciones. **Reemplaza a la versión
anterior (paleta plana violeta + Cambria/Calibri).** El nuevo lenguaje visual es
*premium, con gradientes y tipografía de carácter*. Ver también [[sistema-diseno]].

---

## 1. Tono y Estilo Editorial (Voz de Marca)

Corporativo, sofisticado y persuasivo. Tecnología enterprise que resuelve problemas reales.

* **Data-driven:** cada afirmación respaldada por métricas (*"ahorro de 4 h manuales"*, *"ROI en 6 meses"*).
* **Orientación al ROI:** la narrativa destaca valor comercial/financiero, no solo el logro técnico.
* **Agilidad:** metodologías modernas, despliegue continuo e IA aplicada.

---

## 2. Paleta de Colores (v2 — con gradientes protagonistas)

El acabado ya **no** es violeta plano. La base sigue siendo oscura, pero el color vive
en **gradientes** y en un acento ámbar puntual.

> **Importante (2026-07-07):** la paleta cian→azul→violeta→magenta de abajo es el **tema
> *default* de Campuslands**, no la de todos los decks. Cada presentación deriva su **propia
> paleta del logo del cliente** —**incluido el fondo oscuro teñido**— manteniendo este mismo
> lenguaje visual. Ver receta y catálogo en [[temas-por-cliente]].

### Fondos
| Token | Hex | Uso |
| :--- | :--- | :--- |
| `--bg-0` | `#05070F` | Base más profunda (esquinas, viñeteado). |
| `--bg-1` | `#0A0E1A` | Base estándar de lámina. Prohibido negro puro `#000000`. |
| `--bg-2` | `#0D1424` | Superficies elevadas (tarjetas, paneles). |

### Texto
| Token | Hex | Uso |
| :--- | :--- | :--- |
| `--text-hi` | `#FFFFFF` | Títulos, números de métrica. |
| `--text-mid` | `#C3CBDA` | Cuerpo destacado, subtítulos. |
| `--text-lo` | `#7A8699` | Descripciones, kickers, viñetas. |
| `--text-faint`| `#4A5468` | Detalles, líneas guía. |

### Acentos y gradientes
| Token | Valor | Uso |
| :--- | :--- | :--- |
| `--cyan` | `#35D0F0` | Eyebrows, labels, brackets, íconos. |
| `--blue` | `#4A7DFF` | Paso medio del gradiente, enlaces. |
| `--violet` | `#8B5CF6` | Paso alto del gradiente, acentos. |
| `--magenta` | `#C05CF6` | Cierre del gradiente, highlights. |
| `--amber` | `#F5A623` | **Único acento cálido.** Punto "Confidencial", alertas, dato clave. |
| `--lime` | `#A6E22E` | Uso muy puntual (éxito / check positivo). |
| `--grad-brand` | `linear-gradient(100deg,#35D0F0,#4A7DFF,#8B5CF6,#C05CF6)` | **Gradiente insignia.** Palabra clave del título, barras, bordes activos. |
| `--grad-cyan` | `linear-gradient(120deg,#35D0F0,#4A7DFF)` | Acentos fríos, líneas divisorias. |
| `--grad-violet`| `linear-gradient(120deg,#6E8BFF,#C05CF6)` | Alternativa cálida-fría para variar entre láminas. |

> **Regla de gradiente:** cada lámina debe usar al menos un gradiente (texto, borde,
> figura o glow de fondo). Rota entre `--grad-brand`, `--grad-cyan` y `--grad-violet`
> para que no todas se vean iguales (ver dinamismo en [[sistema-diseno]]).

---

## 3. Tipografía Oficial (v2 — fuentes locales reales)

Se retiran Cambria/Calibri. El sistema usa tres familias cargadas por `@font-face`
desde `recursos/fonts/`:

| Rol | Familia | Pesos usados |
| :--- | :--- | :--- |
| **Display / Títulos** | **Playfair Display** (serif alto contraste; la itálica Black es la firma de marca) | 700, 900, italic 400/900 |
| **Display alterno** | **DM Serif Display** (para variar portadas o cierres) | 400, italic |
| **Labels / Eyebrows** | **Montserrat** (geométrica; siempre MAYÚSCULAS con tracking amplio) | 500, 600, 700 |
| **Cuerpo / Viñetas** | **Poppins** (sans humanista legible) | 300, 400, 500, 600 |

* El **título grande** combina una línea en blanco (`--text-hi`) + una línea clave en
  **gradiente** e **itálica** (`.gradient-text`).
* Eyebrows y labels: Montserrat 600, `letter-spacing: 0.22em–0.34em`, `text-transform: uppercase`, color `--cyan`.
* El bloque `@font-face` canónico está en [[sistema-diseno]] y en `recursos/fonts/`.

---

## 4. Uso de Logotipos (verificación obligatoria)

Assets en `recursos/`:
* `Logo Campuslands  Horizontal Blanco.png` — **el correcto para fondo oscuro** (PNG transparente, blanco). Se copia como `assets/logo-campuslands.png`.
* `Logo Campuslands Horizontal Azul.png` — solo para fondos claros (no usar en estos decks).
* Logo del cliente: PNG transparente que provee el usuario → `assets/logo-cliente.png`.

### Reglas verificadas
1. **Portada:** Campuslands (blanco) en la esquina superior izquierda; el cliente va
   **inline junto a "PARA"** dentro del cuerpo. (Se elimina la antigua regla de "portada
   sin logos".)
2. **Láminas internas:** Campuslands arriba-izquierda, cliente arriba-derecha, ambos
   flotando sobre el fondo (sin cajas ni barras).
3. **Transparencia:** verificar que el PNG del cliente tenga alfa (fondo transparente).
   Si viniera con fondo blanco, recortarlo antes de usar.
4. **Proporción:** nunca deformar. Fijar solo `height` y `width:auto`. Campuslands ~26px
   en portada / ~24px interno; cliente ~58–66px en portada / ~34px interno.
5. **Contraste:** el logo del cliente debe leerse sobre el fondo oscuro; si es muy oscuro,
   colocarlo sobre un chip `--bg-2` con leve padding.
