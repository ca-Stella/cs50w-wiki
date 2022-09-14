from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("dne_error", views.entry, name="dne"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("already_exists_error", views.new, name="already_exists_error"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("wiki/", views.randompg, name="randompg")
]