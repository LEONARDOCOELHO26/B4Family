import sqlite3 as sql
conn  =  sql.connect ( 'bank_database.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()


table = """ CREATE TABLE user (
            ID integer PRIMARY KEY,
            full_name char(255),
            user char(255),
            number int(11),
            password char(255)

        ); """
conn.execute(table)