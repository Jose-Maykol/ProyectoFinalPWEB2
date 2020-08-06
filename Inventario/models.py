from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Provider(models.Model):

    name = models.CharField(max_length= 100, null= True, verbose_name= "Nombre del proveedor")
    adrress = models.CharField(max_length= 100, null= True, verbose_name= "Direccion")
    phone = models.CharField(max_length= 20, null= True, verbose_name= "Numero de telefono")
    email =  models.EmailField(null= True, verbose_name= "E-mail")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural =  "Proveedores"

class Product(models.Model):
    
    PRESENTATIONS = (('Caja','Caja'),('Bolsa','Bolsa'),('Frasco','Frasco'))
    name = models.CharField(max_length= 200, null= True, verbose_name= "Nombre del producto")
    price  = models.FloatField(null= True, verbose_name= "Precio")
    presentation = models.CharField(max_length= 200, null= True, choices= PRESENTATIONS, verbose_name= "Presentación")
    user = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name= "Usuario")
    providers = models.ManyToManyField(Provider, verbose_name = "Proveedores", default= None)
    #Linea = models.ForeignKey(Linea,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural =  "Productos"

class Entry(models.Model):

    product = models.ForeignKey(Product, on_delete= models.CASCADE, verbose_name= "Producto", default= None)
    cant = models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    created_at = models.DateTimeField(auto_now_add=True, null= True, verbose_name= "Fecha de movimiento")
    
    def __str__(self):
        date = str(self.created_at)
        return date
    
    def save(self):
        if self.id:
            old = Entry.objects.get(pk = self.id)
            print(self.cant)
            print(old.cant)
            self.cant = self.cant - old.cant
            print(self.cant)
        super(Entry, self).save()
        #Entry.objects.all().delete()
        create_inventory = False
        for i in Inventory.objects.all():
            if str(self.product.name) == str(i.name_product): 
                create_inventory = False
                I = Inventory.objects.get(id = i.id)
                I.cant = I.cant + self.cant
                I.save()
                break
            if str(self.product.name) != str(i.name_product) and i.id: 
                create_inventory = True
        if create_inventory == True: 
            I = Inventory(product= self, price_product = self.product.price, cant = self.cant, name_product = str(self.product.name),entry_date = self.created_at)
            I.save()
        I = Inventory.objects.all()
        if not I.exists():
            I = Inventory(product = self, price_product = self.product.price, cant = self.cant, name_product = str(self.product.name),entry_date = self.created_at)
            I.save()
        #Inventory.objects.all().delete()
    def delete(self): 
        for i in Inventory.objects.all():
            if str(self.product.name) == str(i.name_product): 
                create_inventory = False
                I = Inventory.objects.get(id = i.id)
                I.cant = I.cant - self.cant
                I.save()
                break
        super(Entry, self).delete()
        

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural =  "Entradas"

class Inventory(models.Model):

    product = models.ForeignKey(Entry, on_delete= models.CASCADE, default= None)
    cant = models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    name_product =  models.CharField(max_length= 100, null= True, verbose_name= "Producto")
    price_product = models.PositiveIntegerField(null= True, verbose_name = "Precio del producto")
    entry_date = models.DateTimeField(auto_now_add=True, null= True,verbose_name= "Fecha de entrada")
    
    def __str__(self):
        return self.name_product

class Sale(models.Model):

    user_name =  models.ForeignKey(User,on_delete= models.CASCADE, verbose_name= "Nombre del cliente", default= None) 
    product = models.ForeignKey(Inventory, on_delete= models.CASCADE, verbose_name= "Producto", default= None)
    cant =  models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    created_at = models.DateTimeField(auto_now_add=True, null= True,verbose_name= "Fecha de venta")

    def __str__(self):
        date = str(self.created_at)
        return date
    
    def save(self):
        if self.id:
            old = Sale.objects.get(pk = self.id)
            print(self.cant)
            print(old.cant)
            self.cant = self.cant - old.cant
            print(self.cant)        
        super(Sale, self).save()
        #Inventory.objects.all().delete()   
        for i in Inventory.objects.all():
            if str(self.product) == str(i):
                I = Inventory.objects.get(id = i.id)
                I.cant = I.cant - self.cant
                I.save()
    @property            
    def total_price(self):
        total_price = 0
        for i in Inventory.objects.all():
            if str(self.product) == str(i):
                I = Inventory.objects.get(id = i.id)
                total_price = I.price_product* self.cant
        return total_price


    class Meta:
        verbose_name = "Salida"
        verbose_name_plural =  "Salidas"
    

