# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:21:08 2020

@author: Vaish
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")

X = dataset.iloc[:,1:2].values
y = dataset.iloc[:, 2].values

#Linear Regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

#Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

#Visualizing Linear Model
plt.figure('Linear Regression', clear = True)
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title("Truth or Bluff (Linear Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Visualizing Polynomial Regression Model
plt.figure('Polynomial Regression', clear = True)
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Visualizing Higher Resolution and Smooth Curve for Polynomial regression Model
plt.figure('For higher resolution and smooth curve', clear = True)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.xlabel('Position Level')
plt.ylabel('Salary')

#Predicting a new result with Linear Regression
lin_reg.predict([[6.5]]) 

#Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))







