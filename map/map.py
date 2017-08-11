import folium
import pandas

volcanoes = pandas.read_csv("volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])

def color_producer(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'


# Create map object
map = folium.Map(location=[38.451478, -98.453700], zoom_start=5, tiles="Mapbox Bright")

## Layers
featGroupV = folium.FeatureGroup(name="Volcanoes")

# Add Markers
for lt, ln, el in zip(lat, lon, elev):
    featGroupV.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el) + "m", color="grey", fill_color=color_producer(el), fill_opacity=0.7, radius=8))

featGroupP = folium.FeatureGroup(name="Population")
# Add polygons
featGroupP.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig'), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(featGroupV)
map.add_child(featGroupP)
map.add_child(folium.LayerControl())
map.save("map.html")
