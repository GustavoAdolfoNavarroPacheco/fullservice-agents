---
name: deteccion-idioma
description: Determina si un perfil de LinkedIn es de habla inglesa o hispana a partir del perfil y sus publicaciones recientes, para que el mensaje de conexión se redacte en el idioma correcto.
---

# Detección de Idioma del Contacto

## Cuándo usar esta skill

Justo antes de redactar el mensaje de conexión para cualquier perfil, y siempre después de que `control-navegador-linkedin` haya abierto y verificado el perfil candidato. Es un paso obligatorio del flujo — ningún mensaje se redacta sin haber pasado por esta skill.

## Entradas

- URL o contenido visible del perfil de LinkedIn (nombre, headline, experiencia).
- Publicaciones o comentarios recientes del perfil, si están disponibles.
- Ubicación indicada en el perfil (ciudad/estado) y nombre de la empresa, como señales secundarias.

## Procedimiento

1. Leer el idioma en que está escrito el propio perfil (headline, sección "Acerca de", experiencia).
2. Si el perfil tiene publicaciones o comentarios recientes, priorizarlos como señal principal — el idioma en que la persona *escribe activamente* pesa más que el idioma de la interfaz o de la ubicación.
3. Usar la ubicación geográfica y el nombre de la empresa como señal de apoyo, nunca como criterio único (hay hispanohablantes en EE. UU. y angloparlantes en LATAM).
4. Si la evidencia es mixta o insuficiente, usar inglés por defecto (idioma base de la plantilla) y dejar constancia de la ambigüedad si el usuario pide detalle.
5. Devolver una etiqueta clara: `EN` o `ES`.

## Reglas obligatorias

- No decidir el idioma únicamente por el país de la empresa o la sede — puede no coincidir con el idioma del contacto.
- No mezclar idiomas dentro de un mismo mensaje.
- Ante ambigüedad real, preferir inglés (plantilla base) antes que arriesgar un mensaje mal dirigido.

## Salida

Una etiqueta de idioma (`EN` / `ES`) que la skill de generación de mensajes personalizados usa para elegir la plantilla base correspondiente.
