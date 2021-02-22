from django import forms
from .models import Problems

class ProblemCreateForm(forms.ModelForm):

    class Meta:
        model = Problems
        fields = ['name_problem', 'url_problem', 'number_solved', 'difficulty', 'reject']