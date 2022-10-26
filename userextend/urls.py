from django.urls import path

from userextend import views

urlpatterns = [
    path('register/', views.EmployeeCreateView.as_view(), name='register')
]
