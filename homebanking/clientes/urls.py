from django.urls import path
from . import views

urlpatterns = [
    path('detalle/', views.detalle_cliente, name='detalle'),
]
