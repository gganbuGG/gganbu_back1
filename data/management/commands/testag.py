from django.core.management.base import BaseCommand
import requests
from data.models import Summoner_rank
from bs4 import BeautifulSoup
import time
import datetime

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
    file = open("./riot_API.txt", "r")
    API_KEY = file.read()
    file.close()
    return API_KEY

def get_TOPs():
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
    
        print(TOPs[0].name, TOPs[3].lose)

        return TOPs
    else :
        return response.status_code

class Command(BaseCommand):
    help = "Update 100 Ranker Data in the database to new Ranker Data."
    def handle(self, *args, **kwargs):

        API_KEY = get_API_key()

        TOPs = get_TOPs()
        update_time = datetime.datetime.now()
        print(update_time)