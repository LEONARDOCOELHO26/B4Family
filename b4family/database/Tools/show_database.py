import sqlite3 as sql
conn  =  sql.connect ( 'extrato.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()



print('\nColumns in bank_user table:')
data=cursor.execute('''SELECT * FROM transacoes''')
for column in data.description:
    print(column[0])
                
print('\nData in user table:')
data=cursor.execute('''SELECT * FROM transacoes''')
for row in data:
    print(row)