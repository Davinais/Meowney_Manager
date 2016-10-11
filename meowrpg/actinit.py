import discord
import random
from .players import *
from .items import get_qua_itemlist
from .classes import get_classlist

async def actinit(player, client, channel):
    await client.send_message(channel, "```1000年前，廢文洗板橫行世間，這時候喵洽勇者勇敢地挑戰廢文大魔神，在經過一翻激烈的戰鬥後終於將其封印！\n"
    "孰料千年的封印卻因為無聊肥宅狂發廢文的舉動而引起共鳴，封印之石產生了裂痕，廢文大魔神即將甦醒！\n"
    "喵洽Meow_Chat此時正遭受廢文軍團的襲擊，喵洽的勇士呀！請幫助喵妮恢復喵洽的秩序好喵？```\n"
    ":arrow_right:{0}是否願意幫助喵妮討伐廢文大魔神？\n\n"
    ":one:為了喵妮的笑容，請交給我吧！\n"
    ":two:什麼！廢文大魔神復活！？呵呵...這不正是我輩宅宅的宿願嗎！！".format(player.mention))

    def gscheck(m):
        opt = ("1", "2")
        return True if m.content in opt else False

    gs = await client.wait_for_message(timeout = 60.0, author = player, check = gscheck)
    gschoice = 2
    if not gs is None:
        gschoice = int(gs.content)
    if gschoice == 1:
        classlist = get_classlist()
        await client.send_message(channel, "```太感謝了！喵洽的勇士呀！請在出發前選擇你嚮往的職業吧！```\n"
        ":arrow_right:{0}請選擇職業\n\n"
        ":one:{1}\n"
        ":two:{2}\n"
        ":three:{3}\n"
        ":four:{4}\n"
        ":five:{5}\n"
        ":six:{6}\n"
        ":seven:{7}\n"
        ":eight:{8}\n"
        ":nine:{9}\n".format(player.mention, classlist[0][1], classlist[1][1], classlist[2][1], classlist[3][1],
        classlist[4][1], classlist[5][1], classlist[6][1], classlist[7][1], classlist[8][1]))

        def classescheck(m):
            opt = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            return True if m.content in opt else False

        classeschoice = await client.wait_for_message(timeout = 60.0, author = player, check = classescheck)
        if classeschoice is None:
            classes = random.randint(1, 9)
            await client.send_message(channel, "{0}，都挑了這麼久還想不到，那喵妮我就幫你挑一個職業好了\n"
            "從現在起，你就是**{1}**了！".format(player.mention, classlist[classes-1][1]))
            class_set(player.id, classes)
        else:
            class_set(player.id, int(classeschoice.content))
        await client.send_message(channel, "```馬上就要出發了呢！喵妮要提醒{0}，每位喵洽勇士只有3生命值跟3精神值哦。遊戲中可利用指令$rpg check 查看目前角色狀態。\n"
        "戰鬥結果如果是<完全勝利>的話會有額外獎勵；\n"
        "若只有<勉強勝利>的話，生命值或精神值會受到損傷；\n"
        "若是<殘念敗北>的話就必須等到明天恢復元氣才能再度挑戰了...```\n"
        "那麼{1}還有想詢問的事情嗎？\n\n"
        ":one:喵妮！你等我，等討伐完魔王之後我們就...\n"
        ":two:嘿嘿！喵妮，出發前先讓我爽一下吧！！(變身成癡漢攻擊喵妮)\n"
        ":three:先別管廢文大魔王了，喵妮有聽過安麗嗎？\n"
        ":four:是嗎...那麼，我出發了！".format(player.name, player.mention))

        def starteventcheck(m):
            opt = ("1", "2", "3", "4")
            return True if m.content in opt else False

        startevent = await client.wait_for_message(timeout = 60.0, author = player, check = starteventcheck)
        starteventchoice = 4
        starteventresult = 3
        if not startevent is None:
            starteventchoice = int(startevent.content)
            starteventresult = random.randint(1, 3)
        statsname = ["ATK", "DEF", "MATK", "MDEF"]
        statsnameCht = ("物攻", "物防", "術傷", "術抗")
        itemcat = ["Weapons", "Armors", "Charms"]
        randstats = random.randint(0, 3)
        randitem = random.randint(0, 2)
        if starteventchoice == 1:
            if starteventresult == 1:
                await client.send_message(channel, "```嗯！我們就是最好的朋友了！```\n{0}`被喵妮發了卡，<{1}>+1`".format(player.mention, statsnameCht[randstats]))
                stats_change(player.id, statsname[randstats], 1)
            elif starteventresult == 2:
                await client.send_message(channel, "```是的哦！我們喵洽Meow_Chat到時就能恢復和平了呢！```\n{0}`受到了喵妮鼓勵，<{1}>+2`".format(player.mention, statsnameCht[randstats]))
                stats_change(player.id, statsname[randstats], 2)
            else:
                await client.send_message(channel, "```「我們...就...？」...```\n{0}`與喵妮產生了曖昧情愫，<{1}>-1`".format(player.mention, statsnameCht[randstats]))
                stats_change(player.id, statsname[randstats], -1)
        elif starteventchoice == 2:
            if starteventresult == 1:
                await client.send_message(channel, "```咦...！...不要！```\n`喵妮隨手拿起了身邊的折凳對`{0}`進行致命性的抵抗，<生命值>-1`".format(player.mention))
                stats_change(player.id, "HP", -1)
            elif starteventresult == 2:
                await client.send_message(channel, "```呢...處男都是這樣的嗎...很困擾呀...```\n{0}`受到了喵妮的諷刺而崩潰，<精神值>-1`".format(player.mention))
                stats_change(player.id, "SAN", -1)
            else:
                itemlist = get_qua_itemlist(itemcat[randitem], 2)
                random.shuffle(itemlist)
                await client.send_message(channel, "```呵呵...{0}真是個風趣的人呢！(推開)，當年的喵洽勇者似乎也是這麼風趣，看來{0}很適合穿戴他留下來的裝備唷！```\n{1}`獲得「{2}」，<{3}>+1`".format(player.name, player.mention, itemlist[0][1], statsnameCht[randstats]))
                items_equip(player.id, itemcat[randitem], itemlist[0][0])
                stats_change(player.id, statsname[randstats], 1)
        elif starteventchoice == 3:
            if starteventresult == 1:
                await client.send_message(channel, "```咦咦！原來{0}也是安麗的會員嗎？噗...喵妮這裏剛好有最新的產品DM唷！```\n{1}`受到了喵妮強制推銷，喵幣-3，<{2}>+2`".format(player.name, player.mention, statsnameCht[randstats]))
                stats_change(player.id, statsname[randstats], 2)
                takecmd = await client.send_message(channel, "$take {0} 3".format(player.mention))
                await asyncio.sleep(0.2)
                await client.delete_message(takecmd)
            elif starteventresult == 2:
                await client.send_message(channel, "```呢...安麗是什麼+.+```\n{0}`強制推銷安麗產品給喵妮，喵幣+3，<{1}>-1`".format(player.mention, statsnameCht[randstats]))
                stats_change(player.id, statsname[randstats], -1)
                awardcmd = await client.send_message(channel, "$award {0} 3".format(player.mention))
                await asyncio.sleep(0.2)
                await client.delete_message(awardcmd)
            else:
                await client.send_message(channel, "```現在不是討論這個的時候了啦！！```\n{0}`被催促著上路，<{1}>+1`".format(player.mention, statsnameCht[randstats]))
                stats_change(player.id, statsname[randstats], 1)
        else:
            if starteventresult == 1:
                await client.send_message(channel, "```真是個男子漢呢...{0}```\n{1}`受到了喵妮的敬仰，<{2}>+2`".format(player.name, player.mention, statsnameCht[randstats]))
                stats_change(player.id, statsname[randstats], 2)
            elif starteventresult == 2:
                itemlist = get_qua_itemlist(itemcat[randitem], 1)
                random.shuffle(itemlist)
                await client.send_message(channel, "```咦咦！...稍等呀！{0}，呼...差點忘了給您這個！```\n{1}`獲得「{2}」`".format(player.name, player.mention, itemlist[0][1]))
                items_equip(player.id, itemcat[randitem], itemlist[0][0])
            else:
                await client.send_message(channel, "```{0}...難道是個無情的人...？```\n{1}`因為讓喵妮落寞著臉，<精神值>-1`".format(player.name, player.mention))
                stats_change(player.id, "SAN", -1)
        process_set(player.id, 10)
    if gschoice == 2:
        await client.send_message(channel, "```{0}...難道是個無情的人...？就這麼不想要幫助喵妮嗎...```{1}`遊戲結束`".format(player.name, player.mention))
