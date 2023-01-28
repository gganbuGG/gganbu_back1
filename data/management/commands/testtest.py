from data.models import Combinations, Combinations_partner, Champion
from django.core.management.base import BaseCommand

def champData(name):
    champ = {
    "TFT8_Kaisa" : 
    {
        "name" : "카이사",
        "traits" : ["정찰단","별 수호자"]
    },
    "TFT8_Lux" : 
    {
        "name" : "럭스",
        "traits" : ["주문투척자","별 수호자"]
    },
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

def EtoKItem(name):
    item = {
        "TFT_Item_GargoyleStoneplate" : "가고일 돌갑옷",
        "TFT_Item_IonicSpark" : "이온충격기",
        "TFT_Item_ZekesHerald" : "지크의 전령",
        "TFT_Item_ArchangelsStaff" : "대천사의 지팡이",
        "TFT8_Item_HeartEmblemItem" : "선의 상징",
        "TFT_Item_JeweledGauntlet" : "보석 건틀릿",
        "TFT_Item_MadredsBloodrazor" : "거인학살자",
        "TFT_Item_StatikkShiv" : "스태틱의 단검",
        "TFT_Item_DragonsClaw" : "용의 발톱",
        "TFT_Item_RedBuff" : "태양불꽃 망토",
        "TFT_Item_UnstableConcoction" : "정의의 손길",
        "TFT_Item_LastWhisper" : "최후의 속삭임",
        "TFT_Item_SpearOfShojin" : "쇼진의 창",
        "TFT_Item_TitanicHydra" : "즈롯 차원문",
        "TFT_Item_GuardianAngel" : "밤의 끝자락",
        "TFT_Item_ThiefsGloves" : "도적의 장갑",
        "TFT_Item_PowerGauntlet" : "방패파괴자",
        "TFT_Item_FrozenHeart" : "수호자의 맹세",
        "TFT_Item_LocketOfTheIronSolari" : "강철의 솔라리 펜던트",
        "TFT_Item_Redemption" : "구원",
        "TFT_Item_RunaansHurricane" : "루난의 허리케인",
        "TFT8_Item_DuelistEmblemItem" : "결투가 상징",
        "TFT_Item_SeraphsEmbrace" : "푸른 파수꾼",
        "TFT_Item_HextechGunblade" : "마법공학 총검",
        "TFT_Item_Zephyr" : "서풍",
        "TFT8_Item_AnimaSquadEmblemItem" : "동물특공대 상징",
        "TFT_Item_BrambleVest" : "덤불조끼",
        "TFT8_Item_InterPolarisEmblemItem" : "레이저단 상징",
        "TFT8_Item_OxForceEmblemItem" : "황소부대 상징",
        "TFT_Item_GuinsoosRageblade" : "구인수의 격노검",
        "TFT_Item_InfinityEdge" : "무한의 대검",
        "TFT_Item_TitansResolve" : "거인의 결의",
        "TFT8_Item_DefenderEmblemItem" : "엄호대 상징",
        "TFT_Item_Bloodthirster" : "피바라기",
        "TFT4_Item_OrnnEternalWinter" : "영원한 겨울",
        "TFT_Item_WarmogsArmor" : "워모그의 갑옷",
        "TFT_Item_RabadonsDeathcap" : "라바돈의 죽음모자",
        "TFT_Item_Morellonomicon" : "모렐로노미콘",
        "TFT8_Item_RenegadeEmblemItem" : "무법자 상징",
        "TFT8_Item_AceEmblemItem" : "에이스 상징",
        "TFT8_Item_BrawlerEmblemItem" : "싸움꾼 상징",
        "TFT_Item_Chalice" : "힘의 성배",
        "TFT8_Item_CivilianEmblemItem" : "민간인 상징",
        "TFT4_Item_OrnnAnimaVisage" : "영혼의 형상",
        "TFT8_Item_ExoPrimeEmblemItem" : "메카: 프라임 상징",
        "TFT4_Item_OrnnMuramana" : "마나자네",
        "TFT_Item_Quicksilver" : "수은",
        "TFT_Item_RapidFireCannon" : "고속 연사포",
        "TFT_Item_Shroud" : "침묵의 장막",
        "TFT_Item_Deathblade" : "죽음의 검",
        "TFT8_Item_MascotEmblemItem" : "마스코트 상징",
        "TFT8_Item_DeadeyeEmblemItem" : "특등사수 상징",
        "TFT4_Item_OrnnRocketPropelledFist" : "로켓 주먹",
        "TFT8_Item_AegisEmblemItem" : "방패대 상징",
        "TFT8_Item_ReconEmblemItem" : "정찰단 상징",
        "TFT_Item_ForceOfNature" : "전략가의 왕관",
        "TFT8_Item_ADMINEmblemItem" : "자동방어체계 상징",
        "TFT4_Item_OrnnZhonyasParadox" : "존야의 역설",
        "TFT4_Item_OrnnInfinityForce" : "무한한 삼위일체",
        "TFT4_Item_OrnnDeathsDefiance" : "죽음의 저항",
        "TFT4_Item_OrnnTheCollector" : "황금 징수의 총",
        "TFT4_Item_OrnnObsidianCleaver" : "흑요석 양날 도끼",
    }
    return item[name]

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        cs = Champion.objects.all()
        for c in cs:
            temp = []
            items = c.items
            for item in items:
                temp.append(EtoKItem(item))
            print(temp)