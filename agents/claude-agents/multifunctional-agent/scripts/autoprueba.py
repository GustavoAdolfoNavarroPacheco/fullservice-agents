"""Prueba de punta a punta del agente multifuncional con DATOS SINTÉTICOS (no usa archivos reales ni el motor de audio).

    python -X utf8 scripts/autoprueba.py [--conservar]

Facturas: genera recibos falsos (PDF con texto, PDF de 3 páginas, imagen sin texto, uno sin hora, uno con nombre de archivo
engañoso), corre inspeccionar + construir y comprueba el orden cronológico, una hoja por factura y el PDF final.
Transcripción: genera un .json de segmentos de ~12 min con dos hablantes, lo convierte en Word + PDF y comprueba las partes,
las etiquetas y la ida y vuelta .json → .md → Word.
Sale con código 0 si todo pasa.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont

import facturas
import transcripcion
from comun import configurar_consola, docx_a_pdf, paginas_pdf

FALLOS: list[str] = []


def verificar(condicion: bool, mensaje: str) -> None:
    print(("  ✓ " if condicion else "  ✗ ") + mensaje)
    if not condicion:
        FALLOS.append(mensaje)


# ---------------------------------------------------------------- datos sintéticos

def _pdf_recibo(ruta: Path, lineas: list[str], paginas: int = 1) -> None:
    doc = fitz.open()
    for p in range(paginas):
        pg = doc.new_page(width=595, height=842)
        y = 80
        for ln in lineas:
            pg.insert_text((60, y), ln if p == 0 else f"{ln} (pág. {p + 1})", fontsize=14)
            y += 26
        if paginas > 1:
            pg.insert_text((60, 700), "Detalle de consumo " * 3, fontsize=11)
    doc.save(str(ruta))


def _png_recibo(ruta: Path) -> None:
    img = Image.new("RGB", (900, 1100), "white")
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype("arial.ttf", 34)
    except OSError:
        f = ImageFont.load_default()
    for i, t in enumerate(["PARQUEADERO DEMO", "Ticket 0001", "Total $ 8.000"]):
        d.text((80, 100 + i * 70), t, fill="black", font=f)
    img.save(ruta)


def prueba_facturas(base: Path) -> None:
    print("\n== Facturas ==")
    lote = base / "lote-demo"
    entrada = lote / "entrada"
    entrada.mkdir(parents=True)
    # nombre de archivo ENGAÑOSO: dice 08h00m pero el recibo es de las 4:15 PM
    _pdf_recibo(entrada / "03112026 - 08h00m - Tienda.pdf", ["Tienda Demo S.A.S.", "Factura de venta", "Fecha: 03/11/2026", "Hora: 4:15 PM", "Total: COP 45,000"])
    _pdf_recibo(entrada / "03112026 - 17h00m - Restaurante.pdf", ["Restaurante Demo", "Date: November 3, 2026", "Start Time: 9:30 AM", "Total: COP 30,000"])
    _pdf_recibo(entrada / "hospedaje.pdf", ["Hotel Demo", "Fecha de emisión: 2026-11-02", "Hora: 21:10", "Total: COP 200,000"], paginas=3)
    _pdf_recibo(entrada / "sin-hora.pdf", ["Papelería Demo", "Fecha: 03/11/2026", "Total: COP 12,000"])
    _png_recibo(entrada / "parqueadero.png")

    facturas.cmd_inspeccionar(lote)
    manif = lote / "manifiesto.json"
    datos = json.loads(manif.read_text(encoding="utf-8"))
    por_archivo = {f["archivo"]: f for f in datos["facturas"]}
    verificar(por_archivo["03112026 - 08h00m - Tienda.pdf"]["hora"] == "16:15", "detecta la hora del recibo (16:15) y no la del nombre del archivo")
    verificar(por_archivo["03112026 - 17h00m - Restaurante.pdf"]["hora"] == "09:30", "detecta «Start Time: 9:30 AM» → 09:30")
    verificar(por_archivo["hospedaje.pdf"]["fecha"] == "2026-11-02", "detecta fecha ISO en un PDF de 3 páginas")
    verificar(por_archivo["parqueadero.png"]["fecha"] is None, "una imagen sin texto no inventa fecha")

    # el agente confirmaría a la vista; aquí se completa lo que la imagen no trae
    por_archivo["parqueadero.png"].update(fecha="2026-11-03", hora="11:05", proveedor="Parqueadero Demo", tipo="Peajes y parqueadero")
    por_archivo["hospedaje.pdf"].update(proveedor="Hotel Demo", tipo="Hospedaje")
    manif.write_text(json.dumps(datos, ensure_ascii=False), encoding="utf-8")

    rc = facturas.cmd_construir(lote, None, False)
    verificar(rc == 0, "construir termina sin error")
    docx = next((lote / "salida").glob("Facturas_*.docx"))
    pdf = docx.with_suffix(".pdf")
    verificar(pdf.exists(), f"existen el Word y el PDF ({docx.name})")
    verificar(docx.name == "Facturas_02-03_Noviembre_2026_Campuslands.docx", "el nombre usa el rango de fechas de los recibos")
    # 5 facturas: la de hospedaje ocupa 3 hojas → 7 hojas
    verificar(paginas_pdf(pdf) == 7, f"7 páginas = 5 facturas (una de 3 páginas): {paginas_pdf(pdf)}")

    items = [facturas._normalizar(f, entrada) for f in json.loads(manif.read_text(encoding="utf-8"))["facturas"]]
    orden = [i["archivo"] for i in facturas.ordenar(items)]
    esperado = ["hospedaje.pdf", "03112026 - 17h00m - Restaurante.pdf", "parqueadero.png", "03112026 - 08h00m - Tienda.pdf", "sin-hora.pdf"]
    verificar(orden == esperado, "orden cronológico por el contenido del recibo, sin hora al final de su día")
    with fitz.open(str(pdf)) as d:
        txt = "\n".join(p.get_text() for p in d)
    compacto = "".join(txt.split())                      # el banner tiene letras espaciadas: el texto extraído sale «F A C T U R A»
    verificar("FACTURA01/5" in compacto and "FACTURA(CONT.)01/5" in compacto and "MiéTIPO" not in compacto and "Lun2nov2026" in compacto,
              "el banner está en el PDF (fecha corta con día) y las hojas extra de una factura llevan «FACTURA (CONT.)»")
    verificar("no coincide con lo que dice el recibo" in txt, "la nota de discrepancia de nombre de archivo aparece en el documento")
    verificar("a. m." not in txt and "p. m." not in txt and "HORA" not in compacto, "la hora NO se imprime en el documento")
    verificar("Pág. 7/7" in txt, "el pie trae «Pág. N/M»")
    with fitz.open(str(pdf)) as d:
        familias = {f[3].split("+")[-1].rsplit("-", 1)[0] for pg in d for f in pg.get_fonts()}
    verificar("Poppins" in familias, "el PDF usa la tipografía Poppins")


# ---------------------------------------------------------------- transcripción

def prueba_transcripcion(base: Path) -> None:
    print("\n== Transcripción ==")
    segs = []
    t = 0.0
    frases = ["Buenos días, empecemos con el primer punto.", "Sí, claro. [Risas] Adelante.", "Gracias, Laura, por recibirnos.", "Con gusto, ingeniero."]
    for i in range(160):
        dur = 4.0 + (i % 3)
        segs.append({"inicio": round(t, 2), "fin": round(t + dur, 2), "hablante": 1 + (i % 2), "texto": frases[i % 4]})
        t += dur + 0.5
    datos = {"titulo": "Transcripción de Audio Completo", "audio": "reunion-demo.mp3", "duracion_s": round(t), "fecha": "2026-11-06", "parte_s": 300,
             "hablantes": {"1": {"nombre": None, "genero": "Hombre"}, "2": {"nombre": "Laura", "genero": "Mujer"}}, "segmentos": segs}
    trabajo = base / "trans" / "trabajo"
    trabajo.mkdir(parents=True)
    (trabajo / "segmentos.json").write_text(json.dumps(datos, ensure_ascii=False), encoding="utf-8")

    m = transcripcion.leer_json(trabajo / "segmentos.json")
    verificar(len(m.partes) == 3 and [p.n for p in m.partes] == [1, 2, 3], f"{len(m.partes)} partes de 5 min para ~{round(t / 60)} min de audio")
    verificar(m.partes[1].lineas[0].ini < "01:00", "los tiempos reinician en la parte 2")
    verificar(m.partes[0].lineas[0].etiqueta == "Hablante 1 (Hombre)" and m.partes[0].lineas[1].etiqueta == "Hablante 2 (Laura)", "etiquetas: «Hablante 1 (Hombre)», «Hablante 2 (Laura)»")
    verificar(all(ln.fin <= "05:00" for p in m.partes for ln in p.lineas), "ninguna línea termina después del corte de su parte")

    (trabajo / "transcripcion.md").write_text(transcripcion.a_md(m), encoding="utf-8")
    m2 = transcripcion.leer_md(trabajo / "transcripcion.md")
    verificar([ln.texto for p in m.partes for ln in p.lineas] == [ln.texto for p in m2.partes for ln in p.lineas], "ida y vuelta .json → .md sin perder texto")
    verificar(m2.audio == "reunion-demo.mp3", "el .md conserva los metadatos (audio, duración, fecha)")

    rc = transcripcion.cmd_construir(trabajo / "transcripcion.md", None, "Transcripcion - demo", None, None, False, False)
    verificar(rc == 0, "construir termina sin error")
    pdf = base / "trans" / "salida" / "Transcripcion - demo.pdf"
    verificar(pdf.exists() and (pdf.with_suffix(".docx")).exists(), "existen el Word y el PDF en salida/")
    with fitz.open(str(pdf)) as d:
        txt = "\n".join(p.get_text() for p in d)
    verificar("Parte 3" in txt and "Hablante 2 (Laura):" in txt and "[Risas]" in txt, "el PDF trae las 3 partes, las etiquetas y las acotaciones")
    verificar("Transcripción de Audio Completo" in txt, "el título es el de la referencia")


def main() -> int:
    configurar_consola()
    ap = argparse.ArgumentParser()
    ap.add_argument("--conservar", action="store_true", help="no borra la carpeta temporal de la prueba")
    a = ap.parse_args()
    base = Path(tempfile.mkdtemp(prefix="multifuncional-autoprueba-"))
    try:
        prueba_facturas(base)
        prueba_transcripcion(base)
    finally:
        if a.conservar:
            print(f"\nArchivos de la prueba en {base}")
        else:
            shutil.rmtree(base, ignore_errors=True)
    print("\n" + ("✓ Todo pasó." if not FALLOS else f"✗ {len(FALLOS)} comprobaciones fallaron:\n  - " + "\n  - ".join(FALLOS)))
    return 0 if not FALLOS else 1


if __name__ == "__main__":
    sys.exit(main())
