import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv("titanic.csv",usecols=["Pclass","Age","Fare","Survived"])
# print(df.isnull().sum()) #age has null so fill those

df["Age"] = df["Age"].fillna(df["Age"].median())
y = df["Survived"]
x = df[["Pclass","Age","Fare"]]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=24)
scaler = StandardScaler() #transform model object
# scaler.fit(x_train) 
# scaler.transform(x_train) #bascically a z transform
#above both can be done in one step
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

#create a logistic regression object
lr_model = LogisticRegression()
lr_model.fit(x_train,y_train) #train or best fit

preds = lr_model.predict(x_test)
print(accuracy_score(y_test, preds))
print(9.93/2.25)