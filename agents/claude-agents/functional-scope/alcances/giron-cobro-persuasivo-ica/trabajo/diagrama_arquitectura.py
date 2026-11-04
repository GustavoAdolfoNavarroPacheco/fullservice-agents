"""Diagrama de arquitectura de alto nivel (sección 9), dibujado solo con lo que describe la propuesta del 2026-10-28.

Uso: python diagrama_arquitectura.py <salida.png>
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

AZUL, VERDE, TINTE, TINTA, GRIS = "#0D497B", "#5DAC6D", "#EEF3F8", "#262626", "#595959"
VERDE_T = "#E8F4EB"
W, H = 2400, 1230


def fuente(tam, negrita=False):
    nombre = "calibrib.ttf" if negrita else "calibri.ttf"
    return ImageFont.truetype(rf"C:\Windows\Fonts\{nombre}", tam)


img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def caja(x0, y0, x1, y1, titulo, lineas=(), relleno=TINTE, borde=AZUL, tam_t=34, tam_l=28):
    d.rounded_rectangle((x0, y0, x1, y1), radius=18, fill=relleno, outline=borde, width=4)
    ft, fl = fuente(tam_t, True), fuente(tam_l)
    alto_total = tam_t + 8 + len(lineas) * (tam_l + 6)
    y = y0 + ((y1 - y0) - alto_total) // 2
    d.text(((x0 + x1) // 2, y), titulo, font=ft, fill=AZUL, anchor="ma")
    y += tam_t + 12
    for ln in lineas:
        d.text(((x0 + x1) // 2, y), ln, font=fl, fill=TINTA, anchor="ma")
        y += tam_l + 6


def zona(x0, y0, x1, y1, titulo, color):
    d.rounded_rectangle((x0, y0, x1, y1), radius=26, outline=color, width=5, fill="white")
    d.text(((x0 + x1) // 2, y0 + 18), titulo, font=fuente(34, True), fill=color, anchor="ma")


def flecha(p0, p1, doble=False, color=GRIS, ancho=5):
    d.line((p0, p1), fill=color, width=ancho)
    import math
    def punta(a, b):
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        l = 22
        pts = [b,
               (b[0] - l * math.cos(ang - 0.45), b[1] - l * math.sin(ang - 0.45)),
               (b[0] - l * math.cos(ang + 0.45), b[1] - l * math.sin(ang + 0.45))]
        d.polygon(pts, fill=color)
    punta(p0, p1)
    if doble:
        punta(p1, p0)


def etiqueta(x, y, texto, tam=26):
    d.text((x, y), texto, font=fuente(tam), fill=GRIS, anchor="mm")


# --- zonas
zona(40, 40, 560, 1120, "Personas", GRIS)
zona(620, 40, 1330, 1120, "Infraestructura de la Alcaldía (nube privada)", AZUL)
zona(1400, 40, 1990, 1120, "Servicios en la nube", VERDE)
zona(2050, 40, 2360, 1120, "Contribuyente", GRIS)

# --- personas
caja(80, 170, 520, 420, "Funcionarios y alcalde", ["Dirección de Industria y", "Comercio, TIC y visitadores", "Computador o celular"])
caja(80, 640, 520, 900, "Equipo de Campuslands", ["Soporte y operación", "Acceso por VPN con", "usuarios nominales"])

# --- Alcaldía
caja(670, 150, 1280, 400, "Servidor de aplicación", ["API · Frontend web (Vue.js)", "Workers y colas (Redis)", "Proxy HTTPS con certificado", "del dominio de la Alcaldía"])
caja(670, 470, 1280, 640, "Servidor de base de datos", ["MariaDB: cartera, contactos,", "trazabilidad"])
caja(670, 700, 1280, 860, "Almacenamiento", ["Grabaciones, transcripciones", "y documentos"])
caja(670, 920, 1280, 1100, "Fuentes institucionales", ["MAT-SIM · SICOG II · Contratos", "Recaudo del operador oficial"], relleno=VERDE_T, borde=VERDE)

# --- nube
caja(1440, 130, 1950, 270, "Retell AI", ["Agente de voz"], relleno=VERDE_T, borde=VERDE)
caja(1440, 320, 1950, 460, "Twilio o Telnyx", ["Telefonía, números colombianos"], relleno=VERDE_T, borde=VERDE)
caja(1440, 510, 1950, 650, "WhatsApp Business", ["API de Meta"], relleno=VERDE_T, borde=VERDE)
caja(1440, 700, 1950, 840, "Proveedor de correo", ["Dominio institucional"], relleno=VERDE_T, borde=VERDE)
caja(1440, 890, 1950, 1030, "Modelo de lenguaje", ["Proveedor por definir"], relleno=VERDE_T, borde=VERDE)
d.text((1695, 1075), "Cámara de Comercio: 2 APIs externas", font=fuente(26), fill=GRIS, anchor="mm")

# --- contribuyente
caja(2090, 300, 2320, 840, "Contribuyente", ["Recibe", "WhatsApp,", "correo y", "llamada del", "asistente", "virtual de", "la Alcaldía"])

# --- flechas
flecha((520, 295), (670, 295), doble=True)                  # funcionarios <-> aplicación
flecha((975, 400), (975, 470), doble=True)                  # app <-> BD
flecha((975, 640), (975, 700), doble=True)                  # BD <-> almacenamiento
flecha((520, 770), (670, 770), doble=True)                  # Campuslands <-> servidores
flecha((975, 860), (975, 920), doble=True)                  # almacenamiento <-> fuentes
d.line(((1305, 200), (1305, 960)), fill=GRIS, width=5)      # bus HTTPS
flecha((1280, 275), (1305, 275))
for y in (200, 390, 580, 770, 960):
    flecha((1305, y), (1440, y), doble=True)
flecha((1695, 270), (1695, 320))                            # Retell -> telefonía
for y in (390, 580, 770):
    flecha((1950, y), (2090, y))                            # telefonía / WhatsApp / correo -> contribuyente
d.text((1200, 1180), "Aplicación ↔ servicios en la nube: HTTPS y webhooks · Funcionarios: red interna · Campuslands y fuentes institucionales: VPN",
       font=fuente(28), fill=GRIS, anchor="mm")

img.save(sys.argv[1])
print(sys.argv[1])
