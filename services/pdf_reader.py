import pdfplumber
import sys
from pathlib import Path


def leer_constancia_sat(ruta_pdf: Path) -> str:
    if not ruta_pdf.exists():
        print("No se encontró la constancia SAT")
        sys.exit(1)

    texto_completo = ""

    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                texto_completo += texto + "\n"

    # Normalizamos texto
    texto_completo = texto_completo.replace("\n", " ")

    razon_social = None
    regimen_capital = None

    # Extracción simple (MVP)
    if "Denominación/Razón Social:" in texto_completo:
        razon_social = texto_completo.split(
            "Denominación/Razón Social:"
        )[1].split("Régimen")[0].strip()

    if "Régimen Capital:" in texto_completo:
        regimen_capital = texto_completo.split(
            "Régimen Capital:"
        )[1].split("Nombre Comercial")[0].strip()

    if not razon_social:
        print("No se pudo obtener la Razón Social del SAT")
        sys.exit(1)

    # Construcción del nombre final
    if regimen_capital:
        nombre_final = f"{razon_social}, {regimen_capital}"
    else:
        nombre_final = razon_social

    return nombre_final
