from data.models import Match, DeckData
from django.core.management.base import BaseCommand
from collections import Counter

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)



class Group:

    def __init__(self, units, augments, placement, core):
        self.units = units
        self.augments = augments
        self.placement = placement
        self.core = core

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        """
        매치데이터 하나씩 하면서 그룹으로 덱 - 덱 모델 만들기
        한글로다가
        """
        matchs = Match.objects.all().order_by('-updated_time')
        d_time = DeckData.objects.all().order_by('-updated_time')
        if not d_time:
            d_time = '2023-01-01 00:00:00'
        else :
            d_time = str(DeckData.objects.all().order_by('-updated_time')[0].updated_time)[:19]

        
        d_time = convert_unixtime(d_time)
        for match in matchs:
            if d_time > convert_unixtime(str(match.updated_time)[:19]) :
                continue
            else :
                group1 = []
                group2 = []
                group3 = []
                group4 = []
                for player in match.info["info"]["participants"]:
                    units = []
                    core = []
                    for unit in player["units"]:
                        units.append(unit["character_id"])
                        if len(unit["itemNames"]) == 3:
                            core.append(unit["character_id"])
                    augments = []
                    for augment in player["augments"]:
                        augments.append(augment)

                    placement = player["placement"]
                    if placement == 1 or placement == 2:
                        placement = 1
                    elif placement == 3 or placement == 4:
                        placement = 2
                    elif placement == 5 or placement == 6:
                        placement = 3
                    elif placement == 7 or placement == 8:
                        placement = 4

                    g = Group(units,augments,placement, core)
                    if player["partner_group_id"] == 1:
                        group1.append(g)
                    elif player["partner_group_id"] == 2:
                        group2.append(g)
                    elif player["partner_group_id"] == 3:
                        group3.append(g)
                    elif player["partner_group_id"] == 4:
                        group4.append(g)
            
                DeckData(placement = group1[0].placement, units1 = group1[0].units, coreunits1 = group1[0].core , units2 = group1[1].units, coreunits2 = group1[1].core , augments1 = group1[0].augments, augments2 = group1[1].augments).save()
                DeckData(placement = group2[0].placement, units1 = group2[0].units, coreunits1 = group2[0].core , units2 = group2[1].units, coreunits2 = group2[1].core , augments1 = group2[0].augments, augments2 = group2[1].augments).save()
                DeckData(placement = group3[0].placement, units1 = group3[0].units, coreunits1 = group3[0].core , units2 = group3[1].units, coreunits2 = group3[1].core , augments1 = group3[0].augments, augments2 = group3[1].augments).save()
                DeckData(placement = group4[0].placement, units1 = group4[0].units, coreunits1 = group4[0].core , units2 = group4[1].units, coreunits2 = group4[1].core , augments1 = group4[0].augments, augments2 = group4[1].augments).save()


