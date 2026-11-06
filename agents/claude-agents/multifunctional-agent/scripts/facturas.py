"""Funcionalidad 1 — Unificación de facturas.

Recibe varias facturas/recibos (PDF o imagen), las ordena cronológicamente según lo que dice CADA RECIBO (no el
nombre del archivo) y entrega un único Word y un único PDF sobre la plantilla de Campuslands (membrete, tipografía
Poppins): una factura por hoja vertical, cada una bajo el banner simétrico (ver `factura_banner.py`), con pie «Página N de M».
La hora se usa para ordenar pero NO se imprime en el documento.

Uso (desde la carpeta multifunctional-agent/):

    python -X utf8 scripts/facturas.py inspeccionar trabajos/facturas/<lote>
        Lee <lote>/entrada/, detecta fecha, hora, proveedor y tipo en el texto de cada recibo y escribe el BORRADOR
        <lote>/manifiesto.json. Lo detectado es una sugerencia: el agente (o la persona) lo confirma mirando cada recibo.

    python -X utf8 scripts/facturas.py construir trabajos/facturas/<lote> [--nombre Facturas_X] [--sin-pdf]
        Lee <lote>/manifiesto.json, ordena, y escribe <lote>/salida/<nombre>.docx y .pdf. Verifica que cada factura
        quede en una sola hoja y que el PDF tenga tantas páginas como hojas.

Manifiesto (un objeto por factura; las rutas son relativas a <lote>/entrada/):
    {"archivo": "recibo.pdf", "fecha": "2026-10-28", "hora": "13:47", "proveedor": "inDrive",
     "tipo": "Transporte", "nota": ""}
    «fecha» es obligatoria; «hora» puede ser null (la factura se ordena al final de su día y se avisa).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import tempfile
from pathlib import Path

import fitz  # PyMuPDF
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Emu, Pt, RGBColor
from PIL import Image, ImageOps

from comun import (PLANTILLA_CAMPUSLANDS, campo, configurar_consola, docx_a_pdf, el, incrustar_fuente, paginas_pdf, rango_fechas,
                   fecha_larga, hora_12h, MESES)
from factura_banner import DatosFactura, agregar_banner

EXT_PDF = {".pdf"}
EXT_IMG = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff", ".gif"}

# Reserva vertical por hoja (twips) para banner + espaciador + leyenda + holgura; el recibo ocupa el resto del área útil de la plantilla.
RESERVA_VERTICAL_TW = 1900
DPI_RENDER = 170
GRIS = "7F7F7F"
FUENTE = "Poppins"

# ---------------------------------------------------------------- detección en el texto

_MES_NOMBRES = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "setiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12,
    "ene": 1, "abr": 4, "ago": 8, "dic": 12,
}
_MES_RE = "|".join(sorted(_MES_NOMBRES, key=len, reverse=True))
_FECHAS = [
    # October 28, 2026 · Oct 28 2026
    (re.compile(rf"\b({_MES_RE})\.?\s+(\d{{1,2}})(?:st|nd|rd|th)?,?\s+(20\d{{2}})\b", re.I), lambda m: (int(m[3]), _MES_NOMBRES[m[1].lower()], int(m[2]))),
    # 29 Oct 2026 · 29 de octubre de 2026 · 29-oct-2026
    (re.compile(rf"\b(\d{{1,2}})[\s\-/]+(?:de\s+)?({_MES_RE})\.?,?[\s\-/]+(?:de\s+)?(20\d{{2}})\b", re.I), lambda m: (int(m[3]), _MES_NOMBRES[m[2].lower()], int(m[1]))),
    # 2026-10-28
    (re.compile(r"\b(20\d{2})[/\-.](\d{1,2})[/\-.](\d{1,2})\b"), lambda m: (int(m[1]), int(m[2]), int(m[3]))),
    # 28/10/2026 (día primero: así se escribe en Colombia)
    (re.compile(r"\b(\d{1,2})[/\-.](\d{1,2})[/\-.](20\d{2})\b"), lambda m: (int(m[3]), int(m[2]), int(m[1]))),
]
_HORA_12 = re.compile(r"\b(\d{1,2}):(\d{2})(?::\d{2})?\s*([AaPp])\.?\s?[Mm]\b\.?")
_HORA_24 = re.compile(r"\b([01]?\d|2[0-3]):([0-5]\d)(?::[0-5]\d)?\b(?!\s*[AaPp]\.?\s?[Mm])")
_CLAVE_HORA = re.compile(r"(start\s*time|hora\s*(de)?\s*(inicio|salida|emisi[oó]n)?|time|hora|inicio)\W{0,6}$", re.I)

# proveedor -> (nombre, tipo). Solo lo que se reconoce con seguridad; lo demás lo completa el agente mirando el recibo.
_PROVEEDORES = [
    (re.compile(r"\bindrive\b|\bindriver\b", re.I), ("inDrive", "Transporte")),
    (re.compile(r"\buber\b", re.I), ("Uber", "Transporte")),
    (re.compile(r"\bdidi\b", re.I), ("DiDi", "Transporte")),
    (re.compile(r"\bcabify\b", re.I), ("Cabify", "Transporte")),
    (re.compile(r"\bbolt\b", re.I), ("Bolt", "Transporte")),
    (re.compile(r"\brappi\b", re.I), ("Rappi", None)),
]
# pistas en el nombre del archivo: 28102026 · 13h31m  (se usan SOLO para avisar de discrepancias)
_NOMBRE_FECHA = re.compile(r"(?<!\d)(\d{2})(\d{2})(20\d{2})(?!\d)")
_NOMBRE_HORA = re.compile(r"(?<!\d)(\d{1,2})h(\d{2})m?\b", re.I)


def _fechas_en(texto: str) -> list[tuple[int, dt.date]]:
    """[(posición, fecha)] en orden de aparición, sin repetidos ni fechas imposibles."""
    out = []
    for rx, conv in _FECHAS:
        for m in rx.finditer(texto):
            try:
                a, me, d = conv(m)
                out.append((m.start(), dt.date(a, me, d)))
            except ValueError:
                pass
    out.sort()
    vistos, res = set(), []
    for pos, f in out:
        if f not in vistos:
            vistos.add(f)
            res.append((pos, f))
    return res


def _horas_en(texto: str) -> list[tuple[int, dt.time, str]]:
    """[(posición, hora, texto_original)]."""
    out = []
    for m in _HORA_12.finditer(texto):
        h, mi, ap = int(m[1]), int(m[2]), m[3].lower()
        if 1 <= h <= 12:
            out.append((m.start(), dt.time(h % 12 + (12 if ap == "p" else 0), mi), m[0].strip()))
    ocupados = {p for p, _, _ in out}
    for m in _HORA_24.finditer(texto):
        if m.start() not in ocupados:
            out.append((m.start(), dt.time(int(m[1]), int(m[2])), m[0].strip()))
    out.sort()
    return out


def _sugerir_hora(texto: str, pos_fecha: int | None, horas) -> dt.time | None:
    if not horas:
        return None
    for pos, h, _ in horas:                                   # una hora precedida de «Start Time», «Hora»…
        if _CLAVE_HORA.search(texto[max(0, pos - 30):pos]):
            return h
    if pos_fecha is not None:
        for pos, h, _ in horas:                               # la primera después de la fecha
            if pos >= pos_fecha:
                return h
    return horas[0][1]


def _pistas_nombre(nombre: str) -> tuple[dt.date | None, dt.time | None]:
    fecha = hora = None
    m = _NOMBRE_FECHA.search(nombre)
    if m:
        try:
            fecha = dt.date(int(m[3]), int(m[2]), int(m[1]))
        except ValueError:
            pass
    m = _NOMBRE_HORA.search(nombre)
    if m and int(m[1]) < 24 and int(m[2]) < 60:
        hora = dt.time(int(m[1]), int(m[2]))
    return fecha, hora


def texto_de(ruta: Path) -> tuple[str, int]:
    """(texto, nº de páginas). Las imágenes y los PDF escaneados no traen texto: el agente debe leerlos a la vista."""
    if ruta.suffix.lower() in EXT_PDF:
        with fitz.open(str(ruta)) as d:
            return "\n".join(p.get_text() for p in d), d.page_count
    return "", 1


def sugerir(ruta: Path) -> dict:
    texto, paginas = texto_de(ruta)
    fechas = _fechas_en(texto)
    horas = _horas_en(texto)
    pos_f, fecha = (fechas[0] if fechas else (None, None))
    hora = _sugerir_hora(texto, pos_f, horas)
    proveedor = tipo = None
    for rx, (nom, tp) in _PROVEEDORES:
        if rx.search(texto) or rx.search(ruta.stem):
            proveedor, tipo = nom, tp
            break
    avisos = []
    if not texto.strip():
        avisos.append("Sin texto extraíble (imagen o escaneo): abre el archivo con Read y completa fecha, hora, proveedor y tipo a la vista.")
    elif not fecha:
        avisos.append("No encontré una fecha en el texto: léela a la vista.")
    if len(fechas) > 1:
        avisos.append("Hay varias fechas en el recibo (" + ", ".join(f.isoformat() for _, f in fechas) + "): confirma cuál es la de la factura.")
    nf, nh = _pistas_nombre(ruta.stem)
    if (nf and fecha and nf != fecha) or (nh and hora and nh != hora):
        avisos.append(f"El nombre del archivo sugiere {nf.isoformat() if nf else '—'} {nh.strftime('%H:%M') if nh else '—'}, "
                      f"pero el recibo dice {fecha.isoformat() if fecha else '—'} {hora.strftime('%H:%M') if hora else '—'}: manda el recibo.")
    return {
        "archivo": ruta.name, "fecha": fecha.isoformat() if fecha else None,
        "hora": hora.strftime("%H:%M") if hora else None, "proveedor": proveedor, "tipo": tipo, "nota": "",
        "paginas": paginas,
        "_deteccion": {"fechas": [f.isoformat() for _, f in fechas], "horas": [t for _, _, t in horas][:8], "avisos": avisos},
    }


# ---------------------------------------------------------------- manifiesto

def _rutas_lote(lote: Path) -> tuple[Path, Path, Path]:
    lote = lote.resolve()
    return lote / "entrada", lote / "manifiesto.json", lote / "salida"


def cmd_inspeccionar(lote: Path) -> int:
    entrada, manif, _ = _rutas_lote(lote)
    if not entrada.is_dir():
        print(f"No existe {entrada}. Crea la carpeta y copia ahí las facturas.")
        return 1
    archivos = sorted(p for p in entrada.iterdir() if p.suffix.lower() in EXT_PDF | EXT_IMG)
    if not archivos:
        print(f"No hay PDF ni imágenes en {entrada}.")
        return 1
    previo = {}
    if manif.exists():                                          # no pisar lo ya confirmado
        try:
            previo = {f["archivo"]: f for f in json.loads(manif.read_text(encoding="utf-8")).get("facturas", [])}
        except Exception:
            pass
    facturas = []
    for a in archivos:
        s = sugerir(a)
        if a.name in previo:
            s = {**s, **{k: v for k, v in previo[a.name].items() if not k.startswith("_")}}
        facturas.append(s)
    datos = {"titulo": "Facturas", "facturas": facturas}
    manif.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Borrador: {manif}\n")
    for f in facturas:
        print(f"· {f['archivo']}  ({f['paginas']} pág.)")
        print(f"    fecha={f['fecha']}  hora={f['hora']}  proveedor={f['proveedor']}  tipo={f['tipo']}")
        for av in f["_deteccion"]["avisos"]:
            print(f"    ⚠ {av}")
    print("\nSiguiente paso: confirma cada dato mirando el recibo (Read), corrige el manifiesto y ejecuta «construir».")
    return 0


def _cargar(manif: Path) -> tuple[dict, list[dict]]:
    datos = json.loads(manif.read_text(encoding="utf-8"))
    return datos, datos["facturas"]


def _normalizar(f: dict, entrada: Path) -> dict:
    """Valida una entrada del manifiesto y la deja tipada. Lanza ValueError con un mensaje claro."""
    nombre = f.get("archivo")
    if not nombre:
        raise ValueError("Hay una factura sin «archivo».")
    ruta = entrada / nombre
    if not ruta.exists():
        raise ValueError(f"No existe {ruta}.")
    if not f.get("fecha"):
        raise ValueError(f"«{nombre}»: falta la fecha. No la invento: léela del recibo y complétala en el manifiesto.")
    try:
        fecha = dt.date.fromisoformat(f["fecha"])
    except ValueError:
        raise ValueError(f"«{nombre}»: fecha «{f['fecha']}» inválida (usa AAAA-MM-DD).")
    hora = None
    if f.get("hora"):
        try:
            hh, mm = f["hora"].split(":")[:2]
            hora = dt.time(int(hh), int(mm))
        except ValueError:
            raise ValueError(f"«{nombre}»: hora «{f['hora']}» inválida (usa HH:MM en 24 h).")
    nota = (f.get("nota") or "").strip()
    if not nota:                                                # aviso automático (sin horas: la hora no se imprime) si el nombre contradice al recibo
        nf, nh = _pistas_nombre(Path(nombre).stem)
        if (nh and hora and nh != hora) or (nf and nf != fecha):
            nota = "El nombre del archivo no coincide con lo que dice el recibo; se usaron los datos del recibo."
    return {"ruta": ruta, "archivo": nombre, "fecha": fecha, "hora": hora, "tipo": (f.get("tipo") or "").strip(),
            "proveedor": (f.get("proveedor") or "").strip(), "nota": nota}


def ordenar(items: list[dict]) -> list[dict]:
    """Cronológico por fecha y hora del recibo. Sin hora: al final de su día, por nombre de archivo."""
    return sorted(items, key=lambda x: (x["fecha"], x["hora"] is None, x["hora"] or dt.time(0, 0), x["archivo"].lower()))


# ---------------------------------------------------------------- imágenes de las facturas

def _renderizar(ruta: Path) -> tuple[list[Image.Image], bool]:
    """Páginas del recibo como imágenes RGB. Devuelve (páginas, es_pdf)."""
    if ruta.suffix.lower() in EXT_PDF:
        imgs = []
        with fitz.open(str(ruta)) as d:
            for p in d:
                pix = p.get_pixmap(dpi=DPI_RENDER, alpha=False)
                imgs.append(Image.frombytes("RGB", (pix.width, pix.height), pix.samples))
        return imgs, True
    img = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
    if max(img.size) > 2600:                                    # fotos enormes: bajan de peso sin perder lectura
        img.thumbnail((2600, 2600))
    return [img], False


def _recortar(img: Image.Image, margen: int = 16, umbral: int = 248) -> Image.Image | None:
    """Quita el blanco alrededor del recibo. None si la página está en blanco."""
    caja = img.convert("L").point(lambda v: 255 if v < umbral else 0).getbbox()
    if not caja:
        return None
    x0, y0, x1, y1 = caja
    return img.crop((max(0, x0 - margen), max(0, y0 - margen), min(img.width, x1 + margen), min(img.height, y1 + margen)))


def _enmarcar(img: Image.Image) -> Image.Image:
    return ImageOps.expand(img, border=2, fill=(201, 209, 219))


def _escala(ancho: int, alto: int, caja_w: float, caja_h: float) -> float:
    """Pulgadas por píxel con que queda la imagen al encajarla en la caja (mide qué tan legible queda)."""
    return min(caja_w, caja_h * ancho / alto) / ancho


def hojas_de(ruta: Path, caja_w_in: float, caja_h_in: float) -> list[Image.Image]:
    """Una lista de imágenes, una por HOJA del documento final (todas verticales, sobre la plantilla).
    · PDF de 1 página o foto -> 1 hoja.
    · PDF de 2 páginas -> una sobre otra en una sola hoja si así conservan al menos el 85 % de su legibilidad; si no, una hoja por página.
    · PDF de 3 o más páginas -> una hoja por página (con banner de «continuación»)."""
    paginas, es_pdf = _renderizar(ruta)
    if es_pdf:
        paginas = [p for p in (_recortar(p) for p in paginas) if p is not None] or paginas[:1]
    if len(paginas) == 2:
        ancho = max(p.width for p in paginas)
        hueco = 24
        lienzo = Image.new("RGB", (ancho, paginas[0].height + hueco + paginas[1].height), "white")
        lienzo.paste(paginas[0], ((ancho - paginas[0].width) // 2, 0))
        lienzo.paste(paginas[1], ((ancho - paginas[1].width) // 2, paginas[0].height + hueco))
        sola = min(_escala(p.width, p.height, caja_w_in, caja_h_in) for p in paginas)
        if _escala(lienzo.width, lienzo.height, caja_w_in, caja_h_in) / sola >= 0.85:
            return [_enmarcar(lienzo)]
    return [_enmarcar(p) for p in paginas]


# ---------------------------------------------------------------- documento Word

def _estilos(doc: Document) -> None:
    n = doc.styles["Normal"]
    n.font.name = FUENTE
    rpr = n.element.get_or_add_rPr()
    for atributo in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rpr.rFonts.set(qn(atributo), FUENTE)
    n.font.size = Pt(9)
    n.paragraph_format.space_before = Pt(0)
    n.paragraph_format.space_after = Pt(0)
    n.paragraph_format.line_spacing = 1.0


def _pie(sec, total_paginas: int) -> None:
    """«Pág. N/M» a la derecha, sobre el pie del membrete (en la primera hoja y en las demás). Es corto a propósito: el membrete trae una línea verde que llega hasta cerca del margen."""
    for pie in (sec.footer, sec.first_page_footer):
        pie.is_linked_to_previous = False
        p = pie.paragraphs[0]
        for r in list(p._p.findall(qn("w:r"))):
            p._p.remove(r)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p.add_run("Pág. ")
        r.font.size, r.font.name, r.font.color.rgb = Pt(8), FUENTE, RGBColor.from_string(GRIS)
        campo(p, "PAGE", "1", tam_pt=8, color=GRIS, fuente=FUENTE)
        r = p.add_run("/")
        r.font.size, r.font.name, r.font.color.rgb = Pt(8), FUENTE, RGBColor.from_string(GRIS)
        campo(p, "NUMPAGES", str(total_paginas), tam_pt=8, color=GRIS, fuente=FUENTE)


def _salto_de_hoja(doc) -> None:
    """Párrafo diminuto (1 pt) que abre una hoja nueva."""
    p = doc.add_paragraph()
    p.paragraph_format.page_break_before = True
    p.paragraph_format.space_before = p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = Pt(1)
    p.add_run().font.size = Pt(1)
    ppr = p._p.get_or_add_pPr()
    rpr = el("w:rPr")
    rpr.append(el("w:sz", w_val=2))
    ppr.append(rpr)


def construir_docx(items: list[dict], destino: Path, factor: float = 1.0) -> int:
    """Escribe el .docx sobre la plantilla de Campuslands. Devuelve el número de hojas. `factor` (<1) reduce las imágenes si no cupieran."""
    doc = Document(str(PLANTILLA_CAMPUSLANDS))
    cuerpo = doc.element.body
    for h in list(cuerpo):
        if h.tag != qn("w:sectPr"):
            cuerpo.remove(h)
    _estilos(doc)
    sec = doc.sections[0]
    ancho_tw = int(sec.page_width.twips - sec.left_margin.twips - sec.right_margin.twips)
    alto_img_tw = int(sec.page_height.twips - sec.top_margin.twips - sec.bottom_margin.twips - RESERVA_VERTICAL_TW)
    ancho_emu, alto_emu = int(ancho_tw * 635), int(alto_img_tw * 635)       # 1 twip = 635 EMU

    plan = []                                                  # [(item, imagen, índice_de_hoja_de_esa_factura)]
    for it in items:
        for i, img in enumerate(hojas_de(it["ruta"], ancho_tw / 1440, alto_img_tw / 1440)):
            plan.append((it, img, i))
    total_hojas = len(plan)
    _pie(sec, total_hojas)
    numero = {id(it): n for n, it in enumerate(items, 1)}

    with tempfile.TemporaryDirectory() as tmp:
        for k, (it, img, sub) in enumerate(plan):
            if k > 0:
                _salto_de_hoja(doc)
            agregar_banner(doc, numero[id(it)], len(items),
                           DatosFactura(it["fecha"], it["hora"], it["tipo"], it["proveedor"]), ancho_tw, continuacion=sub > 0)
            sp = doc.add_paragraph()                           # respiro entre el banner y el recibo
            sp.paragraph_format.space_before = Pt(8)
            sp.paragraph_format.line_spacing = Pt(1)
            sp.add_run().font.size = Pt(1)

            w_emu = min(ancho_emu, int(alto_emu * img.width / img.height)) * factor
            ruta_img = Path(tmp) / f"hoja{k:03d}.png"
            img.save(ruta_img, optimize=True)
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(2)
            forma = p.add_run().add_picture(str(ruta_img), width=Emu(int(w_emu)))
            for lado in ("distT", "distB", "distL", "distR"):         # sin esto LibreOffice añade 0,125" de aire a cada lado y el recibo queda descentrado
                forma._inline.set(lado, "0")
            extra = el("wp:effectExtent")
            for lado in ("l", "t", "r", "b"):
                extra.set(lado, "0")
            forma._inline.extent.addnext(extra)
            forma._inline.docPr.set("descr", f"Imagen de la factura original {it['archivo']}")
            forma._inline.docPr.set("name", f"Factura {numero[id(it)]:02d}")

            leyenda = f"Archivo original: {it['archivo']}" + (f" · {it['nota']}" if it["nota"] and sub == 0 else "")
            c = doc.add_paragraph()
            c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            c.paragraph_format.space_before = Pt(2)
            r = c.add_run(leyenda)
            r.italic, r.font.size, r.font.color.rgb = True, Pt(7), RGBColor.from_string("5B6B7F")

        fechas = [it["fecha"] for it in items]
        cp = doc.core_properties
        cp.title, cp.author, cp.last_modified_by, cp.language = f"Facturas {rango_fechas(fechas)}", "Campuslands Full Service", "Campuslands Full Service", "es-CO"
        incrustar_fuente(doc, FUENTE)                          # Poppins viaja dentro del Word: se ve igual aunque no esté instalada
        destino.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(destino))                                 # dentro del `with`: python-docx lee los PNG temporales al guardar
    return total_hojas


def nombre_salida(fechas: list[dt.date]) -> str:
    a, b = min(fechas), max(fechas)
    mes = lambda f: MESES[f.month - 1].capitalize()
    if a == b:
        cuerpo = f"{a.day:02d}_{mes(a)}_{a.year}"
    elif (a.year, a.month) == (b.year, b.month):
        cuerpo = f"{a.day:02d}-{b.day:02d}_{mes(a)}_{a.year}"
    elif a.year == b.year:
        cuerpo = f"{a.day:02d}_{mes(a)}-{b.day:02d}_{mes(b)}_{a.year}"
    else:
        cuerpo = f"{a.day:02d}_{mes(a)}_{a.year}-{b.day:02d}_{mes(b)}_{b.year}"
    return f"Facturas_{cuerpo}_Campuslands"


def cmd_construir(lote: Path, nombre: str | None, sin_pdf: bool) -> int:
    entrada, manif, salida = _rutas_lote(lote)
    if not manif.exists():
        print(f"No existe {manif}. Corre primero «inspeccionar».")
        return 1
    _, crudas = _cargar(manif)
    try:
        items = [_normalizar(f, entrada) for f in crudas]
    except ValueError as e:
        print(f"✗ {e}")
        return 1
    if not items:
        print("El manifiesto no tiene facturas.")
        return 1
    ordenadas = ordenar(items)
    sin_hora = [i["archivo"] for i in ordenadas if i["hora"] is None]
    nombre = nombre or nombre_salida([i["fecha"] for i in ordenadas])
    docx = salida / f"{nombre}.docx"

    factor = 1.0
    for intento in range(1, 7):
        hojas = construir_docx(ordenadas, docx, factor)
        if sin_pdf:
            break
        pdf = docx_a_pdf(docx)
        n_pdf = paginas_pdf(pdf)
        if n_pdf == hojas:
            break
        factor *= 0.93
        print(f"  (intento {intento}: el PDF tiene {n_pdf} páginas y debería tener {hojas}; reduzco las imágenes a {factor:.0%})")
    else:
        print("✗ No logré que cada factura quepa en una sola hoja. Revisa las imágenes de entrada.")
        return 1

    print(f"\n✓ {len(ordenadas)} facturas · {hojas} hojas")
    for n, i in enumerate(ordenadas, 1):
        print(f"  {n:02d}  {i['fecha'].isoformat()}  {hora_12h(i['hora']):>10}  {i['proveedor'] or '—':<10} {i['tipo'] or '—':<12} {i['archivo']}")
        if i["nota"]:
            print(f"        nota: {i['nota']}")
    if sin_hora:
        print(f"\n⚠ Sin hora (quedaron al final de su día): {', '.join(sin_hora)}")
    print(f"\nWord: {docx}")
    if not sin_pdf:
        print(f"PDF:  {docx.with_suffix('.pdf')}")
    return 0


def main(argv: list[str] | None = None) -> int:
    configurar_consola()
    ap = argparse.ArgumentParser(description="Unificación de facturas (Campuslands).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("inspeccionar", help="detecta fecha/hora/proveedor y escribe el borrador del manifiesto")
    a.add_argument("lote", type=Path)
    b = sub.add_parser("construir", help="ordena y genera el Word y el PDF")
    b.add_argument("lote", type=Path)
    b.add_argument("--nombre", help="nombre de los archivos de salida (sin extensión)")
    b.add_argument("--sin-pdf", action="store_true")
    args = ap.parse_args(argv)
    if args.cmd == "inspeccionar":
        return cmd_inspeccionar(args.lote)
    return cmd_construir(args.lote, args.nombre, args.sin_pdf)


if __name__ == "__main__":
    sys.exit(main())
