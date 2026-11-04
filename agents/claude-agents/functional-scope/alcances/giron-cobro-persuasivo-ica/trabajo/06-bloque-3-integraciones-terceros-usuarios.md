# 06 · Bloque 3 — Integraciones, terceros y usuarios (base para las secciones 4 y 6 del documento)

**Criterio (DEC-008):** todo sale **únicamente de la propuesta (F1)**. Lo que F1 no declara no se pregunta ni se completa: se escribe `[PENDIENTE DE VALIDACIÓN]`.
Estado de lo que sí dice F1: **PROPUESTO (F1)** (oferta sin aceptación de la Alcaldía). Referencias: INT = `02-matriz-informacion.md` §C; PEN = `03-pendientes.md`.

---

## Sección 6 del documento — Fuentes de datos e integraciones

### 6.1 Matriz por sistema (lo que declara F1)

| ID | Sistema | Propósito en el servicio | Datos / mecanismo declarado | Fase | Quién habilita el acceso (F1) | Estado |
|---|---|---|---|---|---|---|
| INT-03 | MAT-SIM | Fiscalización: declaraciones de ICA | **Lectura.** «API interna». Cruce por documento normalizado (NIT con o sin DV) | 1 | Alcaldía: diccionario de datos y acceso a la API | PROPUESTO (F1). Existencia y documentación de la API: `[PENDIENTE DE VALIDACIÓN]` |
| INT-04 | SICOG II | Fiscalización: exógena municipal | **Lectura.** «API interna» | 1 | Alcaldía: diccionario de datos y acceso a la API | PROPUESTO (F1). Ídem |
| INT-05 | Base de contratos de la Alcaldía | Fiscalización: contratistas del municipio | **Lectura.** «API interna» | 1 | Alcaldía: diccionario de datos y acceso | PROPUESTO (F1). Ídem |
| INT-01 / INT-02 | Cámara de Comercio (dos APIs externas de proveedores) | Fiscalización: **municipio de registro** y **fecha de última renovación**; las respuestas se integran y cruzan | **Lectura**, HTTPS. La dirección exacta **no** es un dato garantizado | 1 | Alcaldía: habilitación y credenciales autorizadas; definición de los campos a consultar | PROPUESTO (F1). Proveedores, tarifa y condiciones de acceso: `[PENDIENTE DE VALIDACIÓN]` |
| INT-06 | Capa geográfica de zonas y geocodificación | Mapa de contribuyentes por zona | Capa de zonas en shapefile o GeoJSON; servicio de geocodificación; mapa base de OpenStreetMap (Leaflet) | 1 | Alcaldía: capa de zonas | PROPUESTO (F1). Servicio de geocodificación: `[PENDIENTE DE VALIDACIÓN]` |
| INT-07 | Modelo de lenguaje | Agentes y asistente de consulta | API por HTTPS; consumo dentro del fee | 1 y 2 | Campuslands | PROPUESTO (F1). Proveedor: «por definir» → `[PENDIENTE DE VALIDACIÓN]` |
| INT-08 | API de WhatsApp Business (Meta) | Canal WhatsApp | API saliente y webhooks entrantes por HTTPS; plantillas aprobadas por Meta | 2 | Alcaldía: cuenta de Meta Business y número a su nombre, con documentos de verificación; Campuslands: configuración y acompañamiento de la verificación | PROPUESTO (F1). Contradicción CON-001 sobre si la cuenta ya existe |
| INT-09 | Retell AI | Agente de voz | API saliente y webhooks de consulta (datos del contribuyente y deuda) y de resultado | 2 | Campuslands | PROPUESTO (F1) |
| INT-10 | Twilio o Telnyx | Llamadas a números colombianos | SIP entre la plataforma de voz y el operador | 2 | Alcaldía: números publicados en su web y a su nombre; Campuslands: contratación y pago de la telefonía | PROPUESTO (F1). Elección entre los dos: `[PENDIENTE DE VALIDACIÓN]` (CON-008) |
| INT-11 | Proveedor de correo | Canal de correo con dominio institucional | API o SMTP; SPF, DKIM y DMARC | 2 | Alcaldía: dirección remitente institucional y registros en su dominio; Campuslands: envío desde su proveedor | PROPUESTO (F1). Proveedor: `[PENDIENTE DE VALIDACIÓN]` |
| INT-12 | Operador oficial — link de pago | Pago del ciudadano | Enlace incluido en mensajes de WhatsApp y correo | 2 | Alcaldía: link de pago | PROPUESTO (F1). Operador: `[PENDIENTE DE VALIDACIÓN]` |
| INT-13 | Operador oficial — recaudo | Verificación de pagos (fuente de verdad de los pagos) | **Importación periódica**; asocia pagos con placa y obligación; genera novedades para revisión manual | 3 | Alcaldía: acceso a la información de recaudo | PROPUESTO (F1). Periodicidad y formato: `[PENDIENTE DE VALIDACIÓN]` |
| INT-14 | DIAN (exógena y renta) | Fiscalización | Convenio o solicitud formal de intercambio | **Fase 4 (ampliación, no incluida)** | — | Fuera del alcance actual |

*Nota.* F1 no aporta documentación técnica ni pruebas de acceso de ninguna de estas fuentes. El documento debe decir que **las integraciones con fuentes externas dependen de la disponibilidad efectiva de datos y de accesos autorizados** (frase del propio Anexo), sin presuponer capacidades de las APIs.

### 6.2 Servicios de terceros y quién los asume (según F1)

| Servicio | Lo que dice F1 sobre costo y titularidad | Con la opción de compra (F1) | Estado |
|---|---|---|---|
| Retell AI (voz) | Consumo incluido en el fee | Sigue con su proveedor, bajo sus condiciones | PROPUESTO (F1) |
| Twilio o Telnyx (telefonía) | Campuslands contrata y paga; los números quedan a nombre de la Alcaldía | Sigue con su proveedor | PROPUESTO (F1) |
| WhatsApp Business (Meta) | Campuslands paga el consumo; la cuenta queda a nombre de la Alcaldía | Cuenta ya a nombre de la Alcaldía; el servicio sigue con Meta | PROPUESTO (F1); CON-001 |
| Correo | Campuslands envía desde su proveedor y paga el consumo; remitente institucional definido por la Alcaldía | Sigue con su proveedor | PROPUESTO (F1) |
| Modelo de lenguaje | Consumo incluido en el fee | Sigue con su proveedor | PROPUESTO (F1); proveedor `[PENDIENTE DE VALIDACIÓN]` |
| Dos APIs de Cámara de Comercio | **F1 no dice quién paga** el consumo ni la licencia; solo que la Alcaldía habilita credenciales | `[PENDIENTE DE VALIDACIÓN]` | Costo no asignado en F1 |
| Servicio de geocodificación | F1 no lo asigna | `[PENDIENTE DE VALIDACIÓN]` | Costo no asignado en F1 |
| Node.js, Vue.js, MariaDB, Redis, Leaflet, OpenStreetMap | Código abierto; sin costo de licencia declarado | Conservan sus licencias abiertas | PROPUESTO (F1) |
| Servidores, almacenamiento, licencias de virtualización, canal de 50 Mbps, VPN, dominio y certificado SSL | **Alcaldía** (suministra y financia) | — | PROPUESTO (F1) |

Consumos por encima de la referencia: F1 dice que se aprueban antes con la Alcaldía y que no generan cobros automáticos; **no hay volumen de referencia** (DEC-004) → el documento lo marca `[PENDIENTE DE VALIDACIÓN]`. Campuslands entrega SBOM y plan de salida por proveedor externo.

### 6.3 Responsabilidades sobre datos e integración (tabla de F1, sin cambios)

| Tema | Alcaldía | Campuslands |
|---|---|---|
| Datos | Acceso a las fuentes de fiscalización, diccionario de datos, acceso a recaudo y link de pago | Cruce de fuentes, depuración, carga y controles de calidad |
| Red y seguridad | Dominio y certificado SSL, publicación HTTPS para webhooks, lista blanca de salida, VPN para el equipo de Campuslands, ruta por la VPN existente, canal de 50 Mbps | Lista de puertos y dominios a habilitar; hardening de la aplicación |
| Respaldo y continuidad | Ejecución de backups, réplica fuera del servidor principal, contingencia del data center (RTO/RPO) | Definición de qué respaldar y prueba de restauración con TIC (ver CON-003) |

---

## Sección 4 del documento — Usuarios y permisos

F1 no trae una sección de usuarios ni una matriz de permisos. Se extraen **los actores que F1 menciona** y lo que cada uno hace; los permisos concretos quedan pendientes.

| Actor | Qué hace según F1 | Módulos | Permisos |
|---|---|---|---|
| Alcalde y funcionarios | Consultan en tiempo real la cartera por zona, vigencia, estado y monto, desde computador o celular (Fase 1) | MOD-05, MOD-06 | `[PENDIENTE DE VALIDACIÓN]` |
| Funcionarios de la Dirección de Industria y Comercio | Revisan la clasificación EMPLAZAR antes del contacto; atienden la bandeja de casos escalados (visita, solicitud de acuerdo, verificación de pago, negativa); registran la gestión humana; hacen seguimiento financiero, administrativo y funcional del servicio | MOD-03, MOD-04, MOD-11, MOD-12 | `[PENDIENTE DE VALIDACIÓN]` |
| Funcionarios que realizan visitas | Reciben asignación por zona y registran el resultado en el formulario digital desde el celular (fecha, hora, funcionario, adjuntos) | MOD-13 | `[PENDIENTE DE VALIDACIÓN]` |
| Dirección de TIC | Entrega máquinas virtuales, dominio, VPN, canal y accesos; seguimiento técnico (disponibilidad, integraciones, seguridad, infraestructura); recibe el manual de operación | MOD-02, MOD-16, MOD-19 | `[PENDIENTE DE VALIDACIÓN]` |
| Área jurídica de la Alcaldía | Aprueba guiones, plantillas, reglas de campaña, textos legales, horarios y frecuencia de contacto | MOD-07, MOD-08, MOD-09 | `[PENDIENTE DE VALIDACIÓN]` |
| Equipo de Campuslands | Configura, integra, opera y da soporte; accede por VPN con usuarios nominales | MOD-19, MOD-21 | Usuarios nominales por VPN (PROPUESTO F1); alcance de acceso a datos `[PENDIENTE DE VALIDACIÓN]` |
| Contribuyentes (usuarios externos) | Reciben WhatsApp, correo y llamadas del asistente virtual de la Alcaldía; pagan por el link oficial | MOD-08, MOD-09, MOD-10 | No tienen cuenta en la plataforma (según F1) |

Lo único que F1 declara sobre permisos: autenticación y **autorización basada en roles**, gestión de usuarios funcionarios, cifrado en tránsito y de información sensible, y **logs de auditoría** de las acciones de funcionarios y agentes de IA. No define roles, número de usuarios ni visibilidad por perfil → PEN-013.

---

## Qué queda `[PENDIENTE DE VALIDACIÓN]` en estas dos secciones
PEN-010 (proveedores y costos de Cámara, LLM, correo, geocodificación, telefonía), PEN-011 (existencia y acceso de las APIs internas, formato del recaudo), PEN-013 (roles y permisos), CON-001, CON-003 y CON-008.
