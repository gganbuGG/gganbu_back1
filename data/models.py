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

class Deck(Update):
    winrate = models.FloatField(max_length=30, null=True)
    windefencerate = models.FloatField(max_length=30, null=True)
    avgplace = models.FloatField(max_length=30, null=True)
    units = models.JSONField(null=True)
    core = models.JSONField(null=True)
    augments = models.JSONField(null=True)
    traits = models.JSONField(null=True)
    h_aug = models.CharField(max_length=30, null = True)

class StandardDeck(Update):
    units = models.JSONField(null=True)
    fre = models.IntegerField(null=True)

class PartnerDeck(Update):
    #파트너 덱은 1. 니부모가 뭐냐, 몇등이었냐, 전체 몇번나왔냐, 유닛은 뭐썼냐
    stand  = models.ForeignKey(StandardDeck, on_delete=models.CASCADE)
    placement = models.IntegerField(null=True)
    units = models.JSONField(null=True)

class Synergy(Update):
    stand = models.ForeignKey(StandardDeck, on_delete=models.CASCADE)
    winrate = models.FloatField(max_length=30, null=True)
    windefencerate = models.FloatField(max_length=30, null=True)
    avgplace = models.FloatField(max_length=30, null=True)
    units = models.JSONField(null=True)