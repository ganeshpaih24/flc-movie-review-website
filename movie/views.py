from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import requests

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

def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')


def search(request):
    return render(request,'search.html')
