from django.db import models

# Create your models here.
class Point(models.Model):
    vid = models.CharField(max_length=20)
    lat = models.FloatField()
    long = models.FloatField()
    #vTitle = models.CharField(max_length=120)
    #vDescription = models.CharField(max_length=5000)
    #saving these for when I'm not too lazy to Regex
    #vYoutubeDate = models.DateTimeField()
    #vHelloDate = models.DateTimeField()
