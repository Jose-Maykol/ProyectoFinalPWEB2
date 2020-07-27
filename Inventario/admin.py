from django.contrib import admin
from .models import Productos, Proveedores, Categorias, Metodos_envio, Inventarios

# Register your models here.

admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(Categorias)
admin.site.register(Metodos_envio)
admin.site.register(Inventarios)
