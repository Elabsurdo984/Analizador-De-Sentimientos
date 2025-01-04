# Analisis de Sentimientos con Python
Este proyecto permite realizar un análisis de sentimientos en texto utilizando la librería VADER (Valence Aware Dictionary and sEntiment Reasoner). 
El análisis puede detectar si el texto tiene un tono positivo, negativo o neutral, y asigna una puntuación compuesta general del sentimiento.

## Descripcion:
El programa permite al usuario ingresar un texto, el cual será analizado utilizando el modelo de VADER para obtener el análisis de sentimientos. El modelo genera cuatro puntuaciones:

* **Negativo**: Muestra la intensidad del sentimiento negativo (rango de 0 a 1).
* **Neutral**: Muestra la intensidad del sentimiento neutral (rango de 0 a 1).
* **Positivo**: Muestra la intensidad del sentimiento positivo (rango de 0 a 1).
* **Puntuación Compuesta**: Muestra la puntuación global del sentimiento, que es una combinación de las tres puntuaciones anteriores, con un rango entre -1 (muy negativo) y 1 (muy positivo).

## Requisitos:
* Python 3
* Las siguientes Librerias:
    * nltk
  

Pueden instalarla asi:
`pip install nltk`


Instrucciones para usar
**Descargar el código**: Clona o descarga este repositorio en tu máquina local.

**Ejecutar el programa**:

Abre la terminal o un entorno de desarrollo como Visual Studio Code o Jupyter Notebook.
Ejecuta el script Python:

`python analisis_sentimientos.py`
**Escribir el texto**: El programa pedirá que ingreses un texto en la consola. Escribe cualquier texto que desees analizar y presiona Enter.

**Ver los resultados**: El programa te devolverá las puntuaciones de sentimiento
