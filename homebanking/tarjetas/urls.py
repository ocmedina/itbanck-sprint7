from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_tarjeta, name='crear_tarjeta'),
    path('mis_tarjetas/', views.tarjetas_cliente, name='tarjetas_cliente'),
]
