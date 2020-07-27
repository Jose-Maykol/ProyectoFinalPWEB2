from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Productos(models.Model):

    id_producto = models.AutoField(primary_key = True)
    nombre_producto = models.CharField(max_length = 50, null = True, verbose_name = "Nombre del producto")
    descripcion_producto = models.TextField(null = True, verbose_name = "Descripcion del producto")
    #categoria_id
    precio_unitario = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True, verbose_name = "Precio unitario")
    nivel_nuevaorden = models.IntegerField(blank = True, verbose_name = "Nivel para generar nueva orden")
    prod_descontinuado = models.BooleanField(verbose_name = "Producto descontinuado")
    dias_espera = models.IntegerField(blank = True, verbose_name = "Dias para re-abastecer")

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre_producto']

    def __str__(self):
        return self.nombre_producto


        
class Categorias(models.Model):

    categoria_id = models.AutoField(primary_key = True)
    categoria = models.CharField(max_length = 255, null = True, verbose_name = "Nombre de la categoria")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['categoria_id']

    def __str__(self):
        return self.categoria_id



class Proveedores(models.Model):
    
    id_proveedor = models.AutoField(primary_key = True)
    nombre_proveedor = models.CharField(max_length = 50, null = True, verbose_name = "Nombre del proveedor")
    nombre_contacto = models.CharField(max_length = 50, null = True, verbose_name = "Nombre de contacto representante")
    cargo_contacto = models.CharField(max_length = 50, null = True, verbose_name = "Cargo del contacto")
    direccion = models.CharField(max_length = 255, null = True, verbose_name = "Direccion del proveedor")
    codigo_postal = models.CharField(max_length = 10, null = True, verbose_name = "Cosigo postal")
    ciudad = models.CharField(max_length = 50, null = True, verbose_name = "Ciudad del proveedor")
    pais = models.CharField(max_length = 50, null = True, verbose_name = "Pais")
    telefono = models.CharField(max_length = 12, null = True, verbose_name = "Telefono")
    fax = models.CharField(max_length = 12, null = True, verbose_name = "Fax del proveedor")
    terminos_pago = models.CharField(max_length = 255, null = True, verbose_name = "Terminos de pago")
    email = models.EmailField(max_length = 254, null = True, verbose_name = "Correo electronico") 
    notas = models.CharField(max_length = 255, blank = True, verbose_name = "Notas")

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre_proveedor']

    def __str__(self):
        return self.nombre_proveedor



class Metodos_envio(models.Model):

    id_metodo = models.AutoField(primary_key = True)
    metodo_envio = models.CharField(max_length = 255, null = True, verbose_name = "Metodo del envio")

    class Meta:
        verbose_name = 'Metodo_envio'
        verbose_name_plural = 'Metodos_envios'
        ordering = ['metodo_envio']

    def __str__(self):
        return self.metodo_envio



class Inventarios(models.Model):

    id_inv = models.AutoField(primary_key = True)
    #id_producto =
    cant_disp = models.IntegerField(verbose_name = "Cantidada disponible")
    cant_min = models.IntegerField(verbose_name = "Cantidad mínima")
    cant_max = models.IntegerField(verbose_name = "Cantidad Máxima")

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        ordering = ['id_inv']

    def __str__(self):
        return self.id_inv





