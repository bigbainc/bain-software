# imports
from django.shortcuts import render, redirect
from .models import Question, Category
from .forms import questionForm
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models import Count, Q, Prefetch

@login_required #ensure user is logged in to access this view to prevent unauthorized access
def home_view(request): #the main view for the home page
    print("HOME VIEW RENDERED") #debug print to indicate the view is being accessed
    if request.method == "POST": #check if the request is a POST type (form submission)
        form = questionForm(request.POST) 
        #prevent creation of questions without login
        if not request.user.is_authenticated: #incase a users session expires while on the page
            return redirect('login') #they get redirected to the login page

        if form.is_valid(): 
            question = form.save(commit=False) #create a question object but don't save to database yet
            question.owner = request.user #set the owner of the question to the user making the request
            question.save() #now save the question to the database to generate a primary key
            selected_categories = list(form.cleaned_data.get('tags') or []) #get the selected existing categories from the form
            new_tags_input = form.cleaned_data.get('newtags', '') #new categories input from the form

            new_categories = [] #list to hold newly created category objects
            if new_tags_input: #if there are any new categories that are to be added
                newtaglist = [t.strip() for t in new_tags_input.split(',') if t.strip()] #split the input string into individual category names by splitting at the commas, also stripping whitespace
                for tag_name in newtaglist: #cycle through each new category name
                    category_obj, _ = Category.objects.get_or_create(name=tag_name) #the underscore is to ignore the boolean returned by get_or_create fucntion since this is not needed. the category object is either fetched from the database if it already exists or created if it doesn't
                    new_categories.append(category_obj) #append the new category object to the list

            combined_categories = list({c.id: c for c in chain(selected_categories, new_categories)}.values()) #combine the two lists, ensuring no duplicates by using a dictionary keyed by category id that iterates over both lists, taking the values and converting back to a list
            question.category.set(combined_categories) #overwrites the value of the field: cateogory, for the question object to the combined list of categories

            print("Question saved successfully.") #debug print to indicate successful save
            if request.POST.get('continue') == 'complete':
                return redirect('home')#sebd them back to the home page
        else:
            print("form error:", form.errors.as_json()) #debug print to show form errors if validation fails
    else:
        form = questionForm()

    user_questions = Question.objects.filter(owner=request.user).order_by('-createAt') #get all questions created by the logged in user ordering by creation date backwards
    categories = ( #annotate each category with the count of questions owned by the current user
        Category.objects.annotate(
            question_count=Count('questions', filter=Q(questions__owner=request.user))
        )
        .prefetch_related( #the prefetch related only fetches the questions related to each category that belong to the current user avoiding all questions being fetched for efficiency
            Prefetch('questions', queryset=user_questions, to_attr='owner_questions')
        )
        .order_by('name')
    )
    questions = user_questions

    context = {
        'form': form, #the question creation form (including category selection, question text, answers)
        'categories': categories, #all categories + question counts for the logged in user
        'questions': questions, #all questions created by the user
    }

    return render(request, 'home.html', context)