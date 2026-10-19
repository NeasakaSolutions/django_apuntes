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

- Probar en insomnia con los metodos que se utilizaron en las consultas con parametros:
```bash
http://127.0.0.1:8000/api/v1/ejemplo/3
```

- En views.py agregar la siguiente importacion y modificar el metodo GET:
```python
from django.http import (
        HttpResponse,
        JsonResponse # Importacion que se agrega
)

def get(self, request):
    return JsonResponse({
            "estado": "ok",
            "mensaje": "Metodo GET"
    })
```

- En isnomnia, en el metodo post agregar un body de tipo json y agregar:
```json
{
    "correo": "correo@correo.com",
    "password": "Ijole123"
}
```

- En views.py agregar la importacion:
```python
from http import HTTPStatus
```

- Modificar el metodo post:
```python
def post(self, request):
            # Validaciones:
            if request.data.get("correo") == None or request.data.get("password") == None:

                    return JsonResponse({
                            "estado": "error",
                            "mensaje": "Campos vacios"
                    }, status = HTTPStatus.BAD_REQUEST)

            # Retorno:
            return JsonResponse({
                    "estado": "ok",
                    "mensaje": f"Metodo POST | correo = {request.data.get('correo')}"
            }, status = HTTPStatus.CREATED)
```

- En el metodo get agregar el estado:
```python
def get(self, request):
        return JsonResponse({
                "estado": "ok",
                "mensaje": "Metodo GET"
        }, status = HTTPStatus.OK)
```

- En views.py agregar la importacion:
```python
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
```

- Modificar el metodo POST:
```python
def post(self, request):
            # Parametros:
            correo = request.data.get("correo")
            password = request.data.get("password")
            
            # Validaciones:
            if not isinstance(correo, str) or not isinstance(password, str):
                return JsonResponse({
                        "estado": "error",
                        "mensaje": "Datos invalidos"
                }, status = HTTPStatus.BAD_REQUEST)

            # Eliminar espacios en blanco:
            correo = correo.strip()

            if not correo or not password:
                return JsonResponse({
                        "estado": "error",
                        "mensaje": "Faltan campos obligatorios"
                }, status = HTTPStatus.BAD_REQUEST)

            # Validar formato del correo:
            try:
                validate_email(correo)
            except ValidationError:
                return JsonResponse({
                       "estado": "error",
                       "mensaje": "Correo invalido"
                }, status = HTTPStatus.BAD_REQUEST)

            # Respuesta positiva
            return JsonResponse({
                    "estado": "ok",
                    "mensaje": f"Metodo POST | correo = {request.data.get('correo')}"
            }, status = HTTPStatus.CREATED)
```

