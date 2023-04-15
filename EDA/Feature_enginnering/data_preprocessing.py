# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:58:47 2023

@author: harsh
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler,MinMaxScaler,Normalizer,Binarizer

df = pd.read_csv("wine.csv",usecols=["fixed acidity","residual sugar"])

#minmax (0-1) x-xmin/(xmax-xmin)
m_scaler = MinMaxScaler()
scaled_data = m_scaler.fit_transform(df.dropna())

#standard scalar (-1,1)

s_scaler = StandardScaler()
scaled_data = s_scaler.fit_transform(df.dropna())

#Normalizer  {l2 norm}
norm = Normalizer()
scaled_data = norm.fit_transform(df.dropna())

#binarizer below threh o and > threhsh is 1
binarizer = Binarizer()
binarizer.fit_transform(df.dropna())