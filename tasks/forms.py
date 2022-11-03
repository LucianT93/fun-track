from django.forms import models, TextInput, Textarea, Select
from django import forms
from tasks.models import Tasks


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['assigned_to','experience','currency', 'task_textbox', 'task_creator', 'active']

        widgets = {
            'name' : TextInput(attrs={'placeholder': 'Please enter the task name',
                                           'class': ''}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description',
                                           'class': 'form-control'}),
            'difficulty' : Select()
        }

# class TaskUpdateForm(models.ModelForm):
#     class Meta:
#         model = Tasks
#         exclude = ['experience','currency', 'task_textbox', 'task_creator']
#
#         widgets = {
#             'name'
#         }
