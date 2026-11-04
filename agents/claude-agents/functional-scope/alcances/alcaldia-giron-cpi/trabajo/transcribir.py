"""Transcripción visual y estructural de la propuesta a la estructura estándar de Campuslands.

El texto del archivo fuente NO se modifica; solo cambian: (1) el título de la portada, de «PROPUESTA COMERCIAL Y TÉCNICA»
a «Alcances Tecnicos y Propuestas Comerciales», (2) se quita «Versión 2.0 | » de la portada y (3) se agrega la cláusula de costos que pidió el usuario en 9.4.
Se agrega además la tabla de contenido (estructura). Lee `contenido.json` (generado con `extraer.py` y `python -I`).

Uso: python transcribir.py
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.shared import Pt, Twips  # noqa: E402
from alcance_docx import Alcance, FIRMA_IMAGEN  # noqa: E402

TITULO_ORIGINAL = "PROPUESTA COMERCIAL Y TÉCNICA"
TITULO_NUEVO = "Alcances Tecnicos y Propuestas Comerciales"
CLAUSULA = ("Los costos del proyecto que no estén contemplados en las primeras fases, pero estén directamente relacionados "
            "con la prestación del servicio, serán asumidos por la entidad.")
SALIDA = AQUI.parent / "entrega" / "Alcances Tecnicos y Propuestas Comerciales - Alcaldia de Giron.docx"

bloques = json.loads((AQUI / "contenido.json").read_text(encoding="utf8"))


def texto(b):
    return "".join(r["x"] for r in b["runs"])


a = Alcance()
a.resaltar = False          # transcripción literal: sin resaltar estados ni tocar el texto

# ------------------------------------------------------------------ portada (seis líneas del archivo, sin tarjetas)
assert texto(bloques[0]) == TITULO_ORIGINAL
a.doc.add_paragraph(TITULO_NUEVO, style="Portada Tipo")
a.doc.add_paragraph(texto(bloques[1]), style="Portada Titulo")
a.doc.add_paragraph(style="Portada Regla")
a.doc.add_paragraph(texto(bloques[2]), style="Portada Cliente")
a.doc.add_paragraph(texto(bloques[3]), style="Portada Area")
PREFIJO_VERSION = "Versión 2.0 | "          # el usuario pidió quitar «Versión 2.0» de la portada; la fecha se conserva
assert texto(bloques[4]).startswith(PREFIJO_VERSION)
a.doc.add_paragraph(texto(bloques[4])[len(PREFIJO_VERSION):], style="Portada Area")
nota = a.doc.add_paragraph(texto(bloques[5]), style="Portada Nota")
nota.paragraph_format.space_before = Pt(120)

# ------------------------------------------------------------------ carta de presentación (una hoja)
assert texto(bloques[6]) == "Carta de presentación"
t = a.doc.add_paragraph(texto(bloques[6]), style="Título Sin Numerar")
t.paragraph_format.page_break_before = True
i = 7
primero_cuerpo = True
while not texto(bloques[i]).startswith("Atentamente"):
    b = bloques[i]
    lineas = texto(b).split("\n")
    if len(lineas) > 1 or texto(b).startswith("Girón,"):
        q = a.doc.add_paragraph(style="Carta Datos")
        q.paragraph_format.space_before = Pt(30)
        q.paragraph_format.line_spacing = 1.5
        for k, linea in enumerate(lineas):
            if k:
                q.add_run().add_break()
            r = q.add_run(linea)
            r.font.size = Pt(12)
            r.bold = k == len(lineas) - 1 and len(lineas) > 1
    else:
        q = a.doc.add_paragraph(style="Carta Cuerpo")
        q.paragraph_format.space_before = Pt(18) if primero_cuerpo else Pt(0)
        q.paragraph_format.space_after = Pt(16)
        q.paragraph_format.line_spacing = 1.5
        primero_cuerpo = False
        r = q.add_run(texto(b))
        r.font.size = Pt(12)
    i += 1
lineas = texto(bloques[i]).split("\n")                      # «Atentamente,» + nombre + cargo + correo
q = a.doc.add_paragraph(style="Carta Datos")
q.paragraph_format.space_before = Pt(26)
q.paragraph_format.space_after = Pt(70)
q.add_run(lineas[0]).font.size = Pt(12)
for k, linea in enumerate(lineas[1:]):
    q = a.doc.add_paragraph(style="Carta Datos")
    q.paragraph_format.line_spacing = 1.4
    r = q.add_run(linea)
    r.font.size = Pt(12)
    if k == 0:
        r.bold = True
i += 1

# ------------------------------------------------------------------ tabla de contenido (una hoja)
a.tabla_de_contenido(niveles=2)

# ------------------------------------------------------------------ contenido
LISTA = re.compile(r"^(•|☐|\d+\.\s)")


def cuerpo(b, lista=False):
    q = a.doc.add_paragraph(style="Normal")
    if lista:
        q.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        q.paragraph_format.left_indent = Twips(360)
        q.paragraph_format.first_line_indent = Twips(-200)
        q.paragraph_format.space_after = Pt(3)
    for r in b["runs"]:
        run = q.add_run(r["x"])
        run.bold = r["b"] or None
    return q


def tabla(b):
    filas = [[[texto({"runs": p}) for p in celda] for celda in fila] for fila in b["filas"]]
    celdas = [[c[0] if len(c) == 1 else c for c in fila] for fila in filas]
    n = len(celdas[0])
    largos = [sum(len(c if isinstance(c, str) else " ".join(c)) for c in (f[k] for f in celdas[1:])) / max(1, len(celdas) - 1) for k in range(n)]
    pesos = [1 + min(largo, 70) / 14 for largo in largos]
    a.tabla(None, celdas[0], celdas[1:], pesos)


primer_h1 = True
tras_94 = False
for b in bloques[i:]:
    if b["t"] == "tbl":
        if len(b["filas"]) == 1 and len(b["filas"][0]) == 2 and "YESENIA" in texto({"runs": b["filas"][0][0][0]}):
            izq, der = ([l for l in texto({"runs": p}).split("\n") if l.strip()] for p in (b["filas"][0][0][0], b["filas"][0][1][0]))
            a.firmas_lineas(izq, der, imagen_izq=FIRMA_IMAGEN)
        else:
            tabla(b)
        continue
    est, txt = b["estilo"], texto(b)
    if est == "Ttulo1":
        a.h1(txt, nueva_pagina=primer_h1)
        primer_h1 = False
    elif est == "Ttulo2":
        a.h2(txt)
    elif est == "Ttulo3":
        a.h3(txt)
    elif all(r["b"] for r in b["runs"]) and re.match(r"^\d+\.\d+\.", txt) and len(txt) < 100:
        a.h2(txt)                                           # «9.1. …» son subtítulos del archivo
        tras_94 = txt.startswith("9.4.")
    else:
        q = cuerpo(b, lista=bool(LISTA.match(txt)))
        if txt.startswith("Se firma su aceptación"):
            q.paragraph_format.keep_with_next = True
        if tras_94:                                          # cláusula pedida por el usuario, al final de 9.4
            cuerpo({"runs": [{"x": CLAUSULA, "b": False}]})
            tras_94 = False

a.guardar(SALIDA, TITULO_NUEVO)
print(SALIDA)
