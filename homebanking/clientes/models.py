from django.db import models
from tipo_cliente.models import TipoCliente

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_surname = models.CharField(max_length=100)
    customer_DNI = models.CharField(max_length=10, unique=True)
    branch_id = models.IntegerField()
    dob = models.DateField()
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE, db_column='tipo_cliente_id') 

    def __str__(self):
        return f"{self.customer_name} {self.customer_surname}"
