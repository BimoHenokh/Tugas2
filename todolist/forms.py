from tkinter import Widget
from attr import attr
from django import forms
from .models import Task

# komponen halaman form
class TodolistModelForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user', 'date')
        fields = ('title', 'description')

        Widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})

        }