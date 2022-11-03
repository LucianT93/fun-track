from django.urls import path

from tasks import views

urlpatterns = [
    path('create-task/', views.create_task, name="create_task"),
    path('update-task/<int:pk>', views.update_task, name="update_task"),
]
