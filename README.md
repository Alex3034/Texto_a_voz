# Texto a Voz 🔊

Texto a Voz es un script en Python que convierte artículos web en archivos de audio en formato MP3. Utiliza bibliotecas como `newspaper3k` para extraer el texto de una URL y `gTTS` (Google Text-to-Speech) para generar el archivo de audio.

## Tecnologías utilizadas

[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![newspaper3k](https://img.shields.io/badge/newspaper3k-Extractor-ff6600?style=for-the-badge)](https://newspaper.readthedocs.io/en/latest/)
[![gTTS](https://img.shields.io/badge/gTTS-Google_TTS-34a853?style=for-the-badge)](https://pypi.org/project/gTTS/)
[![argparse](https://img.shields.io/badge/argparse-CLI%20Parser-005f87?style=for-the-badge)](https://docs.python.org/3/library/argparse.html)
- **Python**: Lenguaje de programación principal.
- **newspaper3k**: Biblioteca para extraer y analizar artículos web.
- **gTTS**: Biblioteca para convertir texto a voz usando la API de Google Text-to-Speech.
- **argparse**: Biblioteca para gestionar argumentos en la línea de comandos.

## Características 📊
- **Extracción de texto**: Obtiene el contenido de un artículo web a partir de su URL.
- **Conversión a audio**: Transforma el texto extraído en un archivo de audio MP3.
- **Interfaz de línea de comandos (CLI)**: Permite al usuario proporcionar la URL, personalizar el nombre del archivo de salida y elegir el idioma.
- **Manejo de errores**: Incluye validación de URL y gestión de excepciones para un funcionamiento robusto.
- **División de texto**: Divide el texto en fragmentos más pequeños si supera el límite de caracteres de `gTTS`.

## Instalación 🛠️
Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local.

### Requisitos previos
- Python 3.6 o superior.
- `pip` (gestor de paquetes de Python).

### Pasos
Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/texto-a-voz.git
cd texto-a-voz
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta el script:

```bash
python texto_a_voz.py <URL> --output <nombre_archivo> --lang <código_idioma>
```

### Ejemplo de uso

```bash
python texto_a_voz.py https://ejemplo.com/articulo --output mi_audio.mp3 --lang es
```

## Uso

### Proporcionar la URL como argumento
Puedes ejecutar el script proporcionando directamente la URL del artículo:

```bash
python texto_a_voz.py https://ejemplo.com/articulo --output mi_audio.mp3 --lang es
```

### Modo interactivo
Si no proporcionas una URL, el script te pedirá que la introduzcas manualmente:

```bash
python texto_a_voz.py --output mi_audio.mp3 --lang es
```

Salida esperada:

```
Introduce la URL del artículo (o 'salir' para terminar): https://ejemplo.com/articulo
Título: Ejemplo de artículo
Guardando el artículo como audio...
Parte 1 guardada como mi_audio_parte_1.mp3
Proceso completado.
```

El archivo de audio se guardará en el mismo directorio donde se ejecutó el script.

## Estructura del proyecto 📁

```
texto-a-voz/
├── texto_a_voz.py       # Script principal
├── README.md            # Documentación del proyecto
├── requirements.txt     # Dependencias del proyecto
└── .gitignore           # Archivos y carpetas ignorados por Git
```

## Mejoras futuras 💡
- Agregar una interfaz gráfica con `Tkinter` o `PyQt`.
- Integrar soporte para más idiomas y voces.
- Desplegar el proyecto como aplicación web con `Flask` o `Django`.
- Añadir tests automatizados con `unittest` o `pytest`.

## Licencia 📝
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto 🤝
Si tienes alguna pregunta o sugerencia, puedes contactarme:

- **Nombre**: Alejandro  
- **Email:** alejandrohm98a@gmail.com
- **GitHub:** [@Alex3034](https://github.com/Alex3034)  

¡Gracias por visitar este repositorio! Espero que este proyecto te sea útil. 😊

