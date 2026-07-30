# Consideraciones Técnicas — Checklist

Checklist que se recorre **completo** en toda licitación para producir el
entregable `04 - Consideraciones Tecnicas.md`. El objetivo es que no quede ningún
elemento técnico necesario sin contemplar — y sin costear.

**Cómo se usa:** cada ítem se marca como **Aplica** (con su cita de origen y su
implicación técnica y de esfuerzo), **No aplica** (con la razón), o **Por confirmar
con el usuario**. Un ítem "Aplica" sin horas asignadas en la estimación es una
omisión que la verificación cruzada debe detectar.

---

## 1. Arquitectura y plataforma

- [ ] Tipo de solución: web, móvil, escritorio, API, híbrida.
- [ ] Stack tecnológico: ¿lo impone el RFP o hay libertad de elección?
- [ ] Arquitectura: monolito, microservicios, serverless.
- [ ] Multi-tenant vs. instancia dedicada.
- [ ] Requisitos de navegadores y dispositivos soportados.
- [ ] Compatibilidad con sistemas o versiones legadas exigidas.

## 2. Infraestructura y despliegue

- [ ] ¿Nube, on-premise o híbrido? ¿Lo define el RFP?
- [ ] Proveedor de nube exigido o preferido.
- [ ] **Residencia de datos**: ¿el RFP exige que los datos permanezcan en el país?
- [ ] Ambientes requeridos: desarrollo, pruebas, staging, producción.
- [ ] CI/CD y automatización de despliegues.
- [ ] Dimensionamiento según los volúmenes exigidos.
- [ ] **Quién paga la infraestructura**: ¿va en el precio de la propuesta o la
      provee la empresa solicitante? Determinante para el costeo.

## 3. Capacidad, rendimiento y escalabilidad

- [ ] Usuarios totales y usuarios concurrentes exigidos.
- [ ] Volumen de transacciones y de datos.
- [ ] Tiempos de respuesta exigidos (SLA técnicos).
- [ ] Disponibilidad exigida (ej. 99.5%, 99.9%) y su implicación en arquitectura.
- [ ] Crecimiento proyectado y estrategia de escalamiento.
- [ ] Pruebas de carga exigidas.

## 4. Integraciones

- [ ] Inventario de sistemas con los que hay que integrarse.
- [ ] Protocolos y formatos (REST, SOAP, archivos planos, colas, webhooks).
- [ ] ¿Existe documentación de las APIs de terceros? ¿Ambiente de pruebas?
- [ ] Integraciones con pasarelas de pago, facturación electrónica, entidades
      gubernamentales.
- [ ] Autenticación federada / SSO exigido (SAML, OAuth, LDAP, directorio activo).
- [ ] **Riesgo de dependencia**: integraciones que dependen de terceros fuera del
      control de Campuslands, y su tratamiento en supuestos y cronograma.

## 5. Datos y migración

- [ ] ¿Hay migración de datos desde sistemas existentes?
- [ ] Volumen, calidad y formato de los datos de origen.
- [ ] Estrategia de migración, validación y reversión.
- [ ] Modelo de datos y motor de base de datos exigido.
- [ ] Retención, archivado y depuración de datos.
- [ ] Reportería, BI y analítica exigidas.

## 6. Seguridad y cumplimiento

- [ ] Autenticación, autorización y roles.
- [ ] Cifrado en tránsito y en reposo.
- [ ] **Protección de datos personales** (en Colombia: Ley 1581 de 2012 y su
      régimen), cuando el RFP lo exija.
- [ ] Normas y certificaciones exigidas (ISO 27001, PCI-DSS, otras).
- [ ] Auditoría, trazabilidad y no repudio.
- [ ] Pruebas de seguridad / pentesting exigidos.
- [ ] Respaldo, recuperación y plan de continuidad (RPO/RTO).
- [ ] Gestión de secretos y credenciales.

## 7. Inteligencia artificial — decisión obligatoria

- [ ] **¿El alcance requiere servicios de IA?** Conclusión explícita, sí o no, con
      justificación documental. Ver la tabla de señales en `costeo-ia-tokens.md`.
- [ ] Si **sí**: qué actividades la requieren, qué modelos/servicios se proponen y
      por qué, y remisión al entregable `05` para tokens y costo.
- [ ] Si **sí**: ¿el RFP impone proveedor, modelo o restricción de residencia para
      la IA? ¿Exige modelo local u on-premise?
- [ ] Si **sí**: tratamiento de datos enviados al modelo, retención del proveedor y
      compatibilidad con las exigencias de privacidad del RFP.
- [ ] Si **sí**: mecanismos de control de calidad del componente de IA
      (evaluación, monitoreo, escalamiento a humano, manejo de alucinaciones).
- [ ] Si **no**: se deja constancia escrita de la conclusión y de su razón. **"No
      se mencionó" no es una conclusión.**

## 8. Experiencia de usuario y accesibilidad

- [ ] Requisitos de diseño y de identidad visual de la empresa solicitante.
- [ ] Accesibilidad exigida (WCAG u otro estándar).
- [ ] Multi-idioma.
- [ ] Diseño responsive y soporte móvil.
- [ ] ¿Se exigen prototipos o aprobación de diseño como hito?

## 9. Calidad y pruebas

- [ ] Estrategia y niveles de prueba exigidos.
- [ ] Cobertura de pruebas exigida.
- [ ] UAT: quién lo ejecuta, cuánto dura, qué se necesita de la contraparte.
- [ ] Criterios de aceptación de los entregables.
- [ ] Herramientas de calidad exigidas.

## 10. Operación, soporte y garantía

- [ ] SLA de soporte exigido (horarios, tiempos de respuesta, niveles).
- [ ] Mesa de ayuda: ¿está en el alcance? ¿Con qué capacidad?
- [ ] Período de garantía posterior a la entrega.
- [ ] Mantenimiento correctivo y evolutivo incluido.
- [ ] **Meses de operación incluidos en el alcance** — dato crítico para costear
      infraestructura, licencias y consumo de IA recurrente.
- [ ] Monitoreo y observabilidad.

## 11. Entregables documentales y transferencia

- [ ] Documentación técnica exigida (arquitectura, APIs, base de datos).
- [ ] Manuales de usuario y de administración.
- [ ] Capacitación: audiencias, número de sesiones, modalidad.
- [ ] Transferencia de conocimiento y entrega de código fuente.
- [ ] Propiedad intelectual del desarrollo.

## 12. Licenciamiento y terceros

- [ ] Licencias de software de terceros necesarias y quién las paga.
- [ ] Compatibilidad de licencias open source con las exigencias del RFP.
- [ ] Servicios de terceros con costo recurrente (APIs, mensajería, IA, mapas,
      firma electrónica).
- [ ] Restricciones del RFP sobre subcontratación.

## 13. Gestión del proyecto

- [ ] Metodología exigida o propuesta.
- [ ] Estructura de gobierno y comités.
- [ ] Reportería de avance exigida.
- [ ] Control de cambios de alcance.
- [ ] Interlocutores y dedicación requerida de la empresa solicitante.

## 14. Restricciones de plazo

- [ ] Fecha de inicio y plazo total exigidos.
- [ ] Hitos intermedios con entregables y su relación con los pagos.
- [ ] Penalidades por incumplimiento y su implicación en el riesgo.
- [ ] Dependencias del cronograma que están fuera del control de Campuslands.
- [ ] **Factibilidad del plazo** frente a la estimación de horas (ver
      `estimacion-horas.md` §5). Si no es factible, se reporta al usuario con los
      números.

## 15. Riesgos técnicos

- [ ] Riesgos identificados, con probabilidad, impacto y mitigación.
- [ ] Supuestos que, si fallan, cambian el alcance o el precio.
- [ ] Contingencia técnica y de esfuerzo, explícita y justificada.

---

## Cierre del entregable

El documento `04` cierra con:

1. **Conclusión sobre IA** — afirmación explícita, sí o no, con justificación.
2. **Elementos técnicos que impactan el precio** y no son desarrollo de
   funcionalidades: infraestructura, licencias, servicios recurrentes, migración,
   certificaciones, capacitación, operación.
3. **Supuestos y exclusiones técnicas** que deben aparecer también en la propuesta
   técnica.
4. **Riesgos técnicos** con su tratamiento.
5. **Lista de ítems "Por confirmar con el usuario"** que quedan pendientes, si
   alguno sigue abierto.
