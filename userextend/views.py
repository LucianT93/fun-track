from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from tasks.models import Tasks
from userextend.forms import UserExtendCreationForm, UserUpdateForm
from userextend.models import UserExtend


def user_login_registration(request):
    register_user_form = UserExtendCreationForm()
    if request.method == 'POST':
        if request.POST.get('flag') == 'login':
            username = request.POST['user-login']
            password = request.POST['password-login']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect')
        else:
            registered_user_form = UserExtendCreationForm(request.POST)
            if registered_user_form.is_valid():
                registered_user_form.save()
                return redirect('home')

    return render(request, 'registration/login.html', {'form': register_user_form})


def user_logout(request):
    logout(request)
    return redirect('home')


def get_account(request):
    account = UserExtend.objects.get(user_ptr_id=request.user.id)
    tasks = Tasks.objects.filter(assigned_to=account.id)
    return render(request, 'account/account.html', {'account': account, 'tasks': tasks})


def update_account(request):
    user_to_update = UserExtend.objects.get(user_ptr_id=request.user.id)
    user_update_form = UserUpdateForm(instance=user_to_update)
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, request.FILES, instance=user_to_update)
        print(user_update_form.is_valid())
        if user_update_form.is_valid():
            user_update_form.save()
            return redirect('account')

    return render(request, 'account/update_account.html', {'form': user_update_form})
