from django.shortcuts import render, redirect
from .models import Question
from .forms import questionForm


def home_view(request):
    if request.method == "POST":
        form = questionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = questionForm()
    context = {'form': form}

    return render(request, 'home.html', context)

def test_view(request):
    return render(request, 'test.html')
