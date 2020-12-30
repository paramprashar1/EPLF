import matplotlib.pyplot as plt

X=["ARIMA","KNN","MLP","RFOREST","GRADBOOST","LINREG"]
Y=[0.098,0.054,0.055,0.019,0.044,0.117]
Y_B=[0.092,0.075,0.085,0.076,0.044,0.117]
plt.plot(X,Y)
plt.title("CAPSTONE Comparison of RMSE")
plt.xlabel("Algorithm")
plt.ylabel("Accuracy")
plt.show()