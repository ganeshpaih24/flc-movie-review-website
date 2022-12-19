from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from actor.models import Actor
from movie.models import Movie

# Create your views here.


def actors(request, actor_slug):
	actor = get_object_or_404(Actor, slug=actor_slug)
    movie_data=Movie.objects.filter(Actors=actor)
    
    context = {
		'movie_data': movie_data,
		'actor': actor,
	}
	template = loader.get_template('actor.html')
	return HttpResponse(template.render(context, request))
