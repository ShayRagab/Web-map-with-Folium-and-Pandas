import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
# location[latitude and longitude]
lat = list(data["LAT"])
lon = list(data["LON"])
# the popup info
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 2000:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[34.073636, -118.400195], zoom_start=6, tiles="Mapbox Bright")

# Volcanoes marker layer
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    # for circle marker
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ " m", fill_color=color_producer(el), color='grey', fill_opacity=0.7))

# Population layer
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000
else "orange" if x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("webmap.html")
