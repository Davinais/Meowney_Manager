import discord
import sqlite3
import os
from .calcext import calcext

async def checkstats(player, client, channel):
    dbinitial = False if os.path.exists("rpg.db") else True
    if dbinitial:
        await client.send_message(channel, "喵洽大冒險尚未開始喔，請輸入`$rpg`來成為第一位玩家吧！")
        return
    dbconn = sqlite3.connect("rpg.db")
    dbcursor = dbconn.cursor()
    dbcursor.execute('SELECT * FROM Players WHERE ID = ?',(player.id,))
    playerstats = dbcursor.fetchone()
    if playerstats is None:
        await client.send_message(channel, "{0}還不是喵洽大冒險的玩家喔，快輸入`$rpg`來開始這段旅程吧！".format(player.mention))
        return
    #playerstats: ID, HP, SAN, ATK ,DEF, MATK, MDEF, Classes, Weapons, Armors, Charms, Process
    if playerstats[7] is None:
        await client.send_message(channel, "{0}連職業都沒有選還敢來問狀態，哼！".format(player.mention))
        return
    playerext = {"ATK":0, "DEF":0, "MATK":0, "MDEF":0}
    #檢查職業
    dbcursor.execute('SELECT Name, EXTATK, EXTDEF, EXTMATK, EXTMDEF FROM Classes WHERE ID = ?',(playerstats[7],))
    playerclass = dbcursor.fetchone()
    classname = playerclass[0]
    playerext = await calcext(playerext, playerclass[1], playerclass[2], playerclass[3], playerclass[4])
    #檢查武器
    weapon_name = "<無>"
    if not playerstats[8] is None:
        dbcursor.execute('SELECT Name, EXTATK, EXTDEF, EXTMATK, EXTMDEF FROM Weapons WHERE ID = ?',(playerstats[8],))
        weapon = dbcursor.fetchone()
        weapon_name = weapon[0]
        playerext = await calcext(playerext, weapon[1], weapon[2], weapon[3], weapon[4])
    #檢查身體裝備
    armor_name = "<無>"
    if not playerstats[9] is None:
        dbcursor.execute('SELECT Name, EXTATK, EXTDEF, EXTMATK, EXTMDEF FROM Armors WHERE ID = ?',(playerstats[9],))
        armor = dbcursor.fetchone()
        armor_name = armor[0]
        playerext = await calcext(playerext, armor[1], armor[2], armor[3], armor[4])
    #檢查護符
    charm_name = "<無>"
    if not playerstats[10] is None:
        dbcursor.execute('SELECT Name, EXTATK, EXTDEF, EXTMATK, EXTMDEF FROM Charms WHERE ID = ?',(playerstats[10],))
        charm = dbcursor.fetchone()
        charm_name = charm[0]
        playerext = await calcext(playerext, charm[1], charm[2], charm[3], charm[4])
    #extstr:EXTATK, EXTDEF, EXTMATK, EXTMDEF
    extstr = await get_extstr(playerext)
    await client.send_message(channel, "{0}的喵洽大冒險：\n"
    "```職業： {1}\n"
    "生命值： {2}　　　　精神值： {3}\n"
    "物攻： {4}({5})　　　　物防： {6}({7})\n"
    "術傷： {8}({9})　　　　術防： {10}({11})\n\n"
    "增益武器： {12}\n"
    "身體裝備： {13}\n"
    "飾品　　： {14}```".format(player.mention, classname, str(playerstats[1]), str(playerstats[2]),
    str(playerstats[3]), extstr[0], str(playerstats[4]), extstr[1],
    str(playerstats[5]), extstr[2], str(playerstats[6]), extstr[3], 
    weapon_name, armor_name, charm_name))

async def get_extstr(playerext):
    extstr = []
    if playerext["ATK"] >= 0:
        extstr.append("+"+str(playerext["ATK"]))
    else:
        extstr.append(str(playerext["ATK"]))
    if playerext["DEF"] >= 0:
        extstr.append("+"+str(playerext["DEF"]))
    else:
        extstr.append(str(playerext["DEF"]))
    if playerext["MATK"] >= 0:
        extstr.append("+"+str(playerext["MATK"]))
    else:
        extstr.append(str(playerext["MATK"]))
    if playerext["MDEF"] >= 0:
        extstr.append("+"+str(playerext["MDEF"]))
    else:
        extstr.append(str(playerext["MDEF"]))
    return extstr
