from django.contrib import admin
from .models import Entry, Product , Sale, Provider, Line, Sub_line, Client

# Register your models here.

admin.site.register(Entry)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Provider)
admin.site.register(Line)
admin.site.register(Sub_line)
admin.site.register(Client)