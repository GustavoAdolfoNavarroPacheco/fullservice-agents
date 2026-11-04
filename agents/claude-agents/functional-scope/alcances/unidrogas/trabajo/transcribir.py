"""Transcripción visual y estructural del «Alcance funcional consolidado — Unidrogas» a la estructura estándar de Campuslands.

El texto del archivo fuente NO se modifica. Únicas diferencias: se elimina el ítem «Control de versión y criterio de consolidación»
(su título y su tabla), por indicación del usuario, y se agrega la tabla de contenido (estructura) y una carta de presentación (hoja 3) a pedido del usuario. Lee `contenido.json` y `pie.txt`
(generados con `extraer.py` y `python -I`). Uso: python transcribir.py
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.shared import Pt, RGBColor, Twips  # noqa: E402
from alcance_docx import Alcance, ANCHO_TEXTO, TINTA, _TCPR_ORDEN, _borde_parrafo, _el, _insertar_ordenado  # noqa: E402

SALIDA = AQUI.parent / "entrega" / "Alcance Funcional Consolidado - Unidrogas.docx"
bloques = json.loads((AQUI / "contenido.json").read_text(encoding="utf8"))
PIE = (AQUI / "pie.txt").read_text(encoding="utf8")


def texto(b):
    return "".join(r["x"] for r in b["runs"])


a = Alcance()
a.resaltar = False          # transcripción literal: sin resaltar estados ni tocar el texto

# ------------------------------------------------------------------ pie de página del archivo (en todas las hojas)
sec = a.doc.sections[0]
for pie in (sec.first_page_footer, sec.footer):
    q = pie.paragraphs[0].insert_paragraph_before()
    q.alignment = WD_ALIGN_PARAGRAPH.CENTER
    q.paragraph_format.space_after = Pt(2)
    r = q.add_run(PIE)
    r.font.size = Pt(7.5)
    r.font.color.rgb = a.doc.styles["Normal"].font.color.rgb if False else __import__("docx").shared.RGBColor(0x7F, 0x7F, 0x7F)

# ------------------------------------------------------------------ portada (cinco líneas del archivo, sin tarjetas)
assert texto(bloques[0]).startswith("AUTOMATIZACI") and texto(bloques[4]).startswith("CONFIDENCIAL")
t = a.doc.add_paragraph(texto(bloques[0]), style="Portada Titulo")
t.paragraph_format.space_before = Pt(80)
a.doc.add_paragraph(style="Portada Regla")
q = a.doc.add_paragraph(texto(bloques[1]), style="Portada Cliente")
for r in q.runs:
    r.font.size = Pt(13)
a.doc.add_paragraph(texto(bloques[2]), style="Portada Area")
a.doc.add_paragraph(texto(bloques[3]), style="Portada Area")
nota = a.doc.add_paragraph(texto(bloques[4]), style="Portada Nota")
nota.paragraph_format.space_before = Pt(130)

# ------------------------------------------------------------------ tabla de contenido (una hoja)
a.tabla_de_contenido(niveles=2)

# ------------------------------------------------------------------ carta de presentación (hoja 3; la pidió el usuario, el archivo no la trae)
# Texto redactado solo con datos del propio archivo (portada, sección 1, párrafo «Estado» y tabla de validaciones).
a.carta_presentacion({
    "lugar_fecha": "29 de octubre de 2026",
    "destinatario": ["Señores", "UNIDROGAS S.A."],
    "asunto": "Alcance funcional consolidado — Automatización de contenidos y formación con IA",
    "parrafos": [
        "Campuslands S.A.S. BIC presenta a Unidrogas S.A. el documento de alcance funcional consolidado «Automatización de contenidos y formación "
        "con IA», para su validación funcional, técnica y comercial. El documento organiza la solución en dos componentes independientes y "
        "contratables por separado, Unidrogas Video y Unidrogas Plataforma, y contiene lo siguiente:",
        "El proyecto prioriza Video por la necesidad de contar con un avance funcional durante enero de 2027. Este documento no reemplaza una "
        "cotización aprobada ni constituye orden de inicio, y las funciones condicionadas a terceros se precisarán en la prueba de concepto.",
        "Agradecemos la revisión de los responsables de Aprendizaje y Desarrollo y de TI de Unidrogas, y quedamos atentos a sus observaciones.",
    ],
    "vinetas": [
        "El Componente A, Unidrogas Video, con sus módulos, investigación tecnológica, prueba de concepto y criterios de aceptación (sección 2).",
        "El Componente B, Unidrogas Plataforma, con sus pilares, módulos y condiciones de integración (sección 3).",
        "La arquitectura, la seguridad, los entregables, el cronograma, los consumos, la garantía y las condiciones comerciales (secciones 4 a 10).",
        "Las validaciones pendientes y la aceptación (sección 11).",
    ],
    "firmante": {"nombre": "DIEGO TARAZONA", "cargo": "Gerente Comercial", "entidad": "Campuslands S.A.S. BIC", "correo": "diego@campuslands.com"},
})

# ------------------------------------------------------------------ contenido
# Se elimina el ítem «Control de versión y criterio de consolidación» (título + tabla); su párrafo «Estado: …» se conserva.
assert texto(bloques[5]).startswith("Control de versi") and bloques[6]["t"] == "tbl" and texto(bloques[7]).startswith("Estado:")
resto = bloques[7:]


def cuerpo(b, estilo=None):
    q = a.doc.add_paragraph(style=estilo or "Normal")
    for r in b["runs"]:
        run = q.add_run(r["x"])
        run.bold = r["b"] or None
    return q


def tabla(b):
    filas = [[[texto({"runs": p}) for p in celda] for celda in fila] for fila in b["filas"]]
    celdas = [[c[0] if len(c) == 1 else c for c in fila] for fila in filas]
    n = len(celdas[0])
    largos = [sum(len(c if isinstance(c, str) else " ".join(c)) for c in (f[k] for f in celdas[1:])) / max(1, len(celdas) - 1) for k in range(n)]
    a.tabla(None, celdas[0], celdas[1:], [1 + min(largo, 70) / 14 for largo in largos])


FIRMANTE = {"nombre": "GABRIELA PEDRAZA RUEDA", "cargo": "Directora Full Service Global", "correo": "gabriela.pedraza@campuslands.com"}
FIRMA_IMAGEN_GP = RAIZ / "recursos" / "marca" / "firma-gabriela-pedraza-campuslands.png"


def firmas(b1, b2):
    """Apartado de firma según el ejemplo del usuario: dos columnas iguales. Campuslands (izquierda) con su firma y los datos de la
    firmante; Unidrogas (derecha) con su espacio de firma y, en el lugar de los datos, «Nombre / cargo / fecha:» seguido de líneas para
    escribirlos. Los rótulos salen de las dos últimas líneas del archivo; las rayas bajas pasan a ser líneas dibujadas."""
    p1 = re.split(r"\s{2,}(?=\S)", texto(b1))
    p2 = re.split(r"\s{2,}(?=\S)", texto(b2))
    assert len(p1) == 2 and len(p2) == 2
    rotulo = lambda x: x.split(":")[0].strip() + ":"
    r_unidrogas, r_campuslands = (rotulo(x) for x in p1)
    assert r_unidrogas.startswith("Por Unidrogas") and r_campuslands.startswith("Por Campuslands")
    r_nombre = rotulo(p2[1])
    col, hueco = 4000, ANCHO_TEXTO - 8000
    t = a._tabla(3, [col, hueco, col])
    sin_borde = {"top": (None, 0), "left": (None, 0), "right": (None, 0), "bottom": (None, 0)}
    for fila in t.rows:
        a._fila(fila)
        for c in fila.cells:
            a._celda(c, bordes=sin_borde)
    t.rows[1]._tr.get_or_add_trPr().append(_el("w:trHeight", w_val=1250, w_hRule="atLeast"))

    def linea(celda, txt, negrita=False, color=None, tam=10.5, antes=0, primero=False):
        q = celda.paragraphs[0] if primero else celda.add_paragraph()
        q.style = "Normal"
        q.alignment = WD_ALIGN_PARAGRAPH.LEFT
        q.paragraph_format.space_before = Pt(antes)
        q.paragraph_format.space_after = Pt(2)
        q.paragraph_format.keep_with_next = True
        r = q.add_run(txt)
        r.bold = negrita or None
        r.font.size = Pt(tam)
        if color:
            r.font.color.rgb = color
        return q

    azul = RGBColor(0x0D, 0x49, 0x7B)
    gris = RGBColor(0x40, 0x40, 0x40)
    izq, der = 0, 2
    linea(t.rows[0].cells[izq], r_campuslands, negrita=True, color=azul, tam=11, primero=True)
    linea(t.rows[0].cells[der], r_unidrogas, negrita=True, color=azul, tam=11, primero=True)
    for c in (t.rows[1].cells[izq], t.rows[1].cells[der]):          # espacio de firma con su línea
        a._celda(c, bordes={"bottom": (TINTA, 8)})
        _insertar_ordenado(c._tc.get_or_add_tcPr(), _el("w:vAlign", w_val="bottom"), _TCPR_ORDEN)
        c.paragraphs[0].paragraph_format.keep_with_next = True
    q = t.rows[1].cells[izq].paragraphs[0]
    q.paragraph_format.space_after = Pt(1)
    q.add_run().add_picture(str(FIRMA_IMAGEN_GP), height=Twips(700))
    c = t.rows[2].cells[izq]
    linea(c, FIRMANTE["nombre"], negrita=True, color=azul, tam=11, antes=7, primero=True)
    linea(c, FIRMANTE["cargo"], color=gris)
    linea(c, FIRMANTE["correo"], color=gris)
    c = t.rows[2].cells[der]                                           # mismo lugar y estilo que los datos de la izquierda
    linea(c, r_nombre, negrita=True, color=azul, tam=11, antes=7, primero=True)
    for k in range(2):                                                 # dos líneas para escribir nombre, cargo y fecha
        if k:                                                          # separador mínimo: así las dos líneas no se fusionan en una
            sep = linea(c, "", tam=1)
            sep.paragraph_format.line_spacing = Pt(2)
            sep.paragraph_format.space_after = Pt(0)
        q = linea(c, "", tam=10.5)
        q.paragraph_format.line_spacing = Pt(24)
        q.paragraph_format.space_after = Pt(0)
        _borde_parrafo(q, "bottom", "7F7F7F", 4, 1)
    a._cierre_minimo()


primero = True
i = 0
while i < len(resto):
    b = resto[i]
    if b["t"] == "tbl":
        tabla(b)
    else:
        est, txt = b["estilo"], texto(b)
        if est == "Ttulo1":
            a.h1(txt)
        elif est == "Ttulo2":
            a.h2(txt)
        elif txt.startswith("Por Unidrogas S.A.:"):
            q = None
            firmas(resto[i], resto[i + 1])
            i += 1
        else:
            q = cuerpo(b, "Viñeta" if est == "Listaconvietas" else None)
            if primero:
                q.paragraph_format.page_break_before = True      # el contenido empieza en hoja nueva tras la tabla de contenido
            if txt.startswith("La firma de la versión contractual final"):
                q.paragraph_format.keep_with_next = True
        primero = False
    i += 1

a.guardar(SALIDA, "Alcance Funcional Consolidado — Unidrogas")
print(SALIDA)
