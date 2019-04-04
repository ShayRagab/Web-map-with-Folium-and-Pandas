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

fg=folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    # for circle marker
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ " m", fill_color=color_producer(el), color='grey', fill_opacity=0.7))

map.add_child(fg)

map.save("webmap.html")
