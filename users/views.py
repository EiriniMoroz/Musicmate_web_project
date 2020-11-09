from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def registerPage(request):
	if request.method == 'POST':

		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			#new_user = User.objects.create_user(username=username, password=password)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can now login!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'main/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('startpage')
