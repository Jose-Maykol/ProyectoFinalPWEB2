from django.shortcuts import render, redirect
from .forms import ProviderForm, ProductForm, EntryForm, SaleForm, InventoryForm, ClientForm
from .models import Provider, Product, Entry, Sale, Inventory, Client
from django.contrib.auth.models import User
from accounts.views import login

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        context = {
                'numProvi' : Provider.objects.count(),
                'numProdu' : Product.objects.count(),
                'numAdmin' : User.objects.count(),
                'numClient' : Client.objects.count(),
            }
        return render(request,'home.html', context)
    return redirect("index")

def addProvider(request):
    form = ProviderForm()
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "addProvider.html", {'form' : form})

def editProvider(request, provider_id):
    instancia = Provider.objects.get(id = provider_id)
    form = ProviderForm(instance=instancia)
    if request.method == "POST":
        form = ProviderForm(request.POST, instance = instancia)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
        return redirect("listProvider")
    return render(request, "editProvider.html", {'form' : form})

def deleteProvider(request, provider_id):
    instancia = Provider.objects.get(id = provider_id)
    instancia.delete()
    return redirect('home')

def listProvider(request):
    context = {
        'proveedores' : Provider.objects.all(),
        }
    return render(request, "listProvider.html", context)

def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "addProduct.html", {'form' : form})

def editProduct(request, product_id):
    instancia = Product.objects.get(id = product_id)
    form = ProductForm(instance = instancia)
    if request.method == "POST":
        form = ProductForm(request.POST, instance = instancia)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
        return redirect("listProduct")
    return render(request, "editProduct.html", {'form' : form})

def deleteProduct(request, product_id):
    instancia = Product.objects.get(id = product_id)
    instancia.delete()
    return redirect('home')

def listProduct(request):
    context = {
        'productos' : Product.objects.all(),
        }
    return render(request, "listProduct.html", context)

def addClient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "addClient.html", {'form' : form})

def editClient(request, client_id):
    instancia = Client.objects.get(id = client_id)
    form = ClientForm(instance = instancia)
    if request.method == "POST":
        form = ClientForm(request.POST, instance = instancia)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
        return redirect("listClient")
    return render(request, "editClient.html", {'form' : form})

def deleteClient(request, product_id):
    instancia = Client.objects.get(id = product_id)
    instancia.delete()
    return redirect('home')

def listClient(request):
    context = {
        'clientes' : Client.objects.all(),
        }
    return render(request, "listClient.html", context)

def addEntry(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "addEntry.html", {'form' : form})

def addSale(request):
    form = SaleForm()
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "addSale.html", {'form' : form})

def addInventory(request):
    form = InventoryForm()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "", {'form' : form})

def company(request):
    return render(request,'company.html')

def providers(request):
    return render(request,'providers.html')

def payments(request):
    return render(request,'payments.html')

def categories(request):
    return render(request,'categories.html')

def admin(request):
    return render(request,'administrator.html')

def client(request):
    return render(request,'client.html')

def products(request):
    return render(request,'products.html')

def sales(request):
    return render(request,'sales.html')

def inventory(request):
    return render(request,'inventory.html')
