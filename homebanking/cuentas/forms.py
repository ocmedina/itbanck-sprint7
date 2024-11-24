# cuentas/forms.py
from django import forms
from .models import Cuenta

class CrearCuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['tipo_cuenta', 'saldo_inicial']  # Ajusta según tu modelo
