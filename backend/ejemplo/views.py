# Importaciones:
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.
class Class_Ejemplo(APIView):

    def get(self, request):
        return HttpResponse("Ijole desde la app de ejemplo")

    def post(self, request):
            return HttpResponse("Metodo POST")
    
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
