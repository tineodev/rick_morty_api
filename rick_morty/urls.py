from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("generate/", views.GenerateDB.as_view(), name="generate"),
    path("delete/", views.DeleteDB.as_view(), name="delete"),
    path("list/", views.ListDB.as_view(), name="list"),
]