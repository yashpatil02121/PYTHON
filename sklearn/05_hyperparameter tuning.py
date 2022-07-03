import sklearn 
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=30)
clf=RandomForestClassifier(n_estimators=2, min_samples_split=3,min_samples_leaf=2)
clf.fit(X_train,y_train)
pred = clf.predict(X_test)
print(sklearn.metrics.accuracy_score(y_test,pred))
# print(pred)

from sklearn.model_selection import GridSearchCV
param_grid = {'n_estimators':[2,5,10,20],'min_samples_split':[2,3],'min_sample_leaf':[1,2,3]}
grid_search=GridSearchCV(estimator=clf,param_grid=param_grid)
grid_search.fit(X_train,y_train)
grid_search.best_params_

clf=RandomForestClassifier(n_estimators=5,min_samples_leaf=1,min_samples_split=2)
clf.fit(X_train,y_train)
pred_clf = clf.predict(X_test)
sklearn.metrics.accuracy_score(y_test,pred_clf)