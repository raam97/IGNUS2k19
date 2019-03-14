import sqlite3

conn = sqlite3.connect("ignus.db")


def Team():
    conn.execute('''CREATE TABLE REGISTER(USER_NAME TEXT(50) NOT NULL ,
                 EMAIL VARCHAR(50)  NOT NULL,
                 COLLEGE VARCHAR(50),
                MOBILE VARCHAR(50),
                 EVENT VARCHAR(50))''')
    
Team()
conn.close()
