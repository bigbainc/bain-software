from django import forms
from .models import Question

class questionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question", "solution1", "solution2", "solution3", "solution4"]
        widgets = {
            "Question": forms.Textarea(attrs={"rows":4, "cols":40}),
            "Solution1": forms.Textarea(attrs={"rows":4, "cols":40}),
            "Solution2": forms.Textarea(attrs={"rows":4, "cols":40}),
            "Solution3": forms.Textarea(attrs={"rows":4, "cols":40}),
            "Solution4": forms.Textarea(attrs={"rows":4, "cols":40}),
        }
