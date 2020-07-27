from django.db import models

# Create your models here.

class Productos(models.Model):

    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    descripcion_producto = models.TextField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_nuevaorden = models.IntegerField()
    prod_descontinuado = models.BooleanField()
    dias_espera = models.IntegerField()
        

