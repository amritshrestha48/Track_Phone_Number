import phonenumbers
from phonenumbers import geocoder
#from test import number
import folium

key = "dca6db48284d4cd698e50cae1659d575"    #from opencage side

number = input("Enter the phone number with country code:")

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results [0]['geometry']['lat']
lng = results [0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(Location = [lat,lng], zoom_start = 9)
folium.Marker([lat,lng], popup = number_location). add_to(map_location)
map_location.save("mylocation.html")
