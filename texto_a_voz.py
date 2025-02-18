from newspaper import Article
from gtts import gTTS
import re
import argparse

"""
Script para convertir un artículo web en un archivo de audio.

Uso:

python texto_a_voz.py <URL> [--output <nombre_archivo>] [--lang <código_idioma>]

Ejemplo:

python texto_a_voz.py https://ejemplo.com/articulo --output mi_audio --lang es
"""

# Validar URL
def validar_url(url):
    regex = r'^https?://(?:www\.)?\S+\.\S+$'
    return re.match(regex, url) is not None

# Configurar CLI
parser = argparse.ArgumentParser(description="Convertir un artículo web a audio.")
parser.add_argument("url", nargs="?", help="URL del artículo")
parser.add_argument("--output", "-o", default="articulo.mp3", help="Nombre del archivo de audio")
parser.add_argument("--lang", "-l", default="es", help="Código del idioma (por ejemplo, 'es' para español)")
args = parser.parse_args()

# Si no se proporcionó una URL como argumento
if not args.url:
    while True:
        
        # Pedir al usuario que introduzca la URL del artículo
        url = input("Introduce la URL del artículo (o 'salir' para terminar): ")

        # Permitir al usuario salir del programa
        if url.lower() == "salir":
            print("Saliendo del programa...")
            exit()

        # Validar la URL
        if not validar_url(url):
            print("La URL introducida no es válida. Inténtalo de nuevo.")
            continue  # Volver a pedir la URL

        # Si la URL es válida, salir del bucle
        args.url = url
        break
else:
    # Validar la URL proporcionada como argumento
    if not validar_url(args.url):
        print("La URL proporcionada no es válida.")
        exit(1)

# Intentar descargar y analizar el artículo
try:
    article = Article(args.url)
    article.download()
    article.parse()
except Exception as e:
    print(f"Error al procesar la URL: {e}")
    exit(1)

# Mostrar el título del artículo
print(f"Título: {article.title}")

# Crear un archivo de audio a partir del texto extraído
print("Guardando el artículo como audio...")
max_caracteres = 4000
texto = article.text
partes = [texto[i:i + max_caracteres] for i in range(0, len(texto), max_caracteres)]

for i, parte in enumerate(partes):
    tts = gTTS(parte, lang=args.lang)
    nombre_archivo = f"{args.output}_parte_{i + 1}.mp3"
    tts.save(nombre_archivo)
    print(f"Parte {i + 1} guardada como {nombre_archivo}")

print("Proceso completado.")