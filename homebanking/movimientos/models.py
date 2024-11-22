from django.db import models
from cuentas.models import Cuenta

class Movimiento(models.Model):
    id = models.AutoField(primary_key=True) 
    cuenta_numero = models.ForeignKey(Cuenta, on_delete=models.CASCADE, db_column='cuenta_numero')
    monto = models.IntegerField() 
    tipo_operacion = models.CharField(max_length=50)
    hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movimiento {self.id} - {self.tipo_operacion} - Cuenta {self.cuenta_numero_id}"
