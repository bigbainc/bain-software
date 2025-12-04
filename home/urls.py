from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'), #the single url which is just the home view that is displayed at the root (no path specified, just he domain name)
]