from django.core.management.base import BaseCommand
from data.models import Combinations_partner,Combinations, Champion
from collections import Counter

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)

class Command(BaseCommand):
    help = "챔피언 통계(아이템, tier) - 1등한 소환사 팀에서 자주 등장했던 챔피언의 아이템, 티어 통계"
    def handle(self, *args, **kwargs):
        combinations = Combinations.objects.all().order_by('-updated_time')
        c_time = Champion.objects.all().order_by('-updated_time')
        
        if not c_time:
            c_time = '2023-01-01 00:00:00'
        else :
            c_time = str(Combinations.objects.all().order_by('-updated_time')[0].updated_time)[:19]
        
        c_time = convert_unixtime(c_time)
        for combination in combinations:
            if c_time > convert_unixtime(str(combination.updated_time)[:19]): 
                continue
            units = combination.units
            for unit in units:
                c = Champion.objects.filter(name = unit["character_id"])
                if not c :
                    tiers = []
                    tiers.append(unit["tier"])
                    c = Champion(name = unit["character_id"], items = unit["itemNames"], tier = tiers, rarity = unit["rarity"])
                    c.save()
                else :
                    items = []
                    items = c[0].items
                    tiers = c[0].tier
                    c.delete()
                    for item in unit["itemNames"]:
                        items.append(item)
                    tiers.append(unit["tier"])
                    c = Champion(name = unit["character_id"],items = items, tier = tiers, rarity = unit["rarity"])
                    c.save()

        combinations_partner = Combinations_partner.objects.all().order_by('-updated_time')
        for combination in combinations_partner:
            if c_time > convert_unixtime(str(combination.updated_time)[:19]): 
                continue
            units = combination.units
            for unit in units:
                c = Champion.objects.filter(name = unit["character_id"])
                if not c :
                    tiers = []
                    tiers.append(unit["tier"])
                    c = Champion(name = unit["character_id"], items = unit["itemNames"], tier = tiers, rarity = unit["rarity"])
                    c.save()
                else :
                    items = []
                    items = c[0].items
                    tiers = c[0].tier
                    c.delete()
                    for item in unit["itemNames"]:
                        items.append(item)
                    tiers.append(unit["tier"])
                    c = Champion(name = unit["character_id"],items = items, tier = tiers, rarity = unit["rarity"])
                    c.save()



        