# 📍 Geocoding de Coordenadas con OpenStreetMap (Nominatim)

Este proyecto es un script en Python que toma un archivo de Excel con coordenadas geográficas (`LAT`, `LON`), utiliza la API de OpenStreetMap (Nominatim) para obtener la dirección correspondiente, y guarda el resultado en un nuevo archivo Excel.

---

## 📚 Descripción

- **Entrada:**  
  Un archivo llamado `Coordenadas.xlsx` con columnas de latitud (`LAT`) y longitud (`LON` o `LGN`).

- **Proceso:**  
  - Lee el archivo Excel.
  - Renombra la columna `LGN` a `LON` si es necesario.
  - Usa la API de OpenStreetMap para hacer _reverse geocoding_ de cada coordenada.
  - Agrega una nueva columna `Direccion` con el resultado de la consulta.

- **Salida:**  
  Un archivo llamado `Coordenadas_con_direccion.xlsx` con las direcciones obtenidas.

---

## ⚙️ Requisitos

Antes de ejecutar el script, asegúrate de tener instalado:

- Python 3.7 o superior
- Las siguientes librerías de Python:
  ```bash
  pip install pandas requests openpyxl
🚀 Cómo usar el script
Coloca tu archivo Coordenadas.xlsx en la misma carpeta que el script.

Ejecuta el script en terminal o CMD:

bash
Copiar
Editar
python geocoding.py
El resultado se guardará como Coordenadas_con_direccion.xlsx en la misma carpeta.

🖥️ Código fuente (geocoding.py)
python
Copiar
Editar
import pandas as pd
import requests

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

# Cargar el archivo de coordenadas
file_path = "Coordenadas.xlsx"
df = pd.read_excel(file_path)

# Renombrar columna si es necesario
df.rename(columns={"LGN": "LON"}, inplace=True)

# Obtener direcciones para cada fila
df["Direccion"] = df.apply(lambda row: get_address(row["LAT"], row["LON"]), axis=1)

# Guardar el archivo actualizado
df.to_excel("Coordenadas_con_direccion.xlsx", index=False)
print("✔ Proceso completado. Archivo guardado como 'Coordenadas_con_direccion.xlsx'")
🛠️ Estructura del proyecto
bash
Copiar
Editar
/geocoding-project
│
├── Coordenadas.xlsx        # Archivo original con LAT y LON
├── Coordenadas_con_direccion.xlsx   # Archivo generado
└── geocoding.py            # Script principal
🌎 Consideraciones
Este script utiliza la API pública de OpenStreetMap (Nominatim), que tiene límites de uso. Para cargas muy grandes se recomienda implementar tiempos de espera o utilizar tu propio servidor Nominatim.

Respeta las políticas de uso de la API agregando siempre un User-Agent personalizado en las solicitudes HTTP (ya incluido en el script).

📄 Licencia
Este proyecto se publica bajo la Licencia MIT © 2025.
Uso libre con atribución adecuada.