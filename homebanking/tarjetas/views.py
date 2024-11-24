# tarjetas/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tarjeta

@login_required
def listar_tarjetas(request):
    tarjetas = Tarjeta.objects.filter(cliente=request.user)  # Tarjetas del cliente autenticado
    return render(request, 'tarjetas/listar_tarjetas.html', {'tarjetas': tarjetas})
