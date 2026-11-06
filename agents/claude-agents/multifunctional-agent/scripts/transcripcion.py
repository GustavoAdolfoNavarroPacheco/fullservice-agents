"""Funcionalidad 2 — Transcriptor de audio: del texto transcrito al documento Campuslands (Word + PDF).

Este script NO escucha audio (eso lo hace `transcribir_audio.py`): toma la transcripción ya hecha y la ordena con la
estructura del documento de referencia («Transcripción de Audio Completo»), con el diseño de Campuslands:

    Transcripción de Audio Completo                      ← título
    Parte 1                                              ← una parte por tramo de audio (5 min por defecto);
    [00:00 - 00:02] Hablante 1 (Hombre): texto…             los tiempos reinician en 00:00 en cada parte
    [00:13 - 00:14] Hablante 2 (Hombre): [Asiente] Mm-hmm.
    [00:43 - 00:45] Hablante 3 (Gabriela): …

Entradas aceptadas:
  · un .json de segmentos (lo que escribe transcribir_audio.py; ver wiki/formato-transcripcion.md), o
  · un .md / .txt con el formato de la referencia («## Parte N» y «**[mm:ss - mm:ss] Hablante N (X):** texto»).

Uso (desde la carpeta multifunctional-agent/):
    python -X utf8 scripts/transcripcion.py construir <entrada.json|.md> [--salida DIR] [--nombre X]
                                            [--titulo "…"] [--parte-min 5] [--sin-ficha] [--sin-pdf]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Twips

from comun import (PLANTILLA_CAMPUSLANDS, borde_parrafo, campo, configurar_consola, docx_a_pdf, el, fecha_larga, slug)

# Paleta del membrete de la plantilla Campuslands (la misma que usa el agente de alcances)
AZUL = "0D497B"
VERDE = "5DAC6D"
VERDE_OSCURO = "2F7D45"      # verde con contraste suficiente para texto pequeño
TINTA = "262626"
GRIS = "595959"
TINTE = "EEF3F8"
REGLA = "D5DEE8"
FUENTE = "Calibri"
TITULO_DEFECTO = "Transcripción de Audio Completo"


# ---------------------------------------------------------------- modelo

@dataclass
class Linea:
    ini: str
    fin: str
    etiqueta: str          # «Hablante 1 (Hombre)»
    texto: str


@dataclass
class Parte:
    n: int
    lineas: list[Linea] = field(default_factory=list)


@dataclass
class Modelo:
    titulo: str = TITULO_DEFECTO
    partes: list[Parte] = field(default_factory=list)
    audio: str | None = None
    duracion_s: float | None = None
    fecha: dt.date | None = None
    parte_s: int | None = None
    participantes: list[tuple[str, str]] = field(default_factory=list)   # [(«Hablante 1», «Hombre»)]


def mmss(seg: float, con_horas: bool = False) -> str:
    s = max(0, int(seg))
    if con_horas or s >= 3600:
        return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"
    return f"{s // 60:02d}:{s % 60:02d}"


def duracion_legible(seg: float) -> str:
    s = int(round(seg))
    h, m, ss = s // 3600, s % 3600 // 60, s % 60
    return f"{h} h {m:02d} min {ss:02d} s" if h else f"{m} min {ss:02d} s"


def etiqueta_de(hid, hablantes: dict) -> tuple[str, str]:
    """(«Hablante 3 (Gabriela)», «Gabriela»): nombre si se conoce; si no, el género estimado; si no, solo «Hablante N»."""
    h = hablantes.get(str(hid), {})
    desc = h.get("nombre") or h.get("genero") or ""
    base = f"Hablante {hid}"
    return (f"{base} ({desc})" if desc else base), desc


# ---------------------------------------------------------------- lectura de entradas

_RX_META = re.compile(r"^\s*<!--\s*meta:\s*(\{.*\})\s*-->\s*$")
_RX_PARTE = re.compile(r"^\s*#{1,6}\s*Parte\s+(\d+)\s*$", re.I)
_RX_TITULO = re.compile(r"^\s*#\s+(.+?)\s*$")
_RX_LINEA = re.compile(r"^\s*(?:\*\*)?\\?\[\s*(\d+(?::\d{2}){1,2})\s*[-–]\s*(\d+(?::\d{2}){1,2})\s*\\?\]\s*(.+?):\s*(?:\*\*)?\s*(.*)$")


def _limpia_md(t: str) -> str:
    return t.replace("\\[", "[").replace("\\]", "]").replace("\\*", "*").strip()


def leer_md(ruta: Path) -> Modelo:
    """Lee el formato de la referencia. Las líneas de continuación (sin marca de tiempo) se anexan a la anterior."""
    m = Modelo()
    parte: Parte | None = None
    for crudo in ruta.read_text(encoding="utf-8").splitlines():
        if not crudo.strip():
            continue
        mm = _RX_META.match(crudo)
        if mm:                                           # <!-- meta: {...} --> (lo escribe a_md)
            meta = json.loads(mm[1])
            m.audio, m.duracion_s, m.parte_s = meta.get("audio"), meta.get("duracion_s"), meta.get("parte_s")
            m.fecha = dt.date.fromisoformat(meta["fecha"]) if meta.get("fecha") else None
            continue
        mp = _RX_PARTE.match(crudo)
        if mp:
            parte = Parte(int(mp[1]))
            m.partes.append(parte)
            continue
        ml = _RX_LINEA.match(crudo)
        if ml:
            if parte is None:
                parte = Parte(1)
                m.partes.append(parte)
            etiqueta = _limpia_md(ml[3]).strip("* ")
            parte.lineas.append(Linea(ml[1], ml[2], etiqueta, _limpia_md(ml[4])))
            continue
        mt = _RX_TITULO.match(crudo)
        if mt and not m.partes:
            m.titulo = _limpia_md(mt[1])
            continue
        if parte and parte.lineas:                       # continuación de la línea anterior
            parte.lineas[-1].texto += " " + _limpia_md(crudo)
    if not m.partes:
        raise ValueError(f"No encontré líneas con el formato «[mm:ss - mm:ss] Hablante N (X): texto» en {ruta.name}.")
    vistos: dict[str, str] = {}
    for p in m.partes:
        for ln in p.lineas:
            mh = re.match(r"(Hablante\s+\d+)\s*(?:\((.*)\))?", ln.etiqueta)
            if mh and mh[1] not in vistos:
                vistos[mh[1]] = (mh[2] or "").strip()
    m.participantes = list(vistos.items())
    return m


def leer_json(ruta: Path, parte_min: float | None = None) -> Modelo:
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    parte_s = int((parte_min * 60) if parte_min is not None else datos.get("parte_s", 300))
    hablantes = {str(k): v for k, v in (datos.get("hablantes") or {}).items()}
    m = Modelo(titulo=datos.get("titulo") or TITULO_DEFECTO, audio=datos.get("audio"),
               duracion_s=datos.get("duracion_s"), parte_s=parte_s)
    if datos.get("fecha"):
        m.fecha = dt.date.fromisoformat(datos["fecha"])
    segs = sorted(datos["segmentos"], key=lambda s: (s["inicio"], s.get("fin", 0)))
    if not segs:
        raise ValueError("El JSON no trae segmentos.")
    partes: dict[int, Parte] = {}
    for s in segs:
        texto = (s.get("texto") or "").strip()
        if not texto:
            continue
        idx = int(s["inicio"] // parte_s) if parte_s > 0 else 0
        base = idx * parte_s if parte_s > 0 else 0
        fin = s.get("fin", s["inicio"])
        if parte_s > 0:
            fin = min(fin, base + parte_s)                       # no se muestra un fin posterior al corte de la parte
        et, _ = etiqueta_de(s.get("hablante", 1), hablantes)
        partes.setdefault(idx, Parte(idx + 1)).lineas.append(Linea(mmss(s["inicio"] - base), mmss(max(fin, s["inicio"]) - base), et, texto))
    m.partes = [partes[k] for k in sorted(partes)]
    if parte_s > 0:                                              # numeración continua aunque haya partes sin habla
        for n, p in enumerate(m.partes, 1):
            p.n = n
    usados = sorted({str(s.get("hablante", 1)) for s in segs}, key=lambda x: (len(x), x))
    m.participantes = [(f"Hablante {h}", etiqueta_de(h, hablantes)[1]) for h in usados]
    return m


def a_md(m: Modelo) -> str:
    """Modelo -> markdown con el formato de la referencia (se puede corregir a mano y volver a construir)."""
    meta = {"audio": m.audio, "duracion_s": m.duracion_s, "fecha": m.fecha.isoformat() if m.fecha else None, "parte_s": m.parte_s}
    out = [f"<!-- meta: {json.dumps(meta, ensure_ascii=False)} -->", f"# {m.titulo}", ""]
    for p in m.partes:
        out += [f"## Parte {p.n}", ""]
        for ln in p.lineas:
            out += [f"**[{ln.ini} - {ln.fin}] {ln.etiqueta}:** {ln.texto}", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- documento Word

_RX_INLINE = re.compile(r"\*([^*]+)\*|(\[[^\]]+\])")


def _estilos(doc: Document) -> None:
    def base(est, tam, color=TINTA, negrita=False):
        est.font.name = FUENTE
        est.element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), FUENTE)
        est.font.size, est.font.bold = Pt(tam), negrita
        est.font.color.rgb = RGBColor.from_string(color)
    n = doc.styles["Normal"]
    base(n, 10)
    n.paragraph_format.space_before, n.paragraph_format.space_after, n.paragraph_format.line_spacing = Pt(0), Pt(0), 1.15
    t = doc.styles["Title"]
    base(t, 22, AZUL, True)
    t.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.paragraph_format.space_before, t.paragraph_format.space_after = Pt(0), Pt(4)
    ppr = t.element.get_or_add_pPr()
    for h in ppr.findall(qn("w:pBdr")):
        ppr.remove(h)
    h1 = doc.styles["Heading 1"]
    base(h1, 14, AZUL, True)
    h1.paragraph_format.space_before, h1.paragraph_format.space_after = Pt(16), Pt(6)
    h1.paragraph_format.keep_with_next = True
    ppr = h1.element.get_or_add_pPr()
    for h in ppr.findall(qn("w:numPr")):
        ppr.remove(h)


def _run(par, texto: str, color=TINTA, negrita=False, cursiva=False, tam: float | None = None):
    r = par.add_run(texto)
    r.font.color.rgb = RGBColor.from_string(color)
    r.bold, r.italic = negrita, cursiva
    if tam:
        r.font.size = Pt(tam)
    return r


def _texto_con_estilo(par, texto: str) -> None:
    """Texto de la línea: *cursivas* y [acotaciones] en cursiva, el resto normal. (Los asteriscos no se imprimen.)"""
    pos = 0
    for m in _RX_INLINE.finditer(texto):
        if m.start() > pos:
            _run(par, texto[pos:m.start()])
        _run(par, m[1] if m[1] is not None else m[2], cursiva=True)
        pos = m.end()
    if pos < len(texto):
        _run(par, texto[pos:])


def _pie_pagina(pie) -> None:
    """Número de página «Página N» a la derecha, sobre el pie del membrete."""
    p = pie.paragraphs[0]
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    for x in p._p.findall(qn("w:r")):
        p._p.remove(x)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run("Página ")
    r.font.size, r.font.color.rgb = Pt(8), RGBColor.from_string("7F7F7F")
    campo(p, "PAGE", "1", tam_pt=8, color="7F7F7F")


def _celda(c, relleno=None, ancho=None, borde_inf=REGLA):
    tcpr = c._tc.get_or_add_tcPr()
    if ancho:
        c.width = Twips(ancho)
    if relleno:
        tcpr.append(el("w:shd", w_val="clear", w_color="auto", w_fill=relleno))
    b = el("w:tcBorders")
    for lado in ("top", "left", "right"):
        b.append(el(f"w:{lado}", w_val="nil"))
    b.append(el("w:bottom", w_val="single", w_sz=4, w_space=0, w_color=borde_inf))
    # tcBorders debe ir antes de shd
    shd = tcpr.find(qn("w:shd"))
    (shd.addprevious(b) if shd is not None else tcpr.append(b))
    mar = el("w:tcMar")
    for lado, v in (("top", 60), ("left", 110), ("bottom", 60), ("right", 110)):
        mar.append(el(f"w:{lado}", w_w=v, w_type="dxa"))
    tcpr.append(mar)


def _ficha(doc, m: Modelo, ancho: int) -> None:
    filas = []
    if m.audio:
        filas.append(("Audio", m.audio))
    if m.duracion_s:
        det = duracion_legible(m.duracion_s)
        if m.parte_s:
            det += f" · {len(m.partes)} parte{'s' if len(m.partes) != 1 else ''} de {m.parte_s // 60} min"
        filas.append(("Duración", det))
    if m.fecha:
        filas.append(("Fecha de transcripción", fecha_larga(m.fecha)))
    if m.participantes:
        filas.append(("Participantes", " · ".join(f"{h}" + (f" ({d})" if d else "") for h, d in m.participantes)))
    if not filas:
        return
    t = doc.add_table(rows=len(filas), cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    c1 = 2100
    for i, (k, v) in enumerate(filas):
        a, b = t.rows[i].cells
        _celda(a, TINTE, c1)
        _celda(b, None, ancho - c1)
        pa, pb = a.paragraphs[0], b.paragraphs[0]
        _run(pa, k.upper(), AZUL, True, tam=7.5)
        _run(pb, v, TINTA, False, tam=9)
        for pp in (pa, pb):
            pp.paragraph_format.space_after = Pt(0)
        t.rows[i]._tr.get_or_add_trPr().append(el("w:cantSplit"))
    sp = doc.add_paragraph()
    sp.paragraph_format.space_after = Pt(2)


def construir_docx(m: Modelo, destino: Path, con_ficha: bool = True) -> Path:
    doc = Document(str(PLANTILLA_CAMPUSLANDS))
    cuerpo = doc.element.body
    for h in list(cuerpo):
        if h.tag != qn("w:sectPr"):
            cuerpo.remove(h)
    _estilos(doc)
    sec = doc.sections[0]
    ancho = int(sec.page_width.twips - sec.left_margin.twips - sec.right_margin.twips)
    for pie in (sec.footer, sec.first_page_footer):
        pie.is_linked_to_previous = False
        _pie_pagina(pie)

    t = doc.add_paragraph(m.titulo, style="Title")
    borde_parrafo(t, "bottom", VERDE, sz=12, espacio=6)
    sub = doc.add_paragraph()
    sub.paragraph_format.space_before, sub.paragraph_format.space_after = Pt(6), Pt(8)
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _run(sub, "Campuslands · Full Service", GRIS, tam=9)
    if con_ficha:
        _ficha(doc, m, ancho)

    for parte in m.partes:
        doc.add_paragraph(f"Parte {parte.n}", style="Heading 1")
        for ln in parte.lineas:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(5)
            p.paragraph_format.keep_together = True
            _run(p, f"[{ln.ini} - {ln.fin}] ", VERDE_OSCURO, True)
            _run(p, f"{ln.etiqueta}:", AZUL, True)
            p.add_run(" ")
            _texto_con_estilo(p, ln.texto)

    cp = doc.core_properties
    cp.title, cp.subject, cp.author, cp.last_modified_by, cp.language = m.titulo, "Transcripción de audio", "Campuslands Full Service", "Campuslands Full Service", "es-CO"
    destino.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(destino))
    return destino


# ---------------------------------------------------------------- CLI

def cmd_construir(entrada: Path, salida: Path | None, nombre: str | None, titulo: str | None,
                  parte_min: float | None, sin_ficha: bool, sin_pdf: bool) -> int:
    entrada = entrada.resolve()
    if entrada.suffix.lower() == ".json":
        m = leer_json(entrada, parte_min)
    else:
        m = leer_md(entrada)
        if parte_min is not None:
            print("Aviso: --parte-min solo aplica a entradas .json; el .md ya trae sus partes.")
    if titulo:
        m.titulo = titulo
    if m.fecha is None:
        m.fecha = dt.date.today()
    if salida is None:                       # trabajo/ -> ../salida/ ; en otro caso, junto a la entrada
        salida = entrada.parent.parent / "salida" if entrada.parent.name == "trabajo" else entrada.parent
    salida = salida.resolve()
    nombre = nombre or f"Transcripcion - {slug(Path(m.audio).stem) if m.audio else slug(entrada.stem)}"
    docx = construir_docx(m, salida / f"{nombre}.docx", con_ficha=not sin_ficha)
    n_lin = sum(len(p.lineas) for p in m.partes)
    print(f"✓ {len(m.partes)} partes · {n_lin} intervenciones · {len(m.participantes)} hablantes")
    for h, d in m.participantes:
        print(f"   {h}" + (f" ({d})" if d else ""))
    print(f"Word: {docx}")
    if not sin_pdf:
        print(f"PDF:  {docx_a_pdf(docx)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    configurar_consola()
    ap = argparse.ArgumentParser(description="Transcripción → documento Campuslands (Word + PDF).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("construir")
    b.add_argument("entrada", type=Path)
    b.add_argument("--salida", type=Path)
    b.add_argument("--nombre")
    b.add_argument("--titulo")
    b.add_argument("--parte-min", type=float, help="minutos por parte (solo .json; 0 = sin partes). Por defecto, lo que diga el .json (5).")
    b.add_argument("--sin-ficha", action="store_true", help="omite el cuadro de datos bajo el título")
    b.add_argument("--sin-pdf", action="store_true")
    a = ap.parse_args(argv)
    return cmd_construir(a.entrada, a.salida, a.nombre, a.titulo, a.parte_min, a.sin_ficha, a.sin_pdf)


if __name__ == "__main__":
    sys.exit(main())
