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
import numpy as np
df = pd.read_csv('../MapData/kc_house_data.csv', parse_dates=['date'])
df['zipcode'] = df['zipcode'].astype(str)

# =============================================================================
# print(df.shape)
#print(df.dtypes)
# print(df.columns)
# print(df['lat'].describe())
# =============================================================================


m = folium.Map([df['lat'].mean(), df['long'].mean()], zoom_start=10)

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

#hm = plugins.HeatMap( [ data['lat'] ,  data['long'] ]    for idx, data in df.iterrows())

#hm.add_to(m)


df['count'] = 1
df_zip_count = df[['zipcode', 'count']].groupby('zipcode').aggregate(np.sum)
df_zip_count.reset_index(inplace=True)

df_zip_price = df[['zipcode', 'price']].groupby('zipcode').aggregate(np.mean)
df_zip_price.reset_index(inplace=True)


# =============================================================================
# print(df_zip_count.head)
# print(df_zip_count.columns)
# print(df_zip_count.dtypes)
# 
# =============================================================================


df_zipcode = pd.merge(df_zip_count, df_zip_price, how='left', on=['zipcode'])


def draw_heatmap(df, column_name):
    folium.Choropleth(
        geo_data=open('../MapData/zipcode_king_city.geojson').read(),
        name='choropleth',
        data=df,
        columns=['zipcode', column_name],
        key_on='feature.properties.ZCTA5CE10',
        fill_color='OrRd', #'YlGn',
        fill_opacity=0.7,
        line_opacity=0.9,
        legend_name='# of houses per zip code'
    ).add_to(m)
    
    
    
    m.save('map_{}.html'.format(column_name))
    webbrowser.open_new_tab('map_{}.html'.format(column_name))

for name in ['count', 'price']:
    draw_heatmap(df_zipcode, name)













