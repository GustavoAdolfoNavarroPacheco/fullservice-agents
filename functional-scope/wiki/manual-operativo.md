# Manual operativo — resumen de consulta rápida

Fuente: `recursos/Manual_Agente_Alcances_Funcionales_Campuslands.docx` (v1.0, octubre 2026). Este resumen no lo sustituye; ante duda, manda el manual.

## 1. Bloques de la entrevista y qué debe resolver cada uno (manual §3)

| Bloque | Preguntas que debe resolver |
|---|---|
| Identificación | ¿Cliente, proyecto, patrocinador, responsables, fecha, versión, propósito y audiencia? |
| Problema y valor | ¿Qué problema se resuelve, cuál es la situación actual y qué resultados o KPI se esperan? |
| Usuarios | ¿Qué perfiles usarán el sistema y qué datos/acciones puede realizar cada uno? |
| Alcance | ¿Qué módulos y funcionalidades están incluidos, excluidos o sujetos a otra fase? ¿Qué prioridad tienen? |
| Reglas de negocio | ¿Qué cálculos, umbrales, validaciones, excepciones y aprobaciones se aplican? |
| Datos e integraciones | ¿Qué sistemas, APIs, archivos, campos, volumen, históricos, frecuencia y responsables existen? |
| IA y automatización | ¿Qué tareas realiza la IA, con qué fuentes, qué supervisión humana, límites y trazabilidad? |
| No funcionales | ¿Qué disponibilidad, seguridad, privacidad, rendimiento, respaldo y accesibilidad se requieren? |
| Entregables y pruebas | ¿Qué se entregará por fase y cómo se comprobará su aceptación? |
| Proyecto y operación | ¿Qué cronograma, dependencias, ambientes, despliegue, capacitación, garantía y soporte se acordaron? |
| Comercial y legal | ¿Qué precio, impuestos, hitos de pago, costos recurrentes, licencias, titularidad y exclusiones están confirmados? |

## 2. Contenido esperado de cada sección del documento al cliente (manual §4)

| Sección | Contenido |
|---|---|
| Portada y control documental | Proyecto, cliente, proveedor, versión, fecha, clasificación, responsables; historial de cambios |
| 1. Resumen ejecutivo | Problema, solución, beneficios esperados y alcance en lenguaje de negocio; **sin garantías de resultados no aprobadas** |
| 2. Contexto y objetivos | Situación actual, objetivos específicos, indicadores de éxito, restricciones y dependencias |
| 3. Alcance y límites | Módulos incluidos, fuera de alcance, fases futuras y mapa general de procesos |
| 4. Usuarios y permisos | Actores, perfiles, permisos y niveles de visibilidad; pendientes de validación |
| 5. Requerimientos funcionales | Ficha uniforme por módulo y funcionalidad: id, objetivo, actor, disparador, entradas, flujo, reglas, excepciones, salidas, dependencias y aceptación |
| 6. Fuentes de datos e integraciones | Matriz por sistema: propietario, acceso, interfaz, datos, volumen, frecuencia, autenticación, errores y prerrequisitos |
| 7. IA y automatización | Casos de uso, modelos/servicios confirmados, fuentes autorizadas, validación, explicabilidad, permisos y límites |
| 8. No funcionales | Seguridad, privacidad, auditoría, rendimiento, escalabilidad, respaldo, disponibilidad y ambientes; **sin cifras no acordadas** |
| 9. Arquitectura de alto nivel | Componentes, flujo de información, servicios externos y responsabilidades, con diagrama comprensible |
| 10. Entregables y aceptación | Matriz por fase: entregable, evidencia, responsable de validación, criterios objetivos y procedimiento de observaciones |
| 11. Metodología y cronograma | Fases, hitos, supuestos, dependencias, roles de ambas partes y proceso de cambios |
| 12. Capacitación y transferencia | Sesiones, destinatarios, material, documentación, accesos y entregas de código cuando corresponda |
| 13. Garantía, soporte y operación | Cobertura, exclusiones, inicio, duración, canales, severidades y SLA **únicamente si están acordados** |
| 14. Condiciones comerciales | Precio, impuestos, hitos, costos de terceros, infraestructura, licencias y condiciones de pago **confirmadas** |
| 15. Supuestos, exclusiones y riesgos | Responsabilidades del cliente, límites, dependencias externas y consecuencias de cambios |
| 16. Aprobación y anexos | Firmas o validaciones, glosario, matriz de requisitos, integraciones, pruebas y registro de decisiones |

## 3. Decisiones de interpretación del agente (no vienen literales del manual)

Estas son mis decisiones operativas para aplicar el manual; si el usuario las corrige, se actualizan aquí y en `CLAUDE.md`.

| Tema | Decisión | Por qué |
|---|---|---|
| Formato de entrega | `.docx` editable + Markdown de trabajo | El manual pide «documento editable»; no fija formato |
| Identificadores | RF / MOD / INT / DEC / PEN / CON, estables | El manual exige ID en fichas y matrices, sin esquema |
| Columna «Criticidad» en la matriz de pendientes | Añadida a las 5 columnas del manual | Ordenar las preguntas por BLOQUEANTE/IMPORTANTE/EDITORIAL (§7) |
| Estados del documento | Borrador · Apto para revisión final · Aprobado por cliente | El manual habla de «borrador», «apta para revisión final» y «lista para firma» |
