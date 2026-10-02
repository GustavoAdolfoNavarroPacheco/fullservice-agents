# Cliente ≠ paleta: la marca es siempre Campuslands

> **Regla del 2026-10-02 (reemplaza todo el sistema de "paleta derivada del logo del cliente").**
> Los **colores de fondo** de toda presentación son **siempre y obligatoriamente** los de Campuslands ([[marca-campuslands]] §4).
> El cliente aporta **su logo y su contenido**; no su paleta. Antes (v2) cada deck tomaba los colores del logo del cliente;
> eso queda **archivado** en [[archivo/temas-por-cliente-v2]] y **no se usa** para decks nuevos.

## Qué sí hace el cliente
- Su **logo** (transparente, recortado, con el **mismo peso visual** que el de Campuslands — áreas iguales vía `--k-cliente` de `herramientas/igualar_logos.py`; ver [[marca-campuslands]] §3.5).
- Su **nombre/razón social** (en `<title>`, portada y textos).
- Su **contenido**: dolor, solución, cifras, equipo, inversión.

## Qué NO hace
- No tiñe fondos, gradientes, acentos ni íconos.
- No cambia tipografías.
- No se recolorea su logo. Si no contrasta con el blanco, se pide otra versión del logo (el fondo **no** cambia: tema claro obligatorio).

## Cómo elegir el fondo de cada lámina (en lugar de "derivar la paleta")
1. **Fondo de toda lámina = blanco `#FFFFFF`** (tema claro obligatorio, web y presentación).
2. Verificar que el **logo del cliente** contraste con el blanco (WCAG ≥ 4,5 : 1 en su parte principal). Si es un logo claro/blanco, pedir la versión oscura o a color.
3. El ritmo se da con **arquetipos** distintos entre láminas contiguas y con **tarjetas navy/violeta** como acento (R3), no con cambios de fondo.
4. Acentos: dorado/celeste/verde (+ violeta y navy sobre arena) según los pares de contraste.

## Logo del cliente: lista de comprobación
- [ ] PNG/SVG con **transparencia** real (ver bordes; si trae fondo blanco, recortarlo).
- [ ] Recortado al **contenido exacto** (`getbbox`), sin padding irregular.
- [ ] Copia **sin procesar** en `presentaciones/assets/logos/` (para el portal) y recortada en `assets/` del deck.
- [ ] Probado sobre el blanco; **área igual** a la de Campuslands (`igualar_logos.py` → `--k-cliente`; `verificar_deck.py` ±6 %).
- [ ] Confirmado **mirando** que ninguno de los dos domina; si lo parece, se ajusta `--k-cliente` unos puntos, sin deformar.

## Portal y catálogo
- La entrada del deck en `presentaciones/index.html` usa colores de marca: `accentGrad: linear-gradient(100deg,#2CAAFF,#5E3AE2 60%,#000087)`,
  `glow: rgba(94,58,226,.25)`, `dotColor: #F4B422`.
- `presentaciones/_temas-demo/` es **histórico**: no se agregan tiles nuevos.
