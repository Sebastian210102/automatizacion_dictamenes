class Persona: 

    def __init__(self, nombre_completo : str, rol : str, warnings : list = None):

        self.nombre_completo = nombre_completo
        self.rol = rol

        if warnings is None:
            self.warnings = []
        else:
            self.warnings = warnings
        