from django.db import models
from clientes.models import Cliente

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True) 
    loan_type = models.CharField(max_length=50)
    loan_date = models.DateField() 
    loan_total = models.IntegerField() 
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='customer_id') 

    def __str__(self):
        return f"Préstamo {self.loan_id} - Tipo: {self.loan_type} - Cliente ID: {self.customer_id_id}"
