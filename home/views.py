from django.shortcuts import render, redirect
from .models import Question, Category
from .forms import questionForm
from django.contrib.auth.decorators import login_required
from itertools import chain

@login_required
def home_view(request):
    print("HOME VIEW RENDERED")
    if request.method == "POST":
        print("POST request received")
        form = questionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.owner = request.user
            question.save()
            newCategories = [] # start with empty list
            if newCategories:
                newtaglist = [t.strip() for t in newCategories.split(',') if t.strip()] #splits on commas and removes extra spaces
                for tag_name in newtaglist:
                    category_obj, _ = Category.objects.get_or_create(name=tag_name)
                    newCategories.append(category_obj)# add the new category to the existing list
            question = form.save(commit=False)
            question.save()
            selectedCatagories = form.cleaned_data['tags']  # get selected categories from the form
            combinedList = list({c.id: c for c in chain(selectedCatagories, newCategories)}.values()) # get selected categories from the form AND the new ones
            question.category.set(combinedList) 
            form.save_m2m()
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