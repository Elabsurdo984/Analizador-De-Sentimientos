# Analisis de Sentimientos con Python
Este proyecto permite realizar un análisis de sentimientos en texto utilizando la librería VADER (Valence Aware Dictionary and sEntiment Reasoner). 
El análisis puede detectar si el texto tiene un tono positivo, negativo o neutral, y asigna una puntuación compuesta general del sentimiento.

## Descripcion:
El programa permite al usuario ingresar un texto, el cual será analizado utilizando el modelo de VADER para obtener el análisis de sentimientos. El modelo genera cuatro puntuaciones:

* **Negativo**: Muestra la intensidad del sentimiento negativo (rango de 0 a 1).
* **Neutral**: Muestra la intensidad del sentimiento neutral (rango de 0 a 1).
* **Positivo**: Muestra la intensidad del sentimiento positivo (rango de 0 a 1).
* **Puntuación Compuesta**: Muestra la puntuación global del sentimiento, que es una combinación de las tres puntuaciones anteriores, con un rango entre -1 (muy negativo) y 1 (muy positivo).
