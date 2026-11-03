"""Renderiza un .docx a PDF (LibreOffice) y a PNG (una imagen por página) para revisarlo a la vista.

Uso: python scripts/previsualizar.py "<archivo.docx>" <carpeta-salida> [escala]

Al final avisa de las páginas con mucho espacio vacío (ocupación < 60 %, salvo portada, carta, tabla de contenido y última hoja):
el documento debe evitar esos huecos.

Requiere LibreOffice (winget install TheDocumentFoundation.LibreOffice) y pypdfium2.
LibreOffice no actualiza campos: la tabla de contenido se verá con su texto de relleno hasta que se
actualice en Word (clic derecho → Actualizar campo).
"""
import subprocess
import sys
from pathlib import Path

import pypdfium2 as pdfium

SOFFICE = Path(r"C:\Program Files\LibreOffice\program\soffice.exe")

docx = Path(sys.argv[1]).resolve()
salida = Path(sys.argv[2]).resolve()
escala = float(sys.argv[3]) if len(sys.argv) > 3 else 1.1
salida.mkdir(parents=True, exist_ok=True)
subprocess.run([str(SOFFICE), "--headless", "--convert-to", "pdf", "--outdir", str(salida), str(docx)],
               check=True, capture_output=True, timeout=180)
pdf = pdfium.PdfDocument(str(salida / (docx.stem + ".pdf")))
print("páginas:", len(pdf))
for i in range(len(pdf)):
    ruta = salida / f"{docx.stem}-{i + 1}.png"
    pdf[i].render(scale=escala).to_pil().save(ruta)
    print(ruta)

# Ocupación de cada página (zona de texto, sin membrete ni pie): detecta huecos grandes.
import numpy as np

huecos = []
for i in range(len(pdf)):
    img = np.array(pdf[i].render(scale=0.3).to_pil().convert("L"))
    zona = img[int(img.shape[0] * 0.14):int(img.shape[0] * 0.90)]
    filas = np.where((zona < 200).sum(axis=1) > 0)[0]
    ocupacion = filas.max() / zona.shape[0] if len(filas) else 0
    if 2 < i < len(pdf) - 1 and ocupacion < 0.6:
        huecos.append((i + 1, round(ocupacion * 100)))
print("páginas con huecos (página, % ocupado):", huecos if huecos else "ninguna")
