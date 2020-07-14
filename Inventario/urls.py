
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login',views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    #prueba para ir implementado la pagina
    path('home', views.home, name = 'home'),
    path('company', views.company, name='company'),
    path('providers', views.providers, name='providers'),
    path('payments', views.payments, name='payments'),
    path('categories', views.categories, name='categories'),
    #path('admins', views.admin, name='admin'),
    path('client', views.client, name='client'),
    path('products', views.products , name='products'),
    path('sales', views.sales , name='sales'),
    path('inventory', views.inventory , name='inventory'),
]
