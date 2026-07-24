# Perfil de Usuario y Empresa Objetivo (ICP)

Este documento define quién es el usuario, qué vende Campuslands, y —lo más
importante para este agente— **qué perfil de empresa califica como buen
prospecto**, para orientar los filtros de búsqueda y el criterio de
enriquecimiento.

---

## 1. Identidad: Campuslands Full Service

**Campuslands S.A.S. BIC** (Zona Franca Santander) opera como una **Fábrica
de Software Enterprise (Software House)**, especializada en:
* Inteligencia Artificial (IA) generativa y predictiva.
* Automatización inteligente y transformación digital enterprise.
* **Staffing de talento técnico certificado y de nivel Senior** (desarrolladores
  de software y perfiles con capacidades de IA) — el producto que este
  agente ayuda a vender vía prospección.

## 2. El Usuario (Director / Consultor Comercial)

El usuario es el director o consultor comercial de Full Service. En este
repositorio:
1. **Dirige y cura:** pide búsquedas (por filtro o libres), valida los
   listados generados y decide qué empresas pasan a la siguiente etapa
   (Explorador de Campus).
2. **Interactúa:** usa a Radar de Campus como su herramienta de
   descubrimiento inicial de cuentas, antes de invertir tiempo en
   identificar contactos.

---

## 3. Perfil de Empresa Objetivo (ICP)

Este ICP es la base por defecto que usan las skills `busqueda-web-empresas`
y `enriquecimiento-datos-empresa` para juzgar si una empresa encontrada vale
la pena listar — se ajusta por sesión con los 6 datos del formulario de
intake (ver [[formulario-intake]]), pero estos son los criterios de
referencia cuando el usuario deja un campo sin restricción.

### Perfil ideal
* **Sector:** desarrollo de software, servicios/consultoría IT, tecnología,
  información e internet — y, en general, cualquier empresa con necesidad
  de equipo técnico propio (fintech, healthtech, e-commerce, SaaS, etc.).
* **Tamaño:** preferentemente 50–500 empleados. Segmentación interna:
  pequeña (50–100), mediana (101–250), grande (251–500). Por debajo de 50
  empleados suele faltar presupuesto o estructura recurrente para staffing.
* **Tipo de empresa:** privada (no gobierno, no sector público).
* **Señales de calificación (mientras más, mejor prospecto):**
  crecimiento de plantilla, vacantes abiertas para desarrolladores, ronda de
  inversión reciente, noticias de expansión o transformación digital.
* **Palabras clave asociadas:** SaaS, software, plataforma, cloud, IA, datos,
  automatización.

### Exclusiones estrictas
Gobierno, ONGs, colegios/universidades, agencias de staffing o
reclutamiento (competencia directa).

### Qué buscan las empresas objetivo (para dar contexto al listado entregado)
* **Retorno Financiero (ROI):** cuánto ahorran/ganan al resolver escasez de
  talento técnico con staffing externo.
* **Mitigación de riesgo de contratación:** acceso a talento senior
  certificado sin el costo/tiempo de un proceso de reclutamiento propio.
* **Velocidad:** capacidad de escalar equipos de desarrollo o IA rápido.

---

## 4. Relación con el resto del pipeline

Este ICP es el mismo que usa `IntelligenceCommercial` (Explorador de Campus)
para clasificar contactos en su Fase 2 — ver
`../IntelligenceCommercial/wiki/perfiles-objetivo.md`. La diferencia es de
nivel: aquí calificamos la **empresa**; allá se califica la **persona**
dentro de la empresa ya calificada.
