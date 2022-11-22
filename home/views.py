from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Create your views here.

def home_view(request):
    if not request.user.is_authenticated:
        return render(request, 'home/home.html')
    else:
        return redirect('tasks')
