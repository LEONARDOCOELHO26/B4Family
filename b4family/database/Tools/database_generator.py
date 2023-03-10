import sqlite3 as sql
conn  =  sql.connect ( 'database.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()



table = """ CREATE TABLE bank_user (
            ID integer PRIMARY KEY,
            full_name char(255),
            saldo float,
            user char(255),
            number int(11),
            password char(255),
            conta char(5)
        ); """
conn.execute(table)
table = """ CREATE TABLE transacoes (
            conta char(7),
            data char(50),
            descricao char(50),
            valor float
        ); """
conn.execute(table)


'''conn  =  sql.connect ( 'extrato.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()


table = """ CREATE TABLE transacoes (
            conta char(7),
            data char(50),
            descricao char(50),
            valor float
        ); """
conn.execute(table)'''