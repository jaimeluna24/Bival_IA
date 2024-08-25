# Sistema de Registro de Características de Bivalvos

Este proyecto es un sistema para el registro y gestión de las características de bivalvos. Utiliza Django como framework web y MySQL como base de datos.

## Requisitos

- Python 3.8 o superior
- Django 4.x
- MySQL 5.7 o superior

## Instalación
Crear un entorno virtual y activarlo
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
## Instalar las dependencias de r
pip install -r requirements.txt
Configurar la base de datos

## Crea una base de datos MySQL con el nombre bival_ia. Asegúrate de usar las siguientes credenciales en el archivo settings.py:

python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bival_ia',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
## Configurar las claves secretas

Añade la clave secreta en el archivo settings.py:

python
Copiar código
SECRET_KEY = 'django-insecure-6@(&jjdr*+dl9&dbiiqmv6qr0traifi=jz*%-0)wri+w(e+jd8'
Configura el modo de depuración (Debug):

python
Copiar código
DEBUG = True

## Iniciar el servidor de desarrollo

python manage.py runserver