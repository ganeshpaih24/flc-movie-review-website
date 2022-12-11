from .views import landing,login,register,search
from django.urls import path

urlpatterns = [
    path('', landing, name='landing'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('search/', landing, name='search'),
]