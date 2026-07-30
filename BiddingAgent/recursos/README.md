# recursos/ — Insumos de entrada (SOLO LECTURA)

Fuentes de verdad provistas por el usuario. **El agente nunca edita nada de esta
carpeta.** Para trabajar sobre un modelo de costos, lo copia a
`licitaciones/<slug>/` y edita la copia.

## Documentos por licitación

```
recursos/licitaciones/<slug-licitacion>/
├── <RFP>.pdf                          # 1. Request for Proposal
├── <Aclaraciones y respuestas>.pdf    # 2. Preguntas y respuestas del proceso
├── <Modelo de costos oficial>.xlsx    # 3. Formato de costeo que exige la empresa
└── <Modelo de costos cotizacion>.xlsx # 4. Modelo interno de Campuslands
```

**Los cuatro documentos son obligatorios.** Si falta alguno, el agente pregunta
antes de construir cualquier entregable. Ver `CLAUDE.md` § Insumos que recibo.

Formatos aceptados: PDF, DOCX, XLSX, MD. Se conserva el nombre original del
archivo tal como lo emitió la entidad, para poder citarlo con precisión.

## Recursos de marca y empresa

| Archivo | Uso |
|---|---|
| `Logo Campuslands Horizontal Azul.png` | Logo para documentos de fondo claro (el estándar en entregables licitatorios) |
| `Logo Campuslands  Horizontal Blanco.png` | Logo para fondos oscuros |
| `Logo Campuslands Vertical Azul.png` / `Vertical Blanco.png` | Variantes verticales |
| `isotipo-campuslands.png` | Isotipo |
| `favicon-campuslands.png` | Favicon |
| `Brief Fullservice.pdf` | **Capacidades reales de la empresa.** Fuente única para afirmaciones sobre experiencia, servicios y capacidades en la propuesta |
| `Campuslands_Brandbook2023V2._compressed (1).pdf` | Manual de marca |

## Confidencialidad

`recursos/licitaciones/` contiene documentación de procesos en curso: alcances,
presupuestos oficiales y estrategia de la entidad solicitante. Antes de compartir
este repositorio o subirlo a un remoto, **confirmar con el usuario** si esta carpeta
debe excluirse. No asumir que es seguro por defecto.
