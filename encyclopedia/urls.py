from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("dne_error", views.entry, name="dne"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("already_exists_error", views.new, name="already_exists_error"),
    path("wiki/<str:entry>/edit", views.edit, name="edit")
]