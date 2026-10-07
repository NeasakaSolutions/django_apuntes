# Importaciones:
from django.urls import path
from ejemplo.views import Class_Ejemplo

urlpatterns = [
    # Enrutando las clases que se encuentran en views.py
    path('ejemplo', Class_Ejemplo.as_view()) 
]