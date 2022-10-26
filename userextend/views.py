from django.shortcuts import render
from django.views.generic import CreateView

from userextend.models import UserExtend


class EmployeeCreateView(CreateView):
    template_name = ''
    model = UserExtend
    form_class = ''


