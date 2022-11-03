from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, models

from userextend.models import UserExtend


class UserExtendCreationForm(UserCreationForm):
    class Meta:
        model = UserExtend

        fields = ['image', 'username', 'email', 'password1', 'password2']

        widgets = {
            'email': EmailInput(attrs={
                'placeholder': 'Please enter your email'
            }),
            'username': TextInput(attrs={
                'placeholder': 'Please enter your username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Please enter your password',
                'id': 'pass1_register'
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Please enter your password again',
                'id': 'pass2_register'
            }
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserExtend
        fields = ['image', 'first_name', 'last_name']
