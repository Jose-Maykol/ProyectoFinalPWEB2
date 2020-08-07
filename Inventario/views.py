from django.shortcuts import render, redirect
from .forms import ProviderForm
from .models import Provider, Product, Entry

# Create your views here.
def home(request):
    context = {
        'numProvi' : Provider.objects.count(),
        'numProdu' : Product.objects.count(),
        }
    return render(request,'home.html', context)

def addProvider(request):
    form = ProviderForm()
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
            return redirect('home')
    return render(request, "", {'form' : form})

def editProvider(request, provider_id):
    instancia = Provider.objects.get(id = provider_id)
    form = ProviderForm(instance=instancia)
    if request.method == "POST":
        form = ProviderForm(request.POST, instance = instancia)
        if form.is_valid():
            instancia = form.save(commit = False)
            instancia.save()
    return render(request, "", {'form' : form})

def deleteProvider(request, provider_id):
    instancia = Provider.objects.get(id = provider_id)
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
    return render(request,'admin.html')

def client(request):
    return render(request,'client.html')

def products(request):
    return render(request,'products.html')

def sales(request):
    return render(request,'sales.html')

def inventory(request):
    return render(request,'inventory.html')
