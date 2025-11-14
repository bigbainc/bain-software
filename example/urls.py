# example/urls.py
from django.urls import include, path
from django.shortcuts import render, HttpResponse
from example.views import index

def home(request):
    return HttpResponse("Welcome to the Home Page")

urlpatterns = [
    path('', index),
    path('login/', include('login.urls')),
]