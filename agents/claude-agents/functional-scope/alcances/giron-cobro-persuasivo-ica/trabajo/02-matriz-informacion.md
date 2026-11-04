# 02 · Matriz de información (etapa 2 · Lectura)

Fuente única: **F1** = Propuesta comercial y técnica (28-oct-2026). Convención de estado: **PROPUESTO (F1)** = oferta de Campuslands recogida en F1, **no aceptada** por la Alcaldía;
**PENDIENTE** = falta el dato, está sin cifra o hay contradicción. Ningún dato figura como CONFIRMADO porque no hay aceptación del cliente ni actas de la mesa técnica (ver 01-inventario, X1).
Las citas indican sección de F1; «Anexo» = §12 *Anexo técnico integral*.

## A. Hechos, decisiones, cifras y exclusiones

| # | Bloque | Hecho / decisión / cifra | Fuente (F1 · sección) | Estado | Notas |
|---|---|---|---|---|---|
| 1 | Identificación | Cliente: Alcaldía Municipal de Girón; dependencia usuaria: **Dirección de Industria y Comercio**; seguimiento técnico: **Dirección de TIC** | Portada; §6; Anexo · Seguimiento | PROPUESTO (F1) | Sin nombres de responsables por cargo (la Alcaldía debe designarlos) |
| 2 | Identificación | Proveedor: Campuslands S.A.S. BIC · Full Service; firma Yesenia Merchán (Rep. Legal); carta de Diego Tarazona (Gerente Comercial) | Carta; Formalización | PROPUESTO (F1) | Alcalde: «Campo Elías Ramírez», **C.C. en blanco** |
| 3 | Problema y valor | Objeto: prestar servicio de cobro persuasivo con IA para la cartera de ICA mediante plataforma propia de Campuslands, configurada, integrada, operada y mantenida durante la vigencia | §1; Anexo · Objeto | PROPUESTO (F1) | El Anexo dice «plataforma ya en operación»; F1 no dice dónde ni desde cuándo (ver PEN-001) |
| 4 | Problema y valor | Valor declarado: centralización de cartera, mayor cobertura de contacto, trazabilidad, priorización, menos trabajo manual; **no se garantiza** ahorro ni recaudo | §9.3 | PROPUESTO (F1) | Redacción alineada a la regla 6; no hay línea base ni meta medible |
| 5 | Alcance | Modalidad: **servicio** (no licencia aislada), vigencia **1-ene-2027 a 31-dic-2027**; alistamiento nov–dic 2026 sin fee | §1, §3, §9.1; Anexo · Ruta | PROPUESTO (F1) | |
| 6 | Alcance | Implementación en **3 fases** (F1 «Control de la data»; F2 «Gestión automática multicanal con IA»; F3 «Escalamiento a funcionarios y validación») | Anexo · Fases | PROPUESTO (F1) | Cierre de cada fase: sin fecha (CON-004) |
| 7 | Alcance | **15 componentes funcionales** (MOD-01…MOD-15) y **6 transversales** (MOD-16…MOD-21), listados en la sección B | Anexo · Fases y transversales | PROPUESTO (F1) | Identificadores asignados por este agente (estables desde ahora) |
| 8 | Alcance | Fuentes de fiscalización: MAT-SIM (declaraciones ICA), SICOG II (exógena municipal), Cámara de Comercio (2 APIs externas), base de contratos; **vigencias 2021–2026**; «sin limitar el número de contribuyentes» | Anexo · Objeto; Fase 1 · Fiscalización | PROPUESTO (F1) | Fuentes externas «sujetas a acceso o licenciamiento» (PEN-010, PEN-011) |
| 9 | Alcance | Cruce por **documento normalizado** (NIT con o sin DV), porque los omisos pueden no tener RIT ni placa | Fase 1 · Fiscalización | PROPUESTO (F1) | |
| 10 | Alcance | Producto de fiscalización: **listado Excel** de posibles omisos con columna **EMPLAZAR** (por emplazar / no clasificado para emplazamiento / pendiente de validación); un funcionario revisa antes del contacto | Fase 1 · Fiscalización | PROPUESTO (F1) | Campos del listado: «los del requerimiento» (X2 no aportado) |
| 11 | Alcance | Contacto **en cascada**: WhatsApp (plantilla Meta) → correo con link de pago → llamada del agente de voz; reintentos, exclusión y frecuencia parametrizables | Anexo · Flujo; Fase 2 | PROPUESTO (F1) | Ventana de espera entre canales: «definida» sin valor |
| 12 | Alcance | Escalamiento a funcionarios con **acción recomendada**: visitar, enviar recibo, atender solicitud de acuerdo, verificar pago (o negativa) | Anexo · Flujo; Fase 3 | PROPUESTO (F1) | «Enviar recibo» frente a la exclusión de emitir recibos (PEN-016) |
| 13 | Alcance | Mapa de contribuyentes por zona con **Leaflet**, semáforo de gestión, georreferenciación a partir de dirección; sin dirección identificable → «zona adicional» fuera del mapa | Fase 1 · Mapa; §9.6 | PROPUESTO (F1) | Ubicación aproximada; mejora con coordenadas tomadas en visita; sin umbral de calidad (PEN-022) |
| 14 | Alcance | Visitas: asignación por funcionario y zona; formulario digital desde celular (fecha, hora, funcionario, adjuntos) cuyos campos salen del formato que entregará la Alcaldía | Fase 3 · Visitas | PROPUESTO (F1) | Formato no aportado (X5) |
| 15 | Alcance | Pagos (versión básica): importación **periódica** del recaudo del operador oficial (fuente de verdad), asociación a placa y obligación, actualización de estado, novedades para revisión manual | Fase 3 · Verificación de pagos | PROPUESTO (F1) | Periodicidad y formato: sin definir (PEN-011) |
| 16 | Exclusión | **No** emite cobros oficiales ni recibos (los emite el operador oficial; la plataforma redirige al link de pago); **no** hace cobro coactivo | §1; Anexo · Objeto; Fuera de alcance | PROPUESTO (F1) | |
| 17 | Exclusión | Fuera de alcance: emisión de cobros e impresión de recibos; **visor** de trámites inmobiliarios y de construcción; gestión de **dineros embargados** | Anexo · Fuera de alcance | PROPUESTO (F1) | §11 añade «actos tributarios oficiales» y «cobro coactivo» (CON-002) |
| 18 | Fases futuras | **Fase 4** (ampliación, fuera del servicio inicial): acuerdos de pago; conciliación automática de pagos; asistente por voz para funcionarios; cobro coactivo; fiscalización con DIAN; ReteICA y Autorretención. Se contratan aparte | §11; Anexo · Ampliaciones | PROPUESTO (F1) | No es entregable actual |
| 19 | IA y automatización | Agente de **voz** (Retell AI): llama, se identifica como asistente virtual de la Alcaldía, consulta datos autorizados, maneja objeciones **solo con guiones aprobados**, registra intención/compromiso, transcribe, resume y clasifica | §2; Anexo · IA; Fase 2 | PROPUESTO (F1) | Sin métricas de calidad ni límites cuantitativos (PEN-019) |
| 20 | IA y automatización | Agente de **WhatsApp**: conversación en lenguaje natural, consulta obligaciones, lleva al link de pago oficial, atiende «a cualquier hora» | Anexo · IA; Fase 2 | PROPUESTO (F1) | |
| 21 | IA y automatización | **Asistente de consulta** en lenguaje natural sobre cartera, contribuyente e indicadores | Anexo · IA; Fase 2 · Dashboard de gestión | PROPUESTO (F1) | Aparece en la tabla de IA y en una línea del dashboard; sin ficha propia ni fase explícita (PEN-024) |
| 22 | IA y automatización | La IA no toma decisiones tributarias; georreferenciación, depuración y cruces son **herramientas convencionales**, no IA | §9.2, §9.5 | PROPUESTO (F1) | |
| 23 | IA y automatización | Gobierno de IA: límites de actuación, identificación como asistente virtual, escalamiento a humano, **borrador** de política institucional de IA (referencia UNESCO) | Anexo · Gobierno de IA | PROPUESTO (F1) | |
| 24 | Datos e integraciones | Integraciones (13 en alcance, INT-01…INT-13, + 1 futura, INT-14): ver sección C | Anexo · Integraciones | PROPUESTO (F1) | |
| 25 | Datos e integraciones | La información operativa principal **se mantiene en infraestructura de la Alcaldía**; proveedores externos procesan voz, WhatsApp, correo y LLM; el audio **no transita** por la red de la Alcaldía | §2, §4; Anexo · Arquitectura | PROPUESTO (F1) | Grabaciones, transcripciones, retención y tratamiento: «se definirá con TIC y jurídica» |
| 26 | No funcionales | Seguridad: roles, cifrado en tránsito y de información sensible, gestión de secretos, logs de auditoría (funcionarios y agentes), pruebas básicas **OWASP**, Ley 1581 de 2012 | Anexo · Seguridad | PROPUESTO (F1) | Sin matriz de roles ni de permisos (PEN-013) |
| 27 | No funcionales | Contacto sujeto a **Ley 2300 de 2023**; horarios y frecuencia por concepto jurídico de la Alcaldía | Fase 2 · Motor de campañas; Insumos | PROPUESTO (F1) | Concepto no aportado (X6) |
| 28 | No funcionales | Disponibilidad, rendimiento, concurrencia, RTO/RPO: **no hay cifras**. Respaldo y contingencia del data center: a cargo de la Alcaldía; Campuslands define qué respaldar y prueba restauración | Anexo · Responsabilidades; §9.6 | PENDIENTE | (CON-003; PEN-007) |
| 29 | No funcionales | Soporte: correo `dev@campuslands.com`, **lunes a viernes 8:00–17:00**; tiempos de respuesta por criticidad en un **SLA contractual** aún no definido; «no se presume 24/7» | §7; Anexo · Operación | PENDIENTE (SLA) | Horario PROPUESTO (F1); tiempos PENDIENTES |
| 30 | Arquitectura | Backend Node.js + TypeScript + TypeORM; Vue.js; MariaDB; Redis; Ubuntu Server 24.04 LTS; proxy HTTPS con certificado del dominio de la Alcaldía; Leaflet; **on-premise** en máquinas virtuales de la Alcaldía, sin GPU | §5; Anexo · Stack | PROPUESTO (F1) | |
| 31 | Arquitectura | Servidores de referencia: aplicación 8 vCPU / 16 GB / 100 GB SSD; BD 4–8 vCPU / 16–32 GB / 200 GB SSD + crecimiento; pruebas 4 vCPU / 8–16 GB / 100 GB; grabaciones ≈30 GB/mes | Anexo · Infraestructura | PROPUESTO (F1) | «A ajustar con el volumen real» — volumen sin definir (PEN-003) |
| 32 | Arquitectura | Conectividad: **canal dedicado de 50 Mbps** contratado y pagado por la Alcaldía; entrada pública HTTPS 443 para webhooks de Meta y voz | §4; Anexo · Infraestructura | PROPUESTO (F1) | |
| 33 | Arquitectura | Diagrama de arquitectura de alto nivel | Anexo · Arquitectura | **PENDIENTE** | Marcador de posición; **no está insertado** |
| 34 | Entregables | Entregables por fase (11): parametrización; arquitectura de despliegue; cartera depurada con informe de calidad; servicio F1; servicio F2; servicio F3; informe de validación en operación real; borrador de política de IA; SBOM y plan de salida; código fuente y documentación (solo con opción de compra); manuales, capacitación y acta de inicio | Anexo · Entregables | PROPUESTO (F1) | Aceptación: pruebas de funcionarios **contra criterios que define el levantamiento** (aún no existen) y acta por fase (PEN-006) |
| 35 | Proyecto | Calendario: nov–dic 2026 alistamiento; **1.er día hábil de enero 2027** inicio operativo con «capacidades validadas»; feb–jun 2027 habilitación progresiva (F1–F3); jul–oct 2027 optimización; nov–dic 2027 balance y decisión sobre la opción de compra | §3; Anexo · Ruta | PROPUESTO (F1) | Cronograma definitivo lo aprueba la mesa técnica, jurídica y financiera |
| 36 | Proyecto | Equipo: 8 perfiles (gerente del servicio, líder técnico, integraciones y datos, IA conversacional, infraestructura, analista funcional y de soporte, UX, 2 desarrolladores junior «Camper») | §8; Anexo · Equipo | PROPUESTO (F1) | «Asignación según necesidades de cada etapa»: sin dedicación |
| 37 | Proyecto | Seguimiento institucional: TIC (disponibilidad, integraciones, seguridad, infraestructura) y Dirección de ICA (campañas, indicadores, funcionamiento, facturación); **sin** supervisión por informe de actividades | §6; Anexo · Seguimiento | PROPUESTO (F1) | Indicadores y umbrales: sin definir |
| 38 | Proyecto | Capacitación a funcionarios, documentación técnica, manuales de operación y de usuario, puesta en producción y estabilización inicial | Anexo · Capacitación | PROPUESTO (F1) | Número de sesiones/personas/horas: sin definir |
| 39 | Proyecto | Responsabilidades de la Alcaldía: VMs, almacenamiento, dominio, SSL, VPN, 50 Mbps, lista blanca, accesos a fuentes y recaudo, correo remitente institucional, cuenta Meta Business y números, capa geográfica, formato de visita, procedimientos, concepto jurídico, aprobación de guiones y textos (**14 insumos**) | Anexo · Insumos y Responsabilidades | PROPUESTO (F1) | Casillas sin marcar (☐); sin fecha de entrega ni responsable nominal (PEN-005) |
| 40 | Comercial | **Fee mensual $50.000.000 COP**, impuestos incluidos, enero–diciembre 2027 (12 cuotas → **$600.000.000 COP** en la vigencia, cálculo de este agente) | §9.6 | PROPUESTO (F1) | Sin desglose ni cotización (X3) |
| 41 | Comercial | **Opción facultativa de compra (marca blanca): $540.000.000 COP**, impuestos incluidos, diciembre 2027; los pagos mensuales **no** son abono al precio | §9.6 | PROPUESTO (F1) | |
| 42 | Comercial | Facturación desde enero 2027; **pago a mes vencido desde febrero 2027** (el pago de diciembre cae en enero de 2028, deducción de este agente); «valores incluyen IVA y demás impuestos, **retenciones** y estampillas» | §9.6 | PROPUESTO (F1) | Ambigüedad tributaria y presupuestal (PEN-012) |
| 43 | Comercial | Campuslands asume en el fee: consumo de llamadas/telefonía, WhatsApp, correo y LLM «de acuerdo con las necesidades de la operación»; consumos extraordinarios sujetos a autorización previa; sin cobros automáticos por exceso | §5, §9.2; Anexo · Consumo | PROPUESTO (F1) | **Sin volúmenes de referencia** (PEN-002; CON-006) |
| 44 | Comercial | Costos de terceros que **no** aparecen asignados: dos APIs de Cámara de Comercio (proveedor, tarifa), proveedor LLM («por definir»), geocodificación, licencias de virtualización (esta sí: Alcaldía) | Anexo · Integraciones; Responsabilidades | PENDIENTE | PEN-010 |
| 45 | Legal / PI | Plataforma y configuración de agentes: propiedad de Campuslands; con la opción de compra se transfieren **«derechos de uso, explotación y adaptación» en marca blanca, código fuente y documentación**; terceros (Retell, Twilio/Telnyx, Meta, correo, LLM) no se transfieren; código abierto conserva sus licencias | §9.6; Anexo · Componentes | PROPUESTO (F1) | Regla 9: **revisión jurídica** (PEN-008) |
| 46 | Legal / PI | Campuslands entrega **SBOM** y **plan de salida** con exportación de datos por proveedor externo | §5; Anexo · Stack, Entregables | PROPUESTO (F1) | |
| 47 | Legal | Formalización: vinculante al firmar los representantes y cumplirse requisitos **legales, presupuestales y contractuales**; modificaciones por escrito | Formalización | PROPUESTO (F1) | Documento no firmado |
| 48 | Legal | Mesa técnica, jurídica, administrativa y financiera para aprobar insumos, infraestructura, condiciones, aceptación, cronograma, **consumo de referencia**, protección de datos y condiciones de compra | §10 | PENDIENTE | Es el mecanismo de cierre de casi todos los pendientes |
| 49 | Legal | Garantía, penalidades, terminación anticipada, reajuste de precio, confidencialidad contractual, responsabilidad por errores de la IA: **no mencionados** | — | **PENDIENTE** | PEN-007, PEN-012 |

## B. Módulos identificados (candidatos a ficha funcional §5.1)

| ID | Fase | Módulo | Límite verificable en F1 | Entradas / salidas | Aceptación | Estado |
|---|---|---|---|---|---|---|
| MOD-01 | 1 | Levantamiento y parametrización | Sí: documento con reglas de negocio y criterios | Procedimientos, sesiones → documento | Acta de la Fase 1 | PROPUESTO (F1) |
| MOD-02 | 1 | Arquitectura de despliegue e integración | Parcial: documento previo a crear las VMs | Servidores, puertos, dominios → documento | Acta | PROPUESTO (F1) |
| MOD-03 | 1 | Fiscalización (cruce de 4 fuentes, listado EMPLAZAR) | Parcial: sin volumen ni precisión | MAT-SIM, SICOG II, Cámara, contratos → Excel | PENDIENTE (criterios aún no existen) | PROPUESTO (F1) |
| MOD-04 | 1 | Núcleo de gestión de cartera y cobro | Parcial: «priorización empezando por mayor monto» | Obligaciones, pagos → expedientes, semáforo | PENDIENTE | PROPUESTO (F1) |
| MOD-05 | 1 | Dashboard de cartera | Parcial: filtros, exportación, móvil | Cartera → vistas y reportes | PENDIENTE | PROPUESTO (F1) |
| MOD-06 | 1 | Mapa de contribuyentes por zona | Parcial: sin umbral de georreferenciación | Direcciones, capa de zonas → mapa | PENDIENTE | PROPUESTO (F1) |
| MOD-07 | 2 | Motor de campañas | Parcial: sin concurrencia, horarios ni frecuencia | Segmentos, reglas → mensajes y llamadas | PENDIENTE | PROPUESTO (F1) |
| MOD-08 | 2 | Agente de IA de voz | Parcial: sin métricas | Datos de deuda, guion → llamada, transcripción, clasificación | PENDIENTE | PROPUESTO (F1) |
| MOD-09 | 2 | Agente de IA de WhatsApp | Parcial | Plantillas Meta, obligaciones → conversación | PENDIENTE | PROPUESTO (F1) |
| MOD-10 | 2 | Canal de correo | Sí: envío masivo programado con plantillas | Campaña → correo con link de pago | PENDIENTE | PROPUESTO (F1) |
| MOD-11 | 2 | Dashboard de gestión | Parcial | Intentos y resultados → indicadores por canal | PENDIENTE | PROPUESTO (F1) |
| MOD-12 | 3 | Gestión de casos escalados | Parcial | Casos con acción recomendada → bandeja y transferencia | PENDIENTE | PROPUESTO (F1) |
| MOD-13 | 3 | Gestión de visitas | Parcial: depende del formato de visita | Asignación → formulario, estado del caso | PENDIENTE | PROPUESTO (F1) |
| MOD-14 | 3 | Verificación de pagos (básica) | Parcial: depende de recaudo | Recaudo del operador → estado de cartera, novedades | PENDIENTE | PROPUESTO (F1) |
| MOD-15 | 3 | Validación en operación real | Parcial | Cartera real → informe de validación | Informe de validación | PROPUESTO (F1) |
| MOD-16 | Transv. | Seguridad, privacidad y auditoría | Parcial | — | PENDIENTE | PROPUESTO (F1) |
| MOD-17 | Transv. | Gobierno de IA | Parcial: borrador de política | — | Borrador de política | PROPUESTO (F1) |
| MOD-18 | Transv. | Pruebas y validación | Sí: 5 familias de pruebas | — | Pruebas con funcionarios | PROPUESTO (F1) |
| MOD-19 | Transv. | Alistamiento y despliegue en la nube privada de la Alcaldía | Sí: 8 actividades listadas | VMs → entornos de pruebas y producción | Manual de operación para TIC | PROPUESTO (F1) |
| MOD-20 | Transv. | Capacitación y puesta en producción | Parcial | — | Acta de inicio, manuales | PROPUESTO (F1) |
| MOD-21 | Transv. | Operación del servicio | Parcial: horario, mantenimiento correctivo, monitoreo | Solicitudes → tickets | SLA (pendiente) | PROPUESTO (F1) |

## C. Matriz de integraciones (INT)

| ID | Sistema | Para qué | Mecanismo declarado | Fase | Evidencia de acceso (regla 8) | Estado |
|---|---|---|---|---|---|---|
| INT-01 | Cámara de Comercio — API externa A | Municipio de registro y fecha de última renovación | HTTPS | 1 | **Ninguna**: proveedor sin nombre; credenciales las habilita la Alcaldía | PENDIENTE |
| INT-02 | Cámara de Comercio — API externa B | Ídem, para consolidar | HTTPS | 1 | **Ninguna** | PENDIENTE |
| INT-03 | MAT-SIM | Declaraciones de ICA | «API interna» | 1 | **Ninguna**: sin diccionario ni confirmación de que exista API | PENDIENTE |
| INT-04 | SICOG II | Exógena municipal | «API interna» | 1 | **Ninguna** | PENDIENTE |
| INT-05 | Base de contratos de la Alcaldía | Contratistas del municipio | «API interna» | 1 | **Ninguna** | PENDIENTE |
| INT-06 | Capa geográfica de zonas y geocodificación | Mapa | shapefile / GeoJSON + servicio de geocodificación | 1 | Capa: insumo de la Alcaldía; servicio de geocodificación sin nombre | PENDIENTE |
| INT-07 | Modelo de lenguaje | Asistente y agentes | HTTPS | 1 y 2 | Proveedor «por definir» | PENDIENTE |
| INT-08 | API de WhatsApp Business (Meta) | Canal WhatsApp | API + webhooks | 2 | Cuenta: CON-001 | PENDIENTE |
| INT-09 | Retell AI | Agente de voz | API + webhooks | 2 | Proveedor nombrado; condiciones de uso no aportadas | PROPUESTO (F1) |
| INT-10 | Twilio o Telnyx | Telefonía, números colombianos | SIP | 2 | Elección sin cerrar (CON-008) | PENDIENTE |
| INT-11 | Proveedor de correo | Correo, dominio institucional (SPF, DKIM, DMARC) | API o SMTP | 2 | Proveedor sin nombre | PENDIENTE |
| INT-12 | Operador oficial — link de pago | Pago del ciudadano | Enlace en mensajes | 2 | Operador sin nombre; link por entregar | PENDIENTE |
| INT-13 | Operador oficial — recaudo | Verificación de pagos | Importación periódica | 3 | Operador sin nombre; formato y periodicidad sin definir | PENDIENTE |
| INT-14 | DIAN | Fiscalización | Convenio / solicitud formal | **Fase 4 (fuera del servicio inicial)** | — | Excluido |

## D. Contradicciones y tensiones entre secciones de F1

Se muestran **ambas versiones**; este agente no elige cuál prevalece.

| ID | Tema | Versión A (F1 · sección) | Versión B (F1 · sección) | Prevalece | Confirmado por / fecha |
|---|---|---|---|---|---|
| CON-001 | Cuenta de WhatsApp Business | «La cuenta **ya está a nombre de la Alcaldía**» (Anexo · tabla de componentes) | La cuenta de Meta Business y el número a nombre de la Alcaldía **son un insumo por entregar**, con documentos de verificación (Anexo · Insumos y Responsabilidades) | PENDIENTE | |
| CON-002 | Exclusiones | §11: se excluyen **actos tributarios oficiales, emisión de recibos, cobro coactivo, visor inmobiliario y fondos embargados** (5) | Anexo · Fuera de alcance: **3** exclusiones (cobros/recibos, visor, embargos); el cobro coactivo figura como **ampliación Fase 4**, y «actos tributarios oficiales» no se lista | PENDIENTE | |
| CON-003 | Quién ejecuta los respaldos | §4 y Responsabilidades: la **Alcaldía** aporta y ejecuta backups, réplica y contingencia | Alistamiento: **Campuslands** programa «respaldos de la base de datos» como tarea programada; §9.6: «se coordinará con TIC» | PENDIENTE | |
| CON-004 | Qué hay el primer día y cuándo cierra cada fase | §1, §3: operación funcional **desde el 1.er día hábil de enero 2027** con «capacidades validadas» y **fee desde enero** | §3, Anexo: módulos y canales de las **fases 1 a 3 se habilitan de forma progresiva feb–jun 2027**; «las funcionalidades habilitadas al inicio… se documentarán en actas» (no están listadas) | PENDIENTE | |
| CON-005 | Fiscalización (F1) vs. motor de campañas (F2) | Fase 1 · Fiscalización incluye el **contacto en cascada** a los «por emplazar» y el entregable «Servicio habilitado con… fiscalización» es de F1 | Esa cascada «usa el motor de campañas y los canales de la **Fase 2**»; el entregable del motor es de F2 | PENDIENTE | |
| CON-006 | Consumos por encima de la referencia | §9.2: «consumos extraordinarios sujetos a **autorización previa**» | Anexo: los volúmenes por encima de la referencia «se aprueban antes… y **no generan cobros automáticos**». No dice quién asume el costo una vez aprobados; y **no existe** volumen de referencia (§9.3: «sin establecer cantidades numéricas») | PENDIENTE | |
| CON-007 | Fecha y estado del documento | Portada: **28-oct-2026**, «para revisión técnica, jurídica, financiera y contractual» | Bloque de firma: «se firma su aceptación a los **veintitrés (29)** días del mes de octubre de 2026» en el archivo leído; una captura posterior del usuario muestra «veintitrés (23)»; cédula del alcalde en blanco | PENDIENTE | |
| CON-008 | Proveedor de telefonía | Texto, stack y matriz de propiedad: «**Twilio o Telnyx**» | Matriz de integraciones y Fase 2: solo **Twilio** (y «Telynx» en una viñeta) | PENDIENTE | |

## E. Texto de F1 que parece haber perdido su contenido (para corregir antes de cualquier documento al cliente)

| Ubicación en F1 | Texto actual | Observación |
|---|---|---|
| §2 | «La meta de referencia es de llamadas acordes a las necesidades de la operación, con dimensionamiento de minutos…» | Sin cantidad: parece una cifra eliminada |
| Fase 1 · intro | «consultan… la cartera de **unos** contribuyentes identificados» | Sin cifra |
| Fase 2 · intro | «meta operativa de llamadas acordes a las necesidades de la operación» | Sin cifra |
| Consumo · tabla | «llamadas acordes a las necesidades de la operación, **unos minutos** según las necesidades de la operación» | Frase circular; sin base de cálculo |
| Anexo · Consumo | «Los volúmenes por **encima de esta referencia**…» | La referencia no existe |
| Anexo · Arquitectura | «[embedded content: arquitectura…]» | Diagrama ausente |
| Varios | «Telynx», «telnyx», «sistema operativo» (minúscula), «Implementacion», «Informe técnico» repetido | Editorial |
