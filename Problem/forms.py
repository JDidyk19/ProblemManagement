from django import forms
from .models import Problems, Notate

class ProblemCreateForm(forms.ModelForm):

    class Meta:
        model = Problems
        fields = ['name_problem', 'url_problem', 'number_solved', 'difficulty', 'reject']

class ProblemEditForm(forms.ModelForm):

    class Meta:
        model = Problems
        fields = ['number_solved', 'reject',]

class AddNotateForm(forms.ModelForm):

    class Meta:
        model = Notate
        fields = ['notate']

class EditNotateForm(forms.ModelForm):

    class Meta:
        model = Notate
        fields = ['notate']
