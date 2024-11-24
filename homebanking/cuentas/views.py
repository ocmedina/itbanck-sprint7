# cuentas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CrearCuentaForm

@login_required
def crear_cuenta(request):
    if request.method == 'POST':
        form = CrearCuentaForm(request.POST)
        if form.is_valid():
            cuenta = form.save(commit=False)
            cuenta.cliente = request.user  # Asocia al cliente autenticado
            cuenta.save()
            return redirect('listar_cuentas')  # Redirigir a la vista de listar cuentas
    else:
        form = CrearCuentaForm()
    return render(request, 'cuentas/crear_cuenta.html', {'form': form})
