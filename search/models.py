from django.db import models

class Details(models.Model):
    lat =models.CharField(max_length=200)
    lon =models.CharField(max_length=200)
    dist = models.CharField(max_length=200) 

class FriendObj(models.Model):
    latitutude = models.FloatField(null=True,blank=True,default=None)
    longitude = models.FloatField(null=True,blank=True,default=None)
    user_id=models.IntegerField(default=1)
    name=models.CharField(max_length=200)


    
