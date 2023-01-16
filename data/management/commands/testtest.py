from django.core.management.base import BaseCommand
from data.models import Combinations_partner,Combinations, Champion
from collections import Counter
import datetime

class Command(BaseCommand):
    help = "Update 100 Ranker Data in the database to new Ranker Data."
    def handle(self, *args, **kwargs):

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