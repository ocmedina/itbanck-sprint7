# cuentas/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cuenta

@login_required
def listar_cuentas(request):
    cuentas = Cuenta.objects.filter(cliente=request.user)  # Cuentas del cliente autenticado
    return render(request, 'cuentas/listar_cuentas.html', {'cuentas': cuentas})
