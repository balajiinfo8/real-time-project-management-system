from django import forms
from .models import Todo , Project

# todo models 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'project',
            'title',
            'details',
            'completed'
                ]

# Project models 
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =[
            'name',
            'description',
        ]