from django.db import models

# Create your models here.
class Update(models.Model):
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Summoner_rank(Update):
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

class Match(Update):
    matchId = models.CharField(max_length=30)
    info = models.JSONField(null=True)

    def __str__(self):
        return self.matchId

class Combinations(Update):
    units= models.JSONField(null=True)
    traits = models.JSONField(null=True)
    match = models.ForeignKey("Match",on_delete=models.CASCADE)

class Combinations_partner(Update):

    units= models.JSONField(null=True)
    traits = models.JSONField(null=True)
    match = models.ForeignKey("Match",on_delete=models.CASCADE)

class Champion(Update):
    name = models.CharField(max_length=30)
    items = models.JSONField(null=True)
    tier = models.JSONField(null=True)
    rarity = models.IntegerField(null=True)

class DeckData(Update):
    placement = models.IntegerField(null=True)
    units1 = models.JSONField(null=True)
    units2 = models.JSONField(null=True)
    augments1= models.JSONField(null=True)
    augments2= models.JSONField(null=True)

class Deck(Update):
    win_rate = models.CharField(max_length=30, null=True)
    windefense_rate = models.CharField(max_length=30, null=True)
    place_avg = models.CharField(max_length=30, null=True)
    game_rate = models.CharField(max_length=30, null=True)

