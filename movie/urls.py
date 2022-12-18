from .views import landing,login,register,movieDetails

from django.urls import path
from .views import profile


urlpatterns = [
    path('profile/', profile, name='users-profile'),
    #path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('search/', landing, name='search'),
    path('<imdb_id>/',movieDetails,name='movie-details')
]