from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


# Create your views here.


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('Hello'),
        int_field=Value(123),
        new_budget=F('budget') + 100,
    ).annotate(ffff=F('rating')+F('year'),)
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    # for movie in movies:
        # movie.save()
    return render(request, 'movie_app/all_movies.html',
                  {'movies': movies,
                   'agg': agg,
                   'total': movies.count()
                   })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html',
                  {'movie': movie})


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html',
                  {
                      'directors': directors
                  })

def show_one_director(request, info_director: int):
    director = get_object_or_404(Director, id=info_director)
    return render(request, 'movie_app/one_director.html',
                  {
                      'director': director
                  })

def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html',
                  {
                      'actors': actors
                  })

def show_one_actor(request, info_actor: int):
    actor = get_object_or_404(Actor, id=info_actor)
    return render(request, 'movie_app/one_actor.html',
                  {
                      'actor': actor
                  })

