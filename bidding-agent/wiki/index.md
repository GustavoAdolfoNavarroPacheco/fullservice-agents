# Catálogo de la Wiki (Agente Licitatorio)

Índice de la documentación que mantengo para analizar procesos licitatorios y
construir propuestas técnicas, estimaciones y costeos para Campuslands Full
Service. **Se lee primero, antes de entrar a cualquier página de detalle.**

## Archivos principales

* [Perfil del Agente](perfil-usuario.md) — Rol, reglas fundacionales y expectativas del agente.
* [Flujo de Trabajo](flujo-trabajo.md) — Paso a paso del proceso: ingesta de los 4 documentos, análisis, entregables, verificación.
* [Estructura de la Propuesta Técnica](estructura-propuesta-tecnica.md) — Anatomía de secciones del entregable principal.
* [Estimación de Horas](estimacion-horas.md) — Método de estimación, especialidades, conversión horas↔días y validación contra el plazo del RFP.
* [Consideraciones Técnicas](consideraciones-tecnicas.md) — Checklist de elementos técnicos a evaluar en toda licitación, incluida la decisión sobre IA.
* [Costeo de IA y Tokens](costeo-ia-tokens.md) — Precios vigentes por modelo, método de estimación de tokens y cálculo de costo.
* [Marca Campuslands](marca-campuslands.md) — Identidad visual y tono editorial de los entregables.
* [Bitácora (Log)](log.md) — Registro cronológico de ingestas, propuestas y mantenimiento.

*(Nota: la jerarquía documental, las reglas duras y el flujo completo están
definidos en `CLAUDE.md` en la raíz del proyecto. Esta wiki desarrolla el detalle
de cada pieza.)*

## Habilidades (procedimientos reutilizables)

* `habilidades/ingesta-documentos-licitacion/` — Verificar y leer los 4 documentos oficiales, extraer y numerar requerimientos.
* `habilidades/matriz-cumplimiento/` — Construir la matriz requerimiento × respuesta × origen (gate de cero omisiones).
* `habilidades/estimacion-horas/` — Estimar horas por módulo y especialidad, y validar contra el plazo.
* `habilidades/modelos-costos/` — Llenar y conciliar el modelo oficial de la empresa y el modelo de cotización interno.
* `habilidades/analisis-ia-tokens/` — Determinar si se requiere IA, estimar tokens y costear.

## Fichas por licitación

Cada licitación procesada tiene su ficha en `wiki/licitaciones/<slug>.md` con
datos del proceso, decisiones tomadas, ambigüedades resueltas y estado.

* [IPA PR10598](licitaciones/ipa-pr10598.md) — Agente de IA por WhatsApp para IPA Colombia ("Una Visa por un Sueño"). Estado: Verificación (pendiente de insumos de empresa del usuario).

### Leyenda de estados

| Estado | Significado |
|---|---|
| `Ingesta` | Documentos recibidos, análisis documental en curso. |
| `En consulta` | Bloqueado esperando respuestas del usuario a ambigüedades. |
| `En construcción` | Entregables en elaboración. |
| `Verificación` | Entregables completos, verificación cruzada en curso. |
| `Entregada` | Propuesta entregada al usuario / radicada. |
| `Adjudicada` / `No adjudicada` | Resultado del proceso, cuando se conoce. |
