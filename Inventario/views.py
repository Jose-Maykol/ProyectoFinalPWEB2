from django.shortcuts import render, redirect
from .forms import ProviderForm, ProductForm, EntryForm, SaleForm, InventoryForm, ClientForm, StoreForm, LineForm
from .models import Provider, Product, Entry, Sale, Inventory, Client, Store, Line
from django.contrib.auth.models import User
from accounts.views import login
from django.views import View
from django.utils import timezone
from .render import Render
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        context = {
                'numProvi' : Provider.objects.count(),
                'numProdu' : Product.objects.count(),
                'numAdmin' : User.objects.count(),
                'numClient' : Client.objects.count(),
                'numEntry' : Entry.objects.count(),
                'numSale' : Sale.objects.count(),
                'numStore' : Store.objects.count(),
                'numLineas' : Line.objects.count(),
            }
        return render(request,'home.html', context)
    return redirect("index")

def addStore(request):
    form = StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "addStore.html", {'form' : form})

def editStore(request, store_id):
    instancia = Store.objects.get(id = store_id)
    form = StoreForm(instance=instancia)
    if request.method == "POST":
        form = StoreForm(request.POST, instance = instancia)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
        return redirect("listStore")
    return render(request, "editStore.html", {'form' : form})

def deleteStore(request, store_id):
    instancia = Store.objects.get(id = store_id)
    instancia.delete()
    return redirect('home')

def listStore(request):
    context = {
        'almacenes' : Store.objects.all(),
        }
    return render(request, "listStore.html", context)

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
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            message= "Image upload succesfully"
            return redirect('home')
    return render(request, "addProduct.html", {'form' : form})

def editProduct(request, product_id):
    instancia = Product.objects.get(id = product_id)
    form = ProductForm(instance = instancia)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance = instancia)
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

def deleteClient(request, cliente_id):
    instancia = Client.objects.get(id = cliente_id)
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

def listEntry(request):
    context = {
        'entradas' : Entry.objects.all(),
        }
    return render(request, "listEntry.html", context)

def editEntry(request, entry_id):
    instancia = Entry.objects.get(id = entry_id)
    form = EntryForm(instance = instancia)
    if request.method == "POST":
        form = EntryForm(request.POST, instance = instancia)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
        return redirect("listLine")
    return render(request, "editEntry.html", {'form' : form})

def deleteEntry(request, entry_id):
    instancia = Entry.objects.get(id = entry_id)
    instancia.delete()
    return redirect('home')

def listSale(request):
    context = {
        'salidas' : Sale.objects.all(),
        }
    return render(request, "listSale.html", context)

def editSale(request, sale_id):
    instancia = Sale.objects.get(id = sale_id)
    form = SaleForm(instance = instancia)
    if request.method == "POST":
        form = EntryForm(request.POST, instance = instancia)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
        return redirect("listLine")
    return render(request, "editSale.html", {'form' : form})

def deleteSale(request, entry_id):
    instancia = Sale.objects.get(id = entry_id)
    instancia.delete()
    return redirect('home')

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

def addLine(request):
    form = LineForm()
    if request.method == 'POST':
        form = LineForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "addLine.html", {'form' : form})

def listLine(request):
    context = {
        'lineas' : Line.objects.all(),
        }
    return render(request, "listLine.html", context)

def editLine(request, line_id):
    instancia = Line.objects.get(id = line_id)
    form = LineForm(instance = instancia)
    if request.method == "POST":
        form = LineForm(request.POST, instance = instancia)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
        return redirect("listLine")
    return render(request, "editLine.html", {'form' : form})

def deleteLine(request, line_id):
    instancia = Line.objects.get(id = line_id)
    instancia.delete()
    return redirect('home')



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
    sales = Sale.objects.all()
    return render(request,'sales.html',{'sales':sales})

def inventory(request):
    inventory = Inventory.objects.all()
    return render(request,'inventory.html',{'inventory':inventory})

class Pdf_inventory(View):

    def get(self, request):
        inventory = Inventory.objects.all()
        today = timezone.now()
        params = {
                'today': today,
                'inventory': inventory,
                'request': request
            }
        return Render.render('pdf_inventory.html',params)