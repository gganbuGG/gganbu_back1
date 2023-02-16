
from django.contrib import admin
from .models import Summoner_rank, Match, DeckData, Champion

admin.site.register(Summoner_rank)
admin.site.register(Match)
admin.site.register(DeckData)
admin.site.register(Champion)