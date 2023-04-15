import pandas as pd
import numpy as numpy


df=pd.read_csv("data.csv")
df.isnull().sum()
#drop rows which has missing values
df.dropna(how="any").shape #all drops rows where all values are missing
#only rows dropeed where na is found inthe subset selected
print(df.dropna(how="all",subset=["PoolQC","Fence"]).shape)
print(df.dropna(thresh=2).shape)

#cols dropping using variance threshold
df = pd.read_csv("train.csv",nrows=10000)
x = df.drop(labels=['TARGET'],axis=1)  #independent data
y = df["TARGET"] #dependent data

from sklearn.feature_selection import VarianceThreshold

vart = VarianceThreshold(threshold=0) #model
vart.fit(x)
print(sum(vart.get_support())) #are required columns
total_const_features = x.shape[1] - sum(vart.get_support())
cosnt_columns = x.columns[~vart.get_support()]  
print(x.drop(columns=cosnt_columns,axis=1)) #from 371 85 colukmns are absolete so dropped
