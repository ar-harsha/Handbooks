# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:27:50 2023

@author: harsh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("weight-height.csv",usecols=["Gender","Height"])

#check histogram
# plt.hist(df["Height"],bins=20,rwidth=0.8)
# plt.xlabel("heihgt ")
# plt.ylabel("count")

#outlier removal > 3*std
std = df.Height.std()
mean = df.Height.mean()

upper_limit = mean + (3*std)
lower_limit = mean - (3*std)

# print(df[(df["Height"]<=lower_limit) & (df["Height"] >= upper_limit)])

#outlier removel using z-score
def z_score(df,col):
    x = df[col].values
    mean = df[col].mean()
    std = df[col].std()
    return (x-mean)/std

df["zscore"] = z_score(df, "Height")

mask = (df["zscore"]<-3) | (df["zscore"]>3)
# print(df[mask])
mask = (df["zscore"]>=-3) & (df["zscore"]<=3)
# print(df[mask])

lower_limit = 0.05
upper_limit = .95

result = df.Height.quantile([lower_limit,upper_limit])
outliers_mask = (df.Height < result.loc[lower_limit]) | (df.Height > result.loc[upper_limit])
# print(df[outliers_mask])
outliers_mask = (df.Height >= result.loc[lower_limit]) & (df.Height <= result.loc[upper_limit])
print(df[outliers_mask])