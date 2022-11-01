from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from userextend.forms import UserExtendCreationForm
from userextend.models import UserExtend


class EmployeeCreateView(CreateView):
    template_name = 'registration/register.html'
    model = UserExtend
    form_class = UserExtendCreationForm
    success_url = reverse_lazy('home')


def user_login_registration(request):
    register_user_form = UserExtendCreationForm()
    if request.method == 'POST':
        if request.POST.get('flag') == 'login':
            print(request.POST)
            username = request.POST['user-login']
            password = request.POST['password-login']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect')
        else:
            print(request.POST)
            registered_user_form = UserExtendCreationForm(request.POST)
            if registered_user_form.is_valid():
                registered_user_form.save()
                return redirect('home')

    return render(request, 'registration/login.html', {'form': register_user_form})


def user_logout(request):
    logout(request)
    return redirect('home')
