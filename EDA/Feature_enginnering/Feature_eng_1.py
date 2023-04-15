# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:05:38 2023

@author: harsh
"""

import numpy as np
import pandas as pd

df = pd.read_csv("train.csv")

missing_categoraical_columns= [column for column in df.columns if df[column].nunique() < 10 and df[column].isnull().mean()>0]

print(df[missing_categoraical_columns].isnull().sum())
print(df[missing_categoraical_columns].isnull().mean())

#plotting value counts
# df[missing_categoraical_columns[0]].value_counts().plot(kind='bar')

#drop cols with more tahn 80% null values
cols_to_be_dropped = [col for col in missing_categoraical_columns if df[col].isnull().mean()>=0.8]

df.drop(columns=cols_to_be_dropped,inplace=True)

#missing categorical cols after dropping
missing_categoraical_columns= [column for column in df.columns if df[column].nunique() < 10 and df[column].isnull().mean()>0]

#all missing values are now filled with mode
for col in missing_categoraical_columns:
    df[col].fillna(value=df[col].mode()[0],inplace=True)
    
