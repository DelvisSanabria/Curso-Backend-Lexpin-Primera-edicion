import sys
from fastmcp import FastMCP
import json
import requests
from typing import Any, Dict

#Creamos la instancia de nuestro servidor MCP
mcp = FastMCP("mcp-server-demo", "1.0.0")

#Creamos el formateador de respuestas
def format_response(data: Any) -> Dict[str, Any]:
    if isinstance(data, str):
        payload = data
    else:
        payload = json.dumps(data, indent=4, ensure_ascii=False)
    
    return {"content": [{
        "type": "text",
        "text": payload
    }]} # type: ignore
        
#creamos la herramienta para obtener el clima

@mcp.tool(name="fetch_weather", description="Get the current weather for a given city.")
def fetch_weather_for_city(city: str) -> Dict[str, Any]:
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    request = requests.get(geocode_url, params=params)
    requests.raise_for_status() # type: ignore
    data = request.json()
    
    #Comprobamos si la ciudad existe
    if not data or "results" not in data or len(data["results"]) == 0:
        return format_response(f"No se encontraron datos de geocodificación para la ciudad: {city}")
    
    #Si existe, obtenemos latitud y longitud
    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]
    
    #creamos la url para obtener el clima
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m",
        "forecast_days": 1,
    }
    
    wr = requests.get(weather_url, params=weather_params)
    wr.raise_for_status()  # type: ignore
    weather_data = wr.json()
    
    return format_response(weather_data)

def main() -> None:
    print("iniciando el mcp server demo", flush=True)
    
    try:
        if hasattr(mcp, "run_server_async"):
            import asyncio
            asyncio.run(mcp.run_stdio_async())
        else:
            mcp.run()
    except Exception as e:
        import traceback
        print ("Error al iniciar el servidor MCP:", file=sys.stderr)
        traceback.print_exc()


if __name__ == "__main__":
    main()
