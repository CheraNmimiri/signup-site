from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout



def home(request):
    return render(request,"homepage.html")

def signup(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,"Account created successfully" + user)
            return redirect(login)

            
    context = {'form': form}
    return render(request,"signup.html", context)

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user )
            return redirect(home)
    else:
        messages.info(request,"Username or password incorrect")
    
    context={}
    return render(request,"login.html" , context)