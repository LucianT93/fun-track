from django.forms import models, TextInput, Textarea, Select

from tasks.models import Tasks


class TaskCreationForm(models.ModelForm):
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