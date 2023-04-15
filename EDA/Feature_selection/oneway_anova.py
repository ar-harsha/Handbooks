# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 05:56:12 2023

@author: harsh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

data =  pd.read_csv("ANSUR II MALE Public.csv",nrows=1000)

numeric = ['int16','int32','int64','float16','float32','float64']
data = data.select_dtypes(include=numeric)

#dependent and indepenedent adata 
x = data.drop(columns="Weightlbs",axis=1)
y = data.loc[:,"Weightlbs"]

#split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=24)

#preprocessing scaling data
scaler = StandardScaler()
scaled_train = scaler.fit_transform(x_train)
scaled_test = scaler.fit_transform(x_test)

rf_model = RandomForestRegressor(random_state=24)
rf_model.fit(scaled_train,y_train)

print("f-score: {0}".format(rf_model.score(scaled_test,y_test)))


#one way for feature selection
selector = SelectKBest(f_classif,k=15)
selector.fit(scaled_train,y_train)

cols = selector.get_support(indices=True)

x_train_selected = selector.transform(scaled_train)
print("x_train shape is ",scaled_train.shape)
print("x_train_selected sape is ",x_train_selected.shape)

x_test_selected = selector.transform(scaled_test)

rf_model = RandomForestRegressor(random_state=24)
rf_model.fit(x_train_selected,y_train)

print("rf model score is ",rf_model.score(x_test_selected, y_test))