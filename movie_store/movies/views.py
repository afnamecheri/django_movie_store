from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import Movie,Genre,Actor,Director
from .forms import MovieForm

from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'home.html', {'movies': movies})
    
class ActorListView(View):
    def get(self, request):
        actors = Actor.objects.all()  # Fetch all actors
        return render(request, 'actors_list.html', {'actors': actors})

class DirectorListView(View):
    def get(self, request):
        directors = Director.objects.all()  # Fetch all directors
        return render(request, 'director_list.html', {'directors': directors})


class GenreListView(View):
    def get(self, request):
        genres = Genre.objects.all()  # Fetch all genres
        return render(request, 'genre_list.html', {'genres': genres})

class MovieDetailView(LoginRequiredMixin,View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return render(request, 'movie_detail.html', {'movie': movie})

class MovieCreateView(LoginRequiredMixin,View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'movie_form.html', {'form': form})

    def post(self, request):
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        return render(request, 'movie_form.html', {'form': form})
    
class MovieUpdateView(LoginRequiredMixin,View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(instance=movie)
        return render(request, 'movie_form.html', {'form': form})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-detail', pk=movie.pk)
        return render(request, 'movie_form.html', {'form': form})
    
class MovieListView(LoginRequiredMixin,View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movie_list.html', {'movies': movies})

class MoviesByGenreView(LoginRequiredMixin,View):
    def get(self, request, genre_id):
        genre = get_object_or_404(Genre, id=genre_id)
        movies = genre.movies.all()
        return render(request, 'movie_list.html', {'movies': movies, 'genre': genre})

class MoviesByActorView(LoginRequiredMixin,View):
    def get(self, request, actor_id):
        actor = get_object_or_404(Actor, id=actor_id)
        movies = actor.movies.all()
        return render(request, 'movie_list.html', {'movies': movies, 'actor': actor})

class MoviesByDirectorView(LoginRequiredMixin,View):
    def get(self, request, director_id):
        director = get_object_or_404(Director, id=director_id)
        movies = director.movies.all()
        return render(request, 'movie_list.html', {'movies': movies, 'director': director})