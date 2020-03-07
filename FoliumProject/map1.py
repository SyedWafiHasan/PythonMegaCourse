import folium
import pandas
map = folium.Map(location=[26.8467, 80.9462], zoom_start=5)

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

fg = folium.FeatureGroup("My Group")

for lt, ln, n, el in zip(lat, lon, name, elev):
	s = n + "\n" + str(el) +" metres"
	fg.add_child(folium.Marker(location=[lt, ln], popup=s, icon=folium.Icon(color="red")))


map.add_child(fg)

map.save("Map 1.html")