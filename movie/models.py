from django.db import models
from django.utils.text import slugify
import requests
from io import BytesIO
from django.core import files
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Genre(models.Model):
    title=models.CharField(max_length=25)
    slug=models.SlugField(null=False,unique=True)

    def get_absolute_url(self):
        return reverse('genres', args=[self.slug])

    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.title.replace(" ","")
            self.slug=slugify(self.title)
        return super().save(*args,**kwargs)

class Rating(models.Model):
    source=models.CharField(max_length=50)
    rating=models.CharField(max_length=10)

    def __str__(self):
        return self.source

class Movie(models.Model):
    Title=models.CharField(max_length=200)
    Year=models.CharField(max_length=25,blank=True)
    Rated=models.CharField(max_length=10,blank=True)
    Released=models.CharField(max_length=25,blank=True)
    Runtime=models.CharField(max_length=25,blank=True)
    Genre=models.ManyToManyField(Genre,blank=True)
    Director=models.CharField(max_length=100,blank=True)
    Writer=models.CharField(max_length=300,blank=True)
    Actors=models.CharField(max_length=300,blank=True)
    Plot=models.CharField(max_length=900,blank=True)
    Language=models.CharField(max_length=300,blank=True)
    Country=models.CharField(max_length=100,blank=True)
    Awards=models.CharField(max_length=250,blank=True)
    Poster=CloudinaryField('image')
    Poster_url=models.URLField(blank=True)
    imdbID=models.CharField(max_length=100,blank=True)
    Type=models.CharField(max_length=10,blank=True)
    Ratings = models.ManyToManyField(Rating, blank=True)
    Metascore = models.CharField(max_length=5, blank=True)
    imdbRating = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.Title
    
    def save(self,*args,**kwargs):
        if self.Poster=='' and self.Poster_url != '':
            resp=requests.get(self.Poster_url)
            pb=BytesIO()
            pb.write(resp.content)
            pb.flush()
            file_name=self.Poster_url.split("/")[-1]
            #self.Poster.save(file_name,files.File(pb),save=False)
        return super().save(*args,**kwargs)

RATE_CHOICES = [
    (1, '1- Trash'),
    (2, '2 Terrible'),
    (3, '3 - OK'),
    (4, '4 Good'),
    (5, '5 Perfect'),
]

class Review (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) 
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=300, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return self.user.username