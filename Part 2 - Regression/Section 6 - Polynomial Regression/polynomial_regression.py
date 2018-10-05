#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:48:00 2018

@author: abdulsamad
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn.preprocessing import Imputer

dataset = pd.read_csv('Position_Salaries.csv')

#1:2 because we want to have features as matrix
# and no need for 0 index column because its already encoded in the 1st column
features = dataset.iloc[:, 1:2].values
result = dataset.iloc[:,(np.shape(dataset)[1] - 1)].values


# Steps 
#   1. Create new LinearRegression Model to fit x and y   
#   2. Convert x to x_poly matrix by adding polynomial columns
#   3. Create a new LinearRegression Model to fit x_poly with y     


from sklearn.linear_model import LinearRegression
lin_reg  = LinearRegression()
lin_reg.fit(features, result)

plt.scatter(features,result, c = 'red')
plt.plot(features, lin_reg.predict(features), c = 'blue', label = 'simple linear regression')


from sklearn.preprocessing import PolynomialFeatures

poly_f = PolynomialFeatures(degree = 4)
features_poly = poly_f.fit_transform(features)

lin_reg_poly  = LinearRegression()
lin_reg_poly.fit(features_poly, result)
plt.plot(features, lin_reg_poly.predict(features_poly), c = 'green', label = 'polynomial linear regression')
plt.xlabel('Level')
plt.ylabel('Yearly Salary')
plt.title('Level vs Salary ')
plt.legend()


#prediction  for 6.5 level with Linear regression model
linear_reg_prediction = lin_reg.predict(6.5)
#prediction  for 6.5 level with polynomial Linear regression model
polynomial_linear_reg_predictionlin_reg_poly.predict(poly_f.fit_transform(6.5))

