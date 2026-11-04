"""Construye el documento de Alcance Funcional (Alcaldía de Girón · cobro persuasivo con IA).

Todo el contenido sale de la propuesta comercial y técnica del 2026-10-28 (única fuente). Lo que la propuesta no declara
se escribe «[PENDIENTE DE VALIDACIÓN]». Uso (desde cualquier carpeta):
    python construir_borrador.py <carpeta_temporal_para_el_diagrama>
"""
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
from docx.shared import Cm  # noqa: E402
from alcance_docx import Alcance, FIRMA_IZQ, PENDIENTE_TXT as P  # noqa: E402

TMP = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI
FECHA_ISO = "2026-10-29"
SALIDA = AQUI.parent / "entrega" / f"Alcance Funcional - Alcaldía de Girón - v0.1 - {FECHA_ISO}.docx"
FUENTE = "Propuesta comercial y técnica (2026-10-28)"


def f(sec: str) -> str:
    return f"PROPUESTO — fuente: {FUENTE}, {sec}"


a = Alcance()

# Anchos mínimos para que «PROPUESTO», «PENDIENTE» e «Identificadores» no se partan en dos líneas.
_tabla_base = a.tabla


def _tabla(titulo, encabezados, filas, pesos, nota=None):
    pesos = list(pesos)
    minimos = {"Estado": 1.45, "Identificadores": 1.5, "Fase": 0.75}
    for i, h in enumerate(encabezados):
        if h in minimos:
            pesos[i] = max(pesos[i], minimos[h])
    _tabla_base(titulo, encabezados, filas, pesos, nota)


a.tabla = _tabla

# ------------------------------------------------------------------ portada y control
datos = {
    "titulo": "Servicio inteligente de cobro persuasivo y fiscalización tributaria con IA",
    "cliente": "Alcaldía Municipal de Girón",
    "area": "Industria y Comercio (ICA)",
    "fecha": "29 de octubre de 2026",
    "nota": "Documento confidencial — Para revisión técnica, comercial y jurídica",
}
a.portada(datos)

a.carta_presentacion({
    "lugar_fecha": "Girón, 29 de octubre de 2026",
    "destinatario": ["Señores", "ALCALDÍA MUNICIPAL DE GIRÓN"],
    "asunto": "Alcance funcional del servicio inteligente de cobro persuasivo y fiscalización tributaria con IA — Industria y Comercio (ICA)",
    "parrafos": [
        "Campuslands S.A.S. BIC presenta a la Alcaldía Municipal de Girón el documento de alcance funcional del servicio inteligente de cobro "
        "persuasivo con IA para Industria y Comercio. A partir de la propuesta comercial y técnica del 28 de octubre de 2026, el documento "
        "describe lo siguiente:",
        "El servicio automatiza la gestión multicanal, incluida la interacción conversacional por voz, con intervención de funcionarios cuando "
        "se requiere, sobre infraestructura de la Alcaldía y servicios especializados de IA en nube pública. No sustituye las actuaciones "
        "tributarias oficiales, no emite recibos oficiales ni ejecuta cobro coactivo.",
        "Los datos que la propuesta no declara están marcados como " + P + " y se validarán con los responsables antes de la firma. "
        "Agradecemos la revisión de la Dirección de TIC y de la Dirección de Industria y Comercio.",
    ],
    "vinetas": [
        "El alcance del servicio por fases, con una ficha funcional por módulo (secciones 3 y 5).",
        "Los usuarios, las integraciones con sistemas de la Alcaldía y de terceros, y el uso de IA con sus límites (secciones 4, 6 y 7).",
        "Los entregables con su aceptación, el cronograma, el soporte y las condiciones comerciales (secciones 10 a 14).",
        "Los supuestos, las exclusiones, los riesgos y los pendientes por validar (sección 15).",
    ],
    "firmante": {"nombre": "DIEGO TARAZONA", "cargo": "Gerente Comercial", "entidad": "Campuslands S.A.S. BIC", "correo": "diego@campuslands.com"},
})

a.tabla_de_contenido()

# ------------------------------------------------------------------ 1. Resumen ejecutivo
a.h1("1. Resumen ejecutivo")
a.parrafo("Campuslands S.A.S. BIC propone a la Alcaldía Municipal de Girón un servicio de cobro persuasivo con inteligencia artificial "
          "para la cartera de Industria y Comercio (ICA). El servicio se presta sobre una plataforma de Campuslands, desplegada en la "
          "infraestructura de la Alcaldía, que cruza fuentes institucionales para identificar posibles omisos, contacta a los contribuyentes "
          "por WhatsApp, correo y llamada con un agente de voz, y entrega a los funcionarios cada caso procesado con una acción recomendada.")
a.parrafo("La plataforma no sustituye las actuaciones tributarias oficiales, no emite recibos y no ejecuta cobro coactivo. "
          "La propuesta no garantiza un monto de ahorro ni de recaudo.")
a.tabla("Resumen del servicio propuesto",
        ["Aspecto", "Contenido", "Estado"],
        [["Modalidad", "Servicio (no licencia aislada): plataforma propia configurada, integrada, operada y mantenida por Campuslands", "PROPUESTO"],
         ["Vigencia", "Operación del 1 de enero al 31 de diciembre de 2027; alistamiento en noviembre y diciembre de 2026, sin fee mensual", "PROPUESTO"],
         ["Fases", "Fase 1 Control de la data · Fase 2 Gestión automática multicanal con IA · Fase 3 Escalamiento a funcionarios y validación", "PROPUESTO"],
         ["Fuentes de fiscalización", "MAT-SIM, SICOG II, Cámara de Comercio (dos APIs externas) y base de contratos; vigencias 2021 a 2026", "PROPUESTO"],
         ["Fee mensual", "$50.000.000 COP, impuestos incluidos, de enero a diciembre de 2027", "PROPUESTO"],
         ["Opción facultativa de compra", "$540.000.000 COP, impuestos incluidos, en diciembre de 2027 (marca blanca)", "PROPUESTO"],
         ],
        [1.8, 5.0, 1.2],
        nota="Fuente: " + FUENTE + ", secciones 1, 3 y 9 y anexo técnico.")
a.h2("1.1 Base del documento y estados de la información")
a.parrafo("Este alcance se redacta únicamente con la propuesta comercial y técnica del 28 de octubre de 2026, una oferta sin firma de la Alcaldía; "
          "no se aportaron las actas de la mesa técnica, la cotización ni el requerimiento de la Alcaldía. Quedan 12 pendientes críticos (sección 15) "
          "que deben resolverse antes de la firma.")
a.parrafo("Estados de la información: CONFIRMADO (respaldado por una fuente citada o una aprobación expresa de la Alcaldía; aún no hay información en este estado), "
          "PROPUESTO (contenido de la oferta de Campuslands, aún sin aceptación) y PENDIENTE (dato que la propuesta no declara, marcado como " + P + ").")

# ------------------------------------------------------------------ 2. Contexto y objetivos
a.h1("2. Contexto y objetivos")
a.h2("2.1 Contexto")
a.parrafo("La Alcaldía Municipal de Girón gestiona la cartera de Industria y Comercio (ICA) a través de su Dirección de Industria y Comercio. "
          "La propuesta indica que los datos para identificar a los contribuyentes residen en MAT-SIM (declaraciones de ICA), SICOG II "
          "(exógena municipal), la base de contratos de la Alcaldía y la información de Cámara de Comercio. El recaudo lo gestiona el operador "
          "oficial del municipio, que emite los cobros y es la fuente de verdad de los pagos.")
a.parrafo("El proceso actual de cobro y fiscalización y su volumen no se describen en la propuesta: se documentarán en el levantamiento "
          "de la Fase 1 (RF-001). Línea base: " + P + ".")
a.h2("2.2 Problema y valor esperado")
a.parrafo("La propuesta sustenta el valor en cinco efectos: centralización de la cartera, mayor cobertura de contacto, trazabilidad, "
          "priorización de casos y menos trabajo manual. Afirma que automatizar las conversaciones reduce la necesidad de un call center "
          "presencial dedicado y deja al personal en actuaciones que requieren criterio humano. El ahorro depende de la organización actual y de la adopción del servicio.")
a.h2("2.3 Objetivos")
a.tabla("Objetivos del servicio y su medición",
        ["Objetivo", "Medida o indicador", "Estado"],
        [["Consultar la cartera en tiempo real por zona, vigencia, estado y monto, desde computador o celular", "Consulta disponible al cierre de la Fase 1. Meta: " + P, "PROPUESTO"],
         ["Identificar posibles omisos de ICA cruzando las fuentes institucionales", "Listado con columna EMPLAZAR. Precisión del cruce: " + P, "PROPUESTO"],
         ["Contactar a los contribuyentes en cascada (WhatsApp, correo, llamada) y registrar cada resultado", "Cada intento queda registrado y clasificado. Cantidades: " + P, "PROPUESTO"],
         ["Entregar a los funcionarios cada caso procesado con una acción recomendada", "Bandeja por acción recomendada. Tiempos: " + P, "PROPUESTO"],
         ["Actualizar el estado de cartera con el recaudo del operador oficial", "Importación periódica de recaudo. Periodicidad: " + P, "PROPUESTO"]],
        [3.6, 3.6, 0.8],
        nota="La propuesta no establece metas de recaudo ni de ahorro, y declara expresamente que no las garantiza.")

# ------------------------------------------------------------------ 3. Alcance y límites
a.h1("3. Alcance y límites")
a.h2("3.1 Dentro del alcance")
a.parrafo("El alcance propuesto se organiza en tres fases. Cada módulo se detalla en una ficha funcional de la sección 5.")
a.tabla("Módulos dentro del alcance por fase",
        ["Fase", "Módulos", "Identificadores"],
        [["1. Control de la data", "Levantamiento y parametrización · Arquitectura de despliegue e integración · Fiscalización · Núcleo de gestión de cartera y cobro · Dashboard de cartera · Mapa de contribuyentes por zona", "RF-001 a RF-006"],
         ["2. Gestión automática multicanal con IA", "Motor de campañas · Agente de voz · Agente de WhatsApp · Canal de correo · Dashboard de gestión", "RF-007 a RF-011"],
         ["3. Escalamiento a funcionarios y validación", "Gestión de casos escalados · Gestión de visitas · Verificación de pagos (versión básica) · Validación en operación real", "RF-012 a RF-015"],
         ["Transversal", "Seguridad, privacidad y auditoría · Gobierno de IA · Pruebas y validación · Alistamiento y despliegue · Capacitación y puesta en producción · Operación del servicio", "Secciones 7, 8, 11, 12 y 13"]],
        [2.3, 4.7, 1.0],
        nota="Estado: PROPUESTO. Fuente: " + FUENTE + ", anexo técnico, fases 1 a 3 y componentes transversales.")
a.h2("3.2 Fuera del alcance")
a.parrafo("La propuesta lista exclusiones en dos lugares que no coinciden del todo (sección 11 y anexo técnico). Se muestran ambas; cuál prevalece es " + P + ".")
a.tabla("Exclusiones declaradas",
        ["Exclusión", "Sección 11 de la propuesta", "Anexo técnico", "Estado"],
        [["Actos tributarios oficiales", "Sí", "No se lista", "PENDIENTE"],
         ["Emisión de cobros oficiales e impresión de recibos (la emite el operador oficial)", "Sí", "Sí", "PROPUESTO"],
         ["Cobro coactivo (mandamiento de pago, embargos, remate)", "Sí", "Ampliación de Fase 4", "PROPUESTO"],
         ["Visor de trámites inmobiliarios y de construcción (curadurías, notarías, Instrumentos Públicos)", "Sí", "Sí", "PROPUESTO"],
         ["Gestión de dineros embargados en cuentas bancarias (decisión administrativa)", "Sí", "Sí", "PROPUESTO"],
         ["Ampliaciones a otras secretarías", "Requieren levantamiento, aprobación y contratación independientes", "—", "PROPUESTO"]],
        [3.6, 1.7, 1.5, 1.2])
a.h2("3.3 Fases futuras")
a.parrafo("Los siguientes módulos no forman parte del servicio inicial. Pueden contratarse como ampliación una vez evaluados los resultados del servicio, "
          "con definición funcional, análisis de impacto, cotización y aprobación formal independientes. **No son entregables actuales.**".replace("**", ""))
a.tabla("Ampliación del servicio (Fase 4)",
        ["Módulo", "Qué incluiría (según la propuesta)", "Estado"],
        [["Acuerdos de pago", "Registro de compromisos, documento de acuerdo con plantilla oficial por cédula o placa, cronogramas, recordatorios, seguimiento de cumplimiento y reincorporación al flujo de cobranza", "PROPUESTO"],
         ["Conciliación automática de pagos", "Integración directa con el recaudo, conciliación, pagos parciales, cierre de obligaciones cumplidas y reactivación del cobro", "PROPUESTO"],
         ["Asistente por voz para funcionarios", "Consultas al asistente mediante voz", "PROPUESTO"],
         ["Cobro coactivo", "Paso de persuasivo a coactivo, actos administrativos, embargos, seguimiento hasta remate e integración con el sistema actual de coactivo", "PROPUESTO"],
         ["Fiscalización con información de la DIAN", "Cruce de exógena y renta con la cartera, mediante convenio o solicitud formal de intercambio", "PROPUESTO"],
         ["ReteICA y Autorretención", "Módulos propios con su ventana, carga de cartera y consulta desde el asistente", "PROPUESTO"]],
        [2.1, 4.9, 1.0])
a.h2("3.4 Mapa de procesos")
a.tabla("Flujo del servicio de extremo a extremo",
        ["Paso", "Qué ocurre", "Módulo", "Fase"],
        [["1. Fiscalización", "El servicio cruza MAT-SIM, SICOG II, Cámara de Comercio y la base de contratos e identifica a los contribuyentes por gestionar", "RF-003", "1"],
         ["2. Cartera", "Los contribuyentes identificados quedan clasificados y ubicados por zona, en el dashboard y en el mapa", "RF-004 a RF-006", "1"],
         ["3. Revisión", "Un funcionario revisa la clasificación antes de iniciar el contacto", "RF-003", "1"],
         ["4. Contacto en cascada", "WhatsApp, luego correo y, si no se logra contacto, llamada del agente de voz", "RF-007 a RF-010", "2"],
         ["5. Escalamiento", "Los casos que necesitan una persona pasan a la bandeja de funcionarios con la acción recomendada", "RF-012", "3"],
         ["6. Visita", "Si el caso lo requiere, se asigna una visita y su resultado se registra en un formulario digital", "RF-013", "3"],
         ["7. Pago", "El contribuyente paga por el link oficial y el servicio actualiza su estado con el recaudo del operador oficial", "RF-014", "3"]],
        [1.6, 4.6, 1.2, 0.6],
        nota="Dependencia entre fases por resolver: la propuesta ubica el contacto en cascada a los contribuyentes «por emplazar» en la Fase 1, "
             "pero indica que usa el motor de campañas y los canales de la Fase 2. Además, el recaudo se importa en la Fase 3, "
             "después de las campañas de la Fase 2. Ambos puntos: " + P + ".")

# ------------------------------------------------------------------ 4. Usuarios y permisos
a.h1("4. Usuarios y permisos")
a.parrafo("La propuesta no incluye una matriz de usuarios ni de permisos. Esta sección recoge los actores que la propuesta menciona y lo que cada uno hace; "
          "los permisos concretos quedan " + P + ".")
a.tabla("Actores y su participación",
        ["Actor", "Qué hace según la propuesta", "Módulos", "Permisos"],
        [["Alcalde y funcionarios", "Consultan en tiempo real la cartera por zona, vigencia, estado y monto, desde computador o celular", "RF-005, RF-006", P],
         ["Funcionarios de la Dirección de Industria y Comercio", "Revisan la clasificación EMPLAZAR antes del contacto; atienden la bandeja de casos escalados; registran la gestión humana; hacen el seguimiento financiero, administrativo y funcional del servicio", "RF-003, RF-004, RF-011, RF-012", P],
         ["Funcionarios que realizan visitas", "Reciben la asignación por zona y registran el resultado en el formulario digital desde el celular", "RF-013", P],
         ["Dirección de TIC", "Entrega máquinas virtuales, dominio, VPN, canal de 50 Mbps y accesos; hace el seguimiento técnico; recibe el manual de operación del servidor", "RF-002", P],
         ["Área jurídica de la Alcaldía", "Aprueba guiones, plantillas, reglas de campaña, textos legales, horarios y frecuencia de contacto", "RF-007 a RF-009", P],
         ["Equipo de Campuslands", "Configura, integra, opera y da soporte; accede por VPN con usuarios nominales", "RF-002, sección 13", "Usuarios nominales por VPN. Alcance de acceso a los datos: " + P],
         ["Contribuyentes", "Reciben WhatsApp, correo y llamadas del asistente virtual de la Alcaldía y pagan por el link oficial", "RF-008 a RF-010", "Sin cuenta en la plataforma, según la propuesta"]],
        [1.6, 3.6, 1.2, 1.6],
        nota="Estado: PROPUESTO. La propuesta solo declara autenticación, autorización basada en roles, gestión de usuarios funcionarios y logs de auditoría. "
             "Perfiles, número de usuarios y visibilidad por perfil: " + P + ".")

# ------------------------------------------------------------------ 5. Requerimientos funcionales
a.h1("5. Requerimientos funcionales")
a.parrafo("Cada módulo se describe en una ficha uniforme. Los criterios de aceptación medibles se definen en el levantamiento de la Fase 1 (RF-001); "
          "mientras tanto, cada ficha indica lo que la propuesta declara como resultado verificable. "
          "Los identificadores RF-001 a RF-015 corresponden a los módulos MOD-01 a MOD-15 y no se renumeran entre versiones.")


def ficha(n, mod, fase, nombre, objetivo, pre, flujo, reglas, salidas, dep, crit, sec):
    a.ficha_funcional(f"RF-{n:03d}", nombre, [
        ("Módulo y fase", f"MOD-{n:02d} · Fase {fase}"),
        ("Objetivo y usuario", objetivo),
        ("Precondiciones y entradas", pre),
        ("Flujo principal", flujo),
        ("Reglas y excepciones", reglas),
        ("Salidas", salidas),
        ("Dependencias", dep),
        ("Criterios de aceptación", crit),
        ("Estado", f(sec)),
    ])


a.h2("5.1 Fase 1 — Control de la data")
ficha(1, "MOD-01", 1, "Levantamiento y parametrización del servicio",
      "Documentar cómo se cobra hoy el ICA y fijar reglas de negocio, indicadores y criterios de aceptación. Usuarios: Dirección de Industria y Comercio, Dirección de TIC y equipo de Campuslands.",
      "Procedimientos escritos y aprobados de cobro y fiscalización; sesiones con funcionarios que conocen la operación; histórico de obligaciones 2021–2026.",
      "1. Campuslands revisa los procedimientos y sesiona con los funcionarios. 2. Analiza el histórico de obligaciones 2021–2026. 3. Documenta actores, roles, fuentes, ciclo de vida del cobro persuasivo, reglas de clasificación de deudores, de compromisos de pago, de contacto y de escalamiento. 4. Define indicadores de gestión y recaudo y criterios de aceptación. Aprobación del documento por la Alcaldía: " + P,
      "Las reglas de negocio no están definidas en la propuesta; se definen en este módulo. Reglas de clasificación, semáforo y priorización: " + P,
      "Documento de parametrización del servicio, con reglas de negocio y criterios de aceptación.",
      "Procedimientos escritos y sesiones con funcionarios (insumo de la Alcaldía).",
      "Entrega del documento de parametrización y acta de la Fase 1. Los criterios medibles de cada módulo se definen en este levantamiento.",
      "anexo técnico · Fase 1 · Levantamiento y parametrización")
ficha(2, "MOD-02", 1, "Arquitectura de despliegue e integración",
      "Definir cómo se despliega la plataforma en la infraestructura de la Alcaldía y cómo se integra con sus fuentes y con los servicios en la nube. Usuarios: Dirección de TIC y equipo de Campuslands.",
      "Máquinas virtuales, dominio, certificado SSL, VPN y canal dedicado de 50 Mbps de la Alcaldía; diccionarios de datos de las fuentes.",
      "1. Campuslands entrega el documento de arquitectura de despliegue y la especificación de servidores, puertos y dominios para TIC, antes de que se creen las máquinas virtuales. 2. Despliega la plataforma en la infraestructura de la Alcaldía. 3. Configura las comunicaciones omnicanal y dimensiona las llamadas simultáneas. 4. Mapea los datos de la Alcaldía al modelo de la plataforma y a las integraciones externas, incluido el link de pago. 5. Configura seguridad, autenticación, autorización, trazabilidad y auditoría. 6. Habilita los ambientes de pruebas y producción.",
      "Los servidores de referencia (aplicación 8 vCPU / 16 GB / 100 GB; base de datos 4–8 vCPU / 16–32 GB / 200 GB; pruebas 4 vCPU / 8–16 GB / 100 GB) se ajustan con el volumen real de cartera, que la propuesta no declara: " + P,
      "Documento de arquitectura de despliegue; ambientes de pruebas y producción.",
      "Insumos de infraestructura de la Alcaldía (sección 11). Integraciones de la sección 6.",
      "Documento entregado a TIC antes de crear las máquinas virtuales; ambientes habilitados. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 1 · Arquitectura de despliegue e integración; Infraestructura y responsabilidades")
ficha(3, "MOD-03", 1, "Fiscalización: cruce de fuentes y listado de posibles omisos",
      "Identificar contribuyentes que deben gestionarse, incluidos posibles omisos de ICA. Usuarios: funcionarios de la Dirección de Industria y Comercio.",
      "Acceso a MAT-SIM (declaraciones de ICA), SICOG II (exógena municipal), base de contratos y dos APIs externas de Cámara de Comercio; diccionarios de datos; definición de los campos requeridos de Cámara de Comercio.",
      "1. El servicio cruza las fuentes por número de documento normalizado (NIT con o sin dígito de verificación). 2. Identifica posibles omisos de ICA. 3. Genera un listado en Excel con los campos del requerimiento de la Alcaldía y la columna EMPLAZAR (por emplazar, no clasificado para emplazamiento o pendiente de validación). 4. Un funcionario revisa la clasificación antes del contacto. 5. Los contribuyentes identificados forman la cartera del servicio.",
      "Cubre las vigencias 2021 a 2026, sin limitar el número de contribuyentes. De Cámara de Comercio se consultan municipio de registro y fecha de última renovación; la dirección exacta no es un dato garantizado. Las fuentes externas dependen de acceso o licenciamiento. El acto de emplazamiento y su notificación formal siguen el procedimiento tributario y no los ejecuta la plataforma. Campos del listado y criterios de clasificación EMPLAZAR: " + P,
      "Listado Excel de posibles omisos; cartera depurada y cargada, con informe de calidad de datos.",
      "INT-01 a INT-05; mensajes y guiones aprobados por la jurídica de la Alcaldía.",
      "Cartera generada, depurada y cargada con informe de calidad de datos. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 1 · Fiscalización")
ficha(4, "MOD-04", 1, "Núcleo de gestión de cartera y cobro",
      "Centralizar en un expediente la información del contribuyente, sus obligaciones y la gestión de cobro. Usuarios: funcionarios de la Dirección de Industria y Comercio.",
      "Cartera generada por la fiscalización; histórico de deuda y pagos.",
      "1. La plataforma mantiene módulos de contribuyentes y negocios, obligaciones, histórico de deuda y pagos, y gestión por placa. 2. Clasifica por zonas, estados del proceso de cobro y semáforo de gestión. 3. Registra el historial de actuaciones, la asignación y la gestión de casos. 4. Aplica reglas de priorización de cartera, empezando por las deudas de mayor monto.",
      "Definición de estados y de semáforo: " + P + ". La propuesta no explica qué es la «placa» para obligaciones de ICA: identificador de la obligación " + P,
      "Expediente de cobro con trazabilidad integral; cartera clasificada por zona, estado y semáforo.",
      "RF-001 (reglas); RF-003 (cartera).",
      "Funcionalidad habilitada al cierre de la Fase 1 con acta. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 1 · Núcleo de gestión de cartera y cobro")
ficha(5, "MOD-05", 1, "Dashboard de cartera",
      "Consultar la cartera y sus indicadores en tiempo real. Usuarios: alcalde y funcionarios.",
      "Cartera cargada en la plataforma.",
      "1. El usuario abre el dashboard desde computador o celular. 2. Consulta la vista general o filtra por zona, vigencia, estado y semáforo de gestión. 3. Revisa los indicadores de recuperación de cartera. 4. Genera y exporta reportes.",
      "Los indicadores concretos se definen en el levantamiento (RF-001): " + P,
      "Vistas, filtros, búsquedas y reportes exportables; interfaz adaptable a celular.",
      "RF-004.",
      "Consulta disponible por zona, vigencia, estado y monto desde computador y celular. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 1 · Dashboard de cartera")
ficha(6, "MOD-06", 1, "Mapa de contribuyentes por zona",
      "Ver a los contribuyentes sobre las zonas del municipio con su semáforo de gestión. Usuarios: alcalde y funcionarios.",
      "Capa geográfica de zonas (shapefile o GeoJSON) de la Alcaldía; direcciones de los contribuyentes; servicio de geocodificación.",
      "1. La plataforma normaliza y georreferencia las direcciones. 2. Muestra cada contribuyente en el mapa con el color de su semáforo. 3. El usuario filtra por zona, vigencia, estado, monto y semáforo y ve el conteo de contribuyentes y de cartera por zona. 4. Al seleccionar un marcador, abre la ficha con obligaciones, historial de gestión y estado del contacto.",
      "La ubicación puede empezar aproximada y mejorarse con coordenadas capturadas por funcionarios en visitas; la calidad depende de los datos de la Alcaldía. Los registros sin dirección identificable quedan en la zona adicional y fuera del mapa hasta que se corrijan. Mapa con Leaflet sobre las capas de la Alcaldía o el mapa base de OpenStreetMap. Porcentaje mínimo de ubicación aceptable: " + P,
      "Mapa por zonas con filtros y ficha del contribuyente; vista adaptable a celular.",
      "Capa de zonas (insumo de la Alcaldía); servicio de geocodificación: " + P,
      "Mapa habilitado con los filtros y la ficha descritos. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 1 · Mapa de contribuyentes por zona; §9.6")

a.h2("5.2 Fase 2 — Gestión automática multicanal con IA")
ficha(7, "MOD-07", 2, "Motor de campañas y gestión automática de cobro",
      "Ejecutar campañas de contacto sobre la cartera y sobre los contribuyentes marcados como por emplazar. Usuarios: funcionarios de la Dirección de Industria y Comercio.",
      "Cartera y segmentos parametrizados; plantillas y guiones aprobados por la jurídica de la Alcaldía; canales de WhatsApp, correo y voz configurados.",
      "1. La campaña selecciona un segmento según los criterios parametrizados. 2. Envía un WhatsApp con plantilla aprobada por Meta; si el contribuyente responde, atiende el agente de WhatsApp. 3. Si no responde en la ventana definida, envía un correo con el link de pago oficial. 4. Si sigue sin responder, lo llama el agente de voz. 5. Cada intento queda registrado y clasificado; los casos que requieren una persona escalan a un funcionario.",
      "Las colas y workers respetan la concurrencia, los horarios y la frecuencia permitidos; los horarios los valida la jurídica de la Alcaldía conforme a la Ley 2300 de 2023. Incluye programación de campañas masivas, reglas de reintento, de exclusión y control de frecuencia. Ventana de espera entre canales, frecuencia y concurrencia: " + P,
      "Campañas ejecutadas; resultado de cada intento; casos escalados.",
      "RF-003, RF-008, RF-009, RF-010; concepto jurídico sobre horarios y frecuencia.",
      "Servicio habilitado con motor de campañas al cierre de la Fase 2. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 2 · Motor de campañas")
ficha(8, "MOD-08", 2, "Agente de IA para llamadas de voz",
      "Contactar por teléfono a los contribuyentes en tono amable y persuasivo, dentro de los guiones aprobados. Usuarios: contribuyentes; supervisan los funcionarios.",
      "Guiones y objetivos aprobados por la Alcaldía; datos del contribuyente y su deuda; Retell AI y operador de telefonía con números colombianos.",
      "1. El agente llama y se identifica como asistente virtual de la Alcaldía. 2. Identifica al contribuyente y consulta a la plataforma los datos de su deuda. 3. Gestiona la intención de pago y las objeciones con respuestas permitidas. 4. Captura compromisos de pago. 5. La llamada se transcribe, se resume y se clasifica. 6. Los casos que lo requieren pasan a un funcionario.",
      "Solo actúa dentro de controles y límites de actuación definidos con la Alcaldía; qué puede decir y ofrecer: " + P + ". No toma decisiones tributarias. El audio no pasa por la red de la Alcaldía. Aviso de grabación y retención: " + P,
      "Llamadas, transcripciones, resúmenes y clasificación del resultado.",
      "INT-09 y INT-10; RF-007; gobierno de IA (sección 7).",
      "Servicio habilitado al cierre de la Fase 2 con pruebas conversacionales y de llamadas masivas. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 2 · Agente de IA para llamadas de voz")
ficha(9, "MOD-09", 2, "Agente de IA para WhatsApp",
      "Atender por WhatsApp a los contribuyentes y llevarlos al link de pago oficial. Usuarios: contribuyentes; supervisan los funcionarios.",
      "Cuenta de Meta Business y número a nombre de la Alcaldía, verificados; plantillas aprobadas por Meta.",
      "1. Meta entrega la respuesta del contribuyente por webhook. 2. El agente identifica al contribuyente y consulta sus obligaciones. 3. Presenta las alternativas de pago autorizadas y lo redirige al link de pago oficial. 4. Registra intención y compromiso de pago y envía recordatorios. 5. Las conversaciones no resueltas se registran y se escalan.",
      "Opera a cualquier hora, sin funcionario detrás; no emite recibos. Alternativas de pago autorizadas: " + P,
      "Conversaciones registradas con trazabilidad completa.",
      "INT-08; verificación del número ante Meta; RF-007.",
      "Servicio habilitado al cierre de la Fase 2. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 2 · Agente de IA para WhatsApp")
ficha(10, "MOD-10", 2, "Canal de correo electrónico",
      "Enviar correos de cobro persuasivo con el link de pago oficial. Usuarios: contribuyentes.",
      "Dirección remitente institucional y registros SPF, DKIM y DMARC en el dominio de la Alcaldía; proveedor de envío.",
      "1. Una campaña programa el envío masivo. 2. La plataforma usa la plantilla de cobro persuasivo con el link de pago oficial. 3. Envía el correo desde el proveedor de Campuslands con el remitente institucional.",
      "Se envía un correo por cada contribuyente que no responde por WhatsApp, en cada ciclo. Proveedor de correo: " + P,
      "Correos enviados y registrados en la campaña.",
      "INT-11; RF-007.",
      "Envío masivo programado desde las campañas, con plantillas y link de pago, al cierre de la Fase 2.",
      "anexo técnico · Fase 2 · Canal de correo electrónico")
ficha(11, "MOD-11", 2, "Dashboard de gestión y asistente de consulta",
      "Seguir la ejecución de las campañas y consultar la gestión en lenguaje natural. Usuarios: funcionarios de la Dirección de Industria y Comercio.",
      "Campañas e intentos registrados.",
      "1. El funcionario abre el dashboard. 2. Consulta campañas, llamadas, conversaciones de WhatsApp y envíos de correo. 3. Revisa los indicadores de efectividad por canal. 4. Consulta campañas, llamadas y conversaciones desde el asistente.",
      "El asistente de consulta también aparece en la propuesta como capacidad de IA para preguntas sobre cartera, contribuyentes e indicadores; no tiene módulo ni fase propios: " + P,
      "Tableros de seguimiento e indicadores por canal.",
      "RF-007 a RF-010.",
      "Seguimiento disponible al cierre de la Fase 2. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 2 · Dashboard de gestión; Inteligencia artificial en el servicio")

a.h2("5.3 Fase 3 — Escalamiento a funcionarios y validación")
ficha(12, "MOD-12", 3, "Gestión de casos escalados",
      "Entregar al equipo de la Alcaldía cada caso procesado con la acción recomendada. Usuarios: funcionarios de la Dirección de Industria y Comercio.",
      "Casos escalados por los agentes o por las reglas de campaña.",
      "1. El funcionario abre la bandeja de casos por acción recomendada: visita, solicitud de acuerdo, verificación de pago o negativa. 2. Visualiza y gestiona el caso. 3. La plataforma transfiere la conversación o la llamada a un funcionario. 4. La gestión humana queda en el historial del expediente.",
      "El servicio registra intención y compromiso de pago. El módulo de acuerdos de pago es Fase 4 y no está incluido. La acción «enviar recibo» convive con la exclusión de emisión de recibos (los emite el operador oficial): alcance exacto " + P,
      "Bandeja de casos; historial del expediente actualizado.",
      "RF-007 a RF-009.",
      "Servicio habilitado con bandeja de casos al cierre de la Fase 3. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 3 · Gestión de casos escalados; Ampliación de Fase 4")
ficha(13, "MOD-13", 3, "Gestión de visitas",
      "Asignar visitas y registrar su resultado. Usuarios: funcionarios que realizan visitas.",
      "Formato de registro de visita que entregará la Alcaldía; asignación por funcionario y zona; mapa.",
      "1. El sistema asigna la visita por funcionario y zona, con la lista de contribuyentes y su ubicación en el mapa. 2. El funcionario diligencia desde el celular el formulario digital con fecha, hora, funcionario y adjuntos como fotos o documentos. 3. La plataforma actualiza el estado del caso y el semáforo y lo registra en el historial. 4. Define el siguiente paso: cierre, nueva campaña de contacto, nueva visita o escalamiento.",
      "Los campos del formulario salen del formato de registro de visita de la Alcaldía: " + P,
      "Formulario de resultado; seguimiento de visitas pendientes, realizadas y no efectivas, por funcionario y zona.",
      "Formato de registro de visita (insumo de la Alcaldía); RF-006, RF-012.",
      "Servicio habilitado al cierre de la Fase 3. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 3 · Gestión de visitas")
ficha(14, "MOD-14", 3, "Verificación de pagos (versión básica)",
      "Actualizar el estado de la cartera con el recaudo oficial. Usuarios: funcionarios de la Dirección de Industria y Comercio.",
      "Información de recaudo del operador oficial, que es la fuente de verdad de los pagos.",
      "1. La plataforma importa periódicamente la información de recaudo. 2. Asocia los pagos con placa y obligación. 3. Actualiza el estado de la cartera. 4. Genera novedades para revisión manual.",
      "La plataforma no registra pagos por su cuenta. La conciliación automática es Fase 4. Periodicidad, formato y operador oficial: " + P,
      "Estado de cartera actualizado; novedades para revisión manual.",
      "INT-13.",
      "Verificación básica habilitada al cierre de la Fase 3. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 3 · Verificación de pagos (versión básica)")
ficha(15, "MOD-15", 3, "Validación en operación real",
      "Confirmar el servicio con la cartera real antes de la operación general. Usuarios: funcionarios de la Alcaldía.",
      "Servicio habilitado hasta la Fase 3; cartera real cargada.",
      "1. Los funcionarios validan el servicio con la cartera real. 2. Se cierran las pruebas de recuperación ante fallos y de carga completa. 3. Campuslands emite el informe de validación.",
      "Las pruebas se cierran antes de la operación general.",
      "Informe de validación en operación real.",
      "RF-001 a RF-014.",
      "Informe de validación entregado. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).",
      "anexo técnico · Fase 3 · Validación en operación real")

# ------------------------------------------------------------------ 6. Integraciones
a.h1("6. Fuentes de datos e integraciones")
a.parrafo("La propuesta no aporta documentación técnica ni pruebas de acceso de ninguna fuente. Las integraciones con fuentes externas dependen de "
          "la disponibilidad efectiva de datos y de accesos autorizados.")
a.h2("6.1 Matriz por sistema")
a.tabla("Integraciones del servicio",
        ["ID", "Sistema", "Propósito y mecanismo declarado", "Fase", "Estado"],
        [["INT-01 y INT-02", "Cámara de Comercio (dos APIs externas)", "Municipio de registro y fecha de última renovación; HTTPS; las respuestas se consolidan. La dirección exacta no está garantizada", "1", P + " proveedores, tarifa y acceso"],
         ["INT-03", "MAT-SIM", "Lectura de declaraciones de ICA; «API interna»", "1", P + " existencia y documentación de la API"],
         ["INT-04", "SICOG II", "Lectura de exógena municipal; «API interna»", "1", P + " ídem"],
         ["INT-05", "Base de contratos de la Alcaldía", "Lectura de contratistas del municipio; «API interna»", "1", P + " ídem"],
         ["INT-06", "Capa geográfica y geocodificación", "Capa de zonas (shapefile o GeoJSON) y servicio de geocodificación", "1", P + " servicio de geocodificación"],
         ["INT-07", "Modelo de lenguaje", "Agentes y asistente; API por HTTPS", "1 y 2", P + " proveedor «por definir»"],
         ["INT-08", "WhatsApp Business (Meta)", "Canal WhatsApp; API saliente y webhooks entrantes", "2", "PROPUESTO. Estado de la cuenta: " + P],
         ["INT-09", "Retell AI", "Agente de voz; API saliente y webhooks de consulta y resultado", "2", "PROPUESTO"],
         ["INT-10", "Twilio o Telnyx", "Llamadas a números colombianos; SIP", "2", P + " elección entre ambos"],
         ["INT-11", "Proveedor de correo", "Envío con dominio institucional (SPF, DKIM, DMARC); API o SMTP", "2", P + " proveedor"],
         ["INT-12", "Operador oficial — link de pago", "Enlace en los mensajes de WhatsApp y correo", "2", P + " operador"],
         ["INT-13", "Operador oficial — recaudo", "Importación periódica; fuente de verdad de los pagos", "3", P + " periodicidad y formato"],
         ["INT-14", "DIAN", "Exógena y renta; convenio o solicitud formal", "Fase 4", "Fuera del alcance actual"]],
        [1.0, 1.7, 3.3, 0.6, 1.4],
        nota="Fuente: " + FUENTE + ", anexo técnico, Integraciones y fuentes de datos.")
a.h2("6.2 Servicios de terceros y quién los asume")
a.tabla("Terceros, costos y titularidad según la propuesta",
        ["Servicio", "Costo y titularidad declarados", "Con la opción de compra"],
        [["Retell AI (voz)", "Consumo incluido en el fee", "Sigue con su proveedor, bajo sus condiciones"],
         ["Twilio o Telnyx (telefonía)", "Campuslands contrata y paga; los números quedan a nombre de la Alcaldía", "Sigue con su proveedor"],
         ["WhatsApp Business (Meta)", "Campuslands paga el consumo; la cuenta queda a nombre de la Alcaldía", "El servicio sigue con Meta"],
         ["Correo", "Campuslands envía desde su proveedor y paga el consumo; el remitente lo define la Alcaldía", "Sigue con su proveedor"],
         ["Modelo de lenguaje", "Consumo incluido en el fee", "Sigue con su proveedor"],
         ["Dos APIs de Cámara de Comercio", "La propuesta no dice quién paga el consumo o la licencia. La Alcaldía habilita credenciales: " + P, P],
         ["Geocodificación", "No asignado en la propuesta: " + P, P],
         ["Servidores, almacenamiento, virtualización, canal de 50 Mbps, VPN, dominio y certificado SSL", "A cargo de la Alcaldía", "—"]],
        [2.4, 3.8, 1.8],
        nota="Consumos por encima de la referencia: la propuesta dice que se aprueban antes con la Alcaldía y que no generan cobros automáticos; "
             "no declara un volumen de referencia ni quién asume el costo una vez aprobados: " + P + ".")
a.h2("6.3 Responsabilidades sobre datos y red")
a.tabla("Reparto de responsabilidades según la propuesta",
        ["Tema", "Alcaldía", "Campuslands"],
        [["Datos", "Acceso a las fuentes de fiscalización, diccionario de datos, acceso a recaudo y link de pago", "Cruce de fuentes, depuración, carga y controles de calidad"],
         ["Red y seguridad", "Dominio y certificado SSL, publicación HTTPS para webhooks, lista blanca de salida, VPN para el equipo de Campuslands, canal de 50 Mbps", "Lista de puertos y dominios a habilitar; hardening de la aplicación"],
         ["Correo", "Dirección remitente institucional y registros SPF, DKIM y DMARC", "Envío desde su proveedor, plantillas y pago del consumo"],
         ["Telefonía y WhatsApp", "Cuenta de Meta Business a nombre de la Alcaldía; números publicados en su web", "Contratación y pago de telefonía y consumo de WhatsApp, configuración, acompañamiento de la verificación de Meta y pruebas"],
         ["Respaldo y continuidad", "Ejecución de backups, réplica fuera del servidor principal, contingencia del data center (RTO/RPO)", "Definición de qué respaldar y prueba de restauración junto con TIC. También le asigna los respaldos de la base de datos como tarea programada: quién los ejecuta, " + P],
         ["Monitoreo", "Infraestructura (CPU, disco, disponibilidad)", "Aplicación, logs y alertas"],
         ["Gestión y jurídico", "Responsables por cargo, aprobación de guiones, reglas y textos legales, retención de grabaciones (TRD)", "Propuesta de guiones, reglas y textos para aprobación"]],
        [1.4, 3.3, 3.3])

# ------------------------------------------------------------------ 7. IA
a.h1("7. IA y automatización")
a.parrafo("La IA ejecuta contactos repetitivos y clasifica resultados; las decisiones tributarias siguen a cargo de la Alcaldía. "
          "La depuración, los cruces y la georreferenciación usan herramientas de datos convencionales. "
          "No se promete exactitud perfecta, entrenamiento de modelos ni recomendaciones infalibles.")
a.tabla("Tareas de IA, límites y supervisión",
        ["Componente", "Tarea", "Fuentes autorizadas", "Supervisión y trazabilidad"],
        [["Agente de voz (Retell AI)", "Llamar, identificarse como asistente virtual de la Alcaldía, responder objeciones dentro de los guiones, registrar intención o compromiso", "Datos del contribuyente y su deuda, consultados a la plataforma durante la llamada", "Guiones aprobados por la Alcaldía; transcripción, resumen y clasificación de cada llamada; escalamiento a funcionario; logs de auditoría"],
         ["Agente de WhatsApp", "Conversar en lenguaje natural, consultar obligaciones y llevar al link de pago oficial", "Obligaciones del contribuyente en la plataforma", "Registro completo de interacciones; casos no resueltos pasan a un funcionario"],
         ["Transcripción y resumen", "Transcribir cada llamada, resumirla y clasificar su resultado", "Audio de la llamada", "El funcionario lee el resumen en lugar de escuchar la grabación"],
         ["Acción recomendada", "Proponer el siguiente paso del caso: visita, recibo, solicitud de acuerdo, verificación de pago o negativa", "Datos del expediente", "El funcionario decide y ejecuta"],
         ["Asistente de consulta", "Responder preguntas sobre cartera, contribuyentes o indicadores", "Datos de la plataforma", P]],
        [1.5, 2.4, 1.8, 2.3],
        nota="Estado: PROPUESTO. Fuente: " + FUENTE + ", anexo técnico, Inteligencia artificial en el servicio. "
             "Medidas de calidad, tasa de clasificación correcta y lista de lo que cada agente nunca debe decir u ofrecer: " + P + ".")
a.h2("7.1 Gobierno de IA")
a.vinetas([
    "Definición de los límites de actuación de cada agente: qué puede decir y ofrecer, y cuándo pasa el caso a una persona (RF-008 y RF-009). Contenido: " + P,
    "Propuesta de política institucional de inteligencia artificial para la Alcaldía, con referencia al marco de la UNESCO (entregable transversal).",
    "El procesamiento de IA ocurre en la nube pública de los proveedores; no se instalan modelos ni GPU en los servidores de la Alcaldía.",
])

# ------------------------------------------------------------------ 8. No funcionales
a.h1("8. Requerimientos no funcionales")
a.tabla("Requerimientos no funcionales declarados y pendientes",
        ["Categoría", "Lo que declara la propuesta", "Estado"],
        [["Seguridad", "Autenticación, autorización basada en roles, gestión de usuarios funcionarios, cifrado en tránsito y de información sensible, gestión de secretos, controles de seguridad con pruebas básicas OWASP", "PROPUESTO"],
         ["Auditoría", "Logs de auditoría y trazabilidad de las acciones de funcionarios y de agentes de IA, como evidencia ante entes de control", "PROPUESTO"],
         ["Privacidad y datos personales", "Controles de privacidad y tratamiento conforme a la Ley 1581 de 2012; gestión segura de grabaciones y transcripciones. Roles de responsable y encargado, transferencia a proveedores en la nube y retención (TRD): " + P, "PROPUESTO"],
         ["Contacto al ciudadano", "Horarios y frecuencia conforme a la Ley 2300 de 2023, validados por la jurídica de la Alcaldía", "PROPUESTO"],
         ["Uso y compatibilidad", "Interfaz web adaptable a celular; ambientes de pruebas y producción", "PROPUESTO"],
         ["Rendimiento y concurrencia", "Pruebas de rendimiento, concurrencia y carga completa antes de la operación general. Cifras objetivo: " + P, "PENDIENTE"],
         ["Disponibilidad y continuidad", "Monitoreo de aplicación, logs y alertas; políticas de respaldo y recuperación. Disponibilidad, RTO y RPO: " + P, "PENDIENTE"],
         ["Conservación", "Políticas de conservación y rotación de registros. Periodos de retención de grabaciones: " + P, "PENDIENTE"],
         ["Capacidad", "Almacenamiento de grabaciones de unos 30 GB al mes, dimensionado con el volumen real", "PROPUESTO"]],
        [1.6, 5.4, 1.0])

# ------------------------------------------------------------------ 9. Arquitectura
a.h1("9. Arquitectura de alto nivel")
a.parrafo("La aplicación, la base de datos y los workers corren en los servidores de la Alcaldía. La voz, la telefonía, WhatsApp, el correo y el modelo "
          "de lenguaje son servicios en la nube. Los funcionarios entran por la red interna y la API lee las fuentes de fiscalización y el recaudo por la VPN existente. "
          "El motor de campañas llama a los servicios en la nube por HTTPS y estos devuelven respuestas y resultados por webhooks. La llamada sale de Retell por la telefonía, "
          "por lo que el audio no pasa por la red de la Alcaldía.")
p = a.doc.add_paragraph(style="Tabla Número")
p.add_run("Figura 1")
a.doc.add_paragraph("Arquitectura de alto nivel del servicio", style="Tabla Título")
png = TMP / "arquitectura.png"
subprocess.run([sys.executable, str(AQUI / "diagrama_arquitectura.py"), str(png)], check=True, capture_output=True)
a.doc.add_picture(str(png), width=Cm(15.2))
a.doc.paragraphs[-1].alignment = 1
n = a.doc.add_paragraph(style="Tabla Nota")
r = n.add_run("Nota. ")
r.italic = True
n.add_run("Diagrama elaborado con la descripción de la propuesta (PROPUESTO); la propuesta no incluía el diagrama. ")
a._texto(n, "Entrada pública HTTPS (puerto 443, dominio propio) para los webhooks de Meta y de la plataforma de voz, por un canal dedicado de 50 Mbps que contrata y paga la Alcaldía.")
a.h2("9.1 Pila tecnológica")
a.tabla("Tecnologías y dónde corren",
        ["Capa", "Tecnología", "Dónde corre"],
        [["Backend y API", "Node.js con TypeScript, TypeORM", "Servidor de aplicación (Alcaldía)"],
         ["Frontend web, adaptable a celular", "Vue.js", "Servidor de aplicación (Alcaldía)"],
         ["Base de datos", "MariaDB", "Servidor de base de datos (Alcaldía)"],
         ["Colas, tareas programadas y workers", "Redis", "Servidor de aplicación (Alcaldía)"],
         ["Sistema operativo", "Ubuntu Server 24.04 LTS", "Servidores de la Alcaldía"],
         ["Proxy inverso y certificados", "Proxy HTTPS con certificado SSL del dominio de la Alcaldía", "Servidor de aplicación (Alcaldía)"],
         ["Mapas", "Leaflet sobre capas de la Alcaldía u OpenStreetMap", "Aplicación"],
         ["Agente de voz", "Retell AI", "Nube de Retell AI"],
         ["Telefonía", "Twilio o Telnyx con números colombianos", "Nube del operador"],
         ["WhatsApp", "API de WhatsApp Business (Meta)", "Nube de Meta"],
         ["Correo", "Proveedor de envío con dominio institucional", "Nube del proveedor"],
         ["Modelo de lenguaje", "Proveedor " + P, "Nube del proveedor"]],
        [2.6, 3.4, 2.0])

# ------------------------------------------------------------------ 10. Entregables y aceptación
a.h1("10. Entregables y aceptación")
a.parrafo("Cada fase se habilita tras pruebas de funcionarios de la Alcaldía contra los criterios del levantamiento, y se registra en un acta. "
          "Esos criterios se definen en el levantamiento de la Fase 1, por lo que la columna de aceptación indica lo verificable que declara la propuesta.")
a.tabla("Entregables por fase y aceptación",
        ["Entregable", "Fase", "Aceptación", "Estado"],
        [["Documento de parametrización: procesos, reglas de negocio, indicadores y criterios de aceptación", "1", "Documento y acta de fase. Aprobación: " + P, "PROPUESTO"],
         ["Documento de arquitectura de despliegue y especificación de servidores, puertos y dominios para TIC", "1", "Entregado antes de crear las máquinas virtuales", "PROPUESTO"],
         ["Cartera generada por la fiscalización, depurada y cargada, con informe de calidad de datos", "1", "Informe de calidad de datos", "PROPUESTO"],
         ["Servicio habilitado con gestión de cartera, dashboard, mapa por zonas y fiscalización", "1", "Prueba por funcionarios y acta. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).", "PROPUESTO"],
         ["Servicio habilitado con motor de campañas, agentes de WhatsApp y de voz, canal de correo y dashboard de gestión", "2", "Pruebas conversacionales, de llamadas masivas, WhatsApp, correo y cascada; acta", "PROPUESTO"],
         ["Servicio habilitado con bandeja de casos escalados, gestión de visitas y verificación de pagos básica", "3", "Prueba por funcionarios y acta. Los criterios medibles se definen en el levantamiento de la Fase 1 (RF-001).", "PROPUESTO"],
         ["Informe de validación en operación real", "3", "Informe entregado", "PROPUESTO"],
         ["Propuesta de política institucional de IA", "Transversal", "Propuesta entregada", "PROPUESTO"],
         ["Manuales de operación y de usuario, capacitación, acta de inicio, SBOM y plan de salida con exportación de datos", "Cierre", "Entregados. Cantidad de sesiones: " + P, "PROPUESTO"],
         ["Código fuente y documentación, con derechos de uso, explotación y adaptación en marca blanca", "Opción de compra", "Solo si se ejerce (diciembre de 2027)", "PROPUESTO"]],
        [3.6, 1.3, 2.7, 1.45],
        nota="Fuente: anexo técnico, Entregables del servicio. La propuesta no declara si la aceptación condiciona el pago mensual: " + P + ".")

# ------------------------------------------------------------------ 11. Metodología y cronograma
a.h1("11. Metodología y cronograma")
a.parrafo("La propuesta no describe una metodología de trabajo (por ejemplo, forma de iteración o de seguimiento de avances) más allá de la habilitación por fases, "
          "las pruebas con funcionarios y las actas por fase: " + P + ". El cronograma definitivo lo aprueba la mesa técnica, jurídica y financiera.")
a.tabla("Calendario propuesto",
        ["Periodo", "Qué ocurre", "Evidencia", "Estado"],
        [["Noviembre–diciembre 2026", "Firma, entrega de insumos de la Alcaldía, alistamiento de servidores y canal, carga y depuración de datos, integraciones y pruebas; sin fee mensual", "Inventario de funcionalidades listas para enero", "PROPUESTO"],
         ["Primer día hábil de enero de 2027", "Inicio de operación con las capacidades validadas", "Acta de inicio operativo", "PROPUESTO"],
         ["Febrero–junio 2027", "Habilitación de los módulos y canales pendientes de las fases 1 a 3, validación con funcionarios y ajustes", "Acta por fase", "PROPUESTO"],
         ["Julio–octubre 2027", "Optimización de campañas, fiscalización, escalamiento y seguimiento de indicadores", "Reportes mensuales de seguimiento", "PROPUESTO"],
         ["Noviembre–diciembre 2027", "Cierre de la vigencia, balance del servicio y decisión sobre la opción de compra", "Balance del servicio", "PROPUESTO"]],
        [1.8, 3.6, 1.6, 1.0],
        nota="Qué módulos están disponibles el primer día hábil de enero y la fecha de cierre de cada fase: " + P + ".")
a.h2("11.1 Condiciones de inicio y dependencias")
a.parrafo("La propuesta condiciona el cumplimiento de la ruta a que la Alcaldía entregue los siguientes insumos. Fecha de entrega y responsable nominal de cada uno: " + P + ". "
          "Consecuencia de un retraso sobre el inicio de operación y el fee: " + P + ".")
a.vinetas([
    "Diccionario de datos de MAT-SIM, SICOG II y la base de contratos; definición de los campos requeridos de Cámara de Comercio.",
    "Acceso a las APIs internas de MAT-SIM y SICOG II y a la base de contratos; habilitación y credenciales de las dos APIs externas de Cámara de Comercio.",
    "Link de pago y acceso a la información de recaudo del operador oficial.",
    "Máquinas virtuales de producción y pruebas con Ubuntu Server 24.04 LTS.",
    "Dominio o subdominio, certificado SSL y publicación HTTPS para los webhooks.",
    "Canal de internet dedicado de 50 Mbps y lista blanca de salida hacia los servicios en la nube.",
    "VPN con usuarios nominales para el equipo de Campuslands.",
    "Dirección de correo remitente institucional y registros SPF, DKIM y DMARC en su dominio.",
    "Cuenta de Meta Business y número de WhatsApp a nombre de la Alcaldía, con los documentos de verificación.",
    "Capa geográfica de las zonas del municipio (shapefile o GeoJSON).",
    "Formato de registro de visita.",
    "Procedimientos escritos de cobro y fiscalización, y sesiones con funcionarios que conocen la operación.",
    "Concepto jurídico sobre horarios y frecuencia de contacto (Ley 2300 de 2023) y tratamiento de datos.",
    "Aprobación de guiones, plantillas, reglas de campaña y textos legales.",
])
a.h2("11.2 Equipo del servicio")
a.tabla("Perfiles asignados",
        ["Perfil", "Responsabilidad en el servicio"],
        [["Gerente del servicio", "Punto de contacto con la Alcaldía, seguimiento del avance, reporte mensual y gestión de riesgos"],
         ["Líder técnico", "Arquitectura de despliegue, integraciones y decisiones técnicas con la Dirección de TIC"],
         ["Ingeniero de integraciones y datos", "Carga, depuración y calidad de la cartera; conexión con MAT-SIM, SICOG II, Cámara de Comercio, contratos y el operador oficial"],
         ["Especialista en IA conversacional", "Configuración y ajuste de los agentes de voz y WhatsApp, guiones y gobierno de IA"],
         ["Ingeniero de infraestructura", "Alistamiento del servidor, despliegue, monitoreo, respaldos y actualizaciones"],
         ["Analista funcional y de soporte", "Parametrización, pruebas, capacitación y soporte a funcionarios"],
         ["Diseñador UX", "Adaptación de la interfaz a los flujos de los funcionarios, formulario de visitas, mapa y pruebas de usabilidad"],
         ["Dos desarrolladores junior (Camper)", "Ajustes de parametrización, mejoras correctivas, scripts de integración y carga de datos, y apoyo en pruebas y soporte, con la guía del líder técnico"]],
        [2.6, 5.4],
        nota="Dedicación de cada perfil: la propuesta dice «según necesidades de cada etapa»: " + P + ".")
a.h2("11.3 Seguimiento institucional")
a.tabla("Instancias de seguimiento",
        ["Instancia", "Responsabilidad"],
        [["Dirección de TIC", "Seguimiento técnico y verificación de cumplimiento: disponibilidad, integraciones, infraestructura, seguridad y condiciones técnicas del servicio"],
         ["Dirección de Industria y Comercio", "Seguimiento financiero, administrativo y funcional: campañas, indicadores, funcionamiento para usuarios y facturación"],
         ["Campuslands", "Configuración, integraciones, operación, soporte, monitoreo, correcciones dentro del alcance y reportes de seguimiento"]],
        [2.2, 5.8],
        nota="El servicio se paga mensualmente contra factura y no tiene supervisión con informe de actividades. Indicadores y umbrales de seguimiento: " + P + ".")

# ------------------------------------------------------------------ 12. Capacitación y transferencia
a.h1("12. Capacitación y transferencia")
a.vinetas([
    "Capacitación de funcionarios y documentación técnica, dentro de la puesta en producción (RF-015). Número de sesiones, personas y horas: " + P,
    "Manuales de operación y de usuario, y manual de operación del servidor para TIC (servicios, puertos, rutas y procedimientos de reinicio, respaldo y restauración).",
    "Migración definitiva de información y configuración de los agentes productivos; acompañamiento y estabilización inicial.",
    "Inventario de dependencias y licencias (SBOM) y plan de salida con exportación de datos, por cada proveedor externo.",
    "Si la Alcaldía ejerce la opción de compra en diciembre de 2027: código fuente y documentación del alcance contratado (sección 14).",
])

# ------------------------------------------------------------------ 13. Garantía, soporte y operación
a.h1("13. Garantía, soporte y operación")
a.tabla("Soporte y operación",
        ["Tema", "Lo que declara la propuesta", "Estado"],
        [["Canal", "Requerimientos y tickets a dev@campuslands.com", "PROPUESTO"],
         ["Horario", "Lunes a viernes de 8:00 a. m. a 5:00 p. m.; no se presume soporte 24/7", "PROPUESTO"],
         ["Contenido de cada solicitud", "Asunto, descripción, módulo afectado, fecha, impacto y evidencia disponible", "PROPUESTO"],
         ["Gestión", "Campuslands registra, clasifica, asigna, atiende y comunica el cierre del caso", "PROPUESTO"],
         ["Mantenimiento y operación", "Mantenimiento correctivo y actualizaciones de versión de la plataforma; monitoreo de integraciones y agentes; ajuste de guiones, plantillas y reglas de campaña a solicitud de la Alcaldía", "PROPUESTO"],
         ["Nuevas funcionalidades o procesos ajenos al alcance", "Se tramitan mediante control de cambios", "PROPUESTO"],
         ["Tiempos de respuesta y solución por criticidad (SLA)", "«Se establecerán en el acuerdo de nivel de servicio contractual»", "PENDIENTE"],
         ["Garantía", "No declarada en la propuesta", "PENDIENTE"]],
        [2.4, 4.6, 1.0],
        nota="Cuáles solicitudes se consideran corrección de errores y cuáles nuevas solicitudes, y el SLA y la garantía: " + P + ".")

# ------------------------------------------------------------------ 14. Condiciones comerciales
a.h1("14. Condiciones comerciales")
a.parrafo("Las condiciones de esta sección se transcriben de la propuesta. Ninguna se ha contrastado con una cotización aprobada, que no se aportó (regla de verificación previa a la firma). "
          "Todo lo que no figura en la propuesta queda " + P + ".")
a.tabla("Valores propuestos",
        ["Concepto", "Valor, impuestos incluidos", "Estado"],
        [["Fee mensual de servicio (enero a diciembre de 2027)", "$50.000.000 COP", "PROPUESTO"],
         ["Opción facultativa de compra con marca blanca (diciembre de 2027)", "$540.000.000 COP", "PROPUESTO"]],
        [4.4, 2.6, 1.0],
        nota="Doce cuotas de $50.000.000 suman $600.000.000 COP (operación aritmética de este documento; no figura expresamente en la propuesta). Desglose del fee: " + P + ".")
a.h2("14.1 Facturación y pago")
a.vinetas([
    "La facturación inicia en enero de 2027 por el servicio de ese mes; la Alcaldía paga a mes vencido, comenzando en febrero de 2027, conforme a los trámites y plazos contractuales.",
    "Los valores incluyen «IVA y demás impuestos, retenciones y estampillas aplicables». Alcance de esta frase frente a las retenciones: " + P,
    "Con pago a mes vencido, la cuota de diciembre de 2027 se pagaría en enero de 2028. Vigencia presupuestal aplicable: " + P,
    "Los cánones mensuales remuneran el uso y la operación del servicio y no constituyen abonos al precio de compra.",
    "Reajuste de precio, anticipos e hitos de pago: " + P,
])
a.h2("14.2 Qué cubre el fee")
a.vinetas([
    "Uso de la plataforma de Campuslands y sus actualizaciones de versión.",
    "Consumo de servicios externos: llamadas y telefonía, WhatsApp, correo y modelo de lenguaje, según las necesidades de la operación. Volumen de referencia: " + P,
    "Alistamiento, despliegue, integraciones y carga de datos en la infraestructura de la Alcaldía.",
    "Configuración y ajuste de los agentes de IA y de las campañas.",
    "Equipo asignado, soporte y monitoreo; capacitación y acompañamiento a funcionarios.",
])
a.parrafo("No cubre los servidores y el canal dedicado, que aporta la Alcaldía. Costos de las dos APIs de Cámara de Comercio y de geocodificación: " + P + ".")
a.h2("14.3 Opción de compra y propiedad intelectual")
a.parrafo("La opción de compra es facultativa: exige manifestación expresa de la Alcaldía, instrumento contractual y los trámites presupuestales aplicables. "
          "La propuesta indica que comprende los derechos de uso, explotación y adaptación en marca blanca, el código fuente y la documentación del alcance contratado, y que no transfiere la propiedad de servicios de terceros ni sus licencias. "
          "Si esto equivale a una cesión de titularidad o a una licencia, su exclusividad y el alcance de «adaptación»: " + P + " (requiere revisión jurídica).")
a.tabla("Componentes y qué ocurre con la opción de compra",
        ["Componente", "Tipo", "Con la opción de compra"],
        [["Plataforma: aplicación web, API, motor de campañas y módulos", "Propio de Campuslands", "Se transfiere en marca blanca, con código fuente y documentación"],
         ["Configuración de los agentes: guiones, flujos e instrucciones", "Propio de Campuslands", "Se transfiere con la plataforma"],
         ["Retell AI, Twilio o Telnyx, proveedor de correo y modelo de lenguaje", "Servicios de terceros", "Siguen con su proveedor, bajo sus condiciones"],
         ["API de WhatsApp Business (Meta)", "Servicio de tercero", "El servicio sigue con Meta"],
         ["Node.js, Vue.js, MariaDB, Redis, Leaflet", "Código abierto", "Conservan sus licencias abiertas"]],
        [3.6, 1.8, 2.6],
        nota="Componentes preexistentes de Campuslands distintos de los listados: " + P + ".")
a.h2("14.4 Otras condiciones")
a.vinetas([
    "La propuesta se entiende aceptada y vinculante una vez suscrita por los representantes legales o funcionarios facultados, siempre que se cumplan los requisitos legales, presupuestales y contractuales aplicables.",
    "Cualquier modificación posterior debe constar por escrito y contar con la aprobación de ambas partes.",
    "Penalidades, terminación anticipada, confidencialidad contractual y responsabilidad por errores de los agentes de IA: " + P,
])

# ------------------------------------------------------------------ 15. Supuestos, exclusiones y riesgos
a.h1("15. Supuestos, exclusiones y riesgos")
a.h2("15.1 Supuestos")
a.vinetas([
    "La Alcaldía aporta máquinas virtuales, almacenamiento, dominio, configuración de seguridad, VPN, respaldos y un canal dedicado de 50 Mbps, independiente de los canales institucionales.",
    "Las integraciones con fuentes externas dependen de la disponibilidad efectiva de datos y de accesos autorizados.",
    "La calidad del mapa y de la georreferenciación depende de los datos suministrados por la Alcaldía.",
    "Las decisiones tributarias siguen a cargo de la Alcaldía; la propuesta no garantiza un monto de ahorro ni de recaudo.",
    "No se presume soporte 24/7; el SLA se define en el contrato.",
    "Los guiones, plantillas, reglas y textos legales los aprueba la Alcaldía; los horarios y la frecuencia de contacto los valida su jurídica.",
])
a.h2("15.2 Exclusiones")
a.parrafo("Ver sección 3.2 y las ampliaciones de Fase 4 en la sección 3.3.")
a.h2("15.3 Pendientes bloqueantes")
a.parrafo("Los siguientes puntos deben resolverse antes de la firma. Cada uno se valida con el responsable indicado.")
a.tabla("Pendientes críticos para la aprobación",
        ["ID", "Tema", "Qué falta", "Responsable"],
        [["PEN-002", "Consumos y volúmenes", "Llamadas, minutos y mensajes incluidos en el fee, sin cifra; qué ocurre al superarlos", "Comercial y líder técnico"],
         ["PEN-003", "Universo de cartera", "Número de contribuyentes y obligaciones, que dimensiona servidores, consumos y plazos", "Dirección de ICA e integraciones"],
         ["PEN-004", "Operación en enero", "Módulos disponibles el primer día hábil de 2027 frente a un fee que corre desde enero; fecha de cierre de cada fase", "Comercial, líder técnico y Alcaldía"],
         ["PEN-005", "Condiciones de inicio", "Fecha y responsable de cada insumo de la Alcaldía; efecto de un retraso", "Comercial, jurídico y TIC"],
         ["PEN-006", "Aceptación", "Criterios medibles por módulo y su relación con el pago", "Comercial y Alcaldía"],
         ["PEN-007", "SLA, garantía y soporte", "Tiempos por criticidad, garantía, separación entre errores y nuevas solicitudes", "Comercial y jurídico"],
         ["PEN-008", "Propiedad intelectual", "Alcance de los derechos de la opción de compra y encaje contractual", "Jurídico"],
         ["PEN-009", "Datos personales y contacto", "Responsable y encargado del tratamiento, grabaciones, retención y Ley 2300", "Jurídico (Campuslands y Alcaldía)"],
         ["PEN-010", "Terceros y costos", "Proveedor del modelo de lenguaje, telefonía y correo; proveedor y pago de las APIs de Cámara de Comercio", "Líder técnico y comercial"],
         ["PEN-011", "Integraciones internas", "Existencia, documentación y acceso de las APIs de MAT-SIM, SICOG II, contratos y recaudo", "TIC de la Alcaldía e integraciones"],
         ["PEN-012", "Condiciones comerciales", "Retenciones, vigencia presupuestal, reajuste, hitos de pago y contraste con la cotización", "Comercial, financiera y jurídico"],
         ["PEN-013", "Usuarios y permisos", "Perfiles, número de usuarios y visibilidad por perfil", "Dirección de ICA y TIC"]],
        [0.9, 1.7, 3.8, 1.6],
        nota="El registro completo de pendientes (25) está en el archivo de trabajo del proyecto.")
a.h2("15.4 Riesgos")
a.tabla("Riesgos identificados en la propuesta",
        ["Riesgo", "Efecto", "Mitigación declarada o pendiente"],
        [["Datos o accesos de fuentes externas no disponibles", "Fiscalización incompleta", "La propuesta lo declara como dependencia. Alternativa si una integración no es viable: " + P],
         ["Contactar a quien ya pagó, porque el recaudo se importa en la Fase 3 y las campañas corren en la Fase 2", "Contacto indebido a contribuyentes", P],
         ["Calidad de direcciones", "Contribuyentes fuera del mapa", "Zona adicional hasta corregir; funcionarios capturan coordenadas en visitas"],
         ["Costos de consumo superiores a los previstos", "Costos no cubiertos por el fee", "Aprobación previa de volúmenes; reglas de reparto: " + P],
         ["Retraso en los insumos de la Alcaldía", "Plazo", P]],
        [3.0, 2.0, 3.0])

# ------------------------------------------------------------------ 16. Aprobación y anexos
a.h1("16. Anexos")
a.h2("Anexo A. Glosario")
a.tabla("Términos usados en este documento",
        ["Término", "Significado en este documento"],
        [["ICA", "Impuesto de Industria y Comercio, cuya cartera es el objeto del servicio"],
         ["EMPLAZAR", "Columna del listado de fiscalización con tres valores: por emplazar, no clasificado para emplazamiento o pendiente de validación"],
         ["Contacto en cascada", "Secuencia WhatsApp, correo y llamada del agente de voz, según la respuesta del contribuyente"],
         ["Semáforo de gestión", "Color asignado a cada contribuyente según el estado de su gestión; reglas: " + P],
         ["Fuente de verdad de los pagos", "El operador oficial del municipio; la plataforma importa su información de recaudo"],
         ["Marca blanca", "Operación de la plataforma con identidad institucional de la Alcaldía, con derechos de uso, explotación y adaptación"],
         ["SBOM", "Inventario de dependencias y licencias que Campuslands entrega"],
         ["SLA", "Acuerdo de nivel de servicio que fijará los tiempos de respuesta y solución por criticidad"],
         ["Webhook", "Aviso que un servicio en la nube envía a la plataforma con respuestas y resultados"]],
        [2.2, 5.8])
a.h2("Anexo B. Matriz de trazabilidad de requisitos")
a.tabla("Requisitos funcionales y su origen",
        ["ID", "Requisito", "Fuente", "Prioridad", "Fase", "Aceptación", "Estado"],
        [[f"RF-{i:03d}", nombre, "Anexo técnico", "No declarada", fase, "Ver ficha", "PROPUESTO"] for i, nombre, fase in [
            (1, "Levantamiento y parametrización", "1"), (2, "Arquitectura de despliegue e integración", "1"),
            (3, "Fiscalización", "1"), (4, "Núcleo de gestión de cartera y cobro", "1"), (5, "Dashboard de cartera", "1"),
            (6, "Mapa de contribuyentes por zona", "1"), (7, "Motor de campañas", "2"), (8, "Agente de voz", "2"),
            (9, "Agente de WhatsApp", "2"), (10, "Canal de correo", "2"), (11, "Dashboard de gestión y asistente", "2"),
            (12, "Gestión de casos escalados", "3"), (13, "Gestión de visitas", "3"),
            (14, "Verificación de pagos (básica)", "3"), (15, "Validación en operación real", "3")]],
        [0.8, 2.6, 1.1, 1.2, 0.6, 1.1, 1.0],
        nota="La propuesta no declara prioridad por requisito: " + P + ". Aceptación: ver el campo «Criterios de aceptación» de cada ficha (sección 5).")
a.h2("Anexo C. Integraciones")
a.parrafo("Ver la matriz de la sección 6.1 (INT-01 a INT-14).")
a.h2("Anexo D. Plan de pruebas")
a.tabla("Pruebas declaradas en la propuesta",
        ["Familia", "Alcance declarado", "Estado"],
        [["Integración y datos", "Pruebas de integraciones, funcionales y de calidad de datos", "PROPUESTO"],
         ["Agentes y canales", "Agentes de IA, pruebas conversacionales, llamadas masivas, WhatsApp, envío de correo y cascada entre canales", "PROPUESTO"],
         ["Procesos de negocio", "Verificación de pagos", "PROPUESTO"],
         ["No funcionales", "Seguridad (pruebas básicas OWASP), rendimiento y concurrencia, recuperación ante fallos", "PROPUESTO"],
         ["Aceptación", "Pruebas con funcionarios de la Alcaldía, corrección y estabilización", "PROPUESTO"]],
        [1.8, 5.2, 1.0],
        nota="Los casos de prueba y sus criterios de paso se definen en el levantamiento de la Fase 1.")
a.h2("Anexo E. Registro de decisiones")
a.tabla("Decisiones registradas",
        ["ID", "Fecha", "Decisión", "Origen"],
        [["DEC-001", "2026-10-29", "La propuesta del 28 de octubre de 2026 es el documento vigente; no hay otro posterior", "Chat del proyecto"],
         ["DEC-002", "2026-10-29", "No se dispone de actas de la mesa técnica, cotización ni requerimiento de la Alcaldía; el documento se basa solo en la propuesta", "Chat del proyecto"],
         ["DEC-003", "2026-10-29", "Se produce el alcance funcional para el cliente; no se firma mientras haya pendientes críticos", "Chat del proyecto"],
         ["DEC-008", "2026-10-29", "Lo que la propuesta no declara se marca " + P + " y no se completa con suposiciones", "Chat del proyecto"]],
        [0.9, 1.3, 3.7, 2.1])
a.h1("Referencias")
a.referencias([
    "Campuslands S.A.S. BIC. (2026, 28 de octubre). Propuesta comercial y técnica: Servicio inteligente de cobro persuasivo y fiscalización tributaria con IA [Propuesta]. Alcaldía Municipal de Girón.",
])

a.firmas(
    FIRMA_IZQ,
    {"etiqueta": "POR LA ALCALDÍA", "nombre": "CAMPO ELÍAS RAMIREZ", "documento": "C.C. No. " + P,
     "cargo": "Alcalde", "entidad": "ALCALDÍA DE GIRÓN"},
    texto="Con su firma, las partes manifiestan conocer y aceptar el alcance funcional y técnico, las condiciones económicas, las obligaciones y el "
          "cronograma de este documento y sus anexos, una vez cumplidos los requisitos legales, presupuestales y contractuales aplicables, y resueltos "
          "los pendientes críticos de la sección 15.",
    lugar_fecha="En el municipio de Girón, Santander, a los ____ días del mes de ____________ de ______.",
)

ruta = a.guardar(SALIDA, "Alcance Funcional — Alcaldía de Girón")
print(ruta)
