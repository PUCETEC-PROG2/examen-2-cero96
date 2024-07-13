from django.http import HttpResponse
from django.template import loader
from .models import Movies

def index(request):
    #pokemons = Pokemon.objects.all() ## SELECT * FROM pokedex_pokemon
    movies = Movies.objects.order_by('type') ## SELECT * FROM pokedex_pokemon ORD
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))

def movies(request, movies_id):
    #SELECT * FROM pokedex_pokemon WHERE id='pokemon_id'
    pokemon = Movies.objects.get(id=movies_id)
    template = loader.get_template('display_movies.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))