from django.shortcuts import render, redirect
from .models import Question
from .forms import questionForm


def home_view(request):
    return render(request, 'home.html')

def test_view(request):
    return render(request, 'test.html')

def addQuestion(request):
    if request.method == "POST":
        form = Question(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_question")
    else:
        form = questionForm()
    entries = Question.objects.order_by("-id")[:20]
    return render(request, "home/home.html", {"form": form, "entries": entries})

def getQuestion(request):
    model = Question
    templateName = "home/home.html"
    def get_queryset(self):
        return Question.objects()