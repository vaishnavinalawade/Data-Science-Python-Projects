# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:03:39 2020

@author: Vaish
"""

#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300,random_state=0)

regressor.fit(X,y)

y_pred = regressor.predict([[6.5]])

#Visualizing the Randon Forest Regression
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Truth or Bluff(Random Forest Regressor)")
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()