from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("dne_error", views.entry, name="dne"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new")
]