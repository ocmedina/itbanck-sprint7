# cuentas/urls.py
from django.urls import path
from .views import crear_cuenta, listar_cuentas

urlpatterns = [
    path('crear/', crear_cuenta, name='crear_cuenta'),
    path('listar/', listar_cuentas, name='listar_cuentas'),
]
