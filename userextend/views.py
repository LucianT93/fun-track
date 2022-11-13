import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from tasks.models import Tasks
from userextend.forms import UserExtendCreationForm, UserUpdateForm
from userextend.models import UserExtend


def render_login_registration(request):
    register_user_form = UserExtendCreationForm()
    return render(request, 'registration/login.html', {'form': register_user_form})


def user_login(request):
    print(request.POST)

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    print(user)
    if user:
        login(request, user)
        return HttpResponse(json.dumps({'message': 'success'}), content_type='application/json')
    return HttpResponse(json.dumps({"message": "denied"}), content_type="application/json")


def user_registration(request):
    registered_user_form = UserExtendCreationForm(request.POST)
    if registered_user_form.is_valid():
        registered_user_form.save()
        return HttpResponse(json.dumps({'message': 'success'}), content_type='application/json')
    return HttpResponse(json.dumps({"message": "denied"}), content_type="application/json")


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def get_account(request):
    account = UserExtend.objects.get(user_ptr_id=request.user.id)
    tasks = Tasks.objects.filter(assigned_to=account.id)
    return render(request, 'account/account.html', {'account': account, 'tasks': tasks})


@login_required
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
