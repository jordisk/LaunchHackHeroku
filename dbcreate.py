import sqlite3

conn = sqlite3.connect('rockets.db')

conn.execute('CREATE TABLE TBL_ROCKETS (ID INT PRIMARY KEY NOT NULL, VAR1 INT NOT NULL, VAR2 INT NOT NULL);')
conn.execute('CREATE TABLE TBL_MOTORS (ID INT PRIMARY KEY NOT NULL, VAR1 INT NOT NULL, VAR2 INT NOT NULL);')
conn.close()
