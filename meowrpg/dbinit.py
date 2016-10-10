import sqlite3

async def dbinit():
    dbconn = sqlite3.connect("rpg.db")
    dbcursor = dbconn.cursor()
    dbcursor.executescript("""CREATE TABLE Players(
        ID TEXT PRIMARY KEY,
        HP INTEGER NOT NULL,
        SAN INTEGER NOT NULL,
        ATK INTEGER NOT NULL,
        DEF INTEGER NOT NULL,
        MATK INTEGER NOT NULL,
        MDEF INTEGER NOT NULL,
        Classes INTEGER,
        Weapons INTEGER,
        Armors INTEGER,
        Charms INTEGER,
        Process INTEGER NOT NULL);""")
    dbcursor.executescript("""CREATE TABLE Classes(
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        EXTATK INTEGER,
        EXTDEF INTEGER,
        EXTMATK INTEGER,
        EXTMDEF INTEGER);
    INSERT INTO Classes VALUES (1, '學長的形狀', 5, 4, -1, -2);
    INSERT INTO Classes VALUES (2, '三十歲沒女友', -2, -1, 6, 2);
    INSERT INTO Classes VALUES (3, '巨乳狂熱教徒', 9, -1, 0, -2);
    INSERT INTO Classes VALUES (4, '肥宅', 2, 1, 2, 2);
    INSERT INTO Classes VALUES (5, '自宅警備員', -1, 6, 0, 1);
    INSERT INTO Classes VALUES (6, '％貓愛貓人士', 0, 3, 0, 3);
    INSERT INTO Classes VALUES (7, '蘿莉守護者', 0, 0, 1, 5);
    INSERT INTO Classes VALUES (8, '爆裂魔導士', -2, -2, 12, -2);
    INSERT INTO Classes VALUES (9, '我的王之力RR', 4, 0, 4, 0);
    """)
    dbcursor.executescript("""CREATE TABLE Weapons(
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        QUA INTEGER,
        EXTATK INTEGER,
        EXTDEF INTEGER,
        EXTMATK INTEGER,
        EXTMDEF INTEGER);
    INSERT INTO Weapons VALUES (1, '木劍', 1, 2, 0, 0, 0);
    INSERT INTO Weapons VALUES (2, '木杖', 1, 0, 0, 2, 0);
    INSERT INTO Weapons VALUES (3, '鐵劍', 2, 3, 1, 0, 0);
    INSERT INTO Weapons VALUES (4, '禁忌權杖', 2, -1, 0, 5, 2);
    INSERT INTO Weapons VALUES (5, '貴金屬劍', 3, 5, 1, -1, 1);
    INSERT INTO Weapons VALUES (6, '貓靈杖', 3, 0, 0, 5, 1);
    INSERT INTO Weapons VALUES (7, '喵洽之劍', 4, 9, 0, -1, 0);
    INSERT INTO Weapons VALUES (8, '喵洽之杖', 4, -1, 0, 8, 1);
    """)
    dbcursor.executescript("""CREATE TABLE Armors(
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        QUA INTEGER,
        EXTATK INTEGER,
        EXTDEF INTEGER,
        EXTMATK INTEGER,
        EXTMDEF INTEGER);
    INSERT INTO Armors VALUES (1, '木盾', 1, 0, 2, 0, 0);
    INSERT INTO Armors VALUES (2, '布袍', 1, 0, 0, 1, 1);
    INSERT INTO Armors VALUES (3, '鐵盾', 2, 0, 4, 0, 0);
    INSERT INTO Armors VALUES (4, '古代術袍', 2, 0, 1, 0, 3);
    INSERT INTO Armors VALUES (5, '精緻鎧甲', 3, 0, 4, 0, 2);
    INSERT INTO Armors VALUES (6, '貓靈袍', 3, 0, 2, 1, 3);
    INSERT INTO Armors VALUES (7, '喵洽之鎧', 4, 0, 6, 0, 2);
    INSERT INTO Armors VALUES (8, '喵洽之袍', 4, 0, 3, 0, 5);
    """)
    dbcursor.executescript("""CREATE TABLE Charms(
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        QUA INTEGER,
        EXTATK INTEGER,
        EXTDEF INTEGER,
        EXTMATK INTEGER,
        EXTMDEF INTEGER);
    INSERT INTO Charms VALUES (1, '初心護符', 1, 0, 1, 0, 1);
    INSERT INTO Charms VALUES (2, '封印墜飾', 2, 0, 2, 0, 2);
    INSERT INTO Charms VALUES (3, '貓靈結晶', 3, 1, 2, 1, 3);
    INSERT INTO Charms VALUES (4, '喵妮之心', 4, 3, 3, 2, 2);
    """)
    dbcursor.close()
    dbconn.commit()
    dbconn.close()
