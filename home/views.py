from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')

def statistics_view(request):
    return render(request, 'statistics.html')
