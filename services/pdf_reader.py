import pdfplumber
import sys
from pathlib import Path



def restricciones(inicio, fin ,texto_completo)-> str : 
    if inicio in texto_completo:
        return texto_completo.split(inicio)[1].split(fin)[0].strip()
    else:
        print(f"{inicio} no encontrado")


def leer_constancia_sat(ruta_pdf: Path) -> str:

    if not ruta_pdf .exists():
        print("No se encontró la constancia SAT")
        sys.exit(1)
    diccionario_datos = {
        "razon_social" : None,
        "regimen_capital" : None,
        "rfc" : None
    }
    texto_completo = ""
    RAZON_SOCIAL = None
    REGIMEN_CAPITAL = None
    RFC = None

    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                texto_completo += texto + "\n"


    texto_completo = texto_completo.replace("\n", "")
   
    RFC = restricciones("RFC: ", "Denominación", texto_completo, )
    diccionario_datos["rfc"] = RFC
    RAZON_SOCIAL = restricciones("Denominación/RazónSocial:","RégimenCapital", texto_completo)
    diccionario_datos["razon_social"] = RAZON_SOCIAL
    REGIMEN_CAPITAL = restricciones("RégimenCapital:", "NombreComercial", texto_completo)
    diccionario_datos["regimen_capital"] = REGIMEN_CAPITAL
    # return diccionario_datos
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



