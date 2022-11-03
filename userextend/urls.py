from django.urls import path

from userextend import views

urlpatterns = [
    # path('register/', views.EmployeeCreateView.as_view(), name='register'),
    path('login/', views.user_login_registration, name='login'),
    path("logout/", views.user_logout, name="logout"),
    path("account/", views.get_account, name='account'),
    path("update_account/", views.update_account, name='update_account'),
]
