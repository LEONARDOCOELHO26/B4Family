import geocoder
from geopy.geocoders import Nominatim
g = geocoder.ip('me')

from geopy.geocoders import Nominatim
import datetime
now = datetime.datetime.now()
geolocator = Nominatim(user_agent="geoapiExercises")
def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return city, state, country
print(city_state_country(g.latlng))
print(now.day,"/",now.month,"/",now.year,now.hour,":",now.minute)


