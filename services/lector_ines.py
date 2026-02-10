from pathlib import Path
import pdfplumber
from pathlib import Path
import pandas as pd


# PATH = Path('../input/CONSTANCIA_SITUACION_FISCAL.pdf')
PATH = Path('../input/INE_T1.pdf')



def leer_nombres(path: Path) -> str:
    texto_completo = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            texto = page.extract_words()

            if texto:
                texto_completo += texto + "\n"
    
    print(texto_completo)

leer_nombres(PATH)