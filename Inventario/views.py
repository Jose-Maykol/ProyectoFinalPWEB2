from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home.html')
        else: 
            return render(request,'home.html') 
    else:
        return render(request,'index.html')    
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filters(username=username).exits():
                return redirect('register')
            elif User.objects.filter(email=email).exits():
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                return redirect('login')
        else:
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

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
