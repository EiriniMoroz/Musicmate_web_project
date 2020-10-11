from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect ('login')
        context = {'form': form}
        return render(request, 'users/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password =  request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'users/login.html', context)

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'main/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
