# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:38:33 2018

@author: varun
"""

import folium
import pandas as pd
# create map object
#map = folium.Map(location=[38.1271,39.9131])
#print(map)

map = folium.Map(location=[48.1271,-73.9131],tiles='Stamen Terrain',zoom_start=3)
df =pd.read_csv('volcano.txt',sep=',')

for lat,lon,place,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    folium.Marker(location=[lat,lon],icon =folium.Icon(color='red' if elev in range(0,2000) else 'blue' )).add_to(map)
    
#print(map.save("test.html"))


print(map.save("test2.html"))