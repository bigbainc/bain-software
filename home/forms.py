from django import forms
from .models import Question, Category

class questionForm(forms.ModelForm):
    newtags = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class':'newtags-input', "placeholder":"Enter new categories separated by commas",}),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple 
    )
    class Meta:
        model = Question
        fields = ["question", "solution1", "solution2", "solution3", "solution4"]
        widgets = {
            "question": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Question...", 'class':'question-form'}),
            "solution1": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Answer 1", 'class':'answer-form'}),
            "solution2": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Answer 2", 'class':'answer-form'}),
            "solution3": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Answer 3", 'class':'answer-form'}),
            "solution4": forms.TextInput(attrs={"rows":4, "cols":40, 'placeholder':"Answer 4", 'class':'answer-form'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        new_tags_input = cleaned_data.get('newtags') or ''

        uniqueNewNames = []
        for raw_name in new_tags_input.split(','): #cycle through each category by splitting at comma
            name = raw_name.strip() #remove leading and trailing whitespace
            if not name: 
                continue #skip empty names
            if name not in uniqueNewNames: #the names not already in the list
                uniqueNewNames.append(name) #add unique names to the list 

        if uniqueNewNames: #if any categories were actually created
            existingQuerySet = Category.objects.filter(name__in=uniqueNewNames) #get existing category objects from the database
            existingNames = existingQuerySet.values_list('name', flat=True) #extract just the names from the queryset
            namesToCreate = [name for name in uniqueNewNames if name not in existingNames]
            totalAfterCreate = Category.objects.count() + len(namesToCreate)

            if totalAfterCreate > 4:
                message = "Only 4 categories allowed, this category can't be added"
                self.add_error('newtags', message)
                raise forms.ValidationError(message)

        return cleaned_data
