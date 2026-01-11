from pathlib import Path
import sys 
from services.excel_reader import leer_excel

INPUT_FOLDER = Path("input")
REQUIRED_FILES = ["CONSTANCIA_SITUACION_FISCAL.pdf", "INE_T1.pdf", "INE_T2.pdf", "FOR_28.xlsx", 
                  "INE_REPRESENTANTE.pdf","INE_VISITA.pdf"]
RUTA_EXCEL = Path('input/FOR_28.xlsx')



def verificacion_carpeta(directorio):

    if directorio.exists() and directorio.is_dir():
        print("La carpeta input existe, por lo que se puede seguir")
    else:
        print("Verificar que la carpeta existe o esta mal escrita")
        sys.exit(1)


def verificacion_documento(documento):
    if documento.exists() and documento.is_file():
        print(f'Documento "{documento}" cargado correctamente')
    else:
        print(f'Documento "{documento}" no se encuentra')
        sys.exit(1)

def main():

    verificacion_carpeta(INPUT_FOLDER)

    for file in REQUIRED_FILES:
        file_path = Path(INPUT_FOLDER/file)
        verificacion_documento(file_path)
    
    empresa_a_facturar = leer_excel(RUTA_EXCEL)
    print(f'Empresa a facturar : "{empresa_a_facturar}"')

if __name__ == "__main__":
    main()
