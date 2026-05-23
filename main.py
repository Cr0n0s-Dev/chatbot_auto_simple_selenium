#Fecha de finalización: 23 de mayo del 2026
#Desarrollador: Iván Hernández
#Chatbot simple con agentes especializados para obtener el clima y precios de acciones, usando Selenium para automatizar tareas web si es necesario. Este es el punto de entrada principal del programa.
# Este es el archivo principal que ejecuta el chatbot. Aquí se importan los agentes y se maneja la lógica de interacción con el usuario.

# Importamos tus agentes ya probados
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from funciones_agentes.obtener_clima import obtener_clima

def main():
    # Lista de acciones conocidas para ayudar al clasificador
    acciones_conocidas = ["apple", "tesla", "microsoft", "google", "meta", "nvidia", "netflix", "tsla", "aapl"]

    print("===========================================")
    print("🤖 BIENVENIDO A TU ASISTENTE DE IA 1.0")
    print("Puedo decirte el clima o precios de bolsa.")
    print("Escribe 'salir' para terminar.")
    print("===========================================")

    while True:
        user_input = input("\nPregunta algo > ").lower().strip()
        
        if user_input == "salir": 
            print("Chatbot: ¡Hasta luego, futuro ingeniero!")
            break

        # CLASIFICADOR MEJORADO (Basado en Reglas)
        if any(p in user_input for p in ["clima", "tiempo", "temperatura"]):
            print("Chatbot: Consultando el clima...")
            respuesta = obtener_clima(user_input)
        
        elif any(p in user_input for p in ["precio", "accion", "valor"]) or \
             any(empresa in user_input for empresa in acciones_conocidas):
            print("Chatbot: Consultando datos financieros...")
            respuesta = obtener_precio_accion(user_input)
        
        else:
            respuesta = "No entiendo esa petición. Prueba con 'Precio de Tesla' o 'Clima en Monterrey'."

        print(f"Chatbot: {respuesta}")

# --- IMPORTANTE: Sin esto, el programa no arranca ---
if __name__ == "__main__":
    main()