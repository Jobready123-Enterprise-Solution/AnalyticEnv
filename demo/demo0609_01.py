# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3], [-1.2, 7.8, -6.1], [3.9, 0.4, 2.1], [7.3, -9.9, -4.5]])
print(input_data)
# =============================================================================
# print(type(input_data))
# print(input_data.shape)
# =============================================================================


bz = preprocessing.Binarizer(threshold = 2)
sc = preprocessing.scale(input_data, axis=1)
b_data = bz.transform(input_data)
print(b_data)

print (input_data.mean(axis = 1))
print (sc.mean(axis = 1))

c_list = ['Toronto', 'Paris', 'Montreal']

le = preprocessing.LabelEncoder()
le.fit(c_list)

e_clist=[]
for c in c_list:
    print(c, le.transform([c,]))
    e_clist.append(le.transform([c,])  )         
print(e_clist)   
    
    
# =============================================================================
# e_clist = le.transform([c_list,])
# print(e_clist.shape)
# ohe = preprocessing.OneHotEncoder()
# ohe.fit(e_clist)
# print(e_clist)
# print(ohe.transform(e_clist).toarray())
# =============================================================================
