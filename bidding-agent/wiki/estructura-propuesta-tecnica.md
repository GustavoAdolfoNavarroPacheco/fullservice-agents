# Estructura de la Propuesta Técnica

Anatomía del entregable principal. **El orden y los títulos se ajustan a lo que
exija el RFP**: si el RFP o las aclaraciones definen una estructura obligatoria de
propuesta, esa manda y esta plantilla se adapta a ella. Si el RFP no la define,
se usa esta.

---

## 0. Portada e identificación

- Logo Campuslands (`Logo Campuslands Horizontal Azul.png` sobre fondo claro).
- Objeto de la licitación, **transcrito literalmente del RFP**.
- Identificador del proceso, entidad solicitante, fecha.
- Datos del proponente (razón social, NIT, representante legal) — de
  `recursos/Brief Fullservice.pdf` o confirmados con el usuario. Si falta,
  `[PENDIENTE: …]`.

## 1. Entendimiento del requerimiento

Demuestra que se leyó todo. Resume, con citas, qué necesita la empresa y por qué:
problema de negocio, situación actual, alcance solicitado y restricciones. **Debe
reflejar las aclaraciones**, no solo el RFP — es la primera señal que el comité ve
de que la propuesta está construida sobre la versión vigente del proceso.

## 2. Solución propuesta — descripción por módulos

El cuerpo de la propuesta. Un bloque por módulo:

```
M1. NOMBRE DEL MÓDULO
    Descripción breve del módulo y del problema que resuelve.
    • Funcionalidad         → detalle técnico → requerimientos que cubre (RF-xx)
    • Funcionalidad         → detalle técnico → requerimientos que cubre
```

- Cada funcionalidad cita **qué requerimientos numerados cubre** (enlaza con la
  matriz de cumplimiento).
- El número de módulos y de funcionalidades por módulo es libre: depende del
  alcance real, no hay un conteo fijo.
- **Todo módulo debe tener horas en la estimación** y toda hora debe pertenecer a
  un módulo (regla de verificación cruzada).

## 3. Arquitectura de la solución

- Diagrama de arquitectura (componentes, capas, flujos de datos).
- Stack tecnológico propuesto, **con justificación documental**: si el RFP exige
  una tecnología, se usa esa y se cita; si deja libertad, se justifica la elección
  contra los requerimientos no funcionales.
- Modelo de datos de alto nivel.
- Integraciones con sistemas existentes (cada una citando su requerimiento).
- Estrategia de despliegue e infraestructura.
- Escalabilidad y rendimiento frente a los volúmenes exigidos (usuarios
  concurrentes, transacciones, almacenamiento).

## 4. Componente de inteligencia artificial (si aplica)

Se incluye **solo si** las consideraciones técnicas concluyeron que el alcance
requiere IA. Describe qué actividades la usan, qué servicios/modelos se proponen,
cómo se integran, y remite al entregable `05 - Analisis IA y Tokens` para el
detalle de consumo y costo. Ver `costeo-ia-tokens.md`.

Si **no** aplica, la propuesta lo dice explícitamente en la sección de
consideraciones técnicas — no se omite el tema en silencio.

## 5. Seguridad y cumplimiento

- Autenticación, autorización y gestión de sesiones.
- Cifrado en tránsito y en reposo.
- Tratamiento de datos personales y residencia de datos (aplicable en Colombia:
  Ley 1581 de 2012 y su régimen de protección de datos, cuando el RFP lo exija).
- Auditoría, trazabilidad y registro de eventos.
- Normas y certificaciones exigidas por el RFP (ej. ISO 27001) y cómo se cumplen
  o se acreditan.
- Respaldo, recuperación y continuidad.

## 6. Metodología de trabajo

- Marco de trabajo (típicamente Scrum con sprints), ceremonias y artefactos.
- Gestión de requerimientos y control de cambios.
- Estrategia de pruebas: unitarias, integración, QA funcional, UAT, pruebas de
  carga si el RFP las exige.
- Gestión de riesgos.
- Comunicación y gobierno del proyecto con la contraparte.

## 7. Cronograma

- Fases e hitos **alineados con los plazos exigidos por el RFP**, citando la
  fuente de cada fecha.
- Duración por fase, coherente con la estimación de horas y con el equipo
  propuesto.
- Entregables por hito.
- Dependencias y responsabilidades de la empresa solicitante (accesos, ambientes,
  disponibilidad de usuarios para UAT, información de negocio).

**Regla:** el cronograma debe caber en el plazo del RFP con las horas de la
estimación y el equipo propuesto. Si no cabe, se reporta al usuario con los
números antes de entregar, no se ajusta la estimación para que cuadre.

## 8. Equipo de trabajo

- Roles y perfiles asignados, con la dedicación de cada uno.
- Correspondencia con las especialidades de la estimación de horas.
- Experiencia acreditable exigida por el RFP y cómo se cumple (solo con datos
  reales del brief o confirmados por el usuario).

## 9. Operación, soporte y garantía

- Modelo de soporte y niveles de servicio (SLA) exigidos.
- Garantía posterior a la entrega.
- Mantenimiento y evolución, si el RFP los incluye en el alcance.
- Transferencia de conocimiento y capacitación.

## 10. Supuestos, exclusiones y dependencias

Sección corta pero indispensable: qué se asumió, qué **no** está incluido en el
alcance ni en el precio, y qué necesita Campuslands de la empresa solicitante para
cumplir el cronograma. Protege ambas partes y evita disputas de alcance
posteriores.

## 11. Anexos

- Matriz de cumplimiento (`01`).
- Estimación de horas (`03`).
- Consideraciones técnicas (`04`).
- Análisis de IA y tokens (`05`), si aplica.
- Cualquier anexo que el RFP exija (hojas de vida, certificaciones, estados
  financieros — provistos por el usuario, nunca fabricados).

---

## Reglas de contenido

- **Contenido 100% verídico**, trazable a los documentos suministrados o al brief
  de la empresa. Cero relleno genérico.
- **Cada módulo y funcionalidad cita los requerimientos que cubre.**
- **Sin promesas no respaldadas** ni métricas inventadas.
- Cualquier dato faltante se marca `[PENDIENTE: <qué falta>]` y se reporta al
  usuario; no se entrega una propuesta con pendientes sin resolver.
