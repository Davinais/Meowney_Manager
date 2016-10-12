import discord
import random
from .players import Players
from .items import get_qua_itemlist

async def onjourney(client, caller, channel):
    player = Players(caller)
    result = random.randint(1,10)
    process = player.get_process()
    journey_num = int(process/10)
    statsname = ["ATK", "DEF", "MATK", "MDEF"]
    statsnameCht = ("物攻", "物防", "術傷", "術抗")
    itemcat = ["Weapons", "Armors", "Charms"]
    randstats = random.randint(0, 3)
    randitem = random.randint(0, 2)
    if result == 1:
        await client.send_message(channel, "```看來，似乎無驚無險地通過了此處呢！```\n{0}`無事發生，前進下一節`".format(player.mention))
    #需要喵幣處理
    elif result == 2:
        await client.send_message(channel, "`賢狼赫蘿：`\n```哎呀！真是稀客哪！咱差點就要打烊前往他處囉。\n"
        "我們旅人呀，在各地留下的不是留戀，而是美好的回憶。\n"
        "汝呀，願意用幾枚喵幣來跟咱測試自己的商業眼光嗎？```\n"
        "{0}`輸入0=離開，輸入1~10=跟赫蘿進行一次性普通博弈，輸入50=向赫蘿購買一樣隨機裝備`".format(player.mention))

        def betcoincheck(m):
            opt = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "50")
            return True if m.content in opt else False

        betcoin = await client.wait_for_message(timeout = 60.0, author = player.user, check = betcoincheck)
        betcoinamount = 0

        def coincheck(m):
                opt = ("正", "反")
                return True if m.content in opt else False

        if not betcoin is None:
            betcoinamount = int(betcoin.content)
        if betcoinamount == 0:
            await client.send_message(channel, "```呵...看來小夥子無法當個有氣度的商人哪！```")
        elif betcoinamount == 50:
            await client.send_message(channel, "```汝雖是人類卻居然這麼有膽識呢！```\n:arrow_right:{0}請猜測硬幣為 `正` 或 `反` 面，直接輸入即可".format(player.mention))
            coinflip = await client.wait_for_message(timeout = 60.0, author = player.user, check = coincheck)
            if coinflip is None:
                await client.send_message(channel, "```呵...看來小夥子不夠果斷，無法當個有氣度的商人哪！```")
            else:
                flipresult = ["正", "反"]
                random.shuffle(flipresult)
                if coinflip.content == flipresult[0]:
                    itemlist = get_qua_itemlist(itemcat[randitem], 4)
                    random.shuffle(itemlist)
                    await client.send_message(channel, "```唉呀！咱今天真是遇到好對手啦！雖然輸給了你卻很開心哪！給，「{0}」```".format(itemlist[0][1]))
                    player.items_equip(itemcat[randitem], itemlist[0][0])
                else:
                    await client.send_message(channel, "```呵...看來小夥子還是不及咱賢狼哪！再多多旅行磨練磨練吧！```")
        else:
            await client.send_message(channel, ":arrow_right:{0}請猜測硬幣為 `正` 或 `反` 面，直接輸入即可".format(player.mention))
            coinflip = await client.wait_for_message(timeout = 60.0, author = player.user, check = coincheck)
            if coinflip is None:
                await client.send_message(channel, "```呵...看來小夥子不夠果斷，無法當個有氣度的商人哪！```")
            else:
                flipresult = ["正", "反"]
                random.shuffle(flipresult)
                if coinflip.content == flipresult[0]:
                    await client.send_message(channel, "```唉呀！居然有辦法贏我呢，汝真是個天生的商人呀！那麼就給你[{0}喵幣]跟<{1}+2>作為賭酬吧！```".format(betcoinamount*2, statsnameCht[randstats]))
                    player.stats_change(statsname[randstats], 2)
                else:
                    await client.send_message(channel, "```呵...看來小夥子還是不及咱賢狼哪！再多多旅行磨練磨練吧！```")
        await client.send_message(channel, "```那麼再會啦，賢狼可不適合在同一處待太久哪。```\n"
        "{0}`前進下一節`".format(player.mention))
    player.process_set(process+5)
