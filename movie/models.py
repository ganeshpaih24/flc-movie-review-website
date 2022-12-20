from django.db import models
from actor.models import Actor
from django.utils.text import slugify
import requests
from io import BytesIO
from django.core import files
from django.urls import reverse

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
    Actors=models.ManyToManyField(Actor,blank=True)
    Plot=models.CharField(max_length=900,blank=True)
    Language=models.CharField(max_length=300,blank=True)
    Country=models.CharField(max_length=100,blank=True)
    Awards=models.CharField(max_length=250,blank=True)
    Poster=models.ImageField(upload_to='movies',blank=True)
    Poster_url=models.URLField(blank=True)
    imdbID=models.CharField(max_length=100,blank=True)
    Type=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.Title
    
    def save(self,*args,**kwargs):
        if self.Poster=='' and self.Poster_url != '':
            resp=requests.get(self.Poster_url)
            pb=BytesIO()
            pb.write(resp.content)
            pb.flush()
            file_name=self.Poster_url.split("/")[-1]
            self.Poster.save(file_name,files.File(pb),save=False)
        return super().save(*args,**kwargs)








# from django.contrib.auth.models import User


# # Extending User Model Using a One-To-One Link
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()

#     def __str__(self):
#         return self.user.username
