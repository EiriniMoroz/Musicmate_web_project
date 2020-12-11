from django.contrib import admin
from django.urls import path, include
from .views import *
import userprofile
from . import views
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, userProfileDetailView

urlpatterns = [
    path('edit-my-profile/', views.edit_profile, name="edit"),
    path('search-musicmates/', views.searchMusicmates, name='searchMusicmates'),
    path('search-musicmates-form/', views.searchMusicmatesForm, name='searchMusicmatesForm'),
    path('all-profiles/',UserProfileListCreateView.as_view(),name='all-profiles'),
   # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
    path('view_profile/<slug>/', views.profile_view, name='view-profile'),
	path('friends/', views.friend_list, name='friend_list'),
    path('user/<slug>/', views.profile_view, name='view-profile'),
    path('users/friend-request/send/<int:id>/', views.send_friend_request, name='send_friend_request'),
	path('users/friend-request/cancel/<int:id>/', views.cancel_friend_request, name='cancel_friend_request'),
	path('users/friend-request/accept/<int:id>/', views.accept_friend_request, name='accept_friend_request'),
	path('users/friend-request/delete/<int:id>/', views.delete_friend_request, name='delete_friend_request'),
	path('users/friend/delete/<int:id>/', views.delete_friend, name='delete_friend'),



]
