import sqlite3

playersdb = "rpg.db"

class Players:
    user = None
    id = ""
    name = ""
    mention = None
    __stats = {"HP":0, "SAN":0 ,"ATK":0, "DEF":0, "MATK":0, "MDEF":0}
    __class_id = 0
    __items = {"Weapons":None, "Armors":None, "Charms":None}
    __process = 0
    __need_update = False
    __update_script = ""

    def __init__(self, player):
        dbconn = sqlite3.connect(playersdb)
        dbcursor = dbconn.cursor()
        dbcursor.execute("SELECT * FROM Players WHERE ID = ?",(player.id,))
        #playerstats: ID, HP, SAN, ATK ,DEF, MATK, MDEF, Classes, Weapons, Armors, Charms, Process
        playerdata = dbcursor.fetchone()
        dbcursor.close()
        dbconn.close()
        print(playerdata)
        if not playerdata is None:
            self.user = player
            self.mention = player.mention
            self.id = player.id
            self.name = player.name
            statsname = ("HP", "SAN", "ATK", "DEF", "MATK", "MDEF")
            statstemp = 1
            for statsset in statsname:
                self.__stats[statsset] = playerdata[statstemp]
                statstemp += 1
            self.__class_id = playerdata[7]
            self.__items["Weapons"] = playerdata[8]
            self.__items["Armors"] = playerdata[9]
            self.__items["Charms"] = playerdata[10]
            self.__process = playerdata[11]

    def __del__(self):
        if self.__need_update:
            dbconn = sqlite3.connect(playersdb)
            dbcursor = dbconn.cursor()
            dbcursor.executescript(self.__update_script)
            dbcursor.close()
            dbconn.commit()
            dbconn.close()
            self.__need_update = False

    def get_stats(self):
        return self.__stats

    def get_class_id(self):
        return self.__class_id

    def get_items(self):
        return self.__items

    def get_process(self):
        return self.__process

    def stats_change(self, stats_name, amount):
        self.__stats[stats_name] += amount
        self.__update_script += "UPDATE Players SET " + stats_name + " = " + str(self.__stats[stats_name]) + " WHERE ID = " + self.id + ";\n"
        self.__need_update = True

    def stats_set(self, stats_name, set_number):
        self.__stats[stats_name] = set_number
        self.__update_script += "UPDATE Players SET " + stats_name + " = " + str(self.__stats[stats_name]) + " WHERE ID = " + self.id + ";\n"
        self.__need_update = True

    def class_set(self, class_id):
        self.__class_id = class_id
        self.__update_script += "UPDATE Players SET Classes = " + str(self.__class_id) + " WHERE ID = " + self.id + ";\n"
        self.__need_update = True

    def items_equip(self, item_category, item_id):
        self.__items[item_category] = item_id
        self.__update_script += "UPDATE Players SET " + item_category + " = " + str(self.__items[item_category]) + " WHERE ID = " + self.id + ";\n"
        self.__need_update = True

    def process_set(self, process):
        self.__process = process
        self.__update_script += "UPDATE Players SET Process = " + str(self.__process) + " WHERE ID = " + self.id + ";\n"
        self.__need_update = True
