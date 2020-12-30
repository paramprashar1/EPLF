
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math
from sklearn.externals import joblib
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import max_error
from sklearn.metrics import explained_variance_score
dataset = pd.read_csv('FakeData.csv')
dataset.plot(x='No', y='Load', style='o')  

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['Load'])
#plt.show()
Xfeatures = ['No']
X = dataset[Xfeatures]
y = dataset['Load']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
y_train = np.log10(y_train)
y_test = np.log10(y_test)

reg = LinearRegression()  
reg.fit(X_train, y_train)
training_accuracy = reg.score(X_train, y_train)
test_accuracy = reg.score(X_test, y_test)
rmse_train = np.sqrt(mean_squared_error(reg.predict(X_train),y_train))
rmse_test = np.sqrt(mean_squared_error(reg.predict(X_test),y_test))
print("Training Accuracy = %0.3f, Test Accuracy = %0.3f, RMSE (train) = %0.3f, RMSE (test) = %0.3f" % (training_accuracy, test_accuracy, rmse_train, rmse_test))
y_true=y_test
y_pred=reg.predict(X_test)
print("Linear Regression")
print("exp variance err",explained_variance_score(y_true, y_pred))
print("max error",max_error(y_true, y_pred))
print("mae",mean_absolute_error(y_true, y_pred))
print("mse",mean_squared_error(y_true, y_pred))
print("mean sq log error",mean_squared_log_error(y_true, y_pred))
print("median absolute error",median_absolute_error(y_true, y_pred))
print("r2",r2_score(y_true, y_pred))
print("Success!")