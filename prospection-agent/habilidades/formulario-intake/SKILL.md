---
name: formulario-intake
description: Al empezar la conversación (o al pedir una búsqueda nueva), solicita los 6 datos fijos del formulario de intake (Número de Empresas, Sector, Ubicación, Tamaño, Número de empleados, Facturación anual) y confirma el criterio antes de ejecutar nada.
---

# Formulario de Intake

## Cuándo usar esta skill

Siempre, al empezar la conversación con el usuario, y de nuevo cada vez que
se pide una búsqueda nueva dentro de la misma sesión — antes de que
`busqueda-web-empresas` ejecute una sola consulta. Es el primer paso
obligatorio del flujo de Radar de Campus.

No uses esta skill para: búsquedas de contactos individuales o mensajes de
LinkedIn (eso pertenece a `IntelligenceCommercial`), ni para refinar
parámetros de un lote ya confirmado dentro de la misma búsqueda.

## Entradas

- Mensaje del usuario (puede traer ya todos o algunos de los 6 datos, ej.
  "empresas constructoras en Bogotá, medianas, +100 empleados, facturación
  $5.000.000.000 o más, dame 15", o puede ser genérico, ej. "buscá empresas
  para prospectar").

## Procedimiento

1. Pedir (o confirmar, si ya vinieron en el mensaje inicial) los 6 campos,
   siempre en este orden:
   ```
   1. Número de Empresas
   2. Sector (ej. Constructor)
   3. Ubicación (Ciudad)
   4. Tamaño (Pequeña, Mediana, Grande)
   5. Número de empleados (ej: +100)
   6. Facturación anual (ej. $5.000.000.000 o más)
   ```
2. Si el usuario ya dio un dato claro para un campo, no volver a preguntarlo
   — solo confirmar el resumen mapeado antes de buscar (ver ejemplo en
   `formulario-intake.md`).
3. Si el usuario responde "no sé", "cualquiera", "no aplica" o deja un campo
   sin responder tras pedírselo una vez, marcar ese campo como **sin
   restricción** y seguir — no insistir más de una vez por campo.
4. Si falta específicamente **Número de Empresas**, usar un valor por
   defecto de **10** y comunicarlo explícitamente al usuario antes de
   buscar (ej. "no diste un número, voy a traer 10 empresas por defecto").
5. Si **Tamaño** y **Número de empleados** son contradictorios entre sí
   (ej. "Grande" con "+10 empleados"), preguntar al usuario cuál priorizar
   en vez de asumir.
6. Confirmar el criterio final (los 6 campos, con los que quedaron "sin
   restricción" marcados como tal) antes de pasarlo a `busqueda-web-empresas`.

## Reglas obligatorias

- **Nunca** ejecutar una búsqueda sin haber pasado por este formulario al
  menos una vez en la conversación (aunque sea confirmando datos ya dados).
- No convertir el formulario en un interrogatorio rígido si el usuario ya
  dio la información de forma natural en su mensaje — confirmar y avanzar.
- Aplicar las exclusiones estándar de `perfil-usuario.md` (gobierno, ONGs,
  universidades, agencias de staffing) salvo que el usuario indique lo
  contrario explícitamente.

## Salida

Un criterio de búsqueda estructurado con los 6 campos (valor concreto o
"sin restricción" para cada uno), entregado a `busqueda-web-empresas`.
