from django.http import HttpResponse
from django.shortcuts import render

def login_view(request):
    return HttpResponse("This is the login page.")

def second_page(request):
    return render(request, 'secondpage.html')
