from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from cuentas.models import CuentaCliente 

@login_required
def detalle_cliente(request):
    cliente = Cliente.objects.get(usuario=request.user)
    cuenta = CuentaCliente.objects.get(cliente=cliente)
    return render(request, 'detalle.html', {'cliente': cliente, 'cuenta': cuenta})
