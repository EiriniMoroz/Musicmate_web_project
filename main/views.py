from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def startpage(request):
    return render(request, 'main/startpage.html')

def searchMusicmates(request):
    if request.user.is_authenticated:
        return render(request, 'main/searchMusicmates.html')
    else:
        return redirect('login')
