from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userextend.forms import UserExtendCreationForm
from userextend.models import UserExtend


class EmployeeCreateView(CreateView):
    template_name = 'registration/register.html'
    model = UserExtend
    form_class = UserExtendCreationForm
    success_url = reverse_lazy('home')


