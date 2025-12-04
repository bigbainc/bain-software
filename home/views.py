from django.shortcuts import render, redirect
from .models import Question, Category
from .forms import questionForm
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    print("HOME VIEW RENDERED")
    if request.method == "POST":
        print("POST request received")
        form = questionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            newtags = form.cleaned_data.get('newtags')
            if newtags:
                newtaglist = [t.strip() for t in newtags.split(',') if t.strip()]
                for tag_name in newtaglist:
                    category_obj, created = Category.objects.get_or_create(name=tag_name)
                    form.instance.category.add(category_obj)# add the new category to the existing list
            question = form.save(commit=False)
            question.owner = request.user
            question.save()
            question.category.set(form.cleaned_data['tags']) 
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