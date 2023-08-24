from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.show_all_directors, name='list_directors'),
    path('directors/<int:info_director>', views.show_one_director, name='one_director'),
    path('actors/', views.show_all_actors, name='list_actors'),
    path('actors/<int:info_actor>', views.show_one_actor, name='one_actor'),
]