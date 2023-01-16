from django.core.management.base import BaseCommand
from data.models import Match,Combinations_partner,Combinations
import datetime
class Command(BaseCommand):
    help = "1등한 소환사들의 덱정보 저장"
    def handle(self, *args, **kwargs):
        matchs = Match.objects.all()

        for match in matchs:
            participants = match.info["info"]["participants"]
            for participant in participants:
                if participant["placement"] == 1 :
                    traits = participant["traits"]
                    trait_active1 = []
                    for trait in traits:
                        if trait["tier_current"] > 0:
                            trait_active1.append(trait)
        
                    units = participant["units"]
                    c = Combinations(units = units, traits = trait_active1, match = match)
                    c.save()

                elif participant["placement"] == 2 :
                    traits = participant["traits"]
                    trait_active2 = []
                    for trait in traits:
                        if trait["tier_current"] > 0:
                            trait_active2.append(trait)
        
                    units = participant["units"]
                    c = Combinations_partner(units = units, traits = trait_active2, match = match)
                    c.save()


        update_time = datetime.datetime.now()
        print(update_time)
