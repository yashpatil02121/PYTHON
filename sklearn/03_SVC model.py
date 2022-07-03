import pandas as pd
df= pd.read_csv("Seed_Data.csv")
print(df.describe)
df.info()

X = df.iloc[:,0:7]
X.info()

y = df.iloc[:,7]
print(y.describe)

import sklearn
from sklearn import svm
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=0.2,random_state=13)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit(X_test)
clf = svm.SVC()
clf.fit(X_train,y_train)

pred = clf.predict(X_test)
print(pred)
sklearn.metrics.accuracy_score(y_test,pred)
print(sklearn.metrics.classification_report(y_test,pred))