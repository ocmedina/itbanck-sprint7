from django.db import models
from clientes.models import Cliente
from marca_tarjeta.models import MarcaTarjeta 

class Tarjeta(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20, unique=True)
    cvv = models.IntegerField()
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo = models.CharField(max_length=20)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cliente_id')
    marca_id = models.ForeignKey(MarcaTarjeta, on_delete=models.CASCADE, db_column='marca_id')

    def __str__(self):
        return f"Tarjeta {self.numero} - {self.tipo} - Marca: {self.marca_id.nombre}"
