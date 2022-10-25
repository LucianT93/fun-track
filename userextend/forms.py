from django import forms
from django.contrib.auth.forms import UserCreationForm

from userextend.models import UserExtend


class UserExtendCreationForm(UserCreationForm):
    class Meta:
        model = UserExtend

        fields = []
        widgets = {

        }