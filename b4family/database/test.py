import bcrypt 
password = str(input("input password: ")) 
password = password.encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)) 
print(hashed)
check = str(input("check password: ")) 

import sqlite3 as sql
conn  =  sql.connect ( 'teste_database.db' )
cursor  =  conn.cursor()
cur = conn.cursor()
user = input("user")
password = input("password")
statement = f"SELECT * from bank_user WHERE user='{user}' AND password = '{password}';"
cur.execute(statement)
if not cur.fetchone():
    print("Login failed")
else:
    print("Login successful")

check = check.encode('utf-8') 
if bcrypt.checkpw(check, hashed):
   print("login success")
else:
    print("incorrect password")
