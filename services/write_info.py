def informacion_escrita() -> dict:
    
    diccionario_info_escrita = {
        "actividad_economica" : None, 
        "numero_equipos" : None, 
    }

    for key in diccionario_info_escrita.keys():
        diccionario_info_escrita[key] = input(f"Meter información sobre '{key}'")

    return diccionario_info_escrita


