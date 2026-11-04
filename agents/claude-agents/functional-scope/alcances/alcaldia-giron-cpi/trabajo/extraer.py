"""Extrae el contenido de un .docx a JSON (solo biblioteca estándar; se ejecuta con `python -I`).

Bloques: {"t": "p", "estilo": "...", "runs": [{"x": texto, "b": negrita}]} y
{"t": "tbl", "filas": [[[parrafo, ...], ...], ...]} con cada párrafo como lista de runs.
Los saltos de línea dentro de un párrafo se guardan como «\\n» dentro del texto de un run.
"""
import json
import sys
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
z = zipfile.ZipFile(sys.argv[1])
raiz = ET.fromstring(z.read("word/document.xml"))
cuerpo = raiz.find(W + "body")


def runs(p):
    out = []
    for r in p.findall(W + "r"):
        txt = ""
        for n in r:
            if n.tag == W + "t":
                txt += n.text or ""
            elif n.tag == W + "tab":
                txt += "\t"
            elif n.tag == W + "br" and n.get(W + "type") != "page":
                txt += "\n"
        if not txt:
            continue
        rp = r.find(W + "rPr")
        neg = rp is not None and rp.find(W + "b") is not None
        out.append({"x": txt, "b": neg})
    return out


def estilo(p):
    ppr = p.find(W + "pPr")
    if ppr is not None and ppr.find(W + "pStyle") is not None:
        return ppr.find(W + "pStyle").get(W + "val")
    return ""


bloques = []
for el in cuerpo:
    if el.tag == W + "p":
        rs = runs(el)
        if any(r["x"].strip() for r in rs):
            bloques.append({"t": "p", "estilo": estilo(el), "runs": rs})
    elif el.tag == W + "tbl":
        filas = []
        for tr in el.findall(W + "tr"):
            fila = []
            for tc in tr.findall(W + "tc"):
                fila.append([runs(p) for p in tc.findall(W + "p") if any(r["x"].strip() for r in runs(p))])
            filas.append(fila)
        bloques.append({"t": "tbl", "filas": filas})
json.dump(bloques, open(sys.argv[2], "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(len(bloques), "bloques")
