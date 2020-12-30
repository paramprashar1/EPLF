
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
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


params = {
    'n_estimators': 800,
    'max_depth': 4,
    'learning_rate': 0.001,
    'criterion': 'mse'
}

dataset = pd.read_csv('FakeData.csv')
print("Success!")
# dataset = transform_dataset(dataset)
Xfeatures = ['No','Temp','Buildings','Students','Ex']
X = dataset[Xfeatures]
y = dataset['Load']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
y_train = np.log10(y_train)
y_test = np.log10(y_test)

gradient_boosting_regressor = ensemble.GradientBoostingRegressor(**params)

gradient_boosting_regressor.fit(X_train, y_train)
training_accuracy = gradient_boosting_regressor.score(X_train, y_train)
test_accuracy = gradient_boosting_regressor.score(X_test, y_test)
rmse_train = np.sqrt(mean_squared_error(gradient_boosting_regressor.predict(X_train),y_train))
rmse_test = np.sqrt(mean_squared_error(gradient_boosting_regressor.predict(X_test),y_test))
print("Training Accuracy = %0.3f, Test Accuracy = %0.3f, RMSE (train) = %0.3f, RMSE (test) = %0.3f" % (training_accuracy, test_accuracy, rmse_train, rmse_test))

y_true=y_test
y_pred=gradient_boosting_regressor.predict(X_test)
print("Grad Boost")
print("exp variance err",explained_variance_score(y_true, y_pred))
print("max error",max_error(y_true, y_pred))
print("mae",mean_absolute_error(y_true, y_pred))
print("mse",mean_squared_error(y_true, y_pred))
print("mean sq log error",mean_squared_log_error(y_true, y_pred))
print("median absolute error",median_absolute_error(y_true, y_pred))
print("r2",r2_score(y_true, y_pred))
print("Success!")


