# Importaciones:
from django.urls import path
from ejemplo.views import (
    Class_Ejemplo,
    Class_Ejemplo_Parametros
)

urlpatterns = [
    # Enrutando las clases que se encuentran en views.py
    path('ejemplo', Class_Ejemplo.as_view()),
    path('ejemplo/<int:id>', Class_Ejemplo_Parametros.as_view()),
]