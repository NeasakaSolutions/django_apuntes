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
