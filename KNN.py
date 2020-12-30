import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import math
# from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import max_error
from sklearn.metrics import explained_variance_score
import matplotlib.pyplot as plt
# dataset = transform_dataset(dataset)
dataset = pd.read_csv('C:/Users/Param Prashar/Desktop/Capstone Final Files/Old/FakeData.csv')
print("Success")

# dataset = transform_dataset(dataset)
Xfeatures = ['No','Temp','Ex']
X = dataset[Xfeatures]
y = dataset['Load']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
y_train = np.log10(y_train)
y_test = np.log10(y_test)
reg = KNeighborsRegressor(n_neighbors = 5, algorithm = 'auto')
reg.fit(X_train,y_train)

training_accuracy = reg.score(X_train, y_train)
test_accuracy = reg.score(X_test, y_test)
rmse_train = np.sqrt(mean_squared_error(reg.predict(X_train),y_train))
rmse_test = np.sqrt(mean_squared_error(reg.predict(X_test),y_test))
print("Training Accuracy = %0.3f, Test Accuracy = %0.3f, RMSE (train) = %0.3f, RMSE (test) = %0.3f" % (training_accuracy, test_accuracy, rmse_train, rmse_test))

# Xnew = [[85,14,31,20000,0]]
Xnew2=[[44,23,1]]
predc=10**reg.predict(Xnew2)
print(predc)

# y_true=y_test
# y_pred=reg.predict(X_test)
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# ax.scatter(y_test, y_pred)
# plt.title('K Nearest Neighbor')
# plt.xlabel('Actual')
# plt.ylabel('Predicted')
# # plt.show()
# print("KNN")
# print("exp variance err",explained_variance_score(y_true, y_pred))
# print("max error",max_error(y_true, y_pred))
# print("mae",mean_absolute_error(y_true, y_pred))
# print("mse",mean_squared_error(y_true, y_pred))
# print("mean sq log error",mean_squared_log_error(y_true, y_pred))
# print("median absolute error",median_absolute_error(y_true, y_pred))
# print("r2",r2_score(y_true, y_pred))
# print("Success!")
#
# y_predB=reg.predict(X)
#
# X1=dataset['No']
# X2=dataset['Load']
# plt.plot(X1,X2)
# plt.plot(X1,10**y_predB)
# plt.show()
