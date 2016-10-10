import sqlite3

itemsdb = "rpg.db"

def get_qua_itemlist(item_category, qua):
    dbconn = sqlite3.connect(itemsdb)
    dbcursor = dbconn.cursor()
    dbcursor.execute("SELECT ID, Name FROM "+item_category+" WHERE QUA = ?",(qua,))
    itemlist = dbcursor.fetchall()
    dbcursor.close()
    dbconn.commit()
    dbconn.close()
    return itemlist
