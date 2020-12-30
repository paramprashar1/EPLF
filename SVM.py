
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import math
from sklearn import metrics
from sklearn.svm import SVR

from sklearn.metrics import r2_score
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import max_error
from sklearn.metrics import explained_variance_score


params = {
    'n_estimators': 800,
    'max_depth': 4,
    'learning_rate': 0.001,
    'criterion': 'mse'
}

dataset = pd.read_csv('C:/Users/Param Prashar/Desktop/Capstone Final Files/Old/FakeData.csv')
print("Success")

# dataset = transform_dataset(dataset)
Xfeatures = ['No','Temp','Ex']
X = dataset[Xfeatures]
y = dataset['Load']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
y_train = np.log10(y_train)
y_test = np.log10(y_test)
regressor = SVR(kernel='rbf')
regressor.fit(X_train, y_train)

training_accuracy = regressor.score(X_train, y_train)
test_accuracy = regressor.score(X_test, y_test)
rmse_train = np.sqrt(mean_squared_error(regressor.predict(X_train),y_train))
rmse_test = np.sqrt(mean_squared_error(regressor.predict(X_test),y_test))
print("Training Accuracy = %0.3f, Test Accuracy = %0.3f, RMSE (train) = %0.3f, RMSE (test) = %0.3f" % (training_accuracy, test_accuracy, rmse_train, rmse_test))

y_true=y_test
y_pred=regressor.predict(X_test)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
plt.title('Support Vector Machine')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

print("SVM")
print("exp variance err",explained_variance_score(y_true, y_pred))
print("max error",max_error(y_true, y_pred))
print("mae",mean_absolute_error(y_true, y_pred))
print("mse",mean_squared_error(y_true, y_pred))
print("mean sq log error",mean_squared_log_error(y_true, y_pred))
print("median absolute error",median_absolute_error(y_true, y_pred))
print("r2",r2_score(y_true, y_pred))
print("Success!")

y_predB=regressor.predict(X)
Xnew2=[[44,23,1]]
predc=10**regressor.predict(Xnew2)
print(predc)

X1=dataset['No']
X2=dataset['Load']
plt.plot(X1,X2)
plt.plot(X1,10**y_predB)
plt.show()
