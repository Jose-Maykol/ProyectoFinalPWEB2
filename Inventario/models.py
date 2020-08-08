from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver
# Create your models here.

class Client(models.Model):

    customer_name =  models.CharField(max_length= 60, null= True, verbose_name= "Nombre del cliente")
    phone = models.CharField(max_length=20, null= True, verbose_name= "Numero de telefono")
    email = models.EmailField(null= True, verbose_name= "Correo electronico")
    razon_social = models.CharField(max_length=200,null=True, verbose_name="Razon social")
    RUC =models.CharField(null=True, max_length=11,verbose_name="RUC")

    def __str__(self):
        return self.customer_name
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Line(models.Model):

    line_name = models.CharField(max_length= 30, null= True, verbose_name= "Nombre de la linea")
    #have_sub_line = models.BooleanField(default= False, verbose_name= "Sublinea")
    #sub_line = models.ManyToManyField(Sub_line,verbose_name="Sublineas ", default= None)

    def __str__(self):
        return self.line_name
    
    class Meta:
        verbose_name = "Linea"
        verbose_name_plural = "Lineas"

class Sub_line(models.Model):
    
    #line = models.ForeignKey(Line, on_delete= models.SET_DEFAULT, default= none,blank= True)
    sub_line_name = models.CharField(max_length= 30, null= True, verbose_name= "Nombre de sublinea")

    def __str__(self):
        return self.sub_line_name

    class Meta:
        verbose_name = "Sublinea"
        verbose_name_plural = "Sublineas"
class Provider(models.Model):

    name = models.CharField(max_length= 100, null= True, verbose_name= "Nombre del proveedor")
    adrress = models.CharField(max_length= 100, null= True, verbose_name= "Direccion")
    phone = models.CharField(max_length= 20, null= True, verbose_name= "Numero de telefono")
    email =  models.EmailField(null= True, verbose_name= "E-mail")
    RUC =models.CharField(null=True, max_length=11,verbose_name="RUC")
    razon_social = models.CharField(max_length=20, null=True, verbose_name="Razon social")

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
    user = models.ForeignKey(User, on_delete= models.SET_DEFAULT, verbose_name= "Usuario", default= None)
    providers = models.ManyToManyField(Provider, verbose_name = "Proveedores", default= None)
    line = models.ForeignKey(Line,on_delete = models.SET_DEFAULT, default= None)
    sub_line = models.ForeignKey(Sub_line, on_delete = models.SET_DEFAULT, default = None)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural =  "Productos"

class Entry(models.Model):

    product = models.ForeignKey(Product, on_delete = models.SET_DEFAULT, verbose_name= "Producto", default= None)
    cant = models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    created_at = models.DateTimeField(auto_now_add=True, null= True, verbose_name= "Fecha de movimiento")
    
    def __str__(self):
        date = str(self.created_at)
        return date
    
    def save(self):
        if self.id:
            old = Entry.objects.get(pk = self.id)
            i = Inventory.objects.get(name_product = old.product.name)
            i.cant = i.cant - old.cant
            i.save()
        super(Entry, self).save()
        
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural =  "Entradas"

class Inventory(models.Model):

    product = models.ForeignKey(Entry, on_delete= models.SET_DEFAULT, default= None)
    cant = models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    name_product =  models.CharField(max_length= 100, null= True, verbose_name= "Producto")
    price_product = models.PositiveIntegerField(null= True, verbose_name = "Precio del producto")
    line = models.CharField(max_length= 100,null = True, verbose_name= "Linea del producto")
    sub_line = models.CharField(max_length= 100,null = True, verbose_name= "Sublinea del producto")
    entry_date = models.DateTimeField(auto_now_add=True, null= True,verbose_name= "Fecha de entrada")
    
    def __str__(self):
        return self.name_product

class Sale(models.Model):

    user_name =  models.ForeignKey(User,on_delete= models.SET_DEFAULT, verbose_name= "Usuario", default= None) 
    client = models.ForeignKey(Client, on_delete = models.SET_DEFAULT, default= None, verbose_name= "Cliente")
    product = models.ForeignKey(Inventory, on_delete= models.SET_DEFAULT, verbose_name= "Producto", default= None)
    cant =  models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    created_at = models.DateTimeField(auto_now_add=True, null= True,verbose_name= "Fecha de venta")
    total_price = models.PositiveIntegerField(null = True, verbose_name= "Precio total", blank = True)

    def __str__(self):
        date = str(self.created_at)
        return date
    
    def save(self):
        if self.id:
            old = Sale.objects.get(pk = self.id)
            i = Inventory.objects.get(name_product = old.product.name_product)
            i.cant = i.cant + old.cant 
            i.save() 
        super(Sale, self).save()   
          
    class Meta:
        verbose_name = "Salida"
        verbose_name_plural =  "Salidas"

@receiver(pre_save, sender = Sale)
def get_total_price(sender, instance, **kwargs):
    total_price = instance.product.price_product * instance.cant
    instance.total_price = total_price
    
@receiver(post_delete, sender = Entry)
def delete_entry(sender, instance, **kwargs): 
    removed = Inventory.objects.get(name_product = instance.product.name)
    removed.cant = removed.cant - instance.cant
    removed.save()

@receiver(post_delete, sender = Sale)
def delete_sale(sender, instance, **kwargs):
    removed = Inventory.objects.get(name_product = instance.product.name_product)
    removed.cant = removed.cant + instance.cant
    removed.save()

@receiver(post_save, sender = Entry)
def post_save_entry(sender, instance, **kwargs):
    create_inventory = False
    inventory = Inventory.objects.all()
    for i in inventory:
        if str(instance.product.name) == str(i.name_product): 
            create_inventory = False
            I = Inventory.objects.get(id = i.id)
            I.cant = I.cant + instance.cant
            I.save()
            break
        if str(instance.product.name) != str(i.name_product): 
            create_inventory = True
    if not inventory.exists():
        I = Inventory(product = instance, price_product = instance.product.price, cant = instance.cant, name_product = str(instance.product.name), line= str(instance.product.line), sub_line= str(instance.product.sub_line), entry_date = instance.created_at)
        I.save()
    if create_inventory == True : 
        I = Inventory(product= instance, price_product = instance.product.price, cant = instance.cant, name_product = str(instance.product.name), line= str(instance.product.line), sub_line= str(instance.product.sub_line), entry_date = instance.created_at)
        I.save()
    #Inventory.objects.all().delete()

@receiver(post_save, sender = Sale)
def post_save_sale(sender, instance, **kwargs):
    i = Inventory.objects.get(name_product = str(instance.product))
    i.cant = i.cant - instance.cant
    i.save() 

""" @receiver(post_save, sender = User)
def get_user(sender, instance, **kwargs):
    if kwargs.get('created'):
        user = User.objetcs.get(username = instance)
        Sale.objects.get_or_create(user_name = user) """