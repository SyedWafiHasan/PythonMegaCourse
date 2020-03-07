import folium
import pandas
# TODO : Exercise 113
def colour_producer(elevation):
	if elevation < 1000:
		return 'blue'
	elif 1000 <= elevation < 2000:
		return 'green'
	elif 2000 <= elevation < 3000:
		return 'orange'
	else:
		return 'red'

map = folium.Map(location=[37.0902, -95.7129], zoom_start=5)

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

fg = folium.FeatureGroup("My Group")

for lt, ln, n, el in zip(lat, lon, name, elev):
	s = n + "\n" + str(el) +" metres"
	fg.add_child(folium.Marker(location=[lt, ln], popup=s, icon=folium.Icon(colour_producer(int(el)))))   

map.add_child(fg)

map.save("Map 1.html")