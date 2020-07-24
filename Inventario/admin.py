from django.contrib import admin
from .models import Sell, Product , Operation

# Register your models here.

admin.site.register(Sell)
admin.site.register(Product)
admin.site.register(Operation)