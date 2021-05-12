from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.TextField()
   
   

class Friends(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField()
    body = models.TextField()

class Team(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    MBTI = models.CharField(max_length=50)
    Food = models.CharField(max_length=50)
    hobby = models.CharField(max_length=50)
    
