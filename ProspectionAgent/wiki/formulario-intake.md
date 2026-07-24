# Formulario de Intake

Este documento define el formulario fijo que **Radar de Campus** pide **al
empezar cada conversación** (o al iniciar una búsqueda nueva dentro de una
sesión). Reemplaza al antiguo menú de "4 filtros + Otro". Ver Fase 1 en
`Perplexity.md` y la skill `formulario-intake`.

---

## Los 6 campos (pedir siempre, en este orden)

> **Para buscar empresas necesito estos datos:**
> 1. **Número de Empresas:** ¿cuántas empresas quieres en el listado?
> 2. **Sector:** (ej. Constructor)
> 3. **Ubicación:** (Ciudad)
> 4. **Tamaño:** (Pequeña, Mediana, Grande)
> 5. **Número de empleados:** (ej: +100)
> 6. **Facturación anual:** (ej. $5.000.000.000 o más)

### Detalle de cada campo

| Campo | Qué es | Ejemplo |
|---|---|---|
| Número de Empresas | Meta de resultados del lote — cuántas filas debe tener la tabla final. | 20 |
| Sector | Industria o vertical específica a buscar. | Constructor, Software, Fintech |
| Ubicación | Ciudad (o ciudad + país si hay ambigüedad) donde debe tener sede/operación la empresa. | Bogotá |
| Tamaño | Categoría cualitativa de tamaño. | Pequeña / Mediana / Grande |
| Número de empleados | Umbral cuantitativo de empleados — normalmente un piso mínimo. | +100 |
| Facturación anual | Umbral cuantitativo de ingresos anuales — normalmente un piso mínimo, en la moneda que indique el usuario (COP por defecto si no se especifica). | $5.000.000.000 o más |

**Nota sobre Tamaño vs. Número de empleados:** son dos formas de acotar lo
mismo; si el usuario da ambos y son consistentes, se usan juntos. Si son
contradictorios (ej. "Grande" pero "+10 empleados"), se pregunta al usuario
cuál priorizar en vez de asumir.

---

## Regla de obligatoriedad: flexible

Se preguntan siempre los 6 campos, pero **no se bloquea la búsqueda** por un
dato faltante:
- Si el usuario responde un campo con "no sé", "cualquiera", "no aplica" o
  equivalente, ese campo queda sin restricción y la búsqueda continúa sin él.
- Si el usuario deja un campo completamente sin responder tras pedírselo una
  vez, se asume igual que "sin restricción" para ese campo — no se insiste
  más de una vez por campo.
- El único campo que conviene confirmar si falta es **Número de Empresas**,
  porque define cuándo detener la búsqueda; si el usuario no da un número,
  se usa un valor por defecto razonable (10) y se lo comunico explícitamente.

---

## Ejemplo de uso

> **Usuario:** "Necesito empresas constructoras en Bogotá, medianas, con más
> de 100 empleados y facturación de $5.000.000.000 o más. Dame 15."

Se mapea directo a los 6 campos sin necesidad de repetir el formulario:
- Número de Empresas: 15
- Sector: Construcción
- Ubicación: Bogotá
- Tamaño: Mediana
- Número de empleados: +100
- Facturación anual: $5.000.000.000 o más

Si el mensaje inicial del usuario ya trae todos los datos (como en este
ejemplo), no hace falta repetir la pregunta uno por uno — se confirma el
resumen mapeado y se pasa directo a la búsqueda.

---

## Exclusiones estándar (heredadas del ICP)

Ver el detalle completo en [[perfil-usuario]]. Salvo que el usuario diga lo
contrario, se excluyen: gobierno, ONGs, universidades/colegios, y agencias de
staffing o reclutamiento (competencia directa de Campuslands).
