from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from userextend.models import UserExtend


class UserExtendCreationForm(UserCreationForm):
    class Meta:
        model = UserExtend

        fields = []
        widgets = {

        }


class AuthenticationNewForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your username'
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your password'
            }
        )