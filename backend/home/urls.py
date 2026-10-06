# Importaciones:
from django.urls import path
from home.views import home_inicio

urlpatterns = [
    # Enrutando las clases que se encuentran en views.py
    path('', home_inicio) 
]
