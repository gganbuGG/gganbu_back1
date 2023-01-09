from django.core.management.base import BaseCommand
import requests
from data.models import Summoner_rank
from bs4 import BeautifulSoup
import time


def get_API_key():
    file = open("./riot_API.txt", "r")
    API_KEY = file.read()
    file.close()
    return API_KEY

def get_TOPsNames():
    url = 'https://lolchess.gg/leaderboards?mode=doubleup&region=kr'

    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.select_one('tbody')
        sNames = tbody.select('tr > td.summoner > a')
            
        TOPsNames = []
        for sName in sNames:
            TOPsNames.append(sName.get_text().strip())

        return TOPsNames
    else :
        return response.status_code

def set_rankerData(TOPsNames, API_KEY):
    for sName in TOPsNames:
        url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{sName}?api_key={API_KEY}'

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
                    url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{sName}?api_key={API_KEY}'
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
                    url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{sName}?api_key={API_KEY}'
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
        puuid = data['puuid']
        name = data['name']
        
        s = Summoner_rank(name = name, puuid = puuid)
        s.save()

def delete_rankerData():
    obj = Summoner_rank.objects.all()
    obj.delete()


class Command(BaseCommand):
    help = "Update 100 Ranker Data in the database to new Ranker Data."
    def handle(self, *args, **kwargs):

        API_KEY = get_API_key()

        delete_rankerData()
        TOPsNames = get_TOPsNames()
        set_rankerData(TOPsNames, API_KEY)