#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:16:22 2020

@author: qtangzhu
"""


import seaborn as sns
import pandas as pd
import folium
import folium.plugins as plugins
import webbrowser

df = pd.read_csv('../MapData/kc_house_data.csv', parse_dates=['date'])

# =============================================================================
# print(df.shape)
print(df.dtypes)
# print(df.columns)
# print(df['lat'].describe())
# =============================================================================


m = folium.Map([df['lat'].mean(), df['long'].mean()], zoom_start=12)

fmarker = folium.Marker(location = [df['lat'].mean(), df['long'].mean()], 
              popup='Centre Point', 
              icon=folium.Icon(color='red',icon='info-sign'))
fmarker.add_to(m)

m_cluster= plugins.MarkerCluster().add_to(m)


counter = 1000
for idx, data in df.iterrows(): 
    if idx < counter: 
        folium.Marker(location = [data['lat'], data['long']], 
              popup='size - {}'.format(data['sqft_above'])).add_to(m_cluster)
    else:
        break


m.save('map.html')
webbrowser.open_new_tab('map.html')















