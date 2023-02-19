from data.models import DeckData, Deck, StandardDeck
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
                A.append([i,j])
    A.sort()
    return A

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        help = "더블 덱 "
        """
        뷰티풀 스프로 롤체지지에 있는 덱(챔피언 으로)들 가져와서
        거기서 덱 배열을 만든다
        그게 기준값이고 데이터에서 유닛들 배열을 하나만빼서 같은지 혹은 기준값에서 하나만 빼서 같은지 파악하기 (이때 정렬해놓아서 비교해라)
        같으면 기준값 카운트 +
        거기서 데이터좀 보자고
        """
        #뷰티풀 스프로 롤체지지에 있는 덱(챔피언 으로)들 가져와서
        
        
        stdDeck = StandardDeck.objects.all().order_by('-updated_time')
        stdDeck.delete()
        standard = getSite()
        for sta in standard:
            sd = StandardDeck(units = sta, fre = 0)
            sd.save()
        
        #기준이랑 비교해서 모델에 저장
        for comb in compareDeck(standard):
            deck = StandardDeck.objects.filter(units = comb[0])
            if not deck:
                print("기준덱에서 찾지 못하는 에러")
                return KeyError
            else:
                deck = deck[0]
                deck.fre += 1
                temp = []
                if deck.partner:
                    for i in deck.partner:
                        temp.append(i)
                p = StandardDeck.objects.filter(units = comb[1])
                if not p:
                    print("기준덱에서 찾지 못하는 에러")
                    return KeyError
                else:
                    p = p[0]
                    temp.append(p.units)
                    deck.partner = temp
                deck.save()
        
        #모델에 저장한 파트너 배열을 모델에서 찾아서 partner필드에 쿼리id저장
        a = StandardDeck.objects.all().order_by('-updated_time')
        for i in a:
            temp = []
            for t in i.partner:
                temp.append(str(t))

            c = Counter(temp).most_common(3)
            d = []
            for p in c:
                t = p[0].lstrip("['").rstrip("']").split("', '")
                d.append(StandardDeck.objects.filter(units = t)[0].id)
            i.partner = d
            i.save()
