from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioCuentaCliente
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
from .models import CuentaCliente

@login_required
def crear_cuenta_cliente(request):
    if request.method == 'POST':
        formulario = FormularioCuentaCliente(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Cuenta creada exitosamente!")
            return redirect('crear_cuenta')  
        else:
            messages.error(request, "Hubo un error al crear la cuenta.")
    else:
        formulario = FormularioCuentaCliente()
    
    return render(request, 'crear_cuenta.html', {'formulario': formulario})


@login_required
def listar_cuentas_cliente(request):
    cliente = Cliente.objects.get(usuario=request.user)

    cuentas = CuentaCliente.objects.filter(cliente=cliente)

    return render(request, 'mis_cuentas.html', {'cuentas': cuentas})
