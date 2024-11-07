import main
import requests
import user
import json


def topLogin(data: list) -> None:
    endpoint = main.webhook_discord_url

    rewards: user.Rewards = data[0]
    login: user.Login = data[1]
    bonus: user.Bonus or str = data[2]
    with open('login.json', 'r', encoding='utf-8')as f:
        data22 = json.load(f)

        name1 = data22['cache']['replaced']['userGame'][0]['name']
        fpids1 = data22['cache']['replaced']['userGame'][0]['friendCode']
    
    messageBonus = ''
    nl = '\n'

    if bonus != "No Bonus":
        messageBonus += f"__{bonus.message}__{nl}```{nl.join(bonus.items)}```"

        if bonus.bonus_name != None:
            messageBonus += f"{nl}__{bonus.bonus_name}__{nl}{bonus.bonus_detail}{nl}```{nl.join(bonus.bonus_camp_items)}```"

        messageBonus += "\n"

    jsonData = {
        "content": None,
        "embeds": [
            {
                "title": "FGO Daily Bonus - " + main.fate_region,
                "description": f"Scheluded Login Fate/Grand Order.\n\n{messageBonus}",
                "color": 563455,
                "fields": [
                    {
                        "name": "name",
                        "value": f"{name1}",
                        "inline": True
                    },
                    {
                        "name": "Friend ID",
                        "value": f"{fpids1}",
                        "inline": True
                    },
                    {
                        "name": "Level",
                        "value": f"{rewards.level}",
                        "inline": True
                    },
                    {
                        "name": "Tickets",
                        "value": f"{rewards.ticket}",
                        "inline": True
                    },                    
                    {
                        "name": "Saint Quartz",
                        "value": f"{rewards.stone}",
                        "inline": True
                    },
                    {
                        "name": "IDK",
                        "value": f"{rewards.sqf01}",
                        "inline": True
                    },
                    {
                        "name": "goldenfruit",
                        "value": f"{rewards.goldenfruit}",
                        "inline": True
                    },
                    {
                        "name": "silverfruit",
                        "value": f"{rewards.silverfruit}",
                        "inline": True
                    },
                    {
                        "name": "bronzefruit",
                        "value": f"{rewards.bronzefruit}",
                        "inline": True
                    },
                    {
                        "name": "bluebronzefruit",
                        "value": f"{rewards.bluebronzefruit}",
                        "inline": True
                    },
                    {
                        "name": "bluebronzesapling",
                        "value": f"{rewards.bluebronzesapling}",
                        "inline": True
                    },
                    {
                        "name": "Login Days",
                        "value": f"{login.login_days}",
                        "inline": True
                    },
                    {
                        "name": "Total Days",
                        "value": f"{login.total_days}",
                        "inline": True
                    },
                    {
                        "name": "pureprism",
                        "value": f"{rewards.pureprism}",
                        "inline": True
                    },
                    {
                        "name": "Total Friend Points",
                        "value": f"{login.total_fp}",
                        "inline": True
                    },
                    {
                        "name": "Friend Points Today",
                        "value": f"+{login.add_fp}",
                        "inline": True
                    },
                    {
                        "name": "AP Max",
                        "value": f"{login.remaining_ap}",
                        "inline": True
                    },
                    {
                        "name": "holygrail",
                        "value": f"{rewards.holygrail}",
                        "inline": True
                    },
                    
                ],
                "thumbnail": {
                    "url": "https://www.fate-go.jp/manga_fgo/images/commnet_chara01.png"
                }
            }
        ],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    requests.post(endpoint, json=jsonData, headers=headers)


def shop(item: str, quantity: str) -> None:
    endpoint = main.webhook_discord_url
    
    jsonData = {
        "content": None,
        "embeds": [
            {
                "title": "FGO Daily Bonus - " + main.fate_region,
                "description": f"Purchase successful.",
                "color": 5814783,
                "fields": [
                    {
                        "name": f"Store",
                        "value": f"consume {40 * quantity}Ap Purchase {quantity}x {item}",
                        "inline": False
                    }
                ],
                "thumbnail": {
                    "url": "https://www.fate-go.jp/manga_fgo2/images/commnet_chara10.png"
                }
            }
        ],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    requests.post(endpoint, json=jsonData, headers=headers)


def drawFP(servants, missions) -> None:
    endpoint = main.webhook_discord_url

    message_mission = ""
    message_servant = ""
    
    if (len(servants) > 0):
        servants_atlas = requests.get(
            f"https://api.atlasacademy.io/export/JP/basic_svt_lang_en.json").json()

        svt_dict = {svt["id"]: svt for svt in servants_atlas}

        for servant in servants:
            objectId = servant.objectId
            if objectId in svt_dict:
                svt = svt_dict[objectId]
                message_servant += f"`{svt['name']}` "
            else:
                continue

    if(len(missions) > 0):
        for mission in missions:
            message_mission += f"__{mission.message}__\n{mission.progressTo}/{mission.condition}\n"

    jsonData = {
        "content": None,
        "embeds": [
            {
                "title": "FGO Daily Bonus - " + main.fate_region,
                "description": f"Scheluded Friend Point Fate/Grand Order.\n\n{message_mission}",
                "color": 5750876,
                "fields": [
                    {
                        "name": "Gacha Result",
                        "value": f"{message_servant}",
                        "inline": False
                    }
                ],
                "thumbnail": {
                    "url": "https://www.fate-go.jp/manga_fgo/images/commnet_chara02_rv.png"
                }
            }
        ],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    requests.post(endpoint, json=jsonData, headers=headers)


def LTO_Gacha(servants) -> None:
    endpoint = main.webhook_discord_url

    message_servant = ""
    
    if (len(servants) > 0):
        servants_atlas = requests.get(
            f"https://api.atlasacademy.io/export/JP/basic_svt_lang_en.json").json()

        svt_dict = {svt["id"]: svt for svt in servants_atlas}

        for servant in servants:
            objectId = servant.objectId
            if objectId in svt_dict:
                svt = svt_dict[objectId]
                message_servant += f"`{svt['name']}` "
            else:
                continue

    jsonData = {
        "content": None,
        "embeds": [
            {
                "title": "FGO Limited Gacha - " + main.fate_region,
                "description": f"Scheluded Limit Friend Point Fate/Grand Order.",
                "color": 16711680,
                "fields": [
                    {
                        "name": "Gacha Result",
                        "value": f"{message_servant}",
                        "inline": False
                    }
                ],
                "thumbnail": {
                    "url": "https://www.fate-go.jp/manga_fgo/images/commnet_chara02_rv.png"
                }
            }
        ],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    requests.post(endpoint, json=jsonData, headers=headers)


def Present(name, namegift, object_id_count) -> None:
    endpoint = main.webhook_discord_url
    
    jsonData = {
        "content": None,
        "embeds": [
            {
                "title": "FGO Exchange - JP",
                "description": "Successful",
                "color": 8388736,
                "fields": [
                    {
                        "name": f"{name}",
                        "value": f"{namegift} x{object_id_count}",
                        "inline": False
                    }
                ],
                "thumbnail": {
                    "url": "https://www.fate-go.jp/manga_fgo2/images/commnet_chara06.png"
                }
            }
        ],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    requests.post(endpoint, json=jsonData, headers=headers)







