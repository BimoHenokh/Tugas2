from django import forms
from .models import Task

class TodolistModelForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user', 'date')
        fields = ('title', 'description')