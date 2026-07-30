# Bitácora (Log) del Agente Licitatorio

Registro cronológico de ingestas de documentación, propuestas construidas,
ajustes y mantenimiento de la wiki. Cada entrada debe empezar con un prefijo
consistente para que sea parseable.

Prefijo: `## [YYYY-MM-DD] <tipo> | <descripción>` donde tipo ∈ {setup, ingesta,
build, ajuste, verificacion, lint}.

---

## [2026-07-29] setup | Inicialización del Agente Licitatorio (BiddingAgent).

Creación del agente especialista en licitaciones, preventa técnica, arquitectura de
soluciones y estimación de proyectos de software, siguiendo la estructura de
información de los agentes existentes del monorepo (`CLAUDE.md` como esquema,
`wiki/` con `index.md` + `log.md`, `habilidades/` con SKILLs, `recursos/` de solo
lectura, y carpeta de salidas autocontenida por caso).

**Definido en esta sesión:**

- **Cuatro insumos obligatorios** por licitación: RFP, documento de aclaraciones /
  preguntas y respuestas, modelo de costos oficial de la empresa, y segundo modelo
  de costos (el de cotización). Si falta alguno, el agente pregunta antes de
  construir.
- **Cuatro entregables**: propuesta técnica, estimación de horas de desarrollo,
  consideraciones técnicas (con conclusión explícita sobre IA), y análisis de IA con
  estimación de tokens y costo (solo si se concluye que se requiere IA).
- **Jerarquía documental** ante contradicciones: aclaraciones → adendas → RFP →
  modelo de costos oficial → anexos. Las aclaraciones prevalecen sobre el RFP.
- **Gates de calidad**: matriz de cumplimiento como control de cero requerimientos
  omitidos (se llena antes de la propuesta técnica), validación de factibilidad de
  la estimación contra el plazo exigido, conciliación de los dos modelos de costos,
  y verificación cruzada con rastro auditable antes de entregar.
- **Especialidades de estimación** alineadas con el modelo de costeo interno de
  FullService (DB, UX, FM, BS, BM, QA, IM, MS, MM, IA), con piso mínimo equivalente
  a 0.5 días por ítem y factor de conversión horas↔días declarado explícitamente en
  cada archivo (pendiente de confirmar con el usuario en la primera licitación).
- **Costeo de IA** documentado en `wiki/costeo-ia-tokens.md` con los precios
  vigentes de Claude a esta fecha (Opus 5 $5/$25 por MTok; Sonnet 5 $3/$15, con
  precio promocional $2/$10 hasta 2026-08-31; Haiku 4.5 $1/$5), más los
  multiplicadores que cambian el costo real: lectura de caché ~0.1×, escritura de
  caché 1.25× (TTL 5 min) / 2× (TTL 1 h), y Batch API con 50% de descuento. Regla
  establecida: verificar la vigencia de los precios antes de cada costeo nuevo y
  usar el endpoint oficial de conteo de tokens (nunca `tiktoken`, que subcuenta los
  tokens de Claude).
- **Recursos de marca** copiados desde `QuoteDeveloper/recursos/` (logos
  Campuslands, isotipo, favicon, `Brief Fullservice.pdf`, brandbook) para que el
  agente sea autocontenido.
- **Confidencialidad**: `recursos/licitaciones/` y `licitaciones/` contienen
  información sensible de procesos en curso (precios, estrategia, datos de la
  entidad solicitante). Regla: no mezclar información entre licitaciones y
  confirmar con el usuario antes de subir esas carpetas a un remoto.

Sin licitaciones procesadas todavía.

## [2026-07-29] ingesta | RFP No. PR10598 (IPA Colombia) — análisis documental y bloqueantes.

Recibidos RFP (21-jul-2026), aclaraciones/Q&A (27-jul-2026, 66 preguntas), y dos
documentos adicionales que no corresponden a los roles esperados: un borrador de
alcance previo y superado (23-jun-2026, cifras de 1.000 usuarios ya obsoletas) y
un modelo de costeo/TCO detallado marcado como borrador interno no aprobado de una
firma identificada como "Aurena AI" en colaboración con "Campus Lands". No llegó
un modelo de costos oficial aparte (está embebido en el Anexo 11.3 del RFP) ni el
segundo modelo de costos (cotización interna de FullService).

Construido `licitaciones/ipa-pr10598/00 - Analisis Documental.md` con inventario
de ~60 requerimientos (RF/RNF/TEC/PLZ/ADM/ENT/OPS), plazos, criterios de
evaluación, estructura del formulario de costos, y dos contradicciones resueltas
por jerarquía documental (volumen de usuarios 800 vs. 1.000 obsoleto; estructura
del componente 2 de costos corregida por la Aclaración P15).

**Plazo de radicación: 30-jul-2026, 2:00 pm — menos de 24 horas al momento de esta
ingesta.**

Quedan bloqueantes sin resolver antes de construir los cuatro entregables:
estructura societaria del oferente (el RFP prohíbe consorcios/UT), qué usar como
segundo modelo de costos, y parámetros de negocio del costeo (tasa de derivación,
margen, anticipo). Preguntados al usuario el mismo día.

## [2026-07-29] build | RFP No. PR10598 — construcción completa de los 4 entregables y soporte.

Decisiones del usuario: Campuslands Full Service como único oferente (Aurena AI,
si participa, como subcontratista no visible); segundo modelo de costos
construido desde cero; tasa de derivación al canal humano 15%; margen comercial
22%.

Construidos: `01 - Matriz de Cumplimiento.xlsx` (70 requerimientos, 0 en "No
cumple"), `02 - Propuesta Tecnica.pdf` (16 páginas, 14 módulos M1-M14, arquitectura
con diagrama, KB completa en contexto sin RAG, sin razonamiento extendido),
`03 - Estimacion de Horas.xlsx` (1.093 horas, factible en el plazo de 4 meses),
`04 - Consideraciones Tecnicas.md` (conclusión: SÍ requiere IA), `05 - Analisis IA
y Tokens.xlsx` (USD 534,67 escenario esperado + contingencia, precios Anthropic
verificados 2026-07-29), `06 - Modelo de Costos Oficial.xlsx` (formato exacto del
Anexo 11.3 del RFP, corregido por Aclaración P15/P16) y `07 - Modelo de Costos
Cotizacion.xlsx` (motor interno, conciliado contra 06 sin diferencia), y
`verificacion-cruzada.md`.

**Precio total propuesto: COP 177.384.670 (≈ USD 52.951), con margen 22% e IVA
19% incluidos.**

Pendientes que solo el usuario puede resolver antes de radicar (ver
verificacion-cruzada.md §8): documentación legal y financiera de Campuslands,
3 certificaciones de contratos similares a nombre de Campuslands, hojas de vida
del equipo, y validación de las tarifas supuestas (personal, WhatsApp, pólizas,
retenciones). El Brief de FullService disponible en `recursos/` es un documento
de marketing sin estos datos — no alcanza como fuente para esta sección.

## [2026-07-29] ajuste | Corrección tributaria en 06/07 — el servicio no causa IVA.

El usuario indicó que el software en la nube no causa IVA y que en su lugar hay
que calcular retenciones. Se retiró el IVA del `06 - Modelo de Costos
Oficial.xlsx` (antes 19% sobre el subtotal) y se agregó una hoja "Retenciones"
informativa con ReteFuente (4%, SUPUESTO — tarifa general de servicios para
declarantes de renta, [PENDIENTE: confirmar con contador]) y ReteICA (9,66‰,
SUPUESTO — tarifa general Bogotá, [PENDIENTE: confirmar municipio/tarifa]).
Estas retenciones no se suman al precio: se muestran como deducción sobre el
pago que recibe Campuslands, no como mayor valor que paga IPA. Se recalculó `07`
para mantener la conciliación (diferencia COP 0) y se actualizaron las cifras en
`verificacion-cruzada.md` y en la ficha de la licitación.

**Nuevo precio total: COP 149.062.748 (≈ USD 44.496)**, antes COP 177.384.670
con el IVA que ya no aplica.
