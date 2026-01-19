from core.persona import Persona

ROLES = ['representante', 'testigo_1', 'testigo_2', 'visita'] 


class Proyecto: 
    # Contructor


    def __init__(self, id_proyecto : str, empresa : object, numero_equipos : int ,
                 estado : str, warnings : list = None):
        
        self.id_proyecto = id_proyecto
        self.empresa = empresa
        self.numero_equipos = numero_equipos
        self.estado = estado
        self.personas = []
        if warnings is None:
            self.warnings = []
        else:
            self.warnings = warnings

    #Metodos
    def agregar_persona(self, persona : object):
        if not isinstance(persona, Persona):
            self.warnings.append("Objeto agregado no es Persona")
            return
        
        if not persona.rol:
            self.warnings.append("Persona sin rol definido")
            return

        roles_existentes = [p.rol for p in self.personas]

        if persona.rol in roles_existentes:
            self.warnings.append(f'Rol duplicado : {persona.rol}')
            return
        
        self.personas.append(persona)
        
    def resumen_proyecto(self):
        roles_presentes = [persona.rol for persona in self.personas]
        diccionario_resumen = {
            "ID_Proyecto" : self.id_proyecto,
            "Estado" : self.estado,
            "Numero_quipos" : self.numero_equipos,
            "Empresa" : {
                "razon_social_propetario" : self.empresa.razon_social_propietario,
                "razon_social_usuario" : self.empresa.razon_social_usuario
            },
            "Personas" : {
                "num_personas" : len(self.personas),
                "roles_en_proyecto" :  [persona.rol for persona in self.personas],
                "Roles_faltantes" : [rol for rol in ROLES if rol not in roles_presentes] 
            }
        }
    