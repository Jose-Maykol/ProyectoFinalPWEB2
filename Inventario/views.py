from django.shortcuts import render, redirect

# Create your views here.


#prueba para cargar la pagina
def home(request):
    return render(request,'home.html')

def company(request):
    return render(request,'company.html')

def providers(request):
    return render(request,'providers.html')

def payments(request):
    return render(request,'payments.html')

def categories(request):
    return render(request,'categories.html')

def admin(request):
    return render(request,'admin.html')

def client(request):
    return render(request,'client.html')

def products(request):
    return render(request,'products.html')

def sales(request):
    return render(request,'sales.html')

def inventory(request):
    return render(request,'inventory.html')
