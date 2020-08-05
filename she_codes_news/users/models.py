from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    #where you add bios, profile pics, custom features
    pass


    def __str__(self):
        return self.username

        