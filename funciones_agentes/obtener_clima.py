import requests # Librería para hacer peticiones HTTP (consultar webs)
from Utils.sanitizar import sanitizar

def obtener_clima(user_input):
    # Limpiamos el input para extraer solo la ciudad
    city = sanitizar(user_input)

    try: 
        # Consultamos wttr.in. format=3 devuelve una línea simple (Ciudad: Clima Temp)
        response = requests.get(f"http://wttr.in/{city}?format=3", timeout=10) 
        
        if response.status_code == 200: # Si la respuesta del servidor es OK
            return response.text.strip()
        else:
            return f"No se pudo encontrar el clima para la ciudad: {city}."
    except Exception as e:
        return f"Error al conectar con el servicio de clima: {str(e)}"