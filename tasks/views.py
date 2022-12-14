from django.contrib.auth.decorators import login_required
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.timesince import timesince
from django.views.generic import UpdateView

from tasks.forms import TaskCreationForm, TaskCommentForm
from tasks.models import Tasks
from userextend.models import UserExtend
from django.views.decorators.csrf import csrf_exempt


@login_required
def create_task(request):
    task_create_form = TaskCreationForm()
    users = UserExtend.objects.all()
    if request.method == 'POST':  # verificam daca metoda utilizata ii de POST
        print(request.POST)

        name = request.POST.get('name')
        description = request.POST.get('description')
        difficulty = request.POST.get('difficulty')
        assign_to = int(request.POST.get('assign-to'))

        if difficulty == 'easy':
            experience = 50
            currency = 50
        elif difficulty == 'medium':
            experience = 100
            currency = 100
        else:
            experience = 150
            currency = 150

        task_create = Tasks(
            name=name,
            description=description,
            difficulty=difficulty,
            assigned_to=assign_to,
            experience=experience,
            currency=currency,
            task_creator=UserExtend.objects.get(user_ptr_id=request.user.id)
        )
        task_create.save()
        return redirect('home')

    return render(request, 'tasks/create_task.html', {
        'form': task_create_form,
        'users': users
    })


# Create update task functionality for both managers and users, facem un singur formular si controlam ce se afiseaza din form in front end cu if-uri

@login_required
def update_task(request, pk):
    task_to_update = Tasks.objects.get(id=pk)  # aici vine id-ul din frontend
    task_update_form = TaskCreationForm(instance=task_to_update)
    users = UserExtend.objects.all()
    current_user = UserExtend.objects.get(user_ptr_id=request.user.id)
    if request.method == 'POST':
        print(request.POST)

        task_to_update.name = request.POST.get('name')
        task_to_update.description = request.POST.get('description')
        task_to_update.difficulty = request.POST.get('difficulty')
        task_to_update.active = request.POST.get('active')
        task_to_update.assigned_to = int(request.POST.get('assign-to'))
        task_to_update.task_textbox = request.POST.get('text_box')

        if task_to_update.difficulty == 'easy':
            task_to_update.experience = 50
            task_to_update.currency = 50
        elif task_to_update.difficulty == 'medium':
            task_to_update.experience = 100
            task_to_update.currency = 100
        else:
            task_to_update.experience = 150
            task_to_update.currency = 150

        task_to_update.save()
        return redirect('tasks')

    return render(request, 'tasks/update_tasks.html', {
        'form': task_update_form,
        'users': users,
        'current_user': current_user
    })


@login_required
def tasks(request):
    tasks_list = Tasks.objects.all()
    current_user = UserExtend.objects.get(user_ptr_id=request.user.id)
    return render(request, 'tasks/tasks.html', {'tasks': tasks_list, "current_user": current_user})


@csrf_exempt
def task_detail(request, pk):
    task = Tasks.objects.get(id=pk)
    data = {'id': task.id}
    if request.method == 'POST':
        comment_form = TaskCommentForm()
        query = request.POST
        task = Tasks.objects.get(id=query['id'])
        comments = {comment.creator: comment.body for comment in task.taskcomment_set.all()}
        context_data = {
            'task_id': task.id,
            'task_name': task.name,
            'task_description': task.description,
            'task_updated': task.updated_at.date(),
            'task_creator': task.task_creator,
            'comment_form': comment_form,
            'comments': comments,
            'task_assignee': task.assigned_to,
        }
        return render(request, 'tasks/task_detail.html', context_data)

    return HttpResponse(json.dumps(data), content_type='application/json')


def task_comment(request):
    comment_form = TaskCommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment_form.save()

    return redirect('tasks')
