from django.urls import path

from tasks import views

urlpatterns = [
    path('create-task/', views.create_task, name="create_task"),
    path('update-task/<int:pk>', views.update_task, name="update_task"),
    path('tasks/', views.tasks, name="tasks"),
    path('task_detail/<int:pk>', views.task_detail, name="task_detail"),
    path('task_detail_html/', views.task_detail_html, name="task_detail_html"),
]
