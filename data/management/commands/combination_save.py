from django.core.management.base import BaseCommand
from data.models import Match,Combinations_partner,Combinations

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)
class Command(BaseCommand):
    help = "1등한 소환사들의 덱정보 저장"
    def handle(self, *args, **kwargs):
        matchs = Match.objects.all().order_by('-updated_time')
        c_time = Combinations.objects.all().order_by('-updated_time')
        if not c_time:
            c_time = '2023-01-01 00:00:00'
        else :
            c_time = str(Combinations.objects.all().order_by('-updated_time')[0].updated_time)[:19]

        
        c_time = convert_unixtime(c_time)
        for match in matchs:
            if c_time > convert_unixtime(str(match.updated_time)[:19]) :
                continue
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