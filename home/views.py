from django.shortcuts import render, redirect
from .models import Question
from .forms import questionForm
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    print("HOME VIEW RENDERED")
    if request.method == "POST":
        print("POST request received")
        form = questionForm(request.POST)
        category = request.POST.getlist('tags')
        if form.is_valid():
            if newtags := form.cleaned_data.get('newtags'):
                newtaglist = [tag.strip() for tag in newtags.split(',') if tag.strip()]
                for tag_name in newtaglist:
                    category_obj, created = questionForm.objects.get_or_create(name=tag_name)
                    form.instance.category.add(category_obj)
            question = form.save(commit=False)
            form.instance.owner = request.user
            form.save()
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