import sqlite3

classesdb = "rpg.db"

def get_classlist():
    dbconn = sqlite3.connect(classesdb)
    dbcursor = dbconn.cursor()
    dbcursor.execute("SELECT ID, Name FROM Classes")
    classlist = dbcursor.fetchall()
    dbcursor.close()
    dbconn.close()
    return classlist
