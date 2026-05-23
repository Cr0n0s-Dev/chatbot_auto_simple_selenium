import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# CORRECCIÓN: Se importa correctamente desde webdriver_manager, no desde selenium
from webdriver_manager.chrome import ChromeDriverManager 

# Descarga e instala automáticamente la versión correcta de ChromeDriver que coincida con tu navegador Chrome
driver_path = ChromeDriverManager().install()

# Tu lógica para asegurar que apunte directamente al ejecutable 'chromedriver'
if os.path.basename(driver_path) != "chromedriver":
    dir_path = os.path.dirname(driver_path)
    binary_path = os.path.join(dir_path, "chromedriver")
    if os.path.exists(binary_path):
        driver_path = binary_path

# Asegurar permisos de ejecución en sistemas basados en Unix/Linux/Mac (en Windows no afecta)
os.chmod(driver_path, 0o755)  

# Inicializamos el navegador Chrome usando el servicio del driver instalado
driver = webdriver.Chrome(service=Service(driver_path))

# --- FLUJO DE AUTOMATIZACIÓN ---

# 1. Navegar a Google
driver.get("https://www.google.com")
sleep(2) # Pausa de 2 segundos para dar tiempo a que cargue la interfaz

# 2. Navegar a la página de tu universidad (Hybridge)
driver.get("https://www.hybridge.education")
sleep(3) # Pausa de 3 segundos

# 3. Navegar a YouTube
driver.get("https://www.youtube.com")
sleep(5) # Pausa de 5 segundos para observar la carga

# BUENA PRÁCTICA: Cerramos el navegador al terminar para no dejar procesos basura en la RAM
driver.quit()