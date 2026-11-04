# Manual operativo — resumen de consulta rápida

Fuente: `recursos/Manual_Agente_Alcances_Funcionales_Campuslands.docx` (v1.0, octubre 2026). Este resumen no lo sustituye; ante duda, manda el manual.

## 1. Bloques de revisión y qué debe cubrir cada uno (manual §3)

> Ajuste del usuario (2026-10-29): estos bloques **ya no se usan como entrevista**. Son una lista de revisión del documento: cada bloque se llena con lo que diga la fuente o se marca `[PENDIENTE DE VALIDACIÓN]`; no se le preguntan al usuario.

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
| Portada · Carta de presentación · Tabla de contenido | Una hoja cada una. Portada: título, cliente, y solo las tarjetas «Preparado por» y «Fecha» (**sin Preparado para, estado, versión ni clasificación**); la tabla de contenido va ya generada. Ya no hay página de control documental (ajuste del usuario, 2026-10-29) |
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
| 16. Anexos (y, al final, apartado de firma) | Glosario, matriz de requisitos, integraciones, pruebas y registro de decisiones; la hoja «Aprobación y firmas» cierra el documento |

## 3. Decisiones de interpretación del agente (no vienen literales del manual)

Estas son mis decisiones operativas para aplicar el manual; si el usuario las corrige, se actualizan aquí y en `CLAUDE.md`.

| Tema | Decisión | Por qué |
|---|---|---|
| Formato de entrega | `.docx` editable + Markdown de trabajo | El manual pide «documento editable»; no fija formato |
| Identificadores | RF / MOD / INT / DEC / PEN / CON, estables | El manual exige ID en fichas y matrices, sin esquema |
| Columna «Criticidad» en la matriz de pendientes | Añadida a las 5 columnas del manual | Ordenar las preguntas por BLOQUEANTE/IMPORTANTE/EDITORIAL (§7) |
| Estados del documento | Borrador · Apto para revisión final · Aprobado por cliente | El manual habla de «borrador», «apta para revisión final» y «lista para firma» |
| Preguntas al usuario | **Ninguna por defecto**; si hay archivo, se redacta el borrador en el mismo turno y los vacíos se marcan pendientes | Instrucción del usuario, 2026-10-29: «si se te compartió un archivo, lo más seguro es que no haya más». Sustituye al manual §2 etapa 4 y §10 |
| Estructura del documento | Portada · Carta de presentación · Tabla de contenido · Contenido · Apartado de firma | Instrucción del usuario, 2026-10-29 |
| Versión y clasificación | No aparecen dentro del documento (ni en la portada); la versión vive en el nombre del archivo y la wiki | Instrucción del usuario, 2026-10-29 |
| Firma | Columna izquierda fija (Campuslands); derecha por proyecto; firma escaneada solo en documentos listos para firma | Instrucción del usuario, 2026-10-29 |
| Palabra «borrador» | No aparece dentro del documento; el estado vive en el chat, la wiki y el control de calidad | Instrucción del usuario, 2026-10-29 (segunda ronda) |
| Espacios vacíos | Sin saltos de página forzados entre secciones; fichas que fluyen; se revisa la ocupación de cada página | Instrucción del usuario, 2026-10-29 (segunda ronda) |
