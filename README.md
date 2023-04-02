# 깐부지지
>개발기간 : 2023.01 ~ 2023.02 <br><br>
## 배포주소
>프론트 서버 : https://wkdrhkdwls.github.io/doubleup/ <br>
>백엔드 서버 : http://gganbuback1.pythonanywhere.com/<br><br>
## 프로젝트 소개
> TFT게임의 더블업 모드의 통계를 분석하여 다양한 팀단위 덱 구성시 참고할 수 있는 정보를 제공합니다.<br><br>
> <img src = "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_back1/%EA%B9%90%EB%B6%80%EC%A7%80%EC%A7%80%20api%20list.jpg">
> <br>
> <br>
> 소환사 랭킹<br>
> ```JSON
> {
>    "updated_time": "2023년3월13일12시53분",
>    "data": [
>        {
>            "name": "더블업 끝판왕TV",
>            "profileIcon": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/profileicon/4275.png",
>            "tier": "CHALLENGER",
>            "LP": "2489 LP",
>            "winrate": "78.3%",
>            "game_num": 401,
>            "win": 314,
>            "lose": 87
>        },
>        {
>            "name": "HED MAYNER",
>            "profileIcon": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/profileicon/5645.png",
>            "tier": "CHALLENGER",
>            "LP": "1529 LP",
>            "winrate": "70.2%",
>            "game_num": 275,
>            "win": 193,
>            "lose": 82
>        },
>        {
>            "name": "lIIIllIllIlIIIl",
>            "profileIcon": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/profileicon/5645.png",
>            "tier": "CHALLENGER",
>            "LP": "1529 LP",
>            "winrate": "70.2%",
>            "game_num": 275,
>            "win": 193,
>            "lose": 82
>        },
> ```
> <br>
> <br>
> 챔피언 통계
> <br>
```JSON
{
    "updated_time": "2023년3월13일13시1분",
    "data": [
        {
            "name": "피들스틱",
            "items": {
                "이온 충격기": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_IonicSpark.png",
                "보석 건틀릿": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_JeweledGauntlet.png",
                "모렐로노미콘": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Morellonomicon.png",
                "대천사의 지팡이": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_ArchangelsStaff.png",
                "마법공학 총검": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_HextechGunblade.png"
            },
            "rarity": 6,
            "tier": {
                "1": "59.6%",
                "2": "40.1%",
                "3": "0.3%"
            },
            "bigimg": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-champion/TFT8_Fiddlesticks.TFT_Set8.png",
            "smallimg": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiddlesticks.TFT_Set8.png",
            "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/ChampionBackGround/Fiddlesticks.jpg"
        },
        {
            "name": "알리스타",
            "items": {
                "태양불꽃 망토": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_RedBuff.png",
                "즈롯 차원문": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_TitanicHydra.png",
                "도적의 장갑": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_ThiefsGloves.png",
                "워모그의 갑옷": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_WarmogsArmor.png",
                "침묵의 장막": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Shroud.png"
            },
            "rarity": 2,
            "tier": {
                "1": "16.3%",
                "2": "82.2%",
                "3": "1.6%"
            },
            "bigimg": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-champion/TFT8_Alistar.TFT_Set8.png",
            "smallimg": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Alistar.TFT_Set8.png",
            "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/ChampionBackGround/Alistar.jpg"
        },
        {
            "name": "우르곳",
            "items": {
                "도적의 장갑": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_ThiefsGloves.png",
                "쇼진의 창": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_SpearOfShojin.png",
                "스태틱의 단검": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_StatikkShiv.png",
                "최후의 속삭임": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png",
                "거인 학살자": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
            },
            "rarity": 6,
            "tier": {
                "1": "57.1%",
                "2": "42.2%",
                "3": "0.7%"
            },
            "bigimg": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-champion/TFT8_Urgot.TFT_Set8.png",
            "smallimg": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Urgot.TFT_Set8.png",
            "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/ChampionBackGround/Urgot.jpg"
        },
```
<br>
<br>
개인 덱 통계
<br>

```JSON
{
    "updated_time": "2023년3월13일13시4분",
    "data": [
        {
            "id": 203,
            "name": "민간인 특등사수",
            "traits": [
                {
                    "name": "민간인",
                    "count": 3,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/민간인.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "위협",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/위협.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "병기고",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/병기고.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "타락",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/타락.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "기상캐스터",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/기상캐스터.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "방패대",
                    "count": 3,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/방패대.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/silver.svg"
                },
                {
                    "name": "마스코트",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/마스코트.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "특등사수",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/특등사수.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "황소부대",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/황소부대.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                }
            ],
            "core": [
                {
                    "name": "에코",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Ekko.TFT_Set8.png",
                    "items": [
                        {
                            "name": "도적의 장갑",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_ThiefsGloves.png"
                        },
                        {
                            "name": "이온 충격기",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_IonicSpark.png"
                        },
                        {
                            "name": "덤불 조끼",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_BrambleVest.png"
                        }
                    ]
                },
                {
                    "name": "아펠리오스",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Aphelios.TFT_Set8.png",
                    "items": [
                        {
                            "name": "구인수의 격노검",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_GuinsoosRageblade.png"
                        },
                        {
                            "name": "거인 학살자",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
                        },
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        }
                    ]
                },
                {
                    "name": "피들스틱",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiddlesticks.TFT_Set8.png",
                    "items": [
                        {
                            "name": "이온 충격기",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_IonicSpark.png"
                        },
                        {
                            "name": "보석 건틀릿",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_JeweledGauntlet.png"
                        },
                        {
                            "name": "모렐로노미콘",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Morellonomicon.png"
                        }
                    ]
                }
            ],
            "units": [
                {
                    "name": "갈리오",
                    "cost": 1,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Galio.TFT_Set8.png"
                },
                {
                    "name": "시비르",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Sivir.TFT_Set8.png"
                },
                {
                    "name": "알리스타",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Alistar.TFT_Set8.png"
                },
                {
                    "name": "에코",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Ekko.TFT_Set8.png"
                },
                {
                    "name": "아펠리오스",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Aphelios.TFT_Set8.png"
                },
                {
                    "name": "피들스틱",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiddlesticks.TFT_Set8.png"
                },
                {
                    "name": "잔나",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Janna.TFT_Set8.png"
                },
                {
                    "name": "레오나",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Leona.TFT_Set8.png"
                },
                {
                    "name": "우르곳",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Urgot.TFT_Set8.png"
                }
            ],
            "augments": [
                {
                    "name": "레벨 업!",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/LevelUp3.png"
                },
                {
                    "name": "휴대용 대장간",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/PortableForge2.png"
                },
                {
                    "name": "권투 교습",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Vi.TFT_Set8.png"
                }
            ],
            "winrate": 41.2,
            "windefencerate": 67.1,
            "avgplace": 2.0
        },
        {
            "id": 209,
            "name": "6결투가 해커 제드",
            "traits": [
                {
                    "name": "결투가",
                    "count": 6,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/결투가.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "레이저단",
                    "count": 3,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/레이저단.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "해커",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/해커.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                }
            ],
            "core": [
                {
                    "name": "야스오",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Yasuo.TFT_Set8.png",
                    "items": [
                        {
                            "name": "강철의 솔라리 펜던트",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LocketOfTheIronSolari.png"
                        },
                        {
                            "name": "도적의 장갑",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_ThiefsGloves.png"
                        },
                        {
                            "name": "서풍",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Zephyr.png"
                        }
                    ]
                },
                {
                    "name": "닐라",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Nilah.TFT_Set8.png",
                    "items": [
                        {
                            "name": "강철의 솔라리 펜던트",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LocketOfTheIronSolari.png"
                        },
                        {
                            "name": "서풍",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Zephyr.png"
                        },
                        {
                            "name": "구원",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Redemption.png"
                        }
                    ]
                },
                {
                    "name": "베인",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Vayne.TFT_Set8.png",
                    "items": [
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        },
                        {
                            "name": "무한의 대검",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_InfinityEdge.png"
                        },
                        {
                            "name": "거인 학살자",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
                        }
                    ]
                },
                {
                    "name": "세주아니",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Sejuani.TFT_Set8.png",
                    "items": [
                        {
                            "name": "구원",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Redemption.png"
                        },
                        {
                            "name": "태양불꽃 망토",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_RedBuff.png"
                        },
                        {
                            "name": "모렐로노미콘",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Morellonomicon.png"
                        }
                    ]
                },
                {
                    "name": "제드",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Zed.TFT_Set8.png",
                    "items": [
                        {
                            "name": "밤의 끝자락",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_GuardianAngel.png"
                        },
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        },
                        {
                            "name": "루난의 허리케인",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_RunaansHurricane.png"
                        }
                    ]
                }
            ],
            "units": [
                {
                    "name": "갱플랭크",
                    "cost": 1,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Gangplank.TFT_Set8.png"
                },
                {
                    "name": "피오라",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiora.TFT_Set8.png"
                },
                {
                    "name": "야스오",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Yasuo.TFT_Set8.png"
                },
                {
                    "name": "르블랑",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Leblanc.TFT_Set8.png"
                },
                {
                    "name": "닐라",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Nilah.TFT_Set8.png"
                },
                {
                    "name": "베인",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Vayne.TFT_Set8.png"
                },
                {
                    "name": "세주아니",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Sejuani.TFT_Set8.png"
                },
                {
                    "name": "제드",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Zed.TFT_Set8.png"
                }
            ],
            "augments": [
                {
                    "name": "결투가 문장",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/Duelist-Crest.TFT_Set8.png"
                },
                {
                    "name": "사냥의 전율 II",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/ThrillHunt2.png"
                },
                {
                    "name": "약자 멸시",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Zed.TFT_Set8.png"
                }
            ],
            "winrate": 37.6,
            "windefencerate": 65.0,
            "avgplace": 2.1
        },
        {
            "id": 200,
            "name": "황소부대 비에고 아펠",
            "traits": [
                {
                    "name": "황소부대",
                    "count": 6,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/황소부대.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "무법자",
                    "count": 3,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/무법자.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "병기고",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/병기고.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "위협",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/위협.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "타락",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/타락.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "방패대",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/방패대.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "특등사수",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/특등사수.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "에이스",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/에이스.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                }
            ],
            "core": [
                {
                    "name": "애니",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Annie.TFT_Set8.png",
                    "items": [
                        {
                            "name": "가고일 돌갑옷",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_GargoyleStoneplate.png"
                        },
                        {
                            "name": "덤불 조끼",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_BrambleVest.png"
                        },
                        {
                            "name": "태양불꽃 망토",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_RedBuff.png"
                        }
                    ]
                },
                {
                    "name": "사미라",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Samira.TFT_Set8.png",
                    "items": [
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        },
                        {
                            "name": "마법공학 총검",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_HextechGunblade.png"
                        },
                        {
                            "name": "거인 학살자",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
                        }
                    ]
                },
                {
                    "name": "비에고",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Viego.TFT_Set8.png",
                    "items": [
                        {
                            "name": "보석 건틀릿",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_JeweledGauntlet.png"
                        },
                        {
                            "name": "이온 충격기",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_IonicSpark.png"
                        },
                        {
                            "name": "피바라기",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Bloodthirster.png"
                        }
                    ]
                },
                {
                    "name": "아펠리오스",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Aphelios.TFT_Set8.png",
                    "items": [
                        {
                            "name": "구인수의 격노검",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_GuinsoosRageblade.png"
                        },
                        {
                            "name": "거인 학살자",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
                        },
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        }
                    ]
                }
            ],
            "units": [
                {
                    "name": "탈론",
                    "cost": 1,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Talon.TFT_Set8.png"
                },
                {
                    "name": "애니",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Annie.TFT_Set8.png"
                },
                {
                    "name": "피오라",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiora.TFT_Set8.png"
                },
                {
                    "name": "알리스타",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Alistar.TFT_Set8.png"
                },
                {
                    "name": "사미라",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Samira.TFT_Set8.png"
                },
                {
                    "name": "비에고",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Viego.TFT_Set8.png"
                },
                {
                    "name": "아펠리오스",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Aphelios.TFT_Set8.png"
                },
                {
                    "name": "피들스틱",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiddlesticks.TFT_Set8.png"
                },
                {
                    "name": "레오나",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Leona.TFT_Set8.png"
                }
            ],
            "augments": [
                {
                    "name": "황소부대 문장",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/Ox-Force-Crest.TFT_Set8.png"
                },
                {
                    "name": "황소부대 심장",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/Ox-Force-Heart.TFT_Set8.png"
                },
                {
                    "name": "공범",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Viego.TFT_Set8.png"
                }
            ],
            "winrate": 36.5,
            "windefencerate": 67.2,
            "avgplace": 2.1
        },
```

<br>
<br>
깐부 덱 통계
<br>

```JSON
{
    "updated_time": "2023년3월13일13시4분",
    "data": [
        {
            "id": 203,
            "name": "민간인 특등사수",
            "traits": [
                {
                    "name": "민간인",
                    "count": 3,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/민간인.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "위협",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/위협.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "병기고",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/병기고.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "타락",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/타락.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "기상캐스터",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/기상캐스터.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "방패대",
                    "count": 3,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/방패대.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/silver.svg"
                },
                {
                    "name": "마스코트",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/마스코트.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "특등사수",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/특등사수.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "황소부대",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/황소부대.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                }
            ],
            "core": [
                {
                    "name": "에코",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Ekko.TFT_Set8.png",
                    "items": [
                        {
                            "name": "도적의 장갑",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_ThiefsGloves.png"
                        },
                        {
                            "name": "이온 충격기",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_IonicSpark.png"
                        },
                        {
                            "name": "덤불 조끼",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_BrambleVest.png"
                        }
                    ]
                },
                {
                    "name": "아펠리오스",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Aphelios.TFT_Set8.png",
                    "items": [
                        {
                            "name": "구인수의 격노검",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_GuinsoosRageblade.png"
                        },
                        {
                            "name": "거인 학살자",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
                        },
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        }
                    ]
                },
                {
                    "name": "피들스틱",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiddlesticks.TFT_Set8.png",
                    "items": [
                        {
                            "name": "이온 충격기",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_IonicSpark.png"
                        },
                        {
                            "name": "보석 건틀릿",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_JeweledGauntlet.png"
                        },
                        {
                            "name": "모렐로노미콘",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Morellonomicon.png"
                        }
                    ]
                }
            ],
            "units": [
                {
                    "name": "갈리오",
                    "cost": 1,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Galio.TFT_Set8.png"
                },
                {
                    "name": "시비르",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Sivir.TFT_Set8.png"
                },
                {
                    "name": "알리스타",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Alistar.TFT_Set8.png"
                },
                {
                    "name": "에코",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Ekko.TFT_Set8.png"
                },
                {
                    "name": "아펠리오스",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Aphelios.TFT_Set8.png"
                },
                {
                    "name": "피들스틱",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiddlesticks.TFT_Set8.png"
                },
                {
                    "name": "잔나",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Janna.TFT_Set8.png"
                },
                {
                    "name": "레오나",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Leona.TFT_Set8.png"
                },
                {
                    "name": "우르곳",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Urgot.TFT_Set8.png"
                }
            ],
            "augments": [
                {
                    "name": "레벨 업!",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/LevelUp3.png"
                },
                {
                    "name": "휴대용 대장간",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/PortableForge2.png"
                },
                {
                    "name": "권투 교습",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Vi.TFT_Set8.png"
                }
            ],
            "otherdeckwin": [
                {
                    "deck_id": 197,
                    "winrate": 72.7,
                    "windefencerate": 90.9,
                    "avgplace": 1.4
                },
                {
                    "deck_id": 205,
                    "winrate": 58.3,
                    "windefencerate": 91.7,
                    "avgplace": 1.5
                },
                {
                    "deck_id": 204,
                    "winrate": 45.0,
                    "windefencerate": 70.0,
                    "avgplace": 2.0
                }
            ],
            "otherdeckwindef": [
                {
                    "deck_id": 205,
                    "winrate": 58.3,
                    "windefencerate": 91.7,
                    "avgplace": 1.5
                },
                {
                    "deck_id": 197,
                    "winrate": 72.7,
                    "windefencerate": 90.9,
                    "avgplace": 1.4
                },
                {
                    "deck_id": 204,
                    "winrate": 45.0,
                    "windefencerate": 70.0,
                    "avgplace": 2.0
                }
            ],
            "otherdeckavg": [
                {
                    "deck_id": 197,
                    "winrate": 72.7,
                    "windefencerate": 90.9,
                    "avgplace": 1.4
                },
                {
                    "deck_id": 205,
                    "winrate": 58.3,
                    "windefencerate": 91.7,
                    "avgplace": 1.5
                },
                {
                    "deck_id": 204,
                    "winrate": 45.0,
                    "windefencerate": 70.0,
                    "avgplace": 2.0
                }
            ]
        },
        {
            "id": 209,
            "name": "6결투가 해커 제드",
            "traits": [
                {
                    "name": "결투가",
                    "count": 6,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/결투가.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "레이저단",
                    "count": 3,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/레이저단.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "해커",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/해커.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                }
            ],
            "core": [
                {
                    "name": "야스오",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Yasuo.TFT_Set8.png",
                    "items": [
                        {
                            "name": "강철의 솔라리 펜던트",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LocketOfTheIronSolari.png"
                        },
                        {
                            "name": "도적의 장갑",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_ThiefsGloves.png"
                        },
                        {
                            "name": "서풍",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Zephyr.png"
                        }
                    ]
                },
                {
                    "name": "닐라",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Nilah.TFT_Set8.png",
                    "items": [
                        {
                            "name": "강철의 솔라리 펜던트",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LocketOfTheIronSolari.png"
                        },
                        {
                            "name": "서풍",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Zephyr.png"
                        },
                        {
                            "name": "구원",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Redemption.png"
                        }
                    ]
                },
                {
                    "name": "베인",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Vayne.TFT_Set8.png",
                    "items": [
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        },
                        {
                            "name": "무한의 대검",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_InfinityEdge.png"
                        },
                        {
                            "name": "거인 학살자",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
                        }
                    ]
                },
                {
                    "name": "세주아니",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Sejuani.TFT_Set8.png",
                    "items": [
                        {
                            "name": "구원",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Redemption.png"
                        },
                        {
                            "name": "태양불꽃 망토",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_RedBuff.png"
                        },
                        {
                            "name": "모렐로노미콘",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Morellonomicon.png"
                        }
                    ]
                },
                {
                    "name": "제드",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Zed.TFT_Set8.png",
                    "items": [
                        {
                            "name": "밤의 끝자락",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_GuardianAngel.png"
                        },
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        },
                        {
                            "name": "루난의 허리케인",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_RunaansHurricane.png"
                        }
                    ]
                }
            ],
            "units": [
                {
                    "name": "갱플랭크",
                    "cost": 1,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Gangplank.TFT_Set8.png"
                },
                {
                    "name": "피오라",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiora.TFT_Set8.png"
                },
                {
                    "name": "야스오",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Yasuo.TFT_Set8.png"
                },
                {
                    "name": "르블랑",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Leblanc.TFT_Set8.png"
                },
                {
                    "name": "닐라",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Nilah.TFT_Set8.png"
                },
                {
                    "name": "베인",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Vayne.TFT_Set8.png"
                },
                {
                    "name": "세주아니",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Sejuani.TFT_Set8.png"
                },
                {
                    "name": "제드",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Zed.TFT_Set8.png"
                }
            ],
            "augments": [
                {
                    "name": "결투가 문장",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/Duelist-Crest.TFT_Set8.png"
                },
                {
                    "name": "사냥의 전율 II",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/ThrillHunt2.png"
                },
                {
                    "name": "약자 멸시",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Zed.TFT_Set8.png"
                }
            ],
            "otherdeckwin": [
                {
                    "deck_id": 193,
                    "winrate": 46.2,
                    "windefencerate": 74.1,
                    "avgplace": 1.9
                },
                {
                    "deck_id": 200,
                    "winrate": 42.9,
                    "windefencerate": 75.0,
                    "avgplace": 2.0
                },
                {
                    "deck_id": 188,
                    "winrate": 42.5,
                    "windefencerate": 62.5,
                    "avgplace": 2.0
                }
            ],
            "otherdeckwindef": [
                {
                    "deck_id": 200,
                    "winrate": 42.9,
                    "windefencerate": 75.0,
                    "avgplace": 2.0
                },
                {
                    "deck_id": 193,
                    "winrate": 46.2,
                    "windefencerate": 74.1,
                    "avgplace": 1.9
                },
                {
                    "deck_id": 214,
                    "winrate": 10.0,
                    "windefencerate": 70.0,
                    "avgplace": 2.4
                }
            ],
            "otherdeckavg": [
                {
                    "deck_id": 193,
                    "winrate": 46.2,
                    "windefencerate": 74.1,
                    "avgplace": 1.9
                },
                {
                    "deck_id": 188,
                    "winrate": 42.5,
                    "windefencerate": 62.5,
                    "avgplace": 2.0
                },
                {
                    "deck_id": 200,
                    "winrate": 42.9,
                    "windefencerate": 75.0,
                    "avgplace": 2.0
                }
            ]
        },
        {
            "id": 200,
            "name": "황소부대 비에고 아펠",
            "traits": [
                {
                    "name": "황소부대",
                    "count": 6,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/황소부대.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "무법자",
                    "count": 3,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/무법자.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "병기고",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/병기고.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "위협",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/위협.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "타락",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/타락.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/gold.svg"
                },
                {
                    "name": "방패대",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/방패대.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "특등사수",
                    "count": 2,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/특등사수.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                },
                {
                    "name": "에이스",
                    "count": 1,
                    "img": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/에이스.svg",
                    "bgimg": "https://cdn.jsdelivr.net/gh/gganbuGG/gganbu_front/src/images/Synergy/Tile/bronze.svg"
                }
            ],
            "core": [
                {
                    "name": "애니",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Annie.TFT_Set8.png",
                    "items": [
                        {
                            "name": "가고일 돌갑옷",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_GargoyleStoneplate.png"
                        },
                        {
                            "name": "덤불 조끼",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_BrambleVest.png"
                        },
                        {
                            "name": "태양불꽃 망토",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_RedBuff.png"
                        }
                    ]
                },
                {
                    "name": "사미라",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Samira.TFT_Set8.png",
                    "items": [
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        },
                        {
                            "name": "마법공학 총검",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_HextechGunblade.png"
                        },
                        {
                            "name": "거인 학살자",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
                        }
                    ]
                },
                {
                    "name": "비에고",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Viego.TFT_Set8.png",
                    "items": [
                        {
                            "name": "보석 건틀릿",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_JeweledGauntlet.png"
                        },
                        {
                            "name": "이온 충격기",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_IonicSpark.png"
                        },
                        {
                            "name": "피바라기",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_Bloodthirster.png"
                        }
                    ]
                },
                {
                    "name": "아펠리오스",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Aphelios.TFT_Set8.png",
                    "items": [
                        {
                            "name": "구인수의 격노검",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_GuinsoosRageblade.png"
                        },
                        {
                            "name": "거인 학살자",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_MadredsBloodrazor.png"
                        },
                        {
                            "name": "최후의 속삭임",
                            "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-item/TFT_Item_LastWhisper.png"
                        }
                    ]
                }
            ],
            "units": [
                {
                    "name": "탈론",
                    "cost": 1,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Talon.TFT_Set8.png"
                },
                {
                    "name": "애니",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Annie.TFT_Set8.png"
                },
                {
                    "name": "피오라",
                    "cost": 2,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiora.TFT_Set8.png"
                },
                {
                    "name": "알리스타",
                    "cost": 3,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Alistar.TFT_Set8.png"
                },
                {
                    "name": "사미라",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Samira.TFT_Set8.png"
                },
                {
                    "name": "비에고",
                    "cost": 4,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Viego.TFT_Set8.png"
                },
                {
                    "name": "아펠리오스",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Aphelios.TFT_Set8.png"
                },
                {
                    "name": "피들스틱",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Fiddlesticks.TFT_Set8.png"
                },
                {
                    "name": "레오나",
                    "cost": 5,
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Leona.TFT_Set8.png"
                }
            ],
            "augments": [
                {
                    "name": "황소부대 문장",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/Ox-Force-Crest.TFT_Set8.png"
                },
                {
                    "name": "황소부대 심장",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-augment/Ox-Force-Heart.TFT_Set8.png"
                },
                {
                    "name": "공범",
                    "img": "http://ddragon.leagueoflegends.com/cdn/13.5.1/img/tft-hero-augment/TFT8_Viego.TFT_Set8.png"
                }
            ],
            "otherdeckwin": [
                {
                    "deck_id": 209,
                    "winrate": 61.1,
                    "windefencerate": 83.3,
                    "avgplace": 1.6
                },
                {
                    "deck_id": 205,
                    "winrate": 50.0,
                    "windefencerate": 80.0,
                    "avgplace": 1.8
                },
                {
                    "deck_id": 201,
                    "winrate": 50.0,
                    "windefencerate": 71.4,
                    "avgplace": 1.9
                }
            ],
            "otherdeckwindef": [
                {
                    "deck_id": 209,
                    "winrate": 61.1,
                    "windefencerate": 83.3,
                    "avgplace": 1.6
                },
                {
                    "deck_id": 205,
                    "winrate": 50.0,
                    "windefencerate": 80.0,
                    "avgplace": 1.8
                },
                {
                    "deck_id": 201,
                    "winrate": 50.0,
                    "windefencerate": 71.4,
                    "avgplace": 1.9
                }
            ],
            "otherdeckavg": [
                {
                    "deck_id": 209,
                    "winrate": 61.1,
                    "windefencerate": 83.3,
                    "avgplace": 1.6
                },
                {
                    "deck_id": 205,
                    "winrate": 50.0,
                    "windefencerate": 80.0,
                    "avgplace": 1.8
                },
                {
                    "deck_id": 201,
                    "winrate": 50.0,
                    "windefencerate": 71.4,
                    "avgplace": 1.9
                }
            ]
        },
```
## 사용 툴
><img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
><img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
><img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">
