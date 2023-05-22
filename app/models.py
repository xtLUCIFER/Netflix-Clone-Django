from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class CustomUser(AbstractUser): 
    profile = models.ManyToManyField('Profile',blank=True)


    
    
AGE_CHOICES = (
    ('All','All'),
    ('Kids','Kids')
)
MOVIE_CHOICES = (
    ('seasonal','Seasonal'),
    ('Single','Single')
)
class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)
    

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    name = models.CharField(max_length=255)
    discription = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    video = models.ManyToManyField('Video')
    flyer= models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10,choices=AGE_CHOICES)


    def __str__(self):
        return self.name
    


class Video(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title
    