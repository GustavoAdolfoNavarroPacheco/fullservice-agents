# Bitácora de Actividades (Log)

Registro cronológico de las construcciones, despliegues y mantenimiento de la wiki y presentaciones.

---

## [2026-09-22] build | Alcaldía de Girón — Cobro Coactivo con IA (deck individual, 10 láminas)

* **Fuente:** XLSX nuevo de cotización (`FullServices Cotización Alcaldia de Girón.xlsx`), una sola hoja "Cobro Coactivo" con ~190 funcionalidades en 14 submódulos (Levantamiento → Despliegue). Total `Y1`=`$99.295.168,59` (`=SUMIFS(...)`, ya con margen comercial completo, verificado contra `AC1`=`SUM(AC2:AC219)`), redondeado a `$99.295.169 COP`, pago 40/40/20.
* **Pedido explícito:** deck individual dirigido al Alcalde (distinto del catálogo general de 13 propuestas en `presentaciones/giron/`), tope de **10 láminas**, cronograma "4 meses + pruebas" (mismo patrón del catálogo general), "más dinamismo, que no sea plano", y copy narrado desde la perspectiva del Despacho del Alcalde (gobierno/transparencia/recaudo), no lenguaje corporativo de ROI.
* **Plan de láminas:** 14 submódulos fusionados en 6 láminas de contenido vía `.merge-split`/`.merge-split--trio`/`.split-asym`/`.flow-columns`/icon-grid doble, más portada, contexto (`.pipe-row` de 8 pasos), equipo/cronograma (`.sys-split`) y cierre — 8 arquetipos de layout distintos en 9 láminas de contenido, sin repetir tratamiento visual entre láminas contiguas.
* **Paleta y assets:** reutilizados sin cambios de `presentaciones/giron/` (oro brillante → bronce oscuro del escudo heráldico; logo, favicon y fuentes ya recortados).
* **Iteración de cierre (2 rondas de feedback):** la lámina 10 (Inversión + Cierre) se construyó primero como `cover--close` centrado (todo apilado: inversión, pasos, statement, contacto, lockup) — el usuario la marcó como "mal distribuida" (ronda 1) y se rediseñó a un layout `.internal` de 2 columnas (`.cta`: panel de inversión + hoja de ruta suelta a la izquierda, `.contact-card` con lockup a la derecha). El usuario volvió a marcarla como "muy mal distribuida, no simetría, líneas" (ronda 2) — la columna izquierda era una tarjeta + una lista flotante sin marco, y la tarjeta de contacto quedaba visualmente más alta y sin alinear con nada. Se resolvió con un componente nuevo `.peer-card`: dos tarjetas gemelas (mismo padding, radio, barra de acento izquierda en gradiente de marca, `.peer-card__divider` como línea separadora) dentro de `.cta--pair` (`grid-template-columns:1fr 1fr; align-items:stretch`), de modo que ambas columnas quedan exactamente a la misma altura y alineadas — inversión+pasos en una tarjeta, contacto+lockup en la otra. Verificado en pantalla y en el PDF exportado (ambas tarjetas idénticas en alto).
* **4ª ronda de feedback (mismo día) — deck reducido de 10 a 9 láminas:** el usuario pidió eliminar la columna derecha de la lámina de Equipo/Cronograma ("4 meses + pruebas y go-live", `.timeline-v`), actualizar el título de esa lámina en consecuencia (ya no menciona "4 meses"), mover ahí el bloque de Inversión y Forma de Pago, y **eliminar por completo** la lámina 10 dedicada (Inversión + Cierre/Contacto Campuslands) — sin relocalizar el contacto en ninguna otra parte del deck. Implementado: título de la lámina 9 cambia a "Un equipo dedicado, *inversión clara*" (viewBox del SVG en gradiente medido vía `getBBox()`, `width=7138`); la columna derecha del `.sys-split` pasa de cabecera "4 meses + pruebas y go-live"/`.timeline-v` a cabecera "Inversión y Forma de Pago"/`.invest-block` (reutilizando sin cambios los componentes `.pay-tiles--sm` y `.steps--compact.steps--sm` ya creados en la ronda anterior); la lámina 10 se borra íntegra del `index.html`. Actualizados en cascada: `totalSlides` en `script.js` (10→9), indicador `1 / 10`→`1 / 9`, numeración de página de la lámina 9 (ya era `09`), campo `slides` en `presentaciones/index.html` (`decksData`), y las 3 referencias de conteo de láminas en `wiki/index.md`/`wiki/temas-por-cliente.md`. Re-exportado a PDF: 9 páginas, verificado visualmente sin desbordes.
* **3ª ronda de feedback (mismo día) — desglose elemento por elemento con capturas de referencia:** el usuario pidió 5 cambios puntuales sobre esa misma lámina, cada uno con una imagen de referencia exacta: (1) la tarjeta derecha debe limitarse solo al contenido de contacto (rol/nombre/cargo/email/teléfono); (2) **eliminar por completo** el lockup de logos Campuslands×Girón de esa tarjeta; (3) el bloque de inversión total **sin fondo/tarjeta** y con la cifra **más grande**; (4) que sean **solo los tres cuadros** de pago (sin envoltorio adicional); (5) la lista de 3 pasos **sin fondo** y **un poco más pequeña**. Implementado quitando el wrapper `.peer-card` del lado de inversión (nuevo `.invest-block`, sin `background`/`border`, texto suelto directo sobre el fondo de la lámina — label + `.invest-block__amount` a 30pt, el doble del tamaño anterior de 18pt), quitando `.contact-card__lockup` del marcado de esta lámina (sigue existiendo en CSS por si se reutiliza, pero ya no se referencia aquí), y agregando el modificador `.steps--sm` (dot 26→20px, label 9.6→8.4pt) sobre `.steps--compact`. `.cta--pair` pasa de `1fr 1fr` a `1.2fr .8fr` (la columna de inversión ya no está en una tarjeta y necesita más ancho relativo) con `align-items:center` (ya no `stretch`, porque solo un lado tiene tarjeta). Verificado en pantalla y en el PDF re-exportado.
* **Ajuste de logos (pedido explícito, alcance acotado):** solo 2 puntos agrandados — el lockup del header (`.header-left img` 26→34px, `.logo-client` 42→54px) y el lockup de la lámina de cierre bajo el número de página (`.contact-card__lockup img` 18→26px, `.client` 28→40px) — sin tocar el logo de portada ni el de `.s-header` en las láminas de contenido.
* **Registro:** wiki/index.md, `wiki/temas-por-cliente.md` (nota de reutilización de paleta), tile en `presentaciones/_temas-demo/index.html` (reutiliza `.t-grn`), y alta en el portal `presentaciones/index.html` (`decksData`, insertado al inicio, fecha 2026-09-22) con el logo sin procesar ya existente en `presentaciones/assets/logos/Alcaldia de Giron.png`.

## [2026-09-21] ajuste | Landcargo S.A.S. — Dinamismo de layouts (anti-planitud)

* **Motivo:** el usuario señaló que el deck se veía "plano" — 5 de las 10 láminas (03, 04, 05, 06, 07) usaban el mismo layout `.merge-split` de 2 columnas y las 2 láminas trio (08, 09) también eran visualmente idénticas entre sí. Pedido explícito: "más dinamismo" y que "la mayoría de hojas" dejaran de verse "prácticamente iguales" — sin tocar el contenido/alcance ya aprobado.
* **4 arquetipos de layout nuevos**, todos reutilizando los tokens de marca existentes (sin tocar la paleta):
  - `.icon-grid`/`.icon-card` (lámina 03: Comercial/CRM + Hojas de Vida) — grid de tarjetas con ícono, agrupadas por rótulo en vez de columnas partidas.
  - `.flow-columns`/`.flow-col`/`.flow-step` (lámina 05: Cumplidos → Liquidaciones) — pasos verticales numerados y conectados por línea, con un conector `→` entre los dos encabezados de columna (no centrado contra toda la columna, sino alineado a la altura de "Cumplidos"/"Liquidaciones" — ver nota de UX abajo).
  - `.merge-item--ic` (láminas 06 y 08) — variante de `.merge-item` con badge de ícono circular en gradiente de marca en vez de solo el borde izquierdo; en la lámina 09 se aplicó además `.merge-item--warn` (ícono de alerta) solo a la columna "Riesgos Identificados", diferenciándola de "Fuera de Alcance" (texto plano) y "Próximos Pasos" (convertida a `.flow-col` de pasos numerados) — 3 tratamientos distintos dentro de una misma lámina trio.
  - `.split-asym` (lámina 07: Tesorería + Contable/ERP) — panel angosto de marca (ícono grande + `.flow-col--solo`) a la izquierda, grid de tarjetas ancho a la derecha, en vez de 2 columnas parejas.
  - Iconografía nueva: ~28 íconos de línea (stroke, 24×24) dibujados a mano para los conceptos del SRS (RUN, semáforo, geocerca, FOPAC, DIAN, RNDC, etc.), sin librería externa.
* **Animaciones de entrada por ítem (regla nueva, reutilizable):** `@keyframes itemFadeUp` + `nth-child` stagger aplicado a `.merge-item`, `.icon-card`, `.pipe-item` y `.flow-step` — como el shell alterna `.slide{display:none↔block}`, las animaciones CSS se re-disparan solas cada vez que se revisita una lámina (sin JS adicional). `@media print{ *{animation:none!important} }` agregado al bloque de impresión para que el PDF capture siempre el estado final, nunca un frame a medias.
* **2 rondas de corrección de balance de espacio** (verificación PDF página por página, no solo en navegador): lámina 05 dejaba ~35% de vacío abajo (se centró verticalmente el `.flow-col` y se agrandaron los pasos); lámina 03 con el primer tamaño de `.icon-card` se desbordaba sobre el footer (se recalibró el padding/tipografía a un punto medio); lámina 07 con el primer tamaño de `.split-asym__side` desbordaba el panel angosto sobre el footer (se compactó `.flow-col--solo` y se acortaron 2 descripciones).
* **Corrección de UX del conector (pedido explícito del usuario tras ver la lámina 05):** el `→` entre "Cumplidos" y "Liquidaciones" se centraba inicialmente contra la altura total de la columna (encabezado + 5 pasos), quedando visualmente a la altura del paso 3 sin relación clara con nada. Se rediseñó para anclarse a la altura de los encabezados de columna — ahora lee literalmente "Cumplidos → Liquidaciones", más intencional que un punto medio aritmético.
* **Sin cambios de alcance, contenido ni paleta** — las 10 láminas, el PDF (re-exportado) y el link de Vercel siguen igual; solo cambió el tratamiento visual de 6 láminas.

## [2026-09-21] ajuste | Landcargo S.A.S. — Corrección de láminas 5, 7 y 9 (feedback visual)

* **Lámina 05 (Cumplidos → Liquidaciones):** el conector `→` entre "Cumplidos" y "Liquidaciones" se centraba contra la altura total de cada columna (encabezado + 5 pasos); como las dos columnas tenían alturas de contenido ligeramente distintas (ítem 2 de Cumplidos envolvía a 2 líneas), sus encabezados no quedaban a la misma altura y el conector terminaba apuntando "sin sentido" al nivel del paso 3. **Fix estructural:** se separó cada `.flow-col` en `.flow-col__head` (`flex:none`, altura fija 33px) + `.flow-col__steps` (`flex:1`, centrado solo en el espacio restante) — los encabezados quedan garantizado-nivelados sin importar el contenido. El conector volvió a anclarse a esa misma altura fija (33px desde arriba), leyendo literalmente "Cumplidos → Liquidaciones". Se acortó además la descripción del ítem 2 para reducir el desbalance de alturas entre columnas.
* **Lámina 07 (Tesorería + Contable/ERP):** el panel blanco quedaba pegado al footer pese a varios intentos de `margin-bottom` en `.split-asym` (probado hasta 60px sin ningún efecto visible — se descartó como problema de caché de Chrome headless probando con perfiles de usuario nuevos en cada export, tampoco cambió nada). **Causa real encontrada con un fondo rojo de depuración temporal:** `.split-asym__main` (la grid de tarjetas ERP) desbordaba silenciosamente su propia caja — su contenido necesitaba más alto del que el layout le asignaba y, al no tener `overflow:hidden`, el desborde se pintaba visualmente por debajo sin ser recortado, ignorando cualquier margen del contenedor padre. Se corrigió agregando `overflow:hidden` + `min-height:0` a `.split-asym__main` y reduciendo el tamaño de las `.icon-card` (padding, íconos y tipografía) para que el contenido real quepa dentro de su caja — ahora sí se ve, y respeta, el `margin-bottom` de `.26in` antes del footer.
* **Lámina 09 (Riesgos + Fuera de Alcance + Próximos Pasos):** el usuario reportó desagrado visual general sin especificar la causa exacta — la mezcla de 3 tratamientos distintos en una sola lámina (tarjetas con ícono de alerta + tarjetas de texto plano + timeline numerado) se sentía inconsistente en vez de dinámica. **Rediseño:** las 3 columnas ahora comparten un mismo lenguaje visual — `.flow-col--solo` (timeline vertical numerado) en las tres — diferenciadas solo por el color/glifo del marcador: rojo `!` para Riesgos (`.flow-step--danger`), gris `×` para Fuera de Alcance (`.flow-step--muted`, nuevo modificador), azul de marca 1-4 para Próximos Pasos. Resultado: cohesión dentro de la lámina, pero sigue siendo visualmente distinta de la lámina 08 (que usa grid de tarjetas con ícono).
* **Nota de proceso — debugging de PDF:** confirmado que Chrome headless con `--print-to-pdf` puede servir CSS obsoleto entre invocaciones sucesivas pese a fetch fresco del HTML (la hoja de estilos enlazada no lleva cache-busting); el fix reproducible es lanzar cada export con un `--user-data-dir` nuevo (perfil desechable). Útil para cualquier deck futuro si un cambio de CSS "no aparece" en el PDF pese a estar confirmado en el archivo fuente.

## [2026-09-21] build | Landcargo S.A.S. — Sistema Integrado TMS + ERP a la Medida

* **Fuente:** "Toma de Requerimientos - TMS ERP Landcargo.pdf" (18 páginas, SRS elaborado a partir de la transcripción de la sesión del 09/09/2026) para la transformación de Landcargo de operador **2PL a 4PL**. Documento de alcance funcional puro — sin cifras de inversión, sin lámina de inversión en el deck.
* **Restricción explícita del usuario:** máximo 10 láminas (pedida después de presentar un plan inicial de 18). Los **11 módulos funcionales** del SRS (Comercial/CRM, Hojas de Vida, Despacho, Manifiestos, Cumplidos, Liquidaciones, Tesorería, Tráfico, Flota Propia, Contable/ERP, Transversales) se fusionaron en 5 pares temáticamente afines vía `.merge-split` según la etapa del flujo operativo (captación → despacho/RNDC → cumplido/liquidación → vehículos → pago/contabilización) más 2 láminas `.merge-split--trio` (Transversales+No Funcionales+Interfaces Externas; Riesgos+Fuera de Alcance+Próximos Pasos), sin perder ningún requisito.
* **Diagrama de flujo:** lámina 2 usa `.pipe-row` con los **10 pasos** del ciclo operativo end-to-end (cliente→hoja de vida→inspección→despacho→manifiesto→tráfico→cumplido→liquidación→pago→contabilidad) — el conteo más alto de pasos usado en este componente hasta ahora (el de Chico tenía 7).
* **Paleta:** derivada por muestreo de píxeles del logo — periwinkle (`#3B78DF`, faceta clara del ícono) → azul corporativo (`#0047A0`, faceta oscura + wordmark "CARGO") → azul marino → gris pizarra del wordmark "LAND" (`#504F4F`) como 4ª parada neutra del `--grad-brand`, para distinguirse de la paleta mono-azul ya usada por Marval (ver [[temas-por-cliente]]).
* **Bug de ancho de texto SVG en gradiente (confirmado de nuevo):** el cierre "¿Cuándo *empezamos*?" con el ancho `viewBox` exacto medido por `getBBox()` (4738px) mostró el signo "?" montado sobre la "s" final en el PDF exportado — mismo bug ya documentado para FCV y Miami Aqua Tracking. Se corrigió con un margen de seguridad de ~10% (5250px) en vez del valor exacto medido; verificado en el PDF re-exportado.
* **Ajustes de balance de espacio (regla obligatoria de CLAUDE.md):** la columna "Hojas de Vida" (lámina 3) desbordaba el footer con 6 ítems a tamaño por defecto — se fusionaron los 2 últimos en 1 para bajar a 5. La columna "Fuera de Alcance" (lámina 9, trio) con solo 3 ítems quedaba centrada verticalmente y desalineada respecto a las otras 2 columnas de 4 — se agregó un 4to ítem real del SRS (nota metodológica de la sección 1.4 sobre validación de nombres de sistemas) para igualar el conteo y alinear los 3 encabezados.
* Assets del deck (fuentes, favicon, logo Campuslands) copiados de `chico/` por ser el template más cercano en estructura (shell de un solo escenario + `.merge-split` extensivo); logo del cliente recortado a bbox + padding simétrico ~6% desde `recursos/company-logos/Land Cargo.png` (transparencia real, sin necesidad de reconstrucción de alfa).
* Registrado en `wiki/index.md`, `wiki/temas-por-cliente.md`, el tile nuevo en `presentaciones/_temas-demo/index.html` y el portal `presentaciones/index.html` (al inicio de `decksData`, con logo sin procesar copiado a `presentaciones/assets/logos/`).

## [2026-09-21] build | Financiera Comultrasan — Agente de IA Generativa para el Sistema Normativo Interno

* **Fuente:** SRS de 41 puntos ("Toma de Requerimientos - Agente IA Normativo Comultrasan.docx") + cotización ya existente en `QuoteDeveloperV2/cotizaciones/comultrasan-normativo/` (11 módulos funcionales que mapean casi 1:1 con las secciones del SRS).
* **Restricción explícita del usuario:** máximo 10 láminas. Los 11 módulos se fusionaron en bloques temáticos: Ingesta+Procesamiento (M1+M2, `.merge-split` estándar), Búsqueda Híbrida+RAG+Citación (M3+M4+M5, layout nuevo de 3 columnas `.merge-split--trio`), Omnicanal+Integración (M6+M7) y Seguridad+Telemetría+Auditoría (M8+M9+M10, también trio). El módulo M11 (Transferencia de Conocimiento) no tiene lámina propia — se condensó como una línea en la nota de la lámina de Inversión.
* **Componentes nuevos de sistema de diseño:** `.tier-wrap`/`.tier-row` (lista jerárquica compacta para la Taxonomía Normativa: 6 tipologías con código oficial y descripción), `.kpi-grid`/`.kpi-card` (tira de métricas contractuales, reutilizado también como grid de 4 estadísticas de diagnóstico con el modificador `.kpi-grid--4`), `.route-row`/`.route-tile` (4 fases de hoja de ruta en fila compacta sobre la lámina de Inversión) y `.merge-split--trio` (variante de 3 columnas de `.merge-split` para módulos que no caben en pares).
* **Inversión:** verificada contra la celda **Y122** del XLSX fuente = **$180.637.460 COP** (`Y1 ÷ 0.6`) — el PDF de "Cotización de Alcance" que la herramienta genera automáticamente trae $108.382.476 como "TOTAL", que es solo el costo base `Y1` sin el margen comercial completo; se siguió la regla de [[flujo-trabajo]] de siempre verificar `Y122` en vez de asumir el PDF ya generado. Pago 40/40/20 ($72.254.984 · $72.254.984 · $36.127.492).
* **Paleta:** reutilizada sin cambios de `comultrasan-orbit/` (teal `#0B6667` → verde/lima `#8DC63F`, derivada del logo) — mismo cliente, consistencia de marca entre sus dos proyectos de IA distintos (este es el agente normativo interno; `comultrasan-orbit/` es el agente Orbit para WhatsApp/precalificación de crédito).
* Assets del deck (logo del cliente ya recortado con reconstrucción de alfa, favicon, fuentes) copiados de `comultrasan-orbit/` y `chico/` en vez de reprocesarse desde cero, al ser reutilizables tal cual.
* Registrado en `wiki/index.md` y el portal `presentaciones/index.html` (al inicio de `decksData`). No requirió tile nuevo en `presentaciones/_temas-demo/index.html` ni entrada nueva en `wiki/temas-por-cliente.md` — la paleta Comultrasan ya estaba catalogada ahí desde `comultrasan-orbit/`.

---

## [2026-09-21] build | Unidrogas S.A. — Automatización de Contenidos y Formación con IA

* **Fuente:** un solo Excel (`FullServices NAL 2026.xlsx`) con dos hojas de cotización independientes — "Unidrogas Video" y "Unidrogas Plataforma" — presentadas en ese orden a pedido del usuario.
* **Restricción explícita del usuario:** máximo 10 láminas + validación de que ningún contenido se repitiera entre láminas. Se resolvió agrupando los 10 módulos de la Plataforma en 4 pilares conceptuales, con una lámina de "mapa de alcance" que solo lista nombres (índice) y láminas de detalle separadas que solo desarrollan descripciones — cada bullet/cifra aparece una única vez en todo el deck.
* **Inversión:** Video $27.393.825 COP · Plataforma $43.358.206 COP, ambas = `Y1 ÷ 0.7` de su hoja (este Excel usa margen 0.7, no 0.6 como QuoteDeveloperV2 — ver celdas `Y62`/`Y107`). Lámina de cierre aclara que la cifra de Video se cotiza aparte, sin repetirla.
* **Paleta:** azul `#00ADEF` → verde lima `#A6CE3A`, muestreada por píxeles del logo (2 colores puros, sin variantes intermedias) — marca 100% fría, punto "Confidencial" en ámbar por defecto.
* Registrado en `wiki/index.md`, `wiki/temas-por-cliente.md`, `presentaciones/_temas-demo/index.html` y el portal `presentaciones/index.html` (al inicio de `decksData`).

---

## [2026-09-21] ajuste | Estándar de orden más reciente primero con fecha en portal principal

* **Portal Principal (`presentaciones/index.html`):** Implementación de orden cronológico por defecto de más reciente a más antigua de arriba para abajo, visualización de fechas de desarrollo en cada tarjeta (`.badge-date` y `.meta-pill.date-pill`) y nuevo control interactivo estilizado (`.btn-sort` y menú flotante) para alternar entre "Más reciente a más antiguo" y "Más antiguo a más reciente".
* **Comportamiento del Agente (`CLAUDE.md`, `wiki/flujo-trabajo.md`, `wiki/despliegue.md`):** Actualizada la Regla 3 obligatoria del agente: toda nueva presentación debe registrarse insertándola **en la parte superior (al inicio) del arreglo `decksData` como la más reciente**, acompañada obligatoriamente de sus propiedades de fecha (`date` y `dateFormatted`).

---

## [2026-09-16] ajuste | Chico Soluciones Logísticas S.A.S. — corrección de cifra de inversión y desglose

* **Cifra de inversión corregida** a pedido explícito del usuario: el build inicial usó
  $98.699.961 (el "Total General del Proyecto" del PDF de cotización que `QuoteDeveloperV2` ya
  había generado, cifra de costo + AIU del 10%). El usuario indicó que la cifra comercial real
  es la celda **`Y122`** del XLSX fuente — equivalente a **`Y1 ÷ 0.6`** — que da
  **$143.527.149**. Corregido en la lámina de Inversión y en `wiki/index.md`. Nueva regla
  obligatoria documentada en [[flujo-trabajo]] para no repetir el error en futuros decks desde
  `QuoteDeveloperV2`: siempre verificar `Y122`/`Y1÷0.6` en el XLSX, no confiar en el total del
  PDF auto-generado.
* **Desglose por módulo retirado** a pedido del usuario: se quitó el precio individual junto a
  cada título de módulo en las 5 láminas `.merge-split` (M1-M10) y se reemplazó la cuadrícula de
  14 chips de la lámina de Inversión por **3 tarjetas de forma de pago 40/40/20**
  ($57.410.860 · $57.410.860 · $28.705.430) — componente nuevo `.inv-pay`/`.pay-tile`, CSS
  `.inv-grid`/`.inv-chip` retirado por no uso.
* **Centrado del total corregido:** el número grande de la lámina de Inversión se veía desplazado
  a la izquierda porque el `viewBox` del SVG de texto en gradiente (técnica de §5.2 de
  [[sistema-diseno]]) se había estimado a ojo con un ancho casi el doble del real (14250 vs
  8029 medido) — el texto se dibujaba centrado dentro de una caja mucho más ancha que él mismo,
  dejando espacio vacío visible a la derecha que desplazaba el glifo visualmente a la izquierda
  del centro real. Se remidieron **los 11 `viewBox` de texto en gradiente de todo el deck**
  vía `getBBox()` en el navegador (no solo el de Inversión) y se corrigieron todos a su ancho
  real medido — confirma otra vez la regla ya documentada de nunca estimar el `viewBox` a ojo
  para el build final.

---

## [2026-09-16] build | Chico Soluciones Logísticas S.A.S. — Modernización Logística y Abastecimiento Penitenciario

* Deck nuevo (**10 láminas**) construido a partir de la cotización final en PDF ya generada por
  `QuoteDeveloperV2/cotizaciones/chico-soluciones-logisticas/` (se prefirió sobre el XLSX crudo
  por traer el objetivo redactado, el alcance/fuera-de-alcance y el total con AIU ya incluido).
  Proyecto: sistema de información del modelo APP de Iniciativa Privada presentado al Ministerio
  de Justicia — canal de e-commerce controlado que sustituye el ingreso físico de encomiendas a
  la Población Privada de la Libertad (PPL), con 4 fases transversales + 10 módulos funcionales
  (E-commerce/Catálogo, Anti-Contrabando, RFID, Candados GPS, PPL Connect, INI/K9, Pagos,
  Protección de Datos, Cárceles Productivas, Reportería). Inversión **$98.699.961 COP**.
* **Plan inicial de 12 láminas bajado a 10 a pedido explícito del usuario** ("baja el número de
  láminas a 10 inteligentemente"): se fusionaron Objetivo+Alcance+Arquitectura en una sola lámina
  con diagrama de flujo (`.pipe-row` de 7 pasos, técnica reutilizada de `colbeef-flujo-ia/`) y se
  movieron las 4 Fases Transversales del proyecto al desglose de la lámina de Inversión (en vez
  de una lámina dedicada) — sin perder ningún dato real de la cotización.
* Los 10 módulos funcionales se agruparon en **5 láminas de a 2 módulos** (`.merge-split`,
  patrón de `presentaciones/giron/`) por afinidad temática: Comercio+Pagos, Anti-Contrabando+INI/K9,
  RFID+Candados GPS, PPL Connect+Protección de Datos, Cárceles Productivas+Reportería. El
  `.merge-item` base se ajustó más compacto que el de Girón (gap 5px, padding 5px/10px, texto
  7-7.9pt) tras detectar overflow real con la mitad de 5 ítems (M1) colisionando con el footer —
  el modificador `--roomy` (agrandado) se reserva para las mitades de 2 ítems.
* Paleta derivada por muestreo de píxeles del logo real (azul marino `#044378` del wordmark →
  rosa empolvado `#BC7B7F` del pin/avión de papel). **El usuario pidió explícitamente los 3 hex
  exactos del muestreo** (`#044378`/`#BC7B7F`/`#D9B3B6`) para el gradiente insignia, sin
  profundizarlos — se aplicaron literales en `--grad-brand`/`--grad-cyan`/`--grad-violet` y en
  el `<linearGradient>` SVG inline, mientras los tokens de texto (`--cyan`/`--violet`/`--magenta`)
  se mantuvieron en sus versiones AA-seguras profundizadas. Detalle en [[temas-por-cliente]].
* **Lámina de cierre rediseñada a pedido del usuario** (mostró una captura de referencia): pasó
  del layout `.cta` de 2 columnas (steps + contact-card) al layout centrado tipo portada
  `.cover--close` ya usado en `presentaciones/giron/` — badge "Próxima ventana de lanzamiento:
  ahora", título en gradiente, 3 pasos en línea con círculos numerados, statement de cierre
  narrativo (adaptado al contexto penitenciario/APP), fila de contacto y lockup de logos
  Campuslands×Chico. Primer deck de la familia `.internal`/single-scenario (no sidebar) en
  adoptar este patrón de cierre.
* **Esquinas decorativas (`.corner` tl/tr/bl/br) retiradas de portada y cierre** a pedido
  explícito del usuario — quedan solo los `.deco-rings` de fondo en ambas láminas.
* Verificación: preview en navegador lámina por lámina (balance de espacio corregido en
  `.merge-item` antes de exportar) + export a PDF (10 páginas, shell oculto correctamente) +
  lectura completa del PDF con PyMuPDF, sin hairlines ni desbordes. Registrado en `wiki/index.md`,
  `wiki/temas-por-cliente.md`, `presentaciones/_temas-demo/index.html` y el portal
  `presentaciones/index.html` (`decksData`), con el logo sin procesar copiado a
  `presentaciones/assets/logos/`.

---

## [2026-09-10] ajuste | Colbeef S.A.S. — capturas de evidencia agrandadas (legibilidad)

* El usuario reportó 5 láminas con capturas reales poco legibles (6, 7, 8, 14, 15 — antes 4, 6,
  7, 13, 14 de la numeración previa a agregar Flujo 4). Causa raíz: paneles de texto y filas de
  diagrama compitiendo por el alto de la lámina con las imágenes, más una captura angosta
  (631×98px) forzada al mismo alto que sus pares en un grid de 2 filas.
* **Componente nuevo `.step-track`:** rastreador de pasos horizontal compacto (círculos + línea,
  ~30px de alto) que reemplaza el `.pipe-row` de tarjetas completas (~90px) en las 4 láminas de
  Contingencia — libera ~60px de alto por lámina para las capturas.
* Lámina 6: la captura angosta de "datos del nuevo propietario" se movió a la lámina 5 (donde sí
  hay espacio libre bajo los chips de tags), dejando la 6 con solo 2 capturas grandes a ancho completo.
* Láminas 7 y 8: se quitó el párrafo `s-lead` (redundante con el eyebrow) y se redujo la columna
  de contexto (resultado/tags) para darle todo el ancho restante a las capturas.
* **Corrección de rebote:** al vaciar la lámina 12 (ya no tenía imagen, solo texto) quedó con
  ~50% de espacio en blanco — se agrandó la tipografía y el padding de sus dos tarjetas en vez
  de dejar espacio vacío, siguiendo la regla de balance de espacio de `wiki/sistema-diseno.md`.
* Verificado a 200dpi (resolución de impresión real) con PyMuPDF, no solo en pantalla — el texto
  de las 5 capturas es legible sin necesidad de zoom adicional en el PDF.

---

## [2026-09-10] build | Colbeef S.A.S. — Flujo Conversacional del Agente IA (18 láminas)

* **Fuente:** PDF de 16 páginas compartido inicialmente por el usuario, luego reemplazado por
  un PPTX final de 17 páginas (agregó la lámina "Flujo 4 · Despacho de Cava", ausente del PDF
  original) — el usuario pidió explícitamente mapear **cada página del fuente 1:1** a su propia
  lámina, sin consolidar, más una 18ª lámina de Cierre (patrón `presentaciones/giron/`).
* **Paleta reutilizada** sin cambios de `presentaciones/colbeef-plan-trabajo/` (rojo→verde,
  mismo cliente) — no hizo falta rederivarla del logo.
* **Evidencia real:** se extrajeron con PyMuPDF/PIL las capturas reales embebidas en el PDF/PPTX
  (WhatsApp, tabla de incidentes SIRT, emails de alerta, reporte de CAVA) y se enmarcaron con un
  componente `.evidence-card` nuevo. La lámina de Flujo 4 requirió recortar 2 capturas de una
  única imagen de página completa rasterizada (mismo patrón ya usado para Flujo 3).
* **Bug de hairline confirmado y corregido desde el build inicial:** los 17 títulos con
  `<em class="gradient-text">` (texto negro + gradiente en la misma línea) mostraron el
  recuadro/subrayado de Chrome headless documentado para otros clientes — se migró toda la
  presentación a texto en gradiente vía SVG (`<text fill="url(#gradBrand)">`), midiendo cada
  `viewBox` real con `getBBox()` en el navegador.
* **Iteración de diseño pedida por el usuario:** el resaltado "activo" de paneles y pasos
  (`.panel.active`, `.pipe-item.active`) usaba un `box-shadow` de anillo sólido — el usuario lo
  encontró "feo"; se reemplazó por tinte de fondo + sombra difusa + barra de acento más gruesa.
  Al aplicar el mismo ajuste a `.panel::before` (una barra **lateral**, no superior, a diferencia
  de `.pipe-item::before`) se generó un artefacto de esquina — corregido ajustando el `width` en
  vez del `height` del pseudo-elemento equivocado.
* **Ajuste de evidencia:** la lámina de evidencia de Flujo 2 mostraba una captura muy angosta
  (631×98px) casi ilegible dentro de una columna igual a las otras dos — se rediseñó a un layout
  de 2 tarjetas grandes + 1 franja angosta con leyenda vertical.
* Registrado en `wiki/index.md`, `presentaciones/index.html` (`decksData`) y nota de reutilización
  en `wiki/temas-por-cliente.md` — sin tile nuevo en `_temas-demo/` (paleta ya existente, no nueva).

---

## [2026-09-08] ajuste | Alcaldía Municipal de Girón — inversión total agregada: $546.000.000 COP

* **Cambio de política del deck:** desde el build inicial, este deck se construyó
  explícitamente **sin ninguna cifra de inversión** (a pedido del usuario, registrado en
  varias entradas previas de este log). El usuario pidió ahora agregar el precio total en
  la lámina 11 (Inversión y Forma de Pago) — se agrega solo ahí, el resto del deck (las 13
  propuestas individuales) sigue sin cifras, consistente con el pedido puntual.
* **Tarjeta "Inversión total"** nueva, en la columna "Pagos por hitos" (antes de los tiles
  de 40/40/20): monto grande en `$546.000.000` con "COP" en tipografía menor al lado, barra
  izquierda en `var(--blue)` a tono con el resto del sistema de acentos.
* **Desglose por hito agregado a cada `pay-tile`:** además del porcentaje, cada tile ahora
  muestra el monto exacto — 40% = $218.400.000 (anticipo), 40% = $218.400.000 (mitad de
  proyecto), 20% = $109.200.000 (entrega/go-live). Suma verificada exacta contra el total
  ($218.400.000 × 2 + $109.200.000 = $546.000.000). Los tiles se compactaron (padding
  22px→14px, número 27pt→22pt) para hacer espacio al desglose sin desbordar.
* **Verificación:** antes de agregar contenido se midió que la columna de pago solo estaba
  al 50.5% de su alto disponible (91.5px de 181.2px) — margen de sobra. Tras el agregado
  subió a 65.2%, sin desbordar (confirmado con `getBoundingClientRect`). Barrido de overflow
  automatizado sobre las 12 láminas (0 elementos desbordados) y export a PDF con revisión
  visual a 300dpi de la lámina — tarjeta de inversión total legible y bien alineada, tiles
  con el desglose correcto, sin superposiciones.

---

## [2026-09-08] ajuste | Alcaldía Municipal de Girón — botón ancho de Resumen General pegado al pie de página

* Tras revertir el rediseño con colores de la lámina 2 (a pedido del usuario, ver entrada
  anterior "revert"), volvió a quedar expuesto un defecto ya documentado en la auditoría
  original: el 7° botón (fila impar, ancho completo) quedaba **pegado directamente al pie
  de página, 0px de separación**, mientras que arriba (entre el kicker y la primera fila)
  había 17px de aire. El usuario lo señaló con una imagen de referencia señalando ese
  espacio superior como el que quería replicar abajo.
* **Causa raíz:** `.sol-grid-flat` usaba `flex:1` (se estira a ocupar todo el resto de la
  columna) combinado con `grid-auto-rows:1fr` (reparte esa altura en 4 filas iguales) — el
  grid siempre termina exactamente donde empieza el footer, sin margen posible. Peor aún:
  medido con `getBoundingClientRect`, el contenido de la fila ancha en algunos casos
  desbordaba su propio carril de `1fr` (el borde inferior del botón quedaba por debajo del
  borde inferior del propio grid), agravando el amontonamiento visual.
* **Corrección:** `flex:none` + `grid-auto-rows:min-content` (cada fila mide solo lo que
  necesita su contenido, nunca se estira ni desborda) + `margin-bottom` explícito. Como el
  alto total de la columna es fijo, fue necesario liberar espacio en otro lado para que el
  margen inferior "cupiera": se redujo el `gap` entre filas de 14px a 6px. Calibrado
  iterativamente en el navegador (medir → ajustar → volver a medir) hasta que el espacio
  libre abajo (17-18px) igualara el de arriba (17px, sin tocar el margen superior que el
  usuario ya daba por bueno).
* **Verificación:** barrido de overflow automatizado sobre las 12 láminas (0 elementos
  desbordados) y export a PDF con revisión visual a 300dpi de la lámina — el respiro debajo
  del último botón ahora se lee igual de generoso que el de arriba, sin tocar el pie de
  página.

---

## [2026-09-08] ajuste | Alcaldía Municipal de Girón — cronograma a 5 meses + 1 mes de pruebas y go-live

* El usuario pidió cambiar el cronograma de "4 meses + pruebas" a "5 meses + 1 mes de pruebas
  y go-live" (lámina 10, Equipo y Cronograma). Actualizado en 3 lugares: (1) el título en
  gradiente "Un equipo dedicado y **5 meses** de implementación" (SVG remedido con
  `getBBox()`, ancho casi idéntico al de "4 meses" — 3609 vs. 3631 unidades); (2) el
  subtítulo de la columna "5 meses + 1 mes de pruebas y go-live" (antes "4 meses +
  pruebas, por fases"); (3) la línea de tiempo, que pasa de 5 a 6 pasos — el antiguo "Mes 4"
  ("Cierre de desarrollo, integraciones finales y ajustes por secretaría") se dividió en
  **Mes 4** ("Integraciones finales y ajustes por secretaría") y **Mes 5** ("Cierre de
  desarrollo y consolidación del catálogo completo"), y el paso final se renombró a "Pruebas
  y Go-Live · 1 mes" para que la duración quede explícita igual que en los meses numerados.
  Mes 1-3 quedaron sin cambios.
* **Verificación:** con un paso adicional en la línea de tiempo, se midió que el bloque
  completo (6 pasos + nota de metodología) sigue sin desbordar — 18.4px de margen positivo
  contra el footer — y que el subtítulo nuevo (más largo) sigue en una sola línea. Barrido de
  overflow automatizado sobre la lámina confirmó 0 elementos desbordados. **A pedido
  explícito del usuario, no se regeneró el PDF en este ajuste** — el HTML/CSS desplegado
  queda actualizado, pero `giron.pdf` conserva el cronograma de 4 meses hasta el próximo
  export.

---

## [2026-09-08] ajuste | Alcaldía Municipal de Girón — soporte post go-live especificado a 1 año

* Ajuste puntual pedido por el usuario en la lámina 11 (Inversión y Forma de Pago): la nota
  de "Garantía y soporte" decía "soporte post go-live" sin plazo — se agregó "de 1 año".
  Verificado que el `note-bar` sigue en una sola línea sin desbordar (`scrollHeight ==
  clientHeight`, 1 línea) y confirmado visualmente en el PDF re-exportado.

---

## [2026-09-08] ajuste | Alcaldía Municipal de Girón — láminas 4-9 alineadas al lenguaje visual de la lámina 3

* El usuario pidió, con instrucciones muy puntuales, que las 6 láminas fusionadas (4-9)
  adoptaran el mismo lenguaje visual que la lámina 3 "Agentes IA de Correo" (su referencia
  explícita), y que se corrigiera un desbalance de tamaño entre el texto en itálica/gradiente
  de los títulos y el texto en negrita que lo rodea — en todo el deck, no solo en 4-9.
* **Insignia "Propuesta Técnica N de 07" sin estilo en 4-9:** medido con
  `getBoundingClientRect()`, en la lámina 3 el badge mide el 100% del ancho de columna (es
  hijo directo del grid `.cover__body`, que por defecto estira sus hijos — `justify-items:
  stretch` de CSS Grid); en las láminas 4-9 el mismo `<span class="sol-index">` está envuelto
  en `.merge-topline` (un div normal, sin estirar), y encima la regla que le daba fondo en
  gradiente/píldora estaba **scopeada a `.cover--sol`**, clase que esas 6 láminas no tienen —
  por eso el badge se veía como texto plano sin ningún fondo. Corregido en dos partes: (1) la
  regla base de `.sol-index` se quitó del scope de `.cover--sol` (ahora aplica a cualquier
  lámina que use la insignia); (2) se agregó `width:100%` a `.merge-topline .sol-index` para
  replicar el mismo banner de ancho completo que la lámina 3 logra por el stretch del grid.
* **Título más chico que la lámina 3:** `.merge-title` estaba en 17pt vs. los 19pt de
  `.cover--unified .cover__title` (el tamaño real de la lámina 3, no los 29pt de
  `.cover--sol` a secas — ese valor queda sobrescrito por la cascada). Igualado a 19pt.
  Verificado que ningún título fusionado (incluido el más largo, "Trámites de Ordenamiento ·
  Reparto de Querellas") pasa a 2 líneas con el tamaño nuevo (`getClientRects().length` de
  cada `<h1>` en las 12 láminas, todas en 1).
* **Subtítulos sin color:** en la lámina 3, "PLATAFORMA BASE DE AGENTES IA DE CORREO" /
  "PARAMETRIZACIÓN..." (`.sys-col-head`) llevan el acento ámbar `var(--cyan)` — confirmado
  con `getComputedStyle` que es un color sólido, no un gradiente real (`background-image:
  none`), pese a leerse como "gradiente" a simple vista. En las 6 láminas fusionadas,
  `.merge-half__title` ("Auditoría de EPS/IPS", "Salud Pública", etc.) no tenía ningún acento
  de color — texto negro plano. Igualado al mismo `var(--cyan)` sólido de la lámina 3 (mismo
  color, sin agregar un gradiente CSS real vía `background-clip:text`, que la wiki ya
  documentó como fuente de un bug de hairline en Chrome headless para textos internos —
  ver [[temas-por-cliente]] y los casos de Avicampo/Gas País Chilco).
* **Texto en gradiente/itálica visualmente más chico que el texto en negrita adyacente (en
  TODO el deck, no solo 4-9):** medido con `SVGTextElement.getBBox()` del `<text>` real
  contra un `Range.getBoundingClientRect()` de una letra mayúscula del texto vecino en la
  lámina 3 — el glifo de la palabra en gradiente ocupaba solo el 93.3% de la altura de una
  mayúscula del texto en negrita (el `viewBox` de estas SVG no está recortado al alto real de
  la tinta, así que `height:1em` deja el trazo visible más bajo de lo esperado; el menor
  contraste del dorado sobre el fondo claro —vs. negro— acentuaba aún más la sensación de
  "más chico"). Corregido con `.gt{ height:1.14em !important; }` (el `!important` es
  necesario porque cada `<svg class="gt">` trae su propio `style="height:1em"` inline, que
  gana sobre cualquier regla de hoja de estilos sin `!important`) — el mismo método de
  medición confirmó el nuevo ratio en 106.7% (antes 93.3%), y una revisión visual a zoom alto
  (`--slide-scale:1.9`) mostró "responden" (lámina 3) del mismo peso visual que "el correo"
  vecino. Al ser una regla global sobre `.gt`, corrige el mismo defecto en las 12 láminas del
  deck (Portada, Agentes de Correo, las 6 fusionadas, Equipo/Cronograma, Inversión, Cierre),
  no solo en las que el usuario señaló.
* **Espacio vacío en láminas 5 y 7 (señalado explícitamente por el usuario):** al agrandar
  título+banner de las 6 láminas fusionadas, la fila de contenido (`1fr` del grid interno)
  se achicó, y quedó en evidencia que las láminas 5 ("IVC Sanitario · Archivo de Tránsito", 5
  ítems por lado) y el lado "Comités y Actas" de la lámina 7 (5 ítems) eran las peor llenadas
  del deck (~59-61.5% del alto de columna, medido con el mismo método de `contentSpan/
  containerHeight` que en la auditoría anterior). El modificador `.merge-half--roomy`
  existente (creado para el lado de 3 ítems de la lámina 7) desborda a 5 ítems por lado —
  calculado que 5 tarjetas al tamaño de `--roomy` necesitan ~208px de alto contra los ~143-149px
  disponibles. Se creó un modificador intermedio `.merge-half--fill` (padding y tipografía
  agrandados de forma más moderada, calibrado para 5 ítems) aplicado a ambos lados de la
  lámina 5 y al lado "Comités y Actas" de la lámina 7 (el lado "Mesa de Víctimas", de 3
  ítems, ya tenía `--roomy` de la auditoría anterior y no se tocó). Resultado verificado sin
  desborde (`contentSpan > containerHeight` = false en las 12 láminas): lámina 5 sube a
  100%/96.5% de llenado, lado "Comités y Actas" de la lámina 7 sube a 100% (su vecino "Mesa
  de Víctimas" se mantiene en 69.9%, ya corregido antes — la diferencia ahora se lee como
  "muchas tarjetas chicas" vs. "pocas tarjetas grandes", un contraste editorial intencional,
  no un vacío accidental).
* **Verificación:** cambios probados primero en vivo en el navegador (con cache-busting
  explícito del CSS y recarga completa del HTML — el server estático no revalidaba el disco
  por su cuenta) sobre las láminas puntuales, luego export a PDF completo (12 páginas) y
  revisión visual página por página a 300dpi de las 12 láminas — sin desbordes, sin
  colisiones, banners/títulos/subtítulos consistentes entre la lámina 3 y las 4-9, y sin
  regresión en las láminas 1, 2, 10, 11 y 12 pese al cambio global de `.gt`. Chequeo
  automatizado adicional (`getBoundingClientRect` de cada `h1/h2/p/span/.merge-item` contra
  el borde de cada lámina) confirmó 0 elementos desbordados en las 12 láminas.

---

## [2026-09-08] ajuste | Alcaldía Municipal de Girón — auditoría visual y de consistencia integral (12 láminas)

* El usuario pidió una auditoría profesional completa del deck (no solo corregir lo evidentemente
  roto): revisar las 12 láminas una por una contra el lenguaje visual establecido, y mejorar
  cualquier oportunidad de composición/jerarquía/espaciado aunque la lámina "funcionara" a simple
  vista — sin inventar contenido, cifras ni cambiar el alcance.
* **Metodología:** lectura completa de `index.html`/`styles.css`, recorrido interactivo en
  navegador con medición programática (`getBoundingClientRect`, `getComputedStyle`) de cada
  lámina — porcentaje de llenado de cada columna/mitad, gaps antes del footer, conteo de ítems
  por par fusionado — en vez de solo juicio visual, para detectar asimetrías que no siempre saltan
  a la vista en una lámina aislada. Export a PDF (Chrome headless) y render a PNG (PyMuPDF) para
  la verificación final página por página.
* **Hallazgo principal — inconsistencia entre láminas antiguas y nuevas:** las 6 láminas
  fusionadas (`cover--merge`, láminas 4-9, agregadas en el pase de fusión del 2026-09-09) usaban
  un `<h1 class="merge-title">` de color sólido plano, mientras que **todas** las demás láminas de
  contenido del deck (Portada, Agentes de Correo, Equipo/Cronograma, Inversión, Cierre) destacan
  una palabra o frase clave del título con el gradiente de marca (`.gt` + SVG). Las 6 fusionadas
  eran las únicas que rompían ese lenguaje — se sentían "de otra presentación". Corregido:
  se agregó el mismo tratamiento de gradiente a la palabra/frase principal de cada título fusionado
  ("Salud", "IVC Sanitario", "Cobro Coactivo", "Comités y Actas", "Procesos Disciplinarios",
  "Trámites de Ordenamiento"), midiendo el ancho real del texto con `SVGTextElement.getBBox()`
  (mismo método ya documentado para este deck) antes de fijar el `viewBox`.
* **Hallazgo — espacio vacío desbalanceado:** medido el % de llenado de cada mitad de las 6
  láminas fusionadas, la lámina "Comités y Actas · Mesa de Víctimas" tenía el peor desbalance del
  deck (60% vs. 31% de llenado entre sus dos mitades, por la diferencia de 5 vs. 3 ítems — el
  `align-items:stretch` de `.merge-split` iguala el ALTO del contenedor pero no el peso visual del
  contenido). Y la lámina "Secretaría de Salud" (4 vs. 4 ítems) tenía ambas mitades parejas pero
  igual de vacías (~42%), la segunda peor densidad del deck. Se agregó un modificador
  `.merge-half--roomy` (tarjetas más grandes: padding, tipografía y separación mayores) aplicado
  a las mitades con pocos ítems — Mesa de Víctimas quedó en 68% de llenado (ahora más lleno que su
  vecina) y ambas mitades de Secretaría de Salud subieron a niveles pareja al resto del deck.
* **Hallazgo — chips del Resumen General con relleno interno excesivo:** cada tarjeta de
  navegación de la lámina 2 tenía solo 32px de contenido real (icono+texto) dentro de una fila de
  93px (~65% de espacio vacío), porque `grid-auto-rows:1fr` estira las filas para llenar la
  lámina pero no el contenido de cada una. Se agrandó el ícono, la tipografía y el padding del
  chip para que su propio contenido pese más dentro de la fila, en vez de dejarlo flotando.
* **Hallazgo — grid de equipo con ítem huérfano:** 9 roles en un grid de 2 columnas dejaban el 9º
  chip ("Implementación & Capacitación") solo en la última fila, con la mitad derecha vacía —
  se sentía colocado arbitrariamente. Cambiado a grid de 3 columnas (3×3 exacto, sin huecos) con
  las tarjetas reformateadas a ícono-arriba/texto-abajo para que quepan cómodas en el ancho menor.
* **Hallazgo — lámina de Inversión y Forma de Pago subllenada:** checklist y tiles de pago 40/40/20
  ocupaban solo ~31-35% del alto de columna disponible (la más vacía del deck junto con Mesa de
  Víctimas antes de su fix). Se agrandaron los íconos de check, la tipografía del checklist y los
  números de los tiles de pago — quedó en ~50-59% de llenado, en línea con el resto del cierre.
* **Sin hallazgos en:** logos/proporciones (sin deformación en ninguna lámina), z-index/overflow
  (0 elementos desbordando el borde de lámina fuera de la decoración de anillos, que está pensada
  para clip parcial), consola sin errores, numeración de páginas y footers consistentes en las 12
  láminas, contraste de color, y el bookend de esquinas (`.corner`) en Portada/Cierre — confirmado
  intencional (no aplica a las láminas interiores) tras revisar el HTML de las 12 láminas.
* **Verificación final:** export a PDF (12 páginas) renderizado a PNG a 300dpi (PyMuPDF) y
  revisado lámina por lámina — sin desbordes, sin colisiones, gradientes correctos, balance visual
  parejo entre columnas en las 6 láminas fusionadas. Segunda pasada tras los fixes confirmó que
  ningún ajuste introdujo una regresión en las láminas ya correctas (1, 3, 5, 6, 8, 9, 12).

---

## [2026-09-09] ajuste | Alcaldía Municipal de Girón — fusión de 12 propuestas en 6 láminas (18→12 láminas)

* El usuario pidió una unificación grande y estricta: (1) eliminar 3 frases/ítems puntuales del
  contenido; (2) fusionar 12 de las 13 propuestas técnicas de a 2 por lámina, dividiendo cada
  lámina en mitad izquierda/mitad derecha (una propuesta por lado); (3) reordenar el deck
  completo. Solo Agentes de Correo queda como lámina individual.
* **Contenido eliminado:** "Código fuente 100% propiedad de la Alcaldía de Girón" (checklist de
  la lámina de inversión), "— sin ninguna cifra de inversión visible aquí" (kicker de Agentes de
  Correo) y "Cada una de las siguientes propuestas es una presentación independiente, con su
  propia portada" (kicker del Resumen General, reescrito de todas formas por la fusión).
* **6 pares fusionados** (nombre del apartado resultante entre paréntesis cuando el usuario dio
  uno explícito; si no, se unieron ambos nombres con "·"): Auditoría EPS/IPS + Salud Pública
  (**Secretaría de Salud** — nombre fijo dado por el usuario, no una unión de nombres); IVC
  Sanitario + Archivo de Tránsito; Cobro Coactivo + Gestión Documental; Comités y Actas + Mesa de
  Víctimas; Procesos Disciplinarios + Estampillas Digitales; Trámites de Ordenamiento + Reparto
  de Querellas. Orden final: Resumen General → Agentes de Correo → los 6 pares (en el orden que
  dio el usuario) → Equipo/Cronograma → Inversión/Pago → Cierre/Contacto = **12 láminas** (más la
  portada, sin nav, igual que antes).
* **Patrón nuevo `.cover--merge` / `.merge-split`:** a diferencia de `.sys-split` (que asume un
  único título de lámina para 2 subsistemas de la MISMA propuesta), cada `.merge-half` es una
  propuesta autónoma con su propio título, lead, lista de módulos (formato compacto título+desc
  en una sola línea, "— " como separador) y meta (dependencia · sistemas · módulos). El contenido
  original de cada propuesta se condensó a frases de 3-6 palabras por ítem para que hasta el par
  más denso (7 módulos por lado, Trámites de Ordenamiento + Reparto de Querellas) quepa sin
  desbordar. `.merge-split` es un grid de 2 columnas con `align-items:stretch` (default): ambas
  mitades quedan siempre exactamente a la misma altura sin necesitar subgrid, y cada `.merge-list`
  centra su propio contenido con `justify-content:center` — así una mitad de 3 ítems (Mesa de
  Víctimas) y su vecina de 5 (Comités y Actas) quedan con el mismo espaciado uniforme en vez de
  alturas dispares.
* **Verificación milimétrica** (pedida explícitamente por el usuario — "perfeccionista, detallista,
  milimétrico"): con `getBoundingClientRect()` en las 6 láminas fusionadas se confirmó que (a) el
  título fusionado mide siempre exactamente 25.5px de alto (1 línea, sin excepción, incluso el más
  largo: "Trámites de Ordenamiento · Reparto de Querellas"); (b) `.merge-split` arranca siempre en
  el mismo y=215.1px con la misma altura 382.8px en las 6 láminas; (c) ambas mitades de cada par
  miden el mismo rect exacto (mismo y/height), incluso el par más asimétrico (5 vs. 3 ítems); (d)
  barrido de las 12 láminas confirmó cero desbordes — el contenido más bajo de cada lámina siempre
  queda 23-29px por encima del borde inferior real. Un bug real detectado y corregido en el
  camino: la lámina de Agentes de Correo quedó con el badge "Propuesta Técnica 01 de **13**" sin
  actualizar (residuo de la limpieza de categorías) — debía decir "de 07"; se corrigió tras
  revisar las 12 láminas una por una en vez de confiar en las primeras que se vieron bien.
* **Resumen General reestructurado:** las 3 categorías (Gobierno y Justicia / Atención y Trámites
  / Salud y Bienestar) ya no aplicaban limpio a los pares fusionados — casi todos cruzan
  categorías (ej. IVC Sanitario —Salud— se fusiona con Archivo de Tránsito —Atención—). Se le
  preguntó al usuario y eligió **lista plana sin categorías**: grid de 2 columnas con las 7
  tarjetas en el orden final, sin agrupación temática. El 7º ítem (impar) usa
  `grid-column:1/-1` para ocupar el ancho completo de su fila en vez de dejar una mitad vacía.
* Actualizado en los 3 lugares de la Regla 3: `wiki/index.md`, `presentaciones/index.html`
  (`decksData.giron.slides` "18 Láminas" → "12 Láminas" + descripción). PDF re-exportado (12
  páginas verificadas con PyMuPDF) y las 12 láminas revisadas visualmente una por una (navegador +
  PDF) antes de entregar.

---

## [2026-09-08] ajuste | Miami Aqua Tours (Tracking) — lámina de Inversión simplificada a USD 9.000

* A pedido del usuario, se ajustó la lámina "06 · Inversión" (página 7) de
  `presentaciones/miami-aqua-tracking/`: se retiró el precio individual de cada uno de los 6
  módulos/renglones (`.mc-value`) dejando solo el nombre; se retiró el monto en dólares de cada
  una de las 3 tarjetas del plan de pago 40/40/20 (`.plan-card .info b`) dejando solo el
  porcentaje y la descripción, y se redujo su padding vertical (`.14in`→`.1in`) para compensar
  la altura sobrante; se agregó espacio entre el título y el primer renglón
  (`.invest-wrap{margin-top:.06in→.3in}`); y el total pasó de **$30.744.516,44 COP** a
  **USD $9.000** (cifra nueva provista por el usuario, sin desglose por módulo visible).
* Verificado en navegador (shell de una lámina) y en el PDF reexportado (10 páginas, sin cambio
  de conteo) — el `@media print` no se tocó.
* **Follow-up mismo día:** el usuario pidió mejorar el color del total (`.invest__num .big`,
  naranja plano `var(--blue)`, poco visible sobre la tarjeta clara) y agrandarlo. Se reemplazó el
  `<div>` de texto plano por un `<svg class="gt">` con `fill="url(#gradBrand)"` — mismo patrón ya
  usado en los títulos de este deck (ver §5.2 de [[sistema-diseno]], SVG en vez de
  `background-clip:text` para evitar el hairline al exportar a PDF) — con el ancho del `viewBox`
  medido en vivo vía `getBBox()` (5832px para "USD $9,000" a `font:900 1000px 'Playfair
  Display'`), y se subió el tamaño de `.big` de `26pt` a `36pt`. Verificado sin overflow ni
  colisión con el resto de la tarjeta, en navegador y en el PDF reexportado.

---

## [2026-09-08] ajuste | Alcaldía Municipal de Girón — 3 láminas de cierre (15→18 láminas)

* El usuario pidió 3 láminas nuevas al final del deck de Girón, combinando el contenido de 4
  imágenes de referencia de una propuesta antigua de **otro cliente** (Unidrogas): Equipo del
  Proyecto + Cronograma → lámina 16; Inversión + Forma de Pago y Garantía → lámina 17; Cuándo
  Empezamos → lámina 18 (contacto). El contenido específico de Unidrogas (ERP Maía, fases de
  ingesta/OCR/simulador de arriendos) no aplicaba a Girón (catálogo de 13 soluciones
  municipales distintas) — se generalizó la redacción al alcance de Girón manteniendo la
  misma estructura y cantidad de ítems pedida, y se confirmó el plan con el usuario antes de
  construir (regla obligatoria del esquema).
* **Lámina 16:** `sys-split` de 2 columnas — equipo (grid 2×5 de 9 roles con monograma en
  gradiente oro/bronce + nota "Modelo Campers") y cronograma (timeline vertical de 5 fases).
  Cronograma cambiado de 3.5 a **4 meses + pruebas** a pedido explícito del usuario (Mes 1-4 +
  fase de "Pruebas y Go-Live" separada, en vez de "Mes 4 · 1ª quinc." + "2 sem. finales").
* **Lámina 17:** checklist de alcance (6 ítems) + tiles de pago 40/40/20 + nota de garantía y
  soporte. **Sin ninguna cifra de inversión**, a pedido explícito del usuario.
* **Lámina 18:** estilo portada centrada (como la lámina 1) con 3 pasos, frase de cierre y
  contacto **actualizado** — el de las imágenes de referencia era de una representante
  anterior; se usó el contacto vigente encontrado en la wiki (**Gabriela Pedraza Rueda**,
  Directora Full Service Global, gabriela.pedraza@campuslands.com, +57 300 302 8555, ya usado
  en otros decks recientes) en vez del de la referencia.
* **Bug de CSS Grid resuelto:** `.sys-col` usa `grid-template-rows:subgrid` con 3 filas fijas
  (título/subtítulo/contenido). Las columnas de las láminas 16 y 17 necesitaban **2** bloques
  en la fila de contenido (timeline+nota / tiles+nota) — como hijos directos sueltos, el 2º
  bloque caía en una fila implícita del grid que se dibujaba **encima** del 1º (el texto
  existía en el DOM, con `getBoundingClientRect()` correcto, pero visualmente tapado — se
  diagnosticó con `elementFromPoint()`, que reveló el `.note-bar` cubriendo el timeline). Se
  resolvió envolviendo ambos bloques en un contenedor único `.sys-col-fill` (flex column con
  `margin:auto 0`), que ocupa la fila de contenido como un solo ítem de grid.
* **Ancho de gradiente SVG medido, no estimado:** el patrón `<svg class="gt"><text
  fill="url(#gradBrand)">` de este deck requiere que el `viewBox` width coincida con el ancho
  real del texto a `font-size:1000px`. Un primer intento a ojo dejó el "?" de "¿Cuándo
  empezamos?" superpuesto sobre la "s" final. Se corrigió midiendo el ancho real con
  `SVGTextElement.getBBox()` en el navegador (con la fuente ya cargada vía
  `document.fonts.load()`) — el mismo método, aplicado a un texto ya existente en el deck como
  control, reprodujo su viewBox width original con menos de 1% de error. Método reusable para
  cualquier gradiente-texto nuevo con este patrón, en este u otros decks.
* Actualizado en los 3 lugares de la Regla 3: `wiki/index.md` (15→18 láminas + nota de esta
  optimización), `presentaciones/index.html` (`decksData.giron.slides` "15 Láminas" → "18
  Láminas" + descripción). No aplica `_temas-demo/` ni `temas-por-cliente.md` (mismo cliente,
  sin paleta nueva). PDF re-exportado (18 páginas verificadas con PyMuPDF) y verificado
  visualmente en navegador + PDF antes de entregar.

---

## [2026-09-07] ajuste | Alcaldía Municipal de Girón — optimización a 15 láminas (portada+contenido fusionados)

* El usuario pidió reducir el conteo de láminas ("28 puede ser un número exagerado para el
  alcalde"): cada una de las 13 propuestas pasa de 2 láminas (portada + contenido) a **1
  sola**, excepto el apartado 1 "Resumen General" que se deja intacto con sus 2 láminas.
  Reglas aplicadas a las 13: (1) se parte de la Hoja 1 (portada) como base; (2) se quitan las
  4 esquinas decorativas (`.corner`) para ganar espacio; (3) el título se sube (ya no
  centrado verticalmente, ahora anclado arriba); (4) el contenido real de la Hoja 2
  (`sys-split`/`mod-grid`, con su explicación corta por ítem) se inserta bajo el kicker; (5)
  se quita el bloque "Para [logo Girón]"; (6) se compacta todo (título 16.5pt, badge/kicker
  más chicos) para que quepa junto al contenido sin sobreposición.
* Renumeración de 28→15 láminas hecha con un **script Python** (no a mano): extrae cada
  bloque `<div class="slide">` vía regex por indentación exacta (cuidado: el primer slide
  tenía `class="slide active"`, no `class="slide"` a secas — el patrón inicial lo saltaba y
  fusionaba por error los slides 1 y 2 en un solo bloque; se corrigió a
  `class="slide[^"]*"`), fusiona cada par portada+contenido, y remapea `data-nav`/`goToSlide()`
  restantes con la fórmula `nuevo = (viejo+3)/2`.
* **Vacío de espacio en 2 secciones (Agentes de Correo, Comités y Actas):** ambas tienen una
  columna con una sola tarjeta/panel (`sect-panel`/`highlight-card`) frente a una lista de 3-4
  tarjetas en la columna vecina. El patrón usual (`flex:1`+`justify-content:center` para
  centrar el panel dentro de la altura estirada de la columna) se probó, con `margin:auto`
  como alternativa, y con `grid-template-rows:auto auto auto 1fr` en vez de flex anidado — las
  tres variantes se veían bien en el navegador (pantalla) pero el **PDF exportado con Chrome
  headless seguía mostrando el contenido pegado arriba con un vacío grande abajo**: se
  confirmó que el motor de layout de impresión resuelve el alto disponible de una cadena
  `flex:1` anidada en 3-4 niveles distinto que en pantalla. Se resolvió con un **`min-height`
  fijo** (2.3in) en `.highlight-card`/`.sect-panel` dentro del scope `.cover--unified` — un
  cálculo autocontenido que no depende de que el ancestro reparta espacio sobrante, y por
  tanto es igual en pantalla y en PDF. **Lección para futuros decks:** si una lámina se ve
  bien en el navegador pero mal en el PDF exportado (o viceversa), sospechar de cadenas largas
  de `flex:1`/`margin:auto` anidadas — Chrome headless en modo impresión no siempre las
  resuelve igual que en pantalla.
* Reverificado sin superposiciones ni desbordes de texto en las 15 láminas (chequeo
  automatizado) y lectura visual completa del PDF de 15 páginas (3 rondas de export/revisión
  hasta confirmar el fix del min-height).

---

## [2026-09-07] ajuste | Alcaldía Municipal de Girón — portada del resumen, sidebar reordenado, indicador animado (28 láminas)

* Tras el build inicial de 27 láminas (ver entrada anterior), el usuario pidió 4 ajustes:
  (1) que la lámina de apertura fuera una **portada real** con los logos Campuslands y Girón
  en grande (antes el resumen y la portada compartían una sola lámina, sin lockup de logos);
  (2) **reordenar el sidebar** para que siga el orden real de navegación (se abandonó el
  agrupado por 3 categorías temáticas, que saltaba de la lámina 8 a la 12 a la 24 dentro de un
  mismo grupo — confuso al navegar); (3) **agrandar el logo de Girón** en las 13 portadas de
  cotización (`.cover__client-logo` de 38px a 66px de alto); (4) **animar el indicador de
  selección** del sidebar con una pastilla deslizante en vez de un cambio de fondo instantáneo
  por clase.
* Se separó la lámina 1 en dos: **portada pura** (`.cover--main`, lockup de logos Campuslands ×
  Girón a distinta altura — 42px vs 84px, porque el escudo de Girón es vertical y necesita más
  alto para pesar visualmente igual que el wordmark horizontal de Campuslands) y **resumen/índice**
  (`.cover--index`, con footer de página en vez de la fila de metadatos, que se mudó a la portada).
  Deck completo ahora en **28 láminas**; todos los `data-slide`/`data-nav`/`goToSlide()`/números
  de página del footer se renumeraron +1 con un script (no a mano, para evitar errores).
* **Indicador deslizante:** `#navIndicator`, un `div` `position:absolute` dentro de
  `.sidebar-nav` con `transition` en `transform`/`height`/`opacity`, reposicionado por
  `moveNavIndicator()` en cada navegación y también al expandir/colapsar el sidebar (el colapso
  oculta las etiquetas de grupo y reacomoda los items de inmediato, sin transición propia, así
  que la pastilla se recalcula sin esperar). Patrón adaptado del `.scenario-pill` horizontal de
  Marval a una lista vertical.
* Reverificado sin superposiciones de texto en las 28 láminas (chequeo automatizado) y lectura
  visual del PDF de 28 páginas.

---

## [2026-09-07] build | Alcaldía Municipal de Girón, Santander — 13 Soluciones de IA (27 láminas)

* **Nuevo deck** `presentaciones/giron/` construido a partir de un Excel de cotización con
  **13 hojas** (una por proyecto), del que se extrajo únicamente la jerarquía de alcance
  (módulo → submódulo → funcionalidad) de cada hoja — **sin ninguna cifra de inversión, hora o
  tarifa** en toda la presentación, a pedido explícito del usuario. 13 proyectos: Agentes IA de
  Correo + parametrización por 7 secretarías, Archivo de Tránsito + Notificación de Comparendos,
  Auditoría EPS/IPS, Cobro Coactivo + Alertas de Prescripción, Comités/Actas + Comités Sociales,
  Disciplinarios + Audiencias Virtuales, Estampillas + Actos Administrativos, Gestión Documental,
  IVC Sanitario, Mesa de Víctimas, Ordenamiento + Asistente Normativo IA, Reparto de Querellas +
  Orientación Comisarías de Familia, Salud Pública.
* **Rumbo nuevo pedido por el usuario:** shell de **barra lateral izquierda retráctil** (icon-rail
  ↔ expandida, con transición de ancho animada) en vez del switch de escenarios en la barra
  superior — agrupa las 13 propuestas en 3 bloques temáticos (Gobierno y Justicia · Atención
  Ciudadana y Trámites · Salud y Bienestar) más "Resumen General", saltando a la **portada** de
  cada una. Se sumó una **barra inferior de prev/next + progreso** para moverse entre la portada y
  el contenido de una misma solución. El PDF exporta las 27 láminas a tamaño físico completo, con
  sidebar/header/barra inferior ocultos en `@media print`, igual que el resto de la familia de
  shells (ver [[sistema-diseno]] §6).
* **Corrección de estructura pedida por el usuario a mitad del build:** el primer borrador trataba
  cada una de las 13 cotizaciones como **una sola lámina de contenido, sin portada** — el usuario
  señaló que "cada cotización es una presentación individual" y "como se sabe cada una debe tener
  portada". Se rehizo la estructura a **27 láminas** = 1 resumen + 13 pares (portada + contenido),
  cada portada con su propio título en gradiente, kicker, cliente y meta de 3 columnas
  (Dependencia · Sistemas incluidos · Módulos cubiertos) — variante `.cover--sol` en
  `styles.css`. Todos los enlaces del sidebar y de los chips del resumen se renumeraron a la
  portada de cada solución.
* **Experimento de tipografía descartado el mismo día:** se probó **Poppins como fuente única**
  (display + labels + cuerpo) a pedido inicial del usuario; minutos después el mismo usuario pidió
  volver a las fuentes de siempre. El deck final usa el **estándar v2 sin cambios**: Playfair
  Display (títulos, con texto en gradiente vía SVG) + Montserrat (labels/eyebrows) + Poppins
  (cuerpo) — ver nota en [[sistema-diseno]] §1. Los 27 `viewBox` de los títulos en gradiente se
  remidieron con `getBBox()` real dos veces (una por cada cambio de fuente), nunca estimados.
* **Paleta propia oro brillante → bronce oscuro**, derivada del escudo heráldico monocromático del
  municipio (`#B8903A` dominante); acento "Confidencial" en azul institucional frío `#0E5C8A` por
  ser marca cálida. Registrada en [[temas-por-cliente]] y en el tile de `_temas-demo/index.html`.
* **Bug de balance de espacio corregido antes de entregar** (ver §5.1 de [[sistema-diseno]]): la
  lámina de Mesa de Víctimas (3 módulos, una sola fila) dejaba ~40% de la lámina vacía debajo de
  las tarjetas — se agrandaron tarjetas/íconos/tipografía y se añadieron tags de resumen por
  tarjeta (clase `.mod-card--lg`, modificador `.roomy`) en vez de dejar el espacio sin diseñar.
* **Bug de superposición de texto corregido antes de entregar:** en la lámina de Resumen, la
  columna de 5 cotizaciones (Atención Ciudadana y Trámites, la más larga de las 3) desbordaba
  ~68px sobre la fila de metadatos inferior ("Preparado por"/"Fecha"), y las columnas de 4
  desbordaban ~21px — invisible al ojo en una revisión rápida pero confirmado por
  `getBoundingClientRect()`. Se corrigió reduciendo tipografía/padding de los chips y del
  encabezado de categoría, y liberando espacio vertical en el título/kicker/padding de la
  portada, hasta que las 3 columnas terminan exactamente alineadas con aire limpio antes del
  footer. Verificado con un chequeo automatizado de colisión de cajas de texto sobre las 27
  láminas (0 solapamientos, repetido tras el cambio de portadas y tras el cambio de fuente) además
  de la lectura visual del PDF completo.
* Registrado en `wiki/index.md`, `wiki/temas-por-cliente.md`, `presentaciones/_temas-demo/` y el
  portal `presentaciones/index.html` (`decksData`, id `giron`), más el logo sin procesar en
  `presentaciones/assets/logos/Alcaldia de Giron.png`.

---

## [2026-09-04] build | Miami Aqua Tours — Tracking, Atribución y Optimización del Sitio (10 láminas)

* **Nuevo deck** `presentaciones/miami-aqua-tracking/` (**10 láminas**, comprimido desde un plan
  inicial de 13 a pedido explícito del usuario), construido a partir de un documento de análisis
  técnico (`analisis-miami-aqua-tours (1).pdf`) sobre tracking, atribución de campañas, rendimiento,
  seguridad y frontend del sitio estático de Miami Aqua Tours (Cloudflare Pages + widget embebido de
  Bókun, GA4 directo sin GTM, viabilidad de AnyTrack) — **deck nuevo, sin relación temática** con
  `presentaciones/miami-aqua-tours/` y `miami-aqua-tours-ampliado/` (propuestas de reservas ya
  existentes, tematizadas con la paleta cian/violeta *default* de Campuslands por ser previas a la
  regla de paleta-por-cliente).
* Precios tomados de una segunda fuente aparte (`Cotizacion.xlsx`, hoja "Plantilla" de la herramienta
  de cotización): **5 módulos específicos del proyecto** (Auditoría Técnica y Unificación de
  Arquitectura, Mejoras de Frontend y UX, Rendimiento y Velocidad, Seguridad y Buenas Prácticas,
  Analítica y Tracking de Conversiones) más una categoría genérica de "Estructura y Coordinación del
  Proyecto" que la herramienta agrega a todo proyecto — **inversión $30.744.516,44 COP**, verificada
  exactamente sumando los 9 renglones de módulo contra el total de la hoja. Forma de pago 40/40/20 a
  pedido del usuario (la hoja no la traía).
* Paleta propia **naranja del isotipo/script "Miami" → azul aqua del wordmark "AQUA"/olas**, extraída
  por muestreo de píxeles del PNG (`#E0780A`→`#3C96C8`, anclas `#FFA94D`→`#1B4F6E`) — narrativa
  "atardecer de Miami → océano aqua". Marca mixta (cálido+frío) → punto confidencial en azul
  profundo. Ver bloque completo en [[temas-por-cliente]].
* **Bug de gradiente SVG detectado y corregido en vivo:** las estimaciones iniciales de `viewBox`
  width (heurística ~500–535px/carácter) dejaron uno de los títulos ("cinco frentes") sin llegar al
  tono azul final del gradiente — el viewBox estaba sobredimensionado ~700px respecto al ancho real
  del glifo, así el degradado (0–100% del viewBox) se cortaba antes de tiempo. Se corrigió midiendo
  `getBBox().width` real de las 10 láminas en el navegador (con `document.fonts.ready` y las láminas
  temporalmente visibles) y reemplazando cada `viewBox` por el ancho medido — confirma que la regla ya
  documentada para FCV (medir siempre en vivo, nunca estimar a ojo) aplica también al build inicial,
  no solo a la depuración de un bug ya detectado.
* Registrado en los tres lugares obligatorios: [[index]], catálogo de [[temas-por-cliente]] +
  `presentaciones/_temas-demo/index.html`, y el portal `presentaciones/index.html` (`decksData`).

## [2026-09-01] build | Marval S.A.S. — Fase 1 (Proyecto A: Agente de IA · Proyecto B: Intranet Corporativa)

* **Nuevo deck** `presentaciones/marval-fase1/` (**9+9 láminas**), construido a partir de dos
  propuestas técnicas fuente distintas (`Propuesta_Tecnica_Agente_de_IA_Marval_Fase_1.pdf` y
  `Propuesta_Tecnica_Intranet_Corporativa_Marval.pdf`) que documentan **dos proyectos
  independientes** confirmados en sesión técnica del 21 de agosto de 2026 (arquitectura,
  infraestructura y cronograma propios, cotizados por separado) — distinto del deck ya existente
  `presentaciones/marval/` (Ecosistema de Agentes de IA con Escenario A/B = motor externo vs.
  self-hosted, con precios). Este deck nuevo usa el mismo shell con switch, mapeando
  **Proyecto A = Agente de IA "Marvia"** (Fase 1, alcance acotado a Entregas Digitales en
  Microsoft Teams: OTP, actas/novedades en CRM, RAG sobre Zoho Learn + Oracle/SOHO CRM,
  comparativa Azure OpenAI vs. modelos locales) y **Proyecto B = Intranet Corporativa** (MVP,
  SSO obligatorio con Microsoft Entra ID, 7 módulos informativos, CMS por dominios, sin
  trámites transaccionales en esta fase). **A pedido explícito del usuario, el selector de la
  barra superior se llama "Proyecto A/B" en vez de "Escenario A/B"** (los identificadores
  internos `data-scenario`/`switchScenario()` no cambiaron, solo el texto visible). **Sin
  ninguna cifra de inversión en ninguna lámina** (instrucción explícita del usuario). Reutiliza
  la paleta Marval ya derivada del logo en [[temas-por-cliente]] (azul claro → corporativo →
  marino), sin retematizar. **Nota técnica:** se detectó el hairline de `background-clip:text`
  (bug documentado en [[sistema-diseno]] §5.2) en el título de portada pese a estar en línea
  aislada; se corrigió con la técnica SVG estándar (texto medido vía `getBBox()` en el navegador
  en vez de valores hardcodeados). Exportado a **dos PDFs** (`marval-fase1-proyecto-a.pdf`,
  `marval-fase1-proyecto-b.pdf`, 9 páginas cada uno) vía `?escenario=a|b`.

---

## [2026-08-26] marca | Shell interactivo obligatorio (Web) — una lámina a la vez + retematizado de FCV

* **Regla nueva, a pedido del usuario:** toda presentación **web** se entrega desde ahora dentro
  de un shell de navegación de una sola lámina a la vez (no scroll vertical apilado), calcado del
  patrón ya usado en `presentaciones/marval/`: barra superior (logos Campuslands+cliente ·
  switch de escenario solo si hay 2+ · badge Confidencial coloreado al cliente), lámina centrada
  con sombra que la separa del fondo, barra inferior (flecha atrás · indicador N/total + barra de
  progreso + play/pausa de autoplay · flecha adelante). **No afecta el PDF** — `@media print`
  oculta el shell por completo y cada `.slide` vuelve a su tamaño físico secuencial, igual que
  antes de tenerlo. Documentado en `CLAUDE.md` (nueva sección "Shell interactivo obligatorio")
  y en `wiki/sistema-diseno.md` §6 (snippets HTML/CSS/JS reutilizables, con y sin switch).
* **Bug de nombres de clase evitado:** el `.badge-confidential` de la portada (texto+punto,
  sin fondo) y el nuevo `.badge-confidential` de la barra superior (pill con fondo/borde) NO
  pueden compartir nombre — el de portada se renombró a `.cover-badge-confidential` en el CSS y
  el HTML de FCV para no chocar. Aplicar el mismo renombrado en cualquier deck existente al que
  se le agregue el shell.
* **Confidencial con el color del cliente sin token nuevo:** el badge de la barra superior usa
  `color-mix(in srgb, var(--dot-confidential) 10%/28%, transparent)` para el fondo/borde del
  pill, en vez de un `rgba(...)` hardcodeado por cliente (como hacía `presentaciones/marval/`)
  — generaliza a cualquier paleta sin tocar el contrato de tokens de [[temas-por-cliente]].
* **Retematizado de `presentaciones/fcv/`** (deck registrado ayer) al nuevo shell: HTML
  reestructurado (`<section class="slide …">` → `<div class="slide" data-slide="N"><div
  class="slide-inner …">`, envuelto en `.app-header`/`.app-content`/`.slides-footer-controls`),
  `script.js` nuevo (30 líneas, sin lógica de escenario — FCV tiene uno solo) y ajustes de CSS
  (`.slide`/`.glow-a/b` originales pasan a `.slide-inner`/`.slide-inner.glow-a/b`; `.slide` nuevo
  es el wrapper de paginación con `zoom`/`display:none↔active`).
* **Verificación:** sin captura de navegador disponible esta sesión (Browser pane no desplegado),
  se verificó por DOM/JS — 1 sola `.slide` visible a la vez, gaps simétricos (295px) entre
  header/lámina y lámina/footer, lámina centrada (offset 0px), `navigateSlide`/`toggleAutoplay`
  funcionando — y por PDF: reexportado, **8 páginas** (idéntico conteo), comparación visual
  página por página contra la versión previa **sin diferencias** (sin rastro del shell).
* **Comportamiento nuevo, también a pedido del usuario:** de ahora en adelante, terminado el
  build/ajuste de un deck, se corre `git add . && git commit -m "feat: <Nombre Comercial>" &&
  git push` dentro de `presentaciones/` (su propio repo Git — seguro para `add .` ahí, ya que ese
  repo no contiene nada de `QuoteDeveloperV2/`). Para el repo raíz (`wiki/*.md`, `CLAUDE.md`)
  se mantiene `git add` de archivos puntuales, nunca `.`/`-A` — ver `wiki/despliegue.md` §4.

## [2026-08-26] build | Fundación Cardiovascular de Colombia (FCV) — Desarrollo de Software Especializado (8 láminas)

* **Cliente nuevo, deck atípico a propósito.** El usuario pidió construir una propuesta a partir de
  un brief de 3 secciones (Resumen Ejecutivo, Perfil del Desarrollador, Modalidad de Contratación)
  para una **bolsa de horas de desarrollo con perfiles mixtos** (Full-Stack + Ciberseguridad + IA)
  aplicados a proyectos del sector cardiovascular — señalando explícitamente que "se sale de los
  estándares/reglas que tenemos estipulados" (sin módulos con precio, sin cronograma, sin cifras
  de tarifa pese a que la sección 3 se titulaba "...y Tarifas"). Se construyó **fiel al contenido
  dado, sin inventar cifras**: la lámina 6 quedó titulada solo "Modalidad de Contratación" (se quitó
  el "y Tarifas" del título) y desarrollada de forma cualitativa, con una nota transparente
  ("Tarifas: la tarifa por hora y el tope mensual de la bolsa se definen junto con FCV, según el
  perfil y el alcance") en vez de simular una cifra o dejar la sección vacía. El resto del flujo
  obligatorio del `CLAUDE.md` (paleta del logo, plan confirmado antes de construir, `<head>`
  obligatorio, PDF + Vercel) sí se siguió sin excepción.
* **Cliente y logo:** el usuario proveyó el nombre (Fundación Cardiovascular de Colombia) y el
  logo (`recursos/FCV.png`, isotipo de árbol/corazón multicolor) en un mensaje posterior de
  interrupción, antes de que se presentara el plan. `<title>` = razón social completa tal como la
  dio el usuario (sin sufijo legal adicional, es una Fundación).
* **Paleta propia — la más diversa tematizada hasta ahora:** el logo trae **6 colores reales**
  (teal `#009CB4`, verde `#78B448`, dorado `#F0A830`, magenta `#E43084`, burdeos `#901830`, navy
  `#243078`, extraídos por muestreo de píxeles con Pillow, no a ojo). En vez de usarlos como
  arcoíris plano (rompería el tono "sofisticado" de marca), se narraron como **"cuidado clínico →
  vida → energía → corazón"**: `--grad-brand` recorre teal→verde→dorado→magenta; el burdeos quedó
  como ancla oscura del token `--magenta` (ya AA-seguro sin profundizar, 8.9:1 de contraste). Punto
  confidencial en dorado (marca mixta fría/cálida, mismo criterio que Gas País). Registrada en
  [[temas-por-cliente]] (catálogo + nota técnica) y en `presentaciones/_temas-demo/index.html`
  (tile `.t-fcv`), como exige la regla de registro obligatorio.
* **Fix de logo — wordmark demasiado claro sobre fondo claro:** el PNG del cliente trae el
  wordmark "fcv" y "Cuidamos Vidas" en gris neutro `#A4A7AD`, que sobre el estándar de fondo claro
  medía solo **2.17:1 de contraste** (se veía lavado). Se oscureció selectivamente solo los píxeles
  de baja saturación (`max(r,g,b)-min(r,g,b) < 20`) × 0.66, dejando intactas las hojas de color →
  gris `#6C6E72`, **5.1:1**, AA-seguro. Verificado leyendo los píxeles del `<img>` ya renderizado en
  el navegador (canvas + `getImageData`), no solo el archivo fuente.
* **Bug encontrado y corregido — ancho incorrecto en texto SVG en gradiente:** al calcular el
  `viewBox` de los títulos en gradiente (técnica SVG de [[sistema-diseno]] §5.2), se reescaló por
  error el ancho medido (`getBBox()`) por la proporción alto-real/1083, asumiendo que 1083 era una
  medida por-string en vez de una **constante de la fuente** (Playfair Display Black Italic a
  1000px) independiente del ancho. Eso produjo cajas más angostas que el glifo real; con
  `overflow:visible` el glifo se pintaba igual pero **se montaba sobre el texto siguiente en la
  misma línea** — visible solo en láminas donde el SVG no es el último elemento inline. Detectado
  leyendo el PDF exportado (lámina 3 renderizaba "Un enfoque du,ain mismo desarrollador" en vez de
  "Un enfoque dual, un mismo desarrollador"). Corregido usando el `getBBox().width` real medido
  para las 8 láminas (sin reescalar), re-exportado y reverificado — las 4 láminas con texto después
  del SVG (3, 6, 7, 8) quedaron correctas. Nota técnica completa en [[temas-por-cliente]] para no
  repetir el error en el próximo deck.
* **Verificación:** el Browser pane no pudo tomar screenshots en esta sesión (pane no desplegado),
  así que la verificación visual se hizo por: (a) DOM — `getBoundingClientRect` para overflow y gap
  contra el footer en las 7 láminas internas (todos positivos, 15–31px), sin overflow no intencional
  fuera de `.deco-rings` (decorativo, clip por diseño); (b) export a PDF (8 páginas exactas) leído
  con PyMuPDF a 150dpi por lámina + crops a 600dpi de 3 títulos en gradiente sin hairlines. Sin
  errores de consola; las 11 fuentes usadas cargan 200 OK (se retiraron `PlayfairDisplay-Regular` y
  `Montserrat-Regular` del `@font-face` y de `assets/fonts/` por no usarse en ningún selector).
* **Archivos:** `presentaciones/fcv/` (`index.html`, `styles.css`,
  `assets/` con logo recortado, favicon recortado del isotipo maestro, y las fuentes locales
  usadas) + `fcv.pdf` (8 págs). Contacto de cierre reutilizado
  (Gabriela Pedraza Rueda / Directora Full Service Global), igual que en decks anteriores.

## [2026-08-21] ajuste | Marval S.A.S. — eliminación de precios en ambos escenarios

A pedido del usuario, se retiraron todos los valores/precios de `presentaciones/marval/`,
que solo aparecían en la lámina 8 (Mapa del Ecosistema, `.eco-chip` / `.eco-agent-chip`):

- `index.html`: se quitaron los 8 `<span class="price">` (7 módulos + fila de 5 agentes de
  expansión) y los `id="eco-agente-ia"` / `id="eco-cimientos"` que el switch de escenario usaba
  para sustituir cifras.
- `script.js`: `SCENARIO_DATA` y `applyScenarioContent()` ya no cargan/sustituyen precios;
  solo mantienen badge y versión de escenario.
- `styles.css`: se eliminaron las reglas `.eco-chip .price` y `.eco-agent-chip .price`
  (huérfanas tras el cambio).
- Verificado en navegador (Escenario A y B) que la lámina 8 no deja espacio vacío ni texto de
  precio; regenerados `marval-escenario-a.pdf` y `marval-escenario-b.pdf` (9 páginas cada uno,
  confirmado sin `$` en el texto extraído).

## [2026-08-19] ajuste | Marval S.A.S. — responsividad de la lámina + recorte de contenido

Dos ajustes a pedido del usuario en `presentaciones/marval/`:

1. **Responsividad (el usuario tenía que hacer zoom-out al 75% para ver todo):** causa raíz —
   la lámina usaba unidades físicas fijas (pt/in, igual que el PDF) dentro de una caja que solo
   se dimensionaba por porcentaje del contenedor (`width:min(90%,1200px)` + `aspect-ratio` +
   `max-height:82%`), así que en ventanas más chicas la caja se achicaba pero el contenido en
   pt/in no, y se recortaba por el `overflow:hidden`. Fix: la lámina ahora se dibuja siempre a
   su tamaño nativo (1056×594px = 11in×6.1875in a 96dpi, igual que el PDF) y se reescala como un
   todo según el espacio disponible (`resizeSlideStage()` en `script.js`, recalculado en
   `resize`). **Nota técnica:** el primer intento uso `transform:scale()`, pero combinado con el
   texto SVG en gradiente producía **recortes de renderizado silenciosos en Chrome headless**
   (reproducido de forma determinística con capturas reales a varios tamaños de ventana — el
   texto se cortaba a mitad de palabra pese a que `getBoundingClientRect()` no mostraba ningún
   desborde real, es decir, era un bug de *paint*, no de *layout*). Se resolvió cambiando a
   `zoom` en vez de `transform:scale()`: `zoom` reflowa el layout real (como si el usuario
   cambiara el zoom del navegador) en lugar de componer una capa transformada, y el bug
   desapareció por completo, verificado en 700×600, 963×990, 1366×768 y 1920×1080. `@media
   print` fuerza `zoom:1` explícito para no afectar el PDF.
2. **Recorte de contenido:** se eliminó la lámina "Inversión y Forma de Pago" de ambos
   escenarios (antes lámina 9 de 10); "Mapa del Ecosistema" pasa directamente a "¿Cuándo
   empezamos?". Deck queda en **9 láminas** por escenario. Se limpió el bloque CSS `.invest`
   (ya sin uso) y los campos de `SCENARIO_DATA` asociados en `script.js`.

PDFs regenerados (9 páginas cada uno, verificado con PyMuPDF).

---

## [2026-08-18] build | Marval S.A.S. — Ecosistema de Agentes de IA (switch Escenario A/B)

Deck nuevo (10 láminas) construido a partir de dos cotizaciones XLSX del usuario
(`Cotizacion (1).xlsx` = Escenario A, `Cotizacion (2).xlsx` = Escenario B). Extracción con
`openpyxl` de la estructura por secciones/subsecciones/ítems (columnas L/M/N + totales Y por
grupo X) confirmó que **la única diferencia real entre escenarios es el Motor de IA** (API
externa vs. modelo propio self-hosted + MLOps) — el resto del alcance (Orquestador, Agente de
Gestión Humana, Agente de Soporte TI, capa de datos/intranet/infraestructura, Canal Teams,
Agente de Entregas Digitales, expansión a 5 agentes) es idéntico. Los totales que dio el
usuario ($103.049.261,2 / $118.924.607,4 COP) se verificaron exactamente como costo base ÷ 0.7
de margen.

**Primer deck con shell de switch interactivo** (barra superior con selector de Escenario A/B
tipo píldora, barra inferior con anterior/siguiente + barra de progreso + play-pause de
autoplay), adaptado de la mecánica de `multinal-escenario-b-demo/` pero construido como página
única autocontenida (no una app de 3 vistas). Para minimizar duplicación, las 7 láminas
idénticas entre escenarios llevan `data-scenario="both"` y las cifras que sí cambian (badge de
escenario, 2 chips de precio en el mapa del ecosistema, total e hitos de pago) se actualizan
por JS (`applyScenarioContent()`) en vez de duplicar el DOM; solo la lámina 5 (Motor de IA)
tiene dos variantes completas (`data-scenario="a"` / `"b"`) por diferir en estructura de
contenido, no solo en cifras.

**Exportación a PDF (obligatoria, dos documentos):** dado que la interactividad de una sola
lámina visible a la vez no es imprimible directamente, se añadió soporte de
`index.html?escenario=a|b` (leído en `DOMContentLoaded`) + `@media print` que ignora el estado
de navegación y apila las láminas de `data-scenario="both"` más las del escenario activo,
generando `marval-escenario-a.pdf` y `marval-escenario-b.pdf` (10 páginas cada uno, verificado
con PyMuPDF) desde el mismo `index.html`.

Paleta derivada por muestreo de píxeles reales del logo (`recursos/Marval.jpg`, procesado con
PIL: fondo blanco→transparente por umbral + recorte a bbox visible + padding ~6%): azul claro
`#4888C8` → azul del wordmark `#1068B0` → azul marino profundo `#062A4F`, sobre el estándar de
fondo gris claro + `--bg-wash`. Marca fría → punto "Confidencial" en ámbar por defecto. `<title>`
usa razón social completa **Marval S.A.S.**, confirmada por el usuario vía pregunta directa (no
se asumió el sufijo legal). Registrado en el catálogo de [[temas-por-cliente]] y como tile en
`presentaciones/_temas-demo/index.html`.

---

## [2026-08-10] ajuste | Financiera Comultrasan — Jerarquía visual del precio en Esquema Comercial

A pedido del usuario, en `presentaciones/comultrasan-orbit/` lámina 13: se extrajo la cifra de
inversión del subtítulo ("Pagos por hitos, sin sorpresas" queda solo) y se promovió a un bloque
`.price-hero` propio — etiqueta "INVERSIÓN TOTAL" + cifra grande en Playfair Black Italic
(27pt) — ubicado entre el subtítulo y las 3 tarjetas de hitos (40%/40%/20%), que se
desplazaron hacia abajo para darle espacio. Se limpiaron las dos tarjetas inferiores
("01. Proyecto por Fases" / "02. Acompañamiento Continuo"), quitando el párrafo descriptivo y
reduciendo su padding vertical (.2in→.14in) para que la tarjeta se ajuste al título corto sin
espacio sobrante. Verificado sin desbordamiento con `getBoundingClientRect()` (gap positivo
entre `.commercial-v2` y el footer) y visualmente en el PDF exportado.

---

## [2026-08-09] rediseño | Financiera Comultrasan — Retícula de Portada y contenido de Esquema Comercial

Dos ajustes a pedido explícito del usuario, con rol de "Diseñador UI/UX y Maquetador Senior":

1. **Lámina 1 (Portada):** se reajustó la retícula vertical manteniendo intacto todo el texto,
   los logos y la paleta. Título y subtítulo se movieron hacia arriba, y se amplió el espacio
   entre el logo de Financiera Comultrasan ("PARA") y la franja de datos de contacto. **Nota
   técnica:** el primer intento (solo agregar `margin-top` a `.cover__meta`) produjo un
   **desbordamiento real** — el contenido total superaba los 4.7475in disponibles dentro de
   `.cover` (`.slide` con `overflow:hidden`), cortando literalmente el texto de la franja de
   contacto a la mitad. Se verificó con `getBoundingClientRect()` vía JavaScript en el navegador
   (más preciso que medir a mano o por captura) y se iteró reduciendo el tamaño del título
   (36pt→28pt) y los márgenes/interlineado del bloque hasta lograr **15.49% de margen inferior
   visible** (cumple el ≥15% pedido) con el título subiendo de ~34% a ~29% de la altura de la
   lámina. Método de verificación (medir con `getBoundingClientRect` en vez de solo inspección
   visual) documentado aquí para reutilizar en futuros ajustes de retícula.
2. **Lámina 13 (Esquema Comercial y SLA):** se migró contenido de una lámina de referencia
   externa (deck "Unidrogas", "Forma de Pago y Garantía") que el usuario compartió como
   inspiración de **estructura, no de colores**. Cambios: subtítulo nuevo "Pagos por hitos, sin
   sorpresas — inversión total $85.630.624,33 COP." debajo del título; las 3 tarjetas pequeñas
   ahora muestran el esquema de pago **40% Anticipo de Inicio / 40% A Mitad del Proyecto / 20% A
   la Entrega (Go-Live)**; el panel lateral derecho pasa de "SLA y Soporte" (3 ítems) a
   **"Garantía y soporte"** con los 4 bullets migrados tal cual de la referencia (2 semanas de
   pruebas y estabilización, soporte post go-live, control de cambios documentado, transparencia
   total); y los bloques "01. Proyecto por Fases" / "02. Acompañamiento Continuo" (antes las
   tarjetas de modalidad) se reubicaron debajo de las 3 tarjetas de hitos. Se mantuvo la paleta
   teal→verde y la tipografía Playfair/Montserrat propias del deck — la referencia solo aportó
   el esqueleto de layout (fila de 3 tarjetas + panel lateral).

---

## [2026-08-08] rediseño | Financiera Comultrasan — Arquitectura Técnica y Esquema Comercial

Dos rediseños estructurales completos a pedido del usuario (el ajuste puntual de padding del
2026-08-07 en la lámina 10 no fue suficiente):

1. **Lámina 10 (Arquitectura Técnica):** se abandonó el layout de tabla de una sola tarjeta
   (`.tech-table`/`.tech-row`, donde el texto seguía quedando pegado al borde redondeado) y se
   reemplazó por un **grid de 8 tarjetas independientes 2×4** (`.tech-grid`/`.tech-item`, mismo
   patrón de tarjeta con barra de acento izquierda que el resto del deck). Cada tarjeta tiene su
   propio padding completo por los 4 lados, eliminando de raíz cualquier posibilidad de texto
   tocando o saliéndose del borde.
2. **Lámina 13 (Esquema Comercial y SLA):** rediseño total de la estructura (no de la paleta),
   adaptando el esqueleto de una referencia visual que el usuario compartió (deck "Unidrogas",
   lámina "Forma de Pago y Garantía": fila de 3 tarjetas grandes + panel lateral de checklist con
   checks verdes). Se mapeó el contenido propio de Comultrasan sobre ese esqueleto: 3 tarjetas
   (`.stat-row-3`/`.stat-box`) — Proyecto por Fases (01), Acompañamiento Continuo (02) e
   **Inversión Total $85.630.624,33 COP** como tercera tarjeta con la cifra como elemento
   protagonista — más una leyenda en cursiva debajo, y un panel lateral `.sla-panel` ("SLA y
   Soporte") con los 3 puntos de SLA en checklist con ícono de check. Se mantuvo el sistema
   tipográfico y la paleta teal→verde propios del deck — la referencia solo aportó la
   distribución (fila de tarjetas + panel lateral), no los colores ni la tipografía sans-serif
   del original.

Verificado renderizando ambas láminas a 2.4x con PyMuPDF tras el cambio.

---

## [2026-08-07] ajuste | Financiera Comultrasan — tabla técnica e inversión confirmada

Dos ajustes puntuales a `presentaciones/comultrasan-orbit/` a pedido del usuario:
1. **Lámina 10 (Arquitectura Técnica):** el texto de la primera y última fila quedaba pegado al
   borde redondeado de la tarjeta (`.tech-table` no tenía padding propio, solo las filas). Se
   agregó `padding:.14in 0` al contenedor.
2. **Lámina 13 (Esquema Comercial y SLA):** se unificaron las dos tarjetas de modalidad
   ("Modalidad A · Proyecto por Fases" / "Modalidad B · Acompañamiento Continuo") en una sola
   tarjeta con divisor interno, quitando las palabras "Modalidad A" / "Modalidad B" (quedan solo
   "Proyecto por Fases" y "Acompañamiento Continuo"). Se ajustó el texto de acompañamiento
   continuo a "Posterior al despliegue se puede adquirir soporte...". **Inversión confirmada:**
   reemplazado el texto de rango pendiente por la cifra real **$85.630.624,33 COP**, destacada en
   tamaño grande dentro del mismo banner "Inversión" (ya no es un valor por definir).

---

## [2026-08-06] ajuste | Financiera Comultrasan — corrección pixel-perfect de las 14 láminas

Ronda de correcciones a pedido explícito del usuario ("verificado visualmente pixel por pixel,
sin errores") sobre `presentaciones/comultrasan-orbit/`:

1. **Causa raíz de casi todos los títulos en gradiente mal posicionados/mal dimensionados:**
   la técnica SVG original (`viewBox` con ancho estimado a ojo por conteo de caracteres) producía
   desalineación de línea base y proporciones incorrectas en las 14 láminas. Se probó volver a
   `background-clip:text` (CSS), pero **reprodujo el bug de caja/hairline documentado en
   `wiki/sistema-diseno.md` §5.2** (visible como un recuadro fino alrededor del texto en el PDF
   exportado) — confirmando que el bug sí existe en este Chrome/sesión, a diferencia de lo
   reportado en la verificación de 2026-07-30. **Solución de fondo:** se midieron las métricas
   reales de `PlayfairDisplay-BlackItalic.ttf` con PIL (`ImageFont.getmetrics()` / `getlength()`)
   para cada frase en gradiente, y se construyó el `viewBox` del SVG con el ancho exacto y
   `height = ascent` (texto ubicado en `y = ascent`), de forma que el borde inferior del SVG
   —que es la línea base de un elemento reemplazado inline— coincida matemáticamente con la
   línea base del texto circundante. Resultado: alineación pixel-perfect en las 14 láminas, sin
   caja ni hairline. Documentado como nuevo método de referencia (superior al de §5.2, que sigue
   siendo válido pero con estimación manual de ancho).
2. **Logos:** aumentados en las 14 láminas — Campuslands portada 26→36px, cliente portada
   40→58px; Campuslands interno 20→27px, cliente interno 28→38px (con ajuste de la fila de
   header de `.internal` para acomodarlos).
3. **Portada:** eliminadas las 4 figuras `.corner` (esquinas) a pedido del usuario.
4. **Legibilidad:** oscurecido/agrandado el texto de la columna "Antes" (lámina 5), toda la
   tabla técnica (lámina 10), tarjetas de Propuesta de Valor/Alineación/Métricas (láminas 4, 6,
   7, 11) y el contenido de la mitad inferior de Esquema Comercial y SLA (lámina 13).
5. **Lámina 11 (Métricas):** el grid 3+2 con CSS Grid dejaba la segunda fila de 2 tarjetas
   desalineada a la izquierda; se cambió a `flex-wrap` centrado (`.qc-grid.wrap`).
6. **Lámina 14 (Cierre):** los números dentro de los círculos verdes no quedaban centrados
   (glifos de Playfair Display con métricas irregulares dentro de una fuente serif); se cambió
   la tipografía del dígito a Montserrat. Se retiraron "Liderazgo Expansión Global & Full
   Service", "Campuslands S.A.S. BIC" y "Km.4, Anillo Vial..." de la tarjeta de contacto, y se
   agregó "Directora Full Service Global" + correo (gabriela.pedraza@campuslands.com) + teléfono
   (+57 300 302 8555), cada uno con su ícono.

Verificado renderizando las 14 páginas del PDF exportado a 2.2x con PyMuPDF y revisando cada una
contra la lista de mejoras entregada por el usuario.

---

## [2026-08-05] build | Financiera Comultrasan — Asistente Conversacional con IA (Orbit)

Construcción del deck completo (**14 láminas**) en `presentaciones/comultrasan-orbit/`, a partir
de `Propuesta_Comultrasan_Campuslands_v4.pdf` (propuesta comercial y técnica de 13 páginas para
un asistente conversacional con IA Generativa orquestado por Orbit sobre WhatsApp y el botón
"Canales Digitales"). Mapeo: Portada → Resumen Ejecutivo (statement + 4 resultados esperados) →
Diagnóstico (cita de Angela Latorre + 4 hallazgos) → Propuesta de Valor (grid 2×2) → Funnel
Antes/Después (tabla comparativa 5 filas) → Alineación de Objetivos (Captación/Colocación/
Retención) → Diagrama del orquestador Orbit (3 líneas de negocio) → 2 mockups de flujo
conversacional (Transferencia Bre-B, Precalificación de crédito) → Arquitectura Técnica (tabla
de 8 integraciones) → Métricas Clave (5 KPIs) → Roadmap (timeline de 6 fases) → Esquema Comercial
y SLA → Cierre. Paleta propia derivada del logo (teal `#0B6667` del banner → verde `#3FAA46` →
lima `#8DC63F` del swoosh), registrada en [[temas-por-cliente]] y en el tile de
`presentaciones/_temas-demo/`. El logo del cliente traía el fondo "blanco" con alfa uniforme ~50%
en vez de transparencia real; se reconstruyó el canal alfa por umbral de blancura antes de
recortar (nuevo caso, documentado en [[temas-por-cliente]] por si se repite con otro cliente).

**Balance de espacio — 2 rondas de corrección tras el primer export a PDF:** (1) el diagrama del
orquestador (lámina 7) se renderizó más alto que su caja disponible y, al estar centrado
verticalmente, invadió el título de la lámina — se redujo el diagrama y se cambió a alineación
superior. (2) los dos mockups de chat (láminas 8-9, 6 mensajes cada uno) se desbordaban por debajo
del pie de página — se acortó el texto de los mensajes más largos y se redujo sustancialmente el
padding/gap/tipografía del componente `.chat-mock`. (3) las láminas de grid de una sola fila
(Propuesta de Valor, Alineación de Objetivos, Métricas) dejaban ~40% de aire vacío arriba y abajo
de las tarjetas — se pasó Propuesta de Valor a grid 2×2, Métricas a 3+2, y se agrandaron las
tarjetas de Alineación de Objetivos (con número decorativo grande), siguiendo la regla de balance
de espacio de `wiki/sistema-diseno.md` §5.1. Verificado leyendo las 14 páginas del PDF exportado
con PyMuPDF tras cada ronda.

**Pendiente de confirmación del usuario:** el `<title>` usa "Financiera Comultrasan" — ni el PDF
fuente ni el logo traen el sufijo legal completo de la razón social (S.A.S., Compañía de
Financiamiento, etc.) requerido por la regla obligatoria de `<head>` en `CLAUDE.md`; actualizar
cuando el usuario lo confirme. La fecha de portada ("Agosto 2026") también es un valor por defecto
propuesto, no confirmado explícitamente.

---

## [2026-08-04] ajuste | Gas País Chilco — adición del precio en lámina 11 (Inversión)

Se agregó el valor de inversión, antes marcado "Por definir": **$90.000.000 COP**
(noventa millones de pesos colombianos), en `presentaciones/gaspais-chilco/index.html`
(lámina 11 · "10 · Inversión"). Se ajustó el título de la lámina ("El alcance y la
inversión, definidos") y la nota de pago para reflejar el valor confirmado; la forma
de pago queda pendiente de definir. Se verificó visualmente en navegador y se
regeneró `gaspais-chilco.pdf`.

---

## [2026-07-30] lint | Auditoría del monorepo — 5 correcciones a pedido del usuario

1. **`wiki/index.md`:** se eliminó la entrada duplicada/obsoleta de "Ve a la Segura"
   ("paleta temporal ámbar, valores pendientes de costear") que coexistía con la entrada
   vigente y confirmada (paleta "concierto", inversión $21.808.295 COP).
2. **Entrega obligatoria PDF + Vercel:** se corrigió `CLAUDE.md` (tabla de decisiones
   fundacionales) y `presentaciones/README.md`, que enmarcaban a Vercel como reemplazado
   por el PDF (2026-06-17). Ahora ambos quedan explícitos como obligatorios en toda
   presentación, sin que uno reemplace al otro — el PDF es el archivo final para el
   cliente, el link de Vercel es la versión interactiva que se comparte en el chat.
3. **Reorganización y documentación de 3 carpetas huérfanas** en `presentaciones/`, sin
   README y sin entrada en `wiki/index.md`: resultaron ser variantes intencionales, no
   duplicados accidentales. `multinal-escenario-c-demo/` es la demo original de 26
   láminas del Escenario C (nunca indexada); `multinal-escenario-demo/` y
   `colbeef-demo-f/` son forks "solo simulador" (sin el apartado Presentación) usados
   como destino de los links "Demo Multinal" / "Demo Colbeef" desde
   `fullservice-campuslands/`. Se creó `README.md` en las 3 y se agregaron a
   `wiki/index.md`.
4. **Bug de hairline en texto con gradiente (`background-clip:text` en print) — solución
   de fondo:** se adoptó SVG `<text fill="url(#...)">` como técnica estándar en vez de
   `background-clip:text`, documentada con snippet en §5.2 de `wiki/sistema-diseno.md`.
   Se armó una reproducción fiel del caso que falló en Gas País (mismo título, misma
   fuente Playfair Display Black Italic vía `@font-face` local, mismo comando de export)
   comparando ambas técnicas a 8x/~576dpi con PyMuPDF; **no se logró reproducir el
   hairline en ninguna de las dos versiones** en esta sesión (posible diferencia de
   versión de Chrome), por lo que no hay confirmación 100% empírica de que esto elimina
   el bug original — pero el SVG es estructuralmente inmune a esa clase de artefacto y da
   resultado visual idéntico, así que se adopta igual como estándar para decks nuevos. No
   se regeneraron los PDFs ya entregados (Avicampo, Gas País) con el artefacto conocido.
5. **Logos de cliente faltantes en `recursos/`:** se copiaron desde los `assets/` de cada
   deck ya construido (no fue necesario buscarlos en internet): `Green Metal.png`,
   `Mchaileh.png`, `Miami Aqua Tours.png`. **Compumax queda pendiente** — su logo nunca
   existió como imagen en el repo, ambos decks de Compumax lo recrean como wordmark CSS
   (Poppins, "Compu" gris + "max" azul); conseguir un logo real requeriría buscarlo fuera
   del repo, lo cual requiere permiso explícito del usuario antes de descargar cualquier
   archivo.

## [2026-07-29] ajuste | Gas País Chilco S.A.S. — fix de diagrama de capas + rediseño de Inversión (`presentaciones/gaspais-chilco/`)

* **Lámina 4 (La solución) — texto superpuesto y flechas recortadas:** el `.l-tag` de cada capa (p. ej. "CAPA 2 · CUMPLIMIENTO Y TRAZABILIDAD") tenía `white-space:nowrap` con `letter-spacing:.18em` dentro de una columna de solo 1.5in — el texto desbordaba horizontalmente la columna y se montaba sobre las chips de la columna vecina. Se ensanchó la columna de `.l-head` a 2.15in y se redujo el `letter-spacing` a `.1em`. Las flechas `.arch-conn` (SVG de 13px) vivían en un contenedor de solo 5px de alto, quedando recortadas/apretadas contra las tarjetas vecinas; se subió el contenedor a 16px. Para compensar el espacio adicional se recortó ligeramente el padding de `.layer` y el `gap` de `.arch` — reverificado sin overflow contra el footer (gap de 15px, igual que el resto de láminas).
* **Lámina 11 (Inversión) — rediseño a pedido del usuario:** se eliminó la tabla de 10 filas (`scope-list`) con el desglose de bloques M0–M9, reemplazada por un **hero centrado** (`.invest-solo`) clonado en estructura (no colores ni contenido) de la lámina de Inversión de `presentaciones/compumax-mejoras-multitipo/`: eyebrow "INVERSIÓN TOTAL (COP)" → cifra gigante en gradiente ("Por definir") → párrafo de alcance centrado → nota pequeña sobre forma de pago pendiente. Se retiraron las clases CSS `.scope-wrap/.scope-list/.scope-row/.invest__num` (sin uso) y se agregó `.invest-solo` (portada de `compumax-mejoras-multitipo/styles.css`, adaptada a los tokens de Gas País).
* Re-exportado a PDF (12 páginas), ambas láminas verificadas visualmente sin superposición ni overflow.

## [2026-07-29] build | Gas País Chilco S.A.S. — Plataforma HSE-SST (`presentaciones/gaspais-chilco/`)

* **Origen:** cotización de alcance de FullService Campuslands para Gaspaís Chilco (`Gaspais Chilco - Cotizacion de Alcance.pdf` y `.xlsx` en `QuoteDeveloper/cotizaciones/gaspais-chilco/`) — plataforma HSE/SST con ambiente productivo desde el inicio, 8 módulos (M1–M8) más los bloques transversales M0 (estructura del proyecto) y M9 (arquitectura/seguridad/servicio), para 1.500 usuarios. El PDF trae cifras por módulo ($65.721.634 COP total) pero **el usuario pidió dejar la inversión como "Sin Definir"** para ajustarla más adelante — la lámina 11 muestra el alcance completo de los 10 bloques sin ninguna cifra.
* **Razón social:** confirmada por el usuario como "Gas País Chilco S.A.S." (no aparecía completa ni en el PDF ni en el XLSX, solo "Gaspaís Chilco"/"GAS PAÍS"); usada en `<title>`, meta de portada, alt de logo y footer. El nombre corto "Gaspaís Chilco" se usa en el copy del cuerpo.
* **12 láminas:** Portada, Línea base (métricas), El reto (split), La solución (diagrama de 4 capas: operativa → cumplimiento → riesgo → visibilidad), Módulos I y II (grid 2×2 cada una, los 8 módulos), Arquitectura/seguridad/servicio (split, incluye nota de que el scaffolding de IA de M0 no es un agente conversacional), Quiénes somos, El equipo (8 roles), Cronograma (4 fases), Inversión y alcance (10 bloques M0–M9, "Por definir"), Cierre.
* **Paleta derivada del logo** (`recursos/GasPais.png`, provisto por el usuario a mitad de sesión): el isotipo funde un pétalo amarillo (`#FFD400`) y uno azul (`#0161B8`) en verde (`#4FA647`) donde se superponen; el wordmark es verde bosque sólido (`#0B5E2B`). Se usó esa transición literal como `--grad-brand` (amarillo→verde→azul), primera paleta de 3 hues reales del catálogo. Punto "Confidencial" en dorado por ser marca mixta cálido+frío. Registrada en [[temas-por-cliente]] y en el tile de `presentaciones/_temas-demo/index.html`.
* **Ajustes de balance de espacio (§5.1 [[sistema-diseno]]):** el diagrama de 4 capas desbordaba ~245px al usar el mismo tamaño de tarjeta que una versión de 3 capas — se compactó padding/fuente y se acortaron etiquetas largas hasta ocupar 97% del alto disponible sin overflow. La lista de 10 filas de alcance (lámina 11) igual se ajustó (padding/gap reducidos) para no desbordar su contenedor. La lámina "Quiénes somos" quedó con la variante `.feat-card--lg` **sin definir en el CSS** (se usaba en el HTML pero la clase no existía), dejando 57% de aire vacío bajo las 3 tarjetas; se agregó la clase y se calibró su padding/tipografía para llenar el espacio sin desbordar el texto.
* **Bug de hairline en gradiente de texto — investigado, no resuelto:** se confirmó visualmente en el PDF exportado que `background-clip:text` (portada, títulos y la cifra "Por definir") dibuja un recuadro fino alrededor del texto en Chrome headless, pese a que el elemento ya cumple la regla documentada (`display:inline`). Se probó sin éxito: `background-size:112%` (mitigación ya usada en Colbeef), quitar `color:transparent` redundante, quitar la itálica, y `line-height:1`. Se verificó que el mismo defecto —más sutil, solo en el borde izquierdo— ya existe en el PDF **ya entregado** de `presentaciones/avicampo/` (portada), confirmando que es un bug sistémico de todo el sistema de diseño, no de este deck. Documentado en [[temas-por-cliente]]; pendiente una solución de fondo (posible render del texto en gradiente como SVG).
* Verificado: 12/12 láminas sin overflow contra el footer (chequeo de gap medido por JS, no solo contra el borde de `.slide`), fuentes locales cargando 200 OK, favicon e isotipo de Campuslands recortados a bbox+padding igual que el resto del sistema.

## [2026-07-24] build | FullService Campuslands — presentación corporativa (`presentaciones/fullservice-campuslands/`)

* **Origen:** reconstrucción a partir de un PDF de 2 láminas provisto por el usuario (sin fuente HTML previa en el repo) — se renderizaron sus páginas a imagen con `pypdfium2` para clonar el estilo pixel a pixel (fondo azul marino casi negro, tarjetas con ícono en caja azul + título + descripción, "FullService" en Poppins ExtraBold + "Campuslands" en Playfair Display Italic). No es un deck de cliente: es la presentación institucional de FullService/Campuslands, por lo que no lleva el header/footer con logo de cliente ni la paleta gris-claro v2 — mantiene el estilo oscuro original tal como pidió el usuario.
* **Lámina 1 (rediseñada):** "Software a la Medida" y "Software a la Medida con IA" (2 tarjetas originales) se unificaron en **una sola tarjeta** con descripción fusionada; la columna derecha pasó de 5 a **4 tarjetas** (Software a la Medida · Staffing · BPO · Consultoría), redistribuidas con más padding/gap para llenar el alto sin dejar aire ni apretarse.
* **Lámina 2 (nueva):** "Nuestros Agentes de IA" — grid 2×2 de tarjetas del mismo tamaño para los 4 agentes propios: **Orbit** (agente maestro/orquestador de WhatsApp), **Sora** (RRHH/contratación), **Sales** (ventas 24/7 por WhatsApp) y **Juridsoft** (panel jurídico). Íconos SVG propios dibujados a mano (no hay set de íconos de terceros en el repo).
* **Lámina 3:** la página 2 original ("Portafolio Complementario & IA", 6 tarjetas) se copió intacta sin cambios de contenido ni estilo.
* **Links de redirección:** la tarjeta "Software a la Medida" (lámina 1) y la tarjeta "Sora" (lámina 2) son `<a href>` reales hacia `fullservicepresentations.vercel.app/colbeef-demo/docs/index.html` y `gustavoadolfonavarropacheco.github.io/Sora/` respectivamente (con badge de flecha ↗ visible), verificado por JS en el navegador. Al exportar a PDF con Chrome headless estos quedan como anotaciones de link clicables en el documento.
* **Ajuste de overflow:** la primera versión desbordaba las 3 láminas (tarjetas cortadas y pie de página tapado) por exceso de padding/tipografía frente al alto fijo de 6.1875in. Se recalculó el presupuesto vertical y se redujeron paddings, tamaños de ícono y fuente en `.svc-card`, `.pf-card` y `.ag-card`, y se acortó la descripción fusionada de "Software a la Medida"; verificado con export a PDF + render a imagen de las 3 páginas, sin recortes ni solapamientos.
* Favicon reutilizado de `presentaciones/avicampo/assets/favicon.png` (isotipo Campuslands ya recortado). `<title>` = "FullService Campuslands S.A.S.".
* **Ajuste 2026-07-24 (mismo día):** a pedido del usuario, la tarjeta "Software a la Medida" pasó de 1 link (card completa clicable) a **2 links** — se retiró el wrapper `<a>` de toda la tarjeta y se agregaron 2 píldoras `.svc-link` ("Demo Multinal" → `multinal-escenario-demo/docs/`, "Demo Colbeef" → `colbeef-demo-f/docs/`, ambas en `fullservicepresentations.vercel.app`). El link de Sora se mantuvo sin cambios. La fila de píldoras nueva volvió a desbordar la lámina 1 (Consultoría cortada); se compensó reduciendo aún más el padding vertical de `.hero`, `.svc-card` y `.svc-card--lg` y el gap entre tarjetas — reverificado con export a PDF, sin recortes.

## [2026-07-22] ajuste | Avicampo S.A.S. — cambio de precio + corrección de errores de diseño (`presentaciones/avicampo/`)

* **Cambio de precio:** inversión total actualizada de $30.531.552 a **$43.616.503 COP** (indicado por el usuario). El desglose por módulo se escaló proporcionalmente para mantener consistencia matemática con el nuevo total; pago 40/40/20 recalculado ($17.446.601 / $17.446.601 / $8.723.301).
* **Sobreposición en lámina de Inversión:** la tarjeta de pago "20% Cierre" invadía visualmente el pie de página (el `.pay-plan` apilado verticalmente con 3 tarjetas + textos largos excedía el alto disponible de `.s-body`, sin que el chequeo de gap superficial lo detectara — el desborde ocurría *dentro* de la caja, no en su borde exterior). Se rediseñó `.pay-plan` de columna vertical a **fila horizontal de 3 tarjetas compactas** debajo de `.invest-modules`, liberando suficiente alto.
* **Recorte de texto en lámina Equipo:** la tarjeta "Líder / Arquitecto / Scrum" (3 líneas) se recortaba ~18px contra el `overflow:hidden` de `.team-card` — un bug de sizing de CSS Grid con hijos flex-column y texto que envuelve (el auto-row no reservó la altura real necesaria). Se acortó el título a "Líder / Arquitecto" y se cambió `.team-grid` a `grid-auto-rows:1fr` con `justify-content:center` en la tarjeta, dando más aire de forma uniforme.
* **Caja blanca detrás de las etiquetas "MOD-XX · 0X":** mismo bug de hairline/caja de `background-clip:text` ya documentado (esta vez un rectángulo blanco opaco, no solo una línea) en el `<span class="rf gradient-text">` de cada `.feat-card` — el elemento es `display:block`, el caso exacto que dispara el bug. Se quitó `gradient-text` de las 12 etiquetas `.rf` y se fijó color sólido (`var(--cyan)`, el naranja quemado de marca) en la regla base de `.feat-card .rf`.
* **Aire vacío en Módulo 3 (Chats y Clientes):** 3 tarjetas con texto corto dejaban ~35% de la lámina en blanco. Se añadió la variante `.feat-card--lg` (padding, tipografía y line-height mayores) y se aplicó a esas 3 tarjetas, redistribuyendo el contenido para llenar el espacio disponible (regla de Balance de Espacio §5.1 de [[sistema-diseno]]).
* **Verificación:** export a PDF (Chrome headless, 9 páginas) + inspección visual completa de las 9 láminas a 130dpi y crops a 300dpi de las zonas corregidas, confirmando ausencia de sobreposición, recorte y aire vacío.

## [2026-07-22] build | Avicampo S.A.S. — Evolución del Agente de IA en WhatsApp (`presentaciones/avicampo/`)

* **Alcance leído de** `FullServices NAL 2026 - Avicampo 2.0.xlsx` (hoja "Avicampo 2.0"): 4 módulos de mejora al agente conversacional — Ajustes de Dashboard ($5.259.643), Seguimiento / Informes ($8.834.245), Chats y Clientes ($4.431.805) y Campañas Automatizadas ($7.789.502) — más estructura/UX/implementación ($4.216.356). **Total $30.531.552 COP**, pago 40/40/20 (esquema no especificado en el Excel; confirmado con el usuario).
* **Paleta propia derivada del logo:** sol amarillo (`#FDB913`) → naranja de marca (`#FF8A00`) → verde "frescura" (`#4CAF50`/`#1B5E33`), registrada en [[temas-por-cliente]] y en el tile `.t-avc` de `presentaciones/_temas-demo/index.html`. Fondo gris claro + `--bg-wash` (estándar vigente).
* **9 láminas:** Portada · Contexto y objetivo · Módulo 1 Dashboard (grid) · Módulo 2 Seguimiento (embudo de 5 pasos, layout nuevo `.funnel`) · Módulo 3 Chats y Clientes (grid) · Módulo 4 Campañas (grid) · Equipo y metodología (layout nuevo `.team-grid`) · Inversión (tabla por módulo + pago) · Cierre/CTA.
* **Logo del cliente** recortado a su bbox visible + padding 6% (`assets/logo-cliente.png`); Campuslands azul horizontal recortado igual para fondo claro.
* **Bug de hairline en PDF** (mismo ya documentado para Colbeef): los `<em class="gradient-text">` mezclados en la misma línea que texto negro en `.s-title` dejaban una línea sutil bajo el gradiente al exportar con Chrome headless. Resuelto con dos clases nuevas de acento sólido `.title-accent`/`.title-accent--green` (alternando naranja/verde) para esos 8 títulos internos; se conservó el gradiente en la portada y en la cifra de inversión (verificado limpio ahí a 300dpi).
* **Verificación:** preview en Browser pane (9 láminas, balance de espacio ok) + export a PDF (Chrome headless, 9 páginas = 9 láminas) + inspección a 300dpi con PyMuPDF confirmando ausencia de hairline tras el fix.

## [2026-07-16] ajuste | Multinal S.A.S. — Escenario B, quitar título superior + rediseño de las 3 láminas de agentes (`multinal-escenario-b/` y `multinal-escenario-b-demo/`)

* **Título superior eliminado** (láminas 9, 10, 11): se quitó el `<h2 class="s-title">` ("Agentes de X y Y") que quedaba debajo del indicador `PRY-...`, dejando solo el `s-eyebrow`. Libera ~0.35–0.4in de alto por lámina.
* **Espacio reutilizado:** `.agent-duo` con más `margin-top`, y dentro de cada `.agent-col` se agrandaron `a-eyebrow`/`a-title`/`a-lead`/tarjetas/tag-row. Primer intento demasiado agresivo causó recorte real (tarjetas superpuestas contra el pie de página) — corregido con una segunda pasada más moderada, verificada sin overflow.
* **Nueva variante `.feat-grid--pair`:** las columnas con solo 2 tarjetas (Inventarios, Cartera, Servicio al Cliente) tenían de más espacio libre que las de 3 con el tamaño uniforme; se creó esta variante con tipografía y padding más grandes específicamente para columnas de 2, sin tocar el tamaño ya ajustado de las columnas de 3 (que son las que limitan el espacio disponible). Un primer valor también se pasó de tamaño (se cortó el tag-row de la columna izquierda en la lámina 10) — corregido en una segunda iteración.
* **Verificación:** deck fuente vía PDF (Chrome headless + PyMuPDF, método ya establecido). Demo vía **Playwright conectado por CDP** a una instancia de Chrome con `--remote-debugging-port` — mismo método introducido en el ajuste anterior, reutilizado porque el Browser pane del entorno seguía sin responder. Limpieza de procesos hecha esta vez con PID específico (no `taskkill /IM chrome.exe`) para no repetir el cierre accidental de todas las ventanas de Chrome del sistema.

## [2026-07-16] ajuste | Multinal S.A.S. — Escenario B, texto grande en tarjetas (láminas 3–12) + quitar badge de descuento (`multinal-escenario-b/` y `multinal-escenario-b-demo/`)

* **Tarjetas de funcionalidades más grandes:** `.feat-card` base (rf/h4/p) y padding aumentados; igual en `.feat-grid--dense` (Gobierno de Datos) y `.agent-col .feat-card` (dúos de Agentes IA). Aplicado en ambos: el deck standalone (`styles.css`) y su espejo namespaced en la demo (`style-escenario-b.css`).
* **Bug real encontrado y corregido:** la lámina CRM Corporativo (grid de 4 columnas × 7 tarjetas) se recortó contra el pie de página tras el aumento de fuente — columnas más angostas + texto más grande = tarjetas más altas de lo esperado. Se resolvió aplicando la variante `.feat-grid--dense` (ya probada que cabe con margen) a esa lámina específicamente, en vez de reducir el tamaño para todas.
* **Escenarios de Inversión:** se eliminó el badge "-X% descuento" de las 3 tarjetas (pedido explícito del usuario, resto de la tarjeta intacto).
* **Verificación:** el deck standalone se verificó con el método ya establecido (Chrome headless `--print-to-pdf` + rasterizado PyMuPDF, 16 páginas). Para la demo, las herramientas del Browser pane del entorno no respondieron (clasificador de seguridad no disponible); se instaló **Playwright** (`pip install playwright`) y se conectó vía CDP a una instancia de Chrome lanzada con `--remote-debugging-port`, lo que permitió invocar `jumpToSlide()` real dentro del shell y capturar cada lámina — método más robusto que dejar constancia para futuras sesiones si el Browser pane vuelve a fallar. Detectado y descartado un falso positivo (un "fantasma" de la lámina anterior en la captura) causado por el fade de 0.5s del shell (`transition: opacity 0.5s ease` en `.slide`) — se resolvió esperando 800ms antes de capturar, no era un bug real.
* **Aviso:** al limpiar los procesos de Chrome de prueba se usó `taskkill /IM chrome.exe`, que cerró **todas** las instancias de Chrome del sistema, no solo las de prueba. Corregir en el futuro usando el PID específico devuelto por el lanzamiento, no el nombre del proceso.

## [2026-07-16] ajuste | Colbeef S.A.S. — Simulador Demo, animaciones de "recarga de fondo" al hacer clic en tarjetas + transición fluida de Theme Toggle (`colbeef-demo/docs/`)

* **Causa raíz encontrada:** varios módulos del simulador (Clientes, Conductores, Por Facturar, Usuarios, Chats) recargaban `innerHTML` de la grilla completa — con su animación de entrada `csCardIn`/`csPop`/`cpSlideUp` en cascada — ante interacciones que no debían tocar el fondo: un toggle on/off dentro de una tarjeta (`toggleConductor`, `toggleUsuario`), seleccionar un cliente dentro del modal de asociación de conductor, o cambiar de pestaña dentro del perfil de cliente. Esto hacía que clicar una tarjeta "recargara" visualmente toda la lista detrás.
* **Fix:** nuevo helper `setGridHTML(el, mode, html)` en `script.js` que solo deja reproducir la animación de entrada cuando el "modo" (vista/página/perfil/chat) cambió de verdad; toggles y cambios de pestaña ahora aplican `.no-anim` (nueva utilidad en `style.css`). Se desacopló el modal de asociar conductor (`renderDriverModal`) y el modal de detalle de Por Facturar (`syncFacturarDetailModal`) del re-render de la grilla de fondo — antes cualquier clic dentro del modal reconstruía también la lista detrás. `toggleConductor`/`toggleUsuario` ahora mutan el botón directamente en vez de re-renderizar toda la grilla. El perfil de cliente (`cp-container`) pasó de 5 animaciones escalonadas (`cpSlideUp` con delays 0.05s–0.28s) a una sola animación de opacidad ligera (0.28s).
* **Theme Toggle:** se añadió la transición fluida solicitada por el usuario vía View Transitions API (`document.startViewTransition`) con el clip-path diagonal `reveal-light`/`reveal-dark` (0.7s, `--expo-out`). Se replica la clase `dark-theme`/`light-theme` también en `<html>` porque los pseudo-elementos `::view-transition-*(root)` se anclan ahí, no en `<body>`. Con fallback directo (sin animación) si el navegador no soporta la API.
* Verificado con Chrome embebido vía JS/DOM (mismo nodo de grilla antes/después del toggle, overlay del modal no destruido al seleccionar tarjetas dentro, `no-anim` aplicado correctamente al cambiar de pestaña en perfil de cliente) — el `computer{screenshot}` de esta sesión no respondía de forma persistente, igual que en el deck de Multinal del mismo día.

## [2026-07-16] build | Multinal S.A.S. — Sincronización del deck final al demo interactivo (`multinal-escenario-b-demo/`)

* **Encargo:** llevar el deck ya cerrado (`multinal-escenario-b/`, 16 láminas) al apartado "Presentación" de la demo interactiva, que seguía con las 19 láminas de la primera versión (build del 2026-07-10).
* **Método:** transformación 1:1 aplicando el mismo namespace `.b-deck`/`b-*` ya establecido (prefijo `b-` en cada clase semántica del deck fuente; `slide`→`slide bdeck-slide`; `glow-a`/`glow-b`/`active` sin prefijo, como ya lo hacía el archivo original). `style-escenario-b.css` se actualizó sección por sección: tamaños de letra bumpeados (s-eyebrow/s-title/s-lead/pain-item), Mapa del Ecosistema con precios reales y 6 agentes (antes 7), variante `--dense` para Gobierno de Datos, secciones nuevas `.b-agent-duo` y `.b-scenario-grid`, reemplazo completo del viejo esquema de pago 40/40/20 (`.b-pay-row`/`.b-term`/`.b-txt`, con el token `--b-grad-num` ahora eliminado por quedar sin uso) por `.b-pay-plan`/`.b-plan-card`. `script.js`: `state.totalSlides` 19→16. `index.html`: `<meta name="description">` corregida de "Escenario C" a "Escenario B" (quedó pendiente de un build anterior).
* **Hallazgo de verificación:** el contenedor de diapositivas del shell demo tiene una relación de aspecto ligeramente distinta a la del deck standalone (más ancho y ~30px más bajo), lo que causó un recorte real de 60px en la lámina "Inversión y Alcance" (tarjetas de plan de pago) que no existía en el PDF exportado — se corrigió aparte, específicamente en `style-escenario-b.css`, sin tocar el deck fuente. Verificado con `jumpToSlide()` + medición de `scrollHeight` vs `clientHeight` vía JS en las 16 láminas dentro del shell real (el entorno de screenshot seguía fallando); el "desbordamiento" de 47px detectado en la portada resultó ser solo el anillo decorativo sangrando fuera del borde a propósito (recortado por `overflow:hidden`), no contenido real.

## [2026-07-16] ajuste | Multinal S.A.S. — Escenario B, "Módulos" → "Proyectos" + texto Escenario 2 (`multinal-escenario-b/`)

* Todas las menciones a "módulo(s)" cambiadas a "proyecto(s)" (portada, Inversión y Alcance, Mapa del Ecosistema, las 3 tarjetas de Escenarios de Inversión, Próximos Pasos).
* Énfasis explícito en que son proyectos independientes (no partes de un mismo módulo): portada "13 proyectos independientes", título del Mapa del Ecosistema "Trece proyectos independientes, un solo ecosistema digital", sub de Inversión y Alcance y paso 1 de Próximos Pasos también con "independientes".
* Escenario 2 (Desarrollo Mensual): texto de condiciones cambiado de "Pago del primer mes para iniciar el proyecto." a "Pagos posteriores fijos mensuales hasta finalizar."
* PDF final regenerado y verificado.

## [2026-07-16] ajuste | Multinal S.A.S. — Escenario B, reordenamiento final de láminas 13-15 + export (`multinal-escenario-b/`)

* Orden final: 13 Inversión y Alcance, 14 Mapa del Ecosistema, 15 Escenarios de Inversión Propuestos, 16 Próximos Pasos (antes: Mapa, Escenarios, Inversión). Solo se movieron las 3 secciones y se corrigieron sus `s-eyebrow`/`pg`; contenido intacto.
* En la misma sesión también: alineación superior-izquierda del texto en las tarjetas de la columna izquierda de los dúos de agentes (láminas 10 y 11), vía `.agent-col:first-child .feat-card{ justify-content:flex-start; text-align:left; }`.
* PDF final regenerado y verificado (16 páginas, orden correcto) en `multinal-escenario-b/multinal-escenario-b.pdf`.

## [2026-07-16] ajuste | Multinal S.A.S. — Escenario B, lámina de Escenarios de Inversión + relleno de tarjetas en dúos de agentes (`multinal-escenario-b/`)

* **Lámina nueva "Escenarios de Inversión Propuestos"** (13 · entre Mapa del Ecosistema y Inversión y Alcance; deck pasa de 15 a 16 láminas). Nuevo layout `.scenario-grid`/`.scenario-card` (badge de descuento, título, descripción, valor final en gradiente, condiciones de pago) para los 3 escenarios (Digitalización Total -4%, Desarrollo Mensual -3%, Impacto Modular -2%) — los 3 valores finales verificados por cálculo exacto sobre el total ($754.564.260,69 × 0,96/0,97/0,98).
* **Relleno de tarjetas en columnas de 2 agentes (láminas 10 y 11):** `.agent-col .feat-grid` pasó de `align-content:center` (heredado) a `align-content:stretch`, y `.agent-col .feat-card` ganó `justify-content:center` — así las columnas con solo 2 funcionalidades (antes chicas, con hueco debajo) ahora estiran sus tarjetas para ocupar el mismo alto que la columna vecina de 3, en vez de dejar espacio vacío. Pedido por el usuario con una captura anotada con flechas mostrando el hueco a cubrir.
* Verificado con el mismo método de esta sesión (PDF real vía `chrome.exe --headless --print-to-pdf` + rasterizado con PyMuPDF), incluyendo doble chequeo de que el ajuste `stretch` no reintrodujera el recorte ya corregido en las columnas de 3 tarjetas.

* **Método de verificación (nuevo para este deck):** el navegador embebido del entorno de trabajo dejó de responder a `computer{screenshot}` de forma persistente en esta sesión. Se verificó en su lugar exportando el PDF real con `chrome.exe --headless --print-to-pdf` (el mismo comando de `wiki/despliegue.md`) y rasterizando cada lámina con PyMuPDF (`fitz`) a PNG para inspección visual directa — este método es más fiable que el preview porque usa el mismo motor de renderizado que el PDF final entregado al cliente. Recomendado para futuras verificaciones de este deck si el preview del navegador vuelve a fallar.
* **Bug real encontrado y corregido:** en las láminas de dúo de Agentes IA con 3 tarjetas por columna, la 3ª tarjeta y el `tag-row` de integración quedaban recortados por el `overflow:hidden` de `.slide` — el contenido excedía la altura disponible bajo el renderizado real de Chrome (el chequeo de `scrollHeight` hecho en el navegador embebido en la iteración anterior no lo detectó, dato a tener en cuenta: no confiar en esa medición para este entorno). Se resolvió reduciendo el padding/tipografía específicamente dentro de `.agent-col .feat-card` (no se tocó `.feat-card` global, que sigue con los tamaños grandes pedidos).
* **Precios reales:** se reemplazó "Por Definir" por los valores entregados por el usuario en los 13 módulos (7 core + 6 Agentes de IA, ver tabla en la conversación). Los agentes migraron de la nomenclatura `7A–7G` a códigos oficiales `PRY-015/016/017/018/019/021` (PRY-020 queda reservado/vacante — era el Agente Documental, eliminado).
* **Eliminación del Agente IA Documental:** quedaron 6 agentes en vez de 7. La lámina 11 pasó de "Servicio al Cliente + Documental" a "Servicio al Cliente + Gerencial"; el Agente Gerencial ya no tiene lámina propia. Total de láminas: 15 (antes 16). Todas las menciones "14 módulos" → "13 módulos" (portada, Mapa del Ecosistema, Inversión y Alcance, Próximos Pasos).
* **Inversión y Alcance rediseñada:** orden correcto (título → "Opción 1: Inversión Total, Pago Mes a Mes" → cap → precio total) y el bloque de pago 40/40/20 se reemplazó por 3 tarjetas de plan de pago mensual (12/18/24 meses, tipografía sans bold para los números en vez de la serif `--font-display`), con el total y las 3 cuotas calculados exactamente ($754.564.260,69 · $62.880.355,06 · $41.920.236,71 · $31.440.177,53).
* Próximos Pasos: tipografía ampliada (`.step .lab b/span`, `.step .dot`, `.contact-card`) para legibilidad.

## [2026-07-16] ajuste | Multinal S.A.S. — Escenario B, reestructuración de láminas y precios (`multinal-escenario-b/`)

* **Legibilidad:** subida general de tamaños tipográficos (`.s-title` 22→24pt, `.s-lead` 9.8→10.6pt, `.feat-card h4/p`, `.pain-item .tx`, `.eco-chip .t`, etc.) en `styles.css`.
* **Precios por módulo:** se añadió el token `.eco-chip .price` / `.eco-agent-chip .price` en la lámina "Mapa del Ecosistema" — los 14 módulos (7 core + 7 Agentes de IA) muestran `Por Definir` hasta que el costeo se cierre.
* **Agentes de IA — de 7 láminas a 4:** nuevo layout `.agent-duo` / `.agent-col` (dos columnas con divisor vertical) agrupa 2 agentes por lámina: Comercial+Compras, Inventarios+Cartera, Servicio al Cliente+Documental; el Agente Gerencial queda solo (número impar de agentes) reutilizando el layout de 3 columnas previo.
* **Reordenamiento completo (16 láminas):** Portada, Diagnóstico, 6 módulos core, 4 láminas de Agentes IA, Gobierno de Datos (PRY-008, reinsertada tras el Agente Gerencial — se había omitido en el pedido inicial de renumeración, confirmada su ubicación con el usuario), Mapa del Ecosistema (movida de la posición 3 a la 14, casi al cierre), Inversión y Alcance (con el nuevo texto "Opción 1: Inversión Total, Pago Mes a Mes" sobre el precio), Próximos Pasos.
* Verificado sin overflow ni scroll interno en ninguna de las 16 láminas (`s-body.scrollHeight` vs `clientHeight`) vía JS en el navegador; la herramienta de screenshot del entorno falló repetidamente (timeout), así que la verificación visual final quedó pendiente de que el usuario la confirme al ver el PDF/preview.

## [2026-07-15] build | Colbeef S.A.S. — Demo Interactiva (`colbeef-demo/`)

* **Encargo:** página demo con la misma base que `multinal-escenario-b-demo/`: header con logo/colores de Colbeef, pestañas reducidas de 3 a 2 (Presentación · Simulador Demo — se retiró "Panel de Movimientos", contenido de ERP/WMS específico de Multinal que no aplica) y sin botón de sonido (retirado del header y de la lógica en `script.js`, incluyendo la síntesis de audio por WebAudio que traía el original).
* **Apartado Presentación:** las 11 láminas de `colbeef-plan-trabajo/index.html` se transformaron programáticamente (script Python en el scratchpad de la sesión, no versionado) a un namespace `.cb-deck`/`cb-*`, replicando la técnica ya usada en `.b-deck` para Multinal — evita colisión con las clases genéricas del shell (`.slide`, `.active`) y con la lógica de navegación (`navigateSlide`, `jumpToSlide`, autoplay). `totalSlides` en `script.js` ajustado a 11.
* **Apartado Simulador Demo:** réplica funcional de 10 pantallas de un sistema interno real de Colbeef, a partir de las capturas en `recursos/ColBeef/` (`Cliente.png`, `Conductores.png`, `Por Facturar.png`, `Reportes Cartera.png`, `Inventario Cava.png`, `Salidas Cava.png`, `Chats.png`, `Destinos.png`, `Usuarios.png`, `Configuracion (opcional).png`). El sidebar de íconos se mapeó **1:1** comparando qué ícono aparecía resaltado (`active`) en cada captura, confirmando el orden exacto de las 10 secciones. Decisiones de alcance (confirmadas con el usuario antes de construir):
  1. Datos ficticios nuevos, no reutilizados de las capturas.
  2. Interactividad simulada completa (buscador con filtro en vivo, paginación, toggles activo/inactivo, tabs Planillaje/Cava en Destinos, selección de chat con hilo y envío de mensajes, estado vacío→poblado en Inventario Cava al "importar") — todo en `state` de `script.js`, sin backend.
  3. Volumen de datos representativo (6–8 registros por sección), no el volumen exacto de las capturas.
  4. Código de "Panel de Movimientos" eliminado por completo, no solo oculto.
* **Bugs encontrados y corregidos durante la verificación en navegador (Chrome vía preview):**
  1. El script de transformación de CSS generó, para el bloque de tokens, el selector `.cb-deck .cb-deck` (doblemente anidado) en vez de `.cb-deck` — un comentario entre el primer `.cb-deck` (del reemplazo de `:root`) y el propio `.cb-deck{` engañó al tokenizador. Esto hacía que **ninguna** variable CSS (`--cb-bg-0`, `--cb-grad-brand`, etc.) se aplicara nunca, ya que el selector nunca hace match (solo hay un `.cb-deck` en el DOM). Corregido eliminando el prefijo duplicado.
  2. `.cbdeck-slide` heredó `width:var(--cb-slide-w); height:var(--cb-slide-h)` (11in × 6.1875in fijos) del CSS del PDF standalone — un patrón incorrecto para la demo, donde `.slide` (genérico) ya dimensiona la caja de forma responsiva. La referencia de Multinal usa `width:100%; height:100%`. Corregido para igualar el patrón que funciona.
  3. Con `display:flex` en `.cb-cover` (heredado del fix de centrado vertical del PDF) y sin `top/left/right/bottom` explícitos, un elemento `position:absolute` calculaba mal su ancho (colapsaba a ~138px) en vez de llenar el contenedor — comportamiento de "static position" de CSS para abs-positioned sin offsets, que no ocurre con `display:grid` (usado en la referencia Multinal). Corregido agregando `inset:0` explícito a `.cbdeck-slide`. Verificado que las 11 láminas miden 981×700px tras el fix (medido con `getComputedStyle` vía `javascript_tool`, no solo visualmente).
* **Verificación funcional realizada en navegador (no solo lectura de código):** búsqueda en vivo en Clientes (filtró a 1 resultado), selección de chat en Chats (badge de no-leído desaparece, contador se actualiza, hilo se abre), tabs Planillaje↔Cava en Destinos (datos distintos por tab), paginación en Conductores (páginas 1↔2 con datos distintos), filtro por tipo en Usuarios, toast al hacer click en tarjetas de Configuración, navegación de láminas (`navigateSlide`), 2 pestañas confirmadas en el header (sin botón de sonido) vía `read_page`.
* **Entrega:** `presentaciones/colbeef-demo/docs/index.html` (+ `style.css`, `style-colbeef-deck.css`, `script.js`, `assets/`). Listado en [[index]].

---

## [2026-07-15] ajuste | Colbeef S.A.S. — portada: vuelta a alineación izquierda y simetría vertical real (`colbeef-plan-trabajo/`)

* **Corrección del usuario:** el pedido de centrado del ajuste anterior era **vertical**, no
  horizontal — el centrado horizontal aplicado dejó el contenido "desorganizado", y el vertical
  quedó con la lámina casi desbordándose por abajo (mucho aire arriba, casi nada abajo).
* **Horizontal:** `.cover__body` y sus hijos (`eyebrow`, `título`, `kicker`, `client`, `subtitle`)
  vuelven a `text-align:left`; se quitó `justify-self:center`/`margin:0 auto` y se restauró
  `max-width:8.4in` (el título vuelve a acomodarse en 2 líneas en vez de 3).
* **Vertical — causa raíz:** `.cover` usaba `display:grid` con fila central `1fr` y
  `align-self:center` en `.cover__body`; cuando el contenido de esa fila es más alto que el
  espacio disponible, el centrado por grid no reparte el aire de forma confiable y el bloque
  quedaba pegado hacia abajo. **Fix:** `.cover` pasa a `display:flex; flex-direction:column`, y
  `.cover__body` usa `margin-top:auto; margin-bottom:auto` — con flexbox, márgenes automáticos en
  ambos lados de un hijo reparten el espacio sobrante en partes matemáticamente iguales arriba y
  abajo, independientemente de la altura del contenido (a diferencia del centrado por grid usado
  antes). Verificado por medición de píxeles: ~35px de aire sobre el eyebrow vs. ~30px bajo el
  subtítulo antes del borde de metadatos — dentro del margen de error de la medición manual.
* **Regresión encontrada y corregida en el mismo pase:** el `padding-right`/`margin-right`
  negativo usado para evitar el recorte de la "f" itálica de "Colbeef" (ajuste anterior) generaba
  un **recuadro rojo visible** alrededor de todo el texto en gradiente al exportar a PDF —peor que
  el hairline documentado. **Fix:** se reemplazó por `background-size:112% 100%;
  background-position:0 0;` en `.gradient-text`, `.gt-cyan` y `.gt-violet` — agranda el área de
  pintado del gradiente sin tocar el modelo de caja (padding/margin), evitando el artefacto de
  recuadro. Verificado que la "f" ya no se corta y que las tarjetas con `gt-cyan`/`gt-violet` en
  otras láminas (equipo, stack) no muestran el recuadro.
* **Entrega:** PDF regenerado (`colbeef-plan-trabajo.pdf`, 11 páginas, sin cambio de conteo).
  Verificación visual píxel por píxel de la portada + 3 láminas interiores para descartar
  regresiones del cambio de técnica del gradiente.

---

## [2026-07-15] ajuste | Colbeef S.A.S. — eliminación de cierre y corrección de portada (`colbeef-plan-trabajo/`)

* **Encargo del usuario:** (1) eliminar la última lámina ("Cierre y Próximos Pasos", innecesaria);
  (2) la portada se veía desorganizada — la "f" final de "Colbeef" salía cortada y el contenido se
  salía del margen; pidió centrado horizontal y verificación visual píxel por píxel.
* **Lámina 12 eliminada:** deck pasa de 12 a **11 láminas**. La lámina 11 (Plan de Comunicaciones)
  queda como cierre; su número de pie de página ya era "11", no requirió renumeración.
* **Causa raíz de la "f" cortada:** `background-clip:text` sobre un gradiente pinta el fondo
  únicamente dentro de la caja (padding-box) del elemento. El trazo itálico de la "f" en Playfair
  Display Black excede el ancho de avance del glifo (overhang), quedando fuera de esa caja — esa
  porción no recibe gradiente y se ve "cortada". **Fix:** se agregó `padding-right:.14em` (con
  `margin-right:-.14em` para no desplazar contenido siguiente) a `.gradient-text`, `.gt-cyan` y
  `.gt-violet` en `styles.css`, ampliando el área de pintado del gradiente sin mover el layout.
* **Centrado horizontal:** `.cover__body` pasó de alineado a la izquierda (con `max-width:8.4in`
  dejando un vacío grande a la derecha) a `text-align:center` + `justify-self:center` +
  `margin:0 auto` con `max-width:7.6in`; `.cover__client` (logo + "PARA") ahora centra con
  `justify-content:center`. Topbar y fila de metadatos inferior se mantienen a todo el ancho
  (tratamiento de header/footer estándar del sistema, no es lo que el usuario señaló como
  "desorganizado").
* **Verificación pixel por pixel:** export a PDF con Chrome headless → render de la portada a
  2.5x resolución con PyMuPDF → recorte y zoom sobre la "f" (confirmado el trazo completo, sin
  recorte) y sobre el borde inferior (confirmado que la fila de metadatos no toca ni se corta
  contra el borde de la lámina). Se verificaron además 3 láminas interiores para descartar
  regresiones por el cambio de `.gradient-text` (usado en varios títulos internos) — sin cambios
  de layout, ya que el ajuste es solo de área de pintado, no de tamaño de caja visible.
* **Entrega:** PDF regenerado (`colbeef-plan-trabajo.pdf`, ahora 11 páginas). Actualizado en
  [[index]].

---

## [2026-07-15] build | Colbeef S.A.S. — Plan de Trabajo y SLA (`colbeef-plan-trabajo/`)

* **Encargo:** deck de 12 láminas a partir del "Plan de Trabajo y Acuerdos de Nivel de Servicio
  (SLA)" firmado (PDF fuente, 26 enero 2026): ecosistema de automatización e IA para la operación
  de planta de Colbeef (Recepción/Planillaje IA con OCR, Cava Automatizada, Agente Conversacional,
  Reportes, Facturación Inteligente), integrado con el software existente Informatix.
* **Paleta:** extraída por muestreo de píxeles del logo (`recursos/ColBeef S.A.S`) — rojo
  `#D93A2E`/`#B8341F` (wordmark) → verde `#2E8B4F`/`#1B5E33` (isotipo). Registrada en
  [[temas-por-cliente]] y en el tile `.t-cbf` de `presentaciones/_temas-demo/index.html`.
* **Sin lámina de inversión:** el documento fuente es un Plan de Trabajo/SLA, no una cotización
  con cifras — se omitió para no inventar montos.
* **Numeración de fases:** el Plan de Trabajo firmado salta de Fase 2 a Fase 4 (sin Fase 3) —
  se respetó tal cual en el cronograma, sin inventar una fase faltante.
* **Bugs de verificación en PDF (Chrome headless) encontrados y corregidos:**
  1. Grid de equipo (3×3) invadía la fila del footer — se redujeron paddings/fuentes de
     `.team-card` y el `gap` del grid.
  2. `background-clip:text` (gradiente) en números grandes con `white-space:nowrap`
     (`.stat-card .big`, ej. "Máx. 4h") pintaba un recuadro visible alrededor del texto al
     exportar — se resolvió usando color sólido (`--cyan`/`--violet`) en vez de gradiente para
     esos elementos. Documentado en [[temas-por-cliente]].
  3. Nodo de timeline "S3–6" se partía en dos líneas por ancho insuficiente — se ensanchó
     `.phase .node` y se agregó `white-space:nowrap`.
  4. Correo largo en tarjeta de comunicaciones se desbordaba del borde — se agregó
     `overflow-wrap:anywhere` a `.feat-card p`.
  5. Balance de espacio (§5.1): `.timeline` y `.roles-split > div` no distribuían el aire
     sobrante — se les agregó `flex:1; justify-content:center` para centrar el contenido en
     vez de dejarlo pegado arriba con una franja vacía abajo.
* **Hairline conocido:** el título en gradiente de la portada muestra el hairline documentado en
  [[sistema-diseno]] §"Trampa técnica"; se confirmó que también aparece en el deck de referencia
  Multinal ya entregado, por lo que se aceptó como artefacto sistémico de Chrome headless, no
  como defecto introducido por este deck.
* **Entrega:** PDF exportado (`colbeef-plan-trabajo.pdf`, 12 páginas verificadas 1:1 contra las
  12 láminas). Listado en [[index]].

---

## [2026-07-10] build | Multinal S.A.S. — demo interactiva Escenario B (`multinal-escenario-b-demo/`)

* **Encargo:** duplicar `multinal-escenario-c-demo/` (app demo con 3 apartados: Presentación,
  Simulador Interactivo, Panel de Movimientos) y reemplazar **únicamente** el apartado
  "Presentación" por el contenido del deck `multinal-escenario-b/` (19 láminas), dejando
  Simulador y Panel intactos. Carpeta final renombrada a `multinal-escenario-b-demo/`.
* **Hallazgo técnico:** las 26 láminas de Escenario C dentro del demo usan un sistema de
  componentes propio del shell (`.slide-frame`, `.slide-header`, navegación por
  `data-slide`/`jumpToSlide()` en `script.js`), mientras que el deck de Escenario B usa un sistema
  de diseño completamente distinto (`.s-header`, `.s-body`, `.feat-grid`, tokens propios). No era
  un simple copiar/pegar — se consultó al usuario cómo integrar ambos.
* **Decisión (confirmada con el usuario):** insertar el deck B **tal cual, con su propio diseño**
  (no re-maquetarlo al estilo del shell C). Para lograrlo sin romper nada:
  - Las 19 láminas de B se namespacearon bajo la clase `.b-deck` en una hoja de estilos nueva
    (`docs/style-escenario-b.css`), con todos sus tokens y clases genéricas prefijadas `b-`
    (`.b-gradient-text`, `.b-contact-card`, `.b-badge-confidential`, etc.) para no chocar con las
    clases de igual nombre ya usadas por el shell/Simulador/Panel (`.gradient-text`,
    `.contact-card`, `.badge-confidential`).
  - Cada `<section>` de lámina B conserva las clases `slide` + `data-slide="N"` (1–19) que la
    navegación existente (`navigateSlide()`, contador, barra de progreso) ya sabe manejar —
    solo se le sumó la clase `bdeck-slide` (en vez de `.slide` propio de B) para aplicar su estilo
    visual sin pisar el `.slide` de posicionamiento/show-hide del shell.
  - Se copiaron a `docs/assets/` el logo `logo-cliente.png` y las 14 fuentes locales (`fonts/`)
    que el deck B requiere vía `@font-face`.
  - `state.totalSlides` en `script.js`: `26` → `19`; contador inicial `1 / 26` → `1 / 19`.
* **Verificación:** confirmado con diff que `style.css`, `script.js` (salvo `totalSlides`) y
  `README.md` quedaron sin cambios frente al original; las secciones de Simulador y Panel en
  `index.html` son **byte-idénticas** al original. Navegación probada vía JS en el navegador
  (loop completo de 19 láminas, cambio entre las 3 vistas) — sin errores de consola ni fallos de
  red. El screenshot del navegador del entorno falló por un problema de infraestructura ajeno al
  contenido (se reproduce en una página en blanco); se verificó por `get_page_text` + pruebas
  funcionales en su lugar.
* **Pendiente/nota para el usuario:** el `<title>` y la meta-descripción del `<head>` de
  `multinal-escenario-b-demo/docs/index.html` siguen diciendo "Escenario C" (no se tocaron,
  siguiendo la instrucción de modificar solo el apartado Presentación). Avisar si se desea
  actualizarlos también.

## [2026-07-10] build | Multinal S.A.S. — Plataforma Empresarial 100% Propia, Escenario C (26 láminas)

* **Encargo:** Escenario C (la opción más ambiciosa de 2 para Multinal), a partir de 6 documentos
  fuente (Documento 6C, Alcances RFI/RFP, Cadena de Valor AS-IS, Mapa de Procesos AS-IS,
  Arquitectura Tecnológica AS-IS) y `Multinal SAS - Cotizacion C.xlsx` (11 hojas PRY).
* **Decisión de granularidad (confirmada con el usuario):** el ERP propio agrupa 6 funciones de
  negocio (Compras/Inventarios/Comercial/Facturación/Cartera/Despachos) — cada una recibió su
  propia lámina en vez de una sola lámina "PRY-ERP", igual criterio aplicado por consistencia al
  WMS propio (Recepción/Ubicaciones/Picking-Packing/Despachos-Trazabilidad, 4 láminas).
* **Estructura (26 láminas):** Portada (badge "Escenario C") · Diagnóstico · Visión y 6 Principios
  de Diseño (nueva lámina, sin precedente en B) · Mapa del Ecosistema (5 plataformas + banda de 6
  agentes) · ERP (6 láminas) · WMS (4 láminas) · CRM Ampliado · Firma Electrónica · Gobierno de
  Datos · 6 Agentes de IA (Logístico y Fidelización 100% nuevos; Comercial/Compras/Inventarios/
  Cartera con tarjetas "BASE" heredadas del agente homólogo del Escenario B + tarjetas
  "AMPLIACIÓN C" para las capacidades nuevas — decisión de diseño para no fabricar alcance no
  sustentado en la fuente) · Sustitución de la Arquitectura Legada (nueva lámina: estado de
  ILIMITADA/Siigo/Trazabilidad/Pedbox/Excel) · Inversión y Alcance (**sin cifra**) · Próximos pasos.
* **Verificación:** medición programática de bounding boxes en las 26 láminas → 1 intrusión de
  1px detectada y corregida (texto de `pay-note` recortado); 0 problemas tras el ajuste. Revisión
  visual de portada y 2 láminas densas (CRM Ampliado 4 tarjetas, Sustitución Legada 5 tarjetas).
* **Archivos:** `presentaciones/multinal-escenario-c/` (index.html, styles.css idéntico al de
  Escenario B, assets/ reutilizados), PDF de 26 páginas exportado con Chrome headless.

## [2026-07-10] marca | Nuevo estándar obligatorio: fondo gris claro frío + gradiente de marca

* **Decisión del usuario:** el fondo gris claro neutro usado en Multinal Escenario B deja de ser
  una excepción de un solo deck y pasa a ser el **estándar obligatorio para toda presentación
  nueva** (`CLAUDE.md` Regla 2, reemplaza la regla de fondo oscuro de 2026-07-08). Se le suma un
  requisito nuevo: la gama del **gradiente de marca del cliente** debe superponerse como un
  `--bg-wash` sutil (~5–9% opacidad) sobre la base gris — no queda en fondo gris plano.
* **Logo Campuslands corregido:** el PNG maestro (`recursos/Logo Campuslands Horizontal
  Azul.png`) tiene relleno transparente muy asimétrico (138px arriba vs. 80px abajo sobre 885px
  de alto) que lo hacía ver chico y descentrado a igual `height` CSS. Se recortó a su contenido
  visible + padding simétrico ~6% para el deck de Multinal. Nueva regla en `CLAUDE.md` y
  `wiki/temas-por-cliente.md`: **recortar siempre** el logo maestro antes de copiarlo a
  `assets/` de un deck nuevo, nunca usar el PNG de `recursos/` tal cual.
* **Pendiente (no ejecutado en esta sesión):** los decks previos a esta fecha (Miami Aqua
  Tours, GreenMetal, Mchaileh, Compumax ×2, Ve a la Segura) siguen en el sistema oscuro legado
  y probablemente arrastran el mismo defecto de logo sin recortar — no se tocaron porque el
  usuario pidió actualizar específicamente el deck de Multinal; queda como trabajo futuro si se
  solicita.
* **`wiki/temas-por-cliente.md`** — receta §2 reescrita para el estándar claro; catálogo de
  Multinal actualizado con los tokens reales (antes tenía los tokens oscuros previos a este
  cambio).

## [2026-07-10] ajuste | Multinal Escenario B — correcciones de dato + tema claro (excepción)

* **Correcciones de contenido** (fuente: `_FullServices Cotizaciones Multinal (Proyectos).xlsx`,
  hoja `PRY-008 - Gobierno de Datos`):
  * Slide "Portal de Clientes" (PRY-002): se retiró la mención a FedEx en "Tracking logístico de
    despachos" — Multinal opera flota propia de vehículos de despacho, no usa FedEx.
  * Slide "Portal de Proveedores" (PRY-003): la tarjeta de escalabilidad ahora dice "integración
    con Cadena de Valor" (antes "Workflow").
  * **Renombrado global de PRY-006**: "Motor de Workflow Corporativo" → **"Cadena de Valor"** en
    su propia lámina, el Mapa del Ecosistema y el tag del Agente 7E.
  * **Nuevo módulo PRY-008 — Gobierno de Datos** (lámina 17/19): MDM, diccionario corporativo,
    depuración del legado, linaje y — punto clave del cliente — estándares de captura por
    **código de barras** que reemplazan los catálogos hoy dispersos en **Excel anidados** por
    línea de producto, habilitando el mapeo automático del Portal de Proveedores (PRY-003). El
    deck pasa de 13 a **14 módulos** (18 → **19 láminas**); actualizado el conteo en portada,
    kicker, mapa del ecosistema e Inversión y Alcance.
* **⛔ Excepción de tema — fondo claro (solo este deck):** por pedido explícito del usuario
  ("SOLO SERA EN ESTA PRESENTACION"), `presentaciones/multinal-escenario-b/styles.css` rompe la
  regla de fondo oscuro obligatorio del sistema de diseño: fondo gris claro frío (`--bg-0:#F2F3F5`
  → `--bg-2:#FFFFFF`), texto oscuro (`--text-hi:#14161B`), acentos naranja/índigo profundizados
  para contraste (`--cyan:#A6480A`, `--violet:#5A3FBF`), punto "Confidencial" en azul-cian frío
  más saturado. El logo de Campuslands se cambió a la variante **azul** (antes blanca, invisible
  sobre fondo claro). Esta excepción **no aplica a ningún otro deck** ni cambia la convención
  general de `wiki/sistema-diseno.md`.

---

## [2026-07-09] build | Multinal S.A.S. — Ecosistema Digital Corporativo, Escenario B (18 láminas)

* **Encargo:** Escenario B de 2 propuestas para Multinal S.A.S., a partir de `Multinal SAS -
  Alcances por Proyecto B.xlsx` y `Multinal SAS - Cotizacion B.xlsx`. Regla del cliente: cada
  módulo/agente en **una sola lámina** (nunca repartido en 2), sin límite de número de hojas.
* **Estructura (18 láminas):** Portada (rotulada "Escenario B") · Diagnóstico · Mapa del
  Ecosistema (13 módulos) · PRY-001 a PRY-006 (CRM, Portal Clientes, Portal Proveedores,
  Repositorio Documental, BI, Workflow — una lámina c/u con 5–7 funcionalidades desglosadas de
  la cotización con numeración RF) · PRY-007A a 007G (7 agentes de IA, uno por lámina, con tag
  de integración al módulo core relacionado) · Inversión y Alcance (**sin cifra** — "Valor por
  definir", misma estructura visual `.invest`/`.pay` que otros decks) · Próximos pasos.
* **Paleta:** derivada del logo real (`recursos/Multinal S.A.S.png`, muestreado con PIL) —
  naranja `#FF7A00` del isotipo → índigo `#312883` del wordmark, fondo ámbar-negro teñido, punto
  "Confidencial" en cian frío (regla de marca cálida). Registrada en [[temas-por-cliente]] y
  `presentaciones/_temas-demo/index.html`.
* **Bug corregido en QA:** el primer borrador desbordaba el `.feat-grid` de los módulos de
  5–7 tarjetas hacia el footer (30–110px de intrusión, detectado por el usuario como
  "superposición de texto"); se compactó `feat-card`/`feat-grid` (paddings, fuentes, gaps) y se
  redujo `s-title`/`s-lead`. Verificado con medición programática (bounding boxes) en las 18
  láminas + revisión visual del PDF renderizado con PyMuPDF — 0 desbordes tras el fix.
* **Archivos:** `presentaciones/multinal-escenario-b/` (index.html, styles.css, assets/),
  PDF de 18 páginas exportado con Chrome headless.

## [2026-07-09] lint | Nueva norma obligatoria: balance de espacio (ni vacío ni apretado)

* **Motivo:** tras el ajuste de la timeline de GreenMetal (6 fases en 1 fila dejaba ~40% de la
  lámina vacío debajo), el usuario pidió formalizar la regla: el agente debe evitar espacios
  "vacíos" en las láminas, pero sin caer en el extremo opuesto de apretar todo.
* **`CLAUDE.md`** — nueva regla obligatoria en "Estándar de calidad de diseño": si un bloque deja
  una franja vacía notable (>15–20% de la altura de `.s-body`), redistribuir contenido (más
  filas/columnas, tarjetas/tipografía más grandes, o mayor `gap`/padding) antes de entregar.
* **`wiki/sistema-diseno.md`** — nuevo anti-patrón "Espacio vacío/muerto sin usar" (§5) y nueva
  sección **§5.1 Balance de espacio: ni vacío ni apretado**, con checklist de decisión y el caso
  real de GreenMetal como referencia.

---

## [2026-07-09] ajuste | GreenMetal: timeline de 6 fases en 2 filas + precio actualizado

* **Lámina 04 (`presentaciones/greenmetal-fyswap/index.html` + `styles.css`):** la línea de 6 fases
  en una sola fila quedaba pequeña y dejaba mucho espacio vacío debajo. Se reestructuró en
  `.timeline` con dos `.timeline-row` (3 fases arriba, 3 abajo), cada fila con su propia línea
  conectora; se agrandaron nodos, títulos y texto de cada fase para aprovechar el espacio.
  Verificado sin overflow (bottom de `.timeline` a 447px dentro de una lámina de 594px).
* **Precio actualizado (lámina 07 · Inversión):** de `$42.182.849,99` a **`$60.217.679`**.
* Exportado PDF actualizado (`greenmetal-fyswap.pdf`).

---

## [2026-07-08] ajuste | Mchaileh re-tematizado a verde de marca + 3 reglas nuevas

* **Re-tema Mchaileh (`presentaciones/mchaileh-crm-ia/styles.css`):** el deck seguía en la paleta
  *default* cian/violeta pese a que su logo es 100% verde (lima + hoja/esmeralda). Derivé la paleta
  del logo: gradiente **`#9BD534→#4FD07A→#22B06B→#1FA95F`** (hoja/kelly-forward → esmeralda, sin teal)
  sobre **fondo bosque teñido** (`--bg-0:#040A06 … --bg-deep:#081A0F`). Reemplacé todos los rgba
  cian/violeta/azul hardcodeados por verdes; introduje `--bg-deep` (antes `#0B1120` fijo en `.slide`,
  `.glow-a`, `.glow-b`). Se conserva el rojo semántico en la columna "Antes/HOY". Verificado en navegador.
* **Distinción vs GreenMetal:** GreenMetal = lima-forward → teal, fondo casi neutro; Mchaileh = hoja
  → esmeralda, fondo verde-bosque. Catálogo actualizado en `wiki/temas-por-cliente.md`.
* **Regla 1 (título):** `<title>` ahora = **razón social / nombre corporativo completo** (con sufijo
  legal), p. ej. `Compumax Computer S.A.S.`. Antes era el nombre corto a secas. (`CLAUDE.md` §head.)
* **Regla 2 (color):** todo diseño se inspira en los colores de marca **sobre el oscuro base actual**;
  solo cambia el hue de acento (Azul→Rojo, cian→verde) y el tinte del fondo. (`CLAUDE.md` §Build.3.)
* **Regla 3 (registro):** cada empresa tematizada se registra en `wiki/index.md` **y** en un tile de
  `presentaciones/_temas-demo/index.html` (+ bloque en `temas-por-cliente.md`). (`CLAUDE.md` §Build.9.)
* **Demo de temas:** tile Mchaileh actualizado al verde de marca y **agregado tile de Ve a la Segura**
  (faltaba). Pendiente: export a PDF de Mchaileh y compartir link.

## [2026-07-08] marca | Favicon (isotipo Campuslands) + título = nombre de empresa en toda web

* **Regla nueva estipulada en `CLAUDE.md`** (sección "Requisitos de `<head>`"): toda web debe tener
  (1) favicon = isotipo de Campuslands **sin texto** (casco de astronauta), en `assets/favicon.png`
  de cada deck, referenciado con `<link rel="icon" ...>`; (2) `<title>` = **nombre de la empresa**
  cliente, limpio (sin "Propuesta…", sin S.A.S).
* **Isotipo creado:** recorté el texto del "Logo Campuslands Vertical Azul.png" → `recursos/isotipo-campuslands.png`
  y `recursos/favicon-campuslands.png` (256×256). Fuente de verdad del favicon.
* **Regla nueva de flujo:** al terminar de crear/modificar cualquier presentación, **compartir en el chat**
  el link de Vercel `https://fullservice-presentaciones.vercel.app/<slug>/index.html`.
* **Aplicado a los 8 decks existentes** (compumax-asistente-ia, compumax-mejoras-multitipo, greenmetal-fyswap,
  mchaileh-crm-ia, miami-aqua-tours-ampliado, miami-aqua-tours, ve-a-la-segura, _temas-demo). Verificado en
  navegador: favicon 200, título = nombre de empresa.

## [2026-07-08] ajuste | Fix tipografías en producción (Vercel): fuentes autocontenidas por deck

* **Problema:** en Vercel las tipografías caían a fuentes de respaldo (serif/itálica genérica). Causa: los `@font-face` apuntaban a `../../recursos/fonts/…`, ruta que sube fuera de la carpeta del deck; al desplegar cada presentación desde su propia raíz, `recursos/` queda fuera del despliegue → 404 → fallback. También violaba la regla "cada deck autocontenido".
* **Solución:** cada presentación ahora empaqueta sus `.ttf` en su propio `assets/fonts/` y los `@font-face` apuntan a `assets/fonts/…` (ruta relativa local). Verificado sirviendo cada deck desde su raíz: fuentes 200, ruta vieja 404; render correcto en navegador sin errores de consola.
* **Alcance:** 6 decks premium (compumax-asistente-ia, compumax-mejoras-multitipo, greenmetal-fyswap, mchaileh-crm-ia, miami-aqua-tours-ampliado, ve-a-la-segura) + `_temas-demo`.
* **miami-aqua-tours (legacy):** usaba Cambria/Calibri (fuentes de sistema, propietarias, prohibidas por el CLAUDE.md). Convertida a Playfair Display (títulos) + Poppins (cuerpo) empaquetadas. Cambio visual menor, aprobado por el usuario.
* **Convención nueva a mantener:** NUNCA usar `../../recursos/fonts/` en un deck; siempre copiar las fuentes usadas a `presentaciones/<slug>/assets/fonts/` y referenciarlas con ruta relativa local. `recursos/fonts/` es solo la fuente de verdad.

## [2026-07-08] ajuste | Compumax mejoras multi-tipo: inversión simplificada y eliminación de cierre

* Lámina de inversión (pág. 5): se retiró la sección "Forma de pago" (caption + filas 40/40/20). Se conserva título, "Inversión Total" + monto, texto descriptivo y nota "Valor en pesos…". Recompuesta como hero centrado (`.invest-solo`).
* Eliminada por completo la última lámina "Próximos Pasos".
* El deck pasó de 6 a **5 láminas**; footer de la última queda en 05; gap con footer verificado positivo. PDF re-exportado (5 páginas).
* Nota: cambios **específicos de este deck** por pedido del usuario; NO se promovieron al sistema de diseño ni a la plantilla base.

## [2026-07-08] ajuste | Compumax mejoras multi-tipo: unificación de láminas y nuevo precio

* Unificación de contenido: pág. 3 (NLP) + pág. 4 (Catálogo FORZA) → una sola lámina "Inteligencia de tipo y catálogo"; pág. 5 (Ajustes conversacionales) + pág. 6 (QA) → una sola lámina "Conversación y calidad".
* Nuevo componente de diseño `.duo` (dos bloques temáticos por lámina, con barra de acento azul + violeta) agregado al `styles.css` del deck.
* El deck pasó de 8 a **6 láminas**; footers y numeración renumerados; verificado gap positivo con el footer en todas las láminas internas.
* Precio de cotización actualizado: $11.532.730 → **$8.688.486 COP** (pago 40/40/20 sin cambios).
* Re-exportación a PDF verificada (6 páginas, sin desbordes).

## [2026-07-08] build | Cotización de mejoras multi-tipo de inmueble para Compumax

* Nueva presentación independiente `presentaciones/compumax-mejoras-multitipo/`: adenda técnica al Asistente de IA Inmobiliario de Compumax ya entregado (sin usar la palabra "Fase 2" por pedido del usuario).
* Alcance derivado de la hoja "Compumax" del archivo `FullServices NAL 2026 - Compumax Multi-Tipo (1).xlsx`: detección NLP del tipo de inmueble, filtro de catálogo por tipo integrado a FORZA, ajustes conversacionales no-bloqueantes por fase y QA de regresión end-to-end. Incorpora **Oficinas** como quinto tipo (junto a Apartamento/Casa/Local/Lote ya cubiertos).
* 8 láminas con el mismo sistema v2 y gradiente azul de marca Compumax; se reutiliza el logo de Campuslands y el wordmark recreado de Compumax en cada header.
* Inversión $11.532.730 COP · pago 40/40/20 · sin lámina de cronograma (a pedido del usuario).
* Exportación a PDF verificada (8 páginas, sin desbordes).

## [2026-07-07] build | Creación y compilación de la propuesta técnico-comercial para Ve a la Segura

* Generación de propuesta de alcance en HTML/CSS estructurada en 8 diapositivas para Agente Conversacional Orbit.
* Implementación del sistema v2 Premium con paleta de color ámbar y variable `--bg-deep` como placeholder ante falta del logo del cliente.
* Exportación a PDF exitosa. Valores de inversión marcados como "Pendiente".

## [2026-07-06] setup | Inicialización de la base de conocimiento (wiki) para el Agente de Presentaciones

* Creación de la estructura base de la wiki en base al archivo de configuración [CLAUDE.md](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/CLAUDE.md) y al manual comercial proporcionado por el usuario.
* Poblado de los siguientes archivos de conocimiento:
  - [index.md](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/wiki/index.md): Catálogo y navegación de la wiki.
  - [perfil-usuario.md](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/wiki/perfil-usuario.md): Identidad de Campuslands Full Service y audiencias objetivo.
  - [flujo-trabajo.md](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/wiki/flujo-trabajo.md): Secuencia de pasos obligatorios (alcance → planificación → diseño → exportación).
  - [despliegue.md](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/wiki/despliegue.md): Directivas CSS `@page` y comando de Google Chrome headless para generar PDF.
  - [marca-campuslands.md](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/wiki/marca-campuslands.md): Paleta de colores, tipografía y distribución de logotipos.
  - [sistema-diseno.md](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/wiki/sistema-diseno.md): Tokens CSS, plantillas en grid y restricciones críticas contra anti-patrones visuales de IA.
  - [plantilla-base.md](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/wiki/plantilla-base.md): Especificación secuencial de las 16 diapositivas comerciales estándar.

## [2026-07-06] build | Creación y compilación de la propuesta técnico-comercial para Miami Aqua Tours

* Procesamiento de los requerimientos de la propuesta y extracción del alcance de cotización de `$161.340.551,95 COP` con 22 módulos a partir del archivo Excel `FullServices USA 2026 .xlsx`.
* Creación de la carpeta autocontenida de la presentación en [presentaciones/miami-aqua-tours/](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/miami-aqua-tours/) con:
  - [index.html](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/miami-aqua-tours/index.html): Estructura semántica de 16 diapositivas.
  - [styles.css](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/miami-aqua-tours/styles.css): Estilos e implementaciones del sistema de diseño oscuro de Campuslands con variables CSS oficiales.
  - `assets/`: Logotipo de la marca Campuslands y logotipo del cliente Miami Aqua Tours.
* Exportación a PDF de alta resolución mediante Chrome Headless en modo `--no-margins` a [miami-aqua-tours.pdf](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/miami-aqua-tours/miami-aqua-tours.pdf).
* Verificación exitosa del conteo de páginas (16 páginas exactas).

## [2026-07-06] marca | Rediseño del sistema visual a v2 Premium (gradientes + fuentes locales + dinamismo)

* A pedido del usuario, se eleva el nivel de diseño al de un "diseñador profesional",
  tomando como referencia una portada tipo Unidrogas (serif gradiente + brackets + anillos).
* **Cambios en la wiki:**
  - `marca-campuslands.md`: nueva paleta con gradientes protagonistas (cian→azul→violeta→magenta)
    + acento ámbar; tipografía v2 (Playfair Display, Montserrat, Poppins, DM Serif); reglas
    de logos verificadas (logos SÍ en portada; blanco sobre fondo oscuro).
  - `sistema-diseno.md`: bloque `@font-face` a `recursos/fonts/`, tokens v2, utilidades
    (texto en gradiente, brackets, anillos, badge confidencial), 9 arquetipos de layout para
    dinamismo, anti-patrones actualizados (incl. hairline de `background-clip:text` en print),
    y flujo de verificación (preview + PDF).
  - `plantilla-base.md`: **se elimina la regla de 16 láminas fijas**; ahora es biblioteca
    narrativa flexible con conteo libre.
  - `CLAUDE.md` (proyecto y Downloads): estándar de calidad v2; se corrige referencia rota
    `estructura-propuesta.md` → `plantilla-base.md`.
* **Lámina de referencia construida y verificada:** portada de prueba en
  [presentaciones/miami-aqua-tours-ampliado/](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/miami-aqua-tours-ampliado/index.html)
  con export a PDF (1 página, sin hairlines, fuentes locales y gradiente OK).

## [2026-07-06] build | Deck completo Miami Aqua Tours v2 (8 láminas) sobre el alcance v0.1

* Se completó la propuesta [miami-aqua-tours-ampliado](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/miami-aqua-tours-ampliado/index.html)
  a **8 láminas** (< 10, según pedido), cada una con layout distinto para dinamismo:
  Portada · El Reto (split+cita) · La Solución (4 pilares) · Capacidades Venta (grid M1–M3) ·
  Capacidades Operación (grid M4–M6) · Diferenciador QR (flujo + nota M7) · Inversión (statement) ·
  Cuándo Empezamos (CTA + contacto).
* Fuente de datos: `Miami Aqua Tours - Cotizacion de Alcance.pdf` (v0.1). Cotización de cierre
  **$268.900.920 COP** y contacto **Gabriela Pedraza Rueda** (Directora Full Service Global,
  gabriela.pedraza@campuslands.com, +57 300 302 8555) provistos por el usuario.
* **Verificación:** export a PDF con Chrome headless → **8 páginas exactas** (confirmado por
  `/Count` del PDF; el conteo por form-feeds de pdftotext infla en 1). Se ajustó la paginación a
  `page-break-before` entre láminas para evitar página fantasma. Logos, gradientes, fuentes y
  alineación revisados lámina por lámina.

## [2026-07-06] ajuste | Miami Aqua Tours v2 → precio en USD y fusión de capacidades

* **Precio:** la cotización pasó de `$268.900.920 COP` a **USD $84,000** (por pedido del usuario:
  ya no se cotiza en COP). Actualizado el número grande y el subtexto de la lámina de Inversión.
* **Fusión de láminas:** se unificaron las dos láminas de capacidades (Venta M1–M3 y Operación
  M4–M6) en **una sola** con grid compacto 3×2 (`.cards6`, bullets condensados). El deck bajó de
  **8 a 7 láminas**. Renumerados eyebrows y footers subsiguientes.
* **Verificación:** export a PDF → **7 páginas exactas** (`/Count 7`); sin desbordes en la lámina
  fusionada (medición en navegador: 0 overflow en body y en las 6 tarjetas); precio USD confirmado.

## [2026-07-06] build | Nueva propuesta C.I. Green Metal S.A.S. — FySwap (8 láminas)

* Cliente nuevo: **C.I. Green Metal S.A.S.** ("Minería Urbana", reciclaje/exportación de metal).
  Presentación en [presentaciones/greenmetal-fyswap/](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/greenmetal-fyswap/index.html)
  sobre el módulo **FySwap** (Logística de Salida y Aseguramiento de la Calidad).
* **Fuente de datos:** `GreenMetal_Cotizacion_de_Alcance_FySwap_Recalculado.pdf`. Total real
  **$42.182.849,99 COP**, esfuerzo **85 días**, prioridad Alta. Moneda COP (confirmado por el usuario).
* **Logo del cliente:** extraído del PDF fuente `GM-PRO-TI-2026-001.pdf` con PyMuPDF y se le hizo
  transparente el fondo negro → `assets/logo-cliente.png` (verde sobre oscuro, ideal).
* **Diseño:** se clonó el sistema v2 de miami-aqua-tours-ampliado pero con la **paleta desplazada
  al verde de GreenMetal** (lima→esmeralda→teal→cian). Layouts nuevos: `.timeline` (6 fases) y
  `.qc-grid` (5 controles QA/QC). 8 láminas: Portada · Reto · Solución FySwap · Proceso (timeline) ·
  QA/QC · Integraciones & Usuarios · Inversión · Cuándo Empezamos (contacto Gabriela Pedraza).
* **Verificación:** export a PDF → **8 páginas exactas** (`/Count 8`); medición en navegador sin
  desbordes en las láminas internas; logos Campuslands (izq) + Green Metal (der) en todas.

## [2026-07-07] build | Mchaileh S.A.S — CRM Inmobiliario + Asistente IA (13 láminas)

* Cliente nuevo: **Mchaileh S.A.S** (inmobiliaria). Presentación en
  [presentaciones/mchaileh-crm-ia/](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/mchaileh-crm-ia/index.html)
  sobre un **CRM inmobiliario con IA integrada** (asistente Luce/Lucía).
* **Fuentes de datos:** `Mchaileh_CRM_Cotizacion_Alcance_Recalculado.pdf` (autoritativa) +
  `FullServices NAL 2026 - Mchaileh.xlsx` (días por especialidad) + `..._v0.1_1.pdf` (alcance abierto).
  Total **$24.917.398,68 COP**, esfuerzo **52.5 días**, prioridad Alta. Moneda **COP** (confirmado).
  Reparto de días: Frontend 11.5 · IA 10 · Backend 13 (BS 4.5 + BM 8.5) · QA 7.5 · UX 5 · DB 3.5 · Impl. 2.
* **Decisiones confirmadas por el usuario (AskUserQuestion):** COP · pago **40/40/20** · desglose
  de inversión **por área (8 filas)**, no ítem por ítem.
* **Logo del cliente:** `mchaileh_logopng.png` era transparente pero con **texto negro** (invisible
  sobre fondo oscuro). Se generó `assets/logo-cliente-blanco.png` con PIL recoloreando los píxeles
  grises/negros a blanco y conservando el verde de la casa/eslogan. Se usa la variante blanca en
  portada e internas.
* **Diseño:** clon del sistema v2 (paleta de marca con gradientes). Layouts nuevos reutilizables:
  `.stats` (4 cifras de línea base), `.arch` (diagrama de 3 capas: canales → núcleo CRM+IA → valor),
  `.cards4` (grid de 4 módulos), `.ba` (antes/después), `.who` (quiénes somos), `.team` (esfuerzo +
  8 chips de rol), `.timeline` (5 fases), `.invest2` (tabla por área + pago 40/40/20). 13 láminas:
  Portada · Lo que nos contaron · Reto · Solución/Arquitectura · Capacidades I · Capacidades II ·
  IA en foco · Antes/Después · Quiénes somos · Equipo & Esfuerzo · Cronograma · Inversión · Cierre.
* **Fix técnico (hairline):** los `<div>` con `background-clip:text` (`.tag`, `.num`, `.n`, `.big`)
  dibujaban la línea del gradiente en el borde de la caja al exportar (confirmado con crop a 320dpi).
  Se corrigió con `display:inline-block; width:fit-content;` para que la caja se ajuste al glifo
  (ver [[sistema-diseno]] §5). Los gradientes inline (`<em>`/`<span>`: título, totales) ya eran limpios.
* **Verificación:** export a PDF → **13 páginas exactas** (11×6.1875in); 0px de desborde interno en
  las 13 láminas (medición en navegador); sin errores de consola; crops a 150–320dpi confirman
  gradientes, fuentes locales y logos correctos. Puerto de preview movido a 5599 (5500 ocupado por VS Code).

## [2026-07-07] build | Compumax S.A.S — Asistente de IA Inmobiliario (14 láminas)

* Cliente nuevo: **Compumax S.A.S** (inmobiliaria/constructora). Presentación en
  [presentaciones/compumax-asistente-ia/](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/compumax-asistente-ia/index.html)
  sobre un **Asistente de Ventas Inteligente** (clon Andes Constructora) integrado a **FORZA ERP**.
* **Fuentes de datos:** `Compumax_Cotizacion_Alcance_Recalculado.pdf` (autoritativa, 6 págs) +
  `Compumax_Cotizacion_Alcance_Final.pdf` (alcance detallado) + `FullServices NAL 2026 - Compumax.xlsx`.
  Total **$72.399.974,24 COP**, esfuerzo **154.5 días**, prioridad **Muy Alta**. Moneda COP, pago 40/40/20
  (confirmado por el usuario). Desglose por **6 bloques** (verificado que suman exacto al total):
  Estructura 5.525.993 · F1 Descubrimiento 9.778.955 · F2 Diseño 8.488.483 · F3 Desarrollo 25.162.910 ·
  F4 QA/Piloto 12.298.358 · F5 Transversales 11.145.276.
* **Logo del cliente:** NO vino como archivo (solo imagen en el chat). Confirmado con el usuario:
  **recrear el wordmark**. Se reconstruyó "Compumax" en HTML con Poppins local (`.wm`: "Compu" gris
  #9AA0A6 + "max" azul #1B9BD7), usado en portada e internas. Si luego llega el PNG oficial, se cambia.
* **Diseño:** clon del sistema v2 partiendo de `mchaileh-crm-ia/styles.css`, con la **paleta de
  gradiente sesgada al azul de marca Compumax** (`--grad-brand` cian→#1B9BD7→azul→índigo, sin magenta).
  Layout nuevo: `.statement` + `.type-row` (4 tipos de inmueble: apartamento/casa/local/lote, con SVGs).
  14 láminas: Portada · Oportunidad · Reto · Solución/Arquitectura · Cómo conversa (flow 4 pasos) ·
  Capacidades I · Capacidades II · Multi-tipo de inmueble · Seguridad & cumplimiento · Metodología
  (timeline 5 fases) · Quiénes somos · Equipo & Esfuerzo · Inversión · Cierre.
* **Nota de datos:** los días por especialidad del Excel sumaban ~164 con ruido; se usó el total
  autoritativo del PDF (**154.5 días**) y en la lámina de equipo se muestran las disciplinas sin
  días por rol (para no exponer cifras que no cuadran).
* **Verificación:** export a PDF → **14 páginas exactas** (11×6.1875in); 0px de desborde interno en las
  láminas 2–14 (los 74px de la portada son las `deco-rings` decorativas recortadas por `overflow:hidden`,
  patrón ya validado); wordmark, gradiente azul y fuentes locales confirmados por crops a 150dpi.

## [2026-07-07] marca | Theming por cliente — paleta (y fondo) derivados del logo

* **Motivo:** el usuario pidió que la paleta deje de ser repetitiva; **cada empresa** debe tener
  colores distintos y los **fondos** deben adaptarse al color del logo, manteniendo el estilo premium.
* **Cambio de sistema:** se introduce el token `--bg-deep` (antes `#0B1120` hardcodeado en
  `.slide`/`.glow-a`/`.glow-b`) para que el **fondo sea 100% tematizable**. Se define el **contrato de
  theme-tokens** (lo único que cambia por cliente) y una **receta** logo→paleta (hue análogo para el
  gradiente; fondo teñido con S≈10–22% / L≈4–9%; glows y bordes con el hue; texto tinte leve).
* **Nueva página wiki:** [[temas-por-cliente]] con receta, contrato y **catálogo de paletas** listo
  para pegar (Campuslands default, Compumax azul, GreenMetal lima/teal, Mchaileh esmeralda/teal +
  ejemplos cálido y púrpura). Regla: dos clientes del mismo color se separan por sub-hue.
* **Prueba visual:** [`presentaciones/_temas-demo/`](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/_temas-demo/index.html)
  — misma lámina en 6 paletas con fondo teñido distinto (render por Chrome headless, verificado).
* **Docs actualizados:** `CLAUDE.md` (nuevo paso obligatorio "Paleta por cliente" en Build + flujo +
  estándar de calidad), `wiki/sistema-diseno.md` (`--bg-deep` + anti-patrón "no reusar paleta"),
  `wiki/marca-campuslands.md` (cian/violeta = tema default), `wiki/index.md`.
* **Pendiente (opcional, si el usuario lo pide):** re-tematizar los decks existentes (Compumax,
  GreenMetal, Mchaileh, Miami) pegando su bloque de [[temas-por-cliente]] en `:root` — hoy Mchaileh y
  Compumax aún usan base azul-noche; GreenMetal tiene acentos verdes pero fondo aún navy.

## [2026-07-07] build | Ve a la Segura — Agente Conversacional Orbit (8 láminas, corrección de borrador)

* Cliente nuevo: **Ve a la Segura** (nombre legal en documentos fuente: "Vianla Segura"; se usa
  "Ve a la Segura" por ser el nombre que usa el usuario). Presentación en
  [presentaciones/ve-a-la-segura/](file:///c:/Users/Full%20Service/Downloads/PresentationsDesigner/presentaciones/ve-a-la-segura/index.html)
  sobre el **agente conversacional Orbit** (atención multicanal, clasificación de eventos, venta de
  boletería, voz clonada).
* **Fuentes de datos:** `Ve a la segura.pdf` (alcance sin precios, "pendiente de costear") +
  `Ve a la Segura.xlsx` (hoja "Vianla Segura", costeo real). Total **$21.808.295,04 COP**, ~48 días.
  Moneda COP, pago 40/40/20 (confirmado por el usuario en turno previo a compactación).
  **Advertencia del Excel:** "días por especialidad NO validados... no usar como cotización final sin
  validación" — por eso NO se agregó lámina de equipo con días por rol, y la lámina de inversión
  incluye una nota honesta: "Estimación preliminar del alcance v0.1; sujeta a validación técnica final."
* **Este era el primer deck con el sistema de theming por cliente** (ver [[temas-por-cliente]]).
  Sin logo oficial de Ve a la Segura → paleta **"concierto"** confirmada por el usuario (violeta-negro
  + gradiente rosa→magenta→violeta→índigo) y wordmark recreado ("VE A LA **SEGURA**", "SEGURA" en
  gradiente de marca).
* **Continuación de sesión:** el borrador ya existía (creado antes de un cambio de modelo/compactación)
  pero con bugs de implementación. Se analizó y corrigió:
  1. **Paleta incorrecta:** el `:root` tenía la paleta cálida ámbar/coral (ejemplo de
     `wiki/temas-por-cliente.md`) en vez de la violeta "concierto" confirmada. Corregido.
  2. **`--bg-deep` hardcodeado** en `.glow-a`/`.glow-b` (`#0B1120`) en vez de `var(--bg-deep)`. Corregido.
  3. **Wordmark placeholder:** portada y 6 headers usaban un `<h2>`/`<div>` con estilo inline en vez
     del patrón `.wm` (como Compumax). Corregido y generalizado (`.wm .b` ahora usa `var(--grad-brand)`
     en vez de un color hardcodeado, reutilizable para cualquier cliente sin logo).
  4. **Lámina "La Solución" rota:** usaba `class="pillars"`, que no existe en este `styles.css`
     (se perdió al clonar desde Compumax). Convertida a `.type-row`/`.type-card` (sí definidas).
  5. **Lámina "Módulos" rota:** usaba `class="cards6"` (no definida, sin `display:grid`) con
     `grid-template-columns` inline sin efecto. Cambiada a `.cards4` (que sí define `display:grid`).
  6. **Lámina de Inversión con placeholders sin rellenar:** `$ [Por Costear] COP`, `[XX] días`.
     Reemplazada por tabla `.invest2` con el desglose real de 5 bloques (suma exacta al total) y
     pago 40/40/20.
  7. **Lámina de Cierre completamente rota:** sin `<header>` (sin logos), sin `.s-eyebrow`, usando
     `rem` en vez de `pt`/`in` (inconsistente con el resto del sistema) y `padding-top:100px` que
     causaba **367px de colisión con el footer** (el checker de overflow contra el borde de la lámina
     no lo detectaba, porque el desborde ocurría *dentro* de la caja de `.slide`, invadiendo la fila
     del footer del grid interno). Reconstruida con el patrón `.cta` (pasos + tarjeta de contacto)
     que ya estaba definido en el CSS pero sin usar.
  8. Colisión menor similar en la lámina "Humanización" (tarjetas M3/M4 vs. footer, gap -1 a -13px)
     y en "Inversión" (nota de pago desbordaba a 3ª línea). Corregidas con padding/tipografía más
     compactos y texto más corto.
* **Lección de verificación:** el chequeo de overflow contra `.slide` (usado en decks previos) **no
  detecta colisiones internas contra el footer** cuando el layout es CSS Grid con filas fijas. Se
  añadió un chequeo adicional: medir el gap entre el último elemento de `.s-body` y el `top` de
  `.s-footer` (debe ser positivo) en cada lámina interna, no solo el desborde contra el borde exterior.
* **Verificación:** export a PDF → **8 páginas exactas** (11×6.1875in); 0px de desborde contra el
  borde de cada lámina Y gap positivo contra el footer en las 7 láminas internas; sin errores de
  consola; crops a 150–300dpi confirman paleta violeta, wordmark y ausencia de hairlines.

## [2026-09-29] build | Globant — Dojo × Globant (modelo de células y supervisión), 10 láminas
* Brief: notas de reunión + Excel *Proyección Financiera Campuslands–Globant V2*. Límite de 10 láminas pedido por el usuario: se fusionaron "punto de partida + recalibración" y "escenario financiero + alianza 70/30".
* Carpeta `presentaciones/globant-dojo/` (slug corto), paleta lima/oliva/bosque + negro (ver [[temas-por-cliente]]), fondo gris claro frío con wash lima, shell interactivo de un solo escenario, PDF de 10 páginas.
* Registrado en las 3 ubicaciones: `wiki/index.md`, tile en `_temas-demo` + bloque en `temas-por-cliente.md`, entrada `decksData` en el portal + logo crudo en `assets/logos/Globant.png`.
* Cifras del Excel citadas con hoja/celda (`06_P&G`, `08_CAPEX`, `09_Info_Socios`). Se dejó en la lámina 3 que la nómina de desarrolladores del P&G es "Sin DOJO". No se calcularon cifras derivadas (p. ej. 5 células × 10–15 personas) porque contradicen el dimensionamiento de 3–4 seniors para 38 chicos: pendiente de aclarar con el usuario.
* Pendientes: razón social completa de Globant para el `<title>`; confirmar que el Excel es el escenario recalibrado; el `git push` de `presentaciones/` devolvió 403 (Claude GitHub App sin acceso a la org) — el commit queda local.
* Lección: el export a PDF caía a Georgia/Times en pesos de Playfair no usados en la lámina activa; corregido con `preloadAllFonts()` + `--virtual-time-budget`.

## [2026-09-29] ajuste | Globant — recorte a 5 láminas y nuevos textos (a pedido del usuario)
* Pie de página de todas las internas: "Exploramos · Despegamos · Conquistamos" + "Propuesta Globant Dojo · Campuslands".
* Portada: se eliminaron la etiqueta superior, la píldora de subtítulo, la segunda línea del título y el kicker; queda "Dojo × Globant" (60pt, Globant en gradiente) y "Preparado por: Campuslands S.A.S. BIC".
* Lámina 2 reescrita (talento senior, productos escalables, licencias por sector, SaaS/ERP/CRM); el título baja a 20pt en una línea. Lámina 4: "Un senior, diferentes proyectos" y "2–3 juniors y mid-juniors por proyecto" (también en el texto de cada fila, para mantener coherencia).
* Láminas 5 y 6 unificadas: de la 6 solo pasan los dos textos indicados (sin la cifra 38, sin la matriz de puntos, sin la tarjeta oscura de "3–4 seniors"). Láminas 7–10 eliminadas (el deck queda sin cierre).
* Textos del usuario corregidos ortográficamente ("irán", "específicos", "técnica", "operación") y sin mayúsculas indebidas.
* Sigue sin resolver: la etiqueta "Revisión actual" de la lámina 2 ya no describe el contenido de esa tarjeta.

## [2026-09-29] ajuste | Globant — lámina 6 "Lo que nos están pidiendo hoy las empresas"
* Nueva última lámina con 5 soluciones del portafolio (Plataforma LMS KHC, Agente maestro con IA, Nébula, Agente con IA de RR. HH., Facturación electrónica), cada una con descripción y "¿Qué incluye?". Distribución tomada de la imagen del usuario: 3 columnas, tarjetas con ícono circular y título; el LMS ocupa dos filas por ser la de más contenido (5 tarjetas no llenan una cuadrícula 3×2).
* Título corregido de "no están pidiendo" a "nos están pidiendo" (errata evidente). En Facturación se quitó el inciso "según la descripción del portafolio" (nota interna, no texto de cara al cliente) y se fusionaron bullets que repetían la descripción (Agente maestro, Facturación) para que todo cupiera sin bajar de 8 pt.
* No se incluyó la franja inferior de beneficios de la imagen de referencia porque el usuario no entregó ese contenido.
* Verificación: PDF de 6 páginas, sin fuentes de respaldo, lectura visual sin desbordes contra el footer.

## [2026-09-29] ajuste | Globant — rediseño de la lámina 6 (mosaico dinámico)
* A pedido del usuario ("no me pareció el diseño… más dinámica, mejor distribución, quita el pie de página y los logos de arriba si es necesario"): la lámina 6 pasa a **pantalla completa, sin header de logos ni footer** (se pierde también el número de página en esa lámina; la barra superior del shell interactivo sigue mostrando los logos).
* Composición tipo mosaico: LMS KHC como tarjeta **negra a doble altura** (ancla, eco del wordmark, halo lima), Agente maestro y Facturación en **blanco**, Nébula y Agente de RR. HH. en **verde lima con tinta negra** (contraste alto), insignias 01–05, chip "5 soluciones" y chevrón decorativo.
* Con los ~85 px recuperados la tipografía subió de ~8 pt a 8,5–9,3 pt y se restauraron los bullets originales del LMS (los fusionados en Agente maestro y Facturación se mantienen para que quepan).
* Lección de layout: en una cuadrícula `1fr 1fr` con contenido variable, el `min-content` de las filas hace que la cuadrícula se salga de la lámina aunque el contenedor tenga `min-height:0`; se resolvió recortando tipografía/márgenes hasta que las filas cupieran, y verificando el borde inferior en el PDF.

