from django.db import models

# Create your models here.
class Summoner_rank(models.Model):
    name = models.CharField(max_length=30)
    puuid = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Match(models.Model):
    matchId = models.CharField(max_length=30)
    info = models.JSONField(null=True)

    def __str__(self):
        return self.matchId