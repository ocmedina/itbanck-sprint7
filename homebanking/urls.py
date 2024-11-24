# homebanking/urls.py
from django.urls import path, include

urlpatterns = [
    path('clientes/', include('clientes.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('tarjetas/', include('tarjetas.urls')),
]
