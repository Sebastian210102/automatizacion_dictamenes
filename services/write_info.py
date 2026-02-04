def informacion_escrita() -> dict:
    
    diccionario_info_escrita = {
        "actividad_economica" : None, 
        "numero_equipos" : None, 
        "domicilio" : None, 
        "telefono" : None,
    }

    for key in diccionario_info_escrita.keys():
        diccionario_info_escrita[key] = input(f"Meter información sobre '{key}'")

    return diccionario_info_escrita


print(informacion_escrita())