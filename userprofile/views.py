from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from userprofile.models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import get_user_model
from django.contrib import messages


User = get_user_model()


def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #profile = Profile()
        #profile.user = request.user
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        #profile = Profile()
        #profile.user = request.user
        #profile.save()
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        context ={
        'u_form': u_form,
        'p_form': p_form,
        }
    return render(request, 'userprofile/edit-my-profile.html',context)

def searchMusicmates(request):
    query = request.GET.get('q')
    object_list = Profile.objects.filter(city__exact=query)
    context ={
		'users': object_list
	}
    return render(request, "userprofile/searchMusicmates.html",context)

def searchMusicmatesForm(request):
	return render(request, "userprofile/searchMusicmatesForm.html")
