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

    path('categories', views.categories, name = 'categories'),
    path('products', views.products, name = 'products'),
    path('company', views.company, name = 'company'),
    path('providers', views.providers, name ='providers'),
    path('payments', views.payments, name ='payments'),
    path('client', views.client, name = 'client'),
    path('administrator', views.admin, name = 'administrator'),
    path('sales', views.sales, name = 'sales'),
    path('inventory', views.inventory, name = 'inventory'),
]
