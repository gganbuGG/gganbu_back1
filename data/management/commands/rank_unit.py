from django.core.management.base import BaseCommand
from data.models import DeckData, Champion
import json

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)

def convert_item(items, unit):

    for item in unit["itemNames"]:
        if item == "TFT_Item_ThiefsGloves" or item == "TFT_Item_EmptyBag" : 
            items.append("TFT_Item_ThiefsGloves")
            break
        if ((item[::-1])[:10])[::-1] == "EmblemItem":
            item = "TFT8_EmblemItems/"+item
        elif ((item[::-1])[:5])[::-1] == "GenAE" :
            item = "TFT8_GenAEItems/"+item
        elif ((item[::-1])[:7])[::-1] == "Radiant" :
            item = "Set5_RadiantItems/"+item
        items.append(item)
    return items

def champ_sta():
    
    decks = DeckData.objects.all().order_by('-updated_time')
    c_time = Champion.objects.all().order_by('-updated_time')
    if not c_time:
        c_time = '2023-02-08 00:00:00'
    else :
        c_time = str(Champion.objects.all().order_by('-updated_time')[0].updated_time)[:19]
    
    c_time = convert_unixtime(c_time)
    for deck in decks:
        if c_time > convert_unixtime(str(deck.updated_time)[:19]): 
            continue
        if deck.placement != 1:
            continue
        units1 = deck.units1
        units2 = deck.units2
        units = units1 + units2
        for unit in units:
            character = unit["character_id"]
            c = Champion.objects.filter(name = character)
            if not c :
                tiers = []
                tiers.append(unit["tier"])
                items = []
                items = convert_item(items, unit)
                c = Champion(name = character, items = items, tier = tiers, rarity = unit["rarity"], fre = 1)
                c.save()
            else :
                c[0].tier.append(unit["tier"])
                c[0].items = convert_item(c[0].items, unit)
                c[0].fre = c[0].fre + 1
                c[0].save()
class Command(BaseCommand):
    help = "챔피언 통계(아이템, tier) - 1등한 소환사 팀에서 자주 등장했던 챔피언의 아이템, 티어 통계"
    def handle(self, *args, **kwargs):
        champ_sta()



        