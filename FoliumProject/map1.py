import folium
import pandas

def colour_producer(elevation):
	if elevation < 1000:
		return 'blue'
	elif 1000 <= elevation < 2000:
		return 'green'
	elif 2000 <= elevation < 3000:
		return 'orange'
	else:
		return 'red'

map = folium.Map(location=[37.0902, -95.7129], zoom_start=5, tiles='cartodbpositron')

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

fgv = folium.FeatureGroup("Volcanoes")

for lt, ln, n, el in zip(lat, lon, name, elev):
	s = n + "\n" + str(el) +" metres"
	fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, fill_color=colour_producer(el), popup=s, color='grey', fill_opacity=0.5))   

fgp = folium.FeatureGroup("Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
	style_function=lambda x:{'fillColor' : 'green' if x['properties']['POP2005'] < 100000000
	else 'orange' if 100000000 <= x['properties']['POP2005'] < 1000000000
	else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map 1.html")