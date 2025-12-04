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
