# clientes/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ver_datos_cliente(request):
    cliente = request.user  # Información del cliente autenticado
    return render(request, 'clientes/ver_datos.html', {'cliente': cliente})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def listar_cliente(request):
    cliente = request.user  # Obtiene el usuario autenticado
    return render(request, 'clientes/listar_cliente.html', {'cliente': cliente})
