from django.db import models
import datetime as dt 

# Create your models here.
class Photo(models.Model):
    baseurl = models.CharField(max_length=20)
    url = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=20)
    likes = models.IntegerField()
    caption = models.CharField(max_length=140,default="")
    tags = models.IntegerField(default=0)
    main_colour = models.CharField(max_length=15,default="")
    # article_image = models.ImageField(upload_to = 'articles/',blank=True)