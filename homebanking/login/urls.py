from django.contrib.auth.views import LogoutView
from . import views
from django.urls import path

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('', views.iniciar_sesion, name='login'),
    path('home/', views.home, name='home'),
]
