from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioRegistro, FormularioAutenticacionPersonalizado
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'login/home.html', {'user': request.user})

def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = FormularioRegistro()
    return render(request, 'login/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = FormularioAutenticacionPersonalizado(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '¡Bienvenido de nuevo!')
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = FormularioAutenticacionPersonalizado()
    return render(request, 'login/login.html', {'form': form})
