from django import forms
from .models import Question, Category

class questionForm(forms.ModelForm): #form to create new questions and assign categories
    newtags = forms.CharField( #field for entering new categories
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class':'newtags-input', "placeholder":"Enter new categories separated by commas",}), #custom CSS class and placeholder text
    )
    tags = forms.ModelMultipleChoiceField( #field for selecting existing categories
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple #displays as checkboxes for selecting multiple categories
    )
    class Meta: #metadata for the form
        model = Question
        fields = [ #the fields from the model that are included in the form
            "question",
            "solution1",
            "solution2",
            "solution3",
            "solution4",
            "correct_answer",
        ]
        widgets = { #the widgets used for each field to customise their appearance
            "question": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Question...", 'class':'question-form'}), #specify rows and cols for size, placeholder text, and css class
            "solution1": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Answer 1", 'class':'answer-form'}),
            "solution2": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Answer 2", 'class':'answer-form'}),
            "solution3": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Answer 3", 'class':'answer-form'}),
            "solution4": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Answer 4", 'class':'answer-form'}),
            "correct_answer": forms.RadioSelect(attrs={'class': 'correct-answer-select'}), #radio buttons (the circular ones) for selecting the correct answer
        }

    def clean(self): #custom data validation for the form
        cleaned_data = super().clean() #get the cleaned data from the parent class
        new_tags_input = cleaned_data.get('newtags') or '' #get the newtags input and default to empty string if none

        uniqueNewNames = [] #start with an empty list for the unique category names
        for raw_name in new_tags_input.split(','): #cycle through each category by splitting at comma
            name = raw_name.strip() #remove leading and trailing whitespace
            if not name: 
                continue #skip empty names
            if name not in uniqueNewNames: #the names not already in the list
                uniqueNewNames.append(name) #add unique names to the list 

        if uniqueNewNames: #if any categories were actually created
            existingQuerySet = Category.objects.filter(name__in=uniqueNewNames) #get existing category objects from the database
            existingNames = existingQuerySet.values_list('name', flat=True) #extract just the names from the queryset
            namesToCreate = [name for name in uniqueNewNames if name not in existingNames] #determine which names need to be created
            totalAfterCreate = Category.objects.count() + len(namesToCreate) #calculate total number of categories after creation of new ones

            if totalAfterCreate > 4: #set a maximum of 4 categories
                message = "Only 4 categories allowed, this category can't be added"
                self.add_error('newtags', message)
                raise forms.ValidationError(message)

        return cleaned_data
