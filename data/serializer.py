from rest_framework import serializers
from .models import Summoner_rank, Champion, Deck, Synergy, StandardDeck
from collections import Counter
import json, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
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
class SummonerSerializer(serializers.ModelSerializer) :
    profileIcon = serializers.SerializerMethodField('getProfileIcon')
    class Meta :
        model = Summoner_rank
        fields = ('name', 'profileIcon', 'tier', 'LP', 'winrate', 'game_num', 'win', 'lose' )

    def getProfileIcon(self,obj):
        url = f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/profileicon/{obj.profileIconID}.png"
        return url

class ChampionSerializer(serializers.ModelSerializer) :

    name = serializers.SerializerMethodField('getKname')
    items = serializers.SerializerMethodField('get5items')
    tier = serializers.SerializerMethodField('getTierData')
    bigimg = serializers.SerializerMethodField('getbigimg')
    smallimg = serializers.SerializerMethodField('getsmallimg')
    bgimg = serializers.SerializerMethodField('getbgimg')

    class Meta :
        model = Champion
        fields = ('name', 'items', 'rarity', 'tier', 'bigimg', 'smallimg', 'bgimg')
    
    def getKname(self,obj):
            
        #tft정보 (한글로 바꾸기)
        c = os.path.join(BASE_DIR, 'tft-champion.json')
        with open(c, 'r', encoding='UTF8') as f:
            championName = json.load(f)["data"]
        result = championName[obj.name]["name"]
        f.close()
        return result

    def get5items(self, obj):
         #tft정보 (한글로 바꾸기)
        it = os.path.join(BASE_DIR, 'tft-item.json')
        with open(it, 'r', encoding='UTF8') as f:
            itemName = json.load(f)["data"]
        i = dict()
        for item in Counter(obj.items).most_common(5):
            if (item[0])[:17] == "TFT8_EmblemItems/":
                i[itemName[item[0]]["name"]] = f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-item/{(item[0])[17:]}.png"
            else:
                i[itemName[item[0]]["name"]] = f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-item/{item[0]}.png"
        f.close()
        return i
    
    def getTierData(self, obj):
        all = len(obj.tier)
        count = Counter(obj.tier)
        t = dict()
        t[1] = str(round((count[1]/all)*100, 1))+"%"
        t[2] = str(round((count[2]/all)*100, 1))+"%"
        t[3] = str(round((count[3]/all)*100, 1))+"%"
        return t

    def getbigimg(self, obj):
        url = f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-champion/{obj.name}.TFT_Set8.png"
        return url


    def getsmallimg(self, obj):
        if obj.name == "TFT8_WuKong":
            obj.name = "TFT8_Wukong"
        url = f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-hero-augment/{obj.name}.TFT_Set8.png"
        return url

    def getbgimg(self, obj):
        if obj.name == "TFT8_WuKong":
            obj.name = "TFT8_Wukong"
        url = f"https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/ChampionBackGround/{str(obj.name)[5:]}.jpg"
        return url

class OneDeckSerializer(serializers.ModelSerializer) :
    augments = serializers.SerializerMethodField('getAug')
    units = serializers.SerializerMethodField('getKunit')
    core = serializers.SerializerMethodField('getKcore')
    traits = serializers.SerializerMethodField('getTraits')

    class Meta :
        model = Deck
        fields = ('winrate', 'windefencerate', 'avgplace', 'augments', 'traits', 'units', 'core' )

    
    # champion 데이터 검색으로 찾자
    def getAug(self, obj):
        ag = os.path.join(BASE_DIR, 'tft-augments.json')
        with open(ag, 'r', encoding='UTF8') as f:
            augmentName = json.load(f)["data"]
        f.close()
        hag = os.path.join(BASE_DIR, 'tft-hero-augments.json')
        with open(hag, 'r', encoding='UTF8') as f2:
            haugmentName = json.load(f2)["data"]
        f2.close()
        c = Counter(obj.augments).most_common(2)
        c = [c[0][0], c[1][0], obj.h_aug]
        c0 = augmentName[c[0]]["image"]["full"]
        c1 = augmentName[c[1]]["image"]["full"]
        c2 = haugmentName[c[2]]["image"]["full"]
        c[0] = {"name" : augmentName[c[0]]["name"],
        "img" : f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-augment/{c0}"}
        c[1] = {"name" : augmentName[c[1]]["name"],
        "img" : f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-augment/{c1}"}
        c[2] = {"name" : haugmentName[c[2]]["name"],
        "img" : f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-hero-augment/{c2}"}
        
        return c
        
    
    def getKunit(self, obj):
        pa = os.path.join(BASE_DIR, 'tft-champion.json')
        with open(pa, 'r', encoding='UTF8') as f:
            championName = json.load(f)["data"]
        f.close()
        units = []
        for i in obj.units:
            ima = championName[i]["image"]["full"]
            temp = {
                "name" : championName[i]["name"],
                "img" : f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-hero-augment/{ima}"
            }
            units.append(temp)
        return units

    def getKcore(self, obj):
        pa = os.path.join(BASE_DIR, 'tft-champion.json')
        with open(pa, 'r', encoding='UTF8') as f:
            championName = json.load(f)["data"]
        f.close()
        it = os.path.join(BASE_DIR, 'tft-item.json')
        with open(it, 'r', encoding='UTF8') as f:
            itemName = json.load(f)["data"]
        f.close()
        cores = []
        
        for i in obj.core:
            champ = Champion.objects.filter(name = i)
            items = []
            for item in Counter(champ[0].items).most_common(3):
                ima = itemName[item[0]]["image"]["full"]
                temp = {
                    "name": itemName[item[0]]["name"],
                    "img": f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-item/{ima}"
                }
                items.append(temp)
            ima = championName[i]["image"]["full"]
            temp = {
                "name" : championName[i]["name"],
                "img" : f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-hero-augment/{ima}",
                "items" : items
            }
            cores.append(temp)
        return cores

    def getTraits(self, obj):
        ag = os.path.join(BASE_DIR, 'tft-trait.json')
        with open(ag, 'r', encoding='UTF8') as f:
            traitName = json.load(f)["data"]
        f.close()
        traits = []
        for key in obj.traits.keys():
            ima = traitName[key]["name"]
            if ima == "메카:프라임":
                ima = "메카%20프라임"
            if obj.traits[key]["tier"] == 1:
                tier = "bronze"
            elif obj.traits[key]["tier"] == 2:
                tier = "silver"
            elif obj.traits[key]["tier"] == 3:
                tier = "gold"
            elif obj.traits[key]["tier"] == 1:
                tier = "platinum"
            tr = {
                "name" : traitName[key]["name"],
                "count" : obj.traits[key]["count"],
                "img" : f"https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/{ima}.svg",
                "bgimg" : f"https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/{tier}.svg"
                
            }
            traits.append(tr)

        return traits

class StandardSynergySerializer(serializers.ModelSerializer) :
    # winrate 0 인거는 버릴까
    partnerDeck = serializers.SerializerMethodField('get_partnerDeck')
    units = serializers.SerializerMethodField('getKunit')
    class Meta :
        model = StandardDeck
        fields = ('units', 'partnerDeck')

    def getKunit(self, obj):
        pa = os.path.join(BASE_DIR, 'tft-champion.json')
        with open(pa, 'r', encoding='UTF8') as f:
            championName = json.load(f)["data"]
        f.close()
        units = []
        for i in obj.units:
            ima = championName[i]["image"]["full"]
            temp = {
                "name" : championName[i]["name"],
                "img" : f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-hero-augment/{ima}"
            }
            units.append(temp)
        return units
    
    def get_partnerDeck(self, obj):
        syns = Synergy.objects.filter(stand = obj.id).order_by('-winrate')[:3]
        t = []
        
        for syn in syns:
            units = []
            for i in syn.units:
                pa = os.path.join(BASE_DIR, 'tft-champion.json')
                with open(pa, 'r', encoding='UTF8') as f:
                    championName = json.load(f)["data"]
                f.close()
                ima = championName[i]["image"]["full"]
                if ima == "TFT8_WuKong.TFT_Set8.png":
                    ima = "TFT8_Wukong.TFT_Set8.png"
                temp = {
                    "name" : championName[i]["name"],
                    "img" : f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-hero-augment/{ima}"
                }
                units.append(temp)
            d = {
                "units" : units,
                "winrate" : syn.winrate,
                "windefencerate" : syn.windefencerate,
                "avgplace" : syn.avgplace
            }
            t.append(d)
        return t
