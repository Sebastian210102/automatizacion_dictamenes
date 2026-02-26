import re
import unicodedata
from core.proyecto import Proyecto
from pathlib import Path
import os

def normalizar_nombre_carpeta(nombre) -> str:
    #Quitaremos acentos
    nombre = unicodedata.normalize("NFD", nombre)
    nombre = "".join(c for c in nombre if unicodedata.category(c) != "Mn")

    #Reemplazar todo lo que no sea numero o letra
    nombre = re.sub(r"[^A-Za-z0-9]+","_",nombre)

    return nombre.strip("_")


def crer_carpetas(base_path : Path,razon_social :str, proyecto : Proyecto ) -> Path:

    tipo_tanque = input("Ingrese el tipo de tanque (R para recipiente,G generador ): ").upper()
    nombre_carpeta = f'{normalizar_nombre_carpeta(razon_social)}_({proyecto.numero_equipos}{tipo_tanque})'
   
    empresa_path = base_path / nombre_carpeta

    sub_carpetas = [
        "A", "B", "C"
    ]

    empresa_path.mkdir(parents=True, exist_ok=True)

    for carpeta in sub_carpetas:
        (empresa_path/carpeta).mkdir(exist_ok=True)

    return empresa_path, tipo_tanque


    
def nombre_excel_empresa(nombre_empresa : str, nombre_actual: str) -> str:
    nombre_normalizado = normalizar_nombre_carpeta(nombre_empresa)
    os.rename(nombre_actual, f"{nombre_normalizado}.xlsx")
    return f"{nombre_normalizado}.xlsx"
