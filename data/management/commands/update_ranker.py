from django.core.management.base import BaseCommand
import requests
from data.models import Summoner_rank
from bs4 import BeautifulSoup
import time
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Summoner:
    def __init__(self, name, tier, LP, winrate, game_num, win):
        self.name = name
        self.tier = tier
        self.LP = LP
        self.winrate = winrate
        self.game_num = game_num
        self.win = win
        self.lose = int(game_num)-int(win)

def get_API_key():
    c = os.path.join(BASE_DIR, 'riot_API.txt')
    file = open(c, "r")
    API_KEY = file.read()
    file.close()
    return API_KEY

def get_TOPs():
    # 크롤링해서 정보 객체의 배열로 저장
    url = 'https://lolchess.gg/leaderboards?mode=doubleup&region=kr'

    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.select_one('tbody')
        sNames = tbody.select('tr > td.summoner > a')
        sTiers = tbody.select('tr > td.tier > span.tier-name-sm')
        LPs = tbody.select('tr > td.lp.active')
        winrates = tbody.select('tr > td.winrate')
        game_nums = tbody.select('tr > td.played')
        wins = tbody.select('tr > td.wins')

        TOPs = []

        for i in range(len(sNames)):
            s = Summoner(sNames[i].get_text().strip(), sTiers[i].get_text().strip(), LPs[i].get_text().strip(), winrates[i].get_text().strip(), game_nums[i].get_text().strip(), wins[i].get_text().strip(), )
            TOPs.append(s)

        return TOPs
    else :
        return response.status_code

def set_rankerData(TOPs, API_KEY):
    for top in TOPs:
        url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{top.name}?api_key={API_KEY}'

        response = requests.get(url)
        if response.status_code == 200: # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
            print("...")
            pass
        
        elif response.status_code == 429:
            print('api cost full : infinite loop start')
            start_time = time.time()

            while True: # 429error가 끝날 때까지 무한 루프
                if response.status_code == 429:
                    print('try 10 second wait time')
                    time.sleep(10)
                    url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{top.name}?api_key={API_KEY}'
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
                    url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{top.name}?api_key={API_KEY}'
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
        
        elif response.status_code == 404:
            print('소환사 없음')
            break

        data = response.json()
        print(data)
        puuid = data['puuid']
        name = data['name']
        profileIconId = data['profileIconId']

        s = Summoner_rank(name = name, puuid = puuid, profileIconID = profileIconId, tier = top.tier, LP = top.LP, winrate = top.winrate, game_num= top.game_num, win = top.win, lose = top.lose)
        s.save()

def delete_rankerData():
    # 데이터베이스에 저장되어 있던 object들 삭제
    obj = Summoner_rank.objects.all()
    obj.delete()


class Command(BaseCommand):
    help = "Update 100 Ranker Data in the database to new Ranker Data."
    def handle(self, *args, **kwargs):

        API_KEY = get_API_key()

        delete_rankerData()
        TOPs = get_TOPs()
        if type(TOPs) != list:
            print(TOPs)
            return 
        set_rankerData(TOPs, API_KEY)
        print("ranker update is finished")