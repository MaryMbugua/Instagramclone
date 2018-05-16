from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class comments(models.Model):
    content = models.CharField(max_length=60)
    editor = models.ForeignKey(User)
class Photo(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=True)
    caption = models.CharField(max_length=70,blank=True)
    person = models.ForeignKey(User)
   

class Profile(models.Model):
    person = models.ForeignKey(User)
    user_name = models.CharField(max_length=60)
    bio = HTMLField()
    profile_pic = models.ImageField(upload_to = 'images/',blank=True)
    @classmethod
    def search_by_user_name(cls,search_term):
        profiles = cls.objects.filter(user_name__icontains=search_term)
        return profiles
   
    def __str__(self):
        return self.bio