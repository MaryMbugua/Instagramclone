from django.db import models
import datetime as dt 
from django.contrib.auth.models import User

# Create your models here.
class comments(models.Model):
    content = models.CharField(max_length=60)
    editor = models.ForeignKey(User)
class Photo(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=True)
   

