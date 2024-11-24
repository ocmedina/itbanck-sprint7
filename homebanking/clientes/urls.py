# clientes/urls.py
from django.urls import path
from .views import ver_datos_cliente

urlpatterns = [
    path('datos/', ver_datos_cliente, name='ver_datos_cliente'),
]
from django.urls import path
from .views import listar_cliente

urlpatterns = [
    path('listar-cliente/', listar_cliente, name='listar_cliente'),
]
