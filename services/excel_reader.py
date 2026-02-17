from pathlib import Path
from openpyxl import load_workbook
import sys



def leer_excel(ruta_excel : Path, celda : str) -> str:
    excel = load_workbook(filename = ruta_excel)
    hoja = excel.active

    
    informacion = hoja[celda].value
    
    if informacion is None:
        print(f"El valor en celda {celda} es vacio en {ruta_excel}")
        sys.exit(1)
    


    return informacion
    