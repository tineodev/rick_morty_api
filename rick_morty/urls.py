from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, logout_then_login
from .views import CreateUser

urlpatterns = [
    path("", views.Index.as_view(), name="index"),

    path("list/", views.ListDB.as_view(), name="list"),
    path("detail/<int:id>", views.DetailDB.as_view(), name="detail"),

    path("main_page/", views.MainPage.as_view(), name="main"),
    path("generate/", views.GenerateDB.as_view(), name="generate"),
    path("delete/", views.DeleteDB.as_view(), name="delete"),

    path("accounts/login/", LoginView.as_view(), name="login"),
    path("register/", CreateUser.as_view(), name="register"),
    path("logout/", logout_then_login, name="logout"),
]