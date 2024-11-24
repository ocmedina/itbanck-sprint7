from django.db import models
from clientes.models import Cliente
from empleado.models import Empleado
from sucursal.models import Sucursal

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=200) 
    numero = models.CharField(max_length=10) 
    ciudad = models.CharField(max_length=100)  
    provincia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)  
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True, db_column='cliente_id')  
    empleado_id = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True, db_column='empleado_id') 
    sucursal_id = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True, db_column='sucursal_id')  

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.ciudad}, {self.provincia}"
