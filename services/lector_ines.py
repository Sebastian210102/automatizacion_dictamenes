from pathlib import Path
import pdfplumber
from PIL import ImageOps
import pytesseract
import re

PATH = Path("../input/INE_T1.pdf")

def pdf_a_imagen(path: Path):
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[0]
        img = page.to_image(resolution=300).original
        img = ImageOps.grayscale(img)
        img = ImageOps.autocontrast(img)
        return img
    
def recortar_zona_tarjeta(img):
    width, height = img.size

    #Ajustar según la INE
    left = width * 0.1
    right = width * 0.9
    top = height * 0.2
    bottom = height * 0.6

    return img.crop((left,top,right,bottom))


def recortar_nombre(img_tarjeta):
    width , height = img_tarjeta.size

    left = width * 0.05
    right = width * 0.7
    top = height * 0.25
    bottom = height * 0.5

    return img_tarjeta.crop((left, top, right, bottom))


def ocr_nombre(img_nombre):
    texto = pytesseract.image_to_string(
        img_nombre,
        lang = 'spa',
        config= "--psm 7"
    )

    return texto

def limpiar_nombre(texto):
    texto = texto.upper()
    texto = re.sub(r"[^A-ZÁÉÍÓÚÑ ]", "", texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()

def nombre_valido(nombre):
    partes = nombre.split()
    return len(partes) >= 2 and all(len(p) > 2 for p in partes)

def extraer_nombre_ine(path: Path):
    img = pdf_a_imagen(path)
    tarjeta = recortar_zona_tarjeta(img)
    nombre_img = recortar_nombre(tarjeta)

    raw = ocr_nombre(nombre_img)
    nombre = limpiar_nombre(raw)

    if not nombre_valido(nombre):
        return None  # o marcar para revisión manual

    return nombre


print(extraer_nombre_ine(PATH))