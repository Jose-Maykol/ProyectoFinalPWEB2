from django.contrib import admin
from .models import Entry, Product , Sale, Provider, Line, Store, Client, Inventory

# Register your models here.

admin.site.register(Entry)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Provider)
admin.site.register(Line)
admin.site.register(Store)
admin.site.register(Client)
admin.site.register(Inventory)