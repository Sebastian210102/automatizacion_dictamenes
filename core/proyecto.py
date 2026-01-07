class Proyecto: 

    def __init__(self, id_proyecto : str, empresa : object, numero_equipos : int ,
                 estado : str, warnings : list = None):
        
        self.id_proyecto = id_proyecto
        self.empresa = empresa
        self.numero_equipos = numero_equipos
        self.estado = estado
         
        if warnings is None:
            self.warnings = []
        else:
            self.warnings = warnings
        