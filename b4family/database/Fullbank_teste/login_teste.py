import sqlite3 as sql
import os 
import twilio
import hashlib
from twilio.rest import Client
import keys
client = Client(keys.account_sid, keys.auth_token)

def clear_console():
    os.system('cls')
clear_console()

conn  =  sql.connect ( 'bank_database.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()
user = input("user: ")
password = input("password: ")
password = hashlib.sha256(password.encode()).hexdigest()
cur.execute(f"SELECT * from bank_user WHERE user='{user}' AND password='{password}'")
result = cursor.fetchone()
if not cur.fetchone():
    print("Login failed")
else:
            #localização e o horario
            import geocoder
            from geopy.geocoders import Nominatim
            import datetime
            g = geocoder.ip('me')
            now = datetime.datetime.now()
            geolocator = Nominatim(user_agent="geoapiExercises")
            def city_state_country(coord):
                location = geolocator.reverse(coord, exactly_one=True)
                address = location.raw["address"]
                city = address.get("city", )
                state = address.get('state', )
                country = address.get('country',)
                return city, state, country
            city_bad = str(city_state_country (g.latlng))
            bad_chars = ["(",")","'"]
            test_string = city_bad
            city = ''.join(map(lambda x: x if x not in bad_chars else '', test_string))
            print(city)
            time= f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
            #message
            targetuser = user
            rows = cursor.execute(
                "SELECT number FROM bank_user WHERE user = ?",
            (targetuser,),
            ).fetchall()
            number = str(rows)
            phone_number = "+55" + number[2:13]
            message_sing_in = client.messages.create(
            body=f"{user} a sua conta do B4Family Foi a acessada em {city} ás {time} ",
            from_=keys.twilio_number,
            to=phone_number)

            clear_console()
            cursor.execute(f"SELECT * from bank_user WHERE user='{user}' AND password='{password}'")
            result = cursor.fetchone()
            fullname = result[1]
            limite = 500
            extrato = ""
            numero_saques = 0
            LIMITE_SAQUES = 3



 