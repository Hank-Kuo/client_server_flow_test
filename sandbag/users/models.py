from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #username = models.CharField(max_length=30, unique=False)
    token = models.CharField(max_length=128,unique=True)
    def __str__(self):
        return self.username 

class Token(models.Model):
    token = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)
    username = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.token
