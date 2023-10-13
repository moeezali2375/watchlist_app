from django.urls import path, include
from watchlist_app.api.views import movie_list, movie_detail, delete_movie

urlpatterns = [
    path("list/", movie_list, name="movie-list"),
    path("<int:pk>", movie_detail, name="movie-detail"),
    path("delete/<int:pk>", delete_movie, name="movie-delete"),
]
