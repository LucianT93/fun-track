from django.urls import path

from userextend import views

urlpatterns = [
    path('get_login_register/', views.render_login_registration, name='get_login_register'),
    path('login_register/', views.user_login_registration, name='login_register'),
    path("logout/", views.user_logout, name="logout"),
    path("account/", views.get_account, name='account'),
    path("update_account/", views.update_account, name='update_account'),
]
