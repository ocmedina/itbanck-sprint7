from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioTarjeta
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
from .models import Tarjeta

@login_required
def crear_tarjeta(request):
    if request.method == 'POST':
        form = FormularioTarjeta(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.get(usuario=request.user)
            tarjeta = form.save(commit=False)
            tarjeta.cliente = cliente
            tarjeta.save()
            messages.success(request, '¡La tarjeta se ha creado correctamente!')
            return redirect('home')
    else:
        form = FormularioTarjeta()
    return render(request, 'crear_tarjeta.html', {'form': form})

@login_required
def tarjetas_cliente(request):
    cliente = Cliente.objects.get(usuario=request.user)
    tarjetas = Tarjeta.objects.filter(cliente=cliente)
    return render(request, 'mis_tarjetas.html', {'tarjetas': tarjetas})
