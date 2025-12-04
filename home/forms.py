from django import forms
from .models import Question

class questionForm(forms.ModelForm):
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
