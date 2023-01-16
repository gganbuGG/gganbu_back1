from django.db import models
import datetime

# Create your models here.
class Summoner_rank(models.Model):
    name = models.CharField(max_length=30)
    puuid = models.CharField(max_length=100)
    profileIconId = models.IntegerField(null=True)
    tier = models.CharField(max_length=30, null=True)
    LP = models.CharField(max_length=30, null=True)
    winrate = models.CharField(max_length=30, null=True)
    game_num = models.IntegerField(null=True)
    win = models.IntegerField(null=True)
    lose = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    matchId = models.CharField(max_length=30)
    info = models.JSONField(null=True)

    def __str__(self):
        return self.matchId

class Combinations(models.Model):
    units= models.JSONField(null=True)
    traits = models.JSONField(null=True)
    match = models.ForeignKey("Match",on_delete=models.CASCADE)

class Combinations_partner(models.Model):

    units= models.JSONField(null=True)
    traits = models.JSONField(null=True)
    match = models.ForeignKey("Match",on_delete=models.CASCADE)