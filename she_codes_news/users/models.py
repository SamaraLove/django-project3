from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    #where you add bios, profile pics, custom features
    # 
    # name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    pass
    # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html


    def __str__(self):
        return self.username

