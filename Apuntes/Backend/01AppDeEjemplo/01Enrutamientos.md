## Api de ejemplo:

- Ir a urls.py de backend y configurar la nueva app, en este caso home:
```python
# Importaciones:
from django.urls import include

urlpatterns = [
    path('', include('home.urls')) # Ruta inicial
]
```

- En la app de home, crear el archivo urls.py y escribir:
```python
# Importaciones:
from django.urls import path
from home.views import home_inicio

urlpatterns = [
    # Enrutando las clases que se encuentran en views.py
    path('', home_inicio) 
]
```

- En la app home ir al archivo views.py y agregar:
```python
```

