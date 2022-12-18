from django.urls import path
from .views import profile

urlpatterns = [
    # Add this
    path('profile/', profile, name='users-profile'),
]