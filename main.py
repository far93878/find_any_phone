import phonenumbers
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
from phonenumbers import geocoder
import folium
from my_phone import number

pepnumber = phonenumbers.parse(number)
location =  geocoder.description_for_number(pepnumber, "en")
service_num = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_num, "en"))
print(location)
api_key = "1a0f74baf149451983297e6a515e17e0"
geocoder =OpenCageGeocode(api_key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results [0]['geometry']['lat']
lng = results [0]['geometry']['lng']
print(lat , lng)
my_map = folium.Map(location= [lat, lng] ,zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(my_map)
my_map.save("location.html")