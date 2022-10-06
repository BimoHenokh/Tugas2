from django import forms
from .models import Task

# komponen halaman form
class TodolistModelForm(forms.ModelForm):
    title = forms.TextInput
    description = forms.Textarea

    class Meta:
        model = Task
        exclude = ['user', 'date']
        fields = ['title', 'description']