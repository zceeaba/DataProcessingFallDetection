from django.db import models

# Create your models here.
"""
class Wearable(models.Model):
    id = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30)

class Instances(models.Model):
    timevalue=models.FloatField(default=0)
    acceleration_x=models.FloatField(default=0)
    acceleration_y=models.FloatField(default=0)
    acceleration_z=models.FloatField(default=0)
"""
class Video(models.Model):
    videoid=models.CharField(max_length=200)
    uid=models.CharField(max_length=200)
    date=models.CharField(max_length=200)

class attributes(models.Model):
    type=models.CharField(max_length=200)
    value=models.CharField(max_length=10000)
    video=models.ForeignKey(Video)
