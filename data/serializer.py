from rest_framework import serializers
from .models import Summoner_rank, Champion, Deck
from collections import Counter
import json

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

def EtoK(name):
    augments = {
    "TFT8_Augment_StarGuardianTrait" : "별 수호자 심장",
    "TFT8_Augment_RellSupport" : "변화의 철마술",
    "TFT7_Augment_AxiomArc2" : "원칙의 원형낫2",
    "TFT7_Augment_AxiomArc1" : "원칙의 원형낫1",
    "TFT8_Augment_HackerTrait" : "해커 심장",
    "TFT8_Augment_YasuoCarry" : "흡수의 바람",
    "TFT8_Augment_InterPolarisEmblem" : "레이저단 문장",
    "TFT7_Augment_PandorasBench" : "판도라의 대기석",
    "TFT8_Augment_SonaExile" : "전력망",
    "TFT6_Augment_Diversify2" : "단결된 의지2",
    "TFT6_Augment_Diversify1" : "단결된 의지1",
    "TFT6_Augment_CelestialBlessing1" : "천상의 축복1",
    "TFT8_Augment_JinxCarry" : "신난다!",
    "TFT6_Augment_PortableForge" : "휴대용 대장간",
    "TFT6_Augment_Battlemage1" : "전투 마법사1",
    "TFT6_Augment_Battlemage2" : "전투 마법사2",
    "TFT8_Augment_JaxASCarry" : "가차없는 맹공",
    "TFT8_Augment_ExoPrimeEmblem" : "메카: 프라임 문장",
    "TFT6_Augment_ThrillOfTheHunt1" : "사냥의 전율1",
    "TFT6_Augment_ThrillOfTheHunt2" : "사냥의 전율2",
    "TFT8_Augment_JaxSupport" : "회피",
    "TFT6_Augment_SunfireBoard" : "태양불꽃판",
    "TFT8_Augment_ReconTrait" : "정찰단 심장",
    "TFT8_Augment_EzrealSupport" : "도굴꾼의 전리품",
    "TFT6_Augment_ComponentGrabBag" : "재료 꾸러미",
    "TFT8_Augment_OxForceTrait" : "황소부대 심장",
    "TFT8_Augment_OxForceEmblem" : "황소부대 문장",
    "TFT8_Augment_AnnieSupport" : "불타는 영혼",
    "TFT8_Augment_RenegadeEmblem" : "무법자 문장",
    "TFT6_Augment_CelestialBlessing2" : "천상의 축복2",
    "TFT7_Augment_Preparation2" : "준비2",
    "TFT7_Augment_Preparation1" : "준비1",
    "TFT8_Augment_LeonaSupport" : "절정의 일식",
    "TFT6_Augment_TradeSector" : "교환의 장",
    "TFT7_Augment_BigFriend2" : "커다란 친구2",
    "TFT8_Augment_MordekaiserSupport" : "말살",
    "TFT6_Augment_TomeOfTraits1" : "고대의 기록 보관소1",
    "TFT6_Augment_TomeOfTraits2" : "고대의 기록 보관소2",
    "TFT6_Augment_Featherweights2" : "경량급2",
    "TFT6_Augment_Featherweights1" : "경량급1",
    "TFT8_Augment_SettSupport" : "재생형 보호막",
    "TFT8_Augment_JannaCarry" : "신속한 보도",
    "TFT6_Augment_MetabolicAccelerator" : "대사 촉진제",
    "TFT6_Augment_JeweledLotus" : "보석 연꽃",
    "TFT6_Augment_SecondWind2" : "재생의 바람2",
    "TFT6_Augment_SecondWind1" : "재생의 바람1",
    "TFT8_Augment_NunuSupport" : "퍼지는 웃음",
    "TFT6_Augment_Electrocharge2" : "고전압2",
    "TFT6_Augment_Electrocharge1" : "고전압1",
    "TFT8_Augment_MissFortuneSupport" : "총알은 비를 타고",
    "TFT8_Augment_ChannelerEmblem2" : "주문투척자 왕관",
    "TFT8_Augment_LeBlancGlitch" : "조준 보정",
    "TFT6_Augment_CelestialBlessing3" : "천상의 축복3",
    "TFT8_Augment_LeBlancSupport" : "거울 환영",
    "TFT6_Augment_RichGetRicher" : "부익부",
    "TFT6_Augment_ForceOfNature" : "신병",
    "TFT8_Augment_SonaSupport" : "암류",
    "TFT6_Augment_TriForce2" : "3에 깃든 힘2",
    "TFT6_Augment_TriForce1" : "3에 깃든 힘1",
    "TFT6_Augment_VerdantVeil" : "신록의 장막",
    "TFT8_Augment_RivenSupport" : "금의 환향",
    "TFT6_Augment_ClearMind" : "맑은 정신",
    "TFT7_Augment_UrfsGrabBag2" : "우르프의 꾸러미2",
    "TFT7_Augment_UrfsGrabBag1" : "우르프의 꾸러미1",
    "TFT8_Augment_NilahSupport" : "승리의 장막",
    "TFT6_Augment_RadiantRelics" : "찬란한 유물",
    "TFT8_Augment_AnimaSquadEmblem" : "동물특공대 문장",
    "TFT6_Augment_WoodlandCharm" : "숲의 부적",
    "TFT8_Augment_VayneSupport" : "한밤의 서곡",
    "TFT8_Augment_AceEmblem" : "에이스 문장",
    "TFT8_Augment_UndergroundTheTrait2" : "지하세계 영혼",
    "TFT7_Augment_LivingForge" : "간이 대장간",
    "TFT8_Augment_SejuaniSupport" : "산산조각",
    "TFT7_Augment_LuckyGloves" : "행운의 장갑",
    "TFT8_Augment_SorakaSupport" : "업그레이드: 광란",
    "TFT6_Augment_SlowAndSteady" : "진보의 행진",
    "TFT7_Augment_BirthdayPresents" : "생일 선물",
    "TFT8_Augment_ZedSupport" : "약자 멸시",
    "TFT6_Augment_GachaAddict" : "황금 티켓",
    "TFT8_Augment_AlistarBeefUp" : "괴수",
    "TFT6_Augment_GrandGambler" : "큰손",
    "TFT6_Augment_TradeSectorPlus" : "교환의 장+",
    "TFT8_Augment_HackerEmblem" : "해커 문장",
    "TFT8_Augment_ZoeDoubleTrouble" : "이중 방울",
    "TFT6_Augment_TrueTwos" : "곱빼기",
    "TFT8_Augment_KaisaStarCrossed" : "엇갈린 별",
    "TFT6_Augment_Ascension" : "초월",
    "TFT7_Augment_ClutteredMind" : "어수선한 마음",
    "TFT8_Augment_GenAETrait" : "기계유망주 심장",
    "TFT8_Augment_VelkozFrostburn" : "동상 불태우기",
    "TFT6_Augment_RichGetRicherPlus" : "부익부+",
    "TFT8_Augment_DuelistEmblem" : "결투가 문장",
    "TFT6_Augment_ThreesCompany" : "삼총사",
    "TFT8_Augment_AnimaSquadTrait" : "동물특공대 심장",
    "TFT8_Augment_JinxSupport" : "전부 터져라!",
    "TFT8_Augment_BrawlerEmblem" : "싸움꾼 문장",
    "TFT8_Augment_BrawlerEmblem2" : "싸움꾼 왕관",
    "TFT8_Augment_FioraSupport" : "황소의 활력",
    "TFT8_Augment_ThreatMaxHealth" : "위협 레벨: 최대",
    "TFT7_Augment_BandOfThieves1" : "도둑 무리1",
    "TFT6_Augment_BandOfThieves2" : "도둑 무리2",
    "TFT6_Augment_MeleeStarBlade2" : "나이프의 날2",
    "TFT6_Augment_MeleeStarBlade1" : "나이프의 날1",
    "TFT8_Augment_DuelistTrait" : "결투가 심장",
    "TFT8_Augment_EkkoSupport" : "시공간 붕괴",
    "TFT8_Augment_CamilleSupport" : "마법공학 응징",
    "TFT8_Augment_YasuoSupport" : "추방자의 기백",
    "TFT8_Augment_KayleCarry" : "거룩한 승천",
    "TFT8_Augment_HeartEmblem" : "선의 문장",
    "TFT8_Augment_DravenSupport" : "무자비한 칼날",
    "TFT8_Augment_DravenCarry" : "드레이븐의 리그",
    "TFT6_Augment_TargetDummies" : "허수아비 전선",
    "TFT8_Augment_SylasSupport" : "페트리사이트 사슬",
    "TFT8_Augment_YuumiSupport" : "슈우우웅!",
    "TFT6_Augment_ItemGrabBag1" : "아이템 꾸러미1",
    "TFT6_Augment_ItemGrabBag2" : "아이템 꾸러미2",
    "TFT8_Augment_SyndraSupport" : "예비전력 강화",
    "TFT6_Augment_LudensEcho2" : "루덴의 메아리2",
    "TFT6_Augment_LudensEcho1" : "루덴의 메아리1",
    "TFT8_Augment_SivirCarry" : "배달 팁",
    "TFT8_Augment_KaisaCarry" : "다중 사격",
    "TFT8_Augment_ChannelerEmblem" : "주문투척자 문장",
    "TFT8_Augment_ZoeSupport" : "한숨 잘 시간",
    "TFT6_Augment_MaxLevel10" : "레벨 업!"
        }
        
    return augments[name]

def korean(name, how):
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
    "TFT8_Kayle" : {
        "name" : "케일",
        "traits" : ["지하세계", "결투가"]
    },
    "TFT8_Poppy" : {
        "name" : "뽀삐",
        "traits" : ["기계유망주","엄호대"]
    },
    "TFT8_Galio" : {
        "name" : "갈리오",
        "traits" : ["민간인", "마스코트"]
    },
    "TFT8_Rell" : {
        "name" : "렐",
        "traits" : ["별 수호자","엄호대"]
    },
    "TFT8_Velkoz" : {
        "name" : "벨코즈",
        "traits" : ["위협"]
    },
    "TFT8_Nilah" : {
        "name": "닐라",
        "traits" : ["별 수호자", "결투가"]
    },
    "TFT8_Ashe" : {
        "name":"애쉬",
        "traits" : ["정찰단", "레이저단"]
    },
    "TFT8_Yasuo" : {
        "name":"야스오",
        "traits" : ["레이저단", "결투가"]
    },
    "TFT8_Senna" : {
        "name":"세나",
        "traits" : ["레이저단", "특등사수"]
    },
    "TFT8_Zed" : {
        "name":"제드",
        "traits" : ["결투가", "레이저단", "해커"]
    },
    "TFT8_Lulu" : {
        "name":"룰루",
        "traits" : ["선의", "기계유망주"]
    },
    "TFT8_Nunu" : {
        "name":"누누",
        "traits" : ["마스코트", "기계유망주"]
    },
    "TFT8_Yuumi" : {
        "name":"유미",
        "traits" : ["별 수호자", "선의","마스코트"]
    },
    "TFT8_Zoe" : {
        "name":"조이",
        "traits" : ["기계유망주","익살꾼","해커"]
    },
    "TFT8_Taliyah" : {
        "name":"탈리야",
        "traits" : ["별 수호자", "주문투척자"]
    },
    "TFT8_Sivir" : {
        "name":"시비르",
        "traits" : ["민간인", "특등사수"]
    },
    "TFT8_Gangplank" : {
        "name":"갱플랭크",
        "traits" : ["결투가","우세"]
    },
    "TFT8_WuKong" : {
        "name":"오공",  
        "traits" : ["메카: 프라임", "엄호대"]
    },
    "TFT8_Draven" : {
        "name":"드레이븐",
        "traits" : ["메카: 프라임", "에이스"]
    },
    "TFT8_Malphite" : {
        "name":"말파이트",
        "traits" : ["우세","마스코트"]
    },
    "TFT8_Nasus" : {
        "name":"나서스",
        "traits" : ["마스코트","동물특공대"]
    },
    "TFT8_Jinx" : {
        "name":"징크스",
        "traits" : ["동물특공대","익살꾼"]
    },
    "TFT8_Vayne" : {
        "name":"베인",
        "traits" : ["동물특공대","정찰단","결투가"]
    },
    "TFT8_MissFortune" : {
        "name":"미스포츈",
        "traits" : ["에이스","동물특공대"]
    },
    "TFT8_Chogath" : {
        "name":"초가스",
        "traits" : ["위협"]
    },
    "TFT8_Rammus" : {
        "name":"람머스",
        "traits" : ["위협"]
    },
    "TFT8_BelVeth" : {
        "name":"벨베스",
        "traits" : ["위협"]
    },
    "TFT8_AurelionSol" : {
        "name":"아우렐리온솔",
        "traits" : ["위협"]
    },
    "TFT8_Zac" : {
        "name":"자크",
        "traits" : ["위협"]
    },
    "TFT8_Mordekaiser" : {
        "name":"모데카이저",
        "traits" : ["에이스", "레이저단"]
    },
    "TFT8_Leblanc" : {
        "name":"르블랑",
        "traits" : ["자동방어체계", "해커","주문투척자"]
    },
    "TFT8_Sylas" : {
        "name":"사일러스",
        "traits" : ["동물특공대", "무법자"]
    },
    "TFT8_Camille" : {
        "name":"카밀",
        "traits" : ["자동방어체계","무법자"]
    },
    "TFT8_Ezreal" : {
        "name":"이즈리얼",
        "traits" : ["지하세계","정찰단"]
    },
    "TFT8_Sona" : {
        "name":"소나",
        "traits" : ["지하세계", "선의", "주문투척자"]
    },
    "TFT8_Ekko" : {
        "name":"에코",
        "traits" : ["별 수호자", "방패대","익살꾼"]
    },
    "TFT8_Sett" : {
        "name":"세트",
        "traits" : ["메카: 프라임", "엄호대"]
    },
    "TFT8_Janna" : {
        "name":"잔나",
        "traits" : ["민간인","기상캐스터","주문투척자"]
    },
    "TFT8_Urgot" : {
        "name":"우르곳",
        "traits" : ["위협"]
    },
    "TFT8_Syndra" : {
        "name":"신드라",
        "traits" : ["선의","별 수호자"]
    },
    "TFT8_Fiddlesticks" : {
        "name":"피들스틱",
        "traits" : ["위협","타락"]
    },
    "TFT8_Blitzcrank" : {
        "name":"블리츠크랭크",
        "traits" : ["자동방어체계", "싸움꾼"]
    },
    "TFT8_Renekton" : {
        "name":"레넥톤",
        "traits" : ["싸움꾼","레이저단"]
    },
    "TFT8_Vi" : {
        "name":"바이",
        "traits" : ["싸움꾼", "방패대","지하세계"]
    },
    "TFT8_LeeSin" : {
        "name":"리신",
        "traits" : ["선의","싸움꾼"]
    },
    "TFT8_Riven" : {
        "name":"리븐",
        "traits" : ["동물특공대", "싸움꾼", "엄호대"]
    },
    "TFT8_Jax" : {
        "name":"잭스",
        "traits" : ["메카: 프라임", "싸움꾼"]
    },
    "TFT8_Sejuani" : {
        "name":"세주아니",
        "traits" : ["싸움꾼", "레이저단"]
    },
    "TFT8_Soraka" : {
        "name":"소라카",
        "traits" : ["자동방어체계", "선의"]
    },
    "TFT8_Talon" : {
        "name":"탈론",
        "traits" : ["황소부대", "무법자"]
    },
    "TFT8_Fiora" : {
        "name":"피오라",
        "traits" : ["황소부대", "결투가"]
    },
    "TFT8_Annie" : {
        "name":"애니",
        "traits" : ["황소부대", "기계유망주", "주문투척자"]
    },
    "TFT8_Alistar" : {
        "name":"알리스타",
        "traits" : ["황소부대", "마스코트", "방패대"]
    },
    "TFT8_Viego" : {
        "name":"비에고",
        "traits" : ["황소부대", "무법자"]
    },
    "TFT8_Samira" : {
        "name":"사미라",
        "traits" : ["에이스", "지하세계","특등사수"]
    },
    "TFT8_Aphelios" : {
        "name":"아펠리오스",
        "traits" : ["황소부대", "특등사수", "병기고"]
    },
    "TFT8_Leona" : {
        "name":"레오나",
        "traits" : ["메카: 프라임", "무법자", "방패대"]
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
        url = f"http://gganbuback1.pythonanywhere.com/static/profileicon/{obj.profileIconID}.png"
        return url

class ChampionSerializer(serializers.ModelSerializer) :

    name = serializers.SerializerMethodField('getKname')
    items = serializers.SerializerMethodField('get5items')
    tier = serializers.SerializerMethodField('getTierData')
    bigimg = serializers.SerializerMethodField('getbigimg')
    smallimg = serializers.SerializerMethodField('getsmallimg')

    class Meta :
        model = Champion
        fields = ('name', 'items', 'rarity', 'tier', 'bigimg', 'smallimg')
    
    def getKname(self,obj):
            
        #tft정보 (한글로 바꾸기)
        with open('tft-champion.json', 'r', encoding='UTF8') as f:
            championName = json.load(f)["data"]
        return championName[obj.name]["name"]

    def get5items(self, obj):
         #tft정보 (한글로 바꾸기)
        with open('tft-item.json', 'r', encoding='UTF8') as f:
            itemName = json.load(f)["data"]
        i = dict()
        for item in Counter(obj.items).most_common(5):
            if (item[0])[:17] == "TFT8_EmblemItems/":
                i[itemName[item[0]]["name"]] = f"http://127.0.0.1:8000/static/tft-item/{(item[0])[17:]}.png"
            else:
                i[itemName[item[0]]["name"]] = f"http://127.0.0.1:8000/static/tft-item/{item[0]}.png"
            
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
        url = f"http://127.0.0.1:8000/static/tft-champion/{obj.name}.TFT_Set8.png"
        return url


    def getsmallimg(self, obj):
        url = f"http://127.0.0.1:8000/static/tft-hero-augment/{obj.name}.TFT_Set8.png"
        return url

class OneDeckSerializer(serializers.ModelSerializer) :
    augments = serializers.SerializerMethodField('getKaug')
    units = serializers.SerializerMethodField('getKunit')
    core = serializers.SerializerMethodField('getKcore')

    class Meta :
        model = Deck
        fields = ('winrate', 'windefencerate', 'avgplace', 'units', 'core', 'augments', 'traits')

    
    def getKaug(self, obj):
        augments = []
        for a in obj.augments:
            augments.append(EtoK(a))
        return augments
    
    def getKunit(self, obj):
        units = []
        for a in obj.units:
            units.append(korean(a,"name"))
        return units

    def getKcore(self, obj):
        cores = []
        for c in obj.core:
            cores.append(korean(c,"name"))
        return cores

    def getmosttier(self, obj):
        return Counter(obj.tier).most_common(1)[0][0]

