import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_selection import SelectKBest,chi2
from sklearn.ensemble import ExtraTreesClassifier


df = pd.read_csv("mobile.csv")

x = df.iloc[:,0:20] # independent
y = df.iloc[:,-1]  #target


#univariate selection --------------start
bestfeatures = SelectKBest(score_func=chi2,k=10)
fit = bestfeatures.fit(x,y)

feature_scores = pd.concat([pd.DataFrame(x.columns),pd.DataFrame(fit.scores_)],axis=1)
feature_scores.columns = ["feature","score"]
feature_scores.sort_values(by="score",ascending=False,inplace=True)
print(feature_scores.nlargest(10,"score"))  #top 10 imp features

#univariate selection --------------end

#feature importance ---------start
model = ExtraTreesClassifier()
model.fit(x,y)
plt.figure()
plt.barh(x.columns,model.feature_importances_)
plt.title("feature importance")
# plt.show()
#feature importance ---------end


#correlation     ---------start
correlation_matrix = df.corr()
plt.figure()
sns.heatmap(correlation_matrix,center=0,annot=True)
plt.show()
#correlation     ---------end