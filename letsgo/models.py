from __future__ import unicode_literals
import datetime
from django.db import models



# Create your models here.
class Places(models.Model):
    place_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    #rating = models.DoubleField(blank=True, null=True)
    formatted_time=models.IntegerField(null=True, blank=True)
    time = models.DateField(auto_now_add=True)
    herenow = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=250, default='unverified')
    checkins = models.IntegerField(blank=True, null=True)
    #lastday = models.IntegerField(blank=True, null=True)
    #lastweek = models.IntegerField(blank=True, null=True)
    #lastmonth = models.IntegerField(blank=True, null=True)




class Cafe(models.Model):
	time = models.DateField(auto_now_add=True)
	place_id = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	herenow = models.IntegerField(blank=True, null=True)
	checkins = models.IntegerField(blank=True, null=True)



	