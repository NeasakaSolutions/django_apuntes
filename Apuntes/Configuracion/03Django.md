## Descargar django:

- Ejecutar en terminal (RECUERDA TENER EL ENTORNO VIRTAUL ACTIVO):
```bash
pip install Django
```

## Crear proyecto en django:

- Crear proyecto:
```bash
django-admin startproject backend
```

- Crear aplicacion:
```bash
django-admin startapp home
```

## Descargar Django Restframework:

- Ejecutar en terminal con el entorno encendido:
```bash
pip install djangorestframework
```

- Ir a settings.py y en INSTALLED_APPS agregar rest_framework:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]
```
