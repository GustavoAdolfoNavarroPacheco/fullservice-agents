# Marca Campuslands — Tono para mensajes de LinkedIn

Este documento define el **tono de voz** que debe mantener
`habilidades/generacion-mensajes-personalizados` al redactar solicitudes de conexión de
LinkedIn. **No es una guía de identidad visual** (paleta, tipografía, logos para
diapositivas) — este agente no diseña presentaciones ni genera PDFs; esa guía existe
en `PresentationsDesigner`, que es un agente distinto con audiencia y entregable
distintos (ver [[perfil-usuario]] §4).

---

## 1. Tono y estilo del mensaje de conexión

- **Breve, directo, entre pares (peer-to-peer), consultivo.**
- Nunca lenguaje de venta agresiva, signos de exclamación excesivos, ni superlativos.
- Se adapta al **idioma real del contacto** (detectado por `deteccion-idioma`, EN o ES)
  — nunca se traduce mecánicamente la plantilla base.
- Cabe dentro del límite de caracteres de una nota de conexión de LinkedIn.

## 2. Gancho central del mensaje

- Escalar equipos de desarrollo con talento técnico, específicamente para llevar
  iniciativas de IA de piloto a producción.
- Diferenciador real que sostiene ese gancho (ver `wiki/perfil-usuario.md` §1): el
  talento proviene del programa de formación propio de Campuslands, no de un banco de
  hojas de vida genérico. No es obligatorio mencionarlo en cada mensaje, pero es el
  respaldo real detrás de la promesa si el contacto pregunta.

## 3. Plantillas base

Las plantillas EN/ES vigentes viven en
`habilidades/generacion-mensajes-personalizados/SKILL.md` (fuente única — no se
duplican aquí para evitar que un ajuste a la plantilla quede desincronizado entre dos
archivos).

## 4. Qué no se debe hacer

- No usar paleta de colores, tipografía ni logos de diapositivas — no aplican a un
  mensaje de texto plano de LinkedIn.
- No prometer plazos, precios ni resultados no verificados.
- No inventar contexto sobre la persona o la empresa que no esté verificado en el
  perfil o sus publicaciones recientes.
- No enviar el mensaje en un idioma distinto al detectado por `deteccion-idioma`.

## 5. Assets disponibles en `recursos/`

Logos, isotipo, favicon y brandbook de Campuslands están en `recursos/` como material
de identidad/referencia, pero **no se usan en el flujo actual** de este agente (que no
genera ningún entregable visual). Quedan disponibles por si en el futuro se agrega un
entregable que sí los necesite.
