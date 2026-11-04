---
name: generacion-tabla-registro
description: Registra cada conexión enviada en una tabla estandarizada (Fecha, Empresa, Contacto, Cargo) y la entrega al usuario como output final del trabajo de prospección.
---

# Generación de Tabla de Registro

## Cuándo usar esta skill

Inmediatamente después de que `control-navegador-linkedin` confirme el envío exitoso de una solicitud de conexión con mensaje, y al cierre del trabajo para entregar el resumen consolidado al usuario.

## Entradas

- Por cada conexión enviada: fecha real de envío, nombre de la empresa, nombre del contacto, cargo del contacto.
- Opcional: mensaje enviado e idioma detectado, si el usuario pide detalle ampliado (alineado con el formato `04-informe-divulgacion.csv` de `Perplexity.md`).

## Procedimiento

1. Por cada conexión exitosa, añadir una fila con:
   - **Fecha** en formato `YYYY-MM-DD` (fecha real de ejecución, no de la solicitud del usuario).
   - **Empresa** tal como aparece en el perfil de LinkedIn.
   - **Contacto** (nombre completo del perfil).
   - **Cargo** tal como aparece en el perfil de LinkedIn.
2. No registrar una fila para conexiones que no llevaron mensaje enviado — conexión y mensaje van juntos.
3. Al finalizar la sesión (meta alcanzada o resultados agotados), consolidar todas las filas en una sola tabla en formato Markdown.
4. Anteponer un resumen breve: número de conexiones logradas vs. meta solicitada, y motivo si quedó incompleta.
5. Compartir la tabla completa con el usuario como cierre del trabajo.

## Reglas obligatorias

- No inventar ni completar campos con datos no verificados — usar exactamente lo que aparece en el perfil.
- No mezclar conexiones de sesiones distintas sin indicar la fecha correspondiente a cada una.
- Formato de fecha siempre `YYYY-MM-DD`, sin excepciones.

## Salida

Tabla en Markdown con columnas `Fecha | Empresa | Contacto | Cargo`, más el resumen de cierre, entregada directamente al usuario.
