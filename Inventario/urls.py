from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('home', views.home, name = 'home'),

    path('listStore', views.listStore, name ='listStore'),
    path('addStore', views.addStore, name = 'addStore'),
    path('editStore/<int:store_id>', views.editStore, name = 'editStore'),
    path('deleteStore/<int:store_id>', views.deleteStore, name ='deleteStore'),

    path('listClient', views.listClient, name ='listClient'),
    path('addClient', views.addClient, name = 'addClient'),
    path('editClient/<int:client_id>', views.editClient, name = 'editClient'),
    path('deleteClient/<int:client_id>', views.deleteClient, name ='deleteClient'),
    
    path('listProvider', views.listProvider, name ='listProvider'),
    path('addProvider', views.addProvider, name = 'addProvider'),
    path('editProvider/<int:provider_id>', views.editProvider, name = 'editProvider'),
    path('deleteProvider/<int:provider_id>', views.deleteProvider, name ='deleteProvider'),

    path('listProduct', views.listProduct, name ='listProduct'),
    path('addProduct', views.addProduct, name = 'addProduct'),
    path('editProduct/<int:product_id>', views.editProduct, name = 'editProduct'),
    path('deleteProduct/<int:product_id>', views.deleteProduct, name ='deleteProduct'),

    path('addEntry', views.addEntry, name = 'addEntry'),
    path('addSale', views.addSale, name = 'addSale'),
    path('addInventory', views.addInventory, name = 'addInventory'),

    path('listLine', views.listLine, name ='listLine'),
    path('addLine', views.addLine, name = 'addLine'),
    path('editLine/<int:Line_id>', views.editLine, name = 'editLine'),
    path('deleteLine/<int:Line_id>', views.deleteLine, name ='deleteLine'),

    path('categories', views.categories, name = 'categories'),
    path('products', views.products, name = 'products'),
    path('company', views.company, name = 'company'),
    path('providers', views.providers, name ='providers'),
    path('payments', views.payments, name ='payments'),
    path('client', views.client, name = 'client'),
    path('administrator', views.admin, name = 'administrator'),
    path('sales', views.sales, name = 'sales'),
    path('inventory', views.inventory, name = 'inventory'),

    path('render/pdf/' , views.Pdf_inventory.as_view(), name= 'render/pdf/'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
