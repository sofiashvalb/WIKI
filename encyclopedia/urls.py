from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("edit/", views.edit, name="edit"),
    path("changed/", views.changed, name="changed"),
    path("random_entry/", views.random_entry, name="random_entry")
]
