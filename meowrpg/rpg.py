import discord
import os
import sqlite3
from .dbinit import dbinit
from .actinit import actinit

async def rpg(client, message):
    player = message.author
    dbinitial = False if os.path.exists("rpg.db") else True
    if dbinitial:
        await dbinit()
    dbconn = sqlite3.connect("rpg.db")
    dbcursor = dbconn.cursor()
    dbcursor.execute('SELECT * FROM Players WHERE ID = ?',(player.id,))
    playerstats = dbcursor.fetchone()
    if playerstats is None:
        dbcursor.execute('INSERT INTO Players (ID, HP, SAN, ATK, DEF, MATK, MDEF, Process) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',(player.id, 3, 3, 2, 2, 2, 2, 0))
        dbcursor.execute('SELECT * FROM Players WHERE ID = ?',(player.id,))
        playerstats = dbcursor.fetchone()
    dbcursor.close()
    dbconn.commit()
    dbconn.close()
    #playerstats: ID, HP, SAN, ATK ,DEF, MATK, MDEF, Classes, Weapons, Armors, Charms, Process
    print(playerstats)
    if playerstats[11] == 0:
        await actinit(player, client, message.channel)
