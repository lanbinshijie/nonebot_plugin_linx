from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11 import Bot, Event

import random
from datetime import date

def luck_simple(num):
    if num < 18:
        return '%Worst8%'
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
    await jrrp.finish(message=Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{lucknum}/100，为"{luck_simple(lucknum)}"'))
