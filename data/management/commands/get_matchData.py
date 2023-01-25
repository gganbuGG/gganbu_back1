from django.core.management.base import BaseCommand
import requests
import time
import datetime
from data.models import Match, Summoner_rank

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)

def get_API_key():
    file = open("./riot_API.txt", "r")
    API_KEY = file.read()
    file.close()
    return API_KEY

def get_puuids():
    puuids = []
    obj = Summoner_rank.objects.all()
    for s in obj:
        puuids.append(s.puuid)

    return puuids

def get_matchData(puuids, API_KEY):
    start = Match.objects.all().order_by('-updated_time')
    if not start:
        start = convert_unixtime('2023-01-18 00:00:00'[:19])
    else :
        start = convert_unixtime(str(start[0].updated_time)[:19])
    for puuid in puuids:
        url = f'https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&startTime={start}&count=100&api_key={API_KEY}'
        response = requests.get(url)

        while response.status_code == 429:
            print("try 5 second wait time")
            time.sleep(5)
            url = f'https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&startTime={start}&count=100&api_key={API_KEY}'
            response = requests.get(url)

        ids = response.json()
        for matchid in ids:
            url = f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={API_KEY}'
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
                        url = f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={API_KEY}'
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
                        url = f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={API_KEY}'
                        response = requests.get(url)
                        print(response.status_code)

                    elif response.status_code == 200: # 똑같이 response가 정상이면 loop escape
                        print('total error wait time : ', time.time() - start_time)
                        print('recovery api cost')
                        break

            elif response.status_code == 403: # api갱신이 필요
                print('you need api renewal')
                print('break')
                break

            data = response.json()
            if data['info']['tft_game_type'] == 'pairs':
                m = Match.objects.filter(matchId = matchid)
                if not m :
                    m = Match(matchId = matchid, info = data)
                    m.save()

class Command(BaseCommand):
    help = "Store 'Matchdata' in DB to Use 'Summoner_rank'."
    def handle(self, *args, **kwargs):
        API_KEY = get_API_key()

        puuids = get_puuids()
        get_matchData(puuids, API_KEY)
        Match.objects.order_by('-updated_time')