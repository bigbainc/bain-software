from django.shortcuts import render, redirect
from .models import Question
from .forms import questionForm


def home_view(request):
    print("HOME VIEW RENDERED")
    if request.method == "POST":
        print("POST request received")
        form = questionForm(request.POST)
        if form.is_valid():
            form.save()
            print("Question saved successfully.")
            if request.POST.get('continue') == 'complete':
                return redirect('home')
    else:
        print("ERROR OCCURED: invalid form")
        form = questionForm()
        print("form error:", form.errors.as_json())

    return render(request, 'home.html', {'form': form})

def test_view(request):
    return render(request, 'test.html')