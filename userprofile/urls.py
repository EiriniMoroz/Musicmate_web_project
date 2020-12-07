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


]
