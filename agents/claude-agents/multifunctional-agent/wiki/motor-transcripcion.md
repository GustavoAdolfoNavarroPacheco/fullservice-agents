# Motor de transcripción (local)

Cómo pasa el audio a texto en la funcionalidad 2, qué hay que instalar, cuánto rinde (medido) y dónde falla.
**Todo corre en este equipo**: el audio de una reunión con un cliente no se sube a ningún servicio.

## Cadena

```
audio / video ──ffmpeg──► WAV 16 kHz mono ──faster-whisper──► palabras con tiempos
                                          ──sherpa-onnx──────► tramos «quién habla»  (diarización)
                       unión palabra ↔ hablante ► intervenciones («[mm:ss - mm:ss] Hablante N: texto»)
                       tono de voz (F0)         ► género estimado de cada hablante
                       segmentos.json + transcripcion.md ──transcripcion.py──► Word + PDF Campuslands
```

| Pieza | Qué es | Peso |
|---|---|---|
| **ffmpeg** | Extrae el audio de mp3, mp4, m4a, wav, ogg, webm, mkv… | ya instalado (`winget install Gyan.FFmpeg`) |
| **faster-whisper** | Whisper (OpenAI) optimizado para CPU. Modelos: `small` (≈ 0,5 GB), `medium` (≈ 1,5 GB), **`large-v3-turbo`** (≈ 1,6 GB, el defecto) | `pip install -r scripts/requisitos-audio.txt`; el modelo se baja la primera vez que se usa |
| **sherpa-onnx** | Diarización: segmentación `pyannote 3.0` + huella de voz `3D-Speaker ERes2Net` | ≈ 45 MB, se bajan con `--descargar-modelos` a `recursos/modelos-audio/` (fuera de git) |

Se le pasa a Whisper el arreglo de muestras (no la ruta del archivo) porque su decodificador interno (PyAV) cambia entre versiones y rompió con `av 19`.

## Qué decide el script

- **Intervenciones:** se agrupan palabras del mismo hablante; una pausa > 1,2 s abre una intervención nueva; ninguna pasa de ≈ 28 s (se corta en el siguiente fin de frase); nunca cruza el corte de una parte (5 min).
- **Hablantes pequeños:** uno con menos de max(8 s, 1,5 % de la duración) de voz suele ser ruido o un corte de otro: sus palabras pasan al hablante vecino.
- **Género:** F0 mediana de la voz de cada hablante (autocorrelación sobre sus tramos más largos). `< 155 Hz` → Hombre, `> 175 Hz` → Mujer, en medio → sin género. **Es una estimación**, no un dato.
- **Nombres:** el script nunca los pone; los asigna el agente en la revisión, solo si el audio los revela.

## Rendimiento medido

Prueba del 2026-11-06 con los **primeros 5 min** de una reunión real de ~51 min (sala con varios participantes, audio de sala), en el equipo del usuario, solo CPU, con vocabulario del proyecto. Se contrastó con la transcripción de referencia que aportó el usuario, hecha con otra herramienta.
La «diferencia de palabras» (WER aproximado: palabras distintas / palabras de la referencia, sin tildes ni acotaciones) **no es una medida de error absoluta**: la referencia tampoco es la verdad (trae muletillas y solapamientos que Whisper omite, ≈ 790 palabras frente a ≈ 600). Sirve para comparar modelos entre sí.

| Modelo | Tiempo (5 min de audio, con diarización) | Diferencia de palabras | Observaciones |
|---|---|---|---|
| `small` | ≈ 190 s | ≈ 49 % | Oye mal nombres propios y términos técnicos, inventa palabras («un pesadillo», «las indombras»), pierde frases y confunde hablantes (4 «hablantes» donde hay 3). Sirve de borrador, no de entrega. |
| **`large-v3-turbo`** (por defecto) | ≈ 310 s (≈ 1× la duración del audio) | ≈ 44 % | Frases mucho más legibles y con sentido («leer la oferta», «sin nombres, Gabriela, sin nombres»); separa bien a la anfitriona de la voz masculina dominante (3 hablantes). Aun así necesita revisión: falla en nombres propios («PETI» → «PET») y en cifras. |
| `large-v3-turbo` + `--sin-vad` | ≈ 270 s | ≈ 45 % | Sin mejora medible en esta muestra: se deja el filtro de silencios activado. |

Conclusión: el motor local da un **primer borrador legible**, no una transcripción final. El agente lo revisa (regla dura 8) y lo entrega diciendo que no está verificado de oído. Para una reunión importante conviene escuchar los tramos dudosos o contrastar con otra herramienta.

## Límites que hay que decir siempre

1. El agente **no puede escuchar el audio**: no puede verificar la transcripción de oído. Se entrega como transcripción automática y se sugieren marcas de tiempo para contrastar.
2. Con audio de sala (varias personas hablando a distancia, voces que se pisan) la precisión baja y la diarización mezcla hablantes. Mejora con un micrófono cercano, un solo hablante a la vez y `--hablantes N`.
3. No detecta risas ni gestos (`[Risas]`, `[Asiente]` de la referencia): el motor no los genera y el agente no los inventa.
4. El género es una estimación por tono de voz; los nombres de hablantes son propuestas hasta que el usuario las confirme.

## Qué hacer si el resultado sale flojo

1. Repetir con otro modelo: `--modelo medium` (`small` es más rápido pero peor). El defecto ya es `large-v3-turbo`.
2. Pasar `--vocabulario "nombre1, nombre2, término…"` con los nombres propios y términos del proyecto.
3. Pasar `--hablantes N` si se sabe cuántos participan.
4. Si nada alcanza: transcribir con otra herramienta y entregarle al agente el texto en el formato de la referencia (`.md`); él arma el documento (`wiki/formato-transcripcion.md`).
