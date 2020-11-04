from django.contrib import admin
from django.urls import path, include
from .views import *
import userprofile

urlpatterns = [
    path('edit-my-profile/', ProfileEditView.as_view(), name="edit")
]
