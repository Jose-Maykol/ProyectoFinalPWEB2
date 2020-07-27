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



class Locaciones(models.Model):

    id_loc = models.AutoField(primary_key = True)
    cod_loc = models.CharField(max_length = 15, verbose_name = "Codigo de la localizacion")
    desc_loc = models.CharField(max_length = 150, null = True, verbose_name = "Descripción de la localizacion")
    isla = models.CharField(max_length = 15, null = True, verbose_name = "Codigo de isla de almacen")
    seccion = models.CharField(max_length = 15, null = True, verbose_name = "Codigo de sección")
    nivel = models.CharField(max_length = 15, null = True, verbose_name = "Codigo de nivel")
    contenedor = models.CharField(max_length = 15, null = True, verbose_name = "Codigo de contenedor")
    capacidad = models.IntegerField( null = True, verbose_name = "Capacidad del contenedor")

    class Meta:
        verbose_name = 'Locacion'
        verbose_name_plural = 'Locaciones'
        ordering = ['cod_loc']

    def __str__(self):
        return self.cod_loc



class Historia_mov(models.Model):

    #day  = timezone.now()
    #hour = timezone.now()
    TIPO = (('ENTRADA','ENTRADA'),('SALIDA','SALIDA'))

    id_inv_hist = models.AutoField(primary_key = True)
    tipo_mov = models.CharField(max_length = 25, blank = False, choices = TIPO, verbose_name = "Tipo de movimiento")
    cant_mov = models.IntegerField(blank = False, verbose_name = "Cantidad de movimiento")
    fecha_mov = models.DateField(auto_now = True, verbose_name = "Fecha de movimiento")
    hora_mov = models.DateTimeField(auto_now = True, verbose_name = "Hora de movimiento")
    #id_producto = model|
    #id_empleado =
    lote = models.CharField(max_length = 255, null = True, verbose_name = "Código del lote del producto")
    caducidad = models.DateField(auto_now = False, verbose_name = "Fecha de caducidad")
    #id_loc = 

    class Meta:
        verbose_name = 'Historia_mov'
        verbose_name_plural = 'Historias_mov'
        ordering = ['fecha_mov']

    def __str__(self):
        return self.fecha_mov



class Ordenes_compra(models.Model):

    id_orden_compra = models.AutoField(primary_key = True)
    numero_compra = models.CharField(max_length = 255, null = True, verbose_name = "Numero de la compra")
    #proveedor_id
    #empleado_id
    descripción_compra = models.CharField(max_length = 255, blank = True, null = True, verbose_name = "Descripcion de la compra")
    fecha_orden = models.DateField(auto_now = False, verbose_name = "Fecha de orden")
    #metodoenvio_id
    fecha_embarque = models.DateField(auto_now = False, verbose_name = "Fecha de embarque")
    fecha_requerida = models.DateField(auto_now = False, verbose_name = "Fecha requerida")
    fecha_promesa = models.DateField(auto_now = False, verbose_name = "Fecha promesa")

    class Meta:
        verbose_name = 'Orden_compra'
        verbose_name_plural = 'Ordenes_compra'
        ordering = ['id_orden_compra']

    def __str__(self):
        return self.id_orden_compra



class Detalle_compras(models.Model):
    
    id_detalle_compra = models.AutoField(primary_key = True)
    #producto_id
    #ordencompra_id
    cantidad_orden = models.IntegerField(verbose_name = "Cantidad de orden")
    cantidad_recibida = models.IntegerField(verbose_name = "Cantidad recibida")

    class Meta:
        verbose_name = 'Detalle_compra'
        verbose_name_plural = 'Detalle_compras'
        ordering = ['id_detalle_compra']

    def __str__(self):
        return self.id_detalle_compra




