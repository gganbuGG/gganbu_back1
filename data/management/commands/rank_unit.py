from django.core.management.base import BaseCommand
from data.models import Combinations_partner,Combinations, Champion
from collections import Counter

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)

def EtoK(name):
    champ = {
    "TFT8_Kaisa" : "카이사",
    "TFT8_Lux" : "럭스",
    "TFT8_Kayle" : "케일",
    "TFT8_Poppy" : "뽀삐",
    "TFT8_Galio" : "갈리오",
    "TFT8_Rell" : "렐",
    "TFT8_Velkoz" : "벨코즈",
    "TFT8_Nilah" : "닐라",
    "TFT8_Ashe" : "애쉬",
    "TFT8_Yasuo" : "야스오",
    "TFT8_Senna" : "세나",
    "TFT8_Zed" : "제드",
    "TFT8_Lulu" : "룰루",
    "TFT8_Nunu" : "누누",
    "TFT8_Yuumi" : "유미",
    "TFT8_Zoe" : "조이",
    "TFT8_Taliyah" : "탈리야",
    "TFT8_Sivir" : "시비르",
    "TFT8_Gangplank" : "갱플랭크",
    "TFT8_WuKong" : "오공",
    "TFT8_Draven" : "드레이븐",
    "TFT8_Malphite" : "말파이트",
    "TFT8_Nasus" : "나서스",
    "TFT8_Jinx" : "징크스",
    "TFT8_Vayne" : "베인",
    "TFT8_MissFortune" : "미스포츈",
    "TFT8_Chogath" : "초가스",
    "TFT8_Rammus" : "람머스",
    "TFT8_BelVeth" : "벨베스",
    "TFT8_AurelionSol" : "아우렐리온솔",
    "TFT8_Zac" : "자크",
    "TFT8_Mordekaiser" : "모데카이저",
    "TFT8_Leblanc" : "르블랑",
    "TFT8_Sylas" : "사일러스",
    "TFT8_Camille" : "카밀",
    "TFT8_Ezreal" : "이즈리얼",
    "TFT8_Sona" : "소나",
    "TFT8_Ekko" : "에코",
    "TFT8_Sett" : "세트",
    "TFT8_Janna" : "잔나",
    "TFT8_Urgot" : "우르곳",
    "TFT8_Syndra" : "신드라",
    "TFT8_Fiddlesticks" : "피들스틱",
    "TFT8_Blitzcrank" : "블리츠크랭크",
    "TFT8_Renekton" : "레넥톤",
    "TFT8_Vi" : "바이",
    "TFT8_LeeSin" : "리신",
    "TFT8_Riven" : "리븐",
    "TFT8_Jax" : "잭스",
    "TFT8_Sejuani" : "세주아니",
    "TFT8_Soraka" : "소라카",
    "TFT8_Talon" : "탈론",
    "TFT8_Fiora" : "피오라",
    "TFT8_Annie" : "애니",
    "TFT8_Alistar" : "알리스타",
    "TFT8_Viego" : "비에고",
    "TFT8_Samira" : "사미라",
    "TFT8_Aphelios" : "아펠리오스",
    "TFT8_Leona" : "레오나"
    }

    return champ[name]

class Command(BaseCommand):
    help = "챔피언 통계(아이템, tier) - 1등한 소환사 팀에서 자주 등장했던 챔피언의 아이템, 티어 통계"
    def handle(self, *args, **kwargs):
        combinations = Combinations.objects.all().order_by('-updated_time')
        c_time = Champion.objects.all().order_by('-updated_time')
        
        if not c_time:
            c_time = '2023-01-01 00:00:00'
        else :
            c_time = str(Combinations.objects.all().order_by('-updated_time')[0].updated_time)[:19]
        
        c_time = convert_unixtime(c_time)
        for combination in combinations:
            if c_time > convert_unixtime(str(combination.updated_time)[:19]): 
                continue
            units = combination.units
            for unit in units:
                c = Champion.objects.filter(name = EtoK(unit["character_id"])])
                if not c :
                    tiers = []
                    tiers.append(unit["tier"])
                    c = Champion(name = EtoK(unit["character_id"]), items = unit["itemNames"], tier = tiers, rarity = unit["rarity"])
                    c.save()
                else :
                    items = []
                    items = c[0].items
                    tiers = c[0].tier
                    c.delete()
                    for item in unit["itemNames"]:
                        items.append(item)
                    tiers.append(unit["tier"])
                    c = Champion(name = EtoK(unit["character_id"]),items = items, tier = tiers, rarity = unit["rarity"])
                    c.save()

        combinations_partner = Combinations_partner.objects.all().order_by('-updated_time')
        for combination in combinations_partner:
            if c_time > convert_unixtime(str(combination.updated_time)[:19]): 
                continue
            units = combination.units
            for unit in units:
                c = Champion.objects.filter(name = EtoK(unit["character_id"]))
                if not c :
                    tiers = []
                    tiers.append(unit["tier"])
                    c = Champion(name = EtoK(unit["character_id"]), items = unit["itemNames"], tier = tiers, rarity = unit["rarity"])
                    c.save()
                else :
                    items = []
                    items = c[0].items
                    tiers = c[0].tier
                    c.delete()
                    for item in unit["itemNames"]:
                        items.append(item)
                    tiers.append(unit["tier"])
                    c = Champion(name = EtoK(unit["character_id"]),items = items, tier = tiers, rarity = unit["rarity"])
                    c.save()



        