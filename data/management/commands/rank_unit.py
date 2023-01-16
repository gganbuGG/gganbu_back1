from django.core.management.base import BaseCommand
from data.models import Combinations_partner,Combinations
from collections import Counter
import datetime

class Command(BaseCommand):
    help = "챔피언 통계"
    def handle(self, *args, **kwargs):
        unit_count = []
        combinations = Combinations.objects.all()
        for combination in combinations:
            units = combination.units
            for unit in units:
                unit_count.append(unit["character_id"])

        combinations_partner = Combinations_partner.objects.all()
        for combination in combinations_partner:
            units = combination.units
            for unit in units:
                unit_count.append(unit["character_id"])

        rank = Counter(unit_count).most_common()
        
        for champ in rank:
            print(champ[0] + " : "+ str(champ[1]))
    
        update_time = datetime.datetime.now()
        print(update_time)