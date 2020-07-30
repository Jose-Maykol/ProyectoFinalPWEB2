from django.contrib import admin
from .models import Inventarios, Productos, Categorias, Ordenes_compra, Locaciones, Metodos_envio, Historia_mov, Proveedores, Detalle_compras

# Create your models here.

admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(Categorias)
admin.site.register(Metodos_envio)
admin.site.register(Inventarios)
admin.site.register(Locaciones)
admin.site.register(Historia_mov)
admin.site.register(Detalle_compras)
admin.site.register(Ordenes_compra)
