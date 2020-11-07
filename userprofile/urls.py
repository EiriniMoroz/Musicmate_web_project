from django.contrib import admin
from django.urls import path, include
from .views import *
import userprofile
from . import views


urlpatterns = [
    path('edit-my-profile/', views.edit_profile, name="edit"),
    path('search-musicmates/', views.searchMusicmates, name='searchMusicmates'),
    path('search-musicmates-form/', views.searchMusicmatesForm, name='searchMusicmatesForm')


]
