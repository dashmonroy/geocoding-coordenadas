# Python Geocoding Project

Este proyecto permite obtener direcciones a partir de coordenadas geográficas utilizando la API de OpenStreetMap (Nominatim). La lógica principal se encuentra en el archivo `src/app.py`, que carga un archivo de Excel con coordenadas, renombra una columna si es necesario, obtiene las direcciones y guarda el resultado en un nuevo archivo de Excel.

## Estructura del Proyecto

```
python-geocoding-project
├── src
│   └── app.py
├── requirements.txt
└── README.md
```

## Requisitos

Para ejecutar este proyecto, necesitarás tener instaladas las siguientes dependencias:

- pandas
- requests

Puedes instalar las dependencias utilizando el siguiente comando:

```
pip install -r requirements.txt
```

## Uso

1. Asegúrate de tener un archivo de Excel llamado `Coordenadas.xlsx` en el mismo directorio donde se ejecuta el script.
2. Ejecuta el script `app.py`:

```
python src/app.py
```

3. El resultado se guardará en un nuevo archivo llamado `Coordenadas_con_direccion.xlsx`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, siéntete libre de hacer un fork y enviar un pull request.