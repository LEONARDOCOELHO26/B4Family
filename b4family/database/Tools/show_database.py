import sqlite3 as sql
conn  =  sql.connect ( 'database.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()



print('\nColumns in bank_user table:')
data=cursor.execute('''SELECT * FROM bank_user''')
for column in data.description:
    print(column)
                
print('\nData in user table:')
data=cursor.execute('''SELECT * FROM bank_user''')
for row in data:
    print(row)