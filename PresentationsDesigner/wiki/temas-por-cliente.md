# Cliente ≠ paleta: la marca es siempre Campuslands

> **Regla del 2026-10-02 (reemplaza todo el sistema de "paleta derivada del logo del cliente").**
> Los **colores de fondo** de toda presentación son **siempre y obligatoriamente** los de Campuslands ([[marca-campuslands]] §4).
> El cliente aporta **su logo y su contenido**; no su paleta. Antes (v2) cada deck tomaba los colores del logo del cliente;
> eso queda **archivado** en [[archivo/temas-por-cliente-v2]] y **no se usa** para decks nuevos.

## Qué sí hace el cliente
- Su **logo** (transparente, recortado, **mismo alto** que el de Campuslands; ver [[marca-campuslands]] §3.5).
- Su **nombre/razón social** (en `<title>`, portada y textos).
- Su **contenido**: dolor, solución, cifras, equipo, inversión.

## Qué NO hace
- No tiñe fondos, gradientes, acentos ni íconos.
- No cambia tipografías.
- No se recolorea su logo. Si no contrasta con el fondo elegido, **cambia el fondo de esa zona** (navy ↔ arena) o se pide otra versión del logo.

## Cómo elegir el fondo de cada lámina (en lugar de "derivar la paleta")
1. Arrancar por el **contenido**: datos y comparaciones → **arena**; narrativa y portada/cierre → **navy**; énfasis o variación → **violeta**.
2. Verificar que el **logo del cliente** contraste con ese fondo (si el logo es oscuro monocromo → arena; si es claro → navy/violeta; si es a color con
   mucho navy/violeta → arena). Es una decisión **por lámina**, no por deck.
3. Alternar fondos entre láminas contiguas para el ritmo (R3).
4. Acentos: solo dorado/celeste/verde (+ violeta sobre arena) según los pares de contraste.

## Logo del cliente: lista de comprobación
- [ ] PNG/SVG con **transparencia** real (ver bordes; si trae fondo blanco, recortarlo).
- [ ] Recortado al **contenido exacto** (`getbbox`), sin padding irregular.
- [ ] Copia **sin procesar** en `presentaciones/assets/logos/` (para el portal) y recortada en `assets/` del deck.
- [ ] Probado sobre el fondo de **cada** lámina donde aparece; altura igual a la de Campuslands (`verificar_deck.py`).
- [ ] Si es muy ancho/alto: se mide el área y se ajusta ópticamente **mirando**, sin deformar.

## Portal y catálogo
- La entrada del deck en `presentaciones/index.html` usa colores de marca: `accentGrad: linear-gradient(100deg,#2CAAFF,#5E3AE2 60%,#000087)`,
  `glow: rgba(94,58,226,.25)`, `dotColor: #F4B422`.
- `presentaciones/_temas-demo/` es **histórico**: no se agregan tiles nuevos.
