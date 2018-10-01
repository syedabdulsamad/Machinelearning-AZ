#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:07:10 2018

@author: abdulsamad
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('50_Startups.csv')
features = dataset.iloc[:, :-1].values
result = dataset.iloc[:,4].values


# Categorical data encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder = LabelEncoder()
features[:,3] = labelEncoder.fit_transform(features[:,3])
hotEncoder = OneHotEncoder(categorical_features = [3])
features = hotEncoder.fit_transform(features).toarray()
lastColumn = np.shape(features)[1]
features = features[:, 1:lastColumn]




# training and test sample data
from sklearn.model_selection import train_test_split
feature_train, feature_test, result_train, result_test = train_test_split(features, result, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, result)
predicions = regressor.predict(feature_test)

import statsmodels.formula.api as sm
s = (np.shape(features)[0], 1)


features = np.append(arr = np.ones(s, dtype = int), values = features, axis = 1)
features_OPT = features[:, [0, 1, 2, 3, 4, 5]]

def automatic_backward_elimination(feature_matrix, index_to_remove = -1):
    if index_to_remove >= 0:
        # remove the index and create new features matrix
        feature_matrix = np.delete(feature_matrix, (index_to_remove), axis = 1)
        
    regressor_OLS = sm.OLS(result, exog = feature_matrix).fit()
    max_pValue = max(regressor_OLS.pvalues)
    if max_pValue > 0.05:
       index = np.argmax(regressor_OLS.pvalues)
       automatic_backward_elimination(feature_matrix, index)
    
            
automatic_backward_elimination(features_OPT)




# feature scaling
"""from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
feature_train =  scaler.fit_transform(feature_train)
feature_test =  scaler.transform(feature_test)"""
