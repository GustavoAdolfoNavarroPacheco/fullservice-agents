"""Comprueba que el texto del .docx generado es idéntico al del archivo fuente, línea por línea.

Diferencias permitidas (y solo estas): el título de la portada, el prefijo «Versión 2.0 | » de la portada, la cláusula de costos agregada en 9.4 y la tabla de contenido
(su título «Tabla de contenido» y sus entradas). Uso: python verificar.py
"""
import json
import sys
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

AQUI = Path(__file__).resolve().parent
DOCX = AQUI.parent / "entrega" / "Alcances Tecnicos y Propuestas Comerciales - Alcaldia de Giron.docx"
sys.stdout.reconfigure(encoding="utf-8")


def lineas(texto):
    return [l for l in texto.split("\n") if l.strip()]


# --- fuente
fuente = []
for b in json.loads((AQUI / "contenido.json").read_text(encoding="utf8")):
    if b["t"] == "p":
        fuente += lineas("".join(r["x"] for r in b["runs"]))
    else:
        for fila in b["filas"]:
            for celda in fila:
                for p in celda:
                    fuente += lineas("".join(r["x"] for r in p))

# --- resultado (se omiten la tabla de contenido y su título)
doc = Document(str(DOCX))
salida = []
for el in doc.element.body:
    if el.tag.endswith("}p"):
        p = Paragraph(el, doc)
        if p.style.name in ("toc 1", "toc 2") or p.text.strip() == "Tabla de contenido":
            continue
        salida += lineas(p.text)
    elif el.tag.endswith("}tbl"):
        for fila in Table(el, doc).rows:
            for celda in fila.cells:
                for p in celda.paragraphs:
                    salida += lineas(p.text)

TITULO_ORIGINAL, TITULO_NUEVO = "PROPUESTA COMERCIAL Y TÉCNICA", "Alcances Tecnicos y Propuestas Comerciales"
PREFIJO = "Versión 2.0 | "
esperado = [TITULO_NUEVO if l == TITULO_ORIGINAL else (l[len(PREFIJO):] if l.startswith(PREFIJO) else l) for l in fuente]
clausula = [l for l in salida if l.startswith("Los costos del proyecto que no estén contemplados")]
salida_sin_clausula = [l for l in salida if l not in clausula]

print("líneas fuente:", len(fuente), "| líneas resultado (sin cláusula):", len(salida_sin_clausula), "| cláusulas agregadas:", len(clausula))
dif = [(i, e, s) for i, (e, s) in enumerate(zip(esperado, salida_sin_clausula)) if e != s]
if len(esperado) != len(salida_sin_clausula):
    print("¡Distinto número de líneas!")
print("diferencias:", len(dif))
for i, e, s in dif[:10]:
    print(" ", i, repr(e), "->", repr(s))
print("RESULTADO:", "IDÉNTICO (salvo título, cláusula y tabla de contenido)" if not dif and len(esperado) == len(salida_sin_clausula) else "HAY DIFERENCIAS")
