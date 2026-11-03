---
name: generacion-mensajes-personalizados
description: Redacta el mensaje de conexión de LinkedIn a partir de la plantilla base de Campuslands, adaptado al idioma, cargo, empresa y contexto específico del contacto, con tono directo y consultivo.
---

# Generación de Mensajes Personalizados

## Cuándo usar esta skill

Después de que `deteccion-idioma` haya devuelto la etiqueta de idioma del contacto, y antes de que `control-navegador-linkedin` proceda a pegarlo y enviarlo de forma autónoma.

## Entradas

- Etiqueta de idioma (`EN` / `ES`) de `deteccion-idioma`.
- Nombre, cargo y empresa del contacto.
- Contexto adicional si está disponible (publicación reciente relevante, señal de "hiring on LinkedIn", cambio de trabajo).

## Plantillas base

**EN:**
> Hi [Nombre], noticed your focus on moving AI from pilot to production. Campuslands helps teams scale with devs and technical talent for AI initiatives. Worth a brief chat, or is someone else at [Empresa] handling technical hiring?

**ES:**
> Hola [Nombre], vi tu enfoque en llevar IA de piloto a producción. En Campuslands ayudamos a equipos a escalar con desarrolladores y talento técnico para iniciativas de IA. ¿Valdría la pena una breve charla, o hay alguien más en [Empresa] manejando la contratación técnica?

## Procedimiento

1. Seleccionar la plantilla base según la etiqueta de idioma recibida.
2. Reemplazar [Nombre] y [Empresa] con los datos reales del contacto.
3. Si hay contexto adicional relevante (publicación reciente, señal de contratación activa), ajustar la frase inicial para reflejarlo de forma natural — no es obligatorio forzarlo si no hay nada genuino que decir.
4. Mantener el tono: breve, directo, entre pares, consultivo. Nunca lenguaje de venta agresiva, signos de exclamación excesivos, ni superlativos.
5. Revisar longitud: el mensaje debe caber dentro del límite de caracteres de una nota de conexión de LinkedIn.
6. Entregar el mensaje final listo para su envío autónomo.

## Reglas obligatorias

- No enviar el mensaje sin haber pasado antes por `deteccion-idioma`.
- No usar la plantilla en un idioma distinto al detectado.
- No inventar contexto sobre la persona o la empresa que no esté verificado en el perfil.
- Mantener consistencia de marca con `marca-campuslands.md`.

## Salida

Texto final del mensaje de conexión, en el idioma correcto, listo para ser pegado por `control-navegador-linkedin` para su envío directo.
