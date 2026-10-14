# Marca Campuslands — Entregables Licitatorios

Identidad visual y tono editorial de los entregables de este agente.

> **Regla que manda sobre todo lo demás:** si el RFP o las aclaraciones definen un
> formato obligatorio para la propuesta (plantilla, tipografía, estructura de
> secciones, foliado, formato de archivo), **ese formato manda** y este documento
> se subordina. Incumplir un requisito de forma puede descalificar una propuesta
> técnicamente correcta.

---

## 1. Tono editorial

Formal, técnico y verificable. El lector es un comité evaluador que califica con
una rúbrica, no un cliente en una reunión comercial.

- **Preciso antes que elegante.** Cada afirmación debe poder rastrearse a un
  documento.
- **Sin lenguaje de marketing vacío.** Nada de "solución de clase mundial",
  "sinergias" o superlativos sin respaldo.
- **Sin promesas no respaldadas.** No se afirma una capacidad, certificación o
  experiencia que no esté en `recursos/Brief Fullservice.pdf` o confirmada por el
  usuario.
- **Cifras con fuente.** Toda métrica lleva su origen; si no lo tiene, no va.
- **Vocabulario del RFP.** Se usan los mismos términos que la empresa solicitante
  emplea en sus documentos: facilita al evaluador encontrar lo que busca.

---

## 2. Paleta (obligatoria, colores exactos de marca)

| Token | Hex | Uso |
|---|---|---|
| `--navy` | `#152F5E` | Encabezados de tabla, bandas de total, títulos, footer |
| `--azul-cielo` | `#418BF3` | Bandas de módulo, acentos, eyebrow |
| `--blanco` | `#FFFFFF` | Fondo de página y de filas de contenido |
| `--gris-linea` | `#D6DCE5` | Líneas delgadas del grid (~0.5pt) |
| `--gris-texto` | `#5B6B84` | Texto secundario y detalle técnico |

Paleta clara sobre fondo blanco. **No se usa la paleta oscura con gradientes**
(referencia de marca general de Campuslands, no aplicable a documentos
licitatorios).

## 3. Uso de logotipos

- **Campuslands:** `Logo Campuslands Horizontal Azul.png` sobre fondo claro
  (variante `Blanco` solo si hay fondo oscuro). Arriba a la izquierda.
- **Entidad solicitante:** su logo se usa **solo si el RFP lo autoriza o lo exige**.
  Muchos procesos prohíben el uso de la marca de la entidad en documentos del
  proponente.

## 4. Layout de documentos y tablas

- Tablas con **grid completo**: líneas delgadas grises (`--gris-linea`, ~0.5pt)
  entre filas **y** entre columnas, tipo hoja de cálculo.
- Encabezado de tabla: fondo `--navy`, texto blanco.
- Banda de módulo: fondo `--azul-cielo`, texto blanco.
- Filas de contenido: fondo blanco, texto en navy/gris.
- Fila de total: fondo `--navy`, texto blanco.
- Barra superior de cada página en los azules de marca.
- **Foliado obligatorio** (`Página X de Y`) — muchos procesos lo exigen.
- Tabla de contenido en propuestas de más de ~10 páginas.

## 5. Convenciones en los XLSX

Aplicables a la matriz de cumplimiento, la estimación de horas y el análisis de IA:

- **Fuente Arial**, con jerarquía explícita: 11 bold para encabezados de módulo,
  10 bold para nombres de funcionalidad, 10 regular para detalle. Se especifica
  siempre de forma explícita, no se hereda de la plantilla.
- Encabezados de columna con relleno `--navy` y texto blanco.
- Números con separador de miles y sin decimales innecesarios; monedas con su
  símbolo y código (`COP`, `USD`) declarados.
- **Confidencialidad:** al copiar una plantilla de costeo que contenga hojas de
  otros clientes o procesos, **se eliminan esas hojas** antes de trabajar y antes
  de entregar. La hoja de trabajo se renombra con el identificador de la
  licitación.

## 6. Nomenclatura de archivos

```
licitaciones/<slug-licitacion>/
├── 00 - Analisis Documental.md
├── 01 - Matriz de Cumplimiento.xlsx
├── 02 - Propuesta Tecnica.pdf
├── 03 - Estimacion de Horas.xlsx
├── 04 - Consideraciones Tecnicas.md
├── 05 - Analisis IA y Tokens.xlsx        (solo si se requiere IA)
├── 06 - Modelo de Costos Oficial.xlsx
├── 07 - Modelo de Costos Cotizacion.xlsx
└── verificacion-cruzada.md
```

- El prefijo numérico fija el orden de lectura.
- Si el RFP exige nombres de archivo específicos para la radicación, se generan
  **copias con el nombre exigido** y se conserva la numeración interna para
  trabajo.
- Revisiones antes de la radicación: sufijo `(v2)`, `(v3)`. Se conserva la versión
  anterior hasta que la nueva se confirme como definitiva.
