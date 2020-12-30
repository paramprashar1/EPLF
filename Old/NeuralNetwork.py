
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math
from sklearn.externals import joblib
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.neural_network import MLPRegressor
dataset = pd.read_csv('FakeData.csv')
print("Success!")
# dataset = transform_dataset(dataset)
Xfeatures = ['No','Temp','Buildings','Students','Ex']
X = dataset[Xfeatures]
y = dataset['Load']
print(dataset.corr().round(decimals=3))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
y_train = np.log10(y_train)
y_test = np.log10(y_test)
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)





#mlp = MLPRegressor(hidden_layer_sizes=(500))
#mlp.fit(X_train,y_train)
#MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
#       beta_2=0.999, early_stopping=False, epsilon=1e-08,
#       hidden_layer_sizes=(30, 30, 30), learning_rate='constant',
#       learning_rate_init=0.001, max_iter=200, momentum=0.9,
#       nesterovs_momentum=True, power_t=0.5, random_state=None,
#       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
#       verbose=False, warm_start=False)
#predictions = mlp.predict(X_test)

##print(confusion_matrix(y_test,predictions))
##print(classification_report(y_test,predictions))
##len(mlp.coefs_)
##len(mlp.coefs_[0])
##len(mlp.intercepts_[0])

#mse=0.06
#hidden_layer_sizes = [(100,),(500,),(100,10,),(100,100,)]
#alpha = [0.0001, 0.00001, 0.001]
#learning_rate = [0.0001, 0.001, 0.01]
#max_iter = [200, 1000, 10000]
#grid_search = pd.DataFrame(columns=['hl','a','lr','mi','mae'])
#for hl in hidden_layer_sizes:
#    for a in alpha:
#        for lr in learning_rate:
#            for mi in max_iter:
#                mae = mse
#                params = {'hl':hl, 'a':a, 'lr':lr, 'mi':mi, 'mae':mae}
#                grid_search = grid_search.append(params, ignore_index=True)

#print(grid_search.sort_values('mae').head(1))

#     hl       a      lr   mi   mae
#0  (100,)  0.0001  0.0001  200  0.06

hl, a, lr, mi = (3), 5, 0.001, 1

mod_mlp = MLPRegressor(hidden_layer_sizes=hl, alpha=a, learning_rate_init=lr, max_iter=mi)
mod_mlp.fit(X_train,y_train)
predictions = mod_mlp.predict(X_test)

training_accuracy = mod_mlp.score(X_train, y_train)
test_accuracy = mod_mlp.score(X_test, y_test)
rmse_train = np.sqrt(mean_squared_error(mod_mlp.predict(X_train),y_train))
rmse_test = np.sqrt(mean_squared_error(mod_mlp.predict(X_test),y_test))
print("Training Accuracy = %0.3f, Test Accuracy = %0.3f, RMSE (train) = %0.3f, RMSE (test) = %0.3f" % (training_accuracy, test_accuracy, rmse_train, rmse_test))
