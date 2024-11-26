from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_cuenta_cliente, name='crear_cuenta'),
    path('listar/', views.listar_cuentas_cliente, name='listar_cuentas'),
]