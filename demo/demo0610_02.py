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
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../MapData/kc_house_data.csv', parse_dates=['date'])
df['zipcode'] = df['zipcode'].astype(str)
df['view'] = df['view'].astype('category')
df['waterfront'] = df['waterfront'].astype('category')
df['condition'] = df['condition'].astype('category')
df['grade'] = df['grade'].astype('category')
print(df.dtypes)
print(df.columns)

fig, axList = plt.subplots(nrows=2, ncols=1)
sns.distplot(df['price'], ax=axList[0])
sns.boxplot(df['price'], ax=axList[1])

#sns.jointplot(x=df['sqft_lot'], y=df['price'])
#sns.regplot(x=df['sqft_lot'], y=df['price'])
#sns.relplot(x='sqft_lot', y='price', data = df)
#sns.catplot(x="view", y="price", kind="box", data=df);
#sns.catplot(x="view", kind="count", data=df);

#sns.catplot(x='price', y='view', row='condition', kind='box', data=df)

#df = df[['price', 'sqft_living', 'sqft_lot']]
#sns.pairplot(df)
# =============================================================================
# df['count'] = 1
# df_zip_count = df[['zipcode', 'count']].groupby('zipcode').aggregate(np.sum)
# df_zip_count.reset_index(inplace=True)
# 
# df_zip_price = df[['zipcode', 'price']].groupby('zipcode').aggregate(np.mean)
# df_zip_price.reset_index(inplace=True)
# =============================================================================


# =============================================================================
# print(df_zip_count.head)
# print(df_zip_count.columns)
# print(df_zip_count.dtypes)
# 
# =============================================================================


#df_zipcode = pd.merge(df_zip_count, df_zip_price, how='left', on=['zipcode'])















