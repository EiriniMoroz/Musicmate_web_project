
from django.contrib import admin
from django.urls import path, include
from . import views
import users

urlpatterns = [
    path('', views.about, name='startpage'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),



]
