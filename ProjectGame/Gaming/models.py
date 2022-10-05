from django.db import models


# Create your models here.
class Game(models.Model):
    GameID = models.IntegerField()
    GameName = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    BuildYear = models.IntegerField()
    Downloads = models.IntegerField()
    ActivePlayers = models.IntegerField()
    Size = models.FloatField()
    Creater = models.CharField(max_length=200)
    Version = models.CharField(max_length=200)
    DevicesAvailable = models.CharField(max_length=100, choices=(("Android", "Android"), ("iOS", "iOS"), ("PC", "PC"), ("PlayStation", "PlayStation"), ("Xbox", "Xbox")), default='Android')

class Leadership(models.Model):
    PlayerID = models.IntegerField()
    Rank = models.IntegerField()
    Score = models.IntegerField()
    GameID = models.IntegerField()
    Achievements =  models.CharField(max_length=100,choices=(("Main","Main"), ("InGame","InGame"), ("Friendship","Friendship")), default='Main')
    SessionNumber = models.IntegerField()

class News(models.Model):
    NewsID = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Likes = models.IntegerField()
    Comments =  models.CharField(max_length=100,choices=(("Main","Main"), ("InGame","InGame"), ("Friendship","Friendship")), default='Main')# Change
    Category =  models.CharField(max_length=100,choices=(("Main","Main"), ("InGame","InGame"), ("Friendship","Friendship")), default='Main')# Change

class Players(models.Model):
    PlayerID = models.IntegerField()
    PlayerName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    SignupDate = models.DateTimeField()
    LastLogin = models.DateTimeField()

class Status(models.Model):
    PlayerID = models.IntegerField()
    Active = models.BooleanField()
    GamesPlayed = models.CharField(max_length=100,choices=(("Main","Main"), ("InGame","InGame"), ("Friendship","Friendship")), default='Main')# Change
    HourPlayed = models.FloatField()
    Warnings = models.IntegerField()
    Banned = models.BooleanField()

class Update(models.Model):
    GameID = models.IntegerField()
    UpdateAvailable = models.BooleanField()
    LastUpdate = models.DateTimeField()
    UpdateSize = models.FloatField()
    UpdatedBy = models.CharField(max_length=100)
    UpdatePending = models.BooleanField()
