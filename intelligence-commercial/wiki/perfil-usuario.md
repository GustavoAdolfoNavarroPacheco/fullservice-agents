# Perfil de Usuario y Audiencia — Explorador de Campus

Este documento define el contexto comercial, el rol del usuario y la audiencia objetivo
de la prospección en LinkedIn que hace **Explorador de Campus** (`IntelligenceCommercial`).
No es la misma audiencia ni el mismo servicio que venden los agentes de presentaciones/
cotizaciones/licitaciones — ver §4.

---

## 1. Identidad: Campuslands Full Service

Fuente: `recursos/Brief Fullservice.pdf`.

**Full Service** es el área comercial de **Campuslands S.A.S. BIC** especializada en
soluciones de desarrollo de software. Ofrece tres líneas de servicio:

- **Desarrollo de software a la medida** — proyectos completos.
- **Células de trabajo / Horas** — equipos dedicados o desarrolladores por horas
  (staff augmentation). **Esta es la línea que este agente prospecta en LinkedIn.**
- **Consultoría de transformación digital**.

Valor declarado en el Brief: flexibilidad, acompañamiento continuo, equipo experto,
resultados eficientes.

**Diferenciador real para el outreach:** Campuslands forma a sus propios desarrolladores
mediante un programa de entrenamiento intensivo propio (10 meses, ~1.600 horas de
programación + inglés + liderazgo). El talento que se ofrece en staffing no viene de un
banco de hojas de vida genérico, sino de esta cantera propia — es el argumento que
sostiene el gancho "developers and technical talent for AI initiatives" de la plantilla
de mensaje (ver `habilidades/generacion-mensajes-personalizados/SKILL.md`).

---

## 2. El usuario

El usuario dirige los lotes de prospección de este agente:

1. **Aporta o valida** la lista de empresas objetivo — normalmente ya generada por
   `ProspectionAgent` (Radar de Campus), el eslabón anterior del pipeline.
2. **No aprueba mensaje por mensaje**: por decisión fundacional (ver `Perplexity.md`),
   el envío de solicitudes de conexión es autónomo.
3. **Revisa el resultado** al cierre de cada lote en
   `prospeccion/<slug-lote>/04-informe-divulgacion.csv`.

---

## 3. Audiencia objetivo (contactos en LinkedIn)

Fuente: [[filtros-busqueda]] y [[perfiles-objetivo]].

- **Empresas:** startups y scaleups de software SaaS en EE. UU. (California, Texas,
  New York, Florida, Washington), 51–500 empleados, de capital privado.
- **Contactos prioritarios:** roles de Talento/RR. HH. (Head of Talent, Talent
  Acquisition Manager/Lead/Director, VP Talent, Head of People, People Operations
  Manager, HR Manager, Recruiting Manager, Technical Recruiter).
- **Contactos secundarios (Fase 2 de clasificación):** CTO, VP de Ingeniería, líderes
  de IA y gerentes de contratación técnica — ver [[perfiles-objetivo]] para el detalle
  completo de los 5 perfiles válidos.
- **Qué buscan (según el gancho ya validado de la plantilla de mensaje):** apoyo para
  escalar equipos de desarrollo con talento técnico, en particular para llevar
  iniciativas de IA de piloto a producción.

---

## 4. Qué NO es esta audiencia

Este agente **no** vende lo mismo ni a los mismos compradores que
`PresentationsDesigner`, `QuoteDeveloper` o `BiddingAgent` (que ofrecen proyectos de
software a la medida completos a Directores Generales, CFOs o CTOs de empresas
medianas/grandes, mayormente en LatAm). Explorador de Campus prospecta específicamente
la línea de **staffing de desarrolladores** (Células de trabajo / Horas) entre
Talento/RR. HH. y liderazgo técnico de empresas SaaS en EE. UU. Mezclar ambos perfiles
de audiencia en un mismo mensaje o material sería un error de segmentación.
