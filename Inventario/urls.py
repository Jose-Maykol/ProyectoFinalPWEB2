from django.urls import path
from . import views

urlpatterns = [
    
    path('home', views.home, name = 'home'),
    path('addProvider', views.addProvider, name = 'addProvider'),
    path('editProvider/<int:provider_id>', views.editProvider, name = 'editProvider'),
    path('deleteProvider/<int:provider_id>', views.deleteProvider, name ='deleteProvider'),
    path('addProduct', views.addProduct, name = 'addProduct'),
    path('editProduct/<int:product_id>', views.editProduct, name = 'editProduct'),
    path('deleteProduct/<int:product_id>', views.deleteProduct, name ='deleteProduct'),
    path('addEntry', views.addEntry, name = 'addEntry'),
    path('addSale', views.addSale, name = 'addSale'),
    path('addInventory', views.addInventory, name = 'addInventory'),

    path('categoria', views.categories, name = 'categories'),
    path('productos', views.products, name = 'products'),
    path('empresa', views.company, name = 'company'),
    path('proveedores', views.providers, name ='providers'),
    path('pagos', views.payments, name ='payments'),
    path('clientes', views.client, name = 'client'),
    path('admin', views.admin, name = 'admin'),
    path('Ventas', views.sales, name = 'sales'),
    path('Inventario', views.inventory, name = 'inventory'),
]
