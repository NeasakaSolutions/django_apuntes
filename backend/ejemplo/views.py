# Importaciones:
from rest_framework.views import APIView
from http import HTTPStatus
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import (
        HttpResponse,
        JsonResponse,
)

# Create your views here.
class Class_Ejemplo(APIView):

    def get(self, request):
        return JsonResponse({
                "estado": "ok",
                "mensaje": "Metodo GET"
        }, status = HTTPStatus.OK)

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
    
    def put(self, request):
                return HttpResponse("Metodo PUT")

    def delete(self, request):
                return HttpResponse("Metodo DELETE")

# Clase con parametros
class Class_Ejemplo_Parametros(APIView):

    def get(self, request, id): # Se agregan los nuevos parametros que en este caso es el id
        return HttpResponse(f"Metodo GET con el parametro de id: {id}")
    
    def put(self, request, id):
                return HttpResponse(f"Metodo PUT con el parametro de id: {id}")

    def delete(self, request, id):
                return HttpResponse(f"Metodo DELETE con el parametro de id: {id}")
