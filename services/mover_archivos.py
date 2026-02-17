import os
import shutil
from pathlib import Path



def mover_archivo(origen : Path, destino : Path):
    origen = Path(origen)
    destino = Path(destino)

    if os.path.exists(origen):
        shutil.move(origen, destino)
        print("Archivo movido correctamente")
    else:
        print("El archivo no existe")




