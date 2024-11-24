from django.db import models
from clientes.models import Cliente
from tipo_cuenta.models import TipoCuenta

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True) 
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.CharField(max_length=34, unique=True)
    tipo_id = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, db_column='tipo_id')

    def __str__(self):
        return f"Cuenta {self.account_id} - Cliente ID: {self.customer_id.id}"
