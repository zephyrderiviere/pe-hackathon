from common import*

import geopandas
import folium


#To limit the map at the point of interest
min_lat = df['Latitude'].min()
min_long = df['Longitude'].min()
max_lat = df['Latitude'].max()
max_long = df['Longitude'].max()

earth_map = folium.Map(
    location=(0, 0), 
    zoom_start=3,
    max_bounds=False,
    min_lat=-100,
    max_lat=100,
    min_long=-200,
    max_long=200)

from folium.plugins import MarkerCluster
clusterList = {i: MarkerCluster(name = f"cluster n°{i}", tooltip=f"cluster n°{i}").add_to(earth_map) for i in df.GeoGroup.unique()}

for i in range (len(df)):
    folium.Marker(
        location=(df['Latitude'].iloc[i], df['Longitude'].iloc[i]),
        tooltip=df['ID'].iloc[i],
        popup=f"Date: {df['Date'].iloc[i]} {df['Date'].iloc[i].time}\n Magnitude: {df['Magnitude'].iloc[i]}"
    ).add_to(clusterList[df["GeoGroup"].iloc[i]])




    


earth_map.save("visuals/earthquake.html")


print(df)
print(df.dtypes)