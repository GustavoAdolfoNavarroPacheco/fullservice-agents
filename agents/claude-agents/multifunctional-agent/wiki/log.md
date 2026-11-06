# Bitácora — Agente Multifuncional

Registro cronológico, de más antiguo a más reciente. Formato de cada entrada: `## [AAAA-MM-DD] <tipo> | <título>` (tipos: `creación`, `facturas`, `transcripción`, `ajuste`, `prueba`).

## [2026-11-06] creación | Agente multifuncional (`/multifunctional-agent`)
Se crea el agente con **dos funcionalidades**, elegidas por el usuario con una pregunta clave al inicio de la sesión:

1. **Unificación de facturas** (`scripts/facturas.py`, banner en `scripts/factura_banner.py`): ordena por la fecha y hora que dice cada recibo y entrega Word + PDF, una factura por hoja. Diseño tomado de «Facturas_28-29_Octubre_2026_Campuslands.docx». El banner queda aislado en un solo archivo porque el usuario lo rediseñará más adelante.
2. **Transcriptor de audio** (`scripts/transcribir_audio.py` + `scripts/transcripcion.py`): transcribe en local (faster-whisper + sherpa-onnx) y entrega Word + PDF con la estructura de «Transcripción de Audio Completo» (hooy-transcription.pdf), con el diseño de Campuslands sobre la plantilla Word.

Decisiones: el motor de audio es **local** por confidencialidad (el audio de una reunión con un cliente no sale del equipo); los audios no se versionan; el agente no puede escuchar, así que la transcripción automática se entrega con la advertencia de que no está verificada de oído. Los archivos de ejemplo del usuario (recibos y la transcripción de la Alcaldía de Girón) **no** se copiaron al repositorio: contienen datos personales y de un cliente; las pruebas del repositorio usan datos sintéticos (`scripts/autoprueba.py`).
Se agrega `/multifunctional-agent` como comando de Claude Code (`.claude/commands/` de esta carpeta y de la raíz del repositorio).

## [2026-11-06] ajuste | Comandos «!»
Se incorporan los **comandos «!»**: órdenes cortas (`!optimize`, `!notime`, `!plan`…) que el agente ejecuta de forma obligatoria, dentro de sus reglas duras. Este agente tiene 33 comandos; la regla común, la tabla de comandos y su significado aquí están en la sección «Comandos» de `CLAUDE.md`. Catálogo completo y decisiones: `resources/comandos/catalogo.md`.

## [2026-11-06] prueba | Motor de audio con una reunión real (primeros 5 min)
Se instalaron `faster-whisper` y `sherpa-onnx` (con permiso del usuario) y se probó la cadena completa con los primeros 5 min de una reunión de ~51 min. Resultado: **funciona de punta a punta**, pero con el modelo `small` la precisión es baja (≈ 49 % de diferencia de palabras frente a la referencia); `large-v3-turbo` mejora la legibilidad y la separación de hablantes (≈ 44 %) y pasa a ser el modelo por defecto; `--sin-vad` no mejoró. Cifras, tiempos y límites en `wiki/motor-transcripcion.md`.
Hallazgos corregidos durante la prueba: `faster-whisper 1.2.1` no abre archivos con `av 19` (se le pasa el arreglo de audio en lugar de la ruta) y la extracción del `.tar.bz2` de modelos avisaba de un cambio en Python 3.14 (se usa `filter="data"`).
Quedó **sin probar** el audio completo de ~51 min (solo se probó un tramo de 5 min).

## [2026-11-06] ajuste | Facturas: plantilla Campuslands, Poppins y banner simétrico
A partir de la revisión del primer ejemplo, el usuario pidió: (1) **plantilla de Campuslands** para el documento de facturas, (2) tipografía **Poppins**, (3) **no indicar la hora** de la factura y (4) un banner **simétrico**, sin la barra superior.
Cambios: banner v2 (una franja de cuatro celdas iguales FACTURA · FECHA · TIPO · PROVEEDOR); el documento se arma sobre `recursos/plantilla/Plantilla Word - Campuslands.docx` y todas las hojas son verticales (un recibo de 2 páginas pasa a ir una hoja por página con «FACTURA (CONT.)» cuando apilado quedaría ilegible); la hora se usa solo para ordenar y las notas automáticas ya no la mencionan; pie `Pág. N/M`; Poppins en `recursos/fuentes/`, **incrustada en el Word** y cargada en LibreOffice para el PDF.
Corregido: LibreOffice añadía 0,125″ de aire a cada lado de las imágenes en línea y el recibo quedaba descentrado respecto del banner (se fijan `distL/R=0` y `effectExtent`). La transcripción **no se tocó** (el usuario la dio por buena).

## [2026-11-06] facturas | Facturas Elizabeth (Google Cloud)
Lote de 3 PDF: facturas 5710137748 (30 sep 2026) y 5739539857 (31 oct 2026) y el comprobante de pagos de Firebase (cargo del 4 nov 2026; el resumen se generó el 6 nov). Ordenadas por fecha; ninguna trae hora (se avisó). Dos PDF de 2 páginas ocupan 2 hojas cada uno (la segunda es el resumen de la factura): 3 facturas, 5 hojas. Fecha del comprobante = fecha del cargo (decisión del agente, anotada en la leyenda). Tipo «Software y nube» (se agrega a la lista de tipos).
