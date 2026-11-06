"""Funcionalidad 2 — Del audio a la transcripción con hablantes (todo local: el audio no sale de este equipo).

    audio/video  ─ffmpeg→  WAV 16 kHz mono  ─faster-whisper→  palabras con tiempos
                                            ─sherpa-onnx→     quién habla en cada momento (diarización)
                                            ─unión→           intervenciones «[mm:ss - mm:ss] Hablante N: texto»
                                            ─tono de voz→     género estimado de cada hablante

Escribe en la carpeta de trabajo:
    segmentos.json       datos completos (lo que lee transcripcion.py)
    transcripcion.md     el mismo contenido en el formato de la referencia, para revisar y corregir a mano

Después el agente revisa el .md (nombres, términos mal oídos) y corre `transcripcion.py construir` para el Word y el PDF.

Uso (desde la carpeta multifunctional-agent/):
    python -X utf8 scripts/transcribir_audio.py <audio> --salida trabajos/transcripciones/<slug>/trabajo
        [--modelo large-v3-turbo|medium|small] [--idioma es] [--hablantes N] [--sin-diarizacion]
        [--vocabulario "Girón, PETI, Campuslands"] [--parte-min 5] [--desde SEG] [--hasta SEG]
        [--descargar-modelos]      descarga los modelos de diarización (una sola vez, ~45 MB) en recursos/modelos-audio/

Requisitos (ver scripts/requisitos-audio.txt):  pip install -r scripts/requisitos-audio.txt   + ffmpeg en el PATH.
"""
from __future__ import annotations

import argparse
import bisect
import datetime as dt
import json
import os
import sys
import tarfile
import tempfile
import time
import urllib.request
import wave
import subprocess
from pathlib import Path

from comun import RAIZ, buscar_ffmpeg, configurar_consola

MODELOS_DIR = RAIZ / "recursos" / "modelos-audio"
URL_SEGMENTACION = "https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-segmentation-models/sherpa-onnx-pyannote-segmentation-3-0.tar.bz2"
URL_EMBEDDING = "https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-recongition-models/3dspeaker_speech_eres2net_base_sv_zh-cn_3dspeaker_16k.onnx"
RUTA_SEGMENTACION = MODELOS_DIR / "sherpa-onnx-pyannote-segmentation-3-0" / "model.onnx"
RUTA_EMBEDDING = MODELOS_DIR / "3dspeaker_speech_eres2net_base_sv_zh-cn_3dspeaker_16k.onnx"

SR = 16000
PAUSA_CORTE_S = 1.2           # una pausa más larga que esto abre una intervención nueva
MAX_INTERVENCION_S = 28.0     # y ninguna intervención pasa de esto (se corta en el siguiente fin de frase)
UMBRAL_HOMBRE_HZ = 155
UMBRAL_MUJER_HZ = 175


# ---------------------------------------------------------------- audio

def extraer_wav(origen: Path, destino: Path, desde: float | None, hasta: float | None) -> float:
    ff = buscar_ffmpeg()
    if not ff:
        raise SystemExit("No encuentro ffmpeg. Instálalo (winget install Gyan.FFmpeg) o define la variable FFMPEG con su ruta.")
    cmd = [ff, "-y", "-loglevel", "error"]
    if desde:
        cmd += ["-ss", str(desde)]
    cmd += ["-i", str(origen)]
    if hasta:
        cmd += ["-t", str(hasta - (desde or 0))]
    cmd += ["-vn", "-ac", "1", "-ar", str(SR), "-c:a", "pcm_s16le", str(destino)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not destino.exists():
        raise SystemExit(f"ffmpeg no pudo leer el audio:\n{r.stderr}")
    with wave.open(str(destino)) as w:
        return w.getnframes() / w.getframerate()


def leer_muestras(wav: Path):
    import numpy as np
    with wave.open(str(wav)) as w:
        crudo = w.readframes(w.getnframes())
    return np.frombuffer(crudo, dtype=np.int16).astype(np.float32) / 32768.0


# ---------------------------------------------------------------- transcripción (faster-whisper)

def transcribir(muestras, modelo: str, idioma: str, vocabulario: str | None, duracion: float, vad: bool = True):
    """`muestras`: audio mono 16 kHz como arreglo float32. Se le pasa el arreglo (no la ruta) a faster-whisper para no depender de
    su decodificador interno (PyAV), que cambia entre versiones."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        raise SystemExit("Falta faster-whisper. Ejecuta:  pip install -r scripts/requisitos-audio.txt")
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    print(f"Cargando el modelo «{modelo}» (la primera vez lo descarga)…", flush=True)
    m = WhisperModel(modelo, device="cpu", compute_type="int8")
    prompt = f"Vocabulario de la reunión: {vocabulario}." if vocabulario else None
    segmentos, _ = m.transcribe(muestras, language=idioma, vad_filter=vad, word_timestamps=True, beam_size=5,
                                condition_on_previous_text=False, initial_prompt=prompt)
    palabras, ultimo = [], time.time()
    for s in segmentos:
        for w in (s.words or []):
            palabras.append((float(w.start), float(w.end), w.word))
        if time.time() - ultimo > 20:
            print(f"  transcrito hasta {s.end / 60:5.1f} de {duracion / 60:.1f} min", flush=True)
            ultimo = time.time()
    print(f"Transcripción lista: {len(palabras)} palabras.", flush=True)
    return palabras


# ---------------------------------------------------------------- diarización (sherpa-onnx)

def _descargar(url: str, destino: Path) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    print(f"  descargando {url.rsplit('/', 1)[-1]} …", flush=True)
    urllib.request.urlretrieve(url, destino)


def descargar_modelos() -> None:
    """Modelos de diarización (segmentación pyannote + huella de voz). Solo se llama con --descargar-modelos."""
    if not RUTA_SEGMENTACION.exists():
        tmp = MODELOS_DIR / "segmentacion.tar.bz2"
        _descargar(URL_SEGMENTACION, tmp)
        with tarfile.open(tmp) as t:
            try:
                t.extractall(MODELOS_DIR, filter="data")
            except TypeError:                      # Python < 3.12 no tiene `filter`
                t.extractall(MODELOS_DIR)
        tmp.unlink(missing_ok=True)
    if not RUTA_EMBEDDING.exists():
        _descargar(URL_EMBEDDING, RUTA_EMBEDDING)
    print("Modelos de diarización listos en", MODELOS_DIR)


def diarizar(muestras, n_hablantes: int | None, umbral: float = 0.5):
    """[(inicio, fin, hablante_int)] ordenado por inicio, o None si no se puede diarizar."""
    try:
        import sherpa_onnx
    except ImportError:
        print("⚠ sherpa-onnx no está instalado: no se separarán los hablantes.", flush=True)
        return None
    if not (RUTA_SEGMENTACION.exists() and RUTA_EMBEDDING.exists()):
        print("⚠ Faltan los modelos de diarización: ejecuta con --descargar-modelos (una vez). No se separarán los hablantes.", flush=True)
        return None
    hilos = max(1, (os.cpu_count() or 4) - 1)
    cfg = sherpa_onnx.OfflineSpeakerDiarizationConfig(
        segmentation=sherpa_onnx.OfflineSpeakerSegmentationModelConfig(
            pyannote=sherpa_onnx.OfflineSpeakerSegmentationPyannoteModelConfig(model=str(RUTA_SEGMENTACION)), num_threads=hilos),
        embedding=sherpa_onnx.SpeakerEmbeddingExtractorConfig(model=str(RUTA_EMBEDDING), num_threads=hilos),
        clustering=sherpa_onnx.FastClusteringConfig(num_clusters=n_hablantes or -1, threshold=umbral),
        min_duration_on=0.3, min_duration_off=0.5)
    if not cfg.validate():
        print("⚠ Configuración de diarización inválida: no se separarán los hablantes.", flush=True)
        return None
    sd = sherpa_onnx.OfflineSpeakerDiarization(cfg)
    ultimo = [time.time()]

    def progreso(hechos, total):
        if time.time() - ultimo[0] > 20:
            print(f"  diarizando… {100 * hechos / max(total, 1):3.0f} %", flush=True)
            ultimo[0] = time.time()
        return 0
    print("Separando hablantes…", flush=True)
    res = sd.process(muestras, callback=progreso).sort_by_start_time()
    return [(float(s.start), float(s.end), int(s.speaker)) for s in res]


def _hablante_en(t: float, tramos, inicios) -> int | None:
    """Hablante en el instante t; si cae en un hueco, el del tramo más cercano."""
    i = bisect.bisect_right(inicios, t) - 1
    if i >= 0 and t <= tramos[i][1]:
        return tramos[i][2]
    candidatos = [tramos[j] for j in (i, i + 1) if 0 <= j < len(tramos)]
    if not candidatos:
        return None
    return min(candidatos, key=lambda s: min(abs(t - s[0]), abs(t - s[1])))[2]


# ---------------------------------------------------------------- unión palabras + hablantes

def _absorber_menores(asign: list[int | None], palabras, minimo_s: float) -> list[int | None]:
    """Un «hablante» con muy poca voz suele ser ruido o un corte de otro: se le asigna el hablante vecino."""
    tiempo: dict[int, float] = {}
    for a, (ini, fin, _) in zip(asign, palabras):
        if a is not None:
            tiempo[a] = tiempo.get(a, 0) + (fin - ini)
    menores = {h for h, t in tiempo.items() if t < minimo_s}
    if not menores or len(menores) == len(tiempo):
        return asign
    res = list(asign)
    for i, a in enumerate(res):
        if a in menores:
            vecino = next((res[j] for j in list(range(i - 1, -1, -1)) + list(range(i + 1, len(res))) if res[j] not in menores and res[j] is not None), None)
            res[i] = vecino
    return res


def armar_intervenciones(palabras, tramos, parte_s: int, minimo_hablante_s: float):
    """Devuelve (intervenciones, ids_ordenados). Cada intervención: dict(inicio, fin, hablante, texto)."""
    if tramos:
        inicios = [t[0] for t in tramos]
        asign = [_hablante_en((a + b) / 2, tramos, inicios) for a, b, _ in palabras]
        asign = _absorber_menores(asign, palabras, minimo_hablante_s)
    else:
        asign = [0] * len(palabras)
    previo = 0
    for i, a in enumerate(asign):                       # huecos sin hablante: el anterior
        if a is None:
            asign[i] = previo
        previo = asign[i]
    orden: dict[int, int] = {}                          # renumera 1..N por orden de aparición
    for a in asign:
        orden.setdefault(a, len(orden) + 1)

    res, cur = [], None
    for (ini, fin, txt), a in zip(palabras, asign):
        h = orden[a]
        frontera = parte_s > 0 and cur is not None and int(ini // parte_s) != int(cur["inicio"] // parte_s)
        if cur is not None and not frontera and h == cur["hablante"]:
            largo = fin - cur["inicio"] > MAX_INTERVENCION_S and cur["texto"].rstrip().endswith((".", "?", "!", "…"))
            if ini - cur["fin"] <= PAUSA_CORTE_S and not largo:
                cur["texto"] += txt
                cur["fin"] = fin
                continue
        if cur:
            res.append(cur)
        cur = {"inicio": ini, "fin": fin, "hablante": h, "texto": txt}
    if cur:
        res.append(cur)
    for r in res:
        r["texto"] = r["texto"].strip()
        r["inicio"], r["fin"] = round(r["inicio"], 2), round(r["fin"], 2)
    return [r for r in res if r["texto"]], sorted(set(orden.values())), orden


# ---------------------------------------------------------------- género estimado (tono de voz)

def f0_mediana(muestras, intervalos: list[tuple[float, float]], max_s: float = 90.0) -> float | None:
    """Frecuencia fundamental mediana (Hz) de la voz en los intervalos dados (autocorrelación por tramos de 40 ms)."""
    import numpy as np
    tramo, salto = int(0.04 * SR), int(0.01 * SR)
    lmin, lmax = int(SR / 400), int(SR / 60)
    usados, valores = 0.0, []
    for ini, fin in sorted(intervalos, key=lambda x: x[0] - x[1]):          # primero los más largos
        if usados >= max_s:
            break
        x = muestras[int(ini * SR):int(fin * SR)]
        usados += fin - ini
        for k in range(0, len(x) - tramo, salto * 2):
            f = x[k:k + tramo]
            f = f - f.mean()
            e = float(np.dot(f, f))
            if e / tramo < 1e-5:                           # silencio
                continue
            n = 1 << (2 * tramo - 1).bit_length()
            ac = np.fft.irfft(np.abs(np.fft.rfft(f, n)) ** 2)[:lmax + 1]
            ac = ac / (ac[0] + 1e-9)
            pico = lmin + int(np.argmax(ac[lmin:lmax]))
            if ac[pico] > 0.45:
                valores.append(SR / pico)
    return float(np.median(valores)) if len(valores) >= 20 else None


def genero_estimado(f0: float | None) -> str | None:
    if f0 is None:
        return None
    if f0 < UMBRAL_HOMBRE_HZ:
        return "Hombre"
    if f0 > UMBRAL_MUJER_HZ:
        return "Mujer"
    return None


# ---------------------------------------------------------------- salida

def main(argv: list[str] | None = None) -> int:
    configurar_consola()
    ap = argparse.ArgumentParser(description="Audio → transcripción con hablantes (local).")
    ap.add_argument("audio", type=Path, nargs="?")
    ap.add_argument("--salida", type=Path, help="carpeta de trabajo (por defecto, junto al audio)")
    ap.add_argument("--modelo", default="large-v3-turbo", help="large-v3-turbo (defecto) · medium · small · base · tiny")
    ap.add_argument("--idioma", default="es")
    ap.add_argument("--hablantes", type=int, help="número de hablantes, si se conoce (mejora la separación)")
    ap.add_argument("--umbral", type=float, default=0.5, help="umbral de agrupación de voces sin --hablantes (más alto = menos hablantes)")
    ap.add_argument("--sin-diarizacion", action="store_true")
    ap.add_argument("--sin-vad", action="store_true", help="no descarta los silencios antes de transcribir (en la prueba no mejoró el resultado; riesgo de frases inventadas en silencios)")
    ap.add_argument("--vocabulario", help="nombres propios y términos separados por comas (ayudan a escribirlos bien)")
    ap.add_argument("--parte-min", type=float, default=5.0, help="minutos por parte del documento (defecto 5; 0 = sin partes)")
    ap.add_argument("--desde", type=float, help="segundo inicial (para probar con un tramo)")
    ap.add_argument("--hasta", type=float, help="segundo final")
    ap.add_argument("--descargar-modelos", action="store_true", help="descarga los modelos de diarización y termina si no se da audio")
    a = ap.parse_args(argv)

    if a.descargar_modelos:
        descargar_modelos()
        if not a.audio:
            return 0
    if not a.audio:
        ap.error("falta el archivo de audio")
    audio = a.audio.resolve()
    if not audio.exists():
        raise SystemExit(f"No existe {audio}")
    salida = (a.salida or audio.parent).resolve()
    salida.mkdir(parents=True, exist_ok=True)
    parte_s = int(a.parte_min * 60)

    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "audio16k.wav"
        dur = extraer_wav(audio, wav, a.desde, a.hasta)
        print(f"Audio: {audio.name} · {dur / 60:.1f} min", flush=True)
        t0 = time.time()
        muestras = leer_muestras(wav)
        palabras = transcribir(muestras, a.modelo, a.idioma, a.vocabulario, dur, vad=not a.sin_vad)
        if not palabras:
            raise SystemExit("No se detectó habla en el audio.")
        tramos = None if a.sin_diarizacion else diarizar(muestras, a.hablantes, a.umbral)
        desplaz = a.desde or 0.0
        minimo = max(8.0, 0.015 * dur)
        inter, ids, orden = armar_intervenciones(palabras, tramos, parte_s, minimo)

        hablantes = {}
        for h in ids:
            if tramos:
                ints = [(i["inicio"], i["fin"]) for i in inter if i["hablante"] == h]
                f0 = f0_mediana(muestras, ints)
            else:
                f0 = None
            hablantes[str(h)] = {"nombre": None, "genero": genero_estimado(f0), "f0_hz": round(f0) if f0 else None}
        for i in inter:                                                         # tiempos absolutos si se transcribió un tramo
            i["inicio"], i["fin"] = round(i["inicio"] + desplaz, 2), round(i["fin"] + desplaz, 2)

    avisos = []
    if tramos is None:
        avisos.append("Sin separación de hablantes: todo figura como «Hablante 1». Asignar los turnos a mano (o repetir con diarización).")
    if any(v["genero"] for v in hablantes.values()):
        avisos.append("El género (Hombre/Mujer) es una ESTIMACIÓN por el tono de voz: confirmar con quien conozca a los participantes.")
    datos = {
        "titulo": "Transcripción de Audio Completo", "audio": audio.name, "duracion_s": round(dur + desplaz, 1),
        "fecha": dt.date.today().isoformat(), "parte_s": parte_s,
        "motor": {"transcripcion": f"faster-whisper ({a.modelo})", "diarizacion": "sherpa-onnx (pyannote 3.0 + 3D-Speaker)" if tramos else "ninguna",
                  "tiempo_proceso_s": round(time.time() - t0)},
        "avisos": avisos, "hablantes": hablantes, "segmentos": inter,
    }
    (salida / "segmentos.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")

    import transcripcion
    modelo_doc = transcripcion.leer_json(salida / "segmentos.json")
    (salida / "transcripcion.md").write_text(transcripcion.a_md(modelo_doc), encoding="utf-8")

    print(f"\n✓ {len(inter)} intervenciones · {len(ids)} hablantes · {len(modelo_doc.partes)} partes · {datos['motor']['tiempo_proceso_s']} s de proceso")
    for h in ids:
        v = hablantes[str(h)]
        print(f"   Hablante {h}: género estimado={v['genero'] or 'no determinado'}" + (f" (F0≈{v['f0_hz']} Hz)" if v["f0_hz"] else ""))
    for av in avisos:
        print("⚠", av)
    print(f"\nsegmentos.json y transcripcion.md en {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
