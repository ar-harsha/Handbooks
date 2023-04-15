# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 04:19:51 2023

@author: harsh
"""

import pandas as pd
import numpy as np

from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

data = pd.read_csv("D:/python/INEURON/ML/Feature_selection/ANSUR II MALE Public.csv",nrows=1000)

numeric = ['int16','int32','int64','float16','float32','float64']
data = data.select_dtypes(include=numeric)

#independent and dependent datas
x = data.drop(columns="Weightlbs",axis=1)
y = data.loc[:,"Weightlbs"]

#split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=24)

#preprocessing scaling data
scaler = StandardScaler()
scaled_train = scaler.fit_transform(x_train)
scaled_test = scaler.transform(x_test)    

rf_model = RandomForestRegressor(random_state=24)
rf_model.fit(scaled_train,y_train)

print("f-score: {0}".format(rf_model.score(scaled_test,y_test)))

result = pd.DataFrame(zip(x_train.columns,abs(rf_model.feature_importances_)),columns = ["feature","importance"]).sort_values("importance").reset_index(drop=True)
print(result)

rfe =  RFE(estimator=RandomForestRegressor(random_state=24),n_features_to_select=10)
rfe.fit(scaled_train,y_train)

# print(rfe.support_) #gives a bool of which columns to consider

selected_train = rfe.transform(scaled_train)
selected_test = rfe.transform(scaled_test)

rf_model = RandomForestRegressor(random_state=24)
rf_model.fit(scaled_train,y_train)

print("f-score: {0}".format(rf_model.score(scaled_test,y_test)))


