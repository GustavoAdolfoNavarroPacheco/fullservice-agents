# Bitácora — Agente Desarrollador de Cotizaciones

Registro cronológico, append-only. Prefijo `## [YYYY-MM-DD] <tipo> | <descripción>`
con tipo ∈ {setup, build, ajuste, deploy, lint}.

## [2026-08-05] ajuste | Jerarquía flexible Módulo→Submódulo→Funcionalidad(es) + nuevas reglas de XLSX

A pedido explícito del usuario, tras detectar que las cotizaciones nuevas quedaban más
cortas en volumen de información que las elaboradas a mano (comparación directa:
`CasaBlanca` —desarrollada por el agente, patrón fijo "1 submódulo = 1 descripción"— vs.
`Allied Steel` —hecha a mano, cardinalidad libre de bullets por submódulo—, ambas en
`FullServices_NAL_2026.xlsx`):

1. **Jerarquía de columnas L/M/N reinterpretada**: L=Módulo (sin cambio), **M pasa de
   "Funcionalidad" a "Submódulo"** (encabezado de agrupación, puede repetirse varias veces
   bajo un mismo módulo), **N pasa de "Detalle técnico de una M" a "Funcionalidad atómica"**
   (puede repetirse varias veces bajo un mismo submódulo — mínimo 1, sin techo). Prohibido
   forzar el patrón antiguo de 1 par M+N por bullet. Actualizado en `CLAUDE.md` §Reglas del
   XLSX/PDF y en los espejos `wiki/plantilla-xlsx.md`, `wiki/diseno-pdf-cotizacion.md`,
   `wiki/marca-campuslands.md` §5 y `wiki/perfil-usuario.md`.
2. **Días estimados (B:K) reasignados**: antes iban en la fila M; ahora van **siempre en
   cada fila N** (funcionalidad), nunca en M (submódulo, que no representa una unidad de
   esfuerzo). Cada N bajo un mismo M lleva su propio estimado independiente.
3. **Tipografía formalizada**: Arial — Módulo 11pt negrita, Submódulo 10pt negrita,
   Funcionalidad/Detalle técnico 10pt regular. Ya se aplicaba de facto (ver entradas previas
   del log) pero no estaba documentada explícitamente; ahora vive en `wiki/marca-campuslands.md`
   §5 y `wiki/diseno-pdf-cotizacion.md`.
4. **Nueva excepción a la zona intocable**: además de `Y{barra_gris+2}` (`=Y1/0.6`), se
   agrega `R{barra_gris+3}` = `0.1` (10%, celda de porcentaje AIU) — reemplaza el default de
   la plantilla maestra (40%). Documentado en `CLAUDE.md` §Reglas del XLSX §5 y en
   `wiki/plantilla-xlsx.md` §5.
5. **Referencia de verdad actualizada**: `cotizaciones/compumax/Compumax Computer S.A.S -
   Cotizacion.xlsx` sigue siendo válido para B:K, la fórmula de Y y la zona intocable, pero
   **ya no es referencia de cardinalidad L/M/N** (sigue el patrón antiguo, superado). No se
   reprocesan cotizaciones ya entregadas — este ajuste aplica hacia adelante.

Pendiente (resuelto abajo, 2026-08-05/build Comultrasan): primera cotización construida bajo
esta regla se convierte en la nueva "referencia de verdad" de cardinalidad para
`wiki/plantilla-xlsx.md` §2.

## [2026-08-05] build | Financiera Comultrasan — Asistente Conversacional Orbit (Canales Digitales)

Primera cotización construida en el repo `QuoteDeveloperV2` (repo nuevo, sin historial previo:
no traía `wiki/index.md`, `wiki/log.md`, `scripts/` ni ejemplos en `cotizaciones/` — se crearon
en este build). Fuente de alcance: PDF `Propuesta_Comultrasan_Campuslands_v4.pdf` (propuesta
comercial preparada por Gabriela Pedraza Rueda) + transcripción completa de la reunión de
levantamiento de necesidades con Angela Latorre (Jefe de Canales Virtuales y Electrónicos,
Financiera Comultrasan). Usuario confirmó explícitamente incluir los módulos de fase posterior
(Ventas & Crédito, PQRS & Jurídico) como opcionales dentro de la misma cotización.

- **Alcance**: 5 módulos — M1 Agente Orquestador Orbit, M2 Canales Digitales (alcance inicial
  acordado: transferencias Bre-B, pago de crédito, transferencias generales, registro en
  Agencia Virtual, FAQs de uso), M3 Integraciones y Canales de Entrada (WhatsApp Business,
  botón Canales Digitales del portal web, HubSpot), M4 Ventas y Crédito (opcional, fase
  posterior), M5 PQRS y Jurídico (opcional, fase posterior). Cardinalidad de funcionalidades
  por submódulo: 1 a 4, fiel a lo descrito en la propuesta y la transcripción — primera
  cotización de este repo construida bajo la regla de jerarquía flexible (2026-08-05),
  confirmando que la regla funciona con datos reales de cliente.
- **XLSX**: sin necesidad de insertar filas (alcance cupo en las filas 8-44 de las 112
  disponibles antes de la barra gris en fila 120, posición sin cambios respecto a la
  plantilla maestra). Excepciones aplicadas: `Y122='=Y1/0.6'`, `R123=0.1` (ambas confirmadas
  vacías/default antes de escribir). Recalculado con `scripts/recalc.py` (LibreOffice, con los
  fixes de PATH/AF_UNIX de `project-quotedeveloper-xlsx-workflow`): 0 errores fuera de
  `A140:A144` (defecto preexistente conocido de la plantilla). TOTAL general: **$48.378.375
  COP** (`AC1`).
- **PDF**: generado con `reportlab` (no existía script de PDF reutilizable en este repo nuevo;
  se construyó desde cero siguiendo `wiki/diseno-pdf-cotizacion.md` — paleta clara, grid
  completo, jerarquía Módulo→Submódulo→Funcionalidad, Arial 11/10/10). Doble verificación
  contenido-precio: suma de funcionalidades de cada módulo == subtotal del módulo (columna Y
  del XLSX), y suma de todos los módulos + fases transversales == TOTAL general (`AC1`) —
  ambas coincidieron exactamente. Sin logo de cliente (Comultrasan no aportó uno) — solo
  logo Campuslands.
- **Entregables**: `cotizaciones/comultrasan/Financiera Comultrasan - Cotizacion de Alcance.pdf`
  y `cotizaciones/comultrasan/Financiera Comultrasan - Cotizacion.xlsx` (copia de la plantilla
  maestra con las demás hojas de clientes eliminadas antes de trabajar sobre ella).
- **Pendiente para el usuario**: validar los días estimados por especialidad en el XLSX (no
  fueron confirmados línea por línea con Comultrasan, solo el desglose de alcance del PDF);
  decidir si se comparte el logo de Comultrasan para agregarlo al PDF.

## [2026-08-06] build | Alcaldía Municipal de Girón — Portafolio de 13 proyectos (Proyecto 1/13)

Fuente de alcance: `Propuesta Proyectos Alcaldía Girón v 1.0.docx` (portafolio preliminar de
13 productos, sección 13 "Matriz preliminar de priorización"). El documento contiene 32
productos detallados en 9 secciones; el usuario confirmó que los 13 nombres de la matriz de
priorización son los 13 proyectos a cotizar (cada uno = una cotización independiente), y el
mapeo de qué secciones detalladas incluye cada uno (varios combinan 2 sub-productos de una
misma sección). Estructura de entrega acordada: `cotizaciones/alcaldia-municipal-de-giron/
<slug-proyecto>/` (subcarpeta por proyecto dentro del cliente). Ritmo de trabajo acordado:
un proyecto a la vez, con validación del PDF de alcance antes de pasar al XLSX de cada uno.

**Proyecto 1/13 — Agentes IA de Correo por Dependencia (modelo general).** Consolida §4.3
(Plataforma Base de Agentes IA Especializados por Dependencia) + las 7 instancias específicas
por dependencia (Salud 5.6, Desarrollo Social 6.5, Cobro Coactivo 7.3, Ordenamiento 8.3,
Seguridad 9.3, Control Interno 10.3, Tránsito 11.3) en una única cotización "modelo general",
por instrucción explícita del usuario: este producto es distinto porque su implementación real
se adapta por Secretaría (reglas, taxonomía, KB y escalamiento propios), pero comparte
infraestructura. Nota de variación incluida en el PDF antes de la tabla.

- **Alcance**: 2 módulos — M1 Plataforma Base de Agentes IA de Correo (3 submódulos, 11
  funcionalidades), M2 Parametrización por Secretaría/Dependencia (7 submódulos, uno por
  dependencia, 1 funcionalidad cada uno). PDF validado por el usuario antes de construir el XLSX.
- **XLSX**: sin insertar filas (alcance en filas 8-37 de 112 disponibles). Barra gris sin
  desplazamiento (fila 120). Excepciones `Y122='=Y1/0.6'` y `R123=0.1` confirmadas vacías/default
  antes de escribir. Recalculado con `recalc.py`: 0 errores fuera de `A140:A144` (defecto
  preexistente). TOTAL general: **$29.084.165 COP** (`AC1`), incluidas las 4 filas transversales
  (**$6.065.404 COP**) + módulos (**$23.018.762 COP**) — reconciliado exactamente.
- **PDF**: reescrito con banda "FASES TRANSVERSALES DEL PROYECTO" (4 filas con precio) y
  separador "ALCANCE FUNCIONAL" antes de los módulos, replicando el patrón visto en
  `cotizaciones/comultrasan/` — el primer borrador del PDF (validado en alcance/redacción) no
  incluía esta banda porque aún no había XLSX; se agregó al sincronizar precios reales.
  Sin logo de cliente (Alcaldía no aportó uno) — solo logo Campuslands.
- **Entregables**: `cotizaciones/alcaldia-municipal-de-giron/agentes-ia-correo-por-dependencia/
  Alcaldía Municipal de Girón - Agentes IA de Correo por Dependencia - Cotizacion de
  Alcance.pdf` y `... - Cotizacion.xlsx`.
- **Pendiente para el usuario**: validar los días estimados por especialidad del XLSX (no
  vienen de una reunión de levantamiento con la Alcaldía, sino de criterio de desarrollador
  sobre el documento preliminar); definir si se agrega un logo de la Alcaldía.

**Nota de nomenclatura (post-entrega Proyecto 1)**: el usuario reportó que Excel no podía
abrir el XLSX del Proyecto 1 ("no hemos encontrado..."), con un archivo de bloqueo `~$...`
confirmando que Excel sí llegó a abrir el archivo original antes de fallar. Causa probable:
tildes en el nombre de archivo combinadas con ruta larga (255 caracteres, cerca del límite
de 260 de Windows). **Desde el Proyecto 2 en adelante, los nombres de archivo y carpeta usan
ASCII sin tildes** (`Alcaldia Municipal de Giron - <Proyecto> - Cotizacion[.xlsx| de
Alcance.pdf]`) — el contenido interno de los documentos sigue en español con tildes normales,
solo cambia el nombre de archivo en el sistema de archivos. Los archivos del Proyecto 1 ya
fueron renombrados en el mismo esquema.

### Proyecto 2/13 — Gestión Documental Inteligente (§4.1)

- **Alcance**: 1 módulo, 4 submódulos, 8 funcionalidades — mapeo 1:1 con las 8 capacidades
  listadas en §4.1 del documento fuente (sin combinar ni fragmentar). PDF validado por el
  usuario antes de construir el XLSX.
- **XLSX**: filas 8-20 (de 112 disponibles), sin insertar filas. Excepciones `Y122='=Y1/0.6'`
  y `R123=0.1` confirmadas y aplicadas. 0 errores de fórmula fuera de `A140:A144`. TOTAL
  general: **$16.725.595 COP** (`AC1`) = transversales (**$5.373.562 COP**) + módulo
  (**$11.352.033 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/alcaldia-municipal-de-giron/gestion-documental-inteligente/
  Alcaldia Municipal de Giron - Gestion Documental Inteligente - Cotizacion de Alcance.pdf`
  y `... - Cotizacion.xlsx`. Sin logo de cliente.

**Nota de rutas (post-entrega Proyecto 2)**: el usuario reportó que Excel seguía sin poder
abrir el XLSX aun con nombre sin tildes. Se reprodujo el error directamente con Excel real
(COM automation): abrir vía script funcionó con PowerShell/`openpyxl`, pero el mismo archivo
fallaba en Excel real con "no hemos encontrado el archivo" en rutas de ~236-255 caracteres; el
mismo archivo copiado a una ruta de 34 caracteres abrió sin problema. **Causa raíz: Excel tiene
su propio límite de ruta, más bajo que el límite general de Windows (260)** — no es un tema de
tildes ni de OneDrive (confirmado: `Downloads` no está redirigido a OneDrive en esta máquina).
**Esquema de nombres corregido desde este punto**: `cotizaciones/giron/<slug-proyecto>/
Cotizacion.xlsx` y `Cotizacion de Alcance.pdf` (sin repetir cliente/proyecto en el nombre de
archivo, ya está en la ruta de carpetas) — reduce la ruta completa a ~135-150 caracteres.
Verificado abriendo ambos archivos con Excel real (COM) tras el cambio. Los Proyectos 1 y 2 se
movieron a `cotizaciones/giron/agentes-correo/` y `cotizaciones/giron/gestion-documental/`.

**Nota de granularidad (post-entrega Proyecto 2)**: el usuario preguntó si el nivel de detalle
extraído era el máximo posible del documento fuente. Se confirmó mapeo 1:1 de cada bullet de
"Capacidades propuestas" sin inventar ni omitir. El usuario pidió además: (1) dividir bullets
compuestos (varias capacidades unidas por "y"/comas) en funcionalidades atómicas separadas,
cuando representan capacidades genuinamente distintas — no cuando son dimensiones/niveles de
una sola capacidad (ej. "por series, subseries, expedientes y dependencias" se mantiene como
una sola fila porque son niveles de una misma taxonomía, no funcionalidades independientes); y
(2) agregar una nota de contexto (sin precio) con "Componente tecnológico principal" y
"Clasificación" de cada producto, tomados directo del documento fuente, bajo el objetivo de
cada PDF. **Ambas reglas quedan vigentes para los 13 proyectos desde aquí.** Proyectos 1 y 2
reconstruidos bajo esta regla:

- **Proyecto 1** pasó de 18 a 30 funcionalidades (M1: 11→16, M2: 7→14). Nuevo TOTAL:
  **$30.846.315 COP** (antes $29.084.165 COP).
- **Proyecto 2** pasó de 8 a 15 funcionalidades. Nuevo TOTAL: **$19.320.001 COP** (antes
  $16.725.595 COP).

Ambos re-verificados: 0 errores de fórmula fuera de `A140:A144`, reconciliación exacta
transversales+módulos=TOTAL, fuentes L/M/N correctas, y apertura confirmada con Excel real.

### Proyecto 3/13 — Observatorio de Salud Pública (§5.1)

- **Alcance**: 1 módulo, 4 submódulos, 9 funcionalidades (subieron de 7 a 9 bullets fuente al
  dividir "Mapas de calor y georreferenciación" y "Históricos e informes gerenciales" en
  atómicas separadas, regla vigente desde 2026-08-06). Nota de contexto técnico incluida.
- **XLSX**: filas 8-21, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$14.248.773 COP** (`AC1`) = transversales
  (**$4.267.324 COP**) + módulo (**$9.981.448 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/salud-publica/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (134 caracteres de ruta). Sin logo de
  cliente.

### Proyecto 4/13 — IVC Sanitario (§5.4)

- **Alcance**: 1 módulo, 5 submódulos, 13 funcionalidades (10 bullets fuente, 3 divididos en
  atómicas: "Programación y asignación de visitas", "Registro de resultados y calificación",
  "Integración con 'Negocio Más Confiable' y QR"). Nota de contexto técnico incluida.
- **XLSX**: filas 8-26, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$18.749.358 COP** (`AC1`) = transversales
  (**$4.892.233 COP**) + módulo (**$13.857.126 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/ivc-sanitario/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (134 caracteres). Sin logo de cliente.

### Proyecto 5/13 — Auditoría EPS/IPS y Planes de Mejora (§5.5)

- **Alcance**: 1 módulo, 4 submódulos, 11 funcionalidades (8 bullets fuente, 3 divididos:
  "OCR y extracción estructurada", "Seguimiento de compromisos y evidencias", "Validación
  humana de hallazgos y respuestas"). Nota de contexto técnico incluida.
- **XLSX**: filas 8-23, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$14.109.200 COP** (`AC1`) = transversales
  (**$4.447.447 COP**) + módulo (**$9.661.753 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/auditoria-eps-ips/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (138 caracteres). Sin logo de cliente.

**Ajuste Proyecto 1 (post-entrega Proyecto 5)**: el usuario pidió aclarar que el cobro de
parametrización del Módulo 2 por cada dependencia aplica solo si esa dependencia todavía no
tiene un agente de correo construido previamente. Se agregó esa aclaración a la nota de
variación del PDF (`cotizaciones/giron/agentes-correo/Cotizacion de Alcance.pdf`) — no cambia
funcionalidades, días ni el XLSX, solo el texto de la nota. TOTAL sin cambios:
$30.846.315 COP.

### Proyecto 6/13 — Cobro Coactivo y Alertas de Prescripción (§7.1 + §7.2)

- **Alcance**: 2 módulos (M1 Sistema Integral de Gestión de Cobro Coactivo, M2 Motor de
  Alertas de Términos y Riesgo de Prescripción, combinados por instrucción del usuario), 7
  submódulos, 16 funcionalidades (13 bullets fuente, 3 divididos: "Generación masiva de
  cartas y actos administrativos", "Control de embargos y notificaciones", "Dashboard de
  cartera y carga de trabajo"). Incluye nota del documento sobre desarrollos previos de Cobro
  Coactivo (recomendación de auditoría funcional antes de iniciar como producto nuevo).
- **XLSX**: filas 8-32, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$21.721.845 COP** (`AC1`) = transversales
  (**$5.193.439 COP**) + módulos (**$16.528.406 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/cobro-coactivo/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (135 caracteres). Sin logo de cliente.

**Ajuste Proyecto 1 (post-entrega Proyecto 6)**: el usuario pidió que la misma aclaración de
cobro condicional (parametrización de M2 aplica solo si la dependencia no tiene ya un agente
construido) quedara también en el XLSX, no solo en el PDF. Como el XLSX no tiene una celda de
texto libre apropiada para esto (y la zona O:AC/121-140 es intocable), se usaron
**comentarios de celda de Excel** (`openpyxl.comments.Comment`, sin tocar ningún valor ni
fórmula): uno general en `L28` (encabezado de M2) y uno específico por dependencia en cada
`M29/M32/M35/M38/M41/M44/M47`. Verificado: 0 errores nuevos tras recalcular, TOTAL sin cambios
($30.846.315 COP), comentarios visibles al abrir con Excel real.

### Proyecto 7/13 — Trámites y Agente de Ordenamiento (§8.1 + §8.2)

- **Alcance**: 2 módulos (M1 Plataforma de Trámites Urbanísticos y Certificados, M2 Asistente
  IA Normativo, combinados), 7 submódulos, 15 funcionalidades (13 bullets fuente, 2
  divididos: "Asignación y seguimiento", "Generación de certificados y formatos"). Nota de
  contexto técnico incluida.
- **XLSX**: filas 8-31, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$19.992.383 COP** (`AC1`) = transversales
  (**$5.072.356 COP**) + módulos (**$14.920.027 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/ordenamiento/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (133 caracteres). Sin logo de cliente.

### Proyecto 8/13 — Gestión de Procesos Disciplinarios (§10.1 + §10.2)

- **Alcance**: 2 módulos (M1 Sistema de Gestión de Procesos Disciplinarios, M2 Plataforma de
  Audiencias Virtuales con Transcripción, combinados), 7 submódulos, 16 funcionalidades (13
  bullets fuente, 3 divididos: "Etapas y actuaciones", "Búsqueda y reportes", "Acceso
  restringido y auditoría"). Nota de contexto técnico incluida.
- **XLSX**: filas 8-32, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$20.295.200 COP** (`AC1`) = transversales
  (**$4.907.428 COP**) + módulos (**$15.387.773 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/disciplinarios/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (135 caracteres). Sin logo de cliente.

### Proyecto 9/13 — Comités, Actas y Compromisos (§4.2 + §6.1)

- **Alcance**: 2 módulos. §4.2 (transversal) y §6.1 (Desarrollo Social) describen capacidades
  casi idénticas (transcripción, borrador de acta, decisiones/compromisos, histórico) — para
  no cobrar dos veces lo mismo, M1 cubre la plataforma general una sola vez (9 funcionalidades,
  8 bullets fuente de §4.2 con 1 división: "Integración con calendarios y alertas") y M2 cubre
  solo el esfuerzo adicional específico de §6.1 para comités de alta carga documental (Justicia
  Transicional, COMPOS): 2 funcionalidades. Nota explicando este criterio incluida en el PDF.
- **XLSX**: filas 8-25, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$16.404.950 COP** (`AC1`) = transversales
  (**$4.928.776 COP**) + módulos (**$11.476.174 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/comites-actas/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (134 caracteres). Sin logo de cliente.

### Proyecto 10/13 — Mesa de Víctimas y Pagos (§6.3)

- **Alcance**: 1 módulo, 3 submódulos, 10 funcionalidades (8 bullets fuente, 2 divididos:
  "Registro de miembros y sesiones", "Asistencia y evidencias"). Nota de contexto técnico
  incluida.
- **XLSX**: filas 8-21, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$13.663.746 COP** (`AC1`) = transversales
  (**$4.102.396 COP**) + módulo (**$9.561.350 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/mesa-victimas/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (134 caracteres). Sin logo de cliente.

### Proyecto 11/13 — Reparto de Querellas (§9.1 + §9.2)

- **Alcance**: 2 módulos (M1 Sistema Inteligente de Reparto de Querellas y Solicitudes, M2
  Agente de Orientación Inicial - Comisarías de Familia, combinados), 7 submódulos, 14
  funcionalidades (12 bullets fuente, 2 divididos: "Trazabilidad y alertas", "Priorización y
  escalamiento inmediato de situaciones sensibles"). Nota de contexto técnico incluida,
  aclarando que el agente de orientación es de apoyo, no decisor.
- **XLSX**: filas 8-30, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$17.341.281 COP** (`AC1`) = transversales
  (**$4.748.653 COP**) + módulos (**$12.592.628 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/reparto-querellas/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (138 caracteres). Sin logo de cliente.

### Proyecto 12/13 — Archivo Digital de Tránsito (§11.1 + §11.2)

- **Alcance**: 2 módulos (M1 Sistema de Archivo Digital de Tránsito, M2 Módulo de Integración
  para Notificación de Comparendos, combinados), 5 submódulos, 13 funcionalidades (11 bullets
  fuente, 2 divididos: "Digitalización e indexación", "Control de transferencias y
  conservación"). Incluye nota del documento sobre que M2 está sujeto a viabilidad de
  integración con SOS/RUNT.
- **XLSX**: filas 8-27, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$15.206.182 COP** (`AC1`) = transversales
  (**$4.102.396 COP**) + módulos (**$11.103.786 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/archivo-transito/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (137 caracteres). Sin logo de cliente.

### Proyecto 13/13 — Estampillas Digitales (§12.1 + §12.2)

- **Alcance**: 2 módulos (M1 Plataforma de Estampillas Digitales y Pagos Parametrizados, M2
  Generador Masivo de Actos Administrativos, combinados), 6 submódulos, 15 funcionalidades (14
  bullets fuente, 1 dividido: "Registro y trazabilidad"). Nota de contexto técnico incluida.
- **XLSX**: filas 8-30, sin insertar filas. Excepciones `Y122`/`R123` aplicadas. 0 errores
  fuera de `A140:A144`. TOTAL: **$17.233.608 COP** (`AC1`) = transversales
  (**$4.087.201 COP**) + módulos (**$13.146.406 COP**), reconciliado exactamente.
- **Entregables**: `cotizaciones/giron/estampillas/Cotizacion de Alcance.pdf` y
  `Cotizacion.xlsx`. Apertura verificada con Excel real (132 caracteres). Sin logo de cliente.

## Resumen — Portafolio completo Alcaldía Municipal de Girón (13/13)

Los 13 proyectos del portafolio quedaron cotizados, verificados (0 errores fuera de
`A140:A144`, totales reconciliados, apertura confirmada con Excel real) y entregados:

| # | Proyecto | Carpeta | TOTAL (COP) |
|---|----------|---------|-------------|
| 1 | Agentes IA de Correo por Dependencia | `agentes-correo` | $30.846.315 |
| 2 | Gestión Documental Inteligente | `gestion-documental` | $19.320.001 |
| 3 | Observatorio de Salud Pública | `salud-publica` | $14.248.773 |
| 4 | IVC Sanitario | `ivc-sanitario` | $18.749.358 |
| 5 | Auditoría EPS/IPS y Planes de Mejora | `auditoria-eps-ips` | $14.109.200 |
| 6 | Cobro Coactivo y Alertas de Prescripción | `cobro-coactivo` | $21.721.845 |
| 7 | Trámites y Agente de Ordenamiento | `ordenamiento` | $19.992.383 |
| 8 | Gestión de Procesos Disciplinarios | `disciplinarios` | $20.295.200 |
| 9 | Comités, Actas y Compromisos | `comites-actas` | $16.404.950 |
| 10 | Mesa de Víctimas y Pagos | `mesa-victimas` | $13.663.746 |
| 11 | Reparto de Querellas | `reparto-querellas` | $17.341.281 |
| 12 | Archivo Digital de Tránsito | `archivo-transito` | $15.206.182 |
| 13 | Estampillas Digitales | `estampillas` | $17.233.608 |
| | **TOTAL PORTAFOLIO** | | **$239.132.842** |

Todas las carpetas viven bajo `cotizaciones/giron/<slug-proyecto>/` con `Cotizacion.xlsx` y
`Cotizacion de Alcance.pdf`. Pendiente para el usuario: validar días estimados por
especialidad (no vienen de levantamiento con la Alcaldía, sino de criterio de desarrollador
sobre el documento preliminar); decidir si se agrega un logo de la Alcaldía a los PDF.
