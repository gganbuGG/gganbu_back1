from rest_framework import serializers
from .models import Summoner_rank, Champion
from collections import Counter

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
        "TFT_Item_EmptyBag" : "앰티백"
    }
    return item[name]
class SummonerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Summoner_rank
        fields = ('name', 'profileIconId', 'tier', 'LP', 'winrate', 'game_num', 'win', 'lose' )


class ChampionSerializer(serializers.ModelSerializer) :
    items = serializers.SerializerMethodField('get3items')
    tier = serializers.SerializerMethodField('getmosttier')
    how_many = serializers.SerializerMethodField('gethow')

    class Meta :
        model = Champion
        fields = ('name', 'items', 'rarity', 'tier', 'how_many')
    

    
    def get3items(self, obj):
        items = []
        for name in Counter(obj.items).most_common(3):
            items.append(EtoKItem(name[0]))
        return items
    
    def getmosttier(self, obj):
        return Counter(obj.tier).most_common(1)[0][0]

    def gethow(self, obj):
        return len(obj.tier)
