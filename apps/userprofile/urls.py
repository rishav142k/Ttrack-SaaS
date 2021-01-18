from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("signup/", views.signup.as_view(), name = "signup"),
    path("login/", auth_views.LoginView.as_view(template_name = 'userprofile/login.html'), name = "login")
]