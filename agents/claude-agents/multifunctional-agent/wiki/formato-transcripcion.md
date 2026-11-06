# Formato de la transcripción

Estructura tomada de «hooy-transcription.pdf» (transcripción de una reunión de ~51 min con la Alcaldía de Girón), con el diseño de Campuslands.
La **estructura es la de la referencia, sin cambios**; lo único que se adapta es el diseño.

## Estructura

```
Transcripción de Audio Completo                                    ← título (centrado)

Parte 1                                                            ← una por cada 5 min de audio
[00:00 - 00:02] Hablante 1 (Hombre): ...las cosas de las TIC...
[00:13 - 00:14] Hablante 2 (Hombre): [Asiente] Mm-hmm.
[00:43 - 00:45] Hablante 3 (Gabriela): Sí, está sin nombre.

Parte 2
[00:00 - 00:04] Hablante 1 (Hombre): ...                          ← los tiempos reinician en 00:00
```

- **Partes:** el audio se parte en tramos de 5 minutos (la referencia tiene 11 partes: 10 de 5 min y una de 52 s). Cada parte reinicia el tiempo en `00:00`. Ninguna intervención cruza el corte: el motor la divide ahí.
- **Intervención:** `[inicio - fin] Hablante N (X): texto`. `X` es el **nombre** si el audio lo revela (`Hablante 3 (Gabriela)`); si no, `Hombre` o `Mujer` (estimado por el tono de voz); si tampoco se sabe, solo `Hablante N`.
- **Acotaciones** no verbales entre corchetes y en cursiva: `[Risas]`, `[Asiente]`. Las citas dichas textualmente van en cursiva. No se inventan acotaciones.
- Numeración de hablantes por orden de aparición. Texto literal (regla dura 8).

## Diseño Campuslands (lo que se adapta)

| Elemento | Referencia | Campuslands |
|---|---|---|
| Página | A4 sin membrete | **Plantilla Word de Campuslands** (membrete con logo arriba, dirección abajo), Carta |
| Título | Helvetica 20 negrita, negro azulado | Calibri 22 negrita **azul `0D497B`** con filete verde `5DAC6D` debajo y «Campuslands · Full Service» |
| «Parte N» | Helvetica 14 negrita azul | Calibri 14 negrita azul `0D497B` (estilo Título 1 de Word: aparece en el panel de navegación) |
| Intervención | Marca de tiempo y hablante en negrita negra | Marca de tiempo en **verde `2F7D45`** negrita, hablante en **azul** negrita, texto en `262626` |
| Pie | «Transcripción de Audio Completo … Página N» | «Página N» a la derecha, sobre el pie del membrete |
| Cuadro de datos | no existe | **Añadido**: audio, duración y partes, fecha de transcripción y participantes (se omite con `--sin-ficha`) |

## Entradas que acepta `transcripcion.py`

**`.md`** — el formato de la referencia. Se puede escribir o corregir a mano:

```markdown
<!-- meta: {"audio": "reunion.mp3", "duracion_s": 3051.2, "fecha": "2026-11-06", "parte_s": 300} -->   ← opcional (alimenta el cuadro de datos)
# Transcripción de Audio Completo

## Parte 1

**[00:00 - 00:02] Hablante 1 (Hombre):** ...las cosas de las TIC...

**[00:13 - 00:14] Hablante 2 (Hombre):** *[Asiente]* Mm-hmm.
```

**`.json`** — lo que escribe `transcribir_audio.py` (`segmentos.json`):

```json
{
  "titulo": "Transcripción de Audio Completo", "audio": "reunion.mp3", "duracion_s": 3051.2, "fecha": "2026-11-06", "parte_s": 300,
  "hablantes": {"1": {"nombre": null, "genero": "Hombre"}, "3": {"nombre": "Gabriela", "genero": "Mujer"}},
  "segmentos": [{"inicio": 0.0, "fin": 2.1, "hablante": 1, "texto": "...las cosas de las TIC..."}]
}
```

Los tiempos del `.json` son absolutos (segundos desde el inicio del audio); el constructor los convierte a `mm:ss` relativos a cada parte. Cambiar `--parte-min` re-parte el documento sin volver a transcribir.

## Cómo se construye

`python -X utf8 scripts/transcripcion.py construir <entrada.json|.md> [--salida DIR] [--nombre X] [--titulo "…"] [--parte-min 5] [--sin-ficha] [--sin-pdf]`
→ Word sobre `recursos/plantilla/Plantilla Word - Campuslands.docx` y PDF convertido de ese mismo Word (LibreOffice).
