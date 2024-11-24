# tarjetas/urls.py
from django.urls import path
from .views import listar_tarjetas

urlpatterns = [
    path('listar/', listar_tarjetas, name='listar_tarjetas'),
]
