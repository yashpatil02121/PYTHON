# Train a logistic regression classifier to predict whether a flower is iris virginica or not
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
iris = datasets.load_iris()
# print(list(iris.keys()))
# print(iris['data'].shape)
# print(iris['target'])
# print(iris['DESCR'])

x = iris["data"][:,3:]
y = (iris["target"]==2).astype(np.int)

clf = LogisticRegression()
clf.fit(x,y)
example = clf.predict(([[1.6]]))
print(example)
# print(iris["data"])
# print(x)
# print(y)

# Using matplotlib to plot the visualisation
x_new = np.linspace(0,3,1000).reshape(-1,1)
# print(x_new)
y_prob = clf.predict_proba(x_new)
print(y_prob)
plt.plot(x_new, y_prob[:,1],"g-", label="virginica")
plt.show()



