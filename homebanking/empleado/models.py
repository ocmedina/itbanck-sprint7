from django.db import models
from sucursal.models import Sucursal 

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True) 
    employee_name = models.CharField(max_length=100)
    employee_surname = models.CharField(max_length=100) 
    employee_hire_date = models.DateField()
    employee_DNI = models.CharField(max_length=20, unique=True) 
    branch_id = models.ForeignKey(Sucursal, on_delete=models.CASCADE, db_column='branch_id') 

    def __str__(self):
        return f"{self.employee_name} {self.employee_surname} - Sucursal: {self.branch_id.branch_name}"
