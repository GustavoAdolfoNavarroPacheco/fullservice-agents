# 04 — Consideraciones Técnicas · RFP No. PR10598 (IPA Colombia)

Recorrido completo del checklist de `wiki/consideraciones-tecnicas.md`. Cada ítem
se marca **Aplica** (con cita e implicación), **No aplica** (con razón), o **Por
confirmar con el usuario**.

---

## 1. Arquitectura y plataforma

- **Tipo de solución:** híbrida — servicio backend + integración con plataforma de
  mensajería (WhatsApp Business). **Aplica.** RFP §11.1.4-I.
- **Stack tecnológico:** el RFP no impone stack de desarrollo; sí impone el canal
  (WhatsApp Business API oficial o BSP autorizado) y deja abierta la arquitectura
  de recuperación (RAG vs. contexto completo). **Aplica**, libertad de elección
  documentada en 02 §3.
- **Arquitectura:** servicio en contenedores, no serverless ni monolito clásico —
  justificado en 02 §3 por la necesidad de control total del ciclo de vida del
  agente (trazabilidad del ECA). **Aplica.**
- **Multi-tenant vs. instancia dedicada:** instancia dedicada para este proyecto
  (un solo cliente, IPA, con datos de investigación sensibles). **Aplica.**
- **Navegadores/dispositivos:** no aplica directamente — la interfaz de usuario es
  WhatsApp, no un navegador propio. **No aplica.**
- **Compatibilidad con sistemas legados:** no exigida por el RFP. **No aplica.**

## 2. Infraestructura y despliegue

- **Nube / on-premise:** el RFP no impone proveedor; se propone nube pública.
  **Aplica**, libertad de elección — proveedor específico **[Por confirmar con el
  usuario: preferencia de Campuslands, si existe]**.
- **Residencia de datos:** el RFP no prohíbe transferencia internacional, pero
  exige declararla explícitamente (Aclaración P21, RNF-08). **Aplica.**
- **Ambientes:** desarrollo, preproducción y producción — 3 ambientes (M1, M11).
  **Aplica.**
- **CI/CD:** necesario para el control de versiones exigido por el RFP (RF-04,
  RNF-05). **Aplica.**
- **Dimensionamiento:** validado contra ~12.800 mensajes salientes y ~11.200
  consultas entrantes con altas escalonadas en 8 semanas (RNF-02). **Aplica.**
- **Quién paga la infraestructura:** el proveedor, incluida en el precio
  (Componente 2 del formulario económico, RFP Anexo 11.3). **Aplica.**

## 3. Capacidad, rendimiento y escalabilidad

- **Usuarios totales/concurrentes:** 800 usuarios (grupo de tratamiento 4), piloto
  ~10 (RF-16, RF-17). **Aplica.**
- **Volumen de transacciones:** ~12.800 mensajes salientes programados + ~11.200
  consultas entrantes (valor de planeación 14/usuario) en 8 semanas (RNF-02).
  **Aplica.**
- **Tiempos de respuesta:** no se fija un SLA técnico numérico en el RFP para
  latencia del agente; se declara como buena práctica de diseño (sin razonamiento
  extendido, para mantener latencia baja — ver 02 §3). **Aplica** parcialmente;
  umbral exacto no exigido.
- **Disponibilidad:** 24/7 exigida explícitamente (RNF-01). **Aplica.**
- **Crecimiento proyectado:** la base de 800 usuarios es fija durante todo el
  estudio, sin crecimiento posterior dentro del contrato (Aclaración P59).
  **Aplica** (sin escalamiento adicional a diseñar).
- **Pruebas de carga:** no exigidas explícitamente por el RFP; se recomienda una
  prueba ligera de carga previa al despliegue de los 800 usuarios dado el riesgo
  de límite de mensajería de WhatsApp (RNF-10). **Aplica** (buena práctica, no
  obligación contractual — no genera horas adicionales significativas).

## 4. Integraciones

- **Sistemas con los que integrar:** WhatsApp Business Platform (Cloud API/BSP) y
  el proveedor del modelo de lenguaje (Anthropic API). **Aplica** — RF-02, TEC-01.
- **Protocolos/formatos:** REST/webhooks para WhatsApp; API REST para el modelo de
  lenguaje. **Aplica.**
- **Documentación y ambiente de pruebas de terceros:** WhatsApp Cloud API y
  Anthropic API tienen documentación oficial y sandbox/entornos de prueba
  públicos. **Aplica.**
- **Pasarelas de pago / facturación electrónica / entidades gubernamentales:** no
  requeridas por el alcance. **No aplica.**
- **SSO/autenticación federada:** no exigida — el único usuario del panel
  administrativo es el equipo de Campuslands/IPA, sin integración con directorio
  corporativo de IPA. **No aplica**, salvo que IPA lo requiera para su propio
  acceso al panel — **[Por confirmar con el usuario / con IPA en la fase de
  levantamiento]**.
- **Riesgo de dependencia de terceros:** riesgo identificado y documentado en §15
  — límite de mensajería de WhatsApp Business (250 destinatarios/24h en
  portafolio nuevo) y cambio de tarifas de Meta a partir de octubre de 2026.

## 5. Datos y migración

- **Migración de datos desde sistemas existentes:** no aplica — la base de
  conocimiento es nueva, entregada por IPA en documentos guía, no migrada desde
  un sistema en producción (Aclaración P24). **No aplica.**
- **Modelo de datos:** base relacional para conversaciones, versiones de KB y
  metadatos; almacenamiento de objetos para multimedia. **Aplica.**
- **Retención/depuración de datos:** políticas de retención alineadas al periodo
  del estudio y a las instrucciones de IPA (RNF-07). **Aplica** — política exacta
  se define con IPA en el DPA.
- **Reportería/BI:** los informes de precisión, piloto y despliegue exigidos por
  el RFP (§6) se generan desde el panel de observabilidad (M9). **Aplica.**

## 6. Seguridad y cumplimiento

Ver 02 §5 (Seguridad y cumplimiento) para el detalle completo frente a los
subcriterios D1-D4 del RFP. **Aplica** en su totalidad — es uno de los 6 criterios
de evaluación (15 puntos).
- **Certificaciones (ISO 27001, etc.):** el RFP no exige una certificación
  específica de seguridad. **No aplica** como requisito habilitante.
- **Pentesting:** no exigido explícitamente. **No aplica** como obligación
  contractual (buena práctica recomendable antes del despliegue a 800 usuarios).

## 7. Inteligencia artificial — decisión obligatoria

### ✅ El alcance SÍ requiere servicios de IA.

**Justificación documental:** el objeto mismo del RFP es "diseño, desarrollo e
implementación de un agente de **inteligencia artificial (IA)**" (RFP p.1, título).
El Anexo 11.1 exige explícitamente una "arquitectura basada en un modelo de
lenguaje con recuperación sobre la base de conocimiento" (§11.1.4-I), con
"descripción y justificación del modelo de lenguaje seleccionado" como
subcriterio de evaluación A5 (1,5 puntos), y el propio Anexo 11.3 (Propuesta
económica) define un escenario común de tokens de entrada/salida obligatorio para
costear el consumo del modelo (p.30-31). No es un caso ambiguo: coincide con la
señal más directa de la tabla de `wiki/costeo-ia-tokens.md` ("Chatbot, asistente
virtual, agente conversacional, atención por WhatsApp" + "Búsqueda semántica /
RAG / base de conocimiento").

- **Actividades que requieren IA:** generación conversacional grounded sobre la
  base de conocimiento (M3, M4); clasificación de casos sensibles (M5);
  evaluación de precisión con clave de respuestas (M7).
- **Modelo/servicio propuesto:** Claude Sonnet 5 (Anthropic), justificado en 02
  §3-4. Detalle de tokens y costo en **05 - Analisis IA y Tokens.xlsx**.
- **¿El RFP impone proveedor o restricción de residencia para la IA?** No impone
  proveedor. Sí exige declarar dónde se procesan los datos y garantizar que el
  proveedor del modelo no entrena con datos de conversación (RNF-08, RNF-09).
- **Tratamiento de datos enviados al modelo:** se acreditan los términos
  comerciales vigentes de Anthropic (API comercial, no usa datos de clientes para
  entrenar por defecto). Compatible con las exigencias de privacidad del RFP.
- **Mecanismos de control de calidad del componente de IA:** arnés de evaluación
  de precisión (M7), guardrails de rechazo (M3), clasificador de casos sensibles
  con escalamiento a IPA (M5), monitoreo continuo de métricas (M9).

## 8. Experiencia de usuario y accesibilidad

- **Identidad visual de IPA:** no aplica al agente conversacional (no hay interfaz
  gráfica propia más allá de WhatsApp); si el RFP exige uso de marca IPA en
  contenido, se aplicará según lo que confirme IPA en la fase de levantamiento.
  **Por confirmar.**
- **Accesibilidad (WCAG):** no aplica en sentido estricto de interfaz web; el
  requisito equivalente es el diseño para baja alfabetización (M8), explícitamente
  exigido (RF-15). **Aplica** vía M8.
- **Multi-idioma:** no exigido — el alcance es en español (variantes LatAm y
  venezolana). **No aplica** (un solo idioma, con variantes dialectales).
- **Diseño responsive/móvil:** no aplica — canal es WhatsApp. **No aplica.**
- **Prototipos o aprobación de diseño como hito:** el acta de línea base
  funcional (M1) cumple ese rol para los flujos conversacionales. **Aplica.**

## 9. Calidad y pruebas

- **Estrategia y niveles de prueba:** unitarias e integración del orquestador
  (M3), arnés de evaluación de precisión (M7), UAT conjunta con IPA antes de cada
  hito (02 §6). **Aplica.**
- **Cobertura de pruebas exigida:** no se fija un porcentaje numérico en el RFP.
  **No aplica** como obligación cuantitativa.
- **UAT:** IPA participa validando la clave de respuestas y el umbral de
  precisión antes del piloto (Aclaración P43-48). **Aplica.**
- **Criterios de aceptación de entregables:** IPA revisa y acepta cada entregable
  en 10 días hábiles (Aclaración P62). **Aplica.**
- **Herramientas de calidad exigidas:** ninguna específica. **No aplica.**

## 10. Operación, soporte y garantía

- **SLA de soporte:** canal humano 4 horas hábiles (L-V 8:00-17:00 Colombia,
  Aclaración P6) + guardia 24/7 para casos sensibles (Aclaración P7). **Aplica.**
- **Mesa de ayuda:** sí, en el alcance — el canal humano de derivación (M5).
  **Aplica.**
- **Garantía posterior a la entrega:** soporte de estabilización de 30 días
  posteriores al traspaso (RFP §6, entregable 6). **Aplica.**
- **Mantenimiento correctivo/evolutivo:** durante el contrato principal, incluido
  en el Componente 1/2; posterior al traspaso, cotizado de forma informativa en
  el Componente 7 (fuera del total evaluado). **Aplica.**
- **Meses de operación incluidos en el alcance:** 4 meses de contrato + 30 días de
  estabilización posterior (fuera de esos 4 meses). **Aplica** — dato crítico para
  06/07.
- **Monitoreo y observabilidad:** panel de observabilidad (M9). **Aplica.**

## 11. Entregables documentales y transferencia

- **Documentación técnica exigida:** arquitectura, flujos, prompts, configuración
  del modelo (RFP §6, entregable 2). **Aplica.**
- **Manuales de usuario/administración:** incluidos en el paquete de traspaso
  (M13). **Aplica.**
- **Capacitación:** a la organización implementadora, aún no definida (Aclaración
  P39); alcance exacto se ajusta cuando IPA la identifique. **Aplica.**
- **Transferencia de conocimiento y código fuente:** exigida en su totalidad (RF-21).
  **Aplica.**
- **Propiedad intelectual:** IPA propietaria de todo lo producido; PI preexistente
  de Campuslands bajo licencia perpetua y transferible para este proyecto
  (Aclaración P58, ADM-05). **Aplica.**

## 12. Licenciamiento y terceros

- **Licencias de software de terceros:** WhatsApp Business Platform (gratuita para
  la cuenta, con costo por mensaje/plantilla) y API de Anthropic (pago por
  consumo); ambas a cargo del proveedor durante el contrato (RFP §11.1.6).
  **Aplica.**
- **Compatibilidad de licencias open source:** los componentes de infraestructura
  reutilizables (frameworks, librerías) permanecen bajo su licencia original;
  IPA recibe licencia suficiente para operar la solución (Aclaración P58).
  **Aplica.**
- **Servicios de terceros con costo recurrente:** mensajería WhatsApp, modelo de
  lenguaje, hosting — todos en el Componente 2/3 del formulario económico.
  **Aplica.**
- **Restricciones de subcontratación:** el RFP no restringe la subcontratación
  técnica en general, pero sí exige que las certificaciones de experiencia sean
  del oferente (Aclaración P2) y que no se presente en consorcio/UT (Aclaración
  P3). Campuslands es el único oferente; cualquier apoyo técnico subcontratado no
  figura ante IPA ni aporta experiencia acreditable. **Aplica** — ver decisión de
  estructura societaria en `wiki/licitaciones/ipa-pr10598.md`.

## 13. Gestión del proyecto

- **Metodología:** Scrum con sprints de 2 semanas, adaptado a la puerta de
  aprobación de IPA para cambios de comportamiento del agente (02 §6). **Aplica.**
- **Gobierno y comités:** coordinación periódica con IPA, sin comité formal
  exigido por el RFP. **Aplica** (buena práctica).
- **Reportería de avance:** reportes periódicos a IPA (M14). **Aplica.**
- **Control de cambios de alcance:** todo cambio de alcance se documenta y se
  acuerda por escrito, especialmente los que tocan prompts/flujos/modelo/KB.
  **Aplica.**
- **Interlocutores y dedicación de IPA:** expertos en la materia para validar la
  clave de respuestas y el umbral de precisión (Aclaración P48-49); disponibilidad
  exacta **[Por confirmar con IPA en la fase de levantamiento]**.

## 14. Restricciones de plazo

- **Fecha de inicio/plazo total:** 4 meses desde la firma (RFP §11.1.5). **Aplica.**
- **Hitos intermedios y su relación con pagos:** 6 entregables con fechas fijas
  (RFP §6); pago tras aceptación de IPA (Aclaración P62). **Aplica.**
- **Penalidades por incumplimiento:** el RFP no detalla un régimen de multas en el
  cuerpo compartido; se remite a los Términos y Condiciones del contrato, no
  disponibles antes de la adjudicación (Aclaración P22). **Por confirmar** — no
  bloquea la propuesta.
- **Dependencias fuera del control de Campuslands:** entrega tardía de insumos de
  IPA (Aclaración P10, riesgo R-01 en §15); condiciones de Meta para el límite de
  mensajería y las tarifas de octubre de 2026 (riesgo R-03/R-05 en §15).
- **Factibilidad del plazo:** validada en `03 - Estimacion de Horas.xlsx`, hoja
  "Método y Factibilidad" — **cabe** dentro de los 4 meses con el equipo
  propuesto.

## 15. Riesgos técnicos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Insumos de IPA (KB, taxonomía, clave de respuestas) llegan tarde | Media | Retraso proporcional de entregables dependientes (sin penalización, Aclaración P10) | Fase de levantamiento (M1) explícita al inicio; solicitar insumos con antelación |
| Escalado de límite de mensajería de WhatsApp insuficiente para 800 destinatarios/día | Media | Retraso en el despliegue escalado | Verificar el negocio y solicitar el escalado antes de firmar; distribuir envíos en varios días; hito propio en el cronograma (M2) |
| Cambio de tarifas de Meta para mensajes de servicio (desde oct-2026) | Media | Sobrecosto en el Componente 3 | Cotizar con la tarifa vigente más reciente disponible; revisar antes de firmar (ver 05) |
| Tasa real de derivación al canal humano supera el 15% declarado | Media-alta | Sobrecosto en el Componente 2 (valor global fijo, lo absorbe el proveedor) | Tasa declarada explícitamente en la propuesta (02 §10); diseño del agente orientado a maximizar resolución automática (M3, M7) |
| Ciclo adicional de remediación de precisión antes de superar el umbral | Media | Retraso de 1-2 semanas antes de escalar (contemplado, Aclaración P53) | Construir la clave de respuestas y el arnés de evaluación (M7) con antelación suficiente |
| Vigencia de tarifas promocionales del modelo de lenguaje vence antes del inicio de operación | Media | Sobrecosto si se cotiza con tarifa promocional | Se cotiza con la tarifa estándar vigente, no la promocional (ver 05) |
| Organización implementadora aún no definida | Baja-media | Ajuste del alcance de capacitación en M13 | Diseñar la solución portable y documentada independientemente del receptor final (Aclaración P39) |

---

## Cierre del entregable

1. **Conclusión sobre IA: SÍ se requiere.** Ver §7. El detalle de tokens y costo
   está en `05 - Analisis IA y Tokens.xlsx`.
2. **Elementos técnicos que impactan el precio y no son desarrollo de
   funcionalidades:** infraestructura de 3 ambientes, licencias/servicios de
   WhatsApp y del modelo de lenguaje, canal humano y guardia 24/7 (dotación
   operativa, costeada en FTE-mes en `07`), pólizas exigidas por el RFP,
   capacitación y transferencia, 30 días de soporte de estabilización.
3. **Supuestos y exclusiones técnicas:** ver 02 §10 (se replican íntegros).
4. **Riesgos técnicos:** ver tabla de §15.
5. **Ítems "Por confirmar con el usuario" pendientes:**
   - Proveedor de nube preferido (o libertad total de Campuslands).
   - Si IPA requerirá acceso directo al panel administrativo (y bajo qué
     autenticación).
   - Uso de marca IPA en contenido del agente (a validar con IPA).
   - Disponibilidad exacta de los expertos de IPA para validar clave de
     respuestas y umbral de precisión.
   - Régimen de penalidades contractuales (no disponible antes de adjudicación).
