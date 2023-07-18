import json
import numpy as np
from datetime import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import os

#region Datos
archivo_json = f'datos{date.today().strftime("%d%m%Y")}.json'
directorio = 'D:\OneDrive\Documentos\datasets\precioluz_json'
migeoid = 8741
#endregion

#region Abrir archivo json
ruta_completa = os.path.join(directorio, archivo_json)
if os.path.exists(ruta_completa):
    with open(ruta_completa, "r") as archivo:
        data = json.load(archivo)
else:
    print(f'La ruta {ruta_completa} no existe')
#endregion


#region Manipulación de la información
# Filtramos los datos para solo quedarnos con indicator y values
data = data['indicator']['values']
# Filtramos los datos por localización
filtered_data = [x for x in data if x['geo_id'] == migeoid]
# Encabezados interesantes
columns = ['value', 'datetime']
# Extracción de información
final_data = []
for x in filtered_data:
    final_data.append([x[col] for col in columns])
valores, fechas = zip(*final_data)
fechas = list(map(lambda x: datetime.fromisoformat(x), fechas))
data_transformed = np.stack((np.array(valores), np.array(fechas)), axis=1)
#Creacion del dataframe
valdates_df = pd.DataFrame(data=data_transformed, columns=columns)
#endregion

#region Extracción de datos

avg_price = np.average(valdates_df.value)
max_price = np.max(valdates_df.value)
min_price = np.min(valdates_df.value)

print(f'Fecha: {valdates_df.datetime[0].day}/{valdates_df.datetime[0].month}/{valdates_df.datetime[0].year}\n'
      f'Precio medio de la luz: ')
#endregion

#region Visualización del cambio
x = list(map(lambda x: x.hour, valdates_df.datetime))
y = list(valdates_df.value)
plt.scatter(x=x, y=y, color='red')
plt.plot(x, y, color='blue')
avg = list(map(lambda x: avg_price, valdates_df.datetime.copy()))
plt.plot(x, avg, color='green')
plt.xlabel(f'Hora del día {valdates_df.datetime[0].day}/'
           f'{valdates_df.datetime[0].month}/{valdates_df.datetime[0].year}')
plt.ylabel('Valor del precio de la luz')
plt.legend(labels=['Precio de la luz para esa hora', 'Variacion precio de la luz', 'Precio medio'])
plt.show()
#endregion


