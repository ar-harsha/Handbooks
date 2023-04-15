# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:15:29 2023

@author: harsh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

#one hot encoding
# print(pd.get_dummies(df,columns = ["sex","smoker"]))

#label encoding

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
# print(le.fit_transform(df["sex"]))

print(le.fit_transform(df.day))
print(le.classes_)
print(le.inverse_transform(le.fit_transform(df.day)))