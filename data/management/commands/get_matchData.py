from django.core.management.base import BaseCommand
import requests
import time
from data.models import Match, Summoner_rank, DeckData
import json, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)

def get_API_key():
    c = os.path.join(BASE_DIR, 'riot_API.txt')
    file = open(c, "r")
    API_KEY = file.read()
    file.close()
    return API_KEY

def get_puuids():
    puuids = []
    obj = Summoner_rank.objects.all()
    for s in obj:
        puuids.append(s.puuid)

    return puuids

def askRiot(url):
    #라이엇 api 요청
    response = requests.get(url)

    if response.status_code == 200: # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif response.status_code == 429:
        print('api cost full : infinite loop start')
        start_time = time.time()

        while True: # 429error가 끝날 때까지 무한 루프
            if response.status_code == 429:
                print('try 10 second wait time')
                time.sleep(10)
                response = requests.get(url)
                print(response.status_code)

            elif response.status_code == 200: #다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break

    elif response.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
        print('service available error')
        start_time = time.time()

        while True:
            if response.status_code == 503 or response.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)
                response = requests.get(url)
                print(response.status_code)

            elif response.status_code == 200: # 똑같이 response가 정상이면 loop escape
                print('total error wait time : ', time.time() - start_time)
                print('recovery api cost')
                break

    elif response.status_code == 403: # api갱신이 필요
        print('you need api renewal')
        print('break')
        return 
    #결과 json으로 반환
    return response.json()

def get_matchData(puuids, API_KEY):
    start = Match.objects.all().order_by('-updated_time')
    if not start:
        start = convert_unixtime('2023-02-08 00:00:00'[:19])
    else :
        start = convert_unixtime(str(start[0].updated_time)[:19])
    for puuid in puuids:
        ids = askRiot(f'https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&startTime={start}&count=100&api_key={API_KEY}')
        
        #matchid 리스트가 100개면 100개보다 더 있을 수 있으므로 startTime값 바꿔주고 요청해서 ids 배열에 추가하기
        if len(ids) == 100:
            while True:
                data = askRiot(f'https://asia.api.riotgames.com/tft/match/v1/matches/{ids[0]}?api_key={API_KEY}')
                tempEnd = data["info"]["game_datetime"]
                temp = askRiot(f'https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&startTime={tempEnd}&count=100&api_key={API_KEY}')
                ids = ids + temp
                if len(temp) != 100:
                    break

        for matchid in ids:
            data = askRiot(f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={API_KEY}')
            version = data['info']['game_version']
            if version[:12] != "Version 13.5":
                print("롤토체스 데이터 업데이트")
                break
            #더블업 모드만 저장
            if data['info']['tft_game_type'] == 'pairs':
                m = Match.objects.filter(matchId = matchid)
                #같은 match가 저장되는 일 없게 matchid 검사
                if not m :
                    m = Match(matchId = matchid, info = data)
                    m.save()


class Group:
    def __init__(self, units, augments, placement, core, h_aug):
        self.units = units
        self.augments = augments
        self.placement = placement
        self.core = core
        self.h_aug = h_aug

def match2deck():
    #tft정보 (한글로 바꾸기)
    ag = os.path.join(BASE_DIR, 'tft-augments.json')
    with open(ag, 'r', encoding='UTF8') as f1:
        augmentName = json.load(f1)["data"]
    f1.close()
    he = os.path.join(BASE_DIR, 'tft-hero-augments.json')
    with open(he, 'r', encoding='UTF8') as f2:
        heroAugmentName = json.load(f2)["data"]
    f2.close()
    matchs = Match.objects.all().order_by('-updated_time')
    decks = DeckData.objects.all().order_by('-updated_time')
    if not decks:
        d_time = '2023-02-08 00:00:00'
    else :
        d_time = str(decks[0].updated_time)[:19]
    
    d_time = convert_unixtime(d_time)
    for match in matchs:
        if d_time > convert_unixtime(str(match.updated_time)[:19]) :
            continue
        else :
            #더블업 팀 별로 나누어서 덱 저장
            group1 = []
            group2 = []
            group3 = []
            group4 = []
            for player in match.info["info"]["participants"]:
                core = []
                units = player["units"]
                for unit in player["units"]:
                    if len(unit["itemNames"]) == 3 and ("TFT_Item_ThiefsGloves" not in unit["character_id"] or "TFT_Item_EmptyBag" not in unit["itemNames"]):
                        core.append(unit["character_id"])
                    
                augments = []
                for augment in player["augments"]:
                    try :
                        a = augmentName[augment]
                        augments.append(augment)
                    except KeyError:    
                        #영웅 증강 따로 저장
                        h_aug = augment
                placement = player["placement"]
                if placement == 1 or placement == 2:
                    placement = 1
                elif placement == 3 or placement == 4:
                    placement = 2
                elif placement == 5 or placement == 6:
                    placement = 3
                elif placement == 7 or placement == 8:
                    placement = 4

                g = Group(units,augments,placement, core, h_aug)
                if player["partner_group_id"] == 1:
                    group1.append(g)
                elif player["partner_group_id"] == 2:
                    group2.append(g)
                elif player["partner_group_id"] == 3:
                    group3.append(g)
                elif player["partner_group_id"] == 4:
                    group4.append(g)
        
            DeckData(placement = group1[0].placement, units1 = group1[0].units, coreunits1 = group1[0].core , units2 = group1[1].units, coreunits2 = group1[1].core , augments1 = group1[0].augments, augments2 = group1[1].augments, H_aug1 = group1[0].h_aug, H_aug2 = group1[1].h_aug).save()
            DeckData(placement = group2[0].placement, units1 = group2[0].units, coreunits1 = group2[0].core , units2 = group2[1].units, coreunits2 = group2[1].core , augments1 = group2[0].augments, augments2 = group2[1].augments, H_aug1 = group2[0].h_aug, H_aug2 = group2[1].h_aug).save()
            DeckData(placement = group3[0].placement, units1 = group3[0].units, coreunits1 = group3[0].core , units2 = group3[1].units, coreunits2 = group3[1].core , augments1 = group3[0].augments, augments2 = group3[1].augments, H_aug1 = group3[0].h_aug, H_aug2 = group3[1].h_aug).save()
            DeckData(placement = group4[0].placement, units1 = group4[0].units, coreunits1 = group4[0].core , units2 = group4[1].units, coreunits2 = group4[1].core , augments1 = group4[0].augments, augments2 = group4[1].augments, H_aug1 = group4[0].h_aug, H_aug2 = group4[1].h_aug).save()

class Command(BaseCommand):
    help = "Store 'Matchdata' in DB to Use 'Summoner_rank'. 그리고 덱 저장"
    def handle(self, *args, **kwargs):
        API_KEY = get_API_key()

        puuids = get_puuids()
        print("matchData update start")
        get_matchData(puuids, API_KEY)
        match2deck()
        print("matchData update is finished")