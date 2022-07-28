from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [

    path("register", views.register, name="register"),
    path("login", views.login, name="login"),


]
