"""Comprueba que el texto del .docx generado es idéntico al del archivo fuente, línea por línea (y el del pie de página).

Diferencias permitidas (y solo estas): se elimina el ítem «Control de versión y criterio de consolidación» (su título y su tabla);
se agregan la tabla de contenido (su título y sus entradas) y la carta de presentación pedida por el usuario; el apartado de firma final se adapta al ejemplo del usuario (Campuslands a la izquierda con los datos de
la firmante; sin rayas bajas, que pasan a líneas dibujadas). Uso: python verificar.py
"""
import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

AQUI = Path(__file__).resolve().parent
DOCX = AQUI.parent / "entrega" / "Alcance Funcional Consolidado - Unidrogas.docx"
sys.stdout.reconfigure(encoding="utf-8")


def lineas(texto):
    return [l for l in texto.split("\n") if l.strip()]


# --- fuente, sin el ítem de control de versión (título + tabla siguiente)
bloques = json.loads((AQUI / "contenido.json").read_text(encoding="utf8"))
fuente, saltar_tabla = [], False
for b in bloques:
    if b["t"] == "p":
        txt = "".join(r["x"] for r in b["runs"])
        if txt.startswith("Control de versi"):
            saltar_tabla = True
            continue
        if txt.startswith("Por Unidrogas"):            # apartado de firma adaptado al ejemplo del usuario (rótulos + datos de la firmante)
            fuente += ["Por Campuslands S.A.S. BIC:", "Por Unidrogas S.A.:"]
        elif txt.startswith("Nombre / cargo / fecha"):
            fuente += ["GABRIELA PEDRAZA RUEDA", "Directora Full Service Global", "gabriela.pedraza@campuslands.com", "Nombre / cargo / fecha:"]
        else:
            fuente += lineas(txt)
    else:
        if saltar_tabla:
            saltar_tabla = False
            continue
        for fila in b["filas"]:
            for celda in fila:
                for p in celda:
                    fuente += lineas("".join(r["x"] for r in p))
# las firmas se leen por filas: «Por U», «Por C», «Nombre U», «Nombre C» (mismo orden que en la fuente)

# --- resultado (sin la tabla de contenido ni su título)
doc = Document(str(DOCX))
salida = []
for el in doc.element.body:
    if el.tag.endswith("}p"):
        p = Paragraph(el, doc)
        if p.style.name in ("toc 1", "toc 2", "Carta Datos", "Carta Cuerpo", "Carta Viñeta") or p.text.strip() in ("Tabla de contenido", "Carta de presentación"):
            continue
        salida += lineas(p.text)
    elif el.tag.endswith("}tbl"):
        for fila in Table(el, doc).rows:
            for celda in fila.cells:
                for p in celda.paragraphs:
                    salida += lineas(p.text)

print("líneas fuente (sin control de versión):", len(fuente), "| líneas resultado:", len(salida))
dif = [(i, e, s) for i, (e, s) in enumerate(zip(fuente, salida)) if e != s]
if len(fuente) != len(salida):
    print("¡Distinto número de líneas!")
print("diferencias de cuerpo:", len(dif))
for i, e, s in dif[:10]:
    print(" ", i, repr(e), "->", repr(s))

# --- pie de página
pie_fuente = (AQUI / "pie.txt").read_text(encoding="utf8")
s0 = doc.sections[0]
pies = [pp.text for f in (s0.first_page_footer, s0.footer) for pp in f.paragraphs]
pie_ok = pie_fuente in pies and sum(1 for t in pies if t == pie_fuente) == 2
print("pie de página presente en portada y resto:", pie_ok)
ok = not dif and len(fuente) == len(salida) and pie_ok
print("RESULTADO:", "IDÉNTICO (salvo el ítem de control de versión eliminado y la tabla de contenido)" if ok else "HAY DIFERENCIAS")
