import re
import unicodedata
from pathlib import Path

def normalizar_nombre_carpeta(nombre) -> str:
    #Quitaremos acentos
    nombre = unicodedata.normalize("NFD", nombre)
    nombre = "".join(c for c in nombre if unicodedata.category(c) != "Mn")

    #Reemplazar todo lo que no sea numero o letra
    nombre = re.sub(r"[^A-Za-z0-9]+","_",nombre)

    return nombre.strip("_")


def crer_carpetas(base_path : Path,razon_social :str ) -> Path:

    nombre_carpeta = normalizar_nombre_carpeta(razon_social)
    empresa_path = base_path / nombre_carpeta


    sub_carpetas = [
        "A", "B", "C"
    ]

    empresa_path.mkdir(parents=True, exist_ok=True)

    for carpeta in sub_carpetas:
        (empresa_path/carpeta).mkdir(exist_ok=True)

    return empresa_path