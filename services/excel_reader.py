from pathlib import Path
from openpyxl import load_workbook
import sys



def leer_excel(ruta_excel : Path) -> str:
    excel = load_workbook(filename = ruta_excel)
    hoja = excel.active

    
    empresa_a_facturar = hoja['C14'].value
    
    if empresa_a_facturar is None:
        print("El valor en celda es vacio")
        sys.exit(1)
    


    return empresa_a_facturar
    