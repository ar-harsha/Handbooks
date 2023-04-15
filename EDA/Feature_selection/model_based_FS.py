# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 05:14:11 2023

@author: harsh
"""

import pandas as pd
import numpy as np

from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

data = pd.read_csv("ANSUR II MALE Public.csv",nrows = 1000)

numeric = ['int16','int32','int64','float16','float32','float64']
data = data.select_dtypes(include=numeric)

x = data.drop(columns="Weightlbs",axis=1)
y = data.loc[:,"Weightlbs"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=24)

scaler = StandardScaler()
scaled_train = scaler.fit_transform(x_train)
scaled_test = scaler.transform(x_test)

rf_model = RandomForestRegressor(random_state=24)
rf_model.fit(scaled_train,y_train)

print("f-score for this is {0}",rf_model.score(scaled_test, y_test))

select = SelectFromModel(RandomForestRegressor(random_state=24),threshold="mean")
select.fit(scaled_train,y_train)
x_train_selected = select.transform(scaled_train)
x_test_selected = select.transform(scaled_test)

rf_model = RandomForestRegressor(random_state=24)
rf_model.fit(x_train_selected,y_train)

print("f-score after selcetion is {0} "" {1}".format(rf_model.score(x_test_selected,y_test),"haha"))
