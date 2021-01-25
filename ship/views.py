from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.http import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from ship.models import Product

def index(request):
    product=Product.objects.values().order_by('date')
    if request.method=='POST':
        filter=request.POST['filterdate']
        if filter is None:
            product=Product.objects.values()
        else:
            product=Product.objects.values().filter(date=filter)
    return render(request,'index.html',{'product_list': product})
def add(request):
    if request.method=='POST':
        product_name = request.POST['Item name']
        product_quantity = request.POST['Item quantity']
        status = request.POST['Item status']
        date = request.POST['Date']
        Product.objects.create(product_name=product_name,product_quantity=product_quantity,status=status,date=date)
        return redirect('index')
    return render(request,'HTML/add.html')

def update(request,id):
    product = Product.objects.values().filter(id=id)
    if request.method=='POST':
        product_name = request.POST['Item name']
        product_quantity = request.POST['Item quantity']
        status = request.POST['Item status']
        date = request.POST['Date']
        Product.objects.filter(id=id).update(product_name=product_name,product_quantity=product_quantity,status=status,date=date)
        return redirect('index')
    return render(request,'HTML/update.html', {'product': product})

def delete(request,id):
    Product.objects.filter(id=id).delete()
    return redirect(index)

def signup(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'HTML/signup.html', {'form': form})
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "HTML/login.html",
                    context={"form":form})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')
