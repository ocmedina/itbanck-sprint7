from django.db import models

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)  
    branch_number = models.BinaryField() 
    branch_name = models.CharField(max_length=100) 
    branch_address_id = models.IntegerField()

    def __str__(self):
        return f"{self.branch_name} (ID: {self.branch_id})"
