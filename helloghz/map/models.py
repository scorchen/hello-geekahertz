from django.db import models

# Create your models here.
class Point(models.Model):
    vid = models.CharField(max_length=20)
    lat = models.FloatField()
    long = models.FloatField()
