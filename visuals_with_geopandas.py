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
    max_bounds=True,
    min_lat=min_lat,
    max_lat=max_lat,
    min_long=min_long,
    max_long=max_long)



for i in range (100):
    folium.Marker(
        location=(df['Latitude'].iloc[i], df['Longitude'].iloc[i]),
        tooltip=df['ID'].iloc[i],
        popup=f"Date: {df['Date'].iloc[i]} {df['Time'].iloc[i]}\n Magnitude: {df['Magnitude'].iloc[i]}"
    ).add_to(earth_map)




    


earth_map.save("visuals/earthquake.html")


print(df)
print(df.dtypes)