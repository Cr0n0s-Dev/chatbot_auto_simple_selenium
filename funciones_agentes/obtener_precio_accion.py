import yfinance as yf # Librería para conectar con la API de Yahoo Finance
from Utils.sanitizar import sanitizar # Importamos tu lógica de limpieza

# Diccionario mapeando nombres comunes a Tickers oficiales de bolsa
acciones = {
    "apple": "AAPL",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "facebook": "META",
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "netflix": "NFLX",
}

def obtener_precio_accion(user_input):
    # 1. Limpiamos el input (ej: de "precio de Tesla" pasa a "tesla")
    company_name = sanitizar(user_input).lower().strip()

    # 2. Buscamos en el diccionario usando el nombre limpio
    ticker = acciones.get(company_name)

    # 3. Si no está en el mapa, asumimos que el usuario escribió directamente el ticker (ej: "TSLA")
    if not ticker:
        ticker = company_name.upper()

    try:
        stock = yf.Ticker(ticker) # Creamos el objeto de la acción con Yahoo Finance
        data = stock.history(period="1d") # Pedimos el historial del último día

        if not data.empty: 
            price = data["Close"].iloc[-1] # Obtenemos el último precio de cierre disponible
            return f"El precio de {ticker} es {price:.2f} USD."
        else:
            return f"No encontré datos de bolsa para '{ticker}'."
            
    except Exception as e:
        return f"Error de conexión con Yahoo Finance: {str(e)}"