from django.core.management.base import BaseCommand
from data.models import Combinations_partner,Combinations, Champion
from collections import Counter
import datetime

class Command(BaseCommand):
    help = "챔피언 통계(아이템, tier) - 1등한 소환사 팀에서 자주 등장했던 챔피언의 아이템, 티어 통계"
    def handle(self, *args, **kwargs):
        combinations = Combinations.objects.all()
        for combination in combinations:
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

        combinations_partner = Combinations_partner.objects.all()
        for combination in combinations_partner:
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


        champions = Champion.objects.all()
        rank_unit = dict()
        rank_unit_item = dict()
        rank_unit_tier = dict()

        for champion in champions:
            rank_unit[champion.name] = len(champion.tier)
            unit_items = champion.items
            unit_items = Counter(unit_items).most_common(3)
            rank_unit_item[champion.name] = unit_items
            unit_tiers = champion.tier
            unit_tiers = Counter(unit_tiers).most_common(1)
            rank_unit_tier[champion.name] = unit_tiers

        print(rank_unit)
        print(rank_unit_item)
        print(rank_unit_tier)
    
        update_time = datetime.datetime.now()
        print(update_time)

        