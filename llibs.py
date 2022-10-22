
def compile(text: str, keywords) -> str:
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