from data.models import DeckData,StandardDeck, DoubleDeck
from django.core.management.base import BaseCommand
from collections import Counter
from pathlib import Path
import requests

BASE_DIR = Path(__file__).resolve().parent.parent

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)

def korean(name, how):
    champ = {
    "TFT8_Kaisa" : 
    {
        "name" : "카이사",
        "traits" : ["Set8_Recon","Set8_StarGuardian"]
    },
    "TFT8_Lux" : 
    {
        "name" : "럭스",
        "traits" : ["Set8_Channeler","Set8_StarGuardian"]
    },
    "TFT8_Kayle" : {
        "name" : "케일",
        "traits" : ["Set8_UndergroundThe", "Set8_Duelist"]
    },
    "TFT8_Poppy" : {
        "name" : "뽀삐",
        "traits" : ["Set8_GenAE","Set8_GenAE"]
    },
    "TFT8_Galio" : {
        "name" : "갈리오",
        "traits" : ["Set8_Civilian", "Set8_Mascot"]
    },
    "TFT8_Rell" : {
        "name" : "렐",
        "traits" : ["Set8_StarGuardian","Set8_GenAE"]
    },
    "TFT8_Velkoz" : {
        "name" : "벨코즈",
        "traits" : ["Set8_Threat"]
    },
    "TFT8_Nilah" : {
        "name": "닐라",
        "traits" : ["Set8_StarGuardian", "Set8_Duelist"]
    },
    "TFT8_Ashe" : {
        "name":"애쉬",
        "traits" : ["Set8_Recon", "Set8_SpaceCorps"]
    },
    "TFT8_Yasuo" : {
        "name":"야스오",
        "traits" : ["Set8_SpaceCorps", "Set8_Duelist"]
    },
    "TFT8_Senna" : {
        "name":"세나",
        "traits" : ["Set8_SpaceCorps", "Set8_Deadeye"]
    },
    "TFT8_Zed" : {
        "name":"제드",
        "traits" : ["Set8_Duelist", "Set8_SpaceCorps", "Set8_Hacker"]
    },
    "TFT8_Lulu" : {
        "name":"룰루",
        "traits" : ["Set8_Heart", "Set8_GenAE"]
    },
    "TFT8_Nunu" : {
        "name":"누누",
        "traits" : ["Set8_Mascot", "Set8_GenAE"]
    },
    "TFT8_Yuumi" : {
        "name":"유미",
        "traits" : ["Set8_StarGuardian", "Set8_Heart","Set8_Mascot"]
    },
    "TFT8_Zoe" : {
        "name":"조이",
        "traits" : ["Set8_GenAE","Set8_Prankster","Set8_Hacker"]
    },
    "TFT8_Taliyah" : {
        "name":"탈리야",
        "traits" : ["Set8_StarGuardian", "Set8_Channeler"]
    },
    "TFT8_Sivir" : {
        "name":"시비르",
        "traits" : ["Set8_Civilian", "Set8_Deadeye"]
    },
    "TFT8_Gangplank" : {
        "name":"갱플랭크",
        "traits" : ["Set8_Duelist","Set8_Supers"]
    },
    "TFT8_WuKong" : {
        "name":"오공",  
        "traits" : ["Set8_ExoPrime", "Set8_GenAE"]
    },
    "TFT8_Draven" : {
        "name":"드레이븐",
        "traits" : ["Set8_ExoPrime", "Set8_Ace"]
    },
    "TFT8_Malphite" : {
        "name":"말파이트",
        "traits" : ["Set8_Supers","Set8_Mascot"]
    },
    "TFT8_Nasus" : {
        "name":"나서스",
        "traits" : ["Set8_Mascot","Set8_AnimaSquad"]
    },
    "TFT8_Jinx" : {
        "name":"징크스",
        "traits" : ["Set8_AnimaSquad","Set8_Prankster"]
    },
    "TFT8_Vayne" : {
        "name":"베인",
        "traits" : ["Set8_AnimaSquad","Set8_Recon","Set8_Duelist"]
    },
    "TFT8_MissFortune" : {
        "name":"미스포츈",
        "traits" : ["Set8_Ace","Set8_AnimaSquad"]
    },
    "TFT8_Chogath" : {
        "name":"초가스",
        "traits" : ["Set8_Threat"]
    },
    "TFT8_Rammus" : {
        "name":"람머스",
        "traits" : ["Set8_Threat"]
    },
    "TFT8_BelVeth" : {
        "name":"벨베스",
        "traits" : ["Set8_Threat"]
    },
    "TFT8_AurelionSol" : {
        "name":"아우렐리온솔",
        "traits" : ["Set8_Threat"]
    },
    "TFT8_Zac" : {
        "name":"자크",
        "traits" : ["Set8_Threat"]
    },
    "TFT8_Mordekaiser" : {
        "name":"모데카이저",
        "traits" : ["Set8_Ace", "Set8_SpaceCorps"]
    },
    "TFT8_Leblanc" : {
        "name":"르블랑",
        "traits" : ["Set8_Admin", "Set8_Hacker","Set8_Channeler"]
    },
    "TFT8_Sylas" : {
        "name":"사일러스",
        "traits" : ["Set8_AnimaSquad", "Set8_Renegade"]
    },
    "TFT8_Camille" : {
        "name":"카밀",
        "traits" : ["Set8_Admin","Set8_Renegade"]
    },
    "TFT8_Ezreal" : {
        "name":"이즈리얼",
        "traits" : ["Set8_UndergroundThe","Set8_Recon"]
    },
    "TFT8_Sona" : {
        "name":"소나",
        "traits" : ["Set8_UndergroundThe", "Set8_Heart", "Set8_Channeler"]
    },
    "TFT8_Ekko" : {
        "name":"에코",
        "traits" : ["Set8_StarGuardian", "Set8_Aegis","Set8_Prankster"]
    },
    "TFT8_Sett" : {
        "name":"세트",
        "traits" : ["Set8_ExoPrime", "Set8_GenAE"]
    },
    "TFT8_Janna" : {
        "name":"잔나",
        "traits" : ["Set8_Civilian","Set8_Forecaster","Set8_Channeler"]
    },
    "TFT8_Urgot" : {
        "name":"우르곳",
        "traits" : ["Set8_Threat"]
    },
    "TFT8_Syndra" : {
        "name":"신드라",
        "traits" : ["Set8_Heart","Set8_StarGuardian"]
    },
    "TFT8_Fiddlesticks" : {
        "name":"피들스틱",
        "traits" : ["Set8_Threat","Set8_Corrupted"]
    },
    "TFT8_Blitzcrank" : {
        "name":"블리츠크랭크",
        "traits" : ["Set8_Admin", "Set8_Brawler"]
    },
    "TFT8_Renekton" : {
        "name":"레넥톤",
        "traits" : ["Set8_Brawler","Set8_SpaceCorps"]
    },
    "TFT8_Vi" : {
        "name":"바이",
        "traits" : ["Set8_Brawler", "Set8_Aegis","Set8_UndergroundThe"]
    },
    "TFT8_LeeSin" : {
        "name":"리신",
        "traits" : ["Set8_Heart","Set8_Brawler"]
    },
    "TFT8_Riven" : {
        "name":"리븐",
        "traits" : ["Set8_AnimaSquad", "Set8_Brawler", "Set8_GenAE"]
    },
    "TFT8_Jax" : {
        "name":"잭스",
        "traits" : ["Set8_ExoPrime", "Set8_Brawler"]
    },
    "TFT8_Sejuani" : {
        "name":"세주아니",
        "traits" : ["Set8_Brawler", "Set8_SpaceCorps"]
    },
    "TFT8_Soraka" : {
        "name":"소라카",
        "traits" : ["Set8_Admin", "Set8_Heart"]
    },
    "TFT8_Talon" : {
        "name":"탈론",
        "traits" : ["Set8_OxForce", "Set8_Renegade"]
    },
    "TFT8_Fiora" : {
        "name":"피오라",
        "traits" : ["Set8_OxForce", "Set8_Duelist"]
    },
    "TFT8_Annie" : {
        "name":"애니",
        "traits" : ["Set8_OxForce", "Set8_GenAE", "Set8_Channeler"]
    },
    "TFT8_Alistar" : {
        "name":"알리스타",
        "traits" : ["Set8_OxForce", "Set8_Mascot", "Set8_Aegis"]
    },
    "TFT8_Viego" : {
        "name":"비에고",
        "traits" : ["Set8_OxForce", "Set8_Renegade"]
    },
    "TFT8_Samira" : {
        "name":"사미라",
        "traits" : ["Set8_Ace", "Set8_UndergroundThe","Set8_Deadeye"]
    },
    "TFT8_Aphelios" : {
        "name":"아펠리오스",
        "traits" : ["Set8_OxForce", "Set8_Deadeye", "Set8_Arsenal"]
    },
    "TFT8_Leona" : {
        "name":"레오나",
        "traits" : ["Set8_ExoPrime", "Set8_Renegade", "Set8_Aegis"]
    },
    }

    if how == "name":
        return champ[name]["name"]
    elif how == "traits":
        return champ[name]["traits"]

def getSite():
    #영문 사이트 크롤링
    url = 'https://lolchess.gg/meta?hl=en-US'

    response = requests.get(url)
    #크롤링
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.select('#wrapper > div.container-full > div.guide-meta.mt-4 > div.guide-meta__group.tier-S > div.guide-meta__group__content > div.guide-meta__deck-box')
        
        lst = []
        #덱 마다 살펴보기
        idx = 0
        for deck in tbody:
            sublst = [] # 유닛 목록 저장
            cores = [] # 코어챔피언 목록 저장
            score = 0 #가중치 기준 저장
            tr = deck.select('div.guide-meta__deck-box > div > div.guide-meta__deck__column.champions.mr-2 > div.tft-champion-box')

            url = 'https://lolchess.gg/meta?hl=ko-KR'

            response = requests.get(url)
                #크롤링
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                tbody = soup.select('#wrapper > div.container-full > div.guide-meta.mt-4 > div.guide-meta__group.tier-S > div.guide-meta__group__content > div.guide-meta__deck-box')
                
                deck = tbody[idx]
                try:
                    name = deck.select_one('div.guide-meta__deck__column.name.mr-3 > span')
                    name.decompose()
                    name = deck.select_one('div.guide-meta__deck__column.name.mr-3').get_text().strip()
                except AttributeError:
                    name = deck.select_one('div.guide-meta__deck__column.name.mr-3').get_text().strip()
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

                score += 20

                #아이템 개수 저장
                items_len = len(c.select("div.tft-items > img"))
                if items_len >= 1:
                    cores.append(["TFT8_"+unit, items_len])
                    score += 10 * items_len
                
                sublst.append("TFT8_"+unit)

            s = StandardDeck(name = name, units = sublst, coreunits = cores, fre = 0, score = score)
            s.save()
            idx+=1

def compareStandard():

    standard = StandardDeck.objects.all()
    deckdata = DeckData.objects.all()

    #저장된 덱이 어느 덱에 속하는지 판별하고 등수, 증강체 저장
    for deck in deckdata:

        #units1 검사
        for stand in standard:
            score = 0
            for unit in deck.units1:
                cores = stand.coreunits
                Sunits = stand.units
                if unit["character_id"] in Sunits:
                    score += 20
                    for core in cores:
                        if unit["character_id"] == core[0]:
                            score += 10* core[1]

            #점수가 75%이상 이면 같은 덱으로 판별
            if score >= stand.score * 0.75:
                stand.fre += 1

                aug = []
                if stand.augments:
                    for i in stand.augments:
                        aug.append(i)
                for i in deck.augments1:
                    aug.append(i)
                stand.augments = aug

                haug = []
                if stand.H_aug:
                    for i in stand.H_aug:
                        haug.append(i)
                haug.append(deck.H_aug1)
                stand.H_aug = haug

                placements = []
                if stand.placement:
                    for i in stand.placement:
                        placements.append(i)
                placements.append(deck.placement)
                stand.placement = placements

                stand.save()

        #units2 검사
        for stand in standard:
            score = 0
            for unit in deck.units2:
                cores = stand.coreunits
                Sunits = stand.units
                if unit["character_id"] in Sunits:
                    score += 20
                    for core in cores:
                        if unit["character_id"] == core[0]:
                            score += 10* core[1]

            #점수가 75%이상 이면 같은 덱으로 판별
            if score >= stand.score * 0.75:
                stand.fre += 1

                aug = []
                if stand.augments:
                    for i in stand.augments:
                        aug.append(i)
                for i in deck.augments2:
                    aug.append(i)
                stand.augments = aug

                haug = []
                if stand.H_aug:
                    for i in stand.H_aug:
                        haug.append(i)
                haug.append(deck.H_aug2)
                stand.H_aug = haug

                placements = []
                if stand.placement:
                    for i in stand.placement:
                        placements.append(i)
                placements.append(deck.placement)
                stand.placement = placements

                stand.save()


def statisticsOfStandard():
    standard = StandardDeck.objects.all()

    for stand in standard:
        c = Counter(stand.augments).most_common(2)
        stand.augments = [c[0][0], c[1][0]]
        c = Counter(stand.H_aug).most_common(1)
        stand.H_aug = [c[0][0]]
        win = 0
        windef = 0
        avg = 0
        for i in stand.placement:
            if i == 1:
                win += 1
                windef += 1
            elif i == 2:
                windef += 1
            avg+= i
        stand.winrate = round((win/stand.fre)*100,1)
        stand.windefencerate = round((windef/stand.fre)*100,1)
        stand.avgplace = round((avg/stand.fre),1)
        stand.save()



def check_save_double(standarddecks, decks):
    #스탠다드 덱 하나마다 덱 데이터 살펴보면서 기준맞는지지
    for standarddeck in standarddecks:
        for deck in decks:
            units = [deck.units1,deck.units2]
            scores=[]
            for deckunits in units:
                score = 0
                for unit in deckunits:
                    cores = standarddeck.coreunits
                    Sunits = standarddeck.units
                    if unit["character_id"] in Sunits:
                        score += 20
                        for core in cores:
                            if unit["character_id"] == core[0]:
                                score += 10* core[1]
                scores.append(score)
                
        #하나가 기준에 맞으면 파트너 덱을 스탠다드 덱 살펴보면서 기준맞는지 확인
        #점수가 75%이상 이면 같은 덱으로 판별
            idx = 0
            for score in scores:
                if score >= standarddeck.score * 0.75:
                    if idx == 1:
                        idx = 0
                    else:
                        idx = 1

                    for pstanddeck in standarddecks:
                        score = 0
                        for unit in units[idx]:
                            cores = pstanddeck.coreunits
                            Sunits = pstanddeck.units
                            if unit["character_id"] in Sunits:
                                score += 20
                                for core in cores:
                                    if unit["character_id"] == core[0]:
                                        score += 10* core[1]
                        if score >= standarddeck.score * 0.75:
                            #덱 저장
                            dds = DoubleDeck.objects.filter(parentsdeck = standarddeck)
                            if not dds:
                                dd = DoubleDeck(parentsdeck = standarddeck, deck_id = pstanddeck.id, fre = 1, placement = [deck.placement])
                                dd.save()
                            else:
                                dds = DoubleDeck.objects.filter(deck_id = pstanddeck.id, parentsdeck = standarddeck)
                                if not dds:
                                    dd = DoubleDeck(parentsdeck = standarddeck, deck_id = pstanddeck.id, fre = 1, placement = [deck.placement])
                                    dd.save()
                                    pass
                                else:
                                    dd=dds[0]
                                    dd.fre+=1
                                    temp = []
                                    for i in dd.placement:
                                        temp.append(i)
                                    temp.append(deck.placement)
                                    dd.placement = temp
                                    dd.save()

                                
                                
                                
                                
                    break
                idx += 1


def double_statistics(ds):
    #통계 구하기
    for deck in ds:
        if deck.fre < 10:
            continue
        win = 0
        windef = 0
        avg = 0
        for i in deck.placement:
            if i == 1:
                win += 1
                windef += 1
            elif i == 2:
                windef += 1
            avg+= i
        deck.winrate = round((win/deck.fre)*100,1)
        deck.windefencerate = round((windef/deck.fre)*100,1)
        deck.avgplace = round((avg/deck.fre),1)
        deck.save()



class Command(BaseCommand):
    """
    롤체지지에서 크롤링
    크롤링 - 유닛들 , 아이템
    가중치로 덱 판단
    유닛하나당 기본적으로 20
    아이템 하나당 10 추가 만약 - 바이 알리스타 사미라 세주아니 에코 레오나 아펠리오스 우르곳 피들스틱
                                 20   20      50     50     20   20     50       20     40
    전체 합한거 * 0.75 >= 이면 덱에 포함
    traits, placement, augments 같이 저장

        기준 덱에 외래키 잡고
            for deckdata in deckdatas:
        for i in addDeck(lst, deckdata.units1):
            for j in addDeck(lst, deckdata.units2):
                s = [i ,j]
                s.sort()
                w = Win(deckdata.placement, s[0] ,s[1])
                A.append(w)
    return A
    이런식으로 파트너 덱도 기준에 맞춰서 순위 augment, item, unit 저장
    
    """
    def handle(self, *args, **kwargs):
        
        #r기존의 데이터 삭제
        ds = DoubleDeck.objects.all()
        ds.delete()
        
        #스탠다드덱 받아서 거기서 기준에 맞는 지금의 스탠다드 덱인지 판별하고 맞으면 그 파트너의 덱은 어떤 덱인지
        #확인 후 둘다 기준에 맞으면 더블덱 모델에 부모덱 이랑 몇등인지 증강 등등 다 덱에 추가
        standarddecks = StandardDeck.objects.all()
        decks = DeckData.objects.all()
        check_save_double(standarddecks, decks)
        
        #등수 체크해서 기록 저장
        ds = DoubleDeck.objects.all()
        double_statistics(ds)

        
        #표본이 10개 미만인 데이터 삭제
        ds = DoubleDeck.objects.all()
        for i in ds:
            if not i.winrate:
                i.delete()