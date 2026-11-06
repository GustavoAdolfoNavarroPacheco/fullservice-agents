"""Utilidades compartidas por las dos funcionalidades del agente multifuncional.

  * rutas del agente, localización de LibreOffice y ffmpeg,
  * conversión .docx -> .pdf (LibreOffice, para que el PDF sea idéntico al Word),
  * fechas en español, slugs,
  * pequeños ayudantes de XML de Word (campos PAGE / NUMPAGES, bordes de párrafo).

No tiene dependencias fuera de python-docx / lxml.
"""
from __future__ import annotations

import datetime as dt
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

RAIZ = Path(__file__).resolve().parent.parent          # multifunctional-agent/
PLANTILLA_CAMPUSLANDS = RAIZ / "recursos" / "plantilla" / "Plantilla Word - Campuslands.docx"
FUENTES_DIR = RAIZ / "recursos" / "fuentes"           # Poppins (tipografía oficial de Campuslands)
POPPINS = {"regular": "Poppins-Regular.ttf", "bold": "Poppins-Bold.ttf", "italic": "Poppins-Italic.ttf", "boldItalic": "Poppins-BoldItalic.ttf"}

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


# ---------------------------------------------------------------- consola

def configurar_consola() -> None:
    """La consola de Windows usa cp1252: fuerza UTF-8 para que las tildes no rompan la salida."""
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except Exception:
            pass


# ---------------------------------------------------------------- herramientas externas

def buscar_soffice() -> Path | None:
    """LibreOffice (soffice.exe). Se puede forzar con la variable SOFFICE."""
    candidatos = [os.environ.get("SOFFICE", ""), shutil.which("soffice") or "",
                  r"C:\Program Files\LibreOffice\program\soffice.exe",
                  r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"]
    for c in candidatos:
        if c and Path(c).exists():
            return Path(c)
    return None


def buscar_ffmpeg() -> str | None:
    """ffmpeg (para extraer el audio de mp3/mp4/m4a/wav…). Se puede forzar con la variable FFMPEG."""
    forzado = os.environ.get("FFMPEG", "")
    if forzado and Path(forzado).exists():
        return forzado
    return shutil.which("ffmpeg")


def docx_a_pdf(docx: Path, carpeta_salida: Path | None = None) -> Path:
    """Convierte un .docx a PDF con LibreOffice. El PDF queda junto al .docx (o en `carpeta_salida`)."""
    soffice = buscar_soffice()
    if not soffice:
        raise RuntimeError("No encuentro LibreOffice (soffice.exe). Instálalo con: "
                           "winget install TheDocumentFoundation.LibreOffice  (o define la variable SOFFICE).")
    docx = Path(docx).resolve()
    salida = Path(carpeta_salida).resolve() if carpeta_salida else docx.parent
    salida.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as perfil:       # perfil propio: evita bloqueos si hay otro LibreOffice abierto
        carpeta_fuentes = Path(perfil) / "user" / "fonts"   # LibreOffice carga las fuentes de aquí (Poppins, aunque no esté instalada)
        carpeta_fuentes.mkdir(parents=True, exist_ok=True)
        for ttf in FUENTES_DIR.glob("*.ttf"):
            shutil.copy2(ttf, carpeta_fuentes / ttf.name)
        cmd = [str(soffice), f"-env:UserInstallation={Path(perfil).as_uri()}", "--headless",
               "--convert-to", "pdf", "--outdir", str(salida), str(docx)]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    pdf = salida / (docx.stem + ".pdf")
    if not pdf.exists():
        raise RuntimeError(f"LibreOffice no generó el PDF.\n{r.stdout}\n{r.stderr}")
    return pdf


def paginas_pdf(pdf: Path) -> int:
    import fitz
    with fitz.open(str(pdf)) as d:
        return d.page_count


# ---------------------------------------------------------------- texto y fechas

def slug(texto: str) -> str:
    """Minúsculas, sin tildes ni espacios, separado por guiones (convención del repo)."""
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") or "sin-nombre"


def fecha_larga(f: dt.date, con_dia: bool = False) -> str:
    """28 de octubre de 2026  (con_dia: «Miércoles 28 de octubre de 2026»)."""
    base = f"{f.day} de {MESES[f.month - 1]} de {f.year}"
    return f"{DIAS[f.weekday()].capitalize()} {base}" if con_dia else base


def fecha_corta_con_dia(f: dt.date) -> str:
    """Mié 28 oct 2026 (cabe en una celda del banner)."""
    return f"{DIAS[f.weekday()][:3].capitalize()} {f.day} {MESES[f.month - 1][:3]} {f.year}"


def hora_12h(h: dt.time | None) -> str:
    """13:47 -> «1:47 p. m.»;  None -> «Sin hora»."""
    if h is None:
        return "Sin hora"
    h12 = h.hour % 12 or 12
    return f"{h12}:{h.minute:02d} {'a. m.' if h.hour < 12 else 'p. m.'}"


def rango_fechas(fechas: list[dt.date]) -> str:
    """«28 al 29 de octubre de 2026», «28 de octubre al 2 de noviembre de 2026», …"""
    a, b = min(fechas), max(fechas)
    if a == b:
        return fecha_larga(a)
    if (a.year, a.month) == (b.year, b.month):
        return f"{a.day} al {b.day} de {MESES[a.month - 1]} de {a.year}"
    if a.year == b.year:
        return f"{a.day} de {MESES[a.month - 1]} al {b.day} de {MESES[b.month - 1]} de {a.year}"
    return f"{fecha_larga(a)} al {fecha_larga(b)}"


# ---------------------------------------------------------------- XML de Word

def el(etiqueta: str, **atributos):
    """Crea un elemento OOXML: el('w:shd', w_fill='EEF3F8')  (el guion bajo hace de «:»)."""
    e = OxmlElement(etiqueta)
    for k, v in atributos.items():
        e.set(qn(k.replace("_", ":", 1)), str(v))
    return e


def campo(parrafo, instruccion: str, resultado: str, tam_pt: float | None = None, color: str | None = None,
          negrita: bool = False, fuente: str | None = None) -> None:
    """Campo complejo de Word (PAGE, NUMPAGES…) con su resultado en caché. Word y LibreOffice lo recalculan al abrir/exportar."""
    def corrida():
        r = parrafo.add_run()
        if tam_pt:
            r.font.size = Pt(tam_pt)
        if color:
            r.font.color.rgb = RGBColor.from_string(color)
        if negrita:
            r.font.bold = True
        if fuente:
            r.font.name = fuente
        return r
    corrida()._r.append(el("w:fldChar", w_fldCharType="begin"))
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = f" {instruccion} "
    corrida()._r.append(it)
    corrida()._r.append(el("w:fldChar", w_fldCharType="separate"))
    corrida().text = resultado
    corrida()._r.append(el("w:fldChar", w_fldCharType="end"))


def borde_parrafo(parrafo, lado: str, color: str, sz: int = 4, espacio: int = 4) -> None:
    """Borde fino en un lado del párrafo (top/bottom/left/right). `sz` en octavos de punto."""
    ppr = parrafo._p.get_or_add_pPr()
    pbdr = ppr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        # pBdr va antes de shd/tabs/spacing/ind/jc…: se inserta al principio del pPr (después de pStyle/keepNext… si existen)
        despues = [c for c in ppr if c.tag in (qn("w:pStyle"), qn("w:keepNext"), qn("w:keepLines"),
                                                qn("w:pageBreakBefore"), qn("w:framePr"), qn("w:widowControl"),
                                                qn("w:numPr"), qn("w:suppressLineNumbers"))]
        if despues:
            despues[-1].addnext(pbdr)
        else:
            ppr.insert(0, pbdr)
    pbdr.append(el(f"w:{lado}", w_val="single", w_sz=sz, w_space=espacio, w_color=color))


# ---------------------------------------------------------------- fuentes incrustadas

def incrustar_fuente(doc, familia: str, archivos: dict[str, str] | None = None) -> None:
    """Incrusta una familia TrueType en el .docx (como hace Word con «Incrustar fuentes en el archivo»), para que el documento
    se vea con esa tipografía aunque el equipo que lo abra no la tenga instalada.
    `archivos`: {"regular": nombre.ttf, "bold": …, "italic": …, "boldItalic": …} dentro de FUENTES_DIR (por defecto, Poppins).
    Las fuentes se ofuscan con la clave GUID que exige el formato (XOR de los primeros 32 bytes)."""
    import uuid
    from docx.opc.packuri import PackURI
    from docx.opc.part import Part
    from lxml import etree

    archivos = archivos or POPPINS
    W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    paquete = doc.part.package
    tabla = next((rel.target_part for rel in doc.part.rels.values() if rel.reltype.endswith("/fontTable")), None)
    if tabla is None:
        tabla = Part(PackURI("/word/fontTable.xml"), "application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml",
                     f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:fonts xmlns:w="{W}" xmlns:r="{R}"/>'.encode(), paquete)
        doc.part.relate_to(tabla, R + "/fontTable")
    raiz = etree.fromstring(tabla.blob)
    nsmap = {"w": W, "r": R}
    if "r" not in (raiz.nsmap or {}):                                     # r: debe estar declarado en la raíz para los r:id
        nueva = etree.Element(raiz.tag, nsmap={**raiz.nsmap, "r": R})
        nueva.extend(list(raiz))
        raiz = nueva
    fuente = next((f for f in raiz.findall("w:font", nsmap) if f.get(f"{{{W}}}name") == familia), None)
    if fuente is None:
        fuente = etree.SubElement(raiz, f"{{{W}}}font")
        fuente.set(f"{{{W}}}name", familia)
    n = sum(1 for r in tabla.rels.values() if r.reltype.endswith("/font"))
    for variante, nombre in archivos.items():
        ruta = FUENTES_DIR / nombre
        if not ruta.exists():
            continue
        n += 1
        guid = "{" + str(uuid.uuid4()).upper() + "}"
        clave = bytes.fromhex(guid.strip("{}").replace("-", ""))[::-1]
        datos = bytearray(ruta.read_bytes())
        for i in range(32):
            datos[i] ^= clave[i % 16]
        parte = Part(PackURI(f"/word/fonts/font{n}.odttf"), "application/vnd.openxmlformats-officedocument.obfuscatedFont", bytes(datos), paquete)
        rid = tabla.relate_to(parte, R + "/font")
        emb = etree.SubElement(fuente, f"{{{W}}}embed{variante[0].upper()}{variante[1:]}")
        emb.set(f"{{{R}}}id", rid)
        emb.set(f"{{{W}}}fontKey", guid)
    tabla._blob = etree.tostring(raiz, xml_declaration=True, encoding="UTF-8", standalone=True)

    ajustes = doc.settings.element
    if ajustes.find(f"{{{W}}}embedTrueTypeFonts") is None:
        despues = {"saveSubsetFonts", "saveFormsData", "mirrorMargins", "alignBordersAndEdges", "bordersDoNotSurroundHeader",
                   "bordersDoNotSurroundFooter", "gutterAtTop", "hideSpellingErrors", "hideGrammaticalErrors", "activeWritingStyle",
                   "proofState", "formsDesign", "attachedTemplate", "linkStyles", "stylePaneFormatFilter", "stylePaneSortMethod",
                   "documentType", "mailMerge", "revisionView", "trackRevisions", "doNotTrackMoves", "doNotTrackFormatting",
                   "documentProtection", "autoFormatOverride", "styleLockTheme", "styleLockQFSet", "defaultTabStop"}
        marca = etree.Element(f"{{{W}}}embedTrueTypeFonts")
        ref = next((c for c in ajustes if etree.QName(c).localname in despues), None)
        (ref.addprevious(marca) if ref is not None else ajustes.append(marca))
