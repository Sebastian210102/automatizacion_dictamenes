from pathlib import Path
import sys 

from services.excel_reader import leer_excel
from services.pdf_reader import leer_constancia_sat, normalizar_nombre_empresa
from services.creacion_carpeta import crer_carpetas
from services.write_info import informacion_escrita
from services.excel_writer import escribir_excel
from services.mover_archivos import mover_archivo

from core.empresa import Empresa
from core.proyecto import Proyecto 
from core.persona import Persona

INPUT_FOLDER = Path("input")
REQUIRED_FILES = ["CONSTANCIA_SITUACION_FISCAL.pdf", "FOR_28.xlsx"]
RUTA_EXCEL = Path('input/FOR_28.xlsx')
RUTA_CONSTANCIA = Path("input/CONSTANCIA_SITUACION_FISCAL.pdf")
BASE_EMPRESA = Path("output/empresas")
RUTA_EXCEL_FINAL = Path("input/EXCEL_FINAL.xlsx")

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

    # VERIFICACION DE LOS ARCHIVOS
    verificacion_carpeta(INPUT_FOLDER)

    for file in REQUIRED_FILES:
        file_path = Path(INPUT_FOLDER/file)
        verificacion_documento(file_path)
    


    #Obtener los datos de la empresa
    empresa_a_facturar = leer_excel(RUTA_EXCEL,'C14')
    print(f'Empresa a facturar : "{empresa_a_facturar}"')
    diccionario_datos = leer_constancia_sat(RUTA_CONSTANCIA)
    razon_social_empresa =normalizar_nombre_empresa(diccionario_datos)
    if  len(razon_social_empresa) <= 3:
        print("No se registro de menera correcta la razon social")
        sys.exit(1)
    
    diccionario_informacion_escrita = informacion_escrita()


    #Creando el objeto empresa

    empresa = Empresa(
        razon_social_propietario=razon_social_empresa, 
        razon_social_usuario= razon_social_empresa, 
        rfc= diccionario_datos["rfc"],
        actividad_economica=diccionario_informacion_escrita["actividad_economica"],
        domicilio= diccionario_informacion_escrita["domicilio"],
        telefono= diccionario_informacion_escrita["telefono"],
        empresa_a_facturar=empresa_a_facturar
        )
    

    #Cracion de la carpeta
    ruta_empresa = crer_carpetas(BASE_EMPRESA, empresa.razon_social_usuario)

    print(f'Empresa creada en: {ruta_empresa}')    

    #Creando objeto de el proyecto
    proyecto = Proyecto(
        id_proyecto= "1_D",
        empresa= empresa,
        numero_equipos=diccionario_informacion_escrita["numero_equipos"],
        estado="CREADO",
        warnings= None
        )

    
    #Creación de el objeto persona 

    nombre_atiende_visita = leer_excel(RUTA_EXCEL, "C10").upper()
    nombre_testigo_1 = leer_excel(RUTA_EXCEL, "C11").upper()
    nombre_testigo_2 = leer_excel(RUTA_EXCEL, "C12").upper()
    nombre_representante = leer_excel(RUTA_EXCEL,"C5").upper()

    Persona_antendio_visita = Persona(
        nombre_completo = nombre_atiende_visita,
        rol= "Atiende la visita"
    )
    Persona_testigo_1 = Persona(
        nombre_completo= nombre_testigo_1,
        rol = "Testigo1"
    )
    Persona_testigo_2 = Persona(
        nombre_completo= nombre_testigo_2,
        rol = "Testigo2"
    )
    Persona_representante = Persona(
        nombre_completo= nombre_representante,
        rol = "Representante legal"
    )


    #Escribir en excel
    escribir_excel(empresa, RUTA_EXCEL_FINAL, proyecto, Persona_antendio_visita, Persona_testigo_1, 
                   Persona_testigo_2, Persona_representante)


    #Mover archivos a las carpetas

    mover_archivo(RUTA_CONSTANCIA, f'{ruta_empresa}/B')
    mover_archivo(RUTA_EXCEL, f'{ruta_empresa}/C')

    print(f'''Proyecto creado exitosamente:
        ID : {proyecto.id_proyecto}
        num equipos : {proyecto.numero_equipos}
        empresa : {proyecto.empresa.empresa_a_facturar}
        estado : {proyecto.estado}
        Razon social: {empresa.razon_social_usuario}
        RFC : {empresa.rfc}''')
    
if __name__ == "__main__":
    main()
