import sys
import os

# Agregamos la ruta actual al sistema para que encuentre las carpetas
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("--- REVISANDO CONEXIONES ---")

try:
    # Ajustamos los nombres EXACTOS según tu imagen (minúsculas)
    from funciones_agentes.obtener_precio_accion import obtener_precio_accion
    from funciones_agentes.obtener_clima import obtener_clima
    print("✅ Conexión con agentes: OK")
except Exception as e:
    print(f"❌ Error de importación: {e}")
    print("Tip: Revisa que los nombres de archivos en la carpeta sean 'obtener_clima.py' y 'obtener_precio_accion.py'")

def ejecutar_prueba():
    print("\n--- INICIANDO PRUEBAS DE CAMPO ---")
    
    # Prueba de Acción
    print("Probando Acción (Apple)...")
    try:
        print(f"Resultado: {obtener_precio_accion('Apple')}")
    except Exception as e:
        print(f"Error en Acción: {e}")

    # Prueba de Clima
    print("\nProbando Clima (CDMX)...")
    try:
        print(f"Resultado: {obtener_clima('CDMX')}")
    except Exception as e:
        print(f"Error en Clima: {e}")

if __name__ == "__main__":
    ejecutar_prueba()