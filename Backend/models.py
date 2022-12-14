from datetime import datetime
from django.db import models

# Create your models here.

class Projects(models.Model):
    projectID = models.AutoField(primary_key=True)
    creatorId = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=10000)
    image = models.CharField(max_length=1000)
    minPrice = models.IntegerField()
    targetPrice = models.IntegerField()
    isFeatured = models.BooleanField()
    total = models.IntegerField()
    donateCount = models.IntegerField()

class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    
class Contribution(models.Model):
    contributionID = models.AutoField(primary_key=True)  
    userID = models.CharField(max_length=20)
    projectID = models.CharField(max_length=20)
    amount = models.IntegerField()
