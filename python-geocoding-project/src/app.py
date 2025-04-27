import pandas as pd
import requests
from time import sleep

def get_address(lat, lon):
    """Obtiene la dirección usando la API de OpenStreetMap (Nominatim)."""
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
    headers = {"User-Agent": "GeocodingScript/1.0"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("display_name", "Dirección no encontrada")
        else:
            return "Error en la consulta"
    except Exception as e:
        return f"Error: {e}"

# Cargar el archivo con coordenadas
file_path = "Coordenadas.xlsx"
df = pd.read_excel(file_path)

# Renombrar columna si es necesario
df.rename(columns={"LGN": "LON"}, inplace=True)

# Obtener direcciones
df["Direccion"] = df.apply(lambda row: get_address(row["LAT"], row["LON"]), axis=1)
    
# Guardar el resultado en un nuevo archivo
df.to_excel("Coordenadas_con_direccion.xlsx", index=False)
print("Proceso completado. Archivo guardado como 'Coordenadas_con_direccion.xlsx'")