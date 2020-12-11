from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from userprofile.models import Profile, FriendRequest
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer
from django.http import HttpResponseRedirect

from django.template.context_processors import csrf

User = get_user_model()

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
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
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context ={
        'u_form': u_form,
        'p_form': p_form,
        }
        context.update(csrf(request))#
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


class UserProfileListCreateView(ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]



@login_required
def profile_view(request, slug):
	p = Profile.objects.filter(slug=slug).first()
	u = p.user
	sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
	rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)

	friends = p.friends.all()

	# is this user our friend
	button_status = 'none'
	if p not in request.user.profile.friends.all():
		button_status = 'not_friend'

		# if we have sent him a friend request
		if len(FriendRequest.objects.filter(
			from_user=request.user).filter(to_user=p.user)) == 1:
				button_status = 'friend_request_sent'

	context = {
		'u': u,
		'button_status': button_status,
		'friends_list': friends,
		'sent_friend_requests': sent_friend_requests,
		'rec_friend_requests': rec_friend_requests,
        'profile_image': p.profile_image
	}

	return render(request, "userprofile/profile.html", context)

def friend_list(request):
	p = request.user.profile
	friends = p.friends.all()
	context={
	'friends': friends
	}
	return render(request, "userprofile/friend_list.html", context)

@login_required
def send_friend_request(request, id):
	user = get_object_or_404(User, id=id)
	frequest, created = FriendRequest.objects.get_or_create(
			from_user=request.user,
			to_user=user)
	return HttpResponseRedirect('/user/{}'.format(user.profile.slug))

@login_required
def cancel_friend_request(request, id):
	user = get_object_or_404(User, id=id)
	frequest = FriendRequest.objects.filter(
			from_user=request.user,
			to_user=user).first()
	frequest.delete()
	return HttpResponseRedirect('/user/{}'.format(user.profile.slug))

@login_required
def accept_friend_request(request, id):
	from_user = get_object_or_404(User, id=id)
	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
	user1 = frequest.to_user
	user2 = from_user
	user1.profile.friends.add(user2.profile)
	user2.profile.friends.add(user1.profile)
	frequest.delete()
	return HttpResponseRedirect('/user/{}'.format(request.user.profile.slug))

@login_required
def delete_friend_request(request, id):
	from_user = get_object_or_404(User, id=id)
	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
	frequest.delete()
	return HttpResponseRedirect('/user/{}'.format(request.user.profile.slug))

def delete_friend(request, id):
	user_profile = request.user.profile
	friend_profile = get_object_or_404(Profile, id=id)
	user_profile.friends.remove(friend_profile)
	friend_profile.friends.remove(user_profile)
	return HttpResponseRedirect('/user/{}'.format(friend_profile.slug))
