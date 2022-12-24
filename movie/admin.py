from django.contrib import admin
from .models import Movie,Genre, Review#, Profile

# admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review)