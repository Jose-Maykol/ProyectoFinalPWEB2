from django.contrib import admin
from .models import Productos, Proveedores, Categorias, Metodos_envio, Inventarios, Locaciones, Historia_mov, Detalle_compras, Ordenes_compra

# Register your models here.

admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(Categorias)
admin.site.register(Metodos_envio)
admin.site.register(Inventarios)
admin.site.register(Locaciones)
admin.site.register(Historia_mov)
admin.site.register(Detalle_compras)
admin.site.register(Ordenes_compra)
