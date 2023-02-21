from data.models import DeckData, Deck, StandardDeck, PartnerDeck, Synergy
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent.parent

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)

def compose():
    deckDatas = DeckData.objects.all().order_by('-updated_time')
    d_time = Deck.objects.all().order_by('-updated_time')
    
    if not d_time:
        d_time = '2023-01-01 00:00:00'
    else :
        d_time = str(DeckData.objects.all().order_by('-updated_time')[0].updated_time)[:19]
    
    d_time = convert_unixtime(d_time)

    combs = []
    for deckdata in deckDatas:
        if d_time > convert_unixtime(str(deckdata.updated_time)[:19]):
            continue
        else :
            pass

def getSite():
    url = 'https://lolchess.gg/meta?hl=en-US'

    response = requests.get(url)
    #wrapper > div.container-full > div.guide-meta.mt-4 > div.guide-meta__group.tier-S > div.guide-meta__group__content
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.select('#wrapper > div.container-full > div.guide-meta.mt-4 > div.guide-meta__group.tier-S > div.guide-meta__group__content > div.guide-meta__deck-box')
        
        lst = []
        for deck in tbody:
            sublst = []
            tr = deck.select('div.guide-meta__deck-box > div > div.guide-meta__deck__column.champions.mr-2 > div.tft-champion-box')
            for c in tr:
                unit = c.select_one('div > span.name').get_text()
                if unit == "Kai'Sa":
                    unit = "Kaisa"
                elif unit == "Cho'Gath":
                    unit = 'Chogath'
                elif unit == "Lee Sin":
                    unit = 'LeeSin'
                elif unit == "LeBlanc":
                    unit = 'Leblanc'
                elif unit == "Aurelion Sol":
                    unit = 'AurelionSol'
                elif unit == "Wukong":
                    unit = "WuKong"
                sublst.append("TFT8_"+unit)
            lst.append(sublst)
        return lst
    else :
        return response.status_code

def isDeck(standard, tdata):
    data = []

    for i in tdata:
        data.append(i["character_id"])

    if len(standard) == len(data):
        if sorted(standard) == sorted(data):
            return [True, standard]
    else:
        complement = list(set(data) - set(standard))
        if len(complement) <= 1:
            return [True, standard]
        else:
            return [False, None]


class Win:
    def __init__(self, placement, units1, units2):
        self.placement = placement
        self.units1 = units1
        self.units2 = units2

def compareDeck(lst):

    def addDeck(standard, lst):
        # 기준에 맞는 놈 찾기
        temp = []
        for stand in standard:
            res = isDeck(stand, lst)
            if res != None and res[0]:
                temp.append(res[1])

        return temp
    deckdatas = DeckData.objects.all().order_by('-updated_time')

    A = []
    
    for deckdata in deckdatas:
        for i in addDeck(lst, deckdata.units1):
            for j in addDeck(lst, deckdata.units2):
                s = [i ,j]
                s.sort()
                w = Win(deckdata.placement, s[0] ,s[1])
                A.append(w)
    return A


def makeDeck(syn):
    t = []
    for s in syn:
        t.append(str(s))
    c = Counter(t).most_common()
    temp = []
    for p in c:
        if p[1] >= 10:
            temp.append(p[0].lstrip("['").rstrip("']").split("', '"))
    return temp
class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        help = "더블 덱 "
        
        
        #뷰티풀 스프로 롤체지지에 있는 덱(챔피언 으로)들 가져와서
        
        
        stdDeck = StandardDeck.objects.all().order_by('-updated_time')
        stdDeck.delete()
        standard = getSite()
        for sta in standard:
            sd = StandardDeck(units = sta, fre = 0)
            sd.save()
        
        pDeck = PartnerDeck.objects.all()
        pDeck.delete()
        #기준이랑 비교해서 모델에 저장
        for comb in compareDeck(standard):
            deck = StandardDeck.objects.filter(units = comb.units1)
            if not deck:
                print("기준덱에서 찾지 못하는 에러")
                return KeyError
            else:
                deck = deck[0]
                deck.fre += 1
                p = StandardDeck.objects.filter(units = comb.units2)
                if not p:
                    print("기준덱에서 찾지 못하는 에러")
                    return KeyError
                else:
                    p = p[0]
                    p.fre += 1
                    p.save()

                    #파트너 덱은 1. 니부모가 뭐냐, 몇등이었냐, 전체 몇번나왔냐, 유닛은 뭐썼냐
                    pd = PartnerDeck(stand = deck, placement = comb.placement, units = p.units)
                    pd.save()
                deck.save()
        """
        #모델에 저장한 파트너 배열을 모델에서 찾아서 

        """
        sy = Synergy.objects.all()
        sy.delete()
        for man in StandardDeck.objects.all().order_by('-updated_time'):
            syn = []
            for woman in PartnerDeck.objects.filter(stand = man.id):
                syn.append(woman.units)
            decks = makeDeck(syn)
            for deck in decks:
                win = 0
                winde = 0
                avg = 0
                data = PartnerDeck.objects.filter(units = deck, stand = man.id)
                all = len(data)
                for d in data:
                    if d.placement == 1:
                        win += 1
                    if d.placement <= 2:
                        winde+=1
                    avg += d.placement
                s = Synergy(stand = man, winrate = round((win/all)*100, 1), windefencerate = round((winde/all)*100, 1), avgplace = round(avg/all, 1), units = deck)
                s.save()

        