from django.urls import path

from . import views

app_name = "Pokedex"

urlpatterns = [

    path("", views.PokemonListView.as_view(), name="list"),
    path("listar/", views.PokemonListView.as_view(), name="list"),
    
]