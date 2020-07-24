from django.contrib import admin
from .models import Entry, Product , Sale, Provider

# Register your models here.

admin.site.register(Entry)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Provider)