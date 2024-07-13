from django.urls import path

from movies import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/<int:movies_id>/", views.movies, name="movies"),
]