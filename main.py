from pathlib import Path
import sys 
from services.excel_reader import leer_excel
from core.empresa import Empresa
from core.proyecto import Proyecto 

INPUT_FOLDER = Path("input")
REQUIRED_FILES = ["CONSTANCIA_SITUACION_FISCAL.pdf", "INE_T1.pdf", "INE_T2.pdf", "FOR_28.xlsx", 
                  "INE_REPRESENTANTE.pdf","INE_VISITA.pdf"]
RUTA_EXCEL = Path('input/FOR_28.xlsx')


# Funciones encargadas de validación de los documentos y carpetas
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
    
    #Creando el objeto empresa

    empresa = Empresa(
        razon_social_propietario=None, 
        razon_social_usuario= None, 
        rfc= None,
        actividad_economica=None,
        domicilio= None,
        telefono= None,
        empresa_a_facturar=empresa_a_facturar
        )
    
    #Creando objeto de el proyecto
    proyecto = Proyecto(
        id_proyecto= "1_D",
        empresa= empresa,
        numero_equipos=0,
        estado="CREADO",
        warnings= None
        )
    
    # print(f'''Proyecto creado exitosamente:
    #     ID : {proyecto.id_proyecto}
    #     num equipos : {proyecto.numero_equipos}
    #     empresa : {proyecto.empresa.empresa_a_facturar}
    #     estado : {proyecto.estado}''')

    

if __name__ == "__main__":
    main()
