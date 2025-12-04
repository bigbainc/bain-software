from django import forms
from .models import Question, Category

class questionForm(forms.ModelForm):
    newtags = forms.TextInput({
        "max_length":100,
        "required":False,
        "placeholder":"Enter new categories separated by commas"
    })
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
            "solution1": forms.TextInput(attrs={"rows":4, "cols":40, 'class':'answer-form'}),
            "solution2": forms.TextInput(attrs={"rows":4, "cols":40, 'class':'answer-form'}),
            "solution3": forms.TextInput(attrs={"rows":4, "cols":40, 'class':'answer-form'}),
            "solution4": forms.TextInput(attrs={"rows":4, "cols":40, 'class':'answer-form'}),
        }
