import twilio
from twilio.rest import Client
import keys
client = Client(keys.account_sid, keys.auth_token)



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

"""import sqlite3 as sql
conn  =  sql.connect ( 'bank_database.db' )
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
targetuser = user
rows = cursor.execute(
        "SELECT saldo FROM bank_user WHERE user = ?",
    (targetuser,),
    ).fetchall()"""
#number[2:13]
#number = str(rows)


phone_number = "+5541992483105"
#print(rows)
print(phone_number)
user = "leo"
message_sing_in = client.messages.create(
    body=f"{user} a sua conta do B4Family Foi a acessada em {city} ás {time} ",
    from_=keys.twilio_number,
    to=phone_number)



 