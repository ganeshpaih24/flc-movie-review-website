from .views import landing,login,register,movieDetails,genres,userinfo

from django.urls import path
from .views import profile


urlpatterns = [
    path('profile/', profile, name='users-profile'),
    #path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('search/', landing, name='search'),
    path('<imdb_id>/',movieDetails,name='movie-details'),
    path('genre/<slug:genre_slug>/',genres,name='genres'),
    path('userinfo/',userinfo, name='userinfo')

]