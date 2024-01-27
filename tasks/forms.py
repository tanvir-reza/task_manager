from django.forms import ModelForm
from django import forms
from .models import Task



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','images','priority','complete','due_date']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','required':True}),
            'description': forms.Textarea(attrs={'class':'form-control','required':'True'}),
            'complete': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'due_date': forms.DateInput(attrs={'class':'form-control','type': 'date','required':True}),
            'priority': forms.Select(attrs={'class':'form-control','required':True}),
            'images': forms.FileInput(attrs={'class':'form-control'}),
        }
