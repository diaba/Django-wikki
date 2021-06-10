from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("webpage", views.webpage, name="webpage"),
    path("search", views.search, name="search"),
    path("<str:title>", views.entrypage, name="entrypage"),
]
