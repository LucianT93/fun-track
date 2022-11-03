from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from tasks.forms import TaskCreationForm
from tasks.models import Tasks
from userextend.models import UserExtend


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


#Create update task functionality for both managers and users, facem un singur formular si controlam ce se afiseaza din form in front end cu if-uri


def update_task(request, pk):
    task_to_update = Tasks.objects.get(id=pk) #aici vine id-ul din frontend
    task_update_form = TaskCreationForm(instance=task_to_update)

    users = UserExtend.objects.all()
    if request.method == 'POST':
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

        task_update, created = Tasks.objects.update_or_create(
            name=name,
            description=description,
            difficulty=difficulty,
            assigned_to=assign_to,
            experience=experience,
            currency=currency,
            task_creator=UserExtend.objects.get(user_ptr_id=request.user.id),
        )
        # print(task_update)
        task_update.save()



    return render(request, 'tasks/update_tasks.html', {
        'form': task_update_form,
        'users': users,
    })
