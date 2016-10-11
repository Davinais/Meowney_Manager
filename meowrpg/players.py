import sqlite3

playersdb = "rpg.db"

def get_all_playerstats(player_id):
    dbconn = sqlite3.connect(playersdb)
    dbcursor = dbconn.cursor()
    dbcursor.execute("SELECT * FROM Players WHERE ID = ?",(player_id,))
    playerstats = dbcursor.fetchone()
    dbcursor.close()
    dbconn.commit()
    dbconn.close()
    return playerstats

def stats_change(player_id, stats, amount):
    dbconn = sqlite3.connect(playersdb)
    dbcursor = dbconn.cursor()
    change = ""
    if amount >= 0:
        change = "+"+str(amount)
    else:
        change = str(amount)
    dbcursor.execute("UPDATE Players SET "+stats+" = "+stats+change+" WHERE ID = ?",(player_id,))
    dbcursor.close()
    dbconn.commit()
    dbconn.close()

def prop_set(player_id, prop_name, prop_content):
    dbconn = sqlite3.connect(playersdb)
    dbcursor = dbconn.cursor()
    dbcursor.execute("UPDATE Players SET "+prop_name+" = ? WHERE ID = ?",(prop_content, player_id))
    dbcursor.close()
    dbconn.commit()
    dbconn.close()

def class_set(player_id, class_id):
    prop_set(player_id, "Classes", class_id)

def items_equip(player_id, item_category, item_id):
    prop_set(player_id, item_category, item_id)

def process_set(player_id, process):
    prop_set(player_id, "Process", process)
