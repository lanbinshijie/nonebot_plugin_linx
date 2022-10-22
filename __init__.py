import os
from nonebot import get_driver
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message

global_config = get_driver().config

# 程序代码
import requests

GLOBAL_LINX_DATA_PATH = "LinxData"
GLOBAL_LINX_DATA_REALPATH = os.getcwd()+r"\LinxData"

API_APP_ID = ""
API_APP_SECRET = ""
API_APP_GATHER = (API_APP_ID, API_APP_SECRET)
# 文件夹目录
def checkDataDir():
    if not os.path.exists(GLOBAL_LINX_DATA_PATH):
        os.mkdir(GLOBAL_LINX_DATA_PATH)
def checkSettings():
    try:
        with open("LinxData\\apiSettings.txt","r",encoding="utf-8-sig") as f:
            qwq = f.read().split("\n")
            return (qwq[0],qwq[1])
    except FileNotFoundError as e:
        print("配置文件未找到，程序将无法连接")
        return ("","")
def checkKeys():
    return len(API_APP_ID) == 0

def addMenu(text):
    text += "==============\n"
    text += "Linx机器人\n"
    text += "1.输入.help查看帮助\n"
    return text

# == 初始化代码 =============
checkDataDir()
API_APP_GATHER = checkSettings()
API_APP_ID, API_APP_SECRET = API_APP_GATHER


# 一言
dailyWord = on_command("dailyword",aliases={"每日一句","一句话",}, priority=1)
@dailyWord.handle()
async def _():
    DAILY_TEXT_NUM = 8
    if checkKeys():
        await dailyWord.send(Message("【错误】APPID和APPSECRET未配置，请联系管理员"))
        return
    DAILY_SOURCE = f"http://www.mxnzp.com/api/daily_word/recommend?count={DAILY_TEXT_NUM}&app_id={API_APP_ID}&app_secret={API_APP_SECRET}"
    res = requests.get(DAILY_SOURCE)
    res_text = res.json()
    code = res_text["code"]
    resd = "[CQ:face,id=74]每日一言[CQ:face,id=74]\n"
    resd += "==============\n"
    if code == 1:
        # 拼接文字
        tmp = 1
        for text in res_text["data"]:
            resd += str(tmp) + ". " +text["content"]
            resd += " ——"+text["author"] if len(text["author"]) != 0 else " ——匿名"
            resd += "\n"
            tmp += 1
        resd = addMenu(resd)
    elif code == 101:
        resd = "【警告】你好，你触发了请求告警，请求速度过快！"
    elif code == 0:
        resd = "【错误】API key&pass 配置错误，请联系管理员"
    else:
        resd = "未知错误，抱歉"

    await dailyWord.send(Message(resd))

        
help = on_command("help",aliases={"help",}, priority=1)
@help.handle()
async def _():
    res = requests.get("http://api.imfurry.cn/linx/notice.php")
    res_text = res.json()
    text = res_text["notice"]
    message = "[CQ:face,id=54] Linx 群聊管家 [CQ:face,id=54]" + "\n"
    message += "==================" + "\n"
    message += "[CQ:face,id=55] 版本：Linx 1.0" + "\n"
    message += "[CQ:face,id=66] 1. help - 查看帮助" + "\n"
    message += "[CQ:face,id=66] 2. 每日一句 - 获取名言" + "\n"
    message += "[CQ:face,id=72] 3. 作者：Lanbin" + "\n"
    message += "[CQ:face,id=69] 4. GitHub开源插件" + "\n"
    message += "==================" + "\n"
    message += "[CQ:face,id=113] 最新公告 [CQ:face,id=113]" + "\n"
    message += text + "\n"
    await help.send(Message(message))
