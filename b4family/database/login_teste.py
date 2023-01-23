import twilio
from twilio.rest import Client
import keys
client = Client(keys.account_sid, keys.auth_token)

import sqlite3 as sql
conn  =  sql.connect ( 'bank_database.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()
user = input("user")
password = input("password")
statement = f"SELECT * from user WHERE user='{user}' AND password = '{password}';"
cur.execute(statement)
if not cur.fetchone():
    print("Login failed")
else:
    print("Login successful")
    targetuser = user
    rows = cursor.execute(
        "SELECT number FROM user WHERE user = ?",
    (targetuser,),
    ).fetchall()
    number = str(rows)
    phone_number = "+55" + number[2:13]
    print(rows)
    print(phone_number)

message_sing_in = client.messages.create(
    body="a sua conta do B4Family Foi a acessada",
    from_=keys.twilio_number,
    to=phone_number)



 