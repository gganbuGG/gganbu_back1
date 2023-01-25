from rest_framework import serializers
from .models import Summoner_rank, Champion
from collections import Counter

class SummonerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Summoner_rank
        fields = ('name', 'profileIconId', 'tier', 'LP', 'winrate', 'game_num', 'win', 'lose' )


class ChampionSerializer(serializers.ModelSerializer) :
    items = serializers.SerializerMethodField('get3items')
    tier = serializers.SerializerMethodField('getmosttier')
    how_many = serializers.SerializerMethodField('gethow')

    class Meta :
        model = Champion
        fields = ('name', 'items', 'rarity', 'tier', 'how_many')
    
    def get3items(self, obj):
        items = []
        for name in Counter(obj.items).most_common(3):
            items.append(name[0])
        return items
    
    def getmosttier(self, obj):
        return Counter(obj.tier).most_common(1)[0][0]

    def gethow(self, obj):
        return len(obj.tier)
