"""Banner que encabeza cada factura del documento unificado.

ESTE ES EL ÚNICO ARCHIVO QUE HAY QUE TOCAR PARA CAMBIAR EL DISEÑO DEL BANNER (el usuario lo seguirá mejorando).
`facturas.py` solo llama a `agregar_banner(...)` y no sabe nada del diseño. Mientras la función conserve su firma,
se puede rediseñar por completo (otros colores, logo como imagen, más campos, etc.).

Diseño vigente (v2, 2026-11-06):
  Una sola franja SIMÉTRICA de cuatro celdas iguales y centradas: FACTURA (01 / N) · FECHA · TIPO · PROVEEDOR,
  con el mismo filete azul arriba y abajo y divisores finos entre celdas.
  La marca (logo y membrete) ya la pone la plantilla Word de Campuslands, así que se quitó la barra superior de la v1.
  La HORA ya no se muestra (la hora sigue usándose para ordenar, pero no se imprime).
Tipografía: Poppins. Es una tabla de Word, a todo el ancho del texto.
"""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from xml.sax.saxutils import escape

from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from comun import fecha_corta_con_dia

# ---- paleta y tipografía del banner (cambiar aquí). Paleta del membrete de la plantilla Campuslands.
AZUL = "0D497B"          # filetes y número de factura
FONDO = "EEF3F8"         # fondo de la franja
DIVISOR = "C9D6E3"       # líneas finas entre celdas
ETIQUETA = "5B6B7F"      # FACTURA / FECHA / TIPO / PROVEEDOR
VALOR = "1B2A3A"         # valores
FUENTE = "Poppins"

N_COLUMNAS = 4           # cuatro celdas iguales: la franja es simétrica


@dataclass
class DatosFactura:
    """Lo que el banner necesita saber de una factura. `hora` se conserva para ordenar, pero este diseño NO la imprime."""
    fecha: dt.date
    hora: dt.time | None
    tipo: str
    proveedor: str


def _run(texto: str, color: str, sz: int, negrita=False, espaciado: int | None = None) -> str:
    return (f'<w:r><w:rPr><w:rFonts w:ascii="{FUENTE}" w:cs="{FUENTE}" w:eastAsia="{FUENTE}" w:hAnsi="{FUENTE}"/>'
            + ("<w:b/><w:bCs/>" if negrita else "") + f'<w:color w:val="{color}"/>'
            + (f'<w:spacing w:val="{espaciado}"/>' if espaciado else "")
            + f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr><w:t xml:space="preserve">{escape(texto)}</w:t></w:r>')


def _parrafo(runs: str) -> str:
    return f'<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>{runs}</w:p>'


def _celda(ancho: int, ultima: bool, etiqueta: str, valor_runs: str) -> str:
    derecha = ('<w:right w:val="none" w:sz="0" w:color="FFFFFF"/>' if ultima
               else f'<w:right w:val="single" w:sz="4" w:space="0" w:color="{DIVISOR}"/>')
    bordes = (f'<w:top w:val="single" w:sz="12" w:space="0" w:color="{AZUL}"/><w:left w:val="none" w:sz="0" w:color="FFFFFF"/>'
              f'<w:bottom w:val="single" w:sz="12" w:space="0" w:color="{AZUL}"/>{derecha}')
    mar = '<w:tcMar><w:top w:w="110" w:type="dxa"/><w:left w:w="80" w:type="dxa"/><w:bottom w:w="110" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
    return (f'<w:tc><w:tcPr><w:tcW w:w="{ancho}" w:type="dxa"/><w:tcBorders>{bordes}</w:tcBorders>'
            f'<w:shd w:val="clear" w:color="auto" w:fill="{FONDO}"/>{mar}<w:vAlign w:val="center"/></w:tcPr>'
            + _parrafo(_run(etiqueta, ETIQUETA, 13, negrita=True, espaciado=20)) + _parrafo(valor_runs) + '</w:tc>')


def agregar_banner(doc, indice: int, total: int, datos: DatosFactura, ancho_twips: int, continuacion: bool = False) -> None:
    """Agrega al final del documento el banner de la factura `indice` de `total`.

    ancho_twips: ancho útil de la página (texto) en twips.
    continuacion: True cuando la factura sigue en otra hoja (se repite el banner con «FACTURA (CONT.)»).
    """
    ancho_col = ancho_twips // N_COLUMNAS
    anchos = [ancho_col] * (N_COLUMNAS - 1) + [ancho_twips - ancho_col * (N_COLUMNAS - 1)]
    celdas = [
        ("FACTURA (CONT.)" if continuacion else "FACTURA",
         _run(f"{indice:02d}", AZUL, 26, negrita=True) + _run(f" / {total}", ETIQUETA, 17)),
        ("FECHA", _run(fecha_corta_con_dia(datos.fecha), VALOR, 17, negrita=True)),
        ("TIPO", _run(datos.tipo or "—", VALOR, 17, negrita=True)),
        ("PROVEEDOR", _run(datos.proveedor or "—", VALOR, 17, negrita=True)),
    ]
    cuerpo = "".join(_celda(w, i == len(celdas) - 1, etq, val) for i, (w, (etq, val)) in enumerate(zip(anchos, celdas)))
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in anchos)
    xml = (f'<w:tbl {nsdecls("w")}><w:tblPr><w:tblW w:w="{ancho_twips}" w:type="dxa"/><w:jc w:val="center"/><w:tblLayout w:type="fixed"/></w:tblPr>'
           f'<w:tblGrid>{grid}</w:tblGrid><w:tr><w:trPr><w:cantSplit/></w:trPr>{cuerpo}</w:tr></w:tbl>')

    body = doc.element.body
    sect = body.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr")
    tabla = parse_xml(xml)
    (sect.addprevious(tabla) if sect is not None else body.append(tabla))
