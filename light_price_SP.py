import json
import requests
from datetime import date
import os

#region Datos propios de la solicitud
TOKEN = YOUR_TOKEN
url = 'https://api.esios.ree.es/indicators/1001'
headers = {'Accept': 'application/json; application/vnd.esios-api-v2+json',
           'Content-Type': 'application/json',
           'Host': 'api.esios.ree.es',
           'Authorization': 'Token token=\"TOKEN\"'}
#endregion


def http_req(url_web, headers_pet):
    return requests.get(url, headers=headers)


#region ---Main---
# Llamada
response = http_req(url, headers)
# Comprobar el código de estado de la respuesta
if response.status_code == 200:
    try:
        # Cargamos los datos en formato json
        data = response.json()
        # Guardamos el archivo json
        archivo = f'datos{date.today().strftime("%d%m%Y")}.json'
        directorio = 'D:\OneDrive\Documentos\datasets\precioluz_json'
        ruta_completa = os.path.join(directorio, archivo)
        if not os.path.exists(ruta_completa):
            os.makedirs(directorio)
        with open(ruta_completa, "w") as archivo_json:
            json.dump(data, archivo_json)



    except json.JSONDecodeError:
        print("Archivo JSON de la petición dañado")
        breakpoint()
else:
    print(f"Error en la solicitud: {response.status_code}, {response.reason}")
#endregion
