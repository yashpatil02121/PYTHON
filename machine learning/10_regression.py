import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model

diabetes=datasets.load_diabetes()

diabetes_x=diabetes.data [:,np.newaxis, 2]

diabetes_x_train=diabetes_x[:-30]
diabetes_x_test=diabetes_x[:-30]

diabetes_y_train=diabetes.target[:-30]
diabetes_y_test=diabetes.target[-30:]

model= linear_model.LinearRegression()

model.fit(diabetes_x_train,diabetes_x_train )

model.predict(diabetes_x_train,diabetes_x_train )

# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
# print(diabetes.keys())
# print(diabetes.DESCR)
