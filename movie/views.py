from django.shortcuts import render ,redirect, get_or_create
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import requests
from movie.Models import Movie, Genre, Rating
from actor.Models import Actor
from django.utils.text import slugify



# Create your views here.
def landing(request):
    query=request.GET.get('q')
    if query:
        url='https://www.omdbapi.com/?apikey=c9161d22&s='+query
        response=requests.get(url)
        movie_data=response.json()
        context={
            'query':query,
            'movie_data':movie_data,
        }
        template=loader.get_template('search.html')
        return HttpResponse(template.render(context,request))
    return render(request,'landing.html')

def movieDetails(request,imdb_id):
    if Movie.objects.filter(imdbID=imdb_id).exists():
        movie_data=Movie.objects.get(imdbID=imdb_id)
        our_db=True
    else:
        url='http://www.omdbapi.com/?apikey=c9161d22&i='+imdb_id
        response=requests.get(url)
        movie_data=response.json()

        #inject
        rating_objs=[]
        genre_objs=[]
        actor_objs=[]

        #actor
        actor_list=[x.strip() for x in movie_data['Actors'].split(',')]
        for actor in actor_list:
            a,created=Actor.objects.get_or_create(name=actor)
            actor_objs.append(a)
            
        #genre
        genre_list=list(movie_data['Genre'].replace(" ","").split(','))
        for genre in genre_list:
            genre_slug=slugify(genre)
            g,created=Genre.objects.get_or_create(title=genre,slug=genre_slug)
            genre_objs.append(g)
        
        #Rate
        for rate in movie_data['Ratings']:
            r,created=Rating.objects.get_or_create(source=rate['Source'],rating=rate['Value'])
            rating_objs.append(r)
        
        
        m,created=Movie.objects.get_or_create(
            Title=movie_data['Title'],
            Year=movie_data['Year'],
            Rated=movie_data['Rated'],
            Released=movie_data['Released'],
            Runtime=movie_data['Runtime'],
            Director=movie_data['Director'],
            Writer=movie_data['Writer'],
            Plot=movie_data['Plot'],
            Language=movie_data['Language'],
            Country=movie_data['Country'],
            Awards=movie_data['Awards'],
            Poster_url=movie_data['Poster'],
            Type=movie_data['Type'],
        )
        m.Genre.set(genre_objs)
        m.Actors.set(actor_objs)
        m.Ratings.set(rating_objs)


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')


def search(request):
    return render(request,'search.html')
