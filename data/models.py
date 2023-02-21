from django.db import models

# Create your models here.
class Update(models.Model):
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Summoner_rank(Update):
    name = models.CharField(max_length=30)
    puuid = models.CharField(max_length=100)
    profileIconID = models.IntegerField(null=True)
    tier = models.CharField(max_length=30, null=True)
    LP = models.CharField(max_length=30, null=True)
    winrate = models.CharField(max_length=30, null=True)
    game_num = models.IntegerField(null=True)
    win = models.IntegerField(null=True)
    lose = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Match(Update):
    matchId = models.CharField(max_length=30)
    info = models.JSONField(null=True)

    def __str__(self):
        return self.matchId


class Champion(Update):
    name = models.CharField(max_length=30)
    items = models.JSONField(null=True)
    tier = models.JSONField(null=True)
    rarity = models.IntegerField(null=True)
    fre = models.IntegerField(null=True)

class DeckData(Update):
    placement = models.IntegerField(null=True)
    units1 = models.JSONField(null=True)
    coreunits1 = models.JSONField(null=True)
    units2 = models.JSONField(null=True)
    coreunits2 = models.JSONField(null=True)
    augments1= models.JSONField(null=True)
    augments2= models.JSONField(null=True)
    H_aug1 = models.CharField(max_length=30, null = True)
    H_aug2 = models.CharField(max_length=30, null = True)
class StandardDeck(Update):
    name = models.CharField(max_length=30, null = True)
    units = models.JSONField(null=True)
    coreunits = models.JSONField(null=True)
    augments= models.JSONField(null=True)
    H_aug = models.JSONField(null=True)
    fre = models.IntegerField(null=True)
    placement = models.JSONField(null=True)
    winrate = models.FloatField(null = True)
    windefencerate = models.FloatField(null = True)
    avgplace = models.FloatField(null = True)
    score = models.IntegerField(null=True)