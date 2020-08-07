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

]
