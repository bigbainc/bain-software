from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('secondpage/', views.second_page, name='second_page'),
]