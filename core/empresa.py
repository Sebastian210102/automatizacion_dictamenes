class Empresa: 
    
    def __init__(self, razon_social_propietario: str, razon_social_usuario: str,
                 rfc : str, actividad_economica : str, domicilio : str,
                 telefono : str, empresa_a_facturar : str ):
     
        self.razon_social_usuario = razon_social_propietario
        self.razon_social_usuario = razon_social_usuario
        self.rfc = rfc
        self.actividad_economica = actividad_economica
        self.domicilio = domicilio
        self.telefono = telefono
        self.empresa_a_facturar = empresa_a_facturar
        