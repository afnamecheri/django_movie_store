from django.urls import path
from .views import MovieCreateView, MovieDetailView,MovieUpdateView, MovieListView, MoviesByGenreView, MoviesByActorView, MoviesByDirectorView,HomeView,GenreListView,ActorListView,DirectorListView

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/genre/<int:genre_id>/', MoviesByGenreView.as_view(), name='movies-by-genre'),
    path('movies/actor/<int:actor_id>/', MoviesByActorView.as_view(), name='movies-by-actor'),
    path('movies/director/<int:director_id>/', MoviesByDirectorView.as_view(), name='movies-by-director'),
    path('movies/genres/', GenreListView.as_view(), name='genre-list'),
    path('movies/actors/', ActorListView.as_view(), name='actor-list'),
    path('movies/directors/', DirectorListView.as_view(), name='director-list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)