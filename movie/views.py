from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .models import Movie, Genre, Rating
from actor.models import Actor
from django.utils.text import slugify
from user.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse

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

@login_required(login_url='login')
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
        # actor_list=[x.strip() for x in movie_data['Actors'].split(',')]
        # for actor in actor_list:
        #     a,created=Actor.objects.get_or_create(name=actor)
        #     actor_objs.append(a)
            
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

        #Language
        language_list=[x.strip() for x in movie_data['Language'].split(',')]
        if language_list[0] == 'Hindi':
            genre_slug=slugify("Bollywood")
            g,created=Genre.objects.get_or_create(title="Bollywood",slug=genre_slug)
            genre_objs.append(g)
        elif language_list[0] == 'English':
            genre_slug=slugify("Hollywood")
            g,created=Genre.objects.get_or_create(title="Hollywood",slug=genre_slug)
            genre_objs.append(g)
        elif language_list[0] == 'Tamil':
            genre_slug=slugify("Kollywood")
            g,created=Genre.objects.get_or_create(title="Kollywood",slug=genre_slug)
            genre_objs.append(g)
        elif  language_list[0] == 'Telugu':
            genre_slug=slugify("Tollywood")
            g,created=Genre.objects.get_or_create(title="Tollywood",slug=genre_slug)
            genre_objs.append(g)
        elif language_list[0] == 'Kannada':
            genre_slug=slugify("Sandalwood")
            g,created=Genre.objects.get_or_create(title="Sandalwood",slug=genre_slug)
            genre_objs.append(g)
        else:
            genre_slug=slugify("Others")
            g,created=Genre.objects.get_or_create(title="Others",slug=genre_slug)
            genre_objs.append(g)
        
        if language_list[0] == 'Japanese' and genre_list[0] == 'Animation' and movie_data['Type'] == 'series':
            genre_slug=slugify("Anime")
            g,created=Genre.objects.get_or_create(title="Anime",slug=genre_slug)
            genre_objs.append(g)

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
            imdbID=movie_data['imdbID'],
        )
        m.Genre.set(genre_objs)
        m.Actors.set(actor_objs)
        #m.Ratings.set(rating_objs)

        for actor in actor_objs:
            actor.movies.add(m)
            actor.save()
        m.save()
        our_db=False
    context={
        'movie_data':movie_data,
        'our_db':our_db,
    }
    template=loader.get_template('MovieDetailsPage.html')
    return HttpResponse(template.render(context,request))

def genres(request,genre_slug):
    genre=get_object_or_404(Genre,slug=genre_slug)
    movie_data=Movie.objects.filter(Genre=genre)
    context={
        'movie_data':movie_data,
    }
    template=loader.get_template('genre.html')
    return HttpResponse(template.render(context,request))

def watchlist(request,imdb_id):
    movie=Movie.objects.get(imdbID=imdb_id)
    user=request.user
    profile=Profile.objects.get(user=user)
    profile.to_watch.add(movie)
    return HttpResponseRedirect(reverse('movie-details',args=[imdb_id]))

def watched_movies(request,imdb_id):
    movie=Movie.objects.get(imdbID=imdb_id)
    user=request.user
    profile=Profile.objects.get(user=user)
    if profile.to_watch.filter(imdbID=imdb_id).exists():
        profile.to_watch.remove(movie)
        profile.watched.add(movie)
    else:
        profile.watched.add(movie)
    return HttpResponseRedirect(reverse('movie-details',args=[imdb_id]))