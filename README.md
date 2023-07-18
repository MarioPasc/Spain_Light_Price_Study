# Proyecto: Análisis del precio de la luz con la API de esios

## Descripción

Este proyecto tiene como objetivo realizar un análisis del precio de la luz en España utilizando la API de esios. La API proporciona datos en tiempo real sobre el precio de la electricidad para diferentes horas del día.

El flujo del proyecto consiste en realizar una llamada a la API de esios para obtener los datos del precio de la luz, guardarlos en un archivo JSON en el directorio local, y luego procesar esos datos en otro archivo .py para crear un dataframe y visualizar una gráfica que muestre el precio de la luz y su precio medio a lo largo del tiempo.

## Instalación

1. Asegúrate de tener Python 3 instalado en tu sistema.

2. Instala las dependencias necesarias utilizando el siguiente comando:

```
pip install pandas numpy requests matplotlib
```

3. Clona este repositorio en tu directorio local utilizando el siguiente comando:

```
git clone https://github.com/tu-usuario/tu-repositorio.git
```

## Uso

1. Ejecuta el archivo `api_esios.py` para realizar la llamada a la API de esios y obtener los datos del precio de la luz. Los datos se guardarán en un archivo JSON en el directorio local.

2. Ejecuta el archivo `procesar_datos.py` para procesar los datos del archivo JSON y crear un dataframe. A continuación, se generará una gráfica que muestra el precio de la luz a lo largo del tiempo, así como el precio medio.

## Conclusiones

Para el día 18/07/2023, que es el día en el que se realizó este estudio, el precio de la luz mostró sus mínimos en las primeras horas de la mañana y en las primeras horas de la tarde con un precio medio de 161.33 por Wh (0.1613 por kWh).

## Gráfica del precio de la luz

A continuación se muestra la gráfica del precio de la luz para el día 18/07/2023:

![Gráfica del precio de la luz]([D:\OneDrive\Documentos\imagenespython\precioluz\precioluz.png](https://github.com/Mawio02/Spain_Light_Price_Study/blob/main/precioluz.png))

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.

2. Crea una rama con tu nueva funcionalidad: `git checkout -b nueva-funcionalidad`.

3. Realiza tus cambios y realiza un commit: `git commit -m "Agregada nueva funcionalidad"`.

4. Sube tus cambios a tu fork: `git push origin nueva-funcionalidad`.

5. Abre un Pull Request en este repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## English

# Project: Analysis of electricity price using esios API

## Description

This project aims to perform an analysis of electricity price in Spain using the esios API. The API provides real-time data on electricity price for different hours of the day.

The project flow consists of making a call to the esios API to fetch the electricity price data, saving it in a JSON file in the local directory, and then processing that data in another .py file to create a dataframe and visualize a graph showing the electricity price and its average price over time.

## Installation

1. Make sure you have Python 3 installed on your system.

2. Install the necessary dependencies using the following command:

```
pip install pandas numpy requests matplotlib
```

3. Clone this repository to your local directory using the following command:

```
git clone https://github.com/your-username/your-repository.git
```

## Usage

1. Run the `api_esios.py` file to make the call to the esios API and fetch the electricity price data. The data will be saved in a JSON file in the local directory.

2. Run the `procesar_datos.py` file to process the data from the JSON file and create a dataframe. A graph will be generated showing the electricity price over time, as well as the average price.

## Conclusions

For the day 18/07/2023, which is the day when this study was conducted, the electricity price showed its minimums in the early morning and early afternoon with an average price of 161.33 per Wh (0.1613 per kWh).

## Electricity Price Graph

Below is the graph of the electricity price for the day 18/07/2023:

![Electricity Price Graph]([D:\OneDrive\Documentos\imagenespython\precioluz\precioluz.png](https://github.com/Mawio02/Spain_Light_Price_Study/blob/main/precioluz.png))

## Contribution

If you wish to contribute to this project, follow these steps:

1. Fork the repository.

2. Create a branch with your new feature: `git checkout -b new-feature`.

3. Make your changes and commit: `git commit -m "Added new feature"`.

4. Push your changes to your fork: `git push origin new
