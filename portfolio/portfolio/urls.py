
from django.contrib import admin
from django.urls import path
from .views import homepage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', homepage)
    
]
