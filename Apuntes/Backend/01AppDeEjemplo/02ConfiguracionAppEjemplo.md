## Aplicacion de ejemplo para conceptos basicos

- Crear la nueva app, ejecutar en terminal:
```bash
django-admin startapp ejemplo
```

- Ir al archivo principal de urls (El que se encuentra en la carpeta backend) y agregar la nueva ruta:
```python
# Importaciones:
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), 
    path('api/v1/', include('ejemplo.urls')), # Ruta que se agrega
]
```

- Ir a la app de ejemplo y crear el archivo urls.py:
```python
# Importaciones:
from django.urls import path
from ejemplo.views import Class_Ejemplo

urlpatterns = [
    # Enrutando las clases que se encuentran en views.py
    path('ejemplo', Class_Ejemplo.as_view()) 
]
```

- Ir a views.py de la app ejemplo y agregar:
```python
# Importaciones:
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.
class Class_Ejemplo(APIView):

    def get(self, request):
        return HttpResponse("Ijole desde la app de ejemplo")
```

- En insomnia generar un nuevo proyecto y agregar la ruta:
```bash
http://127.0.0.1:8000/api/v1/ejemplo
```

- Agregar los metodos faltantes y probarlos en insomnia:
```python
def post(self, request):
    return HttpResponse("Metodo POST")
    
def put(self, request):
    return HttpResponse("Metodo PUT")

def delete(self, request):
    return HttpResponse("Metodo DELETE")
```

- En urls.py de la app ejemplo, modificar las importaciones y generar la nueva ruta:
```python
from ejemplo.views import (
    Class_Ejemplo,
    Class_Ejemplo_Parametros
)

urlpatterns = [
    # Enrutando las clases que se encuentran en views.py
    path('ejemplo', Class_Ejemplo.as_view()),
    path('ejemplo/<int:id>', Class_Ejemplo_Parametros.as_view()), # Nueva ruta
]
```

- En views.py agregar los siguientes metodos con sus respectivas id:
```python
# Clase con parametros
class Class_Ejemplo_Parametros(APIView):

    def get(self, request, id): # Se agregan los nuevos parametros que en este caso es el id
        return HttpResponse(f"Metodo GET con el parametro de id: {id}")
    
    def put(self, request, id):
                return HttpResponse(f"Metodo PUT con el parametro de id: {id}")

    def delete(self, request, id):
                return HttpResponse(f"Metodo DELETE con el parametro de id: {id}")
```

