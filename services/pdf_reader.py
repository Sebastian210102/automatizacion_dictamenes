import pdfplumber
import sys
from pathlib import Path

RUTA_CONSTANCIA = Path('../input/CONSTANCIA_SITUACION_FISCAL.pdf')



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


    texto_completo = texto_completo.replace("\n", "")
    razon_social = None
    regimen_capital = None
    if "Denominación/RazónSocial" in texto_completo : 
        razon_social = texto_completo.split("Denominación/RazónSocial:"
                                            )[1].split("RégimenCapital")[0].strip()
    
    if "RégimenCapital" in texto_completo:
        regimen_capital = texto_completo.split("RégimenCapital:"
                                               )[1].split("NombreComercial")[0].strip()
    
    if not razon_social:
        print("No se pudo obtener razón social del SAT")


    #Contricción del nombre final 
    if regimen_capital:
        nombre_final = f"{razon_social}, {regimen_capital}"
    else:
        nombre_final = razon_social

    return razon_social, regimen_capital


razon_social, regimen_capital = leer_constancia_sat(RUTA_CONSTANCIA)

def normalizar_nombre_empresa(razon_social: str, regimen_raw: str) -> str:
    # Separar palabras del nombre (heurística simple)
    nombre = razon_social.upper()

    # Mapeo explícito de regímenes
    MAPEO_REGIMEN = {
        "SOCIEDADDERESPONSABILIDADLIMITADADECAPITALVARIABLE": "S. DE R.L. DE C.V."
    }

    regimen = MAPEO_REGIMEN.get(regimen_raw, regimen_raw)

    return f"{nombre}, {regimen}"




print(normalizar_nombre_empresa(razon_social, regimen_capital))