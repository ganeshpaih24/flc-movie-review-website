from .views import landing, movieDetails, genres,Rate,watched_movies,watchlist
from django.urls import path


urlpatterns = [
    path('', landing, name='landing'),
    path('search/', landing, name='search'),
    path('movie/<imdb_id>/',movieDetails,name='movie-details'),
    path('movie/genre/<slug:genre_slug>/',genres,name='genres'),
    path('movie/<imdb_id>/watchlist/',watchlist,name='watchlist'),
    path('movie/<imdb_id>/watched_movies/',watched_movies,name='watched_movies'),
    path('movie/genre/<slug:genre_slug>/',genres,name='genres'),
    path('movie/<imdb_id>/rate/', Rate, name='rate-movie'),    
]

