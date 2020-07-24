from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    
    PRESENTATIONS = (('Caja','Caja'),('Bolsa','Bolsa'),('Frasco','Frasco'))
    name = models.CharField(max_length= 200, null= True)
    price_in  = models.FloatField(null= True)
    price_out = models.FloatField(null= True)
    cant = models.IntegerField(null= True)
    presentation = models.CharField(max_length= 200, null= True, choices= PRESENTATIONS)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    #category = models.CharField(max_length= 100, null= True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)

class Operation(models.Model):
    OPERATION = (('Entrada', 'Entrada'),('Salida','Salida'))
    product_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    cant = models.IntegerField(null= True)
    operation_type = models.CharField(max_length= 100, null= True, choices= OPERATION)
    #sell_id =  
    created_at = models.DateTimeField(auto_now_add=True, null= True)

class Sell(models.Model):

    user_name =  models.ForeignKey(User,on_delete= models.CASCADE) 
    operation_type = models.ForeignKey(Operation, on_delete= models.CASCADE) 
    cant =  models.IntegerField(null= True)
    cash = models.FloatField(null= True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
