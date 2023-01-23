import sqlite3 as sql
conn  =  sql.connect ( 'testedatabase.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()

table = """ CREATE TABLE bank (
            user char(255)
            passoword(255) 
            saldo float
        ); """
teste = cursor.execute('''SELECT * from bank''')
user = input("user")
password = input("password")
saldo = 0
statement = f"SELECT * from bank WHERE user='{user}' AND password = '{password}';"
cur.execute(statement)
saldo = (teste)
print (saldo)
if not cur.fetchone():
            print("Login failed")
else:
            print("Bem-vindo de volta",user,saldo)

    
        # Display columns
print('\nColumns in bank_user table:')
data=cursor.execute('''SELECT * FROM bank''')
for column in data.description:
        print(column[0])
        
    # Display data
print('\nData in bank table:')
cursor.execute('''SELECT saldo FROM bank where user='{user}';''')
data= cursor.fetchall()
print(data)


conn . close ()   
#else:
#print ("Operação falhou")

if (conn):
    conn.close()
    print("\nThe SQLite connection is closed.")