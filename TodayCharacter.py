import os
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11 import Bot, Event


import random
from datetime import date

def compile(text: str) -> str:
    KEYWORDS_FOR_TODAYCHARACTER = {}
    if os.path.exists("LinxData\characterSettings.txt"):
        with open("LinxData\characterSettings.txt", "r",encoding="utf-8-sig") as f:
            reading = f.read()
        reading = reading.split("\n")
        for i in reading:
            tmp = i.split("=")
            KEYWORDS_FOR_TODAYCHARACTER[tmp[0]] = tmp[1]
    else:
        with open("LinxData\characterSettings.txt", "w",encoding="utf-8") as f:
            f.write("""
                %Best8%=大胸
                %Best7%=小胸
                %Best6%=看起来不错
                %Best5%=还可以吧
                %Best4%=末吉
                %Best3%=小吉
                %Best2%=吉
                %Best1%=大吉
            """)
        KEYWORDS_FOR_TODAYCHARACTER = {
            "%Best8%":"大胸",
            "%Best7%":"有点小凶",
            "%Best6%":"这不对劲",
            "%Best5%":"你不太行呀",
            "%Best4%":"末吉",
            "%Best3%":"小吉",
            "%Best2%":"吉",
            "%Best1%":"大吉",
        }
    content = text
    for key in KEYWORDS_FOR_TODAYCHARACTER.items():
        content = content.replace(key[0],key[1])
    return content

def luck_simple(num):
    if num < 18:
        return '%Best8%'
    elif num < 28:
        return '%Best7%'
    elif num < 38:
        return '%Best6%'
    elif num < 48:
        return '%Best5%'
    elif num < 60:
        return '%Best4%'
    elif num < 71:
        return '%Best3%'
    elif num < 90:
        return '%Best2%'
    else:
        return '%Best1%'

jrrp = on_command("jrrp",aliases={"jrrp","rp"})
@jrrp.handle()
async def _(bot: Bot, event: Event):
    rnd = random.Random()
    rnd.seed((int(date.today().strftime("%y%m%d")) * 45) * (int(event.get_user_id()) * 55))
    lucknum = 100 - rnd.randint(1, 100)
    print(event.get_user_id())
    await jrrp.finish(message=Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{lucknum}/100，为"{compile(luck_simple(lucknum))}"'))
