import sqlite3 as sql
conn  =  sql.connect ( 'nome_do_banco_de_dados.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()



print('\nColumns in bank_user table:')
data=cursor.execute('''SELECT * FROM numeros_gerados''')
for column in data.description:
    print(column)
                
print('\nData in user table:')
data=cursor.execute('''SELECT * FROM numeros_gerados''')
for row in data:
    print(row)