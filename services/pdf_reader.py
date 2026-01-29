import pdfplumber
import sys
from pathlib import Path





def leer_constancia_sat(ruta_pdf: Path) -> str:
    if not ruta_pdf.exists():
        print("No se encontró la constancia SAT")
        sys.exit(1)
    diccionario_datos = {
        "razon_social" : None,
        "regimen_capital" : None,
        "rfc" : None,
        "actividad_economica" : None
    }
    texto_completo = ""

    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                texto_completo += texto + "\n"


    texto_completo = texto_completo.replace("\n", "")
    razon_social = None
    regimen_capital = None
    if "Denominación/RazónSocial" in texto_completo : 
        razon_social = texto_completo.split("Denominación/RazónSocial:"
                                            )[1].split("RégimenCapital")[0].strip()
        diccionario_datos["razon_social"] = razon_social
    if "RégimenCapital" in texto_completo:
        regimen_capital = texto_completo.split("RégimenCapital:"
                                               )[1].split("NombreComercial")[0].strip()
        diccionario_datos["regimen_capital"] = regimen_capital
    if not razon_social:
        print("No se pudo obtener razón social del SAT")





    return diccionario_datos


# print(leer_constancia_sat(Path("../input/CONSTANCIA_SITUACION_FISCAL.pdf")))

def normalizar_nombre_empresa(diccionario_datos : dict) -> str:
    # Separar palabras del nombre (heurística simple)
    nombre = diccionario_datos["razon_social"].upper()

    # Mapeo explícito de regímenes
    MAPEO_REGIMEN = {
        "SOCIEDADDERESPONSABILIDADLIMITADADECAPITALVARIABLE": "S. DE R.L. DE C.V."
    }

    regimen = MAPEO_REGIMEN.get(diccionario_datos["regimen_capital"], diccionario_datos["regimen_capital"])

    return f"{nombre}, {regimen}"



