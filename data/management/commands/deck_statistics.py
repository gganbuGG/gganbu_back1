from data.models import DeckData,Deck
from django.core.management.base import BaseCommand
from collections import Counter
from pathlib import Path

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

class Comb():
    def __init__(self, units, augments, placement, core, h_aug):
        self.units = units
        self.augments = augments
        self.placement = placement
        self.core = core
        self.h_aug = h_aug


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        """
        
        """
        deckDatas = DeckData.objects.all().order_by('-updated_time')
        Deck.objects.all().order_by('-updated_time').delete()
        combs = []
        for deckdata in deckDatas:
            un1 = []
            for u in deckdata.units1:
                un1.append(u["character_id"])
            un2 = []
            for u in deckdata.units2:
                un2.append(u["character_id"])
            combs.append(Comb(un1, deckdata.augments1, deckdata.placement, deckdata.coreunits1, deckdata.H_aug1))
            combs.append(Comb(un2, deckdata.augments2, deckdata.placement, deckdata.coreunits2, deckdata.H_aug2))

        
        unitstring = []
        for comb in combs:
            unitstring.append(str(comb.units))
        
        count = Counter(unitstring).most_common()
        decks = []
        for c in count:
            if c[1] >= 10 and c[0] != "[]":
                decks.append(c)
        #decks : 진짜덱들
        for deck in decks:
            one = 0
            defence = 0
            pl = 0
            augments = []
            h_augs =[]
            cores= []
            for comb in combs:
                if deck[0] == str(comb.units):
                    units = comb.units
                    if comb.placement == 1:
                        one += 1
                    if comb.placement <= 2:
                        defence += 1
                    for aug in comb.augments:
                        augments.append(aug)
                    h_augs.append(comb.h_aug)
                    for core in comb.core:
                        cores.append(core)
                    pl += comb.placement
            ag = []
            for i in Counter(augments).most_common(2):
                ag.append(i[0])
            hag = Counter(h_augs).most_common(1)
            hag = hag[0][0]
            core = []
            for i in Counter(cores).most_common(3):
                core.append(i[0])

            temp = []
            traits = []
            for unit in units:
                temp.append(korean(unit, "traits"))
            for t in temp:
                for trait in t:
                    traits.append(trait)

            tra = {
                }
            for trait in Counter(traits).most_common():
                if trait[0] == "Set8_GenAE":
                    if trait[1] < 5 and trait[1] >= 3:
                        tier = 1
                    elif trait[1] >= 5:
                        tier = 3
                    else:
                        tier = 0

                elif trait[0] == "Set8_AnimaSquad":
                    if trait[1] >= 3 and trait[1] < 5:
                        tier = 1
                    elif trait[1] >= 5 and trait[1] < 7:
                        tier = 3
                    elif trait[1] >=7 :
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_SpaceCorps":
                    if trait[1] >= 3 and trait[1] < 5:
                        tier = 1
                    elif trait[1] >= 5 and trait[1] <7:
                        tier = 2
                    elif trait[1] >= 7 and trait[1] < 9:
                        tier = 3
                    elif trait[1] >=9 :
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_ExoPrime":
                    if trait[1] >= 3 and trait[1] < 5:
                        tier = 1
                    elif trait[1] >= 5:
                        tier = 3
                    else:
                        tier = 0
                        
                elif trait[0] == "Set8_Civilian":
                    if trait[1] == 1:
                        tier = 1
                    elif trait[1] == 2:
                        tier = 2
                    elif trait[1] >=3 :
                        tier = 3
                    else:
                        tier = 0
                
                elif trait[0] == "Set8_StarGuardian":
                    if trait[1] >= 3 and trait[1] < 5:
                        tier = 1
                    elif trait[1] >= 5 and trait[1] < 7:
                        tier = 2
                    elif trait[1] >= 7 and trait[1] < 9:
                        tier = 3
                    elif trait[1] >= 9:
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_Arsenal":
                    tier = 3

                elif trait[0] == "Set8_Supers":
                    if trait[1] >= 3: 
                        tier = 3
                    else:
                        tier = 0

                elif trait[0] == "Set8_Threat":
                    tier = 3

                elif trait[0] == "Set8_Admin":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 6:
                        tier = 3
                    elif trait[1] >=6 :
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_UndergroundThe":
                    if trait[1] >= 3 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 5:
                        tier = 2
                    elif trait[1] == 5 :
                        tier = 3
                    elif trait[1] >=6:
                        tier = 4
                    else:
                        tier = 0
                        
                elif trait[0] == "Set8_OxForce":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 6:
                        tier = 2
                    elif trait[1] >=6 and trait[1] < 8:
                        tier = 3
                    elif trait[1] >= 8:
                        tier = 4
                    else:
                        tier = 0
                
                elif trait[0] == "Set8_Duelist":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 6:
                        tier = 2
                    elif trait[1] >=6 and trait[1] < 8:
                        tier = 3
                    elif trait[1] >= 8:
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_Forecaster":
                    tier = 3

                elif trait[0] == "Set8_Mascot":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 6:
                        tier = 2
                    elif trait[1] >=6 and trait[1] < 8:
                        tier = 3
                    elif trait[1] >= 8:
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_Renegade":
                    if trait[1] >= 3 and trait[1] < 6:
                        tier = 3
                    elif trait[1] >= 6:
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_Aegis":
                    if trait[1] >= 2 and trait[1] < 3:
                        tier = 1
                    elif trait[1] >= 3 and trait[1] < 4:
                        tier = 2
                    elif trait[1] >=4 and trait[1] < 5:
                        tier = 3
                    elif trait[1] >= 5:
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_Heart":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 6:
                        tier = 2
                    elif trait[1] >=6:
                        tier = 3
                    else:
                        tier = 0

                elif trait[0] == "Set8_Brawler":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 6:
                        tier = 2
                    elif trait[1] >=6 and trait[1] < 8:
                        tier = 3
                    elif trait[1] >= 8:
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_Defender":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 6:
                        tier = 3
                    elif trait[1] >=6:
                        tier = 4
                    else:
                        tier = 0

                elif trait[0] == "Set8_Ace":
                    if trait[1] == 1:
                        tier = 1
                    elif trait[1] >= 2 and trait[1] < 4:
                        tier = 0
                    elif trait[1] == 4:
                        tier = 3
                    else:
                        tier = 0
                        
                elif trait[0] == "Set8_Prankster":
                    if trait[1] >= 2 and trait[1] < 3:
                        tier = 1
                    elif trait[1] >= 3:
                        tier = 3
                    else:
                        tier = 0
                        
                elif trait[0] == "Set8_Recon":
                    if trait[1] >= 2  and trait[1] < 3:
                        tier = 1
                    elif trait[1] >= 3 and trait[1] < 4:
                        tier = 2
                    elif trait[1] >= 4:
                        tier = 3
                    else:
                        tier = 0

                elif trait[0] == "Set8_Channeler":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4 and trait[1] < 6:
                        tier = 2
                    elif trait[1] >=6 and trait[1] < 8:
                        tier = 3
                    elif trait[1] >= 8:
                        tier = 4
                    else:
                        tier = 0
                
                elif trait[0] == "Set8_Corrupted":
                    tier = 3

                elif trait[0] == "Set8_Deadeye":
                    if trait[1] >= 2 and trait[1] < 4:
                        tier = 1
                    elif trait[1] >= 4:
                        tier = 3
                    else:
                        tier = 0
                    
                elif trait[0] == "Set8_Hacker":
                    if trait[1] >= 2 and trait[1] < 3:
                        tier = 1
                    elif trait[1] >= 3 and trait[1] < 4:
                        tier = 2
                    elif trait[1] >= 4:
                        tier = 3
                    else:
                        tier = 0

                    
                active = {
                }
                active["tier"] = tier
                active["count"] = trait[1]
                tra[trait[0]] = active

            #t = sorted(tra.items(), key=lambda x: x[1])
            t = sorted(list(tra.items()), key= lambda x: x[1]["tier"], reverse=True)
            d = {}
            for temp in t:
                d[temp[0]] = temp[1]["count"]

            d = Deck(winrate = round(((one * deck[1])/len(deckDatas))*100, 1), windefencerate = round(((defence * deck[1])/len(deckDatas))*100,1), avgplace = round(pl/deck[1],1), units = units, augments = ag, traits = d,core= core, h_aug = hag)
            d.save()