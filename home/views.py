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
            selected_categories = list(form.cleaned_data.get('tags') or [])
            new_tags_input = form.cleaned_data.get('newtags', '')

            new_categories = []
            if new_tags_input:
                newtaglist = [t.strip() for t in new_tags_input.split(',') if t.strip()]
                for tag_name in newtaglist:
                    category_obj, _ = Category.objects.get_or_create(name=tag_name)
                    new_categories.append(category_obj)

            combined_categories = list({c.id: c for c in chain(selected_categories, new_categories)}.values())
            question.category.set(combined_categories)

            print("Question saved successfully.")
            if request.POST.get('continue') == 'complete':
                return redirect('home')
        else:
            print("form error:", form.errors.as_json())
    else:
        form = questionForm()

    return render(request, 'home.html', {'form': form})

def get_categoryTitles(request):
    categories = Category.objects.all()
    print("catergories found:", categories)
    categoryTitles = [category.name for category in categories]
    print("category titles:", categoryTitles)
    return categoryTitles