#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:16:22 2020

@author: qtangzhu
"""
import numpy as np

import seaborn as sns
import pandas as pd
import folium
import folium.plugins as plugins
import webbrowser

df = pd.read_csv('../MapData/kc_house_data.csv', parse_dates=['date'])

# =============================================================================
# print(df.shape)
#print(df.dtypes)
# print(df.columns)
# print(df['lat'].describe())
# =============================================================================


m = folium.Map([df['lat'].mean(), df['long'].mean()], zoom_start=12)

# =============================================================================
# fmarker = folium.Marker(location = [df['lat'].mean(), df['long'].mean()], 
#               popup='Centre Point', 
#               icon=folium.Icon(color='red',icon='info-sign'))
# fmarker.add_to(m)
# 
# m_cluster= plugins.MarkerCluster().add_to(m)
# 
# 
# counter = 1000
# for idx, data in df.iterrows(): 
#     if idx < counter: 
#         folium.Marker(location = [data['lat'], data['long']], 
#               popup='size - {}'.format(data['sqft_above'])).add_to(m_cluster)
#     else:
#         break
# =============================================================================

#hm = plugins.HeatMap( [data['lat'], data['long']] for idx, data in df.iterrows())
#hm.add_to(m)
df['zipcode']=df['zipcode'].astype(str)
df['count'] = 1
zip_agg = df.groupby('zipcode').aggregate([np.mean, np.sum])
zip_agg.reset_index(inplace=True)
df_zip_count = zip_agg['zipcode'].to_frame()
print(df_zip_count.shape)
df_zip_count['count']=zip_agg['count']['sum'].to_frame()
#df_zip_count['count']=df_zip_count_2
#print(df_zip_count_2.columns)
#df_zip_count.reset_index(inplace=True)
print(df_zip_count)

#zipcode_data = pd.merge(df, df_zip_count, how='left', on=['zipcode'])
geo_path = '../MapData/zipcode_king_city.json'
#   zipcode = folium.Map(location=[data['lat'].mean(), data['long'].mean()], zoom_start=9)
#m.choropleth(geo_data= open(geo_path).read(),
#                         data=df_zip_count, 
#                         columns = ['zipcode', 'count'], key_on = 'feature.properties.ZCTA5CE10',
#                         fill_color='OrRd', fill_opacity=0.9,line_opacity=0.2)


folium.Choropleth(
    geo_data=open(geo_path).read(),
    name='choropleth',
    data=df_zip_count,
    columns = ['zipcode', 'count'], 
    key_on = 'feature.properties.ZCTA5CE10',
    fill_color='OrRd',
    fill_opacity=0.9,
    line_opacity=0.9,
    reset=True,
    legend_name='Unemployment Rate (%)'
).add_to(m)


folium.LayerControl().add_to(m)
m.save('map.html')
webbrowser.open_new_tab('map.html')














