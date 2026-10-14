---
name: busqueda-web-empresas
description: Construye y ejecuta búsquedas en la web abierta (nunca LinkedIn) a partir del criterio confirmado por formulario-intake, y recopila candidatos hasta acercarse al Número de Empresas solicitado.
---

# Búsqueda Web de Empresas

## Cuándo usar esta skill

Inmediatamente después de que `formulario-intake` entregue el criterio de
búsqueda confirmado (los 6 campos, con "sin restricción" donde aplique).

No uses esta skill para: navegar o buscar dentro de LinkedIn/Sales
Navigator bajo ninguna circunstancia, ni para buscar personas/contactos
individuales.

## Entradas

- Criterio estructurado de `formulario-intake`: Número de Empresas, Sector,
  Ubicación, Tamaño, Número de empleados, Facturación anual.
- ICP de referencia en `perfil-usuario.md` (para descartar resultados que no
  califican en los campos que el usuario dejó "sin restricción").

## Procedimiento

1. Construir la o las consultas de búsqueda combinando Sector + Ubicación
   como base, y usando Tamaño/Número de empleados/Facturación anual como
   filtros adicionales cuando el usuario los dio.
2. Buscar en la web abierta: buscadores generales, directorios
   empresariales, gremios sectoriales, Superintendencia de Sociedades,
   portales de empleo y sitios corporativos — ver `enlaces-utiles.md` como
   punto de partida, sin limitarse a esa lista.
3. Para cada empresa que aparezca, registrar: razón social, sitio web (si se
   encuentra) y la fuente/URL donde se encontró la mención.
4. Descartar de inmediato cualquier resultado proveniente de LinkedIn —
   buscar la misma información en otra fuente en vez de usarla.
5. Aplicar las exclusiones estándar del ICP (gobierno, ONGs, universidades,
   agencias de staffing/reclutamiento) antes de considerar candidata a una
   empresa.
6. Deduplicar candidatos por dominio o razón social normalizada.
7. Seguir buscando hasta acercarse al **Número de Empresas** solicitado, o
   hasta agotar razonablemente las fuentes disponibles — lo que ocurra
   primero.

## Reglas obligatorias

- **Nunca** usar LinkedIn ni Sales Navigator como fuente de búsqueda o
  verificación.
- **Nunca** inventar empresas ni completar el listado con nombres no
  encontrados realmente en una fuente, aunque falten empresas para llegar
  al Número de Empresas pedido.
- Cada candidato debe tener al menos una fuente verificable antes de pasar a
  `enriquecimiento-datos-empresa`.
- Si la búsqueda no alcanza el Número de Empresas solicitado, decirlo
  explícitamente al usuario en vez de rellenar el listado con empresas que
  no calzan con el criterio.

## Salida

Lista preliminar de empresas candidatas (razón social + sitio web + fuente
inicial), entregada a `enriquecimiento-datos-empresa`.
