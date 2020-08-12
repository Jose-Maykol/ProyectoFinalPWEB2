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

    def save(self):
        if self.id:
            old = Line.objects.get(pk = self.id)
            sale = Sale.objects.filter(client = self)
            for s in sale:
                s.client = self
                s.save()
        super(Client, self).save()

    def __str__(self):
        return self.customer_name
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Line(models.Model):

    line_name = models.CharField(max_length= 30, null= True, verbose_name= "Nombre de la linea")

    def __str__(self):
        return self.line_name
    
    class Meta:
        verbose_name = "Linea"
        verbose_name_plural = "Lineas"

    def save(self):
        if self.id:
            old = Line.objects.get(pk = self.id)
            product = Product.objects.filter(line = old)
            for p in product:
                p.line = self
                p.save()
        super(Line, self).save()

class Provider(models.Model):

    name = models.CharField(max_length= 100, null= True, verbose_name= "Nombre del proveedor")
    adrress = models.CharField(max_length= 100, null= True, verbose_name= "Direccion")
    phone = models.CharField(max_length= 20, null= True, verbose_name= "Numero de telefono")
    email =  models.EmailField(null= True, verbose_name= "E-mail")
    RUC =models.CharField(null=True, max_length=11,verbose_name="RUC")
    razon_social = models.CharField(max_length=20, null=True, verbose_name="Razon social")

    def save(self):
        if self.id:
            old = Provider.objects.get(pk = self.id)
            product = Product.objects.filter(line = old)
            for p in product:
                p.providers = self
                p.save()
        super(Provider, self).save()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural =  "Proveedores"

class Product(models.Model):
    
    PRESENTATIONS = (('Unidad','Unidad'),
                        ('Lata','Lata'),
                        ('Paquete','Paquete'),
                        ('KIT','KIT'),
                        ('Caja','Caja'),
                        ('Bolsa','Bolsa'),
                        ('Frasco','Frasco'))
    name = models.CharField(max_length= 200, null= True, verbose_name= "Nombre del producto")
    price  = models.FloatField(null= True, verbose_name= "Precio")
    presentation = models.CharField(max_length= 200, null= True, choices= PRESENTATIONS, verbose_name= "Presentación")
    user = models.ForeignKey(User, on_delete= models.SET_DEFAULT, verbose_name= "Usuario", default= None)
    providers = models.ForeignKey(Provider, on_delete= models.SET_DEFAULT, verbose_name = "Proveedor", default= None)
    line = models.ForeignKey(Line,on_delete = models.SET_DEFAULT, default= None,null= True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return self.name

    def save(self):
        if self.id:
            old = Product.objects.get(pk = self.id)
            inventory = Inventory.objects.filter(name_product = old.name)
            for i in inventory:
                i.name_product = self.name
                i.price_product = self.price
                i.providers = str(self.providers)
                i.line = str(self.line)
                i.presentation = self.presentation
                i.save()
        super(Product, self).save()

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural =  "Productos"

class Store(models.Model):

    store_name = models.CharField(null= True, max_length= 50, verbose_name= "Nombre de almacen")
    location = models.CharField(null= True, max_length= 100, verbose_name= "Ubicacion")

    def __str__(self):
        return self.store_name

    def save(self):
        if self.id:
            old = Store.objects.get(pk = self.id)
            inventory = Inventory.objects.get(store = old.store_name)
            for i in inventory:
                i.store = self.store_name
                i.save()
        super(Store, self).save()
    class Meta:
        
        verbose_name = "Almacen"
        verbose_name_plural = "Almacenes"

class Entry(models.Model):

    store = models.ForeignKey(Store, on_delete = models.SET_DEFAULT, verbose_name= "Almacen", default= None, null= True)
    product = models.ForeignKey(Product, on_delete = models.SET_DEFAULT, verbose_name= "Producto", default= None, null= True)
    cant = models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    created_at = models.DateTimeField(auto_now_add=True, null= True, verbose_name= "Fecha de movimiento")
    
    def __str__(self):
        date = str(self.created_at)
        return date
    
    def save(self):
        if self.id:
            old = Entry.objects.get(pk = self.id)
            i = Inventory.objects.get(name_product = old.product.name, store= str(old.store))
            i.cant = i.cant - old.cant
            i.save()
        super(Entry, self).save()
        
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural =  "Entradas"

class Inventory(models.Model):

    store = models.CharField(max_length = 50, null= True, verbose_name= "Almacen")
    product = models.ForeignKey(Entry, on_delete= models.SET_DEFAULT, default= None, null= True)
    cant = models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    name_product =  models.CharField(max_length= 100, null= True, verbose_name= "Producto")
    presentation = models.CharField(max_length= 110, null = True, verbose_name= "Presentación")
    price_product = models.PositiveIntegerField(null= True, verbose_name = "Precio del producto")
    providers = models.CharField(null = True, verbose_name= "Proveedor", max_length= 100)
    line = models.CharField(max_length= 100,null = True, verbose_name= "Linea del producto")
    entry_date = models.DateTimeField(auto_now_add=True, null= True,verbose_name= "Fecha de entrada")
    
    def __str__(self):
        return f'{self.store}, {self.name_product}'

class Sale(models.Model):

    user_name =  models.ForeignKey(User,on_delete= models.SET_DEFAULT, verbose_name= "Usuario", default= None) 
    client = models.ForeignKey(Client, on_delete = models.SET_DEFAULT, default= None, verbose_name= "Cliente", null= True)
    product = models.ForeignKey(Inventory, on_delete= models.SET_DEFAULT, verbose_name= "Producto", default= None)
    store = models.ForeignKey(Store, on_delete = models.SET_DEFAULT, verbose_name= "Almacen", default= None)
    cant =  models.PositiveIntegerField(null= True, verbose_name= "Cantidad")
    created_at = models.DateTimeField(auto_now_add=True, null= True,verbose_name= "Fecha de venta")
    total_price = models.PositiveIntegerField(null = True, verbose_name= "Precio total", blank = True)

    def __str__(self):
        date = str(self.created_at)
        return date
    
    def save(self):
        if self.id:
            old = Sale.objects.get(pk = self.id)
            i = Inventory.objects.get(name_product = old.product.name_product, store= str(old.store))
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
    removed = Inventory.objects.get(name_product = str(instance.product.name), store= str(instance.store))
    removed.cant = removed.cant - instance.cant
    removed.save()

@receiver(post_delete, sender = Sale)
def delete_sale(sender, instance, **kwargs):
    removed = Inventory.objects.get(name_product = instance.product.name_product, store= str(instance.store))
    removed.cant = removed.cant + instance.cant
    removed.save()

@receiver(post_save, sender = Entry)
def post_save_entry(sender, instance, **kwargs):
    create_inventory = False
    inventory = Inventory.objects.all()
    for i in inventory:
        if str(instance.product.name) == str(i.name_product) and str(instance.store) == str(i.store): 
            create_inventory = False
            I = Inventory.objects.get(id = i.id)
            I.cant = I.cant + instance.cant
            I.save()
            break
        if ((str(instance.product.name) == str(i.name_product)) or (str(instance.product.name) != str(i.name_product))) and str(instance.store) != str(i.store) :  
            create_inventory = True
    if not inventory.exists():
        I = Inventory(store= str(instance.store), product = instance, price_product = instance.product.price, cant = instance.cant, name_product = str(instance.product.name), presentation = str(instance.product.presentation), providers= str(instance.product.providers), line= str(instance.product.line), entry_date = instance.created_at)
        I.save()
    if create_inventory == True : 
        I = Inventory(store= str(instance.store), product= instance, price_product = instance.product.price, cant = instance.cant, name_product = str(instance.product.name),  presentation = str(instance.product.presentation), providers= str(instance.product.providers), line= str(instance.product.line), entry_date = instance.created_at)
        I.save()
    #Inventory.objects.all().delete()

@receiver(post_save, sender = Sale)
def post_save_sale(sender, instance, **kwargs):
    i = Inventory.objects.get(name_product = str(instance.product), store= str(instance.store))
    i.cant = i.cant - instance.cant
    i.save()