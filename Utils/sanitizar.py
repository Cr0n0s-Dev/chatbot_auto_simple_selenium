def sanitizar(name): 
    # Agregamos "predio" (por si el usuario escribe mal) y "precio de"
    prefixes = [
        "precio de la accion de", "precio de la accion", "precio de", "precio del", 
        "predio de", "precio", "predio", "accion de", "accion", "dame el", "de"
    ]
    
    name = name.lower().strip()

    # Eliminamos las palabras de ruido una por una
    for p in prefixes:
        # Usamos replace con espacio para no borrar letras dentro de palabras
        if name.startswith(p + " "):
            name = name[len(p):].strip()
        elif name == p:
            name = "" # Caso donde solo escriben la palabra prohibida
            
    return name