import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# CORRECCIÓN: Importación correcta desde su librería real
from webdriver_manager.chrome import ChromeDriverManager 

# Importación de tus agentes locales (todo en minúsculas)
from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from Utils.sanitizar import sanitizar

# --- CONFIGURACIÓN DE ARGUMENTOS DE SELENIUM (Navegador Invisible) ---
options = Options()
options.add_argument("--headless")  # Ejecuta Chrome de fondo sin abrir la ventana visual
options.add_argument("--disable-gpu")  # Deshabilita gráficos pesados (ahorra procesador)
options.add_argument("--no-sandbox")  # Evita problemas de permisos en servidores/contenedores
options.add_argument("--disable-dev-shm-usage")  # Evita que se sature la memoria compartida temporal

# Configuración para simular ser un humano real y evadir bloqueos antibots
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")  # Oculta el rastro de Selenium

# --- INSTALACIÓN Y CONFIGURACIÓN DEL DRIVER ---
driver_path = ChromeDriverManager().install()

if os.path.basename(driver_path) != "chromedriver":
    dir_path = os.path.dirname(driver_path)
    binary_path = os.path.join(dir_path, "chromedriver")
    if os.path.exists(binary_path):
        driver_path = binary_path

os.chmod(driver_path, 0o755)  # Permisos de ejecución del binario

# Encendemos el navegador invisible global que usará todo el script
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# --- CLASIFICADOR DE INTENCIONES (NLU Simple) ---
def procesar_input(user_input):
    acciones_conocidas = ["apple", "tesla", "microsoft", "google", "meta", "nvidia", "netflix", "tsla", "aapl"]
    
    # Pasamos a minúsculas para evaluar las reglas de la IA de forma segura
    input_eval = user_input.lower().strip()
    
    # Intención 1: Clima
    if any(p in input_eval for p in ["clima", "temperatura", "tiempo"]):
        return obtener_clima(user_input)
        
    # Intención 2: Acciones (Palabras clave o si menciona una empresa directo)
    elif any(p in input_eval for p in ["precio", "accion", "acción", "valor"]) or \
         any(empresa in input_eval for empresa in acciones_conocidas):
        return obtener_precio_accion(user_input)
    
    return None  # Si no se detecta ninguna intención, regresamos None para manejarlo en el flujo principal

# --- BUCLE PRINCIPAL DE INTERACCIÓN ---
print('Hola, soy un agente de Selenium invisible. Puedo ayudarte a obtener información del clima o el precio de una acción. ¿En qué puedo ayudarte?')

while True:
    try:
        user_input = input("\nUsuario: ").strip()
        if not user_input:
            print("Por favor, ingresa una consulta válida.")
            continue

        # CORRECCIÓN: Evaluación individual para que cualquiera de estas palabras cierre el programa
        if user_input.lower() in ["salir", "adiós", "adios", "chau"]:
            print("Agente de Selenium: ¡Hasta luego!")
            break

        # Enviamos la entrada al procesador/clasificador
        respuesta = procesar_input(user_input)
        
        if respuesta is None:
            print("Agente de Selenium: Lo siento, no puedo procesar esa consulta. Por favor, intenta preguntando por el clima o una acción.")
        else: 
            # Imprimimos directamente el texto que nos regresó el agente
            print(f"Agente de Selenium: {respuesta}")

    except KeyboardInterrupt:  # CORRECCIÓN: 'KeyboardInterrupt' lleva la K mayúscula en Python
        print("\nAgente de Selenium: ¡Hasta luego!")
        break
    except Exception as e:
        print(f"Agente de Selenium: Ocurrió un error inesperado: {e}")

# CIERRE REQUERIDO: Mata el proceso oculto de Chrome en la RAM al terminar
driver.quit()