import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar el lexicón de VADER si no lo tienes
nltk.download('vader_lexicon')

# Inicializar el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Escribe un texto para analizar el sentimiento: ")

# Analizar el sentimiento del texto ingresado
sentimiento = sia.polarity_scores(texto_usuario)

# Mostrar el análisis
print("\nAnálisis de Sentimiento del texto:")
print(f"Negativo: {sentimiento['neg']}")
print(f"Neutral: {sentimiento['neu']}")
print(f"Positivo: {sentimiento['pos']}")
print(f"Puntuación compuesta: {sentimiento['compound']}")
